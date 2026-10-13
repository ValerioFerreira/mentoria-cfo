import "server-only";
import type { Contest, OnlineCharge, OnlineChargeStatus, PaymentMethod } from "@/generated/prisma/client";
import { approveWaitlistEntry } from "@/lib/admin/approve-core";
import { mercadoPagoConfigured, mercadoPagoToken, mpRequest, MercadoPagoError, notificationUrl, siteUrl } from "@/lib/billing/mercado-pago";
import { db } from "@/lib/db";
import { audit } from "./audit";
import { grantAccessUntilExam, revokeAccessAfterFullReversal } from "./contracts";
import { CommerceError } from "./errors";
import { fromCents, toCents } from "./money";
import { registerProviderPayment, reverseProviderPayment } from "./payments";

/**
 * Cobrança online pela conta Mercado Pago da empresa. Fluxo:
 *   1. o servidor calcula o saldo da contratação (o navegador nunca envia valor) e cria a cobrança no Mercado Pago;
 *   2. o cliente paga; o Mercado Pago avisa pelo webhook assinado;
 *   3. a aprovação é CONSULTADA na API autenticada e só então vira recebimento no mesmo livro-caixa dos lançamentos
 *      manuais (comissão do parceiro, estorno e acesso até a prova seguem as mesmas regras de lib/commerce).
 */

const DAY_MS = 86_400_000;
const PIX_TTL_MS = DAY_MS;
const CHECKOUT_TTL_MS = 2 * DAY_MS;
/** descrição na fatura do cartão (máx. 22 caracteres) */
const STATEMENT_DESCRIPTOR = "MISSAOMENTORIA";

export interface MpPayment {
  id: number | string;
  status: string;
  status_detail?: string | null;
  transaction_amount: number | string;
  transaction_amount_refunded?: number | string | null;
  currency_id: string;
  external_reference?: string | null;
  metadata?: { contract_id?: string; charge_id?: string } | null;
  date_approved?: string | null;
  date_last_updated?: string | null;
  date_of_expiration?: string | null;
  payment_method_id?: string | null;
  payment_type_id?: string | null;
  point_of_interaction?: { transaction_data?: { qr_code?: string; qr_code_base64?: string; ticket_url?: string } };
}

export type ChargeView = Pick<OnlineCharge, "id" | "kind" | "status" | "checkoutUrl" | "qrCode" | "qrCodeBase64" | "ticketUrl" | "expiresAt"> & { amountCents: number };

function view(c: OnlineCharge): ChargeView {
  return {
    id: c.id,
    kind: c.kind,
    status: c.status,
    checkoutUrl: c.checkoutUrl,
    qrCode: c.qrCode,
    qrCodeBase64: c.qrCodeBase64,
    ticketUrl: c.ticketUrl,
    expiresAt: c.expiresAt,
    amountCents: toCents(c.amount),
  };
}

/** O Mercado Pago pede data com deslocamento; usamos o horário de Recife (UTC−3). */
function recifeIso(d: Date): string {
  return `${new Date(d.getTime() - 3 * 3_600_000).toISOString().slice(0, 23)}-03:00`;
}

function centsOf(value: number | string | null | undefined): number {
  const n = Number(value ?? 0);
  if (!Number.isFinite(n) || n < 0) throw new Error("Invalid Mercado Pago amount");
  return Math.round(n * 100);
}

function assertOnline() {
  if (!mercadoPagoConfigured()) throw new CommerceError("O pagamento online ainda não está disponível. Tente novamente em breve.", "MP_NOT_CONFIGURED");
}

let accountOkUntil = 0;
/** Só para testes: esquece a conferência da conta. */
export function resetAccountCheck() {
  accountOkUntil = 0;
}

/**
 * Trava de segurança antes de abrir QUALQUER cobrança: o token precisa ser da conta do MERCADOPAGO_SELLER_ID e, com
 * credencial de produção, o titular não pode ser pessoa física (CPF). Assim um token antigo ou trocado nunca recebe
 * dinheiro por engano. Só o resultado positivo é guardado (10 min); qualquer dúvida recusa a cobrança.
 */
