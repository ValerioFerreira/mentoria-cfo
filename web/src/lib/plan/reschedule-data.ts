// Liga o motor da reprogramação (lib/planner/reschedule.ts, puro) ao banco: carrega o plano ACTIVE do aluno, calcula a prévia e,
// ao aplicar, grava os movimentos. As server actions (reschedule-actions.ts) são só a casca de autenticação e validação.
import { db } from "@/lib/db";
import { activityDetail } from "@/lib/activity-detail";
import { addDaysISO, diffDaysISO, firstStudyISO, todayISO } from "@/lib/plan-time";
import { planReschedule, type EngineActivity, type EngineResult } from "@/lib/planner/reschedule";
import type {
  OverdueActivity, RescheduleApplied, RescheduleError, RescheduleInput, ReschedulePreview, RescheduleWarning,
} from "@/lib/planner/reschedule-types";

const ymd = (d: Date) => d.toISOString().slice(0, 10);
const RECENT_DAYS = 14;
const DELAY_SHARE = 0.5;
const err = (error: string): RescheduleError => ({ ok: false, error });

type Row = Awaited<ReturnType<typeof loadRows>>["rows"][number];

async function loadRows(planId: string) {
  const rows = await db.activity.findMany({
    where: { planId },
    select: {
      id: true, key: true, type: true, subjectId: true, aulaId: true, plannedMinutes: true, status: true, scope: true, turbo: true,
      dayIndex: true, sortOrder: true, weekId: true, quizQuestions: true, fixRanges: true, rescheduledAt: true,
      subject: { select: { name: true } },
      aula: { select: { shortTitle: true } },
      refs: { select: { refActivity: { select: { key: true } } } },
      segments: { select: { segmentId: true, segment: { select: { startTopic: true, sortOrder: true } } } },
    },
  });
  return { rows };
}

export interface Scenario {
  plan: { id: string; params: Record<string, unknown>; contest: string | null };
  startIso: string;
  todayOrd: number;
  firstOrd: number;
  lastContentOrd: number;
  eveOrd: number;
  weeklyMinutes: number;
  weekIdByIndex: Map<number, string>;
  rows: Row[];
  engine: EngineActivity[];
  rowById: Map<string, Row>;
  ordOf: Map<string, number>;
  /** atrasadas: pendentes de aula em dia anterior a hoje */
  overdueIds: Set<string>;
}

/** Carrega o plano ACTIVE do aluno em "dias do plano". Erro legível quando não dá para reprogramar. */
export async function loadScenario(userId: string, now: Date = new Date()): Promise<Scenario | RescheduleError> {
  const plan = await db.plan.findFirst({
    where: { userId, status: "ACTIVE" },
    select: { id: true, startDate: true, examDate: true, params: true, contest: true, weeks: { select: { id: true, index: true } } },
  });
  if (!plan) return err("Você não tem um plano ativo para reprogramar.");
  const params = (plan.params as Record<string, unknown>) ?? {};
  const startIso = ymd(plan.startDate);
  const today = todayISO(now);
  const todayOrd = diffDaysISO(startIso, today);
  const examOrd = diffDaysISO(startIso, ymd(plan.examDate));
  const firstOrd = Math.max(0, diffDaysISO(startIso, firstStudyISO(plan)));
  const weeklyMinutes = Number(params.weeklyMinutes) > 0 ? Number(params.weeklyMinutes) : Math.max(60, Math.round(Number(params.hoursPerWeek ?? 0) * 60));
  if (!(weeklyMinutes > 0)) return err("Não foi possível ler a meta semanal deste plano.");
  const { rows } = await loadRows(plan.id);
  if (rows.some((r) => r.dayIndex === null)) return err("Este plano é antigo (sem dia marcado em cada atividade) e não permite reprogramar. Refaça o plano para usar este recurso.");
  const weekIndex = new Map(plan.weeks.map((w) => [w.id, w.index]));
  const ordOf = new Map(rows.map((r) => [r.id, (weekIndex.get(r.weekId)! - 1) * 7 + r.dayIndex!]));
  const engine: EngineActivity[] = rows.map((r) => ({
    id: r.id, key: r.key, type: r.type, subjectId: r.subjectId, aulaId: r.aulaId, minutes: r.plannedMinutes, ord: ordOf.get(r.id)!, sortOrder: r.sortOrder,
    // atividade dispensada na reprogramação (SKIPPED com rescheduledAt) sai do plano; as demais SKIPPED (dispensa normal) contam como feitas
    status: r.status, scope: r.scope, turbo: r.turbo, refKeys: r.refs.map((x) => x.refActivity.key),
  }));
  const overdueIds = new Set(engine.filter((a) => (a.status === "PENDING" || a.status === "IN_PROGRESS") && a.scope === "AULA" && a.ord < todayOrd).map((a) => a.id));
  return {
    plan: { id: plan.id, params, contest: plan.contest }, startIso, todayOrd, firstOrd, lastContentOrd: examOrd - 2, eveOrd: examOrd - 1, weeklyMinutes,
    weekIdByIndex: new Map(plan.weeks.map((w) => [w.index, w.id])), rows, engine, rowById: new Map(rows.map((r) => [r.id, r])), ordOf, overdueIds,
  };
}

