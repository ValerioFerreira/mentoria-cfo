// Motor de planejamento: gera as metas semanais (e a divisão por dias) a partir das escolhas do aluno.
import { computeCoverage, gapWarnings } from "./coverage";
import { CONTENT_ENDS_DAYS_BEFORE_EXAM, EXAM_TOTAL_QUESTIONS, MAX_SELECTION_EFFICIENCY, PACKING_EFFICIENCY, WEEKLY_SLACK } from "./constants";
import { addDays, diffDays, nextMonday, weekday, weeksUntil } from "./dates";
import { calendarCapacity, scheduleCalendar } from "./days";
import { buildEveReview, buildSpareReview, type ReviewSubject } from "./review";
import { buildSubjectQueue } from "./schedule";
import { selectContent, type SelectedSubject } from "./select";
import type { ContestCoverage, Known, PlanInput, PlanResult, PlannedActivity, PlannedWeek } from "./types";

export * from "./types";
export { nextMonday, mondayOf, dayIndexOf } from "./dates";
export { hoursPerDayLabel, bandOf } from "./bands";

export class PlanInputError extends Error {}

function validate(input: PlanInput): void {
  if (input.subjects.length === 0) throw new PlanInputError("Escolha ao menos uma disciplina.");
  if (input.combo) {
    const { members, priority } = input.combo;
    if (members.length !== 2 || !members.some((m) => m.contest === priority)) throw new PlanInputError("Combo inválido: escolha qual concurso é a prioridade.");
  }
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

/**
 * Gera o plano. No Modo Turbo o objetivo é completar o edital: se, por qualquer razão (poucos resumos, encaixe), o plano com Turbo
 * cobrir MENOS do que o plano normal, vale o normal, e o aviso diz que o Turbo não trouxe ganho.
 */
export function generatePlan(input: PlanInput): PlanResult {
  const plan = generatePlanOnce(input);
  if (!input.turbo || plan.params.summaryUnits === 0) return plan;
  const normal = generatePlanOnce({ ...input, turbo: false });
  if (normal.params.editalFits) return normal; // o edital já cabe sem resumos: o Turbo não tem o que trocar
  if (plan.coverage.selected + 1e-9 >= normal.coverage.selected) return plan;
  return { ...normal, warnings: ["Modo Turbo: com os resumos disponíveis hoje ele não aumentaria a cobertura do edital, então o plano foi montado no modo normal.", ...normal.warnings] };
}

function generatePlanOnce(input: PlanInput): PlanResult {
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
      contest: input.contest,
      members: input.combo?.members.map((m) => m.contest),
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
      // peso do concurso do aluno (ou do combo); o do catálogo é o do CBMPE Oficial
      examQuestions: input.examQuestions?.[subject.id] ?? subject.examQuestions,
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

  const coverage = input.combo
    ? comboCoverage(chosen, sel, known, input.combo, input.examQuestions ?? {})
    : computeCoverage(chosen, sel, known, input.examQuestions ? { examQuestions: input.examQuestions, editalTotal: input.examTotalQuestions ?? EXAM_TOTAL_QUESTIONS } : undefined);
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
      request: {
        hoursPerWeek: input.hoursPerWeek,
        turbo: input.turbo === true,
        firstDay: firstOrd,
        ...(input.contest ? { contest: input.contest } : {}),
        ...(input.combo ? { combo: { contests: input.combo.members.map((m) => m.contest), priority: input.combo.priority } } : {}),
        subjects: input.subjects.map((s) => ({ id: s.id, level: s.level })),
        known: Object.fromEntries(Object.entries(known).filter(([, v]) => v > 0)) as Record<string, Known>,
        excludedAulas: [...excludedAulas],
      },
      turbo: input.turbo === true,
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

/** Cobertura do combo: o geral usa o peso combinado (W); cada prova é detalhada com as questões e o total dela. */
function comboCoverage(chosen: SelectedSubject[], sel: ReturnType<typeof selectContent>, known: Record<string, Known>, combo: NonNullable<PlanInput["combo"]>, weightedQuestions: Record<string, number>) {
  const editalTotal = combo.members.reduce((n, m) => n + m.weight * m.totalQuestions, 0);
  const cov = computeCoverage(chosen, sel, known, { examQuestions: weightedQuestions, editalTotal });
  const contests: ContestCoverage[] = combo.members.map((m) => {
    const rows = cov.subjects
      .map((s) => ({ subjectId: s.subjectId, examQuestions: m.examQuestions[s.subjectId] ?? 0, coverage: s.coverage }))
      .filter((r) => r.examQuestions > 0);
    const pts = rows.reduce((n, r) => n + r.examQuestions, 0);
    const covPts = rows.reduce((n, r) => n + r.examQuestions * r.coverage, 0);
    return { contest: m.contest, weight: m.weight, selected: pts > 0 ? covPts / pts : 0, edital: covPts / m.totalQuestions, subjects: rows };
  });
  return { ...cov, contests };
}

export { EXAM_TOTAL_QUESTIONS };
export function defaultStart(todayIso: string): string {
  return nextMonday(todayIso);
}
