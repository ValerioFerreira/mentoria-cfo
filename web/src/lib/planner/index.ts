// Motor de planejamento: gera as metas semanais (e a divisão por dias) a partir das escolhas do aluno.
import { computeCoverage, gapWarnings } from "./coverage";
import { EXAM_TOTAL_QUESTIONS, FINAL_REVIEW_WEEKS, MIN_FINAL_REVIEW_WEEKS, PACKING_EFFICIENCY, WEEKLY_SLACK } from "./constants";
import { addDays, dayIndexOf, nextMonday, weekday, weeksUntil } from "./dates";
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
  const weeklyMinutes = Math.max(60, Math.floor(input.hoursPerWeek * 60 * slack));
  const totalWeeks = weeksUntil(input.startDate, input.examDate);
  const firstDay = input.firstDay ?? 0;
  const known = input.known ?? {};
  const chosen: SelectedSubject[] = input.subjects.map((s) => ({
    subject: input.catalog.subjects.find((x) => x.id === s.id)!,
    level: s.level,
  }));
  // a semana em que o aluno começa no meio vale só os dias que restam
  const capacityOf = (finalWeeks: number) => {
    const reviewWeeksMin = Math.min(finalWeeks, totalWeeks - 1);
    const contentWeeks = totalWeeks - reviewWeeksMin;
    return { contentWeeks, capacityMinutes: Math.round((contentWeeks - 1 + weekFraction(firstDay)) * weeklyMinutes) };
  };
  const focus = input.hoursPerWeek <= 21 ? 3 : input.hoursPerWeek <= 28 ? 4 : 5;
  // Seleciona o conteúdo e o distribui nas semanas. `eff` é a fração da capacidade que a seleção pode ocupar
  // (o encaixe nunca é perfeito); se mesmo assim sobrar atividade sem semana, repete com menos.
  const attempt = (fw: number, eff: number) => {
    const cap = capacityOf(fw);
    const sel = selectContent(chosen, input.segments, Math.round(cap.capacityMinutes * eff), known);
    // filas por disciplina: ciclos das aulas selecionadas na ordem do curso
    const streams: StreamInfo[] = chosen.map(({ subject }) => {
      const queue = subject.aulas
        .filter((a) => sel.tierByAula.has(a.id))
        .sort((a, b) => a.number - b.number)
        .flatMap((a) => buildAulaCycle(sel.blueprints.get(a.id)!, sel.tierByAula.get(a.id)!));
      return { subjectId: subject.id, examQuestions: subject.examQuestions, sortOrder: subject.sortOrder, queue };
    });
    const queued = streams.reduce((n, s) => n + s.queue.length, 0);
    const schedule = scheduleStreams(streams.filter((s) => s.queue.length > 0), weeklyMinutes, cap.contentWeeks, input.startDate, focus, firstDay);
    const leftover = queued - schedule.reduce((n, w) => n + w.activities.length, 0);
    return { cap, sel, schedule, leftover };
  };
  // Revisão final: 2 semanas por padrão. Se o tempo não bastar para VER o edital inteiro (só Teoria + Questões),
  // a revisão encolhe até o piso e a semana volta a ser conteúdo: cobrir o edital vale mais do que revisá-lo.
  const explicitFinal = input.finalReviewWeeks;
  let finalWeeks = explicitFinal ?? FINAL_REVIEW_WEEKS;
  let eff = PACKING_EFFICIENCY;
  let cur = attempt(finalWeeks, eff);
  while (explicitFinal === undefined && finalWeeks > MIN_FINAL_REVIEW_WEEKS && cur.sel.fullMinutes > cur.cap.capacityMinutes * eff) {
    finalWeeks--;
    cur = attempt(finalWeeks, eff);
  }
  for (let guard = 0; cur.leftover > 0 && guard < 8; guard++) {
    eff -= 0.02;
    cur = attempt(finalWeeks, eff);
  }
  const { sel, schedule: contentSchedule } = cur;
  const { contentWeeks, capacityMinutes } = cur.cap;

  // semanas de revisão: as finais + qualquer folga que sobrou (inclui as aulas que o aluno já domina)
  // só entram trechos que tiveram Teoria agendada (ou aulas que o aluno domina)
  const studied = new Set(contentSchedule.flatMap((w) => w.activities.filter((a) => a.type === "TEORIA").flatMap((a) => a.segmentIds)));
  const reviewSubjects: ReviewSubject[] = chosen.map(({ subject }) => {
    const aulas = subject.aulas
      .filter((a) => sel.tierByAula.has(a.id) || sel.mastered.has(a.id))
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
  const reviewWeeks = buildReviewWeeks({
    firstIndex: contentSchedule.length + 1,
    lastIndex: totalWeeks,
    startDate: input.startDate,
    weeklyMinutes,
    subjects: reviewSubjects,
    firstDay,
  });
  const weeks: PlannedWeek[] = [...contentSchedule, ...reviewWeeks];
  // nada é agendado no dia da prova nem depois dela: a última semana termina na véspera
  const examDay = dayIndexOf(input.examDate);
  const lastWeek = weeks[weeks.length - 1];
  if (lastWeek && examDay > 0) {
    lastWeek.activities = lastWeek.activities.map((a) => (a.day !== undefined && a.day >= examDay ? { ...a, day: examDay - 1 } : a));
  }

  const coverage = computeCoverage(chosen, sel, known);
  const warnings: string[] = [];
  if (explicitFinal === undefined && finalWeeks < FINAL_REVIEW_WEEKS) {
    warnings.push("Para ver o edital inteiro no tempo disponível, a revisão final foi reduzida a 1 semana; as revisões ficam para o que sobrar.");
  }
  if (sel.floorShortfall) warnings.push("O tempo disponível não cobre nem uma aula essencial de cada disciplina; priorizamos as de maior peso na prova.");
  warnings.push(...gapWarnings(input.catalog, input.subjects.map((s) => s.id)));

  const plannedMinutes = contentSchedule.reduce((n, w) => n + w.targetMinutes, 0);
  // horas por semana para VER o edital inteiro (só Teoria + Questões), com a revisão final no piso
  const closing = capacityOf(explicitFinal ?? MIN_FINAL_REVIEW_WEEKS);
  const fullEditalHoursPerWeek = Math.ceil(sel.fullMinutes / 60 / (closing.contentWeeks - 1 + weekFraction(firstDay)) / slack / PACKING_EFFICIENCY);
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