export const isScenario = (x: Scenario | RescheduleError): x is Scenario => !("ok" in x);

/** Fixação e caderno só dizem "questões comentadas"/"caderno de N questões": o assunto vem da aula. */
const titleOf = (r: Row): string => {
  const detail = activityDetail({ type: r.type, scope: r.scope, fixRanges: r.fixRanges, quizQuestions: r.quizQuestions, segments: r.segments });
  if (r.scope === "FINAL") return detail ?? r.aula.shortTitle;
  return detail && (r.type === "FIXACAO" || r.type === "QUESTOES") ? `${r.aula.shortTitle} · ${detail}` : (detail ?? r.aula.shortTitle);
};

/** As atividades atrasadas do aluno, na ordem do plano (para a lista do passo 1). */
export function overdueOf(sc: Scenario): OverdueActivity[] {
  return [...sc.overdueIds]
    .map((id) => sc.rowById.get(id)!)
    .sort((a, b) => sc.ordOf.get(a.id)! - sc.ordOf.get(b.id)! || a.sortOrder - b.sortOrder)
    .map((r) => ({
      id: r.id, title: titleOf(r), subjectName: r.subject.name, type: r.type, plannedMinutes: r.plannedMinutes,
      date: addDaysISO(sc.startIso, sc.ordOf.get(r.id)!), status: r.status as "PENDING" | "IN_PROGRESS",
    }));
}

async function importanceByAula(sc: Scenario): Promise<Record<string, number> | undefined> {
  const aulas = [...new Set(sc.rows.map((r) => r.aulaId))];
  const rows = await db.segmentImportance.findMany({
    where: { contest: (sc.plan.contest ?? "CBMPE_OFICIAL") as never, segment: { aulaId: { in: aulas } }, appears: true },
    select: { score: true, segment: { select: { aulaId: true } } },
  });
  if (!rows.length) return undefined;
  const acc = new Map<string, number[]>();
  for (const r of rows) if (r.score !== null) acc.set(r.segment.aulaId, [...(acc.get(r.segment.aulaId) ?? []), r.score]);
  return Object.fromEntries([...acc].map(([a, v]) => [a, v.reduce((x, y) => x + y, 0) / v.length]));
}

export interface Computed {
  sc: Scenario;
  result: EngineResult;
  importance?: Record<string, number>;
}

