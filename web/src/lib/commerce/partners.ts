import "server-only";
import { randomInt } from "node:crypto";
import type { Prisma } from "@/generated/prisma/client";
import { hashPassword } from "@/lib/auth/password";
import { db } from "@/lib/db";
import { audit } from "./audit";
import { COUPON_CODE, normalizeCouponCode } from "./contracts";
import { CommerceError } from "./errors";
import { summarizeLedger, type PartnerBalance } from "./ledger";
import { fromCents, toCents } from "./money";
import { assertEffectiveDate } from "./payments";
import { PARTNER_COUPON_DISCOUNT_POINTS } from "./pricing";

type Tx = Prisma.TransactionClient;

export const USERNAME = /^[a-z0-9][a-z0-9._-]{2,19}$/;
const EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
export const MIN_PARTNER_PASSWORD = 8;

async function lockPartner(tx: Tx, partnerId: string) {
  await tx.$queryRaw`SELECT "id" FROM "Partner" WHERE "id" = ${partnerId} FOR UPDATE`;
}

/** Código livre derivado do nome de usuário (ex.: "JOAO.S" -> "JOAOS15"); acrescenta dígitos se já existir. */
async function freeCouponCode(tx: Tx, username: string): Promise<string> {
  const base = username.toUpperCase().replace(/[^A-Z0-9]/g, "").slice(0, 14).padEnd(4, "X");
  const first = `${base}${PARTNER_COUPON_DISCOUNT_POINTS}`;
  if (!(await tx.partnerCoupon.findUnique({ where: { code: first }, select: { id: true } }))) return first;
  for (let i = 0; i < 20; i++) {
    const code = `${base}${randomInt(100, 1000)}`;
    if (!(await tx.partnerCoupon.findUnique({ where: { code }, select: { id: true } }))) return code;
  }
  throw new CommerceError("Não foi possível gerar um código de cupom livre. Informe um código manualmente.");
}

async function assertCouponFree(tx: Tx, code: string) {
  if (!COUPON_CODE.test(code)) throw new CommerceError("O cupom deve ter de 4 a 20 letras maiúsculas ou números.");
  if (await tx.partnerCoupon.findUnique({ where: { code }, select: { id: true } })) {
    throw new CommerceError("Este código de cupom já existe (códigos não são reaproveitados).", "COUPON_TAKEN");
  }
}

export interface CreatePartnerInput {
  email: string;
  username: string;
  password: string;
  name?: string | null;
  couponCode?: string | null;
  /** o e-mail já tem conta: transformar essa conta em parceira (sem criar outra e sem trocar a senha) */
  linkExisting?: boolean;
}

