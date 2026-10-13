import "server-only";
import type { Contest, Prisma } from "@/generated/prisma/client";
import { db } from "@/lib/db";
import { audit } from "./audit";
import { CommerceError } from "./errors";
import { fromCents, toCents } from "./money";
import { accessEndForExamDate, quote } from "./pricing";

type Tx = Prisma.TransactionClient;

export const COUPON_CODE = /^[A-Z0-9]{4,20}$/;

export function normalizeCouponCode(raw: unknown): string | null {
  if (typeof raw !== "string") return null;
  const code = raw.trim().toUpperCase();
  return code ? code : null;
}

/** Trava por cliente dentro da transação: impede duas contratações simultâneas do mesmo e-mail. */
async function lockCustomer(tx: Tx, email: string) {
  await tx.$queryRaw`SELECT pg_advisory_xact_lock(hashtext(${`contract:${email}`}))::text`;
}

export async function lockContract(tx: Tx, contractId: string) {
  await tx.$queryRaw`SELECT "id" FROM "Contract" WHERE "id" = ${contractId} FOR UPDATE`;
}

/**
 * Valida o cupom para uma nova contratação. Recusa: inexistente, desativado, parceiro desativado e autoindicação.
 * A mensagem é a mesma para inexistente/desativado (não revela quais códigos existem).
 */
export async function resolveCoupon(tx: Tx, code: string, customer: { email: string; userId?: string | null }) {
  if (!COUPON_CODE.test(code)) throw new CommerceError("Cupom inválido ou desativado.", "COUPON_INVALID");
  const coupon = await tx.partnerCoupon.findUnique({
    where: { code },
    include: { partner: { select: { id: true, active: true, userId: true, user: { select: { email: true } } } } },
  });
  if (!coupon || !coupon.active || !coupon.partner.active) throw new CommerceError("Cupom inválido ou desativado.", "COUPON_INVALID");
  if (coupon.partner.user.email.toLowerCase() === customer.email || (customer.userId && coupon.partner.userId === customer.userId)) {
    throw new CommerceError("O cupom de parceiro não pode ser usado pelo próprio parceiro.", "SELF_REFERRAL");
  }
  return coupon;
}

/** Oferta atual de um concurso (preço de lançamento sem cupom), ou motivo de indisponibilidade. */
export async function contestOffer(contest: Contest) {
  const setting = await db.contestSetting.findUnique({ where: { contest } });
  if (!setting?.category) return { available: false as const, examDate: setting?.examDate ?? null };
  return { available: true as const, category: setting.category, examDate: setting.examDate, quote: quote(setting.category) };
}

/** Confere categoria e cupom sem gravar nada (usado antes de criar a inscrição da lista de espera). */
export async function previewContract(contest: Contest, customerEmail: string, couponCode?: string | null) {
  const email = customerEmail.trim().toLowerCase();
  const code = normalizeCouponCode(couponCode);
  return db.$transaction(async (tx) => {
    const setting = await tx.contestSetting.findUnique({ where: { contest } });
    if (!setting?.category) throw new CommerceError("Este concurso está em revisão administrativa e ainda não pode ser contratado.", "CATEGORY_MISSING");
    const coupon = code ? await resolveCoupon(tx, code, { email }) : null;
    return quote(setting.category, coupon?.discountPoints ?? 0);
  });
}

export interface CreateContractInput {
  contest: Contest;
  customerEmail: string;
  customerName?: string | null;
  userId?: string | null;
  waitlistEntryId?: string | null;
  couponCode?: string | null;
}

export interface CreateContractResult {
  contractId: string;
  created: boolean;
  /** contratação anterior sem pagamento substituída (troca de cupom) */
  replacedId?: string;
}

/**
 * Registra a contratação de acesso até a prova (= obrigação financeira) com preço calculado no servidor.
 * Há no máximo uma contratação não cancelada por e-mail e concurso: repetir o pedido devolve a existente;
 * trocar o cupom só é possível enquanto nada foi recebido (a anterior fica cancelada no histórico).
 */