/** Roda o motor sobre as atividades escolhidas. Erro legível para escolha inválida. */
export async function compute(sc: Scenario, input: RescheduleInput): Promise<Computed | RescheduleError> {
  const ids = [...new Set(input.activityIds)];
  if (ids.length === 0) return err("Escolha ao menos uma atividade atrasada.");
  if (ids.some((id) => !sc.overdueIds.has(id))) return err("Só atividades atrasadas e pendentes podem ser reprogramadas. Atualize a página e escolha de novo.");
  if (sc.todayOrd > sc.lastContentOrd) return err("O plano já está na reta final (véspera da prova): não há mais dias para reprogramar.");
  let targetOrd: number | undefined;
  if (input.params.option === "MOVE_TO_DAY") {
    if (!input.params.targetDate) return err("Escolha o dia para onde levar as atividades.");
    targetOrd = diffDaysISO(sc.startIso, input.params.targetDate);
    if (targetOrd < Math.max(sc.todayOrd, sc.firstOrd) || targetOrd > sc.lastContentOrd) return err("O dia escolhido precisa estar entre hoje e dois dias antes da prova.");
  }
  const importance = input.params.option === "RECALC_REST" ? await importanceByAula(sc) : undefined;
  const result = planReschedule({
    activities: sc.engine, weeklyMinutes: sc.weeklyMinutes, todayOrd: sc.todayOrd, firstOrd: sc.firstOrd, lastContentOrd: sc.lastContentOrd, eveOrd: sc.eveOrd,
    selectedIds: ids, params: input.params, targetOrd, importanceByAula: importance,
  });
  return { sc, result, importance };
}

const hm = (min: number) => (min >= 60 ? `${Math.floor(min / 60)} h${min % 60 ? ` ${min % 60} min` : ""}` : `${min} min`);

interface History {
  at: string;
}
const history = (params: Record<string, unknown>): History[] => (Array.isArray(params.reschedules) ? (params.reschedules as History[]) : []);

export function buildPreview(c: Computed, input: RescheduleInput, now: Date = new Date()): ReschedulePreview {
  const { sc, result: r } = c;
  const date = (ord: number) => addDaysISO(sc.startIso, ord);
  const row = (id: string) => sc.rowById.get(id)!;
  const base = (id: string) => ({ id, title: titleOf(row(id)), subjectName: row(id).subject.name, plannedMinutes: row(id).plannedMinutes });
  const typeOf = (id: string) => row(id).type as OverdueActivity["type"];
  const moves = r.placements
    .map((p) => ({
      ...base(p.id), type: typeOf(p.id), fromDate: date(p.fromOrd), toDate: date(p.toOrd), reason: p.reason,
      ...(p.causedById ? { dependsOnTitle: titleOf(row(p.causedById)) } : {}),
    }))
    .sort((a, b) => a.toDate.localeCompare(b.toDate) || a.title.localeCompare(b.title));
  const importanceOf = (id: string) => c.importance?.[row(id).aulaId] ?? null;
  const doesNotFit = r.doesNotFit.map((id) => ({ ...base(id), importance: importanceOf(id) })).sort((a, b) => (a.importance ?? 50) - (b.importance ?? 50));
  const yielded = r.yielded.map((id) => ({ ...base(id), importance: null }));

  const warnings: RescheduleWarning[] = [];
  const over = r.warnings.filter((w) => w.code === "OVER_DAY_TARGET");
  if (over.length) warnings.push({ code: "OVER_DAY_TARGET", message: `${over.length} ${over.length === 1 ? "dia passa" : "dias passam"} da meta de estudo (no pior, ${hm(Math.max(...over.map((w) => w.minutes ?? 0)))} a mais).` });
  const overSubj = r.warnings.filter((w) => w.code === "OVER_SUBJECT_DAY");
  if (overSubj.length) warnings.push({ code: "OVER_SUBJECT_DAY", message: `Em ${overSubj.length} ${overSubj.length === 1 ? "dia" : "dias"}, uma disciplina passa de 2 horas.` });
  for (const w of r.warnings) {
    if (w.code === "SPARE_REVIEW_YIELDED") warnings.push({ code: w.code, message: `${w.count} ${w.count === 1 ? "revisão geral de sobra cede o lugar e sairá" : "revisões gerais de sobra cedem o lugar e sairão"} do plano.` });
    else if (w.code === "COVERAGE_IMPACT") warnings.push({ code: w.code, message: `Dispensar ${w.count} ${w.count === 1 ? "atividade" : "atividades"} (${hm(w.minutes ?? 0)}) tira esse conteúdo do plano e reduz a cobertura do edital.` });
    else if (w.code === "MANY_DEPENDENTS") warnings.push({ code: w.code, message: `A reprogramação desloca ${w.count} atividades seguintes, mais de 30% do que ainda falta no plano.` });
    else if (w.code === "DOES_NOT_FIT") {
      warnings.push({
        code: w.code,
        message: r.noFitLeavesPlan
          ? `${w.count} ${w.count === 1 ? "atividade não cabe até a véspera da prova e sairá" : "atividades não cabem até a véspera da prova e sairão"} do plano. Saem primeiro as de menor importância para o concurso.`
          : `${w.count} ${w.count === 1 ? "atividade não coube" : "atividades não couberam"} até a véspera da prova e continua${w.count === 1 ? "" : "m"} onde estava${w.count === 1 ? "" : "m"} (atrasada${w.count === 1 ? "" : "s"}).`,
      });
    }
  }

  // atraso recorrente: 2 reprogramações ou mais nos últimos 14 dias, ou atraso acima de 50% da meta semanal
  const since = now.getTime() - RECENT_DAYS * 86_400_000;
  const recent = history(sc.plan.params).filter((h) => new Date(h.at).getTime() >= since).length;
  const overdueMinutes = [...sc.overdueIds].reduce((n, id) => n + row(id).plannedMinutes, 0);
  const suggestRedoPlan = recent >= 2 || overdueMinutes > sc.weeklyMinutes * DELAY_SHARE;
  if (suggestRedoPlan) {
    warnings.push({
      code: "RECURRENT_DELAY",
      message: recent >= 2
        ? `Você já reprogramou ${recent} vezes nas últimas duas semanas. Talvez o plano esteja pesado para o tempo que você tem.`
        : `O atraso (${hm(overdueMinutes)}) passa de metade da sua meta semanal. Talvez o plano esteja pesado para o tempo que você tem.`,
    });
  }

  return {
    ok: true,
    option: input.params.option,
    moves,
    dismissed: r.dismissed,
    doesNotFit,
    noFitLeavesPlan: r.noFitLeavesPlan,
    yielded,
    dayLoads: r.dayLoads.map((d) => ({ date: date(d.ord), before: d.before, after: d.after, target: d.target })),
    warnings,
    dependentsMoved: r.dependentsMoved,
    dependentsShare: r.pendingCount ? r.dependentsMoved / r.pendingCount : 0,
    suggestRecalc: input.params.option !== "RECALC_REST" && (r.doesNotFit.length > 0 || (r.pendingCount > 0 && r.dependentsMoved / r.pendingCount > 0.3)),
    suggestRedoPlan,
  };
}

