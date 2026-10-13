"use server";

// Pagamento online da contratação (Mercado Pago, conta da empresa). Só o id da contratação vem do navegador:
// valor, descontos e dono são conferidos no servidor, e a contratação precisa ser do usuário da sessão.
import { revalidatePath } from "next/cache";
import { getCurrentUser } from "@/lib/auth/session";
import { db } from "@/lib/db";
import { type ActionResult, toActionError } from "./errors";
import { toCents } from "./money";
import { reconcilePendingCharges, startCardCheckout, startPixCharge, type ChargeView } from "./online";

async function ownContractId(contractId: unknown): Promise<string | null> {
  const user = await getCurrentUser();
  if (!user || typeof contractId !== "string" || contractId.length > 64) return null;
  const c = await db.contract.findFirst({
    where: { id: contractId, OR: [{ userId: user.id }, { customerEmail: user.email.toLowerCase() }] },
    select: { id: true },
  });
  return c?.id ?? null;
}

export type PixPayload = { qrCode: string; qrCodeBase64: string; expiresAt: string | null; amountCents: number };

export async function createPix(contractId: string): Promise<ActionResult<PixPayload>> {
  const id = await ownContractId(contractId);
  if (!id) return { ok: false, message: "Contratação não encontrada." };
  try {
    const c: ChargeView = await startPixCharge(id);
    if (!c.qrCode || !c.qrCodeBase64) return { ok: false, message: "Não foi possível gerar o Pix agora. Tente novamente." };
    return { ok: true, message: "Pix gerado.", data: { qrCode: c.qrCode, qrCodeBase64: c.qrCodeBase64, expiresAt: c.expiresAt?.toISOString() ?? null, amountCents: c.amountCents } };
  } catch (err) {
    return toActionError(err, "gerar Pix");
  }
}

export async function createCardCheckout(contractId: string): Promise<ActionResult<{ url: string }>> {
  const id = await ownContractId(contractId);
  if (!id) return { ok: false, message: "Contratação não encontrada." };
  try {
    const c = await startCardCheckout(id);
    if (!c.checkoutUrl) return { ok: false, message: "Não foi possível abrir o pagamento por cartão agora." };
    return { ok: true, message: "Redirecionando…", data: { url: c.checkoutUrl } };
  } catch (err) {
    return toActionError(err, "abrir checkout");
  }
}

export type PaymentProgress = { paid: boolean; dueCents: number; status: string };

/** Acompanhamento da página de pagamento: reconsulta o Pix pendente (cobre webhook atrasado) e devolve o saldo. */
export async function checkPayment(contractId: string): Promise<ActionResult<PaymentProgress>> {
  const id = await ownContractId(contractId);
  if (!id) return { ok: false, message: "Contratação não encontrada." };
  try {
    await reconcilePendingCharges({ contractId: id, minAgeMs: 4000, limit: 3 });
  } catch (err) {
    // indisponibilidade do provedor não impede mostrar o saldo atual
    console.error("[online-payment] acompanhamento", err instanceof Error ? err.message : "erro");
  }
  const c = await db.contract.findUniqueOrThrow({ where: { id }, select: { finalAmount: true, paidAmount: true, status: true } });
  const dueCents = toCents(c.finalAmount) - toCents(c.paidAmount);
  if (dueCents <= 0) revalidatePath("/pagamentos");
  return { ok: true, message: "", data: { paid: dueCents <= 0 && c.status !== "CANCELLED", dueCents: Math.max(0, dueCents), status: c.status } };
}
