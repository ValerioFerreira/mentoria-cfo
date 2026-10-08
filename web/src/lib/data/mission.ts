import "server-only";
import { db } from "@/lib/db";
import { dateOfPlanDay, effectiveDays, firstStudyISO, planPosition, todayISO, type PlanPosition } from "@/lib/plan-time";
import { secondsByActivity } from "@/lib/data/study";
import { activityDetail } from "@/lib/activity-detail";
import type { ActivityRowData } from "@/components/activity-row";

export interface MissionRow extends ActivityRowData {
  /** semana do plano (1…N) e dia da semana (0 = segunda … 6 = domingo) */
  week: number;
  day: number;
  date: string;
  spent: number;
}

type PlanWithWeeks = NonNullable<Awaited<ReturnType<typeof import("@/lib/data/study").getActivePlan>>>;

const OPEN = new Set(["PENDING", "IN_PROGRESS"]);

/**
 * Tudo o que a "Missão de hoje" precisa: as atividades do dia, as atrasadas (dias anteriores ainda abertas)
 * e o próximo dia com atividades (para quem quiser adiantar).
 */
export async function getMission(userId: string, plan: PlanWithWeeks) {
  const startIso = plan.startDate.toISOString().slice(0, 10);
  const today = todayISO();
  const firstStudy = firstStudyISO(plan);
  const pos: PlanPosition = planPosition(startIso, plan.weeks.length, today, firstStudy);

  const all = plan.weeks.flatMap((w) =>
    effectiveDays(w.activities).map((a) => ({ ...a, week: w.index, date: dateOfPlanDay(startIso, w.index, a.day), kind: w.kind })),
  );
  const todayRows = pos.state === "during" ? all.filter((a) => a.date === today) : [];
  const overdue = pos.state === "after" ? all.filter((a) => OPEN.has(a.status)) : all.filter((a) => a.date < today && OPEN.has(a.status));
  const futureOpen = all.filter((a) => a.date > today && OPEN.has(a.status));
  const nextDate = futureOpen.length ? futureOpen.reduce((m, a) => (a.date < m ? a.date : m), futureOpen[0].date) : null;
  const upcoming = nextDate ? all.filter((a) => a.date === nextDate && OPEN.has(a.status)) : [];

  const ids = [...new Set([...todayRows, ...overdue, ...upcoming].map((a) => a.id))];
  const [details, seconds] = await Promise.all([
    db.activity.findMany({
      where: { id: { in: ids } },
      select: { id: true, type: true, scope: true, fixRanges: true, quizQuestions: true, aula: { select: { number: true, shortTitle: true } }, segments: { select: { segment: { select: { startPage: true, endPage: true } } } } },
    }),
    secondsByActivity(userId, ids),
  ]);
  const detailOf = new Map(details.map((d) => [d.id, d]));
  const toRow = (a: (typeof all)[number]): MissionRow => ({
    id: a.id, type: a.type, status: a.status, subjectId: a.subjectId, scope: a.scope, plannedMinutes: a.plannedMinutes,
    aula: detailOf.get(a.id)?.aula ?? { number: 0, shortTitle: "" }, detail: detailOf.has(a.id) ? activityDetail(detailOf.get(a.id)!) : null, week: a.week, day: a.day, date: a.date, spent: seconds.get(a.id) ?? 0,
  });
  const byOrder = (x: { week: number; day: number }, y: { week: number; day: number }) => x.week - y.week || x.day - y.day;
  return {
    pos,
    today,
    startIso,
    firstStudy,
    rows: todayRows.map(toRow),
    overdue: overdue.map(toRow).sort(byOrder),
    upcoming: upcoming.map(toRow),
    upcomingDate: nextDate,
  };
}
