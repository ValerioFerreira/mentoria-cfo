import "server-only";
import type { Contest, ContractStatus, PaymentMethod, Prisma } from "@/generated/prisma/client";
import { db } from "@/lib/db";
import { summarizeLedger } from "./ledger";
import { toCents } from "./money";
import { PARTNER_COUPON_DISCOUNT_POINTS } from "./pricing";

/** Mínimo de indicados para exibir a taxa de conversão. */
export const MIN_CONVERSION_SAMPLE = 5;

/** Saldo consolidado de um cliente (todas as contratações não canceladas, mantidas separadas no detalhe). */
export async function customerBalance(email: string) {
  const contracts = await db.contract.findMany({
    where: { customerEmail: email.toLowerCase(), status: { not: "CANCELLED" } },
    select: { finalAmount: true, paidAmount: true },
  });
  const dueCents = contracts.reduce((s, c) => s + toCents(c.finalAmount), 0);
  const receivedCents = contracts.reduce((s, c) => s + toCents(c.paidAmount), 0);
  return { contracts: contracts.length, dueCents, receivedCents, balanceCents: dueCents - receivedCents };
}

/**
 * Painel do parceiro autenticado. Recebe o id do USUÁRIO da sessão (nunca um id de parceiro vindo do navegador).
 * Não expõe e-mails, nomes nem detalhes financeiros individuais dos clientes indicados.
 */
export async function partnerDashboard(userId: string, now = new Date()) {
  const partner = await db.partner.findUnique({
    where: { userId },
    include: { coupons: { where: { active: true }, select: { code: true, discountPoints: true }, take: 1 } },
  });
  if (!partner || !partner.active) return null;
  const pid = partner.id;
  const referredUsers = await db.partnerReferral.count({ where: { partnerId: pid } });
  const contracts = await db.contract.findMany({
    where: { partnerId: pid, status: { not: "CANCELLED" } },
    select: { id: true, customerEmail: true, contest: true, paidAmount: true, createdAt: true, status: true },
  });
  const entries = await db.commissionEntry.findMany({
    where: { partnerId: pid },
    orderBy: { createdAt: "desc" },
    select: { id: true, kind: true, amount: true, basisAmount: true, availableAt: true, createdAt: true, contract: { select: { contest: true } } },
  });
  const payouts = await db.partnerPayout.findMany({ where: { partnerId: pid }, orderBy: { paidAt: "desc" }, select: { id: true, amount: true, paidAt: true, method: true } });
  const paying = new Set(contracts.filter((c) => toCents(c.paidAmount) > 0).map((c) => c.customerEmail));
  const balance = summarizeLedger(
    entries.map((e) => ({ amountCents: toCents(e.amount), availableAt: e.availableAt })),
    payouts.map((p) => toCents(p.amount)),
    now,
  );
  return {
    coupon: partner.coupons[0] ? { code: partner.coupons[0].code, discountPoints: partner.coupons[0].discountPoints } : null,
    discountPoints: partner.coupons[0]?.discountPoints ?? PARTNER_COUPON_DISCOUNT_POINTS,
    referredUsers,
    payingUsers: paying.size,
    conversion: referredUsers >= MIN_CONVERSION_SAMPLE ? paying.size / referredUsers : null,
    contracts: contracts.length,
    receivedCents: contracts.reduce((s, c) => s + toCents(c.paidAmount), 0),
    balance,
    history: [
      ...entries.map((e) => ({
        id: e.id,
        type: e.kind === "ACCRUAL" ? ("COMISSAO" as const) : ("REVERSAO" as const),
        date: e.createdAt.toISOString(),
        availableAt: e.availableAt.toISOString(),
        pending: e.availableAt > now,
        contest: e.contract.contest,
        amountCents: toCents(e.amount),
        basisCents: toCents(e.basisAmount),
      })),
      ...payouts.map((p) => ({
        id: p.id,
        type: "REPASSE" as const,
        date: p.paidAt.toISOString(),
        availableAt: p.paidAt.toISOString(),
        pending: false,
        contest: null as Contest | null,
        amountCents: -toCents(p.amount),
        basisCents: 0,
        method: p.method,
      })),
    ].sort((a, b) => b.date.localeCompare(a.date)),
  };
}

export type PartnerDashboard = NonNullable<Awaited<ReturnType<typeof partnerDashboard>>>;

/* ───────────────────────── Administração ───────────────────────── */

export interface FinanceFilters {
  q?: string; // e-mail ou nome do cliente
  contest?: Contest;
  status?: ContractStatus;
  method?: PaymentMethod;
  from?: Date;
  to?: Date; // inclusivo (fim do dia)
  partnerId?: string;
}

