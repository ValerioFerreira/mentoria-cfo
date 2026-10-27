import "server-only";
import { db } from "@/lib/db";
import { planPosition, todayISO } from "@/lib/plan-time";

export async function getActivePlan(userId: string) {
  return db.plan.findFirst({
    where: { userId, status: "ACTIVE" },
    orderBy: { version: "desc" },
    include: {
      subjects: { include: { subject: { select: { id: true, name: true, examQuestions: true, block: true } } } },
      weeks: {
        orderBy: { index: "asc" },
        include: { activities: { select: { id: true, type: true, subjectId: true, aulaId: true, status: true, plannedMinutes: true, scope: true, dayIndex: true, sortOrder: true } } },
      },
    },
  });
}

export async function getPendingPlan(userId: string) {
  const user = await db.user.findUnique({ where: { id: userId }, select: { role: true } });
  if (user?.role === "ADMIN") {
    await db.plan.updateMany({
      where: { userId, status: "PENDING_ANALYSIS" },
      data: { status: "ACTIVE" },
    });
    return null;
  }
  const plan = await db.plan.findFirst({
    where: { userId, status: "PENDING_ANALYSIS" },
    orderBy: { version: "desc" },
    select: {
      id: true,
      status: true,
      createdAt: true,
      examDate: true,
      params: true,
      subjects: { select: { subjectId: true } },
    },
  });
  // ciclo do edital (concurso sem data de prova): a "data" do plano é o fim do ciclo, não a prova
  return plan && (plan.params as { cycle?: number } | null)?.cycle ? { ...plan, examDate: null } : plan;
}

/** Segundos estudados por atividade (soma dos registros de tempo). */
export async function secondsByActivity(userId: string, activityIds?: string[]): Promise<Map<string, number>> {
  const rows = await db.timeLog.groupBy({
    by: ["activityId"],
    where: { userId, activityId: activityIds ? { in: activityIds } : { not: null } },
    _sum: { seconds: true },
  });
  return new Map(rows.filter((r) => r.activityId).map((r) => [r.activityId!, r._sum.seconds ?? 0]));
}

export function currentWeekIndex(startDate: Date, totalWeeks: number, now = new Date()): number {
  return planPosition(startDate.toISOString().slice(0, 10), totalWeeks, todayISO(now)).week;
}

export async function getWeek(userId: string, planId: string, index: number) {
  const week = await db.week.findFirst({
    where: { planId, index, plan: { userId, status: "ACTIVE" } },
    include: {
      activities: {
        orderBy: { sortOrder: "asc" },
        include: { subject: { select: { name: true } }, aula: { select: { number: true, shortTitle: true } }, segments: { select: { segment: { select: { startTopic: true, sortOrder: true } } } } },
      },
    },
  });
  if (!week) return null;
  const seconds = await secondsByActivity(userId, week.activities.map((a) => a.id));
  return { week, seconds };
}

export async function getActivity(userId: string, id: string) {
  return db.activity.findFirst({
    where: { id, week: { plan: { userId, status: "ACTIVE" } } },
    include: {
      subject: { select: { id: true, name: true } },
      aula: { select: { id: true, number: true, shortTitle: true, printedOffset: true } },
      week: { select: { id: true, index: true, planId: true, plan: { select: { contest: true } } } },
      segments: {
        include: {
          segment: { include: { bizu: { include: { items: { orderBy: { sortOrder: "asc" } } } } } },
        },
      },
      refs: {
        include: {
          refActivity: {
            select: {
              id: true, key: true, status: true,
              aula: { select: { number: true, shortTitle: true } },
              segments: { select: { segmentId: true } },
            },
          },
        },
      },
      timeLogs: { orderBy: { startedAt: "desc" } },
    },
  });
}
