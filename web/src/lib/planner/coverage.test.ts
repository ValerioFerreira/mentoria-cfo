import { describe, expect, it } from "vitest";
import { computeCoverage, gapWarnings } from "./coverage";
import { selectContent } from "./select";
import { EXAM_TOTAL_QUESTIONS } from "./constants";
import { mkAulaWithSegs, mkCatalog, mkSegments, mkSubject } from "./testkit";
import type { Gap, Level } from "./types";

function world(completeness?: number) {
  const a1 = mkAulaWithSegs("a/a01", 1, 6, 12, 12, { incidence: 5, commentedRuns: [[200, 235]] });
  const a2 = mkAulaWithSegs("a/a02", 2, 4, 12, 12, { incidence: 3 });
  const a3 = mkAulaWithSegs("a/a03", 3, 3, 12, 12, { incidence: 2 });
  const b1 = mkAulaWithSegs("b/a01", 1, 5, 12, 12, { incidence: 4 });
  const subjects = [
    mkSubject("a", [a1.aula, a2.aula, a3.aula], { examQuestions: 10, sortOrder: 1, ...(completeness !== undefined ? { materialCompleteness: completeness } : {}) }),
    mkSubject("b", [b1.aula], { examQuestions: 5, sortOrder: 2 }),
  ];
  const segments = mkSegments(a1.segs, a2.segs, a3.segs, b1.segs);
  const chosen = (level: Level = 1) => subjects.map((subject) => ({ subject, level }));
  return { subjects, segments, chosen };
}

