import { describe, expect, it } from "vitest";
import { generatePlan } from "./index";
import { loadCatalog, loadExamQuestions, loadImportance, loadSegments } from "./fixtures";
import { CONTEST_SUBJECTS } from "../contests";
import { planFromResult, verifyPlan, type VerifyContext, type VerifyPlan } from "./verify";
import type { Known, Level, PlanInput } from "./types";

const catalog = loadCatalog();
const segments = loadSegments();
const importance = loadImportance("CBMPE_OFICIAL");
const examQuestions = loadExamQuestions("CBMPE_OFICIAL");
const allSummaries = Object.values(segments).flat().map((x) => x.id);
const ALL = CONTEST_SUBJECTS.CBMPE_OFICIAL.filter((id) => id !== "lingua-espanhola");
const START = "2026-10-12";
const EXAM = "2027-02-28";
const ctx: VerifyContext = { catalog, segments, importance, summaries: new Set(allSummaries) };

const build = (hours: number, level: Level, extra: Partial<PlanInput> = {}, subjects = ALL) => {
  const input: PlanInput = { catalog, segments, startDate: START, examDate: EXAM, hoursPerWeek: hours, subjects: subjects.map((id) => ({ id, level })), importance, examQuestions, summaries: allSummaries, contest: "CBMPE_OFICIAL", ...extra };
  return planFromResult(generatePlan(input), START, EXAM);
};
const clone = (p: VerifyPlan): VerifyPlan => JSON.parse(JSON.stringify(p));
const codes = (p: VerifyPlan) => verifyPlan(p, ctx).errors.map((e) => e.code);

describe("verificação de planos: planos do motor passam", () => {
  const scenarios: [number, Level, boolean][] = [[14, 0, false], [21, 1, true], [28, 2, false], [40, 2, true], [50, 3, false]];
  for (const [hours, level, turbo] of scenarios) {
    it(`${hours} h · nível ${level}${turbo ? " · Turbo" : ""}: LIBERAR, sem erros`, () => {
      const r = verifyPlan(build(hours, level, { turbo }), ctx);
      expect(r.errors, JSON.stringify(r.errors.slice(0, 3))).toEqual([]);
      expect(r.verdict).toBe("LIBERAR");
    }, 30_000);
  }
  it("com anamnese ('já estudei', 'domino') e assuntos desmarcados", () => {
    const aulas = catalog.subjects.find((s) => s.id === "matematica")!.aulas.filter((a) => a.selectable);
    const known: Record<string, Known> = { [aulas[0].id]: 2, [aulas[1].id]: 1 };
    const p = build(25, 1, { known, excludedAulas: [aulas[2].id] });
    expect(verifyPlan(p, ctx).errors).toEqual([]);
    expect(p.request.excludedAulas).toEqual([aulas[2].id]);
  });
  it("início no meio da semana e prova numa segunda-feira", () => {
    const p = planFromResult(generatePlan({ catalog, segments, startDate: START, firstDay: 3, examDate: "2027-02-22", hoursPerWeek: 25, subjects: ALL.slice(0, 5).map((id) => ({ id, level: 1 as Level })) }), START, "2027-02-22");
    expect(verifyPlan(p, ctx).errors).toEqual([]);
  });
});

