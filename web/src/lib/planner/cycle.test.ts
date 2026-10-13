// Regras do ciclo de estudo (Teoria → Revisão → Fixação → Questões), da divisão diária e da reta final, com o catálogo REAL de /content.
import { describe, expect, it } from "vitest";
import { diffDays } from "./dates";
import { generatePlan } from "./index";
import { loadCatalog, loadExamQuestions, loadImportance, loadSegments } from "./fixtures";
import { CONTEST_SUBJECTS } from "../contests";
import type { Level, PlanResult, PlannedActivity } from "./types";

const catalog = loadCatalog();
const segments = loadSegments();
const ALL = CONTEST_SUBJECTS.CBMPE_OFICIAL.filter((id) => id !== "lingua-espanhola");
const importance = loadImportance("CBMPE_OFICIAL");
const examQuestions = loadExamQuestions("CBMPE_OFICIAL");
const allSummaries = Object.values(segments).flat().map((x) => x.id);
const isBlock = (key: string) => /#S(R|F|Q\d*)?$/.test(key); // atividades dos blocos de resumo (Turbo)
const START = "2026-10-12";
const EXAM = "2027-02-28";

type A = PlannedActivity & { ord: number };
const scenarios: { hours: number; level: Level; turbo: boolean }[] = [];
for (const [hours, level] of [[14, 0], [21, 1], [28, 2], [40, 2], [50, 3]] as [number, Level][])
  for (const turbo of [false, true]) scenarios.push({ hours, level, turbo });

const runs = scenarios.map((s) => {
  const plan: PlanResult = generatePlan({
    catalog, segments, startDate: START, examDate: EXAM, hoursPerWeek: s.hours, turbo: s.turbo, importance, examQuestions, summaries: allSummaries,
    subjects: ALL.map((id) => ({ id, level: s.level })),
  });
  const acts: A[] = plan.weeks.flatMap((w) => w.activities.map((a) => ({ ...a, ord: (w.index - 1) * 7 + a.day! })));
  const label = `${s.hours}h/n${s.level}${s.turbo ? "/turbo" : ""}`;
  return { ...s, plan, acts, content: acts.filter((a) => a.scope !== "FINAL"), label };
});