/** Grava o resultado numa transação: dia, ordem do dia, status, rescheduledAt, meta das semanas e o histórico em params.reschedules. */
export async function applyComputed(c: Computed, input: RescheduleInput, now: Date = new Date()): Promise<RescheduleApplied> {
  const { sc, result: r } = c;
  const leaves = new Set([...r.dismissed, ...r.yielded, ...(r.noFitLeavesPlan ? r.doesNotFit : [])]);
  const moved = new Map(r.placements.map((p) => [p.id, p.toOrd]));
  const weekOfOrd = (ord: number) => sc.weekIdByIndex.get(Math.floor(ord / 7) + 1);
  for (const [id, ord] of moved) if (!weekOfOrd(ord)) throw new Error(`Semana inexistente para a atividade ${id}.`);

  // nova posição de cada atividade (semana, dia) e ordem dentro da semana
  const pos = new Map<string, { weekId: string; day: number; ord: number }>();
  for (const row of sc.rows) {
    const ord = moved.get(row.id) ?? sc.ordOf.get(row.id)!;
    pos.set(row.id, { weekId: moved.has(row.id) ? weekOfOrd(ord)! : row.weekId, day: ord % 7, ord });
  }
  const affectedWeeks = new Set<string>([...moved.keys(), ...leaves].map((id) => pos.get(id)!.weekId));
  for (const id of moved.keys()) affectedWeeks.add(sc.rowById.get(id)!.weekId); // semana de origem também
  const updates = new Map<string, { weekId?: string; dayIndex?: number; sortOrder?: number; status?: "SKIPPED"; rescheduledAt?: Date }>();
  for (const id of moved.keys()) {
    const p = pos.get(id)!;
    updates.set(id, { ...(updates.get(id) ?? {}), weekId: p.weekId, dayIndex: p.day, rescheduledAt: now });
  }
  for (const id of leaves) updates.set(id, { ...(updates.get(id) ?? {}), status: "SKIPPED", rescheduledAt: now });

  const sortOf = new Map<string, number>();
  const weekMinutes = new Map<string, number>();
  for (const weekId of affectedWeeks) {
    const inWeek = sc.rows.filter((row) => pos.get(row.id)!.weekId === weekId);
    const byOrd = new Map<number, typeof inWeek>();
    for (const row of inWeek) byOrd.set(pos.get(row.id)!.ord, [...(byOrd.get(pos.get(row.id)!.ord) ?? []), row]);
    let i = 0;
    for (const ord of [...byOrd.keys()].sort((a, b) => a - b)) {
      const list = byOrd.get(ord)!;
      const wanted = r.order.get(ord); // ordem refeita do dia (orderDay); dias que não mudaram mantêm a ordem que tinham
      const ordered = wanted
        ? [...list].sort((a, b) => (wanted.indexOf(a.id) === -1 ? 999 : wanted.indexOf(a.id)) - (wanted.indexOf(b.id) === -1 ? 999 : wanted.indexOf(b.id)))
        : [...list].sort((a, b) => a.sortOrder - b.sortOrder);
      for (const row of ordered) sortOf.set(row.id, i++);
    }
    // meta da semana = soma das atividades que continuam no plano (dispensadas na reprogramação saem da conta)
    weekMinutes.set(weekId, inWeek.filter((row) => !leaves.has(row.id) && !(row.status === "SKIPPED" && row.rescheduledAt)).reduce((n, row) => n + row.plannedMinutes, 0));
  }
  for (const [id, order] of sortOf) {
    if (order !== sc.rowById.get(id)!.sortOrder) updates.set(id, { ...(updates.get(id) ?? {}), sortOrder: order });
  }

  const entry = {
    at: now.toISOString(), option: input.params.option, selected: new Set(input.activityIds).size, moved: moved.size,
    dependents: r.dependentsMoved, dismissed: r.dismissed.length, yielded: r.yielded.length, doesNotFit: r.doesNotFit.length,
  };
  const ids = [...updates.keys()];
  await db.$transaction(
    async (tx) => {
      // um UPDATE ... FROM unnest(...) por bloco de 300 (centenas de atividades, uma ida ao banco por bloco); null = não muda o campo
      for (let i = 0; i < ids.length; i += 300) {
        const part = ids.slice(i, i + 300);
        const get = <T,>(f: (u: NonNullable<ReturnType<typeof updates.get>>) => T) => part.map((id) => f(updates.get(id)!));
        await tx.$executeRawUnsafe(
          `UPDATE "Activity" a SET
             "weekId" = COALESCE(d.week, a."weekId"),
             "dayIndex" = COALESCE(d.day, a."dayIndex"),
             "sortOrder" = COALESCE(d.so, a."sortOrder"),
             "status" = COALESCE(d.st::"ActivityStatus", a."status"),
             "rescheduledAt" = COALESCE(d.ra::timestamp, a."rescheduledAt")
           FROM unnest($1::text[], $2::text[], $3::int[], $4::int[], $5::text[], $6::text[]) AS d(id, week, day, so, st, ra)
           WHERE a."id" = d.id`,
          part,
          get((u) => u.weekId ?? null),
          get((u) => u.dayIndex ?? null),
          get((u) => u.sortOrder ?? null),
          get((u) => u.status ?? null),
          get((u) => (u.rescheduledAt ? u.rescheduledAt.toISOString() : null)),
        );
      }
      for (const [weekId, minutes] of weekMinutes) await tx.week.update({ where: { id: weekId }, data: { targetMinutes: minutes } });
      const params = { ...sc.plan.params, reschedules: [...history(sc.plan.params), entry].slice(-50) };
      await tx.plan.update({ where: { id: sc.plan.id }, data: { params: params as object } });
    },
    { timeout: 60_000, maxWait: 10_000 },
  );
  return { ok: true, moved: moved.size, dismissed: r.dismissed.length + (r.noFitLeavesPlan ? r.doesNotFit.length : 0) + r.yielded.length };
}
