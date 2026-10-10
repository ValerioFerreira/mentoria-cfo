import { describe, expect, it } from "vitest";
import { buildBlueprint } from "./blueprint";
import { apportion, buildAulaCycle, scheduleStreams, type StreamInfo } from "./schedule";
import { mkAct, mkAula, mkSeg } from "./testkit";
import type { Level, PlannedActivity } from "./types";

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
  it("Essencial: só Teorias na ordem e o caderno ao final (sem Revisão nem Fixação)", () => {
    const cyc = buildAulaCycle(bp(6, { runs: [[1, 48]] }), 1);
    expect(cyc.map((a) => a.type)).toEqual(["TEORIA", "TEORIA", "TEORIA", "TEORIA", "TEORIA", "TEORIA", "QUESTOES"]);
    expect(cyc[0].key).toBe("d/a01#T1");
    expect(cyc.at(-1)!.key).toBe("d/a01#Q1");
  });
  it("Essencial de aula curta (menos de 6 Teorias) não tem caderno", () => {
    expect(buildAulaCycle(bp(3), 1).map((a) => a.type)).toEqual(["TEORIA", "TEORIA", "TEORIA"]);
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
  it("toda referência (refKeys) aponta para uma atividade anterior do mesmo ciclo", () => {
    const cyc = buildAulaCycle(bp(8, { runs: [[1, 60]] }), 3);
    const seen = new Set<string>();
    for (const a of cyc) {
      for (const k of a.refKeys) expect(seen.has(k), `${a.key} -> ${k}`).toBe(true);
      seen.add(a.key);
    }
  });
  it("Modo Turbo: consolida as unidades em uma única atividade de resumo cobrindo todos os trechos", () => {
    const cyc = buildAulaCycle({ ...bp(6, { runs: [[1, 48]] }), turbo: true }, 3);
    expect(cyc.every((a) => a.type === "TEORIA" && a.turbo === true)).toBe(true);
    expect(cyc).toHaveLength(1);
    expect(cyc[0].segmentIds).toHaveLength(6);
  });
  it("cada Teoria cobre exatamente os trechos da sua unidade e os minutos seguem o blueprint", () => {
    const b = bp(3, { load: 12 });
    const cyc = buildAulaCycle(b, 1);
    expect(cyc.flatMap((a) => a.segmentIds)).toEqual(["d/a01/s01", "d/a01/s02", "d/a01/s03"]);
    expect(cyc.map((a) => a.minutes)).toEqual([60, 60, 60]);
  });
});

function stream(subjectId: string, mins: number[], examQuestions = 10, sortOrder = 1): StreamInfo {
  return { subjectId, examQuestions, sortOrder, queue: mins.map((m, i) => mkAct(`${subjectId}#${i}`, "TEORIA", subjectId, m)) };
}
const all = (weeks: ReturnType<typeof scheduleStreams>) => weeks.flatMap((w) => w.activities);