function contractWhere(f: FinanceFilters): Prisma.ContractWhereInput {
  const w: Prisma.ContractWhereInput = {};
  if (f.q) w.OR = [{ customerEmail: { contains: f.q.toLowerCase() } }, { customerName: { contains: f.q, mode: "insensitive" } }];
  if (f.contest) w.contest = f.contest;
  if (f.status) w.status = f.status;
  if (f.partnerId) w.partnerId = f.partnerId;
  if (f.from || f.to) w.createdAt = { ...(f.from ? { gte: f.from } : {}), ...(f.to ? { lte: f.to } : {}) };
  if (f.method) w.payments = { some: { method: f.method } };
  return w;
}

export async function listContracts(f: FinanceFilters, take = 200) {
  const where = contractWhere(f);
  const [rows, agg] = await Promise.all([
    db.contract.findMany({
      where,
      orderBy: { createdAt: "desc" },
      take,
      select: {
        id: true, customerEmail: true, customerName: true, contest: true, category: true, originalAmount: true, discountAmount: true,
        finalAmount: true, paidAmount: true, status: true, createdAt: true, couponCode: true, accessGrantedAt: true, accessUntil: true,
        userId: true, examDateAtContract: true, partner: { select: { user: { select: { username: true } } } },
        _count: { select: { payments: true, reversals: true } },
      },
    }),
    db.contract.aggregate({ where: { ...where, status: where.status ?? { not: "CANCELLED" } }, _sum: { finalAmount: true, paidAmount: true }, _count: true }),
  ]);
  return {
    rows,
    totals: {
      count: agg._count,
      dueCents: toCents(agg._sum.finalAmount ?? 0),
      receivedCents: toCents(agg._sum.paidAmount ?? 0),
    },
  };
}

export async function listPayments(f: FinanceFilters, take = 300) {
  const where: Prisma.ManualPaymentWhereInput = {};
  if (f.method) where.method = f.method;
  if (f.from || f.to) where.paidAt = { ...(f.from ? { gte: f.from } : {}), ...(f.to ? { lte: f.to } : {}) };
  const cw: Prisma.ContractWhereInput = {};
  if (f.q) cw.OR = [{ customerEmail: { contains: f.q.toLowerCase() } }, { customerName: { contains: f.q, mode: "insensitive" } }];
  if (f.contest) cw.contest = f.contest;
  if (f.status) cw.status = f.status;
  if (Object.keys(cw).length) where.contract = cw;
  const rows = await db.manualPayment.findMany({
    where,
    orderBy: [{ paidAt: "desc" }, { createdAt: "desc" }],
    take,
    select: {
      id: true, amount: true, paidAt: true, method: true, receiptRef: true, note: true, createdAt: true,
      createdBy: { select: { name: true, email: true } },
      contract: { select: { id: true, customerEmail: true, customerName: true, contest: true, status: true } },
      reversals: { select: { id: true, amount: true, kind: true, reason: true, effectiveAt: true, createdAt: true, createdBy: { select: { name: true, email: true } } } },
    },
  });
  return rows;
}

/** Clientes com as obrigações somadas (saldo consolidado por e-mail). */
export async function listCustomers(f: FinanceFilters) {
  const rows = await db.contract.findMany({
    where: { ...contractWhere(f), status: f.status ?? { not: "CANCELLED" } },
    select: { customerEmail: true, customerName: true, userId: true, contest: true, finalAmount: true, paidAmount: true, status: true },
    orderBy: { createdAt: "desc" },
  });
  const map = new Map<string, { email: string; name: string | null; hasAccount: boolean; contests: Contest[]; dueCents: number; receivedCents: number; overpaid: boolean }>();
  for (const r of rows) {
    const cur = map.get(r.customerEmail) ?? { email: r.customerEmail, name: r.customerName, hasAccount: false, contests: [], dueCents: 0, receivedCents: 0, overpaid: false };
    cur.hasAccount ||= Boolean(r.userId);
    cur.contests.push(r.contest);
    cur.dueCents += toCents(r.finalAmount);
    cur.receivedCents += toCents(r.paidAmount);
    cur.overpaid ||= r.status === "OVERPAID";
    map.set(r.customerEmail, cur);
  }
  return [...map.values()];
}

