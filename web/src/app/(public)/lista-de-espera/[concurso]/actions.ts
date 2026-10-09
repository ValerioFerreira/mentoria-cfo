"use server";

import { headers } from "next/headers";
import * as z from "zod";
import type { WaitlistPlan } from "@/generated/prisma/client";
import { registerFailure, tooManyAttempts } from "@/lib/auth/rate-limit";
import { contestBySlug } from "@/lib/contests";
import { db } from "@/lib/db";
import { buildPixPayload, pixConfig, pixQrDataUri, type PixConfig } from "@/lib/pix";
import { PLAN_KEYS, WAITLIST_PLANS } from "@/lib/plans";

/** Nome de usuário: 3 a 20 caracteres, minúsculas, números, ponto, hífen e sublinhado. */
const USERNAME = /^[a-z0-9][a-z0-9._-]{2,19}$/;

export type UsernameCheck = { available: boolean; message: string };

export async function checkUsername(raw: string): Promise<UsernameCheck> {
  const username = raw.trim().toLowerCase();
  if (!USERNAME.test(username)) return { available: false, message: "Use de 3 a 20 caracteres: letras minúsculas, números, ponto, hífen ou sublinhado." };
  const [user, entry] = await Promise.all([
    db.user.findUnique({ where: { username }, select: { id: true } }),
    db.waitlistEntry.findUnique({ where: { username }, select: { id: true } }),
  ]);
  if (user || entry) return { available: false, message: "Este nome de usuário já está em uso." };
  return { available: true, message: "Nome de usuário disponível." };
}

export type JoinState =
  | undefined
  | {
      errors?: Record<string, string[]>;
      message?: string;
      /** pagamento a exibir depois do cadastro */
      payment?: { payload: string; qr: string; email: string; plan: string; amount: string; alreadyJoined: boolean; txId: string };
    };

const JoinSchema = z.object({
  name: z.string().trim().min(5, "Informe o nome completo.").max(120, "Nome muito longo."),
  email: z.email("E-mail inválido.").trim().toLowerCase().max(60, "Use um e-mail com até 60 caracteres."),
  username: z.string().trim().toLowerCase(),
  plan: z.enum(PLAN_KEYS, { error: "Escolha um plano." }),
});

/** Código Pix e QR Code do plano escolhido (a mensagem do Pix é o e-mail). */
async function paymentFor(cfg: PixConfig, planKey: WaitlistPlan, email: string, alreadyJoined: boolean, username?: string) {
  const plan = WAITLIST_PLANS[planKey];
  const cleanId = (username ? `CFO${username}` : `CFO${email.split("@")[0]}`).replace(/[^a-zA-Z0-9]/g, "").slice(0, 25);
  const payload = buildPixPayload({ ...cfg, amount: plan.amount }, email, cleanId);
  return { payload, qr: await pixQrDataUri(payload), email, plan: plan.name, amount: plan.price, alreadyJoined, txId: cleanId };
}

async function clientKey(): Promise<string> {
  const h = await headers();
  const ip = h.get("x-forwarded-for")?.split(",")[0]?.trim() || h.get("x-real-ip") || "local";
  return `waitlist:${ip}`;
}

export async function joinWaitlist(slug: string, _: JoinState, formData: FormData): Promise<JoinState> {
  const contest = contestBySlug(slug);
  if (!contest) return { message: "Concurso não encontrado." };
  const cfg = pixConfig();
  if (!cfg) return { message: "O pagamento por Pix ainda não está configurado. Tente novamente em breve." };

  const key = await clientKey();
  if (tooManyAttempts(key)) return { message: "Muitas tentativas. Aguarde alguns minutos e tente novamente." };
  registerFailure(key); // conta toda tentativa: o limite é por envio, não por erro

  const parsed = JoinSchema.safeParse(Object.fromEntries(formData));
  if (!parsed.success) return { errors: z.flattenError(parsed.error).fieldErrors as Record<string, string[]> };
  const { name, email, username, plan } = parsed.data;

  // quem já está na lista para este concurso só revê o pagamento (sem criar duplicata); se ainda não pagou, vale o plano escolhido agora
  const existing = await db.waitlistEntry.findUnique({ where: { contest_email: { contest: contest.key, email } } });
  if (existing) {
    // com o Pix já conferido, o plano que vale é o que foi pago
    const effective = existing.paidAt && existing.plan ? existing.plan : plan;
    if (!existing.paidAt && existing.plan !== plan) await db.waitlistEntry.update({ where: { id: existing.id }, data: { plan } });
    return { payment: await paymentFor(cfg, effective, email, true, existing.username) };
  }

  if (await db.user.findUnique({ where: { email }, select: { id: true } })) {
    return { errors: { email: ["Este e-mail já tem acesso ao MentorIA. Entre com a sua senha."] } };
  }
  const check = await checkUsername(username);
  if (!check.available) return { errors: { username: [check.message] } };

  try {
    await db.waitlistEntry.create({ data: { contest: contest.key, name, email, username, plan } });
  } catch {
    // corrida entre duas pessoas escolhendo o mesmo usuário
    return { errors: { username: ["Este nome de usuário já está em uso."] } };
  }
  return { payment: await paymentFor(cfg, plan, email, false, username) };
}
