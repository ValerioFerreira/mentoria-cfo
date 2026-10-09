"use server";

import { redirect } from "next/navigation";
import * as z from "zod";
import { db } from "@/lib/db";
import { hashPassword, verifyPassword } from "@/lib/auth/password";
import { clearFailures, registerFailure, tooManyAttempts } from "@/lib/auth/rate-limit";
import { createSession, destroySession } from "@/lib/auth/session";

export type AuthState = { errors?: Record<string, string[]>; message?: string } | undefined;

const SignupSchema = z.object({
  name: z.string().trim().min(2, "Informe seu nome."),
  email: z.email("E-mail inválido.").trim().toLowerCase(),
  password: z.string().min(8, "A senha precisa ter ao menos 8 caracteres."),
  invite: z.string().trim().min(4, "Informe o código de convite."),
});

export async function signup(_: AuthState, formData: FormData): Promise<AuthState> {
  const parsed = SignupSchema.safeParse(Object.fromEntries(formData));
  if (!parsed.success) return { errors: z.flattenError(parsed.error).fieldErrors as Record<string, string[]> };
  const { name, email, password, invite } = parsed.data;

  const inv = await db.invite.findUnique({ where: { code: invite } });
  if (!inv || inv.usedAt || (inv.email && inv.email.toLowerCase() !== email)) {
    return { errors: { invite: ["Convite inválido, já usado ou emitido para outro e-mail."] } };
  }
  if (await db.user.findUnique({ where: { email } })) {
    return { errors: { email: ["Este e-mail já está cadastrado."] } };
  }

  const passwordHash = await hashPassword(password);
  // o nome de usuário escolhido na lista de espera passa para a conta (se ainda estiver livre)
  const waiting = await db.waitlistEntry.findFirst({ where: { email }, orderBy: { createdAt: "asc" } });
  const username = waiting && !(await db.user.findUnique({ where: { username: waiting.username }, select: { id: true } })) ? waiting.username : undefined;
  const user = await db.$transaction(async (tx) => {
    const u = await tx.user.create({ data: { name, email, username, passwordHash, role: inv.makeAdmin ? "ADMIN" : "USER" } });
    await tx.invite.update({ where: { id: inv.id }, data: { usedAt: new Date(), usedByUserId: u.id } });
    return u;
  });
  await createSession(user.id);
  redirect("/");
}

const LoginSchema = z.object({
  email: z.email("E-mail inválido.").trim().toLowerCase(),
  password: z.string().min(1, "Informe a senha."),
});

export async function login(_: AuthState, formData: FormData): Promise<AuthState> {
  const parsed = LoginSchema.safeParse(Object.fromEntries(formData));
  if (!parsed.success) return { errors: z.flattenError(parsed.error).fieldErrors as Record<string, string[]> };
  const { email, password } = parsed.data;
  if (tooManyAttempts(email)) return { message: "Muitas tentativas. Aguarde alguns minutos e tente novamente." };

  const user = await db.user.findUnique({ where: { email } });
  const ok = user ? await verifyPassword(password, user.passwordHash) : false;
  if (!user || !ok) {
    registerFailure(email);
    return { message: "E-mail ou senha incorretos." };
  }
  clearFailures(email);
  await createSession(user.id);
  redirect("/");
}

export async function logout(): Promise<void> {
  await destroySession();
  redirect("/login");
}
