// Motor de planejamento: gera as metas semanais (e a divisão por dias) a partir das escolhas do aluno.
import { computeCoverage, gapWarnings } from "./coverage";
import { EXAM_TOTAL_QUESTIONS, FINAL_REVIEW_WEEKS, WEEKLY_SLACK } from "./constants";
import { addDays, nextMonday, weekday, weeksUntil } from "./dates";
import { weekFraction } from "./days";
import { buildReviewWeeks, type ReviewSubject } from "./review";
import { buildAulaCycle, scheduleStreams, type StreamInfo } from "./schedule";
import { selectContent, type SelectedSubject } from "./select";
import type { PlanInput, PlanResult, PlannedWeek } from "./types";

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
  const finalWeeks = input.finalReviewWeeks ?? FINAL_REVIEW_WEEKS;
  const weeklyMinutes = Math.max(60, Math.floor(input.hoursPerWeek * 60 * slack));
  const totalWeeks = weeksUntil(input.startDate, input.examDate);
  const reviewWeeksMin = Math.min(finalWeeks, totalWeeks - 1);
  const contentWeeks = totalWeeks - reviewWeeksMin;
  const firstDay = input.firstDay ?? 0;
  // a semana em que o aluno começa no meio vale só os dias que restam
  const capacityMinutes = Math.round((contentWeeks - 1 + weekFraction(firstDay)) * weeklyMinutes);
  const known = input.known ?? {};

  const chosen: SelectedSubject[] = input.subjects.map((s) => ({
    subject: input.catalog.subjects.find((x) => x.id === s.id)!,
    level: s.level,
  }));
  const sel = selectContent(chosen, input.segments, capacityMinutes, known);

  // filas por disciplina: ciclos das aulas selecionadas na ordem do curso
  const streams: StreamInfo[] = chosen.map(({ subject }) => {
    const queue = subject.aulas
      .filter((a) => sel.tierByAula.has(a.id))
      .sort((a, b) => a.number - b.number)
      .flatMap((a) => buildAulaCycle(sel.blueprints.get(a.id)!, sel.tierByAula.get(a.id)!));
    return { subjectId: subject.id, examQuestions: subject.examQuestions, sortOrder: subject.sortOrder, queue };
  });
  const focus = input.hoursPerWeek <= 21 ? 3 : input.hoursPerWeek <= 28 ? 4 : 5;
  const contentSchedule = scheduleStreams(streams.filter((s) => s.queue.length > 0), weeklyMinutes, contentWeeks, input.startDate, focus, firstDay);

  // semanas de revisão: as finais + qualquer folga que sobrou (inclui as aulas que o aluno já domina)
  const reviewSubjects: ReviewSubject[] = chosen.map(({ subject }) => {
    const aulas = subject.aulas
      .filter((a) => sel.tierByAula.has(a.id) || sel.mastered.has(a.id))
      .sort((a, b) => b.incidence - a.incidence);
    return {
      subjectId: subject.id,
      examQuestions: subject.examQuestions,
      sortOrder: subject.sortOrder,
      segments: aulas.flatMap((a) => (input.segments[a.id] ?? []).map((s) => ({ id: s.id, aulaId: a.id }))),
    };
  });
  const reviewWeeks = buildReviewWeeks({
    firstIndex: contentSchedule.length + 1,
    lastIndex: totalWeeks,
    startDate: input.startDate,
    weeklyMinutes,
    subjects: reviewSubjects,
    firstDay,
  });
  const weeks: PlannedWeek[] = [...contentSchedule, ...reviewWeeks];

  const coverage = computeCoverage(chosen, sel, known);
  const warnings: string[] = [];
  if (sel.floorShortfall) warnings.push("O tempo disponível não cobre nem uma aula essencial de cada disciplina; priorizamos as de maior peso na prova.");
  warnings.push(...gapWarnings(input.catalog, input.subjects.map((s) => s.id)));

  const plannedMinutes = contentSchedule.reduce((n, w) => n + w.targetMinutes, 0);
  const fullEditalHoursPerWeek = Math.ceil(sel.fullMinutes / 60 / (contentWeeks - 1 + weekFraction(firstDay)) / slack);
  return {
    params: {
      hoursPerWeek: input.hoursPerWeek,
      slotsPerWeek: Math.round((weeklyMinutes / 60) * 10) / 10,
      weeklyMinutes,
      totalWeeks,
      contentWeeks,
      reviewWeeks: totalWeeks - contentSchedule.length,
      capacityHours: Math.round(capacityMinutes / 60),
      plannedHours: Math.round(plannedMinutes / 60),
      fullEditalHoursPerWeek,
      startDate: input.startDate,
      firstStudyDate: addDays(input.startDate, firstDay),
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
