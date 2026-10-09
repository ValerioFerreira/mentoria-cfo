"use server";

import * as z from "zod";
import { revalidatePath } from "next/cache";
import { db } from "@/lib/db";
import { requireUser } from "@/lib/auth/dal";
import { hashPassword, verifyPassword } from "@/lib/auth/password";
import { generateTemporaryPassword, sendPasswordResetEmail } from "@/lib/email";

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

  const loginUrl = `${(process.env.SITE_URL || "https://mentoria-cfo.vercel.app").replace(/\/$/, "")}/login`;

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