async function assertCompanyAccount() {
  if (Date.now() < accountOkUntil) return;
  let me: { id: number | string; identification?: { type?: string } };
  try {
    me = await mpRequest("/users/me");
  } catch (err) {
    return failure(err, "conferência da conta");
  }
  const seller = process.env.MERCADOPAGO_SELLER_ID?.trim();
  const live = !mercadoPagoToken().startsWith("TEST-");
  if ((seller && seller !== String(me.id)) || (live && me.identification?.type?.toUpperCase() === "CPF")) {
    console.error("[online-payment] conta do token não confere com a configuração (vendedor/CNPJ): cobrança recusada");
    throw new CommerceError("O pagamento online está indisponível no momento. Fale com a administração.", "MP_ACCOUNT_MISMATCH");
  }
  accountOkUntil = Date.now() + 10 * 60_000;
}

async function payableContract(contractId: string) {
  const c = await db.contract.findUnique({ where: { id: contractId } });
  if (!c) throw new CommerceError("Contratação não encontrada.");
  if (c.status === "CANCELLED") throw new CommerceError("Esta contratação foi cancelada.");
  const dueCents = toCents(c.finalAmount) - toCents(c.paidAmount);
  if (dueCents <= 0) throw new CommerceError("Esta contratação já está quitada.", "NOTHING_DUE");
  return { contract: c, dueCents };
}

/** Cobranças sem retorno do provedor (queda no meio da criação) deixam de ser reaproveitadas. */
async function dropStaleCharges(contractId: string, kind: "PIX" | "CHECKOUT") {
  await db.onlineCharge.updateMany({
    where: {
      contractId,
      kind,
      status: "PENDING",
      OR: [
        { providerPaymentId: null, preferenceId: null, createdAt: { lt: new Date(Date.now() - 5 * 60_000) } },
        { expiresAt: { lt: new Date() } },
      ],
    },
    data: { status: "EXPIRED" },
  });
}

function failure(err: unknown, what: string): never {
  console.error(`[online-payment] ${what} falhou`, { status: err instanceof MercadoPagoError ? err.status : undefined, error: err instanceof Error ? err.message : "erro desconhecido" });
  throw new CommerceError("Não foi possível gerar o pagamento agora. Tente novamente em instantes.", "MP_FAILED");
}

/** Pix dinâmico (QR Code e copia e cola) com o saldo da contratação. Reaproveita o Pix pendente do mesmo valor. */
export async function startPixCharge(contractId: string): Promise<ChargeView> {
  assertOnline();
  await assertCompanyAccount();
  const { contract, dueCents } = await payableContract(contractId);
  await dropStaleCharges(contractId, "PIX");
  const reusable = await db.onlineCharge.findFirst({
    where: { contractId, kind: "PIX", status: "PENDING", providerPaymentId: { not: null }, amount: fromCents(dueCents), expiresAt: { gt: new Date(Date.now() + 60_000) } },
    orderBy: { createdAt: "desc" },
  });
  if (reusable) return view(reusable);

  const charge = await db.onlineCharge.create({ data: { contractId, kind: "PIX", amount: fromCents(dueCents) } });
  try {
    const expires = new Date(Date.now() + PIX_TTL_MS);
    const p = await mpRequest<MpPayment>("/v1/payments", {
      method: "POST",
      headers: { "X-Idempotency-Key": charge.id },
      body: JSON.stringify({
        transaction_amount: dueCents / 100,
        description: `Acesso ilimitado até a prova · ${contract.contest}`,
        payment_method_id: "pix",
        payer: { email: contract.customerEmail },
        external_reference: contract.id,
        metadata: { contract_id: contract.id, charge_id: charge.id },
        notification_url: notificationUrl(),
        date_of_expiration: recifeIso(expires),
        statement_descriptor: STATEMENT_DESCRIPTOR,
      }),
    });
    const t = p.point_of_interaction?.transaction_data;
    if (!p.id || !t?.qr_code || !t.qr_code_base64) throw new Error("Mercado Pago did not return the Pix instructions");
    if (centsOf(p.transaction_amount) !== dueCents || p.currency_id !== "BRL") throw new Error("Mercado Pago returned a different amount");
    const saved = await db.onlineCharge.update({
      where: { id: charge.id },
      data: {
        providerPaymentId: String(p.id),
        qrCode: t.qr_code,
        qrCodeBase64: t.qr_code_base64,
        ticketUrl: t.ticket_url ?? null,
        expiresAt: p.date_of_expiration ? new Date(p.date_of_expiration) : expires,
      },
    });
    return view(saved);
  } catch (err) {
    await db.onlineCharge.update({ where: { id: charge.id }, data: { status: "CANCELLED" } });
    return failure(err, "criação do Pix");
  }
}