describe("verificação de planos: defeitos injetados são encontrados", () => {
  const base = build(28, 2, { turbo: false });
  const find = (p: VerifyPlan, type: string, pred: (a: VerifyPlan["activities"][number]) => boolean = () => true) => p.activities.find((a) => a.type === type && a.scope === "AULA" && pred(a))!;

  it("Revisão antes da Teoria que revê", () => {
    const p = clone(base);
    const r = find(p, "REVISAO");
    const t = p.activities.find((a) => a.key === r.refKeys[0])!;
    r.week = t.week;
    r.day = t.day;
    expect(codes(p)).toContain("REVISAO_NO_DIA_DA_TEORIA");
  });
  it("Questões sem a Revisão da aula", () => {
    const p = clone(base);
    const q = find(p, "QUESTOES");
    p.activities = p.activities.filter((a) => !(a.type === "REVISAO" && a.aulaId === q.aulaId && a.scope === "AULA"));
    expect(codes(p)).toContain("QUESTOES_SEM_REVISAO");
  });
  it("Fixação no mesmo dia das Questões", () => {
    const p = clone(base);
    const f = find(p, "FIXACAO");
    const q = find(p, "QUESTOES", (a) => a.aulaId === f.aulaId);
    q.week = f.week;
    q.day = f.day;
    expect(codes(p)).toContain("QUESTOES_SEM_FOLGA_FIXACAO");
  });
  it("Teoria sem caderno de Questões", () => {
    const p = clone(base);
    const t = find(p, "TEORIA");
    p.activities = p.activities.filter((a) => !(a.type === "QUESTOES" && a.refKeys.includes(t.key)));
    expect(codes(p)).toContain("TEORIA_SEM_CADERNO");
  });
  it("disciplina que o aluno não pediu", () => {
    const p = clone(base);
    p.request.subjects = p.request.subjects.filter((s) => s.id !== "fisica");
    expect(codes(p)).toContain("DISCIPLINA_NAO_PEDIDA");
  });
  it("disciplina pedida que ficou de fora", () => {
    const p = clone(base);
    p.activities = p.activities.filter((a) => a.subjectId !== "fisica");
    for (const w of p.weeks) w.targetMinutes = p.activities.filter((a) => a.week === w.index).reduce((n, a) => n + a.minutes, 0);
    expect(codes(p)).toContain("DISCIPLINA_SEM_CONTEUDO");
  });
  it("aula que o aluno disse dominar ou desmarcou aparece no plano", () => {
    const p = clone(base);
    const t = find(p, "TEORIA");
    p.request.known = { [t.aulaId]: 2 };
    expect(codes(p)).toContain("AULA_DOMINADA");
    p.request.known = {};
    p.request.excludedAulas = [t.aulaId];
    expect(codes(p)).toContain("AULA_EXCLUIDA");
  });
  it("mais de 2 h da mesma disciplina no dia e semana acima da meta", () => {
    const p = clone(base);
    const subj = p.activities[0].subjectId;
    const day = p.activities[0];
    for (const a of p.activities.filter((x) => x.subjectId === subj).slice(0, 4)) {
      a.week = day.week;
      a.day = day.day;
    }
    const c = codes(p);
    expect(c).toContain("DISCIPLINA_DIA_EXCESSO");
  });
  it("atividade depois de D-2 e véspera sem a Revisão final", () => {
    const p = clone(base);
    const last = p.activities.filter((a) => a.scope === "AULA").at(-1)!;
    last.week = p.weeks.length;
    last.day = 5;
    expect(codes(p)).toContain("DEPOIS_DE_D2");
    const q = clone(base);
    q.activities = q.activities.filter((a) => !a.key.endsWith("#VESPERA"));
    expect(codes(q)).toContain("VESPERA");
  });
  it("sobra de tempo com aulas pedidas fora do plano", () => {
    const p = clone(base);
    p.params.capacityHours = Math.round((p.params.capacityHours ?? 100) * 3); // o plano usa só ~1/3 da capacidade
    const t = find(p, "TEORIA");
    p.activities = p.activities.filter((a) => a.aulaId !== t.aulaId && !a.segmentIds.some((s) => s.startsWith(t.aulaId)));
    expect(codes(p)).toContain("FALTOU_AULA_SOBROU_TEMPO");
  });
  it("minutos fora da faixa, soma da semana errada e referência inexistente", () => {
    const p = clone(base);
    find(p, "TEORIA").minutes = 7;
    p.weeks[0].targetMinutes += 10;
    find(p, "REVISAO").refKeys = ["nao/existe#T1"];
    const c = codes(p);
    expect(c).toContain("MINUTOS_FORA_DA_FAIXA");
    expect(c).toContain("SEMANA_SOMA");
    expect(c).toContain("REF_INEXISTENTE");
  });
  it("Turbo: atividade de resumo sem Turbo pedido ou sem resumo disponível; bloco com Questões antes da Revisão", () => {
    const turbo = build(21, 1, { turbo: true });
    const p = clone(turbo);
    p.request.turbo = false;
    expect(codes(p)).toContain("TURBO_NAO_PEDIDO");
    const s = clone(turbo);
    const resumo = s.activities.find((a) => a.turbo)!;
    const small: VerifyContext = { ...ctx, summaries: new Set(allSummaries.filter((id) => !resumo.segmentIds.includes(id))) };
    expect(verifyPlan(s, small).errors.map((e) => e.code)).toContain("RESUMO_INEXISTENTE");
    const b = clone(turbo);
    const bq = b.activities.find((a) => a.type === "QUESTOES" && /#SQ\d*$/.test(a.key))!;
    const sr = b.activities.find((a) => a.type === "TEORIA" && a.turbo && bq.refKeys.includes(a.key))!;
    bq.week = sr.week;
    bq.day = sr.day;
    expect(codes(b)).toContain("CADERNO_NO_DIA_DA_TEORIA");
  });
  it("trecho fora do edital do concurso", () => {
    const p = clone(base);
    const t = find(p, "TEORIA");
    const bad: VerifyContext = { ...ctx, importance: { ...importance, [t.segmentIds[0]]: null } };
    expect(verifyPlan(p, bad).errors.map((e) => e.code)).toContain("FORA_DO_EDITAL");
  });
  it("relatório traz veredito, motivos e estatísticas", () => {
    const p = clone(base);
    find(p, "TEORIA").minutes = 7;
    const r = verifyPlan(p, ctx);
    expect(r.verdict).toBe("BLOQUEAR");
    expect(r.errors[0].message.length).toBeGreaterThan(10);
    expect(r.stats.atividades).toBe(p.activities.length);
  });
});
