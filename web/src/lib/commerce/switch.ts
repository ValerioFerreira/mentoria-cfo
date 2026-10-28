import "server-only";
import type { Contest } from "@/generated/prisma/client";
import { db } from "@/lib/db";
import { audit } from "./audit";
import { parseCouponCodes, resolveCoupons } from "./coupons";
import { lockCustomer } from "./contracts";
import { CommerceError } from "./errors";
import { fromCents, toCents } from "./money";
import { allocateDiscountPoints, quote, switchQuote } from "./pricing";

/** Prefixo da regra comercial das contratações geradas pela troca de concurso (`TROCA:<concurso de origem>`). */
export const SWITCH_RULE_PREFIX = "TROCA:";

export interface SwitchOffer {
  mode: "FREE" | "PAY";
  /** preço atual do concurso de destino no site (com o desconto do site, sem cupons) */
  targetSiteCents: number;
  /** preço atual do concurso de origem no site */
  currentSiteCents: number;
  /** tudo o que o aluno já pagou e vale como crédito */
  creditCents: number;
  residualCents: number;
  couponPoints: number;
  discountCents: number;
  finalCents: number;
  coupons: { code: string; kind: "SITE" | "PARTNER"; discountPoints: number }[];
  capped: boolean;
}

async function siteCents(contest: Contest): Promise<number> {
  const setting = await db.contestSetting.findUnique({ where: { contest } });
  if (!setting?.category) throw new CommerceError("Este concurso está em revisão administrativa e ainda não pode ser contratado.", "CATEGORY_MISSING");
  return quote(setting.category, 0, setting).finalCents;
}

/**
 * Crédito do aluno = valor pago na contratação base (a mais recente que não veio de uma troca) + o que pagou nas trocas
 * já feitas. Assim, ir e voltar entre concursos nunca cobra duas vezes a mesma diferença.
 */
export async function creditOf(email: string): Promise<number> {
  const contracts = await db.contract.findMany({
    where: { customerEmail: email.toLowerCase(), status: { not: "CANCELLED" } },
    orderBy: { createdAt: "desc" },
    select: { paidAmount: true, pricingRule: true },
  });
  let base = true;
  let credit = 0;
  for (const c of contracts) {
    const isSwitch = c.pricingRule.startsWith(SWITCH_RULE_PREFIX);
    if (!isSwitch && !base) continue;
    if (!isSwitch) base = false;
    credit += Math.max(0, toCents(c.paidAmount));
  }
  return credit;
}

/**
 * Situação da troca do concurso do aluno: gratuita quando o destino custa o mesmo ou menos no site (ou quando o que já
 * foi pago cobre o preço); caso contrário, o aluno paga a diferença, com cupons incidindo sobre ela.
 */
export async function offerSwitch(input: { email: string; from: Contest; to: Contest; isAdmin?: boolean; couponCodes?: string | null }): Promise<SwitchOffer> {
  const free = (extra: Partial<SwitchOffer> = {}): SwitchOffer => ({
    mode: "FREE", targetSiteCents: 0, currentSiteCents: 0, creditCents: 0, residualCents: 0, couponPoints: 0, discountCents: 0, finalCents: 0, coupons: [], capped: false, ...extra,
  });
  if (input.isAdmin || input.from === input.to) return free();
  const email = input.email.toLowerCase();
  const target = await siteCents(input.to);
  // concurso de origem sem categoria (cadastro antigo): sem preço de referência, vale o valor do destino
  const current = await siteCents(input.from).catch(() => 0);
  const credit = await creditOf(email);
  const owned = await db.contract.count({ where: { customerEmail: email, contest: input.to, status: { in: ["PAID", "OVERPAID"] } } });
  if (owned > 0 || target <= current) return free({ targetSiteCents: target, currentSiteCents: current, creditCents: credit });

  const codes = parseCouponCodes(input.couponCodes);
  const resolved = await db.$transaction((tx) => resolveCoupons(tx, codes, { email }));
  const requested = resolved.applied.map((c) => c.discountPoints);
  const q = switchQuote(target, credit, requested);
  const base = { targetSiteCents: target, currentSiteCents: current, creditCents: credit, residualCents: q.residualCents, couponPoints: q.couponPoints, discountCents: q.discountCents, finalCents: q.finalCents, coupons: resolved.applied, capped: requested.reduce((a, b) => a + b, 0) > q.couponPoints };
  return q.residualCents === 0 ? free(base) : { mode: "PAY", ...base };
}

export type StartSwitchResult = { contractId: string } | { applied: true };

/**
 * Registra a cobrança da diferença como uma contratação do concurso de destino (valor e cupons calculados aqui, no
 * servidor). Cobrança anterior da mesma troca, sem pagamento, é substituída. Diferença zerada pelos cupons: troca direta.
 */
