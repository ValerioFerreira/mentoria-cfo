// Reprogramação de atividades atrasadas: ordem T → R → F → Q com folga, dependentes reorganizadas, limites do dia e D-2/D-1.
// Duas camadas: um plano pequeno montado à mão (regras isoladas) e planos REAIS gerados pelo motor (invariantes em todas as opções).
import { describe, expect, it } from "vitest";
import { diffDays } from "./dates";
import { dayTarget } from "./days";
import { loadCatalog, loadExamQuestions, loadImportance, loadSegments } from "./fixtures";
import { generatePlan } from "./index";
import { depsFromKeys, planReschedule, type EngineActivity, type EngineInput, type EngineResult, type EngineStatus } from "./reschedule";
import type { RescheduleParams } from "./reschedule-types";
import { CONTEST_SUBJECTS } from "../contests";
import { MAX_SAME_SUBJECT_MINUTES_PER_DAY } from "./constants";
import type { Level, PlanResult } from "./types";

// ───────────────────────────── plano pequeno, à mão ─────────────────────────────
let n = 0;
const act = (key: string, type: EngineActivity["type"], ord: number, over: Partial<EngineActivity> = {}): EngineActivity => ({
  id: key, key, type, subjectId: "s1", aulaId: key.split("#")[0], minutes: 60, ord, sortOrder: n++, status: "PENDING", scope: "AULA", turbo: false, refKeys: [], ...over,
});
const W = 420; // ≈ 65 min por dia útil
const base = (activities: EngineActivity[], params: RescheduleParams, over: Partial<EngineInput> = {}): EngineInput => ({
  activities, weeklyMinutes: W, todayOrd: 10, firstOrd: 0, lastContentOrd: 40, eveOrd: 41, selectedIds: [], params, ...over,
});
const finalOrd = (input: EngineInput, r: EngineResult) => {
  const m = new Map(input.activities.map((a) => [a.id, a.ord]));
  for (const p of r.placements) m.set(p.id, p.toOrd);
  return m;
};

describe("depsFromKeys", () => {
  const acts = [
    act("a/a01#T1", "TEORIA", 1),
    act("a/a01#T2", "TEORIA", 2),
    act("a/a01#R1", "REVISAO", 4, { refKeys: ["a/a01#T1", "a/a01#T2"] }),
    act("a/a01#F1", "FIXACAO", 6),
    act("a/a01#Q1", "QUESTOES", 8),
    act("a/a01#Q2", "QUESTOES", 9),
    act("FINAL#s1#R1-1", "REVISAO", 30, { scope: "FINAL" }),
  ];
  const deps = depsFromKeys(acts);
  const of = (id: string) => (deps.get(id) ?? []).map((d) => `${d.id}:${d.gap}`).sort();
  it("reconstrói o ciclo T → R → F → Q com as folgas", () => {
    expect(of("a/a01#T1")).toEqual([]);
    expect(of("a/a01#T2")).toEqual(["a/a01#T1:0"]);
    expect(of("a/a01#R1")).toEqual(["a/a01#T1:1", "a/a01#T2:1"]);
    expect(of("a/a01#F1")).toEqual(["a/a01#R1:1"]);
    expect(of("a/a01#Q1")).toEqual(["a/a01#F1:1"]);
    expect(of("a/a01#Q2")).toEqual(["a/a01#F1:1", "a/a01#Q1:0"]);
    expect(of("FINAL#s1#R1-1")).toEqual([]);
  });
  it("blocos do Turbo: resumo → revisão → fixação → caderno", () => {
    const b = [
      act("x/a01/s01#S", "TEORIA", 1, { turbo: true }),
      act("x/a01/s01#SR", "REVISAO", 3, { refKeys: ["x/a01/s01#S"] }),
      act("x/a01/s01#SF", "FIXACAO", 5),
      act("x/a01/s01#SQ1", "QUESTOES", 7, { refKeys: ["x/a01/s01#S"] }),
    ];
    const d = depsFromKeys(b);
    const get = (id: string) => (d.get(id) ?? []).map((x) => `${x.id}:${x.gap}`).sort();
    expect(get("x/a01/s01#SR")).toEqual(["x/a01/s01#S:1"]);
    expect(get("x/a01/s01#SF")).toEqual(["x/a01/s01#SR:1"]);
    expect(get("x/a01/s01#SQ1")).toEqual(["x/a01/s01#S:1", "x/a01/s01#SF:1", "x/a01/s01#SR:1"].sort());
  });
});

