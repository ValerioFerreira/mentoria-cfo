"use server";

import { revalidatePath } from "next/cache";
import { db } from "@/lib/db";
import { requireUser } from "@/lib/auth/dal";
import { sendPlanReadyEmail } from "@/lib/email";

export interface ReleaseResult {
  success: boolean;
  message: string;
  plansActivated: number;
  totalUsers: number;
  emailsSent: number;
  errors: number;
}

export async function releasePlansAndNotifyAll(): Promise<ReleaseResult> {
  const admin = await requireUser();
  if (admin.role !== "ADMIN") {
    throw new Error("Acesso não autorizado. Apenas administradores podem executar esta ação.");
  }

  // 1. Atualiza todos os planos pendentes para ACTIVE
  const updateResult = await db.plan.updateMany({
    where: { status: "PENDING_ANALYSIS" },
    data: { status: "ACTIVE" },
  });
  const plansActivated = updateResult.count;

  // 2. Busca todos os usuários cadastrados na plataforma
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

  revalidatePath("/");
  revalidatePath("/plano");
  revalidatePath("/semana");
  revalidatePath("/admin/cadastros");
  revalidatePath("/admin/liberacao");

  const message =
    `Operação concluída: ${plansActivated} planejamento(s) liberado(s) para o status ATIVO. ` +
    `${emailsSent} e-mail(s) enviado(s) de um total de ${users.length} usuário(s) cadastrado(s).` +
    (errors > 0 ? ` (${errors} aviso(s) de envio registrado(s) no log).` : "");

  return {
    success: true,
    message,
    plansActivated,
    totalUsers: users.length,
    emailsSent,
    errors,
  };
}
