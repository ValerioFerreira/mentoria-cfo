import "server-only";
import { db } from "@/lib/db";
import { todayISO } from "@/lib/plan-time";
import { regeneratePlanForUser } from "./regenerate";
import type { Contest } from "@/generated/prisma/client";

/** Data da prova cadastrada em Administração › Concursos (AAAA-MM-DD), ou null se ainda não há data. */
export async function contestExamDate(contest: Contest): Promise<string | null> {
  const s = await db.contestSetting.findUnique({ where: { contest }, select: { examDate: true } });
  return s?.examDate?.toISOString().slice(0, 10) ?? null;
}

/** Nº do ciclo do edital gravado no plano (concurso sem data de prova), ou null. */
export function planCycle(params: unknown): number | null {
  const c = (params as { cycle?: unknown } | null)?.cycle;
  return typeof c === "number" && c > 0 ? c : null;
}

/**
 * Ciclo do edital: quando o ciclo do plano vigente termina, o plano recomeça (ciclo seguinte) a partir de hoje; se o concurso
 * ganhou data de prova, o plano é refeito até a prova. Devolve true quando refez o plano.
 */
export async function ensurePlanCycle(userId: string): Promise<boolean> {
  const plan = await db.plan.findFirst({
    where: { userId, status: "ACTIVE" },
    orderBy: { version: "desc" },
    select: { id: true, params: true, contest: true, examDate: true },
  });
  if (!plan || !planCycle(plan.params)) return false;
  const hasDate = plan.contest ? await contestExamDate(plan.contest) : null;
  // o "examDate" do ciclo é o dia seguinte ao último dia do ciclo
  if (!hasDate && todayISO() < plan.examDate.toISOString().slice(0, 10)) return false;
  const r = await regeneratePlanForUser(plan.id, { nextCycle: !hasDate });
  return r.success;
}

/** Data da prova cadastrada: refaz, a partir de hoje e até a prova, os planos em ciclo do edital desse concurso. */
export async function replanCyclePlans(contest: Contest): Promise<{ done: number; failed: number }> {
  const plans = await db.plan.findMany({
    where: { contest, status: { in: ["ACTIVE", "PENDING_ANALYSIS"] } },
    select: { id: true, params: true },
  });
  let done = 0;
  let failed = 0;
  for (const p of plans.filter((x) => planCycle(x.params))) {
    const r = await regeneratePlanForUser(p.id).catch(() => ({ success: false }));
    if (r.success) done++;
    else failed++;
  }
  return { done, failed };
}
