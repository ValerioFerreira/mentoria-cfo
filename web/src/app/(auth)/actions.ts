"use server";

import { redirect } from "next/navigation";
import * as z from "zod";
import { db } from "@/lib/db";
import { hashPassword, verifyPassword } from "@/lib/auth/password";
import { clearFailures, registerFailure, tooManyAttempts } from "@/lib/auth/rate-limit";
import { createSession, destroySession, getCurrentUser } from "@/lib/auth/session";
import { ensureDefaultAdmin, DEFAULT_ADMIN_EMAIL } from "@/lib/auth/admin-bootstrap";
import { generateTemporaryPassword, sendPasswordResetEmail } from "@/lib/email";

export type AuthState = { errors?: Record<string, string[]>; message?: string; success?: boolean } | undefined;

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

  // Garante bootstrap automático caso o admin padrão esteja entrando pela primeira vez
  if (email === DEFAULT_ADMIN_EMAIL.toLowerCase()) {
    try {
      await ensureDefaultAdmin();
    } catch (e) {
      console.error("Erro no bootstrap do admin durante login:", e);
    }
  }

  const user = await db.user.findUnique({ where: { email } });
  const ok = user ? await verifyPassword(password, user.passwordHash) : false;
  if (!user || !ok) {
    registerFailure(email);
    return { message: "E-mail ou senha incorretos." };
  }

  // Verifica se o acesso do usuário expirou
  if (user.accessExpiresAt && user.accessExpiresAt < new Date()) {
    return { message: "Seu período de acesso ao MentorIA expirou. Entre em contato com a administração." };
  }

  clearFailures(email);
  await createSession(user.id);

  // Se o usuário precisa trocar a senha temporária, vai para /trocar-senha
  if (user.mustChangePassword) {
    redirect("/trocar-senha");
  }

  redirect("/");
}

export async function logout(): Promise<void> {
  await destroySession();
  redirect("/login");
}

const ChangePasswordSchema = z
  .object({
    password: z.string().min(8, "A nova senha deve ter no mínimo 8 caracteres."),
    confirmPassword: z.string().min(1, "Confirme a nova senha."),
  })
  .refine((d) => d.password === d.confirmPassword, {
    message: "As senhas não coincidem.",
    path: ["confirmPassword"],
  });

export async function changePassword(_: AuthState, formData: FormData): Promise<AuthState> {
  const user = await getCurrentUser();
  if (!user) redirect("/login");

  const parsed = ChangePasswordSchema.safeParse(Object.fromEntries(formData));
  if (!parsed.success) return { errors: z.flattenError(parsed.error).fieldErrors as Record<string, string[]> };

  const { password } = parsed.data;
  const passwordHash = await hashPassword(password);

  await db.user.update({
    where: { id: user.id },
    data: {
      passwordHash,
      mustChangePassword: false,
    },
  });

  redirect("/");
}

const ForgotPasswordSchema = z.object({
  email: z.email("Informe um e-mail válido.").trim().toLowerCase(),
});

export async function requestPasswordReset(_: AuthState, formData: FormData): Promise<AuthState> {
  const parsed = ForgotPasswordSchema.safeParse(Object.fromEntries(formData));
  if (!parsed.success) return { errors: z.flattenError(parsed.error).fieldErrors as Record<string, string[]> };

  const { email } = parsed.data;
  if (tooManyAttempts(`reset:${email}`)) {
    return { message: "Muitas solicitações recentes. Aguarde alguns minutos." };
  }
  registerFailure(`reset:${email}`);

  const user = await db.user.findUnique({ where: { email } });
  if (user) {
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
  }

  // Mensagem segura genérica para evitar enumeração de e-mails
  return {
    success: true,
    message: "Se o e-mail informado estiver cadastrado, uma nova senha temporária foi enviada. Verifique sua caixa de entrada e a pasta de spam.",
  };
}