/** Checkout Pro: página do Mercado Pago para cartão (à vista). O cartão nunca passa por este sistema. */
export async function startCardCheckout(contractId: string): Promise<ChargeView> {
  assertOnline();
  await assertCompanyAccount();
  const { contract, dueCents } = await payableContract(contractId);
  await dropStaleCharges(contractId, "CHECKOUT");
  const reusable = await db.onlineCharge.findFirst({
    where: { contractId, kind: "CHECKOUT", status: "PENDING", checkoutUrl: { not: null }, amount: fromCents(dueCents), expiresAt: { gt: new Date(Date.now() + 60_000) } },
    orderBy: { createdAt: "desc" },
  });
  if (reusable) return view(reusable);

  const charge = await db.onlineCharge.create({ data: { contractId, kind: "CHECKOUT", amount: fromCents(dueCents) } });
  try {
    const expires = new Date(Date.now() + CHECKOUT_TTL_MS);
    const back = new URL(`/pagamentos/retorno?contrato=${encodeURIComponent(contract.id)}`, siteUrl()).toString();
    const pref = await mpRequest<{ id: string; init_point: string }>("/checkout/preferences", {
      method: "POST",
      headers: { "X-Idempotency-Key": charge.id },
      body: JSON.stringify({
        items: [{ id: contract.id, title: "Acesso ilimitado até a prova", quantity: 1, currency_id: "BRL", unit_price: dueCents / 100 }],
        payer: { email: contract.customerEmail },
        external_reference: contract.id,
        metadata: { contract_id: contract.id, charge_id: charge.id },
        notification_url: notificationUrl(),
        back_urls: { success: back, pending: back, failure: back },
        auto_return: "approved",
        statement_descriptor: STATEMENT_DESCRIPTOR,
        payment_methods: { installments: 1, excluded_payment_types: [{ id: "ticket" }, { id: "atm" }] },
        expires: true,
        expiration_date_to: recifeIso(expires),
      }),
    });
    if (!pref.id || !pref.init_point) throw new Error("Mercado Pago did not return the checkout");
    const saved = await db.onlineCharge.update({ where: { id: charge.id }, data: { preferenceId: pref.id, checkoutUrl: pref.init_point, expiresAt: expires } });
    return view(saved);
  } catch (err) {
    await db.onlineCharge.update({ where: { id: charge.id }, data: { status: "CANCELLED" } });
    return failure(err, "criação do checkout");
  }
}

/** Cancela no Mercado Pago os Pix pendentes de uma contratação que deixou de valer (melhor esforço). */
export async function cancelPendingCharges(contractId: string): Promise<void> {
  const pending = await db.onlineCharge.findMany({ where: { contractId, status: "PENDING" } });
  for (const c of pending) {
    await db.onlineCharge.update({ where: { id: c.id }, data: { status: "CANCELLED" } });
    if (c.kind === "PIX" && c.providerPaymentId && mercadoPagoConfigured()) {
      try {
        await mpRequest(`/v1/payments/${encodeURIComponent(c.providerPaymentId)}`, { method: "PUT", body: JSON.stringify({ status: "cancelled" }) });
      } catch (err) {
        console.error("[online-payment] cancelamento do Pix não confirmado", { status: err instanceof MercadoPagoError ? err.status : undefined });
      }
    }
  }
}

export interface SyncResult {
  contractId: string;
  status: string;
  detail: string | null;
  /** o que a conciliação fez neste evento */
  outcome: "RECEIVED" | "REVERSED" | "UNCHANGED" | "PENDING" | "CLOSED" | "NEEDS_REVIEW";
}

const MONEY_STATUSES = new Set(["approved", "refunded", "charged_back", "in_mediation"]);

function chargeStatusOf(p: MpPayment): OnlineChargeStatus {
  const detail = (p.status_detail ?? "").toLowerCase();
  switch (p.status.toLowerCase()) {
    case "approved":
      return centsOf(p.transaction_amount_refunded) > 0 ? "REFUNDED" : "APPROVED";
    case "refunded":
      return "REFUNDED";
    case "charged_back":
    case "in_mediation":
      return "CHARGED_BACK";
    case "rejected":
      return "REJECTED";
    case "cancelled":
      return detail.includes("expired") ? "EXPIRED" : "CANCELLED";
    default:
      return "PENDING";
  }
}