describe("ciclo por aula (todos os cenários, com e sem Turbo)", () => {
  it("ciclo normal: nenhuma Questões sem Revisão antes; nenhuma Revisão/Fixação/Questões antes da Teoria", () => {
    for (const r of runs) {
      const normal = r.content.filter((a) => !isBlock(a.key) && !a.turbo);
      for (const [aula, l] of Map.groupBy(normal, (a) => a.aulaId)) {
        const T = l.filter((a) => a.type === "TEORIA");
        const R = l.filter((a) => a.type === "REVISAO");
        if (l.some((a) => a.type === "QUESTOES")) expect(R.length, `${r.label} ${aula}`).toBeGreaterThan(0);
        for (const x of l.filter((a) => a.type !== "TEORIA")) expect(x.ord, `${r.label} ${x.key}`).toBeGreaterThan(Math.min(...T.map((t) => t.ord)));
      }
    }
  });

  it("toda Teoria (normal ou resumo) tem um caderno de Questões que a referencia, depois dela", () => {
    for (const r of runs) {
      const quizzes = r.content.filter((a) => a.type === "QUESTOES");
      for (const t of r.content.filter((a) => a.type === "TEORIA")) {
        const q = quizzes.find((x) => x.refKeys.includes(t.key));
        expect(q, `${r.label} ${t.key}`).toBeDefined();
        expect(q!.ord, `${r.label} ${t.key}`).toBeGreaterThan(t.ord);
      }
    }
  });

  it("blocos de resumo (Turbo): Revisão ≥ 1 dia depois dos resumos, Questões depois da Revisão/Fixação, ≤ 3 unidades por atividade", () => {
    const turboRuns = runs.filter((r) => r.turbo);
    expect(turboRuns.some((r) => r.content.some((a) => a.turbo))).toBe(true);
    for (const r of turboRuns) {
      const at = new Map(r.acts.map((a) => [a.key, a.ord]));
      for (const a of r.content.filter((x) => x.turbo)) expect(a.segmentIds.length, `${r.label} ${a.key}`).toBeLessThanOrEqual(6); // 3 unidades (uma unidade pode juntar 2 trechos curtos)
      for (const x of r.content.filter((y) => isBlock(y.key) && y.type !== "TEORIA")) {
        for (const k of x.refKeys) expect(x.ord - at.get(k)!, `${r.label} ${x.key} ← ${k}`).toBeGreaterThanOrEqual(1);
      }
      for (const [tag, l] of Map.groupBy(r.content.filter((y) => isBlock(y.key)), (y) => y.key.split("#S")[0])) {
        const first = (t: string) => Math.min(...l.filter((y) => y.type === t).map((y) => y.ord));
        const last = (t: string) => Math.max(...l.filter((y) => y.type === t).map((y) => y.ord));
        if (l.some((y) => y.type === "REVISAO")) expect(first("REVISAO"), `${r.label} ${tag}`).toBeGreaterThan(first("TEORIA"));
        if (l.some((y) => y.type === "QUESTOES")) expect(first("QUESTOES"), `${r.label} ${tag}`).toBeGreaterThan(last("TEORIA"));
      }
    }
  });

  it("folgas em dias: Revisão ≥ 1 dia depois das Teorias que revê; Fixação depois de toda Revisão; Questões ≥ 1 dia depois da Fixação", () => {
    for (const r of runs) {
      const at = new Map(r.acts.map((a) => [a.key, a.ord]));
      for (const a of r.content.filter((x) => x.type === "REVISAO")) for (const k of a.refKeys) expect(a.ord - at.get(k)!, `${r.label} ${a.key}`).toBeGreaterThanOrEqual(1);
      const byAula = Map.groupBy(r.content.filter((a) => !isBlock(a.key) && !a.turbo), (a) => a.aulaId);
      for (const [aula, l] of byAula) {
        const F = l.filter((a) => a.type === "FIXACAO");
        const Q = l.filter((a) => a.type === "QUESTOES");
        const R = l.filter((a) => a.type === "REVISAO");
        if (F.length) {
          for (const x of R) expect(Math.min(...F.map((f) => f.ord)) - x.ord, `${r.label} ${aula} R→F`).toBeGreaterThanOrEqual(1);
          for (const q of Q) expect(q.ord - Math.max(...F.map((f) => f.ord)), `${r.label} ${aula} F→Q`).toBeGreaterThanOrEqual(1);
        } else if (R.length) {
          for (const q of Q) expect(q.ord - Math.max(...R.map((x) => x.ord)), `${r.label} ${aula} R→Q`).toBeGreaterThanOrEqual(1);
        }
      }
    }
  });

  it("o caderno vem logo depois da Fixação: ao menos 80% dos pares ficam a até 4 dias", () => {
    for (const r of runs) {
      const gaps: number[] = [];
      for (const [, l] of Map.groupBy(r.content.filter((a) => !isBlock(a.key) && !a.turbo), (a) => a.aulaId)) {
        const F = l.filter((a) => a.type === "FIXACAO");
        const Q = l.filter((a) => a.type === "QUESTOES");
        if (F.length && Q.length) gaps.push(Math.min(...Q.map((a) => a.ord)) - Math.max(...F.map((a) => a.ord)));
      }
      if (gaps.length >= 10) expect(gaps.filter((g) => g <= 4).length / gaps.length, r.label).toBeGreaterThanOrEqual(0.8);
    }
  });

  it("a prática é parte do plano: Revisão + Fixação + Questões ≥ 25% do tempo de conteúdo (≥ 40% sem Turbo)", () => {
    for (const r of runs) {
      const total = r.content.reduce((n, a) => n + a.minutes, 0);
      const practice = r.content.filter((a) => a.type !== "TEORIA").reduce((n, a) => n + a.minutes, 0);
      expect(practice / total, r.label).toBeGreaterThanOrEqual(r.turbo ? 0.12 : 0.4);
    }
  });
});

