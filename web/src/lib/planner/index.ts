// Motor de planejamento: gera as metas semanais (e a divisão por dias) a partir das escolhas do aluno.
import { computeCoverage, gapWarnings } from "./coverage";
import { CONTENT_ENDS_DAYS_BEFORE_EXAM, EXAM_TOTAL_QUESTIONS, MAX_SELECTION_EFFICIENCY, PACKING_EFFICIENCY, WEEKLY_SLACK } from "./constants";
import { addDays, diffDays, nextMonday, weekday, weeksUntil } from "./dates";
import { calendarCapacity, scheduleCalendar } from "./days";
import { buildEveReview, buildSpareReview, type ReviewSubject } from "./review";
import { buildSubjectQueue } from "./schedule";
import { selectContent, type SelectedSubject } from "./select";
import type { PlanInput, PlanResult, PlannedActivity, PlannedWeek } from "./types";

export * from "./types";
export { nextMonday, mondayOf, dayIndexOf } from "./dates";
export { hoursPerDayLabel, bandOf } from "./bands";

export class PlanInputError extends Error {}

function validate(input: PlanInput): void {
  if (input.subjects.length === 0) throw new PlanInputError("Escolha ao menos uma disciplina.");
  if (!(input.hoursPerWeek >= 5 && input.hoursPerWeek <= 80)) throw new PlanInputError("Horas por semana fora do intervalo (5–80).");
  if (weekday(input.startDate) !== 1) throw new PlanInputError("A data de início do plano deve ser uma segunda-feira.");
  const fd = input.firstDay ?? 0;
  if (!Number.isInteger(fd) || fd < 0 || fd > 6) throw new PlanInputError("Dia de início inválido.");
  if (weeksUntil(input.startDate, input.examDate) < 2) throw new PlanInputError("A data da prova está muito próxima para montar um plano.");
  if (diffDays(input.startDate, input.examDate) - CONTENT_ENDS_DAYS_BEFORE_EXAM < fd) throw new PlanInputError("A data da prova está muito próxima para montar um plano.");
  const byGroup = new Map<string, number>();
  for (const sel of input.subjects) {
    const subj = input.catalog.subjects.find((s) => s.id === sel.id);
    if (!subj) throw new PlanInputError(`Disciplina desconhecida: ${sel.id}`);
    if (subj.languageGroup) byGroup.set(subj.languageGroup, (byGroup.get(subj.languageGroup) ?? 0) + 1);
  }
  for (const [group, n] of byGroup) {
    if (n > 1) throw new PlanInputError(`Escolha apenas uma língua estrangeira (${group}): Inglês ou Espanhol.`);
  }
}