async function logOnce(contractId: string, action: string, providerPaymentId: string, data: Record<string, string | number | null>) {
  const done = await db.auditLog.findFirst({
    where: { entityType: "Contract", entityId: contractId, action, data: { path: ["providerPaymentId"], equals: providerPaymentId } },
    select: { id: true },
  });
  if (done) return;
  await db.$transaction((tx) => audit(tx, { actorId: null, action, entityType: "Contract", entityId: contractId, data: { providerPaymentId, ...data } }));
}

/**
 * Concilia UM pagamento do Mercado Pago (já consultado na API autenticada) com a contratação.
 * Devolve null quando o pagamento não pertence a nenhuma contratação (cobranças antigas seguem o fluxo legado).
 * Idempotente: repetir o mesmo evento, ou receber eventos fora de ordem, não duplica recebimentos nem estornos.
 */
export async function syncContractPayment(p: MpPayment): Promise<SyncResult | null> {
  const ref = p.metadata?.contract_id ?? p.external_reference ?? null;
  const contract = ref ? await db.contract.findUnique({ where: { id: ref } }) : null;
  if (!contract) return null;
  // só vale pagamento de uma contratação para a qual ESTE sistema abriu uma cobrança
  const opened = await db.onlineCharge.count({ where: { contractId: contract.id } });
  if (opened === 0) return null;

  if (p.currency_id !== "BRL") throw new Error("Payment currency does not match the contract");
  const providerId = String(p.id);
  const status = p.status.toLowerCase();
  const detail = p.status_detail ?? null;
  const chargeStatus = chargeStatusOf(p);

  const touchCharge = async () => {
    // Pix: a cobrança é este pagamento. Checkout Pro: várias tentativas dividem a preferência, então só os estados
    // com dinheiro (aprovado/estornado/contestado) a fecham; uma tentativa recusada não a invalida.
    const moneyState = chargeStatus === "APPROVED" || chargeStatus === "REFUNDED" || chargeStatus === "CHARGED_BACK";
    await db.onlineCharge.updateMany({
      where: {
        contractId: contract.id,
        OR: [
          { kind: "PIX", providerPaymentId: providerId },
          ...(moneyState && p.metadata?.charge_id ? [{ kind: "CHECKOUT" as const, id: p.metadata.charge_id }] : []),
        ],
      },
      data: { status: chargeStatus },
    });
  };

  const approvedAt = p.date_approved ? new Date(p.date_approved) : null;
  if (!approvedAt || !MONEY_STATUSES.has(status)) {
    // ainda sem dinheiro: pendente, recusado ou cancelado/vencido
    await touchCharge();
    return { contractId: contract.id, status, detail, outcome: chargeStatus === "PENDING" ? "PENDING" : "CLOSED" };
  }

  const amountCents = centsOf(p.transaction_amount);
  if (amountCents <= 0) throw new Error("Payment amount is not positive");
  const method: PaymentMethod = p.payment_method_id === "pix" ? "PIX" : "CARTAO";

  let received;
  try {
    received = await registerProviderPayment(
      {
        contractId: contract.id,
        amountCents,
        paidAt: approvedAt,
        method,
        receiptRef: `MP-${providerId}`,
        note: `Mercado Pago · ${p.payment_method_id ?? p.payment_type_id ?? "online"}`,
        idempotencyKey: `mp:payment:${providerId}`,
      },
      { providerPaymentId: providerId },
    );
  } catch (err) {
    if (err instanceof CommerceError && err.code === "CONTRACT_CANCELLED") {
      // dinheiro real numa contratação cancelada: não perder o aviso nem ficar repetindo o evento
      await touchCharge();
      await logOnce(contract.id, "PAYMENT_ON_CANCELLED_CONTRACT", providerId, { amount: fromCents(amountCents) });
      console.error("[online-payment] pagamento aprovado em contratação cancelada: revisar e devolver", { contractId: contract.id });
      return { contractId: contract.id, status, detail, outcome: "NEEDS_REVIEW" };
    }
    throw err;
  }
  let outcome: SyncResult["outcome"] = received.duplicate ? "UNCHANGED" : "RECEIVED";

  // estornos: total, parcial ou contestação perdida (em análise ou ganha não revoga nada)
  const refunded = centsOf(p.transaction_amount_refunded);
  const lost = status === "charged_back" && (detail ?? "").toLowerCase() === "reimbursed";
  const targetCents = status === "refunded" || lost ? amountCents : Math.min(refunded, amountCents);
  if (targetCents > 0) {
    const payment = await db.manualPayment.findUniqueOrThrow({ where: { id: received.paymentId }, include: { reversals: { select: { amount: true } } } });
    const already = payment.reversals.reduce((sum, r) => sum + toCents(r.amount), 0);
    const delta = targetCents - already;
    if (delta > 0) {
      await reverseProviderPayment({
        paymentId: payment.id,
        amountCents: delta,
        kind: "ESTORNO",
        reason: lost ? "Contestação (chargeback) perdida no Mercado Pago" : status === "refunded" ? "Reembolso total no Mercado Pago" : "Reembolso parcial no Mercado Pago",
        effectiveAt: p.date_last_updated ? new Date(p.date_last_updated) : new Date(),
        idempotencyKey: `mp:refund:${providerId}:${targetCents}`,
      });
      outcome = "REVERSED";
    }
  }

  await touchCharge();

  // acesso: quitou e a conta já existe => libera até a prova; ficou sem nada recebido => encerra o que esta contratação deu
  const fresh = await db.contract.findUniqueOrThrow({ where: { id: contract.id } });
  if (toCents(fresh.paidAmount) <= 0) {
    await revokeAccessAfterFullReversal(fresh.id, lost ? "Contestação perdida" : "Reembolso total");
  } else if ((fresh.status === "PAID" || fresh.status === "OVERPAID") && fresh.userId && !fresh.accessGrantedAt) {
    try {
      await grantAccessUntilExam(fresh.id, null);
    } catch (err) {
      // p.ex. data da prova ainda não cadastrada: o recebimento fica registrado e o administrador libera depois
      if (!(err instanceof CommerceError)) throw err;
      await logOnce(fresh.id, "ACCESS_GRANT_PENDING", providerId, { code: err.code });
    }
  } else if ((fresh.status === "PAID" || fresh.status === "OVERPAID") && !fresh.userId) {
    await approveWaitlistAfterPayment(fresh, providerId);
  }
  return { contractId: contract.id, status, detail, outcome };
}