describe("scheduleStreams", () => {
  it("agenda todas as atividades quando há semanas suficientes, preservando a ordem dentro de cada disciplina", () => {
    const streams = [stream("a", Array(20).fill(60), 10, 1), stream("b", Array(20).fill(60), 10, 2)];
    const weeks = scheduleStreams(streams, 600, 10, "2026-10-12", 2);
    expect(all(weeks)).toHaveLength(40);
    for (const id of ["a", "b"]) {
      const keys = all(weeks).filter((x) => x.subjectId === id).map((x) => x.key);
      expect(keys).toEqual(Array.from({ length: 20 }, (_, i) => `${id}#${i}`));
    }
  });
  it("cada semana respeita a meta com no máximo 5% de folga e traz índice e data corretos", () => {
    const weeks = scheduleStreams([stream("a", Array(30).fill(45)), stream("b", Array(30).fill(75), 20, 2)], 600, 8, "2026-10-12", 2);
    weeks.forEach((w, i) => {
      expect(w.index).toBe(i + 1);
      expect(w.kind).toBe("CONTENT");
      expect(w.startDate).toBe(new Date(Date.UTC(2026, 9, 12) + i * 7 * 86_400_000).toISOString().slice(0, 10));
      expect(w.targetMinutes).toBe(w.activities.reduce((n, a) => n + a.minutes, 0));
      expect(w.targetMinutes).toBeLessThanOrEqual(600 * 1.05 + 1e-9);
    });
  });
  it("nunca passa de maxWeeks e o excedente simplesmente não é agendado", () => {
    const weeks = scheduleStreams([stream("a", Array(100).fill(60))], 300, 3, "2026-10-12", 1);
    expect(weeks).toHaveLength(3);
    expect(all(weeks).length).toBeLessThan(100);
  });
  it("para quando as filas acabam (não gera semanas vazias)", () => {
    const weeks = scheduleStreams([stream("a", [60, 60])], 600, 10, "2026-10-12", 1);
    expect(weeks).toHaveLength(1);
    expect(weeks[0].activities).toHaveLength(2);
  });
  it("sem filas não há semanas", () => {
    expect(scheduleStreams([], 600, 10, "2026-10-12", 3)).toEqual([]);
    expect(scheduleStreams([stream("a", [])], 600, 10, "2026-10-12", 3)).toEqual([]);
  });
  it("foco: com 3 disciplinas e foco 2, a primeira semana tem no máximo as 2 de maior fração pendente (ou amplia só se faltar conteúdo)", () => {
    const streams = [stream("a", Array(30).fill(60), 30, 1), stream("b", Array(30).fill(60), 20, 2), stream("c", Array(30).fill(60), 10, 3)];
    const [w1] = scheduleStreams(streams, 600, 10, "2026-10-12", 2);
    expect(new Set(w1.activities.map((a) => a.subjectId)).size).toBeLessThanOrEqual(2);
  });
  it("todas as atividades da semana recebem dia 0–6", () => {
    const weeks = scheduleStreams([stream("a", Array(20).fill(60)), stream("b", Array(20).fill(60), 10, 2)], 840, 6, "2026-10-12", 2);
    for (const a of all(weeks)) {
      expect(Number.isInteger(a.day)).toBe(true);
      expect(a.day).toBeGreaterThanOrEqual(0);
      expect(a.day).toBeLessThanOrEqual(6);
    }
  });
  it("primeira semana parcial (começo na quinta): só dias 3–6 e meta proporcional", () => {
    const full = scheduleStreams([stream("a", Array(40).fill(60)), stream("b", Array(40).fill(60), 10, 2)], 840, 4, "2026-10-12", 2, 0);
    const part = scheduleStreams([stream("a", Array(40).fill(60)), stream("b", Array(40).fill(60), 10, 2)], 840, 4, "2026-10-12", 2, 3);
    expect(Math.min(...part[0].activities.map((a) => a.day!))).toBeGreaterThanOrEqual(3);
    expect(part[0].targetMinutes).toBeLessThan(full[0].targetMinutes);
    // a segunda semana volta a ser cheia
    expect(Math.min(...part[1].activities.map((a) => a.day!))).toBe(0);
  });
  it("é determinístico", () => {
    const mk = () => [stream("a", Array(25).fill(50), 12, 1), stream("b", Array(25).fill(70), 18, 2), stream("c", Array(25).fill(35), 5, 3)];
    expect(scheduleStreams(mk(), 700, 12, "2026-10-12", 2)).toEqual(scheduleStreams(mk(), 700, 12, "2026-10-12", 2));
  });
  it("não altera as atividades recebidas além de atribuir o dia (cópias)", () => {
    const s = stream("a", [60, 60]);
    const original = JSON.parse(JSON.stringify(s.queue)) as PlannedActivity[];
    scheduleStreams([s], 600, 3, "2026-10-12", 1);
    expect(s.queue).toEqual(original);
  });
});
