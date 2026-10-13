"use server";

import { revalidatePath } from "next/cache";
import { db } from "@/lib/db";
import { requireAdmin } from "@/lib/auth/dal";
import { hashPassword } from "@/lib/auth/password";
import { generateTemporaryPassword, sendApprovalEmail, sendResendCredentialsEmail } from "@/lib/email";
import { regeneratePlanForUser } from "@/lib/plan/regenerate";
import { cancelContract, grantAccessUntilExam, linkContractsToUser } from "@/lib/commerce/contracts";
import { CommerceError } from "@/lib/commerce/errors";

export type AdminActionResult = { success: boolean; message: string; tempPassword?: string };
export type ValidityOption = "EXTEND_30_DAYS" | "EXTEND_60_DAYS" | "EXTEND_90_DAYS" | "INDEFINITE" | "CUSTOM_DATE";

export async function approveRegistration(
  entryId: string,
  duration: "UNTIL_EXAM" | "30_DAYS" | "INDEFINITE",
  opts: { override?: boolean; justification?: string } = {},
): Promise<AdminActionResult> {
  const admin = await requireAdmin();
  if (duration !== "UNTIL_EXAM" && duration !== "30_DAYS" && duration !== "INDEFINITE") {
    return { success: false, message: "Validade inválida." };
  }

  const entry = await db.waitlistEntry.findUnique({ where: { id: entryId } });
  if (!entry) {
    return { success: false, message: "Registro da lista de espera não encontrado." };
  }

  // acesso até a prova: precisa da contratação (obrigação financeira) desta inscrição
  const contract = await db.contract.findFirst({
    where: { customerEmail: entry.email, contest: entry.contest, status: { not: "CANCELLED" } },
    orderBy: { createdAt: "desc" },
    select: { id: true },
  });
  if (duration === "UNTIL_EXAM" && !contract) {
    return { success: false, message: "Esta inscrição não tem contratação registrada. Registre-a em Financeiro ou escolha outra validade." };
  }

  const tempPassword = generateTemporaryPassword("MTR");
  const passwordHash = await hashPassword(tempPassword);

  const accessExpiresAt =
    duration === "30_DAYS"
      ? new Date(Date.now() + 30 * 24 * 60 * 60 * 1000)
      : null;

  let accessUntil: Date | null = null;
  try {
    await db.$transaction(async (tx) => {
      // Cria ou atualiza o usuário no banco
      const existingUser = await tx.user.findUnique({ where: { email: entry.email }, include: { partner: { select: { id: true } } } });
      let userId: string;
      if (!existingUser) {
        // Garante que o username não conflita
        let username = entry.username;
        const userWithUsername = await tx.user.findUnique({ where: { username } });
        if (userWithUsername) {
          username = `${username}_${Math.floor(100 + Math.random() * 900)}`;
        }
        userId = (
          await tx.user.create({
            data: { name: entry.name, email: entry.email, username, passwordHash, mustChangePassword: true, accessExpiresAt, role: "USER" },
          })
        ).id;
      } else {
        if (existingUser.role !== "USER") throw new CommerceError("Este e-mail pertence a um administrador.");
        if (existingUser.partner) throw new CommerceError("Este e-mail é de um parceiro: libere o acesso pela contratação, em Financeiro (a senha do parceiro não é trocada).");
        userId = existingUser.id;
        await tx.user.update({ where: { id: userId }, data: { passwordHash, mustChangePassword: true, accessExpiresAt } });
      }
      await linkContractsToUser(tx, userId, entry.email);
      if (duration === "UNTIL_EXAM" && contract) {
        // mesma regra do Financeiro: exige data da prova e quitação (ou liberação justificada)
        const g = await grantAccessUntilExam(contract.id, admin.id, { ...opts, newAccount: true }, tx);
        accessUntil = g.until;
      }
      await tx.waitlistEntry.update({
        where: { id: entry.id },
        data: { status: "APPROVED", paidAt: entry.paidAt ?? new Date(), approvedAt: new Date(), accessDuration: duration },
      });
    });
  } catch (err) {
    if (err instanceof CommerceError) return { success: false, message: err.message };
    throw err;
  }

  // Envia e-mail de aprovação
  const loginUrl = `${(process.env.SITE_URL || "https://www.missaomentoria.com.br").replace(/\/$/, "")}/login`;

  let emailSent = false;
  try {
    const emailRes = await sendApprovalEmail({
      to: entry.email,
      name: entry.name,
      tempPassword,
      accessDuration: duration,
      accessUntil,
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
  const admin = await requireAdmin();

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

  // obrigação sem nada recebido é cancelada (fica no histórico); com valores recebidos, o estorno é feito no Financeiro
  const open = await db.contract.findMany({ where: { customerEmail: entry.email, contest: entry.contest, status: "OPEN" }, select: { id: true } });
  for (const c of open) {
    try {
      await cancelContract(c.id, `Inscrição rejeitada: ${reason?.trim() || "pagamento não identificado"}`, admin.id);
    } catch (err) {
      if (!(err instanceof CommerceError)) throw err;
    }
  }

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