/**
 * Inscrição da lista de espera quitada: cria a conta e libera o acesso até a prova sem esperar o administrador
 * (mesmo caminho da aprovação manual). Se algo impede (data da prova pendente, e-mail de administrador/parceiro),
 * o pagamento fica registrado e o motivo vai para os pontos de atenção; o administrador aprova depois em Cadastros.
 */
async function approveWaitlistAfterPayment(c: { id: string; customerEmail: string; contest: Contest; waitlistEntryId: string | null }, providerId: string) {
  const entry = c.waitlistEntryId
    ? await db.waitlistEntry.findUnique({ where: { id: c.waitlistEntryId }, select: { id: true, status: true } })
    : await db.waitlistEntry.findFirst({ where: { email: c.customerEmail, contest: c.contest }, select: { id: true, status: true } });
  if (!entry || entry.status !== "PENDING") return;
  const r = await approveWaitlistEntry({ entryId: entry.id, duration: "UNTIL_EXAM", actorId: null, onlyIfPending: true });
  if (!r.success && r.code !== "ALREADY_HANDLED") await logOnce(c.id, "ACCESS_GRANT_PENDING", providerId, { code: r.code ?? "UNKNOWN" });
}

/** Consulta o pagamento na API autenticada e concilia. */
export async function syncProviderPayment(paymentId: string): Promise<SyncResult | null> {
  const p = await mpRequest<MpPayment>(`/v1/payments/${encodeURIComponent(paymentId)}`);
  return syncContractPayment(p);
}

/**
 * Reconsulta no Mercado Pago os Pix ainda pendentes (últimos dias): recupera avisos de webhook perdidos ou atrasados
 * e fecha os vencidos. Usado pelo botão do Financeiro e pela página de pagamento do cliente.
 */
