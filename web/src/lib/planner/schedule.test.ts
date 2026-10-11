import { describe, expect, it } from "vitest";
import { buildBlueprint } from "./blueprint";
import { withSummaryUnit } from "./blueprint";
import { apportion, buildAulaCycle, buildSubjectQueue, buildSummaryBlock, type BlockUnit } from "./schedule";
import { mkAula, mkSeg } from "./testkit";
import type { Level } from "./types";

const bp = (n: number, opts: { level?: Level; runs?: [number, number][]; pages?: number; load?: number } = {}) =>
  buildBlueprint(
    mkAula("d/a01", 1, { commentedRuns: opts.runs ?? [] }),
    Array.from({ length: n }, (_, i) => mkSeg("d/a01", i + 1, opts.pages ?? 12, opts.load ?? 12, 1 + i * 12)),
    opts.level ?? 0,
  );

describe("apportion (maiores restos)", () => {
  it("soma sempre o total pedido", () => {
    const cases: [number[], number][] = [[[1, 1, 1], 10], [[5, 3, 2], 7], [[70, 20, 10], 3], [[1], 5], [[0.2, 0.3, 0.5], 9], [[10, 10], 0]];
    for (const [w, t] of cases) expect(apportion(w, t).reduce((a, b) => a + b, 0)).toBe(t);
  });
  it("é proporcional aos pesos", () => {
    expect(apportion([1, 1, 2], 8)).toEqual([2, 2, 4]);
    expect(apportion([5, 3, 2], 10)).toEqual([5, 3, 2]);
  });
  it("garante ao menos 1 a cada peso quando o total comporta", () => {
    const out = apportion([100, 1, 1], 5);
    expect(out.every((n) => n >= 1)).toBe(true);
    expect(out.reduce((a, b) => a + b, 0)).toBe(5);
  });
  it("com total menor que o nº de pesos, alguns ficam com 0 (sem inventar cotas)", () => {
    const out = apportion([1, 1, 1, 1], 2);
    expect(out.reduce((a, b) => a + b, 0)).toBe(2);
    expect(out.filter((n) => n === 0)).toHaveLength(2);
  });
  it("lista vazia; pesos todos zero não geram NaN", () => {
    expect(apportion([], 5)).toEqual([]);
    const z = apportion([0, 0, 0], 6);
    expect(z.reduce((a, b) => a + b, 0)).toBe(6);
    expect(z.every((n) => Number.isFinite(n))).toBe(true);
  });
  it("é determinístico e desempata pelo índice", () => {
    expect(apportion([1, 1, 1], 1)).toEqual([1, 0, 0]);
    expect(apportion([1, 1, 1], 4)).toEqual([2, 1, 1]);
  });
});