describe("computeCoverage", () => {
  it("com tempo de sobra: cobertura 100%, profundidade 100% e nada fica de fora", () => {
    const w = world();
    const sel = selectContent(w.chosen(), w.segments, 1e6);
    const cov = computeCoverage(w.chosen(), sel);
    expect(cov.selected).toBeCloseTo(1);
    expect(cov.depth).toBeCloseTo(1);
    for (const s of cov.subjects) {
      expect(s.coverage).toBeCloseTo(1);
      expect(s.notCovered).toEqual([]);
      expect(s.plannedHours).toBeGreaterThan(0);
    }
    // 15 das 70 questões da prova
    expect(cov.edital).toBeCloseTo(15 / EXAM_TOTAL_QUESTIONS);
  });
  it("cobertura da disciplina é limitada pela completude do material", () => {
    const w = world(0.8);
    const sel = selectContent(w.chosen(), w.segments, 1e6);
    const cov = computeCoverage(w.chosen(), sel);
    const a = cov.subjects.find((s) => s.subjectId === "a")!;
    expect(a.coverage).toBeCloseTo(0.8);
    expect(a.materialCompleteness).toBe(0.8);
    expect(cov.subjects.find((s) => s.subjectId === "b")!.coverage).toBeCloseTo(1);
  });
  it("aula dominada conta como vista; a profundidade dela é 60%", () => {
    const w = world();
    const known = { "b/a01": 2 as const };
    const sel = selectContent(w.chosen(), w.segments, 1e6, known);
    const cov = computeCoverage(w.chosen(), sel, known);
    const b = cov.subjects.find((s) => s.subjectId === "b")!;
    expect(b.coverage).toBeCloseTo(1);
    expect(b.depth).toBeCloseTo(0.6);
    expect(b.aulas).toEqual([]);
    expect(b.plannedHours).toBe(0);
  });
  it("com pouco tempo, a cobertura cai, as aulas ausentes aparecem em notCovered (por incidência) e as horas respeitam a capacidade", () => {
    const w = world();
    const full = selectContent(w.chosen(), w.segments, 1e6).fullMinutes;
    const cap = full * 0.4;
    const sel = selectContent(w.chosen(), w.segments, cap);
    const cov = computeCoverage(w.chosen(), sel);
    expect(cov.selected).toBeLessThan(1);
    expect(cov.selected).toBeGreaterThan(0);
    const missing = cov.subjects.flatMap((s) => s.notCovered);
    expect(missing.length).toBeGreaterThan(0);
    for (const s of cov.subjects) {
      const inc = s.notCovered.map((n) => n.incidence);
      expect(inc).toEqual([...inc].sort((x, y) => y - x));
      expect(s.notCovered.length).toBeLessThanOrEqual(6);
    }
    expect(cov.subjects.reduce((n, s) => n + s.plannedHours, 0) * 60).toBeLessThanOrEqual(cap + 5 * 6); // arredondamento a 0,1 h por disciplina
  });
  it("0 ≤ cobertura ≤ 1 e 0 ≤ profundidade ≤ 1 para várias capacidades e níveis", () => {
    const w = world();
    const full = selectContent(w.chosen(), w.segments, 1e6).fullMinutes;
    for (const level of [0, 1, 2, 3] as Level[])
      for (const frac of [0, 0.2, 0.7, 1, 1.5, 3, 10]) {
        const sel = selectContent(w.chosen(level), w.segments, full * frac);
        const cov = computeCoverage(w.chosen(level), sel);
        for (const x of [cov.selected, cov.edital, cov.depth, ...cov.subjects.flatMap((s) => [s.coverage, s.depth])]) {
          expect(x).toBeGreaterThanOrEqual(0);
          expect(x).toBeLessThanOrEqual(1 + 1e-9);
        }
        expect(cov.edital).toBeLessThanOrEqual(cov.selected + 1e-9);
      }
  });
  it("mais tempo nunca reduz a cobertura", () => {
    const w = world();
    const full = selectContent(w.chosen(), w.segments, 1e6).fullMinutes;
    let prev = 0;
    for (const frac of [0, 0.1, 0.3, 0.6, 1, 2, 5]) {
      const sel = selectContent(w.chosen(), w.segments, full * frac);
      const c = computeCoverage(w.chosen(), sel).selected;
      expect(c).toBeGreaterThanOrEqual(prev - 1e-9);
      prev = c;
    }
  });
  it("páginas de teoria cobertas nunca passam das elegíveis; minutos somam por tipo", () => {
    const w = world();
    const sel = selectContent(w.chosen(), w.segments, 1e6);
    const cov = computeCoverage(w.chosen(), sel);
    for (const s of cov.subjects) {
      expect(s.theoryPagesCovered).toBeLessThanOrEqual(s.theoryPagesEligible);
      const sum = s.minutes.teoria + s.minutes.revisao + s.minutes.fixacao + s.minutes.questoes;
      expect(s.plannedHours).toBeCloseTo(sum / 60, 1);
    }
    expect(cov.subjects.find((s) => s.subjectId === "a")!.theoryPagesEligible).toBe((6 + 4 + 3) * 12);
  });
  it("Modo Turbo marca as aulas em resumo no relatório", () => {
    const w = world();
    const full = selectContent(w.chosen(), w.segments, 1e6).fullMinutes;
    const sel = selectContent(w.chosen(), w.segments, full * 0.7, {}, true);
    const cov = computeCoverage(w.chosen(), sel);
    const turbo = cov.subjects.flatMap((s) => s.aulas).filter((a) => a.turbo);
    expect(turbo.length).toBe(sel.turboAulas.size);
    expect(turbo.length).toBeGreaterThan(0);
  });
  it("sem disciplinas escolhidas não há divisão por zero", () => {
    const sel = selectContent([], {}, 100);
    const cov = computeCoverage([], sel);
    expect(cov.selected).toBe(0);
    expect(cov.edital).toBe(0);
    expect(cov.depth).toBe(0);
    expect(cov.subjects).toEqual([]);
  });
});

describe("gapWarnings", () => {
  const gap = (id: string, subject: string, severity: Gap["severity"]): Gap => ({ id, subject, item: `item-${id}`, evidence: "", severity, remedy: "Veja o complemento." });
  const catalog = { ...mkCatalog([]), gaps: [gap("1", "a", "high"), gap("2", "a", "medium"), gap("3", "a", "low"), gap("4", "b", "high")] };
  it("avisa só lacunas altas e médias das disciplinas escolhidas", () => {
    const w = gapWarnings(catalog, ["a"]);
    expect(w).toEqual([
      "Lacuna no material (alta): item-1. Veja o complemento.",
      "Lacuna no material (média): item-2. Veja o complemento.",
    ]);
  });
  it("sem disciplinas ou sem lacunas, nenhum aviso", () => {
    expect(gapWarnings(catalog, [])).toEqual([]);
    expect(gapWarnings(mkCatalog([]), ["a"])).toEqual([]);
    expect(gapWarnings(catalog, ["c"])).toEqual([]);
  });
});