describe("reprogramação em plano pequeno", () => {
  // aula atrasada: Teoria e Revisão no passado; Fixação e Questões no futuro; dias 10–12 já cheios de outra disciplina
  const chain = () => [
    act("a/a01#T1", "TEORIA", 2),
    act("a/a01#R1", "REVISAO", 4, { refKeys: ["a/a01#T1"] }),
    act("a/a01#F1", "FIXACAO", 12),
    act("a/a01#Q1", "QUESTOES", 14),
  ];
  const filler = (from: number, to: number) => Array.from({ length: to - from + 1 }, (_, i) => act(`o/o${from + i}#T1`, "TEORIA", from + i, { subjectId: "s2", aulaId: `o/o${from + i}` }));

  it("SPREAD coloca as atrasadas hoje ou depois e mantém a ordem T → R → F → Q com folga", () => {
    const acts = chain();
    const input = base(acts, { option: "SPREAD", windowDays: 7, extraLoadPct: 25 }, { selectedIds: ["a/a01#T1", "a/a01#R1"] });
    const r = planReschedule(input);
    const ord = finalOrd(input, r);
    expect(ord.get("a/a01#T1")!).toBeGreaterThanOrEqual(10);
    expect(ord.get("a/a01#R1")! - ord.get("a/a01#T1")!).toBeGreaterThanOrEqual(1);
    expect(ord.get("a/a01#F1")! - ord.get("a/a01#R1")!).toBeGreaterThanOrEqual(1);
    expect(ord.get("a/a01#Q1")! - ord.get("a/a01#F1")!).toBeGreaterThanOrEqual(1);
    expect(r.doesNotFit).toEqual([]);
  });

  it("a cascata empurra as dependentes quando a selecionada cai depois do que elas esperavam", () => {
    // dias 10–12 sem folga (60 + 60 > 125% de ~65): a Teoria só cabe a partir do dia 13 e o resto da aula vem junto
    const acts = [...chain(), ...filler(10, 12)];
    const input = base(acts, { option: "SPREAD", windowDays: 7, extraLoadPct: 25 }, { selectedIds: ["a/a01#T1", "a/a01#R1"] });
    const r = planReschedule(input);
    const ord = finalOrd(input, r);
    expect(ord.get("a/a01#T1")!).toBeGreaterThanOrEqual(13);
    expect(ord.get("a/a01#R1")! - ord.get("a/a01#T1")!).toBeGreaterThanOrEqual(1);
    const f = r.placements.find((p) => p.id === "a/a01#F1");
    expect(f?.reason).toBe("DEPENDENT");
    expect(f?.causedById).toBe("a/a01#R1");
    expect(ord.get("a/a01#F1")! - ord.get("a/a01#R1")!).toBeGreaterThanOrEqual(1);
    expect(ord.get("a/a01#Q1")! - ord.get("a/a01#F1")!).toBeGreaterThanOrEqual(1);
    expect(r.dependentsMoved).toBeGreaterThanOrEqual(1);
  });

  it("não mexe nas dependentes que já estavam depois da folga", () => {
    const acts = chain();
    acts[2].ord = 30;
    acts[3].ord = 32;
    const input = base(acts, { option: "SPREAD", windowDays: 7, extraLoadPct: 25 }, { selectedIds: ["a/a01#T1", "a/a01#R1"] });
    const r = planReschedule(input);
    expect(r.placements.map((p) => p.id).sort()).toEqual(["a/a01#R1", "a/a01#T1"]);
    expect(r.dependentsMoved).toBe(0);
  });

  it("FILL_GAPS nunca passa da meta do dia", () => {
    const acts = [...chain(), ...filler(10, 12)];
    const input = base(acts, { option: "FILL_GAPS" }, { selectedIds: ["a/a01#T1", "a/a01#R1"] });
    const r = planReschedule(input);
    const ord = finalOrd(input, r);
    const byDay = new Map<number, number>();
    for (const a of acts) byDay.set(ord.get(a.id)!, (byDay.get(ord.get(a.id)!) ?? 0) + a.minutes);
    for (const p of r.placements) expect(byDay.get(p.toOrd)!, `dia ${p.toOrd}`).toBeLessThanOrEqual(dayTarget(W, p.toOrd) + 1e-6);
  });

  it("FILL_GAPS: uma revisão geral de sobra cede o lugar quando não há folga", () => {
    // todos os dias de 10 a 40 estão no limite da meta, mas o dia 22 (uma terça) tem uma revisão geral de sobra
    const days = Array.from({ length: 31 }, (_, i) => 10 + i);
    const full = days.map((d) =>
      d === 22
        ? act("FINAL#s2#R1-1", "REVISAO", d, { subjectId: "s2", aulaId: "o/x", scope: "FINAL", minutes: 60 })
        : act(`o/o${d}#T1`, "TEORIA", d, { subjectId: "s2", aulaId: `o/o${d}`, minutes: Math.floor(dayTarget(W, d)) - (Math.floor(dayTarget(W, d)) % 5) }),
    );
    const acts = [act("a/a01#T1", "TEORIA", 2, { minutes: 30 }), ...full];
    const input = base(acts, { option: "FILL_GAPS" }, { selectedIds: ["a/a01#T1"] });
    const r = planReschedule(input);
    expect(r.yielded).toEqual(["FINAL#s2#R1-1"]);
    expect(r.placements.find((p) => p.id === "a/a01#T1")?.toOrd).toBe(22);
    expect(r.warnings.some((w) => w.code === "SPARE_REVIEW_YIELDED")).toBe(true);
  });

  it("se uma atividade da cadeia não cabe, as anteriores que seriam movidas voltam ao lugar (nada de Revisão no passado e Teoria no futuro)", () => {
    // o dia 10 tem folga, mas do dia 11 em diante todos os dias estão lotados: a Teoria caberia, a Revisão (1 dia depois) não
    const full = Array.from({ length: 30 }, (_, i) => act(`o/o${11 + i}#T1`, "TEORIA", 11 + i, { subjectId: "s2", aulaId: `o/o${11 + i}`, minutes: 70 }));
    const acts = [...chain().slice(0, 2), ...full];
    const input = base(acts, { option: "FILL_GAPS" }, { selectedIds: ["a/a01#T1", "a/a01#R1"] });
    const r = planReschedule(input);
    expect(r.placements.some((p) => p.id === "a/a01#T1" || p.id === "a/a01#R1")).toBe(false);
    expect(r.doesNotFit.sort()).toEqual(["a/a01#R1", "a/a01#T1"]);
    const ord = finalOrd(input, r);
    expect(ord.get("a/a01#R1")! - ord.get("a/a01#T1")!).toBeGreaterThanOrEqual(1); // a ordem original continua valendo
  });

  it("MOVE_TO_DAY leva tudo ao dia escolhido, respeitando a folga entre Teoria e Revisão", () => {
    const acts = chain();
    const input = base(acts, { option: "MOVE_TO_DAY" }, { selectedIds: ["a/a01#T1", "a/a01#R1"], targetOrd: 15 });
    const r = planReschedule(input);
    const ord = finalOrd(input, r);
    expect(ord.get("a/a01#T1")).toBe(15);
    expect(ord.get("a/a01#R1")).toBe(16); // mesmo pedindo o dia 15, a Revisão espera 1 dia depois da Teoria
    expect(ord.get("a/a01#F1")! - 16).toBeGreaterThanOrEqual(1);
  });

  it("DISMISS dispensa as selecionadas, libera as dependentes e avisa o impacto", () => {
    const acts = chain();
    const input = base(acts, { option: "DISMISS" }, { selectedIds: ["a/a01#T1", "a/a01#R1"] });
    const r = planReschedule(input);
    expect(r.dismissed.sort()).toEqual(["a/a01#R1", "a/a01#T1"]);
    expect(r.placements).toEqual([]); // Fixação e Questões não dependem mais de nada que ficou para trás
    expect(r.warnings.find((w) => w.code === "COVERAGE_IMPACT")?.count).toBe(2);
  });

  it("o que passa de D-2 vira 'não cabe' e fica onde estava; D-1 não é tocado", () => {
    const acts = [...chain(), ...filler(10, 11), act("FINAL#s1#VESPERA", "REVISAO", 41, { scope: "FINAL" })];
    const input = base(acts, { option: "SPREAD", windowDays: 3 }, { selectedIds: ["a/a01#T1", "a/a01#R1"], lastContentOrd: 11 });
    const r = planReschedule(input);
    expect(r.placements.every((p) => p.toOrd <= 11)).toBe(true);
    expect(r.placements.some((p) => p.id === "FINAL#s1#VESPERA")).toBe(false);
    expect(r.doesNotFit.length).toBeGreaterThan(0);
    expect(r.warnings.some((w) => w.code === "DOES_NOT_FIT")).toBe(true);
  });

  it("nunca passa de 120 min da mesma disciplina no dia", () => {
    const acts = [act("a/a01#T1", "TEORIA", 2), act("b/b01#T1", "TEORIA", 3, { aulaId: "b/b01" }), act("c/c01#T1", "TEORIA", 4, { aulaId: "c/c01" })];
    const input = base(acts, { option: "SPREAD", windowDays: 3, extraLoadPct: 40 }, { selectedIds: acts.map((a) => a.id) });
    const r = planReschedule(input);
    const ord = finalOrd(input, r);
    const per = new Map<number, number>();
    for (const a of acts) per.set(ord.get(a.id)!, (per.get(ord.get(a.id)!) ?? 0) + a.minutes);
    for (const m of per.values()) expect(m).toBeLessThanOrEqual(MAX_SAME_SUBJECT_MINUTES_PER_DAY);
  });
});