export function generatePlan(input: PlanInput): PlanResult {
  validate(input);
  const slack = input.slack ?? WEEKLY_SLACK;
  const weeklyMinutes = Math.max(60, Math.floor(input.hoursPerWeek * 60 * slack));
  const totalWeeks = weeksUntil(input.startDate, input.examDate);
  const firstOrd = input.firstDay ?? 0;
  // O conteúdo corre até D-2; a véspera (D-1) tem uma única Revisão. Os dias contam desde a segunda da semana 1.
  const examOrd = diffDays(input.startDate, input.examDate);
  const lastOrd = examOrd - CONTENT_ENDS_DAYS_BEFORE_EXAM;
  const eveOrd = examOrd - 1;
  const known = input.known ?? {};
  const excludedAulas = new Set(input.excludedAulas ?? []);
  const chosen: SelectedSubject[] = input.subjects.map((s) => ({
    subject: input.catalog.subjects.find((x) => x.id === s.id)!,
    level: s.level,
  }));
  const capacityMinutes = Math.round(calendarCapacity(weeklyMinutes, firstOrd, lastOrd));

  // Seleciona o conteúdo e o agenda dia a dia. `eff` é a fração da capacidade que a seleção pode ocupar
  // (o encaixe e as folgas entre as etapas do ciclo nunca são perfeitos); se sobrar atividade sem dia, repete com menos.
  const attempt = (eff: number) => {
    const sel = selectContent(chosen, input.segments, Math.round(capacityMinutes * eff), known, input.turbo === true, excludedAulas, {
      importance: input.importance,
      summaries: input.summaries ? new Set(input.summaries) : undefined,
      examQuestions: input.examQuestions,
    });
    // filas por disciplina: ciclos das aulas selecionadas na ordem do curso (e blocos de resumo, no Turbo)
    const streams = chosen.map(({ subject }) => {
      const queue = buildSubjectQueue(
        subject.aulas
          .filter((a) => !excludedAulas.has(a.id) && sel.tierByAula.has(a.id))
          .sort((a, b) => a.number - b.number)
          .map((a) => ({ bp: sel.blueprints.get(a.id)!, tier: sel.tierByAula.get(a.id)! })),
      );
      return { subjectId: subject.id, examQuestions: input.examQuestions?.[subject.id] ?? subject.examQuestions, sortOrder: subject.sortOrder, queue };
    });
    const cal = scheduleCalendar(streams, { weeklyMinutes, firstOrd, lastOrd });
    return { sel, cal };
  };
  // Maior fração da capacidade com que o conteúdo selecionado cabe por inteiro (busca binária: o resultado é determinístico).
  let eff = MAX_SELECTION_EFFICIENCY;
  let cur = attempt(eff);
  if (cur.cal.leftover > 0) {
    let lo = 0.4;
    let hi = eff;
    let best: ReturnType<typeof attempt> | null = null;
    for (let i = 0; i < 9; i++) {
      const mid = (lo + hi) / 2;
      const r = attempt(mid);
      if (r.cal.leftover === 0) {
        lo = mid;
        best = r;
      } else hi = mid;
    }
    eff = lo;
    cur = best ?? attempt(lo);
  }
  const { sel, cal } = cur;

  // revisões fora do ciclo: só entram trechos que tiveram Teoria agendada (ou aulas que o aluno domina)
  const studied = new Set([...cal.days.values()].flat().filter((a) => a.type === "TEORIA").flatMap((a) => a.segmentIds));
  const reviewSubjects: ReviewSubject[] = chosen.map(({ subject }) => {
    const aulas = subject.aulas
      .filter((a) => !excludedAulas.has(a.id) && (sel.tierByAula.has(a.id) || sel.mastered.has(a.id)))
      .sort((a, b) => b.incidence - a.incidence);
    return {
      subjectId: subject.id,
      examQuestions: subject.examQuestions,
      sortOrder: subject.sortOrder,
      segments: aulas.flatMap((a) =>
        (input.segments[a.id] ?? []).filter((s) => sel.mastered.has(a.id) || studied.has(s.id)).map((s) => ({ id: s.id, aulaId: a.id })),
      ),
    };
  });
  // dias que sobraram depois de todo o conteúdo: revisão geral + cadernos mistos
  const days = new Map(cal.days);
  const spare = buildSpareReview({ fromOrd: Math.max(firstOrd, cal.lastContentOrd + 1), toOrd: lastOrd, weeklyMinutes, subjects: reviewSubjects });
  for (const [ord, acts] of spare) days.set(ord, acts);
  const eve = buildEveReview(reviewSubjects, eveOrd);
  if (eve) days.set(eveOrd, [eve]);

  // semanas: da 1ª até a que contém a véspera da prova
  const lastWeek = Math.floor(eveOrd / 7) + 1;
  const weeks: PlannedWeek[] = [];
  for (let w = 1; w <= lastWeek; w++) {
    const activities: PlannedActivity[] = [];
    for (let d = (w - 1) * 7; d < w * 7; d++) activities.push(...(days.get(d) ?? []));
    weeks.push({
      index: w,
      startDate: addDays(input.startDate, (w - 1) * 7),
      kind: activities.some((a) => a.scope !== "FINAL") ? "CONTENT" : "FINAL_REVIEW",
      targetMinutes: activities.reduce((n, a) => n + a.minutes, 0),
      activities,
    });
  }
  const contentWeeks = weeks.reduce((n, w) => (w.kind === "CONTENT" ? w.index : n), 0);

  const coverage = computeCoverage(chosen, sel, known);
  const warnings: string[] = [];
  if (sel.turboAulas.size > 0) {
    warnings.push(`Modo Turbo: ${[...sel.tierByAula.keys()].reduce((n, id) => n + sel.blueprints.get(id)!.summary.length, 0)} assuntos de menor importância no concurso serão estudados por resumo analítico para você ver mais do edital no tempo disponível.`);
  }
  if (sel.floorShortfall) warnings.push("O tempo disponível não cobre nem uma aula do ciclo mínimo de cada disciplina; priorizamos as de maior peso na prova.");
  warnings.push(...gapWarnings(input.catalog, input.subjects.map((s) => s.id)));

  const plannedMinutes = weeks.reduce((n, w) => n + w.activities.filter((a) => a.scope !== "FINAL").reduce((m, a) => m + a.minutes, 0), 0);
  // horas por semana para fechar o ciclo mínimo de TODAS as aulas (Teoria + Revisão curta + Questões)
  const fullEditalHoursPerWeek = Math.ceil(sel.fullMinutes / 60 / (capacityMinutes / weeklyMinutes) / slack / Math.min(eff, PACKING_EFFICIENCY));
  return {
    params: {
      hoursPerWeek: input.hoursPerWeek,
      slotsPerWeek: Math.round((weeklyMinutes / 60) * 10) / 10,
      weeklyMinutes,
      totalWeeks,
      contentWeeks,
      reviewWeeks: totalWeeks - contentWeeks,
      capacityHours: Math.round(capacityMinutes / 60),
      plannedHours: Math.round(plannedMinutes / 60),
      fullEditalHoursPerWeek,
      editalFits: [...sel.blueprints.keys()].every((id) => sel.tierByAula.has(id)) && sel.turboAulas.size === 0,
      turboAulas: sel.turboAulas.size,
      summaryUnits: [...sel.tierByAula.keys()].reduce((n, id) => n + sel.blueprints.get(id)!.summary.length, 0),
      startDate: input.startDate,
      firstStudyDate: addDays(input.startDate, firstOrd),
      examDate: input.examDate,
    },
    weeks,
    coverage,
    warnings,
  };
}

export { EXAM_TOTAL_QUESTIONS };
export function defaultStart(todayIso: string): string {
  return nextMonday(todayIso);
}
