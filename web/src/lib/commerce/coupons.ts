import "server-only";
import type { Coupon, Prisma } from "@/generated/prisma/client";
import { db } from "@/lib/db";
import { audit } from "./audit";
import { COUPON_CODE, normalizeCouponCode } from "./coupon-codes";
import { CommerceError } from "./errors";

export { COUPON_CODE, MAX_COUPONS_PER_CONTRACT, couponSetKey, normalizeCouponCode, parseCouponCodes } from "./coupon-codes";
import { MAX_DISCOUNT_POINTS } from "./pricing";

type Tx = Prisma.TransactionClient;

export interface AppliedCouponInfo {
  code: string;
  kind: "SITE" | "PARTNER";
  /** pontos percentuais do cupom */
  discountPoints: number;
}

/**
 * Valida cada código para uma nova contratação e separa o cupom de parceiro (no máximo um) dos cupons do site.
 * Recusa: formato inválido, inexistente, desativado, parceiro desativado, autoindicação e mais de um cupom de parceiro.
 * A mensagem é a mesma para inexistente/desativado (não revela quais códigos existem). Sem `customer`, a verificação
 * de autoindicação é pulada (simulação de preço antes de o cliente informar o e-mail; a contratação confere de novo).
 */
export async function resolveCoupons(tx: Tx, codes: readonly string[], customer?: { email: string; userId?: string | null }) {
  let partner: Awaited<ReturnType<typeof findPartnerCoupon>> = null;
  const site: Coupon[] = [];
  for (const code of codes) {
    const invalid = () => new CommerceError(`Cupom inválido ou desativado: ${code}.`, "COUPON_INVALID");
    if (!COUPON_CODE.test(code)) throw invalid();
    const siteCoupon = await tx.coupon.findUnique({ where: { code } });
    if (siteCoupon) {
      if (!siteCoupon.active) throw invalid();
      site.push(siteCoupon);
      continue;
    }
    const pc = await findPartnerCoupon(tx, code);
    if (!pc || !pc.active || !pc.partner.active) throw invalid();
    if (partner) throw new CommerceError("Use apenas um cupom de parceiro por contratação.", "COUPON_INVALID");
    if (customer && (pc.partner.user.email.toLowerCase() === customer.email || (customer.userId && pc.partner.userId === customer.userId))) {
      throw new CommerceError("O cupom de parceiro não pode ser usado pelo próprio parceiro.", "SELF_REFERRAL");
    }
    partner = pc;
  }
  const applied: AppliedCouponInfo[] = [
    ...(partner ? [{ code: partner.code, kind: "PARTNER" as const, discountPoints: partner.discountPoints }] : []),
    ...site.map((c) => ({ code: c.code, kind: "SITE" as const, discountPoints: c.discountPoints })),
  ];
  return { partner, site, applied };
}

function findPartnerCoupon(tx: Tx, code: string) {
  return tx.partnerCoupon.findUnique({
    where: { code },
    include: { partner: { select: { id: true, active: true, userId: true, user: { select: { email: true } } } } },
  });
}

/** Códigos de cupom são únicos entre cupons do site e de parceiros (nunca reaproveitados). */
export async function assertCodeFree(tx: Tx, code: string, ignoreId?: string) {
  if (!COUPON_CODE.test(code)) throw new CommerceError("O cupom deve ter de 4 a 20 letras maiúsculas ou números.");
  const [site, partner] = await Promise.all([
    tx.coupon.findUnique({ where: { code }, select: { id: true } }),
    tx.partnerCoupon.findUnique({ where: { code }, select: { id: true } }),
  ]);
  if ((site && site.id !== ignoreId) || partner) {
    throw new CommerceError("Este código de cupom já existe (códigos não são reaproveitados).", "COUPON_TAKEN");
  }
}

/* ───────────── Gestão (admin) ───────────── */

function parsePoints(raw: unknown): number {
  const n = typeof raw === "number" ? raw : Number(String(raw ?? "").trim().replace(",", "."));
  if (!Number.isInteger(n) || n < 1 || n > MAX_DISCOUNT_POINTS) {
    throw new CommerceError(`O desconto deve ser um percentual inteiro de 1 a ${MAX_DISCOUNT_POINTS}.`);
  }
  return n;
}

export interface SiteCouponRow {
  id: string;
  code: string;
  discountPoints: number;
  active: boolean;
  createdAt: Date;
  deactivatedAt: Date | null;
  uses: number;
}