export async function startSwitchContract(input: { userId: string; email: string; name: string | null; from: Contest; to: Contest; couponCodes?: string | null }): Promise<StartSwitchResult> {
  const email = input.email.toLowerCase();
  const offer = await offerSwitch({ email, from: input.from, to: input.to, couponCodes: input.couponCodes });
  if (offer.mode === "FREE") return { applied: true };
  if (offer.finalCents <= 0) {
    await db.$transaction((tx) => audit(tx, { actorId: input.userId, action: "CONTEST_SWITCH_FREE_BY_COUPON", entityType: "User", entityId: input.userId, data: { from: input.from, to: input.to, coupons: offer.coupons.map((c) => c.code) } }));
    return { applied: true };
  }
  return db.$transaction(async (tx) => {
    await lockCustomer(tx, email);
    const setting = await tx.contestSetting.findUnique({ where: { contest: input.to } });
    if (!setting?.category) throw new CommerceError("Este concurso está em revisão administrativa e ainda não pode ser contratado.", "CATEGORY_MISSING");
    const resolved = await resolveCoupons(tx, parseCouponCodes(input.couponCodes), { email, userId: input.userId });
    const pending = await tx.contract.findMany({
      where: { customerEmail: email, contest: input.to, status: "OPEN", pricingRule: { startsWith: SWITCH_RULE_PREFIX } },
      include: { _count: { select: { payments: true } } },
    });
    for (const p of pending) {
      if (p._count.payments > 0) continue;
      await tx.contract.update({ where: { id: p.id }, data: { status: "CANCELLED", cancelledAt: new Date(), cancelReason: "Substituída: nova simulação da troca de concurso." } });
    }
    const partner = resolved.partner;
    const requested = [...(partner ? [partner.discountPoints] : []), ...resolved.site.map((c) => c.discountPoints)];
    const q = switchQuote(quote(setting.category, 0, setting).finalCents, offer.creditCents, requested);
    const applied = allocateDiscountPoints(requested).applied;
    const partnerPoints = partner ? applied[0] : 0;
    const siteApplied = partner ? applied.slice(1) : applied;
    const contract = await tx.contract.create({
      data: {
        userId: input.userId,
        customerEmail: email,
        customerName: input.name,
        contest: input.to,
        category: setting.category,
        examDateAtContract: setting.examDate,
        pricingRule: `${SWITCH_RULE_PREFIX}${input.from}`,
        originalAmount: fromCents(q.residualCents),
        launchDiscountPoints: 0,
        partnerDiscountPoints: partnerPoints,
        couponDiscountPoints: siteApplied.reduce((a, b) => a + b, 0),
        discountAmount: fromCents(q.discountCents),
        finalAmount: fromCents(q.finalCents),
        couponId: partner?.id ?? null,
        couponCode: partner?.code ?? null,
        partnerId: partner?.partnerId ?? null,
        siteCoupons: { create: resolved.site.map((c, i) => ({ couponId: c.id, code: c.code, discountPoints: c.discountPoints, appliedPoints: siteApplied[i] ?? 0 })) },
      },
    });
    if (partner) {
      const referral = await tx.partnerReferral.findUnique({ where: { customerEmail: email } });
      if (!referral) await tx.partnerReferral.create({ data: { partnerId: partner.partnerId, customerEmail: email, userId: input.userId, couponId: partner.id, couponCode: partner.code, firstContractId: contract.id } });
    }
    await audit(tx, {
      actorId: input.userId,
      action: "CONTRACT_CREATED",
      entityType: "Contract",
      entityId: contract.id,
      data: { switch: { from: input.from, to: input.to, creditCents: offer.creditCents, residualCents: q.residualCents }, finalAmount: fromCents(q.finalCents), coupons: resolved.applied.map((c) => c.code) },
    });
    return { contractId: contract.id };
  });
}

/**
 * Conclui a troca depois do pagamento: devolve o concurso de destino da troca quitada mais recente que ainda não foi
 * aplicada (a troca é aplicada uma única vez, registrada em auditoria), ou null.
 */
export async function pendingPaidSwitch(userId: string, email: string): Promise<{ contractId: string; contest: Contest } | null> {
  const c = await db.contract.findFirst({
    where: { OR: [{ userId }, { customerEmail: email.toLowerCase() }], status: { in: ["PAID", "OVERPAID"] }, pricingRule: { startsWith: SWITCH_RULE_PREFIX } },
    orderBy: { createdAt: "desc" },
    select: { id: true, contest: true },
  });
  if (!c) return null;
  const done = await db.auditLog.count({ where: { action: "CONTEST_SWITCH_APPLIED", entityType: "Contract", entityId: c.id } });
  return done ? null : { contractId: c.id, contest: c.contest };
}

export async function markSwitchApplied(userId: string, contractId: string, contest: Contest) {
  await db.$transaction((tx) => audit(tx, { actorId: userId, action: "CONTEST_SWITCH_APPLIED", entityType: "Contract", entityId: contractId, data: { contest } }));
}