/** Cadastra um parceiro: usuário comum (acesso acadêmico normal) + permissões de parceiro + cupom exclusivo. */
export async function createPartner(input: CreatePartnerInput, actorId: string): Promise<{ partnerId: string; couponCode: string; linked: boolean }> {
  const email = input.email.trim().toLowerCase();
  const username = input.username.trim().toLowerCase();
  if (!EMAIL.test(email) || email.length > 120) throw new CommerceError("E-mail inválido.");
  if (!USERNAME.test(username)) throw new CommerceError("Nome de usuário: 3 a 20 caracteres (minúsculas, números, ponto, hífen ou sublinhado).");
  const wanted = normalizeCouponCode(input.couponCode);

  const existing = await db.user.findUnique({ where: { email }, include: { partner: { select: { id: true } } } });
  if (existing) {
    if (existing.role === "ADMIN") throw new CommerceError("Este e-mail pertence a um administrador e não pode ser parceiro.");
    if (existing.partner) throw new CommerceError("Este e-mail já está cadastrado como parceiro.");
    if (!input.linkExisting) {
      throw new CommerceError(
        "Este e-mail já pertence a um usuário. Marque \"Vincular à conta existente\" para torná-lo parceiro sem criar outra conta (a senha atual dele é mantida).",
        "EMAIL_EXISTS",
      );
    }
  } else if (input.password.length < MIN_PARTNER_PASSWORD) {
    throw new CommerceError(`A senha inicial precisa ter ao menos ${MIN_PARTNER_PASSWORD} caracteres.`);
  }
  const passwordHash = existing ? null : await hashPassword(input.password);

  return db.$transaction(async (tx) => {
    let userId: string;
    if (existing) {
      userId = existing.id;
      if (!existing.username) {
        const taken = await tx.user.findUnique({ where: { username }, select: { id: true } });
        if (!taken) await tx.user.update({ where: { id: userId }, data: { username } });
      }
    } else {
      const [byUsername, waiting] = await Promise.all([
        tx.user.findUnique({ where: { username }, select: { id: true } }),
        tx.waitlistEntry.findUnique({ where: { username }, select: { email: true } }),
      ]);
      if (byUsername || (waiting && waiting.email !== email)) throw new CommerceError("Este nome de usuário já está em uso.");
      const user = await tx.user.create({
        data: { email, username, name: input.name?.trim() || username, passwordHash: passwordHash!, role: "USER", mustChangePassword: false },
      });
      userId = user.id;
    }
    const code = wanted ?? (await freeCouponCode(tx, username));
    await assertCouponFree(tx, code);
    const partner = await tx.partner.create({ data: { userId, createdById: actorId } });
    await tx.partnerCoupon.create({ data: { partnerId: partner.id, code, discountPoints: PARTNER_COUPON_DISCOUNT_POINTS } });
    await audit(tx, { actorId, action: "PARTNER_CREATED", entityType: "Partner", entityId: partner.id, data: { userId, email, username, coupon: code, linkedExisting: Boolean(existing) } });
    return { partnerId: partner.id, couponCode: code, linked: Boolean(existing) };
  });
}

export async function updatePartnerProfile(partnerId: string, input: { name?: string | null; username?: string | null; email?: string | null }, actorId: string) {
  return db.$transaction(async (tx) => {
    const p = await tx.partner.findUnique({ where: { id: partnerId }, include: { user: true } });
    if (!p) throw new CommerceError("Parceiro não encontrado.");
    const data: Prisma.UserUpdateInput = {};
    const name = input.name?.trim();
    if (name) data.name = name.slice(0, 120);
    const username = input.username?.trim().toLowerCase();
    if (username && username !== p.user.username) {
      if (!USERNAME.test(username)) throw new CommerceError("Nome de usuário inválido.");
      if (await tx.user.findUnique({ where: { username }, select: { id: true } })) throw new CommerceError("Este nome de usuário já está em uso.");
      data.username = username;
    }
    const email = input.email?.trim().toLowerCase();
    if (email && email !== p.user.email) {
      if (!EMAIL.test(email) || email.length > 120) throw new CommerceError("E-mail inválido.");
      if (await tx.user.findUnique({ where: { email }, select: { id: true } })) throw new CommerceError("Este e-mail já pertence a outro usuário.");
      data.email = email;
    }
    await tx.user.update({ where: { id: p.userId }, data });
    await audit(tx, { actorId, action: "PARTNER_UPDATED", entityType: "Partner", entityId: partnerId, data: { name: data.name ?? null, username: data.username ?? null, email: data.email ?? null } });
  });
}

/**
 * Exclui o cadastro de parceiro (e os cupons dele). Só é permitido sem histórico financeiro (contratações, comissões ou repasses):
 * com histórico, o caminho é desativar, para preservar a contabilidade. A conta de usuário continua como conta comum.
 */
export async function deletePartner(partnerId: string, actorId: string) {
  return db.$transaction(async (tx) => {
    await lockPartner(tx, partnerId);
    const p = await tx.partner.findUnique({ where: { id: partnerId }, include: { user: { select: { email: true, username: true } }, coupons: { select: { code: true } } } });
    if (!p) throw new CommerceError("Parceiro não encontrado.");
    const [contracts, commissions, payouts, referrals] = await Promise.all([
      tx.contract.count({ where: { partnerId } }),
      tx.commissionEntry.count({ where: { partnerId } }),
      tx.partnerPayout.count({ where: { partnerId } }),
      tx.partnerReferral.count({ where: { partnerId } }),
    ]);
    if (contracts + commissions + payouts + referrals > 0) {
      throw new CommerceError("Este parceiro tem indicações, contratações, comissões ou repasses. Para preservar o histórico financeiro, desative-o em vez de excluir.", "PARTNER_HAS_HISTORY");
    }
    await tx.partnerCoupon.deleteMany({ where: { partnerId } });
    await tx.partner.delete({ where: { id: partnerId } });
    await audit(tx, { actorId, action: "PARTNER_DELETED", entityType: "Partner", entityId: partnerId, data: { email: p.user.email, username: p.user.username, coupons: p.coupons.map((c) => c.code) } });
  });
}