export async function listSiteCoupons(): Promise<SiteCouponRow[]> {
  const rows = await db.coupon.findMany({ orderBy: [{ active: "desc" }, { createdAt: "desc" }], include: { _count: { select: { contracts: true } } } });
  return rows.map((c) => ({ id: c.id, code: c.code, discountPoints: c.discountPoints, active: c.active, createdAt: c.createdAt, deactivatedAt: c.deactivatedAt, uses: c._count.contracts }));
}

export async function createSiteCoupon(input: { code: string; discountPoints: unknown }, actorId: string): Promise<{ id: string; code: string }> {
  const code = normalizeCouponCode(input.code) ?? "";
  const points = parsePoints(input.discountPoints);
  try {
    return await db.$transaction(async (tx) => {
      await assertCodeFree(tx, code);
      const c = await tx.coupon.create({ data: { code, discountPoints: points, createdById: actorId } });
      await audit(tx, { actorId, action: "SITE_COUPON_CREATED", entityType: "Coupon", entityId: c.id, data: { code, discountPoints: points } });
      return { id: c.id, code };
    });
  } catch (err) {
    throw uniqueToTaken(err);
  }
}

/**
 * Edita o percentual (vale só para novas contratações: as antigas guardam o que foi aplicado) e, enquanto o cupom
 * não foi usado em nenhuma contratação, também o código.
 */
export async function updateSiteCoupon(id: string, input: { code?: string | null; discountPoints: unknown }, actorId: string) {
  const points = parsePoints(input.discountPoints);
  try {
    return await db.$transaction(async (tx) => {
      const c = await tx.coupon.findUnique({ where: { id }, include: { _count: { select: { contracts: true } } } });
      if (!c) throw new CommerceError("Cupom não encontrado.");
      const code = normalizeCouponCode(input.code) ?? c.code;
      if (code !== c.code) {
        if (c._count.contracts > 0) throw new CommerceError("Este cupom já foi usado em contratações: o código não pode mais mudar. Crie outro cupom e inative este.");
        await assertCodeFree(tx, code, c.id);
      }
      if (code === c.code && points === c.discountPoints) return;
      await tx.coupon.update({ where: { id }, data: { code, discountPoints: points } });
      await audit(tx, {
        actorId,
        action: "SITE_COUPON_UPDATED",
        entityType: "Coupon",
        entityId: id,
        data: { before: { code: c.code, discountPoints: c.discountPoints }, after: { code, discountPoints: points } },
      });
    });
  } catch (err) {
    throw uniqueToTaken(err);
  }
}

export async function setSiteCouponActive(id: string, active: boolean, actorId: string) {
  return db.$transaction(async (tx) => {
    const c = await tx.coupon.findUnique({ where: { id } });
    if (!c) throw new CommerceError("Cupom não encontrado.");
    if (c.active === active) return;
    await tx.coupon.update({ where: { id }, data: { active, deactivatedAt: active ? null : new Date() } });
    await audit(tx, { actorId, action: active ? "SITE_COUPON_ACTIVATED" : "SITE_COUPON_DEACTIVATED", entityType: "Coupon", entityId: id, data: { code: c.code } });
  });
}

/** Exclui o cupom. Com uso em contratações, o caminho é inativar (o histórico das contratações fica preservado). */
export async function deleteSiteCoupon(id: string, actorId: string) {
  return db.$transaction(async (tx) => {
    const c = await tx.coupon.findUnique({ where: { id }, include: { _count: { select: { contracts: true } } } });
    if (!c) throw new CommerceError("Cupom não encontrado.");
    if (c._count.contracts > 0) {
      throw new CommerceError("Este cupom já foi usado em contratações. Para preservar o histórico, inative-o em vez de excluir.", "COUPON_HAS_HISTORY");
    }
    await tx.coupon.delete({ where: { id } });
    await audit(tx, { actorId, action: "SITE_COUPON_DELETED", entityType: "Coupon", entityId: id, data: { code: c.code, discountPoints: c.discountPoints } });
  });
}

function uniqueToTaken(err: unknown): unknown {
  if (err && typeof err === "object" && "code" in err && (err as { code?: string }).code === "P2002") {
    return new CommerceError("Este código de cupom já existe (códigos não são reaproveitados).", "COUPON_TAKEN");
  }
  return err;
}
