"use server";

import * as z from "zod";
import { revalidatePath } from "next/cache";
import { cookies } from "next/headers";
import type { Contest } from "@/generated/prisma/client";
import { db } from "@/lib/db";
import { requireUser } from "@/lib/auth/dal";
import { hashPassword, verifyPassword } from "@/lib/auth/password";
import { generateTemporaryPassword, sendPasswordResetEmail } from "@/lib/email";
import { CONTEST_SUBTITLES, CONTESTS } from "@/lib/contests";
import { CONTEST_COOKIE, getUserContest } from "@/lib/user-contest";
import { toActionError } from "@/lib/commerce/errors";
import { markSwitchApplied, offerSwitch, pendingPaidSwitch, startSwitchContract } from "@/lib/commerce/switch";

export type ProfilePasswordState = { errors?: Record<string, string[]>; message?: string; success?: boolean } | undefined;

const UpdatePasswordSchema = z
  .object({
    currentPassword: z.string().min(1, "Informe a senha atual."),
    newPassword: z.string().min(8, "A nova senha precisa ter ao menos 8 caracteres."),
    confirmPassword: z.string().min(1, "Confirme a nova senha."),
  })
  .refine((d) => d.newPassword === d.confirmPassword, {
    message: "A confirmação não coincide com a nova senha.",
    path: ["confirmPassword"],
  });

export async function updateUserPassword(_: ProfilePasswordState, formData: FormData): Promise<ProfilePasswordState> {
  const sessionUser = await requireUser();
  if (sessionUser.isPartner) return { message: "A senha de parceiro é gerenciada pela administração." };
  const user = await db.user.findUnique({ where: { id: sessionUser.id } });
  if (!user) return { message: "Usuário não encontrado." };

  const parsed = UpdatePasswordSchema.safeParse(Object.fromEntries(formData));
  if (!parsed.success) return { errors: z.flattenError(parsed.error).fieldErrors as Record<string, string[]> };

  const { currentPassword, newPassword } = parsed.data;

  // Valida senha atual
  const ok = await verifyPassword(currentPassword, user.passwordHash);
  if (!ok) {
    return { errors: { currentPassword: ["Senha atual incorreta."] } };
  }

  const passwordHash = await hashPassword(newPassword);
  await db.user.update({
    where: { id: user.id },
    data: {
      passwordHash,
      mustChangePassword: false,
    },
  });

  revalidatePath("/perfil");
  return { success: true, message: "Sua senha foi alterada com sucesso!" };
}

export async function sendSelfPasswordReset(): Promise<{ success: boolean; message: string }> {
  const sessionUser = await requireUser();
  if (sessionUser.isPartner) return { success: false, message: "A senha de parceiro é gerenciada pela administração." };
  const user = await db.user.findUnique({ where: { id: sessionUser.id } });
  if (!user) return { success: false, message: "Usuário não encontrado." };

  const tempPassword = generateTemporaryPassword("REC");
  const passwordHash = await hashPassword(tempPassword);

  await db.user.update({
    where: { id: user.id },
    data: {
      passwordHash,
      mustChangePassword: true,
    },
  });

  const loginUrl = `${(process.env.SITE_URL || "https://www.missaomentoria.com.br").replace(/\/$/, "")}/login`;

  await sendPasswordResetEmail({
    to: user.email,
    name: user.name ?? undefined,
    tempPassword,
    loginUrl,
  });

  return {
    success: true,
    message: `Uma nova senha temporária foi enviada para ${user.email}. Ao sair ou fazer novo login, você a utilizará para trocar sua senha.`,
  };
}

export type ContestSwitchView =
  | {
      ok: true;
      mode: "FREE" | "PAY";
      targetSiteCents: number;
      creditCents: number;
      residualCents: number;
      couponPoints: number;
      finalCents: number;
      coupons: { code: string; kind: "SITE" | "PARTNER"; discountPoints: number }[];
      capped: boolean;
    }
  | { ok: false; message: string };

function validTarget(contestKey: string): string | null {
  if (!(contestKey in CONTEST_SUBTITLES)) return "Concurso inválido.";
  // só concursos com plano pronto: os demais estão em desenvolvimento (lista de espera)
  if (!CONTESTS.find((c) => c.key === contestKey)?.available) return "O plano deste concurso ainda está em desenvolvimento.";
  return null;
}