/** Desativar bloqueia novos logins e derruba as sessões abertas; nada do histórico é apagado. */
export async function setPartnerActive(partnerId: string, active: boolean, actorId: string) {
  return db.$transaction(async (tx) => {
    const p = await tx.partner.findUnique({ where: { id: partnerId } });
    if (!p) throw new CommerceError("Parceiro não encontrado.");
    if (p.active === active) return;
    await tx.partner.update({ where: { id: partnerId }, data: { active, deactivatedAt: active ? null : new Date() } });
    if (!active) await tx.session.deleteMany({ where: { userId: p.userId } });
    await audit(tx, { actorId, action: active ? "PARTNER_ACTIVATED" : "PARTNER_DEACTIVATED", entityType: "Partner", entityId: partnerId });
  });
}

/** Nova senha definida pelo administrador (o parceiro não troca a própria senha). Encerra as sessões abertas. */
export async function resetPartnerPassword(partnerId: string, password: string, actorId: string) {
  if (password.length < MIN_PARTNER_PASSWORD) throw new CommerceError(`A senha precisa ter ao menos ${MIN_PARTNER_PASSWORD} caracteres.`);
  const passwordHash = await hashPassword(password);
  return db.$transaction(async (tx) => {
    const p = await tx.partner.findUnique({ where: { id: partnerId } });
    if (!p) throw new CommerceError("Parceiro não encontrado.");
    await tx.user.update({ where: { id: p.userId }, data: { passwordHash, mustChangePassword: false } });
    await tx.session.deleteMany({ where: { userId: p.userId } });
    await audit(tx, { actorId, action: "PARTNER_PASSWORD_RESET", entityType: "Partner", entityId: partnerId });
  });
}

/** Substitui o cupom ativo: o anterior fica desativado (histórico e contratações antigas inalterados). */
export async function replacePartnerCoupon(partnerId: string, newCode: string | null, actorId: string): Promise<string> {
  return db.$transaction(async (tx) => {
    await lockPartner(tx, partnerId);
    const p = await tx.partner.findUnique({ where: { id: partnerId }, include: { user: { select: { username: true, email: true } } } });
    if (!p) throw new CommerceError("Parceiro não encontrado.");
    const code = normalizeCouponCode(newCode) ?? (await freeCouponCode(tx, p.user.username ?? p.user.email.split("@")[0]));
    await assertCouponFree(tx, code);
    const now = new Date();
    const old = await tx.partnerCoupon.findMany({ where: { partnerId, active: true }, select: { id: true, code: true } });
    await tx.partnerCoupon.updateMany({ where: { partnerId, active: true }, data: { active: false, deactivatedAt: now, replacedAt: now } });
    await tx.partnerCoupon.create({ data: { partnerId, code, discountPoints: PARTNER_COUPON_DISCOUNT_POINTS } });
    await audit(tx, { actorId, action: "COUPON_REPLACED", entityType: "Partner", entityId: partnerId, data: { from: old.map((c) => c.code), to: code } });
    return code;
  });
}

/** Ativa/desativa um cupom. Cada parceiro tem no máximo um cupom ativo. */
export async function setCouponActive(couponId: string, active: boolean, actorId: string) {
  return db.$transaction(async (tx) => {
    const c = await tx.partnerCoupon.findUnique({ where: { id: couponId } });
    if (!c) throw new CommerceError("Cupom não encontrado.");
    await lockPartner(tx, c.partnerId);
    if (c.active === active) return;
    if (active) {
      const other = await tx.partnerCoupon.findFirst({ where: { partnerId: c.partnerId, active: true, id: { not: c.id } }, select: { code: true } });
      if (other) throw new CommerceError(`O parceiro já tem o cupom ativo ${other.code}. Desative-o antes.`);
    }
    await tx.partnerCoupon.update({ where: { id: couponId }, data: { active, deactivatedAt: active ? null : new Date() } });
    await audit(tx, { actorId, action: active ? "COUPON_ACTIVATED" : "COUPON_DEACTIVATED", entityType: "Partner", entityId: c.partnerId, data: { code: c.code } });
  });
}