describe("buildAulaCycle", () => {
  it("Mínimo: Teorias, Revisão curta (até 4 Teorias), Fixação e caderno, nessa ordem", () => {
    const cyc = buildAulaCycle(bp(6, { runs: [[1, 48]] }), 1);
    expect(cyc.map((a) => a.type)).toEqual(["TEORIA", "TEORIA", "TEORIA", "REVISAO", "TEORIA", "TEORIA", "TEORIA", "REVISAO", "FIXACAO", "QUESTOES", "QUESTOES"]);
  });
  it("toda aula com Teoria fecha o ciclo com Revisão e Questões, até no Mínimo", () => {
    const cyc = buildAulaCycle(bp(3), 1);
    expect(cyc.map((a) => a.type)).toEqual(["TEORIA", "TEORIA", "TEORIA", "REVISAO", "QUESTOES"]);
  });
  it("Completo: cada Revisão vem logo depois do grupo de Teorias que ela revê", () => {
    const cyc = buildAulaCycle(bp(4, { level: 0 }), 2); // grupos de 2
    expect(cyc.map((a) => a.key)).toEqual(["d/a01#T1", "d/a01#T2", "d/a01#R1", "d/a01#T3", "d/a01#T4", "d/a01#R2", "d/a01#Q1", "d/a01#Q2"]);
    const r1 = cyc.find((a) => a.key === "d/a01#R1")!;
    expect(r1.refKeys).toEqual(["d/a01#T1", "d/a01#T2"]);
    expect(r1.segmentIds).toEqual(["d/a01/s01", "d/a01/s02"]);
  });
  it("Fixação vem depois das Revisões e antes dos cadernos, com as faixas de páginas", () => {
    const cyc = buildAulaCycle(bp(4, { runs: [[100, 111]] }), 2);
    const order = cyc.map((a) => a.type);
    expect(order.indexOf("FIXACAO")).toBeGreaterThan(order.lastIndexOf("REVISAO"));
    expect(order.indexOf("QUESTOES")).toBeGreaterThan(order.indexOf("FIXACAO"));
    expect(cyc.find((a) => a.type === "FIXACAO")!.fixRanges).toEqual([{ start: 100, end: 111 }]);
  });
  it("Questões: caderno de 25 questões / 60 min, não misto, atrelado às Teorias do grupo", () => {
    const q = buildAulaCycle(bp(6), 3).filter((a) => a.type === "QUESTOES");
    expect(q.length).toBeGreaterThan(0);
    for (const a of q) {
      expect(a.quiz).toEqual({ questions: 25, limitSeconds: 3600, mixed: false });
      expect(a.refKeys.length).toBeGreaterThan(0);
      expect(a.scope).toBe("AULA");
    }
  });
  it("chaves únicas, todas as Teorias presentes e subjectId vindo do id da aula", () => {
    for (const tier of [1, 2, 3] as const) {
      const cyc = buildAulaCycle(bp(9, { runs: [[1, 120]] }), tier);
      expect(new Set(cyc.map((a) => a.key)).size).toBe(cyc.length);
      expect(cyc.filter((a) => a.type === "TEORIA")).toHaveLength(9);
      for (const a of cyc) expect(a.subjectId).toBe("d");
    }
  });
  it("pré-requisitos: Revisão ≥ 1 dia depois das Teorias; Fixação depois das Revisões; Questões ≥ 1 dia depois da Fixação", () => {
    const cyc = buildAulaCycle(bp(4, { runs: [[1, 24]] }), 2);
    const by = new Map(cyc.map((a) => [a.key, a]));
    for (const r of cyc.filter((a) => a.type === "REVISAO")) {
      expect(r.after.map((d) => d.key).sort()).toEqual([...r.refKeys].sort());
      for (const d of r.after) expect(d.gap).toBeGreaterThanOrEqual(1);
    }
    const fix = cyc.find((a) => a.type === "FIXACAO")!;
    expect(fix.after.map((d) => d.key).sort()).toEqual(cyc.filter((a) => a.type === "REVISAO").map((a) => a.key).sort());
    for (const q of cyc.filter((a) => a.type === "QUESTOES")) {
      expect(q.after.some((d) => d.key === fix.key && d.gap >= 1)).toBe(true);
    }
    // todo pré-requisito existe e aparece antes na fila
    cyc.forEach((a, i) => {
      for (const d of a.after) expect(cyc.findIndex((x) => x.key === d.key), `${a.key} ← ${d.key}`).toBeLessThan(i);
      expect(by.has(a.key)).toBe(true);
    });
  });
  it("sem Fixação, as Questões dependem da última Revisão (≥ 1 dia)", () => {
    const cyc = buildAulaCycle(bp(4), 1);
    const r = cyc.find((a) => a.type === "REVISAO")!;
    const q = cyc.find((a) => a.type === "QUESTOES")!;
    expect(q.after).toContainEqual({ key: r.key, gap: 1 });
  });
});