// ───────────────────────────── planos reais ─────────────────────────────
const catalog = loadCatalog();
const segments = loadSegments();
const ALL = CONTEST_SUBJECTS.CBMPE_OFICIAL.filter((id) => id !== "lingua-espanhola");
const importance = loadImportance("CBMPE_OFICIAL");
const examQuestions = loadExamQuestions("CBMPE_OFICIAL");
const START = "2026-10-12";
const EXAM = "2027-02-28";

function real(hours: number, level: Level, turbo: boolean, today: number) {
  const plan: PlanResult = generatePlan({
    catalog, segments, startDate: START, examDate: EXAM, hoursPerWeek: hours, turbo, importance, examQuestions,
    summaries: Object.values(segments).flat().map((x) => x.id), subjects: ALL.map((id) => ({ id, level })),
  });
  const examOrd = diffDays(START, EXAM);
  const acts: EngineActivity[] = plan.weeks.flatMap((w) =>
    w.activities.map((a, i) => {
      const ord = (w.index - 1) * 7 + a.day!;
      // até 10 dias antes de hoje: atrasado (pendente); antes disso, feito; de hoje em diante, pendente
      const status: EngineStatus = ord < today - 10 ? "DONE" : "PENDING";
      return {
        id: a.key, key: a.key, type: a.type, subjectId: a.subjectId, aulaId: a.aulaId, minutes: a.minutes, ord, sortOrder: i, status,
        scope: a.scope ?? "AULA", turbo: !!a.turbo, refKeys: a.refKeys,
      };
    }),
  );
  const overdue = acts.filter((a) => a.status === "PENDING" && a.ord < today && a.scope === "AULA");
  return { plan, acts, overdue, weeklyMinutes: plan.params.weeklyMinutes ?? hours * 60, examOrd };
}