async function balanceIn(tx: Tx | typeof db, partnerId: string, now: Date): Promise<PartnerBalance> {
  const [entries, payouts] = await Promise.all([
    tx.commissionEntry.findMany({ where: { partnerId }, select: { amount: true, availableAt: true } }),
    tx.partnerPayout.findMany({ where: { partnerId }, select: { amount: true } }),
  ]);
  return summarizeLedger(
    entries.map((e) => ({ amountCents: toCents(e.amount), availableAt: e.availableAt })),
    payouts.map((p) => toCents(p.amount)),
    now,
  );
}

export function partnerBalance(partnerId: string, now = new Date()) {
  return balanceIn(db, partnerId, now);
}

export interface PayoutInput {
  partnerId: string;
  amountCents: number;
  paidAt: Date;
  method: string;
  receiptRef?: string | null;
  note?: string | null;
  idempotencyKey: string;
}

/** Registra um repasse já pago ao parceiro, limitado ao saldo disponível (com estornos e compensações). */
export async function registerPayout(input: PayoutInput, actorId: string): Promise<{ payoutId: string; duplicate: boolean }> {
  if (!Number.isSafeInteger(input.amountCents) || input.amountCents <= 0) throw new CommerceError("Informe um valor maior que zero.");
  assertEffectiveDate(input.paidAt);
  const method = input.method.trim();
  if (method.length < 2) throw new CommerceError("Informe a forma de pagamento ou a referência do repasse.");
  const key = input.idempotencyKey.trim();
  if (key.length < 8) throw new CommerceError("Envio inválido: recarregue a página e tente novamente.");
  const receiptRef = input.receiptRef?.trim() || null;

  const prior = await db.partnerPayout.findUnique({ where: { idempotencyKey: key }, select: { id: true } });
  if (prior) return { payoutId: prior.id, duplicate: true };
  try {
    return await db.$transaction(async (tx) => {
      await lockPartner(tx, input.partnerId);
      const p = await tx.partner.findUnique({ where: { id: input.partnerId }, select: { id: true } });
      if (!p) throw new CommerceError("Parceiro não encontrado.");
      if (receiptRef && (await tx.partnerPayout.findFirst({ where: { partnerId: p.id, receiptRef: { equals: receiptRef, mode: "insensitive" } }, select: { id: true } }))) {
        throw new CommerceError("Já existe um repasse com este comprovante.", "DUPLICATE_RECEIPT");
      }
      const balance = await balanceIn(tx, p.id, new Date());
      if (input.amountCents > balance.availableCents) {
        throw new CommerceError(`Valor acima do saldo disponível para repasse (${fromCents(balance.availableCents).replace(".", ",")}).`, "OVER_BALANCE");
      }
      const payout = await tx.partnerPayout.create({
        data: { partnerId: p.id, amount: fromCents(input.amountCents), paidAt: input.paidAt, method, receiptRef, note: input.note?.trim() || null, createdById: actorId, idempotencyKey: key },
      });
      await audit(tx, { actorId, action: "PAYOUT_REGISTERED", entityType: "Partner", entityId: p.id, data: { payoutId: payout.id, amount: fromCents(input.amountCents), paidAt: input.paidAt.toISOString(), method } });
      return { payoutId: payout.id, duplicate: false };
    });
  } catch (err) {
    if (err && typeof err === "object" && "code" in err && (err as { code?: string }).code === "P2002") {
      const again = await db.partnerPayout.findUnique({ where: { idempotencyKey: key }, select: { id: true } });
      if (again) return { payoutId: again.id, duplicate: true };
    }
    throw err;
  }
}