export async function contractDetail(id: string) {
  const c = await db.contract.findUnique({
    where: { id },
    include: {
      user: { select: { id: true, email: true, name: true, accessExpiresAt: true } },
      partner: { select: { id: true, user: { select: { username: true, name: true } } } },
      payments: {
        orderBy: { paidAt: "asc" },
        include: {
          createdBy: { select: { name: true, email: true } },
          reversals: { orderBy: { createdAt: "asc" }, include: { createdBy: { select: { name: true, email: true } } } },
        },
      },
      commissions: { orderBy: { createdAt: "asc" } },
    },
  });
  if (!c) return null;
  const [setting, history, balance] = await Promise.all([
    db.contestSetting.findUnique({ where: { contest: c.contest } }),
    db.auditLog.findMany({ where: { entityType: "Contract", entityId: id }, orderBy: { createdAt: "desc" }, take: 100 }),
    customerBalance(c.customerEmail),
  ]);
  return { contract: c, setting, history, customer: balance };
}

export async function auditHistory(f: { from?: Date; to?: Date; entityType?: string }, take = 300) {
  return db.auditLog.findMany({
    where: {
      ...(f.entityType ? { entityType: f.entityType } : {}),
      ...(f.from || f.to ? { createdAt: { ...(f.from ? { gte: f.from } : {}), ...(f.to ? { lte: f.to } : {}) } } : {}),
    },
    orderBy: { createdAt: "desc" },
    take,
  });
}

/** Lista de parceiros com saldos (administração). */
export async function listPartners(now = new Date()) {
  const partners = await db.partner.findMany({
    orderBy: { createdAt: "desc" },
    include: {
      user: { select: { email: true, username: true, name: true } },
      coupons: { where: { active: true }, select: { code: true } },
      commissions: { select: { amount: true, availableAt: true } },
      payouts: { select: { amount: true } },
      _count: { select: { referrals: true, contracts: true } },
    },
  });
  return partners.map((p) => ({
    id: p.id,
    active: p.active,
    email: p.user.email,
    username: p.user.username,
    name: p.user.name,
    coupon: p.coupons[0]?.code ?? null,
    referrals: p._count.referrals,
    contracts: p._count.contracts,
    balance: summarizeLedger(p.commissions.map((e) => ({ amountCents: toCents(e.amount), availableAt: e.availableAt })), p.payouts.map((x) => toCents(x.amount)), now),
  }));
}

export async function partnerAdminDetail(partnerId: string, f: FinanceFilters, now = new Date()) {
  const p = await db.partner.findUnique({
    where: { id: partnerId },
    include: { user: { select: { id: true, email: true, username: true, name: true } }, coupons: { orderBy: { createdAt: "desc" } } },
  });
  if (!p) return null;
  const period = f.from || f.to ? { ...(f.from ? { gte: f.from } : {}), ...(f.to ? { lte: f.to } : {}) } : undefined;
  // consultas em sequência: são pequenas e assim não abrem 7 conexões de uma vez no pool
  const referrals = await db.partnerReferral.findMany({ where: { partnerId, ...(period ? { createdAt: period } : {}) }, orderBy: { createdAt: "desc" } });
  const contracts = await db.contract.findMany({
    where: contractWhere({ ...f, partnerId }),
    orderBy: { createdAt: "desc" },
    include: { payments: { select: { id: true, amount: true, paidAt: true, method: true, reversals: { select: { amount: true } } } } },
  });
  const entries = await db.commissionEntry.findMany({
    where: { partnerId, ...(period ? { createdAt: period } : {}), ...(f.contest ? { contract: { contest: f.contest } } : {}) },
    orderBy: { createdAt: "desc" },
    include: { contract: { select: { id: true, customerEmail: true, contest: true } }, payment: { select: { id: true, amount: true, paidAt: true } }, reversal: { select: { id: true, reason: true } } },
  });
  const payouts = await db.partnerPayout.findMany({ where: { partnerId, ...(period ? { paidAt: period } : {}) }, orderBy: { paidAt: "desc" }, include: { createdBy: { select: { name: true, email: true } } } });
  const allEntries = await db.commissionEntry.findMany({ where: { partnerId }, select: { amount: true, availableAt: true } });
  const allPayouts = await db.partnerPayout.findMany({ where: { partnerId }, select: { amount: true } });
  const history = await db.auditLog.findMany({ where: { entityType: "Partner", entityId: partnerId }, orderBy: { createdAt: "desc" }, take: 100 });
  return {
    partner: p,
    referrals,
    contracts,
    entries,
    payouts,
    history,
    balance: summarizeLedger(allEntries.map((e) => ({ amountCents: toCents(e.amount), availableAt: e.availableAt })), allPayouts.map((x) => toCents(x.amount)), now),
  };
}
