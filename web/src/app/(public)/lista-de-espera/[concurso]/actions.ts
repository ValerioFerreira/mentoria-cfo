"use server";

import { headers } from "next/headers";
import * as z from "zod";
import { registerFailure, tooManyAttempts } from "@/lib/auth/rate-limit";
import { contestBySlug } from "@/lib/contests";
import { db } from "@/lib/db";
import { mercadoPagoConfigured } from "@/lib/billing/mercado-pago";
import { createContract, previewContract } from "@/lib/commerce/contracts";
import { cancelPendingCharges, startPixCharge } from "@/lib/commerce/online";
import { CommerceError } from "@/lib/commerce/errors";
import { formatBRL, fromCents, toCents } from "@/lib/commerce/money";
import { buildPixPayload, pixConfig, pixQrDataUri } from "@/lib/pix";

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

export interface PaymentInfo {
  payload: string;
  qr: string;
  email: string;
  plan: string;
  /** valor a pagar agora (saldo da contratação), ex.: "42,00" */
  amount: string;
  original: string;
  discounts: string;
  couponCode: string | null;
  alreadyJoined: boolean;
  txId: string;
}

export type JoinState =
  | undefined
  | {
      errors?: Record<string, string[]>;
      message?: string;
      /** pagamento a exibir depois do cadastro */
      payment?: PaymentInfo;
    };

const JoinSchema = z.object({
  name: z.string().trim().min(5, "Informe o nome completo.").max(120, "Nome muito longo."),
  email: z.email("E-mail inválido.").trim().toLowerCase().max(60, "Use um e-mail com até 60 caracteres."),
  username: z.string().trim().toLowerCase(),
  coupon: z.string().trim().max(20, "Cupom inválido.").optional(),
});

/**
 * Pix com o saldo da contratação, calculado no servidor. Com o Mercado Pago configurado (conta da empresa) o Pix é
 * dinâmico e a confirmação é automática; sem ele, vale o Pix estático (PIX_KEY) conferido pela administração.
 */
async function paymentFor(contractId: string, alreadyJoined: boolean): Promise<PaymentInfo | null> {
  const c = await db.contract.findUniqueOrThrow({ where: { id: contractId } });
  const due = toCents(c.finalAmount) - toCents(c.paidAmount);
  if (due <= 0) return null;
  let payload: string | null = null;
  let qr: string | null = null;
  let txId = c.customerEmail.replace(/[^a-zA-Z0-9]/g, "").slice(0, 25) || "ALUNO";
  if (mercadoPagoConfigured()) {
    try {
      const charge = await startPixCharge(contractId);
      if (charge.qrCode && charge.qrCodeBase64) {
        payload = charge.qrCode;
        qr = charge.qrCodeBase64.startsWith("data:") ? charge.qrCodeBase64 : `data:image/png;base64,${charge.qrCodeBase64}`;
        txId = charge.id;
      }
    } catch (err) {
      if (!(err instanceof CommerceError) && !pixConfig()) throw err;
    }
  }
  if (!payload || !qr) {
    const cfg = pixConfig();
    if (!cfg) return null;
    payload = buildPixPayload({ ...cfg, amount: fromCents(due) }, c.customerEmail, txId);
    qr = await pixQrDataUri(payload);
  }
  return {
    payload,
    qr,
    email: c.customerEmail,
    plan: "Acesso ilimitado até a prova",
    amount: formatBRL(due).replace("R$ ", ""),
    original: formatBRL(toCents(c.originalAmount)),
    discounts: `${c.launchDiscountPoints}% de lançamento${c.partnerDiscountPoints ? ` + ${c.partnerDiscountPoints}% do cupom ${c.couponCode}` : ""}`,
    couponCode: c.couponCode,
    alreadyJoined,
    txId,
  };
}

async function clientKey(): Promise<string> {
  const h = await headers();
  const ip = h.get("x-forwarded-for")?.split(",")[0]?.trim() || h.get("x-real-ip") || "local";
  return `waitlist:${ip}`;
}

function contractError(err: unknown): JoinState {
  if (err instanceof CommerceError) {
    if (err.code === "COUPON_INVALID" || err.code === "SELF_REFERRAL" || err.code === "CONTRACT_LOCKED") return { errors: { coupon: [err.message] } };
    return { message: err.message };
  }
  console.error("[waitlist] contratação falhou", err instanceof Error ? err.message : "erro desconhecido");
  return { message: "Não foi possível registrar a contratação agora. Tente novamente em instantes." };
}

export async function joinWaitlist(slug: string, _: JoinState, formData: FormData): Promise<JoinState> {
  const contest = contestBySlug(slug);
  if (!contest) return { message: "Concurso não encontrado." };
  if (!pixConfig() && !mercadoPagoConfigured()) return { message: "O pagamento por Pix ainda não está configurado. Tente novamente em breve." };

  const key = await clientKey();
  if (tooManyAttempts(key)) return { message: "Muitas tentativas. Aguarde alguns minutos e tente novamente." };
  registerFailure(key); // conta toda tentativa: o limite é por envio, não por erro (também freia tentativas de cupom)

  const parsed = JoinSchema.safeParse(Object.fromEntries(formData));
  if (!parsed.success) return { errors: z.flattenError(parsed.error).fieldErrors as Record<string, string[]> };
  const { name, email, username, coupon } = parsed.data;

  // quem já está na lista para este concurso revê o pagamento (sem duplicar a obrigação)
  const existing = await db.waitlistEntry.findUnique({ where: { contest_email: { contest: contest.key, email } } });
  if (existing) {
    try {
      const r = await createContract({ contest: contest.key, customerEmail: email, customerName: existing.name, waitlistEntryId: existing.id, couponCode: coupon }, null);
      if (r.replacedId) await cancelPendingCharges(r.replacedId);
      const payment = await paymentFor(r.contractId, true);
      if (!payment) return { message: "O pagamento desta inscrição já foi registrado. Aguarde o e-mail com o seu acesso." };
      return { payment };
    } catch (err) {
      return contractError(err);
    }
  }

  if (await db.user.findUnique({ where: { email }, select: { id: true } })) {
    return { errors: { email: ["Este e-mail já tem acesso ao MentorIA. Entre com a sua senha."] } };
  }
  const check = await checkUsername(username);
  if (!check.available) return { errors: { username: [check.message] } };

  // categoria e cupom conferidos antes de gravar a inscrição
  try {
    await previewContract(contest.key, email, coupon);
  } catch (err) {
    return contractError(err);
  }

  let entryId: string;
  try {
    entryId = (await db.waitlistEntry.create({ data: { contest: contest.key, name, email, username, plan: "UNTIL_EXAM" } })).id;
  } catch {
    // corrida entre duas pessoas escolhendo o mesmo usuário
    return { errors: { username: ["Este nome de usuário já está em uso."] } };
  }
  try {
    const r = await createContract({ contest: contest.key, customerEmail: email, customerName: name, waitlistEntryId: entryId, couponCode: coupon }, null);
    if (r.replacedId) await cancelPendingCharges(r.replacedId);
    const payment = await paymentFor(r.contractId, false);
    return payment ? { payment } : { message: "Inscrição registrada." };
  } catch (err) {
    return contractError(err);
  }
}
