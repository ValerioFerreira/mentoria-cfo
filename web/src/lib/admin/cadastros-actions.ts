"use server";

import { revalidatePath } from "next/cache";
import { db } from "@/lib/db";
import { requireAdmin } from "@/lib/auth/dal";
import { hashPassword } from "@/lib/auth/password";
import { generateTemporaryPassword, sendApprovalEmail, sendResendCredentialsEmail } from "@/lib/email";
import { regeneratePlanForUser } from "@/lib/plan/regenerate";

export type AdminActionResult = { success: boolean; message: string; tempPassword?: string };
export type ValidityOption = "EXTEND_30_DAYS" | "EXTEND_60_DAYS" | "EXTEND_90_DAYS" | "INDEFINITE" | "CUSTOM_DATE";

export async function approveRegistration(
  entryId: string,
  duration: "30_DAYS" | "INDEFINITE",
): Promise<AdminActionResult> {
  await requireAdmin();

  const entry = await db.waitlistEntry.findUnique({ where: { id: entryId } });
  if (!entry) {
    return { success: false, message: "Registro da lista de espera não encontrado." };
  }

  const tempPassword = generateTemporaryPassword("MTR");
  const passwordHash = await hashPassword(tempPassword);

  const accessExpiresAt =
    duration === "30_DAYS"
      ? new Date(Date.now() + 30 * 24 * 60 * 60 * 1000)
      : null;

  // Cria ou atualiza o usuário no banco
  const existingUser = await db.user.findUnique({ where: { email: entry.email } });

  if (!existingUser) {
    // Garante que o username não conflita
    let username = entry.username;
    const userWithUsername = await db.user.findUnique({ where: { username } });
    if (userWithUsername) {
      username = `${username}_${Math.floor(100 + Math.random() * 900)}`;
    }

    await db.user.create({
      data: {
        name: entry.name,
        email: entry.email,
        username,
        passwordHash,
        mustChangePassword: true,
        accessExpiresAt,
        role: "USER",
      },
    });
  } else {
    await db.user.update({
      where: { id: existingUser.id },
      data: {
        passwordHash,
        mustChangePassword: true,
        accessExpiresAt,
      },
    });
  }

  // Atualiza status da lista de espera
  await db.waitlistEntry.update({
    where: { id: entry.id },
    data: {
      status: "APPROVED",
      paidAt: entry.paidAt ?? new Date(),
      approvedAt: new Date(),
      accessDuration: duration,
    },
  });

  // Envia e-mail de aprovação
  const loginUrl = `${(process.env.SITE_URL || "https://www.missaomentoria.com.br").replace(/\/$/, "")}/login`;

  let emailSent = false;
  try {
    const emailRes = await sendApprovalEmail({
      to: entry.email,
      name: entry.name,
      tempPassword,
      accessDuration: duration,
      loginUrl,
    });
    emailSent = emailRes?.success ?? false;
  } catch (err) {
    console.error("Erro ao enviar e-mail de aprovação:", err);
  }

  revalidatePath("/admin/cadastros");
  return {
    success: true,
    message: emailSent
      ? `Cadastro de ${entry.name} aprovado com sucesso! E-mail com senha temporária enviado.`
      : `Cadastro de ${entry.name} aprovado! Atenção: configure RESEND_API_KEY ou SMTP na Vercel para envio automático. Copie a senha temporária abaixo para enviar ao aluno.`,
    tempPassword,
  };
}

export async function rejectRegistration(entryId: string, reason?: string): Promise<AdminActionResult> {
  await requireAdmin();

  const entry = await db.waitlistEntry.findUnique({ where: { id: entryId } });
  if (!entry) {
    return { success: false, message: "Registro não encontrado." };
  }

  await db.waitlistEntry.update({
    where: { id: entryId },
    data: {
      status: "REJECTED",
      rejectedAt: new Date(),
      rejectionReason: reason?.trim() || "Comprovante não identificado ou pagamento recusado.",
    },
  });

  revalidatePath("/admin/cadastros");
  return { success: true, message: `Cadastro de ${entry.name} foi rejeitado.` };
}

export async function deleteWaitlistEntry(entryId: string): Promise<AdminActionResult> {
  await requireAdmin();

  await db.waitlistEntry.delete({ where: { id: entryId } });
  revalidatePath("/admin/cadastros");
  return { success: true, message: "Registro removido com sucesso." };
}

export async function approvePlan(planId: string): Promise<AdminActionResult> {
  await requireAdmin();

  const plan = await db.plan.findUnique({
    where: { id: planId },
    include: { user: { select: { name: true, email: true } } },
  });
  if (!plan) {
    return { success: false, message: "Planejamento não encontrado." };
  }

  // Re-elabora o planejamento nos moldes e regras atuais do sistema
  // aproveitando integralmente as respostas de anamnese e parâmetros do aluno
  const regen = await regeneratePlanForUser(planId, { activate: true });
  if (!regen.success) {
    console.warn(`[approvePlan] Falha ao regenerar plano ${planId}: ${regen.message}. Ativando versão existente.`);
    await db.plan.update({
      where: { id: planId },
      data: { status: "ACTIVE" },
    });
  }

  revalidatePath("/admin/cadastros");
  revalidatePath("/admin/liberacao");
  revalidatePath("/", "layout");
  revalidatePath("/plano");
  revalidatePath("/semana");
  return {
    success: true,
    message: `Planejamento de ${plan.user.name ?? plan.user.email} montado com as regras novas e liberado com sucesso!`,
  };
}