export async function reconcilePendingCharges(opts: { contractId?: string; limit?: number; minAgeMs?: number } = {}) {
  assertOnline();
  const pending = await db.onlineCharge.findMany({
    where: {
      status: "PENDING",
      kind: "PIX",
      providerPaymentId: { not: null },
      ...(opts.contractId ? { contractId: opts.contractId } : {}),
      createdAt: { gt: new Date(Date.now() - 4 * DAY_MS) },
      ...(opts.minAgeMs ? { updatedAt: { lt: new Date(Date.now() - opts.minAgeMs) } } : {}),
    },
    orderBy: { createdAt: "asc" },
    take: opts.limit ?? 25,
  });
  const out = { checked: 0, received: 0, errors: 0 };
  for (const c of pending) {
    out.checked += 1;
    try {
      const r = await syncProviderPayment(c.providerPaymentId!);
      if (r?.outcome === "RECEIVED" || r?.outcome === "REVERSED") out.received += 1;
      await db.onlineCharge.update({ where: { id: c.id }, data: { updatedAt: new Date() } });
    } catch (err) {
      out.errors += 1;
      console.error("[online-payment] reconciliação falhou", { status: err instanceof MercadoPagoError ? err.status : undefined });
    }
  }
  return out;
}

export interface AccountStatus {
  configured: boolean;
  webhookSecretSet: boolean;
  sellerIdSet: boolean;
  appUrl: string | null;
  /** resposta do próprio endereço do webhook a um aviso SEM assinatura: 401 = no ar e protegido; 3xx = o endereço redireciona (o Mercado Pago não segue redirecionamento) */
  webhook: { status: number | null; redirectTo: string | null };
  mode: "producao" | "teste" | null;
  account: null | { id: string; nickname: string | null; documentType: string | null; matchesSellerId: boolean | null };
  error: string | null;
}

/** Diagnóstico para o administrador conferir QUAL conta está conectada (empresa × CPF) sem expor segredos. */
export async function mercadoPagoAccountStatus(): Promise<AccountStatus> {
  const status: AccountStatus = {
    configured: mercadoPagoConfigured(),
    webhookSecretSet: Boolean(process.env.MERCADOPAGO_WEBHOOK_SECRET),
    sellerIdSet: Boolean(process.env.MERCADOPAGO_SELLER_ID),
    appUrl: null,
    webhook: { status: null, redirectTo: null },
    mode: null,
    account: null,
    error: null,
  };
  try {
    status.appUrl = siteUrl().origin;
  } catch {
    status.error = "APP_URL não configurada.";
  }
  if (status.appUrl) {
    try {
      const r = await fetch(notificationUrl(), { method: "POST", redirect: "manual", headers: { "content-type": "application/json" }, body: "{}", signal: AbortSignal.timeout(8000), cache: "no-store" });
      status.webhook.status = r.status;
      status.webhook.redirectTo = r.status >= 300 && r.status < 400 ? r.headers.get("location") : null;
    } catch {
      /* sem resposta: aparece como "não verificado" */
    }
  }
  let token: string;
  try {
    token = mercadoPagoToken();
  } catch {
    status.error = status.error ?? "Token do Mercado Pago não configurado.";
    return status;
  }
  status.mode = token.startsWith("TEST-") ? "teste" : "producao";
  try {
    const me = await mpRequest<{ id: number | string; nickname?: string; identification?: { type?: string } }>("/users/me");
    const seller = process.env.MERCADOPAGO_SELLER_ID;
    status.account = {
      id: String(me.id),
      nickname: me.nickname ?? null,
      documentType: me.identification?.type?.toUpperCase() ?? null,
      matchesSellerId: seller ? seller.trim() === String(me.id) : null,
    };
  } catch (err) {
    status.error = err instanceof MercadoPagoError ? `O Mercado Pago recusou o token (HTTP ${err.status}).` : "Não foi possível consultar o Mercado Pago.";
  }
  return status;
}


/** Números do painel do administrador: Pix aguardando pagamento e ocorrências que pedem ação (últimos 60 dias). */
export async function onlineOverview() {
  const now = Date.now();
  const [pending, alerts] = await Promise.all([
    db.onlineCharge.count({ where: { status: "PENDING", providerPaymentId: { not: null }, expiresAt: { gt: new Date(now) } } }),
    db.auditLog.findMany({
      where: { action: { in: ["PAYMENT_ON_CANCELLED_CONTRACT", "ACCESS_GRANT_PENDING", "ACCESS_REVIEW_NEEDED", "AUTO_APPROVAL_EMAIL_FAILED"] }, createdAt: { gt: new Date(now - 60 * DAY_MS) } },
      orderBy: { createdAt: "desc" },
      take: 20,
    }),
  ]);
  return { pending, alerts };
}