export async function createContract(input: CreateContractInput, actorId: string | null): Promise<CreateContractResult> {
  const email = input.customerEmail.trim().toLowerCase();
  const code = normalizeCouponCode(input.couponCode);
  return db.$transaction(async (tx) => {
    await lockCustomer(tx, email);
    const setting = await tx.contestSetting.findUnique({ where: { contest: input.contest } });
    if (!setting?.category) {
      throw new CommerceError("Este concurso está em revisão administrativa e ainda não pode ser contratado.", "CATEGORY_MISSING");
    }
    const coupon = code ? await resolveCoupon(tx, code, { email, userId: input.userId }) : null;

    const existing = await tx.contract.findFirst({
      where: { customerEmail: email, contest: input.contest, status: { not: "CANCELLED" } },
      orderBy: { createdAt: "desc" },
      include: { _count: { select: { payments: true } } },
    });
    let replacedId: string | undefined;
    if (existing) {
      if ((existing.couponId ?? null) === (coupon?.id ?? null) || (!coupon && existing.couponId)) {
        // mesmo pedido (ou pedido sem cupom sobre uma contratação com cupom): mantém o que já foi registrado
        if (input.userId && !existing.userId) await tx.contract.update({ where: { id: existing.id }, data: { userId: input.userId } });
        return { contractId: existing.id, created: false };
      }
      if (existing._count.payments > 0 || existing.accessGrantedAt) {
        throw new CommerceError("Já existe uma contratação com pagamento para este concurso; o cupom não pode mais ser alterado.", "CONTRACT_LOCKED");
      }
      await tx.contract.update({
        where: { id: existing.id },
        data: { status: "CANCELLED", cancelledAt: new Date(), cancelReason: "Substituída: cupom informado depois da inscrição." },
      });
      await audit(tx, { actorId, action: "CONTRACT_REPLACED", entityType: "Contract", entityId: existing.id, data: { reason: "coupon_changed" } });
      replacedId = existing.id;
    }

    const q = quote(setting.category, coupon?.discountPoints ?? 0);
    const contract = await tx.contract.create({
      data: {
        userId: input.userId ?? null,
        customerEmail: email,
        customerName: input.customerName?.trim() || null,
        waitlistEntryId: input.waitlistEntryId ?? null,
        contest: input.contest,
        category: q.category,
        examDateAtContract: setting.examDate,
        pricingRule: q.pricingRule,
        originalAmount: fromCents(q.originalCents),
        launchDiscountPoints: q.launchDiscountPoints,
        partnerDiscountPoints: q.partnerDiscountPoints,
        discountAmount: fromCents(q.discountCents),
        finalAmount: fromCents(q.finalCents),
        couponId: coupon?.id ?? null,
        couponCode: coupon?.code ?? null,
        partnerId: coupon?.partnerId ?? null,
      },
    });

    // atribuição: só pelo cupom, e o primeiro vínculo do cliente é mantido (nunca transferido)
    if (coupon) {
      const referral = await tx.partnerReferral.findUnique({ where: { customerEmail: email } });
      if (!referral) {
        await tx.partnerReferral.create({
          data: { partnerId: coupon.partnerId, customerEmail: email, userId: input.userId ?? null, couponId: coupon.id, couponCode: coupon.code, firstContractId: contract.id },
        });
      }
    }
    await audit(tx, {
      actorId,
      action: "CONTRACT_CREATED",
      entityType: "Contract",
      entityId: contract.id,
      data: { contest: input.contest, category: q.category, rule: q.pricingRule, finalAmount: fromCents(q.finalCents), coupon: coupon?.code ?? null, partnerId: coupon?.partnerId ?? null, replacedId: replacedId ?? null },
    });
    return { contractId: contract.id, created: true, replacedId };
  });
}

/** Liga contratações e indicações registradas pelo e-mail (lista de espera) à conta criada depois. */
export async function linkContractsToUser(tx: Tx, userId: string, email: string) {
  const customerEmail = email.toLowerCase();
  await tx.contract.updateMany({ where: { customerEmail, userId: null }, data: { userId } });
  await tx.partnerReferral.updateMany({ where: { customerEmail, userId: null }, data: { userId } });
}

/** Cancela uma contratação sem valores recebidos (com pagamentos, é preciso estorná-los antes). */
export async function cancelContract(contractId: string, reason: string, actorId: string) {
  const why = reason.trim();
  if (why.length < 5) throw new CommerceError("Informe o motivo do cancelamento (mínimo de 5 caracteres).");
  return db.$transaction(async (tx) => {
    await lockContract(tx, contractId);
    const c = await tx.contract.findUnique({ where: { id: contractId } });
    if (!c) throw new CommerceError("Contratação não encontrada.");
    if (c.status === "CANCELLED") throw new CommerceError("Esta contratação já está cancelada.");
    if (toCents(c.paidAmount) > 0) throw new CommerceError("Há valores recebidos: registre o estorno antes de cancelar.");
    await tx.contract.update({ where: { id: c.id }, data: { status: "CANCELLED", cancelledAt: new Date(), cancelReason: why, cancelledById: actorId } });
    await audit(tx, { actorId, action: "CONTRACT_CANCELLED", entityType: "Contract", entityId: c.id, data: { reason: why } });
  });
}

