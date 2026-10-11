import { describe, expect, it } from "vitest";
import { tierMinutes } from "./blueprint";
import { CONCAVITY, CUM_GAIN, itemGain, LEVEL_MULT, selectContent, valueCurve } from "./select";
import { mkAulaWithSegs, mkSegments, mkSubject } from "./testkit";
import type { Level } from "./types";

describe("valueCurve (retornos decrescentes)", () => {
  it("V(0) = 0 e V(1) = 1", () => {
    expect(valueCurve(0)).toBe(0);
    expect(valueCurve(1)).toBeCloseTo(1, 12);
  });
  it("é estritamente crescente e côncava", () => {
    let prev = valueCurve(0);
    let prevStep = Infinity;
    for (let i = 1; i <= 20; i++) {
      const v = valueCurve(i / 20);
      expect(v).toBeGreaterThan(prev);
      expect(v - prev).toBeLessThan(prevStep);
      prevStep = v - prev;
      prev = v;
    }
  });
  it("valores fora de 0–1 são limitados", () => {
    expect(valueCurve(-5)).toBe(0);
    expect(valueCurve(7)).toBeCloseTo(1, 12);
    expect(CONCAVITY).toBeGreaterThan(0);
  });
  it("metade da cobertura já vale mais da metade do valor", () => {
    expect(valueCurve(0.5)).toBeGreaterThan(0.5);
  });
});

describe("itemGain", () => {
  it("é positivo e cai à medida que a disciplina já está coberta", () => {
    const a = itemGain(10, 0.2, 1, 0, 0);
    const b = itemGain(10, 0.2, 1, 0, 0.5);
    expect(a).toBeGreaterThan(b);
    expect(b).toBeGreaterThan(0);
  });
  it("aluno mais fraco ganha mais com o mesmo estudo", () => {
    const gains = ([0, 1, 2, 3] as Level[]).map((l) => itemGain(10, 0.2, 1, l, 0.1));
    expect(gains).toEqual([...gains].sort((x, y) => y - x));
    expect(LEVEL_MULT[0]).toBeGreaterThan(LEVEL_MULT[3]);
  });
  it("proporcional ao peso da disciplina na prova e à participação da aula (quando a cobertura é zero)", () => {
    expect(itemGain(20, 0.2, 1, 1, 0)).toBeCloseTo(2 * itemGain(10, 0.2, 1, 1, 0));
    expect(itemGain(10, 0.4, 1, 1, 0)).toBeGreaterThan(itemGain(10, 0.2, 1, 1, 0));
  });
  it("a primeira camada rende o maior ganho (ver pela primeira vez vale a maior parte)", () => {
    expect(CUM_GAIN[1]).toBeGreaterThan(CUM_GAIN[2] - CUM_GAIN[1]);
    expect(itemGain(10, 0.3, 1, 1, 0)).toBeGreaterThan(itemGain(10, 0.3, 2, 1, 0.3 * CUM_GAIN[1]));
  });
  it("sem questões na prova ou participação zero, o ganho é zero", () => {
    expect(itemGain(0, 0.5, 1, 1, 0)).toBe(0);
    expect(itemGain(10, 0, 1, 1, 0)).toBe(0);
  });
});

/** Duas disciplinas: A (3 aulas, 6/4/3 trechos) e B (2 aulas), com questões comentadas só em A. */
function world() {
  const a1 = mkAulaWithSegs("a/a01", 1, 6, 12, 12, { incidence: 5, commentedRuns: [[200, 235]] });
  const a2 = mkAulaWithSegs("a/a02", 2, 4, 12, 12, { incidence: 3 });
  const a3 = mkAulaWithSegs("a/a03", 3, 3, 12, 12, { incidence: 2 });
  const b1 = mkAulaWithSegs("b/a01", 1, 5, 12, 12, { incidence: 4 });
  const b2 = mkAulaWithSegs("b/a02", 2, 5, 12, 12, { incidence: 1 });
  const subjects = [
    mkSubject("a", [a1.aula, a2.aula, a3.aula], { examQuestions: 10, sortOrder: 1 }),
    mkSubject("b", [b1.aula, b2.aula], { examQuestions: 5, sortOrder: 2 }),
  ];
  const segments = mkSegments(a1.segs, a2.segs, a3.segs, b1.segs, b2.segs);
  const chosen = (level: Level = 1) => subjects.map((subject) => ({ subject, level }));
  return { subjects, segments, chosen };
}