/** Simulação da troca (só exibe): o preço é sempre recalculado no servidor ao iniciar a troca. */
export async function previewContestSwitch(contestKey: string, couponCodes?: string): Promise<ContestSwitchView> {
  const user = await requireUser();
  const invalid = validTarget(contestKey);
  if (invalid) return { ok: false, message: invalid };
  if (typeof couponCodes === "string" && couponCodes.length > 150) return { ok: false, message: "Cupons demais: informe até 5 códigos." };
  try {
    const from = await getUserContest(user.email);
    const o = await offerSwitch({ email: user.email, from, to: contestKey as Contest, isAdmin: user.role === "ADMIN", couponCodes });
    return { ok: true, mode: o.mode, targetSiteCents: o.targetSiteCents, creditCents: o.creditCents, residualCents: o.residualCents, couponPoints: o.couponPoints, finalCents: o.finalCents, coupons: o.coupons, capped: o.capped };
  } catch (err) {
    return toActionError(err, "simular troca de concurso");
  }
}

async function applyContest(email: string, contestKey: string) {
  const jar = await cookies();
  jar.set(CONTEST_COOKIE, contestKey, { path: "/", maxAge: 365 * 86400, sameSite: "lax" });
  try {
    await db.waitlistEntry.updateMany({ where: { email: email.toLowerCase() }, data: { contest: contestKey as Contest } });
  } catch (err) {
    console.error("[updateUserContest] Erro ao sincronizar waitlistEntry:", err);
  }
  revalidatePath("/", "layout");
  revalidatePath("/perfil");
}

/** Troca gratuita (concurso de preço igual ou menor no site). Troca para um mais caro passa por `startContestUpgrade`. */
export async function updateUserContest(contestKey: string): Promise<{ success: boolean; message: string; requiresPayment?: boolean }> {
  const user = await requireUser();
  const invalid = validTarget(contestKey);
  if (invalid) return { success: false, message: invalid };
  try {
    const from = await getUserContest(user.email);
    const o = await offerSwitch({ email: user.email, from, to: contestKey as Contest, isAdmin: user.role === "ADMIN" });
    if (o.mode === "PAY") return { success: false, requiresPayment: true, message: "Este concurso custa mais que o seu: pague a diferença para trocar." };
  } catch (err) {
    return { success: false, message: toActionError(err, "trocar concurso").message };
  }
  await applyContest(user.email, contestKey);
  return { success: true, message: `Concurso alterado para ${CONTEST_SUBTITLES[contestKey as Contest]}.` };
}

/** Inicia a troca para um concurso mais caro: gera a cobrança da diferença (com cupons) e leva ao pagamento. */
export async function startContestUpgrade(contestKey: string, couponCodes?: string): Promise<{ success: boolean; message: string; payUrl?: string }> {
  const user = await requireUser();
  const invalid = validTarget(contestKey);
  if (invalid) return { success: false, message: invalid };
  if (typeof couponCodes === "string" && couponCodes.length > 150) return { success: false, message: "Cupons demais: informe até 5 códigos." };
  try {
    const from = await getUserContest(user.email);
    const row = await db.user.findUnique({ where: { id: user.id }, select: { name: true } });
    const r = await startSwitchContract({ userId: user.id, email: user.email, name: row?.name ?? null, from, to: contestKey as Contest, couponCodes });
    if ("applied" in r) {
      await applyContest(user.email, contestKey);
      return { success: true, message: `Concurso alterado para ${CONTEST_SUBTITLES[contestKey as Contest]}.` };
    }
    return { success: true, message: "Diferença calculada. Redirecionando para o pagamento…", payUrl: `/pagamentos/contratacao/${r.contractId}` };
  } catch (err) {
    return { success: false, message: toActionError(err, "iniciar troca de concurso").message };
  }
}

/** Depois de paga a diferença, aplica a troca (uma única vez). */
export async function finishContestUpgrade(): Promise<{ success: boolean; message: string } | null> {
  const user = await requireUser();
  const paid = await pendingPaidSwitch(user.id, user.email);
  if (!paid) return null;
  await markSwitchApplied(user.id, paid.contractId, paid.contest);
  await applyContest(user.email, paid.contest);
  return { success: true, message: `Pagamento confirmado. Concurso alterado para ${CONTEST_SUBTITLES[paid.contest]}.` };
}