export interface GrantOptions {
  /** libera mesmo com saldo pendente (exige justificativa) */
  override?: boolean;
  justification?: string;
  /** conta recém-criada: o acesso passa a valer até a prova mesmo que o registro diga "sem prazo" */
  newAccount?: boolean;
}

/**
 * Concede (ou estende) o acesso acadêmico até o fim do dia da prova oficial do concurso contratado.
 * Separado do financeiro: exige quitação, salvo liberação explícita do administrador com justificativa.
 */
export async function grantAccessUntilExam(contractId: string, actorId: string | null, opts: GrantOptions = {}, client?: Tx) {
  const run = async (tx: Tx) => {
    await lockContract(tx, contractId);
    const c = await tx.contract.findUnique({ where: { id: contractId }, include: { user: { select: { id: true, accessExpiresAt: true } } } });
    if (!c) throw new CommerceError("Contratação não encontrada.");
    if (c.status === "CANCELLED") throw new CommerceError("Contratação cancelada não concede acesso.");
    if (!c.user) throw new CommerceError("A contratação ainda não está ligada a uma conta: aprove o cadastro primeiro.", "NO_USER");
    const setting = await tx.contestSetting.findUnique({ where: { contest: c.contest } });
    if (!setting?.examDate) {
      throw new CommerceError("Data da prova deste concurso pendente: cadastre a data oficial em Financeiro › Concursos antes de liberar o acesso.", "EXAM_DATE_PENDING");
    }
    const settled = c.status === "PAID" || c.status === "OVERPAID";
    const justification = opts.justification?.trim() ?? "";
    if (!settled) {
      if (!opts.override) throw new CommerceError("Há saldo pendente nesta contratação. Para liberar mesmo assim, confirme com justificativa.", "BALANCE_PENDING");
      if (justification.length < 10) throw new CommerceError("Justifique a liberação com saldo pendente (mínimo de 10 caracteres).");
    }
    const end = accessEndForExamDate(setting.examDate);
    const current = c.user.accessExpiresAt;
    // `null` = acesso sem prazo (cadastros antigos): não é reduzido, salvo em conta recém-criada
    const keepIndefinite = current === null && !opts.newAccount;
    const nextExpires = keepIndefinite ? null : current && current > end ? current : end;
    if (!keepIndefinite) await tx.user.update({ where: { id: c.user.id }, data: { accessExpiresAt: nextExpires } });
    await tx.contract.update({ where: { id: c.id }, data: { accessGrantedAt: new Date(), accessUntil: end, accessGrantedById: actorId } });
    await audit(tx, {
      actorId,
      action: "ACCESS_GRANTED",
      entityType: "Contract",
      entityId: c.id,
      data: { userId: c.user.id, until: end.toISOString(), settled, override: !settled, justification: settled ? null : justification, keptIndefinite: keepIndefinite },
    });
    return { until: end, keptIndefinite: keepIndefinite };
  };
  return client ? run(client) : db.$transaction(run);
}

/**
 * Estorno total (ou contestação perdida) de uma contratação cujo acesso já foi liberado: encerra o acesso que
 * ESTA contratação concedeu. Só mexe na conta quando o prazo dela veio desta contratação; se a conta tem prazo
 * maior por outro motivo, apenas registra a necessidade de revisão. Nunca altera acessos sem prazo.
 */
export async function revokeAccessAfterFullReversal(contractId: string, reason: string) {
  return db.$transaction(async (tx) => {
    await lockContract(tx, contractId);
    const c = await tx.contract.findUnique({ where: { id: contractId }, include: { user: { select: { id: true, accessExpiresAt: true } } } });
    if (!c || !c.accessGrantedAt || !c.accessUntil) return { revoked: false as const, reviewNeeded: false };
    if (toCents(c.paidAmount) > 0) return { revoked: false as const, reviewNeeded: false };
    const ownsDeadline = Boolean(c.user?.accessExpiresAt && c.user.accessExpiresAt.getTime() === c.accessUntil.getTime());
    if (c.user && ownsDeadline) await tx.user.update({ where: { id: c.user.id }, data: { accessExpiresAt: new Date() } });
    await tx.contract.update({ where: { id: c.id }, data: { accessGrantedAt: null, accessUntil: null, accessGrantedById: null } });
    await audit(tx, {
      actorId: null,
      action: ownsDeadline ? "ACCESS_REVOKED" : "ACCESS_REVIEW_NEEDED",
      entityType: "Contract",
      entityId: c.id,
      data: { reason, userId: c.userId, previousUntil: c.accessUntil.toISOString() },
    });
    return { revoked: ownsDeadline as boolean, reviewNeeded: !ownsDeadline } as { revoked: boolean; reviewNeeded: boolean };
  });
}
