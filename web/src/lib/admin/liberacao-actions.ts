"use server";

import { revalidatePath } from "next/cache";
import { db } from "@/lib/db";
import { requireUser } from "@/lib/auth/dal";
import { sendPlanReadyEmail } from "@/lib/email";
import { setPlatformReleased, isPlatformReleased } from "@/lib/system-settings";
import { regeneratePlanForUser } from "@/lib/plan/regenerate";

export interface ReleaseResult {
  success: boolean;
  message: string;
  plansActivated: number;
  totalUsers: number;
  emailsSent: number;
  errors: number;
  isPlatformReleased: boolean;
}

/**
 * Executa a Liberação Geral do Sistema:
 * 1. Ativa a flag global PLATFORM_RELEASED = true.
 * 2. Re-elabora todos os planos pendentes nas regras novas e ativa para o status ACTIVE.
 * 3. Notifica todos os alunos cadastrados por e-mail.
 */
export async function releasePlansAndNotifyAll(): Promise<ReleaseResult> {
  const admin = await requireUser();
  if (admin.role !== "ADMIN") {
    throw new Error("Acesso não autorizado. Apenas administradores podem executar esta ação.");
  }

  // 1. Ativa a liberação geral da plataforma no banco de dados
  await setPlatformReleased(true);

  // 2. Re-elabora e ativa todos os planos pendentes para ACTIVE nas regras novas
  const pendingPlans = await db.plan.findMany({
    where: { status: "PENDING_ANALYSIS" },
    select: { id: true },
  });
  let plansActivated = 0;
  for (const p of pendingPlans) {
    const res = await regeneratePlanForUser(p.id, { activate: true });
    if (res.success) {
      plansActivated++;
    } else {
      await db.plan.update({ where: { id: p.id }, data: { status: "ACTIVE" } });
      plansActivated++;
    }
  }

  // 3. Busca todos os usuários cadastrados na plataforma
  const users = await db.user.findMany({
    select: { id: true, name: true, email: true },
    orderBy: { createdAt: "asc" },
  });

  const appUrl =
    process.env.APP_URL ||
    (process.env.VERCEL_PROJECT_PRODUCTION_URL ? `https://${process.env.VERCEL_PROJECT_PRODUCTION_URL}` : "http://localhost:3000");

  const loginUrl = `${appUrl}/plano`;

  let emailsSent = 0;
  let errors = 0;

  for (const user of users) {
    try {
      const res = await sendPlanReadyEmail({
        to: user.email,
        name: user.name,
        loginUrl,
      });
      if (res.success) {
        emailsSent++;
      } else {
        errors++;
      }
    } catch (err) {
      console.error(`[releasePlansAndNotifyAll] Erro ao enviar e-mail para ${user.email}:`, err);
      errors++;
    }
  }

  revalidatePath("/", "layout");
  revalidatePath("/plano");
  revalidatePath("/semana");
  revalidatePath("/questoes");
  revalidatePath("/simulados");
  revalidatePath("/admin/cadastros");
  revalidatePath("/admin/liberacao");

  const message =
    `Liberação Geral Ativada com Sucesso! ${plansActivated} planejamento(s) ativado(s). ` +
    `${emailsSent} e-mail(s) enviado(s) de um total de ${users.length} usuário(s) cadastrado(s). ` +
    `Planejamento, Questões e Simulados agora estão 100% disponíveis para todos os alunos.` +
    (errors > 0 ? ` (${errors} aviso(s) de envio registrado(s) no log).` : "");

  return {
    success: true,
    message,
    plansActivated,
    totalUsers: users.length,
    emailsSent,
    errors,
    isPlatformReleased: true,
  };
}

/**
 * Alterna a liberação geral da plataforma (liga/desliga o acesso geral dos alunos).
 */
export async function togglePlatformRelease(released: boolean): Promise<{ success: boolean; isReleased: boolean; message: string }> {
  const admin = await requireUser();
  if (admin.role !== "ADMIN") {
    throw new Error("Acesso não autorizado. Apenas administradores podem executar esta ação.");
  }

  await setPlatformReleased(released);

  if (released) {
    // Ao ativar, re-elabora e ativa também quaisquer planos em análise nas regras novas
    const pendingPlans = await db.plan.findMany({
      where: { status: "PENDING_ANALYSIS" },
      select: { id: true },
    });
    for (const p of pendingPlans) {
      const res = await regeneratePlanForUser(p.id, { activate: true });
      if (!res.success) {
        await db.plan.update({ where: { id: p.id }, data: { status: "ACTIVE" } });
      }
    }
  }

  revalidatePath("/", "layout");
  revalidatePath("/plano");
  revalidatePath("/semana");
  revalidatePath("/questoes");
  revalidatePath("/simulados");
  revalidatePath("/admin/liberacao");

  return {
    success: true,
    isReleased: released,
    message: released
      ? "Plataforma liberada com sucesso para todos os usuários cadastrados!"
      : "Plataforma bloqueada para alunos comuns (disponível apenas para administradores).",
  };
}