describe("Modo Turbo: blocos de resumo", () => {
  /** `n` unidades em resumo de uma disciplina, em `aulas` aulas de `per` unidades cada. */
  const units = (aulas: number, per: number, tier: 1 | 2 | 3 = 1): BlockUnit[] =>
    Array.from({ length: aulas }, (_, ai) => {
      const aulaId = `d/a${String(ai + 1).padStart(2, "0")}`;
      let b = buildBlueprint(mkAula(aulaId, ai + 1, { commentedRuns: [[1, 24]] }), Array.from({ length: per }, (_, i) => mkSeg(aulaId, i + 1, 12, 12, 1 + i * 12)), 0);
      for (const u of [...b.teoria]) b = withSummaryUnit(b, u);
      return b.summary.map((unit) => ({ aulaId, unit, bp: b, tier }));
    }).flat();

  it("até 3 unidades por atividade de resumo (~20 min cada), podendo cruzar aulas", () => {
    const cyc = buildSummaryBlock(units(2, 3));
    const s = cyc.filter((a) => a.type === "TEORIA");
    expect(s).toHaveLength(2);
    expect(s.every((a) => a.turbo && a.segmentIds.length <= 3 && a.minutes <= 60)).toBe(true);
    expect(s[0].segmentIds).toEqual(["d/a01/s01", "d/a01/s02", "d/a01/s03"]);
    expect(s[0].minutes).toBe(60);
    const cross = buildSummaryBlock(units(3, 2)).filter((a) => a.type === "TEORIA"); // 6 unidades em aulas de 2
    expect(cross.map((a) => a.segmentIds.length)).toEqual([3, 3]);
    expect(new Set(cross[0].segmentIds.map((id) => id.split("/")[1])).size).toBe(2); // a atividade atravessa duas aulas
  });
  it("ciclo flexibilizado: mínimo = resumos + caderno curto de 15 questões (1 por 6 unidades); sem Revisão nem Fixação", () => {
    const cyc = buildSummaryBlock(units(2, 6));
    expect(cyc.map((a) => a.type)).toEqual(["TEORIA", "TEORIA", "TEORIA", "TEORIA", "QUESTOES", "QUESTOES"]);
    for (const q of cyc.filter((a) => a.type === "QUESTOES")) {
      expect(q.quiz).toEqual({ questions: 15, limitSeconds: 2400, mixed: false });
      expect(q.minutes).toBe(40);
      expect(q.after.some((d) => d.gap >= 1)).toBe(true);
    }
  });
  it("camadas 2 e 3 acrescentam Revisão (metade do tempo) e Fixação reduzida (30 min), antes dos cadernos", () => {
    const cyc = buildSummaryBlock(units(2, 6, 3));
    const order = cyc.map((a) => a.type);
    expect(order).toContain("REVISAO");
    expect(order.indexOf("FIXACAO")).toBeGreaterThan(order.lastIndexOf("REVISAO"));
    expect(order.indexOf("QUESTOES")).toBeGreaterThan(order.indexOf("FIXACAO"));
    for (const r of cyc.filter((a) => a.type === "REVISAO")) expect(r.minutes).toBeLessThanOrEqual(35);
    expect(cyc.find((a) => a.type === "FIXACAO")!.minutes).toBe(30);
    const keys = new Set(cyc.map((a) => a.key));
    expect(keys.size).toBe(cyc.length);
    cyc.forEach((a, i) => {
      for (const d of a.after) expect(cyc.findIndex((x) => x.key === d.key), `${a.key} ← ${d.key}`).toBeLessThan(i);
    });
  });
  it("buildSubjectQueue: aulas só em resumo formam um bloco; uma aula normal no meio fecha o bloco anterior; blocos têm teto de 9 unidades", () => {
    const mk = (aulaId: string, n: number, summary: boolean) => {
      let b = buildBlueprint(mkAula(aulaId, Number(aulaId.slice(-2)), { commentedRuns: [[1, 12]] }), Array.from({ length: n }, (_, i) => mkSeg(aulaId, i + 1, 12, 12, 1 + i * 12)), 0);
      if (summary) for (const u of [...b.teoria]) b = withSummaryUnit(b, u);
      return { bp: b, tier: 1 as const };
    };
    const q = buildSubjectQueue([mk("d/a01", 4, true), mk("d/a02", 4, true), mk("d/a03", 2, false), mk("d/a04", 3, true)]);
    const blockA = q.filter((a) => a.turbo);
    expect(blockA.flatMap((a) => a.segmentIds).filter((id) => id.startsWith("d/a01") || id.startsWith("d/a02"))).toHaveLength(8);
    const firstNormal = q.findIndex((a) => a.aulaId === "d/a03" && a.type === "TEORIA");
    expect(q.slice(0, firstNormal).some((a) => a.type === "QUESTOES")).toBe(true); // o bloco a01+a02 fecha antes da aula normal
    expect(q.filter((a) => a.type === "TEORIA" && !a.turbo)).toHaveLength(2);
    const big = buildSubjectQueue([mk("d/a01", 11, true)]);
    expect(big.filter((a) => a.type === "QUESTOES").length).toBeGreaterThanOrEqual(2);
    expect(new Set(big.filter((a) => a.type === "TEORIA").map((a) => a.cycle)).size).toBe(2); // 9 + 2 unidades
  });
});