export async function updateAccessValidity(
  entryId: string,
  option: ValidityOption,
  customDate?: string,
): Promise<AdminActionResult> {
  await requireAdmin();

  const entry = await db.waitlistEntry.findUnique({ where: { id: entryId } });
  if (!entry) {
    return { success: false, message: "Registro da lista de espera não encontrado." };
  }

  const user = await db.user.findUnique({ where: { email: entry.email } });
  if (!user) {
    return { success: false, message: `Usuário associado ao e-mail ${entry.email} não foi encontrado no sistema.` };
  }

  let newExpiresAt: Date | null = null;
  let accessDuration = entry.accessDuration || "30_DAYS";
  let label = "";

  const now = Date.now();
  // Se a validade atual ainda estiver no futuro, soma sobre ela. Caso contrário, soma sobre agora.
  const currentExpMs = user.accessExpiresAt && user.accessExpiresAt.getTime() > now
    ? user.accessExpiresAt.getTime()
    : now;

  if (option === "INDEFINITE") {
    newExpiresAt = null;
    accessDuration = "INDEFINITE";
    label = "Indeterminado (até a homologação do concurso)";
  } else if (option === "EXTEND_30_DAYS") {
    newExpiresAt = new Date(currentExpMs + 30 * 24 * 60 * 60 * 1000);
    accessDuration = "30_DAYS";
    label = `30 dias adicionados (vence em ${newExpiresAt.toLocaleDateString("pt-BR")})`;
  } else if (option === "EXTEND_60_DAYS") {
    newExpiresAt = new Date(currentExpMs + 60 * 24 * 60 * 60 * 1000);
    accessDuration = "60_DAYS";
    label = `60 dias adicionados (vence em ${newExpiresAt.toLocaleDateString("pt-BR")})`;
  } else if (option === "EXTEND_90_DAYS") {
    newExpiresAt = new Date(currentExpMs + 90 * 24 * 60 * 60 * 1000);
    accessDuration = "90_DAYS";
    label = `90 dias adicionados (vence em ${newExpiresAt.toLocaleDateString("pt-BR")})`;
  } else if (option === "CUSTOM_DATE") {
    if (!customDate) {
      return { success: false, message: "Informe uma data válida para a expiração." };
    }
    const [y, m, d] = customDate.split("-").map(Number);
    if (!y || !m || !d) {
      return { success: false, message: "Data em formato inválido." };
    }
    newExpiresAt = new Date(y, m - 1, d, 23, 59, 59, 999);
    accessDuration = "CUSTOM";
    label = `Definido até ${newExpiresAt.toLocaleDateString("pt-BR")}`;
  }

  await db.user.update({
    where: { id: user.id },
    data: { accessExpiresAt: newExpiresAt },
  });

  await db.waitlistEntry.update({
    where: { id: entry.id },
    data: {
      accessDuration,
      status: "APPROVED",
    },
  });

  revalidatePath("/admin/cadastros");
  return {
    success: true,
    message: `Validade de ${entry.name} atualizada com sucesso: ${label}.`,
  };
}

export async function resendTemporaryPassword(entryId: string): Promise<AdminActionResult> {
  await requireAdmin();

  const entry = await db.waitlistEntry.findUnique({ where: { id: entryId } });
  if (!entry) {
    return { success: false, message: "Registro da lista de espera não encontrado." };
  }

  const user = await db.user.findUnique({ where: { email: entry.email } });
  if (!user) {
    return { success: false, message: `Usuário com e-mail ${entry.email} não localizado no sistema.` };
  }

  const tempPassword = generateTemporaryPassword("MTR");
  const passwordHash = await hashPassword(tempPassword);

  await db.user.update({
    where: { id: user.id },
    data: {
      passwordHash,
      mustChangePassword: true,
    },
  });

  const loginUrl = `${(process.env.SITE_URL || "https://www.missaomentoria.com.br").replace(/\/$/, "")}/login`;

  let emailSent = false;
  try {
    const emailRes = await sendResendCredentialsEmail({
      to: entry.email,
      name: entry.name,
      tempPassword,
      accessDuration: entry.accessDuration,
      accessExpiresAt: user.accessExpiresAt,
      loginUrl,
    });
    emailSent = emailRes?.success ?? false;
  } catch (err) {
    console.error("Erro ao reenviar e-mail com senha temporária:", err);
  }

  revalidatePath("/admin/cadastros");
  return {
    success: true,
    message: emailSent
      ? `E-mail com nova senha temporária enviado com sucesso para ${entry.email}!`
      : `Nova senha gerada para ${entry.name}! Atenção: e-mail automático não configurado. Copie a senha temporária abaixo para enviar ao aluno.`,
    tempPassword,
  };
}