const OPTIONS: RescheduleParams[] = [
  { option: "SPREAD", windowDays: 3, extraLoadPct: 15 },
  { option: "SPREAD", windowDays: 7, extraLoadPct: 25 },
  { option: "SPREAD", windowDays: 14, extraLoadPct: 40 },
  { option: "FILL_GAPS" },
  { option: "MOVE_TO_DAY" },
  { option: "DISMISS" },
  { option: "RECALC_REST" },
];

describe("planos reais: invariantes de toda reprogramação", () => {
  for (const [hours, level, turbo] of [[21, 1, false], [28, 2, true], [40, 2, false]] as [number, Level, boolean][]) {
    const today = 45;
    const R = real(hours, level, turbo, today);
    it(`${hours}h/n${level}${turbo ? "/turbo" : ""}: há atrasadas para reprogramar`, () => {
      expect(R.overdue.length).toBeGreaterThan(5);
    });
    for (const params of OPTIONS) {
      const label = `${hours}h/n${level}${turbo ? "/turbo" : ""} · ${params.option}${params.windowDays ? ` ${params.windowDays}d` : ""}`;
      it(label, () => {
        const input: EngineInput = {
          activities: R.acts, weeklyMinutes: R.weeklyMinutes, todayOrd: today, firstOrd: 0, lastContentOrd: R.examOrd - 2, eveOrd: R.examOrd - 1,
          selectedIds: R.overdue.map((a) => a.id), params, targetOrd: today + 3,
        };
        const r = planReschedule(input);
        const ord = finalOrd(input, r);
        const byId = new Map(R.acts.map((a) => [a.id, a]));
        const gone = new Set([...r.dismissed, ...r.yielded, ...(r.noFitLeavesPlan ? r.doesNotFit : [])]);

        // 1. nada vai para antes de hoje, nem depois de D-2, e a véspera não é tocada
        for (const p of r.placements) {
          expect(p.toOrd, `${p.id} antes de hoje`).toBeGreaterThanOrEqual(today);
          expect(p.toOrd, `${p.id} depois de D-2`).toBeLessThanOrEqual(R.examOrd - 2);
          expect(byId.get(p.id)!.ord).toBe(p.fromOrd);
          expect(byId.get(p.id)!.ord).not.toBe(R.examOrd - 1);
        }
        // 2. ordem T → R → F → Q com a folga, para tudo o que está no plano depois da reprogramação
        const deps = depsFromKeys(R.acts);
        const noFit = new Set(r.doesNotFit);
        for (const a of R.acts) {
          if (a.status !== "PENDING" || gone.has(a.id) || noFit.has(a.id)) continue;
          for (const d of deps.get(a.id) ?? []) {
            const dep = byId.get(d.id)!;
            if (gone.has(d.id) || noFit.has(d.id)) continue;
            if (!r.placements.some((p) => p.id === a.id || p.id === d.id)) continue; // só o que a reprogramação tocou
            const depOrd = dep.status === "DONE" ? Math.min(dep.ord, today) : ord.get(d.id)!;
            expect(ord.get(a.id)!, `${a.key} depois de ${dep.key}`).toBeGreaterThanOrEqual(depOrd + d.gap);
          }
        }
        // 3. ≤ 120 min da mesma disciplina no dia, nos dias que a reprogramação tocou
        const touched = new Set(r.placements.map((p) => p.toOrd));
        const per = new Map<string, number>();
        for (const a of R.acts) {
          if (gone.has(a.id)) continue;
          const o = ord.get(a.id)!;
          if (touched.has(o)) per.set(`${o}|${a.subjectId}`, (per.get(`${o}|${a.subjectId}`) ?? 0) + a.minutes);
        }
        if (params.option !== "MOVE_TO_DAY") for (const [k, m] of per) expect(m, k).toBeLessThanOrEqual(MAX_SAME_SUBJECT_MINUTES_PER_DAY);
        // 4. os minutos nunca mudam e cada atividade aparece uma só vez na ordem do dia
        for (const ids of r.order.values()) expect(new Set(ids).size).toBe(ids.length);
        // 5. a opção respeita o que promete
        if (params.option === "DISMISS") expect(r.dismissed.length).toBe(R.overdue.length);
        if (params.option !== "DISMISS") expect(r.dismissed).toEqual([]);
        if (params.option === "FILL_GAPS") for (const p of r.placements.filter((x) => x.reason === "SELECTED")) expect(p.toOrd).toBeGreaterThanOrEqual(today);
      });
    }
  }
});