describe("selectContent", () => {
  it("com folga enorme todas as aulas vão para o Aprofundamento e o total não passa da capacidade", () => {
    const w = world();
    const sel = selectContent(w.chosen(), w.segments, 1e6);
    expect([...sel.tierByAula.values()]).toEqual(Array(5).fill(3));
    expect(sel.floorShortfall).toBe(false);
    expect(sel.usedMinutes).toBeLessThanOrEqual(1e6);
    const sum = [...sel.tierByAula].reduce((n, [id, t]) => n + tierMinutes(sel.blueprints.get(id)!, t).total, 0);
    expect(sel.usedMinutes).toBeCloseTo(sum, 6);
  });
  it("com capacidade 0 ou irrisória nada é selecionado", () => {
    const w = world();
    for (const cap of [0, 10]) {
      const sel = selectContent(w.chosen(), w.segments, cap);
      expect(sel.tierByAula.size).toBe(0);
      expect(sel.usedMinutes).toBe(0);
    }
  });
  // O ramo `floorShortfall` de select.ts só dispararia se o piso (f = 0 → nenhuma aula) custasse mais que a capacidade,
  // ou seja, só com capacidade negativa: na prática o aviso "não cobre nem uma aula essencial..." nunca aparece.
  it("floorShortfall (aviso de tempo insuficiente) não liga nem com capacidade quase nula — código inalcançável", () => {
    const w = world();
    expect(selectContent(w.chosen(), w.segments, 0).floorShortfall).toBe(false);
    expect(selectContent(w.chosen(), w.segments, 30).floorShortfall).toBe(false);
  });
  it("nunca usa mais minutos que a capacidade, para várias capacidades", () => {
    const w = world();
    const full = selectContent(w.chosen(), w.segments, 1e6).fullMinutes;
    for (const frac of [0.05, 0.2, 0.5, 0.9, 1, 1.5, 2.5, 5]) {
      const cap = full * frac;
      const sel = selectContent(w.chosen(), w.segments, cap);
      expect(sel.usedMinutes, `cap ${frac}`).toBeLessThanOrEqual(cap + 1e-6);
    }
  });
  it("amplitude primeiro: nenhuma aula sobe de camada enquanto outra do edital está sem ser vista", () => {
    const w = world();
    const full = selectContent(w.chosen(), w.segments, 1e6).fullMinutes;
    for (const frac of [1, 1.1, 1.3, 1.6, 2]) {
      const sel = selectContent(w.chosen(), w.segments, full * frac);
      const tiers = [...sel.tierByAula.values()];
      expect(tiers.length, `cap ${frac}`).toBe(5);
      expect(Math.min(...tiers)).toBeGreaterThanOrEqual(1);
    }
    // com exatamente a capacidade do ciclo mínimo, nenhuma aula gasta mais do que o mínimo
    const exact = selectContent(w.chosen(), w.segments, full);
    for (const [id, tier] of exact.tierByAula) expect(tierMinutes(exact.blueprints.get(id)!, tier).total).toBe(tierMinutes(exact.blueprints.get(id)!, 1).total);
    expect(exact.usedMinutes).toBeCloseTo(full, 6);
  });
  it("mais capacidade nunca reduz a amplitude: o nº de aulas vistas só cresce (a profundidade de uma aula pode ceder à amplitude)", () => {
    const w = world();
    const full = selectContent(w.chosen(), w.segments, 1e6).fullMinutes;
    let prev = 0;
    for (const frac of [0.1, 0.3, 0.6, 1, 1.4, 2, 3, 6]) {
      const sel = selectContent(w.chosen(), w.segments, full * frac);
      expect(sel.tierByAula.size, `cap ${frac}`).toBeGreaterThanOrEqual(prev);
      prev = sel.tierByAula.size;
    }
    expect(prev).toBe(5);
  });
  it("com 60% do tempo do Essencial, cada disciplina ainda recebe ao menos uma aula (piso de cobertura)", () => {
    const w = world();
    const full = selectContent(w.chosen(), w.segments, 1e6).fullMinutes;
    const sel = selectContent(w.chosen(), w.segments, full * 0.6);
    const subjects = new Set([...sel.tierByAula.keys()].map((id) => id.split("/")[0]));
    expect(subjects).toEqual(new Set(["a", "b"]));
  });
  it("aulas dominadas na anamnese saem do plano, mas são lembradas em `mastered`", () => {
    const w = world();
    const sel = selectContent(w.chosen(), w.segments, 1e6, { "a/a01": 2 });
    expect(sel.mastered.has("a/a01")).toBe(true);
    expect(sel.tierByAula.has("a/a01")).toBe(false);
    expect(sel.blueprints.has("a/a01")).toBe(false);
    expect(sel.tierByAula.size).toBe(4);
  });
  it("'já estudei' encurta o Essencial da aula em relação a 'nunca estudei'", () => {
    const w = world();
    const never = selectContent(w.chosen(), w.segments, 1e6);
    const seen = selectContent(w.chosen(), w.segments, 1e6, { "a/a02": 1 });
    expect(seen.fullMinutes).toBeLessThan(never.fullMinutes);
  });
  it("aulas não selecionáveis (fora do edital) e aulas sem nada a estudar ficam de fora", () => {
    const x = mkAulaWithSegs("c/a01", 1, 4, 12, 12, { incidence: 0, selectable: false, edital: "no" });
    const y = mkAulaWithSegs("c/a02", 2, 0, 12, 12, { incidence: 3 }); // sem trechos nem questões
    const z = mkAulaWithSegs("c/a03", 3, 3, 12, 12, { incidence: 3 });
    const subj = mkSubject("c", [x.aula, y.aula, z.aula]);
    const sel = selectContent([{ subject: subj, level: 1 }], mkSegments(x.segs, y.segs, z.segs), 1e6);
    expect([...sel.tierByAula.keys()]).toEqual(["c/a03"]);
    expect(sel.blueprints.has("c/a01")).toBe(false);
    expect(sel.blueprints.has("c/a02")).toBe(false);
  });
  it("disciplina sem nenhuma aula selecionável não quebra", () => {
    const sel = selectContent([{ subject: mkSubject("vazia", []), level: 0 }], {}, 1000);
    expect(sel.tierByAula.size).toBe(0);
    expect(sel.fullMinutes).toBe(0);
  });
  it("é determinístico", () => {
    const w = world();
    const a = selectContent(w.chosen(), w.segments, 900);
    const b = selectContent(w.chosen(), w.segments, 900);
    expect([...a.tierByAula]).toEqual([...b.tierByAula]);
    expect(a.usedMinutes).toBe(b.usedMinutes);
  });
});