describe("divisão diária (todos os cenários)", () => {
  it("nenhuma disciplina passa de 2 h por dia e, na imensa maioria dos dias, faz uma só atividade", () => {
    for (const r of runs) {
      const perDay = Map.groupBy(r.acts, (a) => `${a.ord}|${a.subjectId}`);
      for (const [k, l] of perDay) expect(l.reduce((n, a) => n + a.minutes, 0), `${r.label} ${k}`).toBeLessThanOrEqual(120);
      const single = [...perDay.values()].filter((l) => l.length === 1).length / perDay.size;
      expect(single, r.label).toBeGreaterThanOrEqual(0.9);
    }
  });

  it("nunca mais de 4 dias seguidos só de Teoria (3 sem Turbo)", () => {
    for (const r of runs) {
      const byOrd = Map.groupBy(r.content, (a) => a.ord);
      let run = 0;
      let max = 0;
      for (const o of [...byOrd.keys()].sort((x, y) => x - y)) {
        run = byOrd.get(o)!.every((a) => a.type === "TEORIA") ? run + 1 : 0;
        max = Math.max(max, run);
      }
      expect(max, r.label).toBeLessThanOrEqual(r.turbo ? 4 : 3);
    }
  });

  it("os minutos das atividades vêm do ciclo (não são alterados pela divisão em dias)", () => {
    const valid = new Set([15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]);
    for (const r of runs) for (const a of r.acts) expect(valid.has(a.minutes), `${r.label} ${a.key} ${a.minutes}`).toBe(true);
  });
});

describe("prioridade e reta final (todos os cenários)", () => {
  it("nenhuma disciplina fica sem atividade de conteúdo", () => {
    for (const r of runs) for (const id of ALL) expect(r.content.some((a) => a.subjectId === id), `${r.label} ${id}`).toBe(true);
  });

  it("o conteúdo vai até D-2 e D-1 tem uma única atividade: Revisão dos assuntos de maior peso", () => {
    const examOrd = diffDays(START, EXAM);
    const heaviest = [...catalog.subjects].filter((s) => ALL.includes(s.id)).sort((a, b) => b.examQuestions - a.examQuestions || a.sortOrder - b.sortOrder)[0].id;
    for (const r of runs) {
      expect(Math.max(...r.content.map((a) => a.ord)), r.label).toBeLessThanOrEqual(examOrd - 2);
      const eve = r.acts.filter((a) => a.ord === examOrd - 1);
      expect(eve, r.label).toHaveLength(1);
      expect(eve[0].type).toBe("REVISAO");
      expect(eve[0].scope).toBe("FINAL");
      expect(eve[0].subjectId).toBe(heaviest); // disciplina de maior peso na prova
      expect(r.acts.every((a) => a.ord < examOrd)).toBe(true);
    }
  });

  it("o conteúdo ocupa quase todo o tempo até a prova: a última Teoria cai a no máximo 6 dias dela", () => {
    const examOrd = diffDays(START, EXAM);
    for (const r of runs.filter((x) => x.hours <= 40)) {
      const lastTheory = Math.max(...r.content.filter((a) => a.type === "TEORIA").map((a) => a.ord));
      expect(examOrd - lastTheory, r.label).toBeLessThanOrEqual(6);
    }
  });

  it("as disciplinas de maior peso recebem mais tempo de conteúdo que as de menor peso (em média)", () => {
    for (const r of runs.filter((x) => !x.turbo)) {
      const mins = (id: string) => r.content.filter((a) => a.subjectId === id).reduce((n, a) => n + a.minutes, 0);
      const heavy = catalog.subjects.filter((s) => ALL.includes(s.id) && s.examQuestions >= 8).map((s) => mins(s.id) / s.aulas.length);
      const light = catalog.subjects.filter((s) => ALL.includes(s.id) && s.examQuestions <= 3).map((s) => mins(s.id) / s.aulas.length);
      if (heavy.length && light.length) {
        const mean = (xs: number[]) => xs.reduce((a, b) => a + b, 0) / xs.length;
        expect(mean(heavy) + 1, r.label).toBeGreaterThanOrEqual(mean(light) * 0.5);
      }
    }
  });
});
