"use server";

import { revalidatePath } from "next/cache";
import { db } from "@/lib/db";
import { requireAdmin } from "@/lib/auth/dal";
import { hashPassword } from "@/lib/auth/password";
import { generateTemporaryPassword, sendApprovalEmail } from "@/lib/email";

export type AdminActionResult = { success: boolean; message: string; tempPassword?: string };

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