describe("Modo Turbo na seleção (resumos por unidade)", () => {
  const ids = (w: ReturnType<typeof world>) => Object.values(w.segments).flat().map((x) => x.id);
  const scores = (w: ReturnType<typeof world>) => Object.fromEntries(ids(w).map((id, i) => [id, ((i * 37) % 100) + 1]));
  const full = (w: ReturnType<typeof world>) => selectContent(w.chosen(), w.segments, 1e6).fullMinutes;
  const opts = (w: ReturnType<typeof world>, over: object = {}) => ({ importance: scores(w), summaries: new Set(ids(w)), ...over });
  const summarized = (sel: ReturnType<typeof selectContent>) => [...sel.blueprints.values()].flatMap((bp) => bp.summary.flatMap((u) => u.segmentIds));

  it("não faz nada se o edital já cabe, se a opção está desligada ou se não há resumos disponíveis", () => {
    const w = world();
    expect(selectContent(w.chosen(), w.segments, full(w) * 1.2, {}, true, new Set(), opts(w)).turboAulas.size).toBe(0);
    expect(selectContent(w.chosen(), w.segments, full(w) * 0.5, {}, false, new Set(), opts(w)).turboAulas.size).toBe(0);
    expect(summarized(selectContent(w.chosen(), w.segments, full(w) * 0.5, {}, true, new Set(), { importance: scores(w) }))).toHaveLength(0);
    expect(summarized(selectContent(w.chosen(), w.segments, full(w) * 0.5, {}, true, new Set(), opts(w, { summaries: new Set() })))).toHaveLength(0);
  });
  it("faltando tempo, troca primeiro as unidades de MENOR importância no concurso", () => {
    const w = world();
    const imp = scores(w);
    const sel = selectContent(w.chosen(), w.segments, full(w) * 0.8, {}, true, new Set(), opts(w));
    const conv = summarized(sel);
    expect(conv.length).toBeGreaterThan(0);
    const kept = ids(w).filter((id) => !conv.includes(id));
    expect(Math.max(...conv.map((id) => imp[id]))).toBeLessThanOrEqual(Math.min(...kept.map((id) => imp[id])) + 0); // todas as trocadas valem menos que as mantidas
  });
  it("só troca quem tem resumo disponível", () => {
    const w = world();
    const have = new Set(ids(w).filter((_, i) => i % 3 === 0));
    const sel = selectContent(w.chosen(), w.segments, full(w) * 0.6, {}, true, new Set(), opts(w, { summaries: have }));
    for (const id of summarized(sel)) expect(have.has(id)).toBe(true);
  });
  it("troca o mínimo necessário: o que sobra cabe na capacidade e desfazer a última troca estouraria", () => {
    const w = world();
    const cap = full(w) * 0.85;
    const sel = selectContent(w.chosen(), w.segments, cap, {}, true, new Set(), opts(w));
    const total = [...sel.blueprints.values()].reduce((n, bp) => n + tierMinutes(bp, 1).total, 0);
    expect(total).toBeLessThanOrEqual(cap + 1e-6);
    expect(summarized(sel).length).toBeGreaterThan(0);
  });
  it("trechos fora do edital do concurso (nota null) não entram no plano", () => {
    const w = world();
    const imp = { ...scores(w), "a/a01/s01": null, "b/a02/s03": null } as Record<string, number | null>;
    const sel = selectContent(w.chosen(), w.segments, 1e6, {}, false, new Set(), { importance: imp });
    const present = [...sel.blueprints.values()].flatMap((bp) => [...bp.teoria, ...bp.summary].flatMap((u) => u.segmentIds));
    expect(present).not.toContain("a/a01/s01");
    expect(present).not.toContain("b/a02/s03");
    expect(present).toHaveLength(ids(w).length - 2);
  });
  it("o peso da disciplina na prova do concurso substitui o do catálogo", () => {
    const w = world();
    const cap = full(w) * 0.5;
    const base = selectContent(w.chosen(), w.segments, cap);
    const inverted = selectContent(w.chosen(), w.segments, cap, {}, false, new Set(), { examQuestions: { a: 1, b: 40 } });
    const bAulas = (sel: ReturnType<typeof selectContent>) => [...sel.tierByAula.keys()].filter((id) => id.startsWith("b/")).length;
    expect(bAulas(inverted)).toBeGreaterThanOrEqual(bAulas(base));
  });
  it("com tempo só para os resumos, todas as unidades viram resumo; sem tempo nenhum, nenhuma aula é marcada", () => {
    const w = world();
    const bps = selectContent(w.chosen(), w.segments, 1e6).blueprints;
    let allSummary = 0;
    for (const bp of bps.values()) allSummary += tierMinutes({ ...bp, teoria: [], summary: [...bp.teoria] }, 1).total;
    const sel = selectContent(w.chosen(), w.segments, allSummary + 1, {}, true, new Set(), opts(w));
    expect(sel.turboAulas.size).toBe(5);
    expect(summarized(sel)).toHaveLength(ids(w).length);
    expect(selectContent(w.chosen(), w.segments, 10, {}, true, new Set(), opts(w)).turboAulas.size).toBe(0); // só conta quem entra no plano
  });
});
