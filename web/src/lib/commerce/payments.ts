import "server-only";
import type { PaymentMethod, Prisma, ReversalKind } from "@/generated/prisma/client";
import { db } from "@/lib/db";
import { todayISO } from "@/lib/plan-time";
import { audit } from "./audit";
import { lockContract } from "./contracts";
import { CommerceError } from "./errors";
import { fromCents, toCents } from "./money";
import { COMMISSION_HOLD_DAYS, COMMISSION_RATE_BP, commissionTarget, financialStatus } from "./pricing";

type Tx = Prisma.TransactionClient;

const DAY_MS = 86_400_000;
/** teto de sanidade por lançamento (R$ 100.000,00) */
const MAX_CENTS = 10_000_000;
export const PAYMENT_METHODS: PaymentMethod[] = ["PIX", "TRANSFERENCIA", "DINHEIRO", "OUTRO"];

function assertAmount(cents: number) {
  if (!Number.isSafeInteger(cents) || cents <= 0) throw new CommerceError("Informe um valor maior que zero.");
  if (cents > MAX_CENTS) throw new CommerceError("Valor acima do limite permitido por lançamento.");
}

/** A data efetiva não pode estar no futuro (dia civil de Recife). */
export function assertEffectiveDate(d: Date, now = new Date()) {
  if (Number.isNaN(d.getTime())) throw new CommerceError("Data inválida.");
  if (d.toISOString().slice(0, 10) > todayISO(now)) throw new CommerceError("A data efetiva não pode estar no futuro.");
  if (d.getUTCFullYear() < 2025) throw new CommerceError("Data efetiva fora do período aceito.");
}

function isUniqueViolation(err: unknown): boolean {
  return Boolean(err && typeof err === "object" && "code" in err && (err as { code?: string }).code === "P2002");
}

export interface ContractTotals {
  paidCents: number;
  reversedCents: number;
  validReceivedCents: number;
  finalCents: number;
  balanceCents: number; // devido − recebido (negativo = excedente)
  status: "OPEN" | "PARTIAL" | "PAID" | "OVERPAID" | "CANCELLED";
}

/**
 * Recalcula a contratação a partir dos lançamentos (pagamentos − estornos), atualiza os campos materializados
 * e lança a diferença de comissão do parceiro, ligada ao pagamento/estorno que a causou. Idempotente.
 */
export async function recomputeContract(
  tx: Tx,
  contractId: string,
  trigger: { paymentId: string; reversalId?: string; sourceKey: string; basisCents: number; paymentPaidAt: Date },
): Promise<ContractTotals> {
  const c = await tx.contract.findUniqueOrThrow({ where: { id: contractId } });
  const [pay, rev] = await Promise.all([
    tx.manualPayment.aggregate({ where: { contractId }, _sum: { amount: true } }),
    tx.paymentReversal.aggregate({ where: { contractId }, _sum: { amount: true } }),
  ]);
  const paidCents = toCents(pay._sum.amount ?? 0);
  const reversedCents = toCents(rev._sum.amount ?? 0);
  const valid = paidCents - reversedCents;
  if (valid < 0) throw new CommerceError("Estornos maiores que os pagamentos recebidos.");
  const finalCents = toCents(c.finalAmount);
  const status = c.status === "CANCELLED" ? "CANCELLED" : financialStatus(valid, finalCents);
  await tx.contract.update({ where: { id: contractId }, data: { paidAmount: fromCents(valid), status } });

  if (c.partnerId) {
    await tx.$queryRaw`SELECT "id" FROM "Partner" WHERE "id" = ${c.partnerId} FOR UPDATE`;
    const current = await tx.commissionEntry.aggregate({ where: { contractId }, _sum: { amount: true } });
    const delta = commissionTarget(valid, finalCents) - toCents(current._sum.amount ?? 0);
    if (delta !== 0) {
      // a comissão de um pagamento (e a reversão dela) fica disponível ao fim da garantia contada da data do pagamento
      const availableAt = new Date(trigger.paymentPaidAt.getTime() + COMMISSION_HOLD_DAYS * DAY_MS);
      await tx.commissionEntry.create({
        data: {
          partnerId: c.partnerId,
          contractId,
          paymentId: trigger.paymentId,
          reversalId: trigger.reversalId ?? null,
          kind: delta > 0 ? "ACCRUAL" : "REVERSAL",
          amount: fromCents(delta),
          basisAmount: fromCents(trigger.basisCents),
          rateBp: COMMISSION_RATE_BP,
          availableAt,
          sourceKey: trigger.sourceKey,
        },
      });
    }
  }
  return { paidCents, reversedCents, validReceivedCents: valid, finalCents, balanceCents: finalCents - valid, status };
}

export interface RegisterPaymentInput {
  contractId: string;
  amountCents: number;
  paidAt: Date;
  method: PaymentMethod;
  receiptRef?: string | null;
  note?: string | null;
  idempotencyKey: string;
}

export interface PaymentResult {
  paymentId: string;
  duplicate: boolean;
  totals?: ContractTotals;
}

/** Registra um pagamento recebido. Repetir o mesmo envio (mesma chave) não duplica o lançamento. */
export async function registerPayment(input: RegisterPaymentInput, actorId: string): Promise<PaymentResult> {
  assertAmount(input.amountCents);
  assertEffectiveDate(input.paidAt);
  if (!PAYMENT_METHODS.includes(input.method)) throw new CommerceError("Forma de pagamento inválida.");
  const key = input.idempotencyKey.trim();
  if (key.length < 8) throw new CommerceError("Envio inválido: recarregue a página e tente novamente.");
  const receiptRef = input.receiptRef?.trim() || null;

  const prior = await db.manualPayment.findUnique({ where: { idempotencyKey: key }, select: { id: true } });
  if (prior) return { paymentId: prior.id, duplicate: true };
  try {
    return await db.$transaction(async (tx) => {
      await lockContract(tx, input.contractId);
      const c = await tx.contract.findUnique({ where: { id: input.contractId }, select: { id: true, status: true, userId: true } });
      if (!c) throw new CommerceError("Contratação não encontrada.");
      if (c.status === "CANCELLED") throw new CommerceError("Contratação cancelada não recebe pagamentos.");
      if (receiptRef) {
        const same = await tx.manualPayment.findMany({ where: { receiptRef: { equals: receiptRef, mode: "insensitive" } }, include: { reversals: { select: { amount: true } } } });
        const live = same.find((p) => toCents(p.amount) - p.reversals.reduce((s, r) => s + toCents(r.amount), 0) > 0);
        if (live) throw new CommerceError("Este comprovante já foi lançado em outro pagamento. Confira o histórico antes de registrar de novo.", "DUPLICATE_RECEIPT");
      }
      const payment = await tx.manualPayment.create({
        data: {
          contractId: c.id,
          amount: fromCents(input.amountCents),
          paidAt: input.paidAt,
          method: input.method,
          receiptRef,
          note: input.note?.trim() || null,
          createdById: actorId,
          idempotencyKey: key,
        },
      });
      const totals = await recomputeContract(tx, c.id, { paymentId: payment.id, sourceKey: `payment:${payment.id}`, basisCents: input.amountCents, paymentPaidAt: input.paidAt });
      await audit(tx, {
        actorId,
        action: "PAYMENT_REGISTERED",
        entityType: "Contract",
        entityId: c.id,
        data: { paymentId: payment.id, amount: fromCents(input.amountCents), method: input.method, paidAt: input.paidAt.toISOString(), status: totals.status },
      });
      if (totals.status === "OVERPAID") {
        await audit(tx, { actorId, action: "OVERPAYMENT_DETECTED", entityType: "Contract", entityId: c.id, data: { excess: fromCents(-totals.balanceCents), paymentId: payment.id } });
      }
      return { paymentId: payment.id, duplicate: false, totals };
    });
  } catch (err) {
    if (isUniqueViolation(err)) {
      const again = await db.manualPayment.findUnique({ where: { idempotencyKey: key }, select: { id: true } });
      if (again) return { paymentId: again.id, duplicate: true };
    }
    throw err;
  }
}

export interface ReversePaymentInput {
  paymentId: string;
  amountCents: number;
  kind: ReversalKind;
  reason: string;
  effectiveAt: Date;
  idempotencyKey: string;
}

/** Estorno/correção (total ou parcial) de um pagamento. O lançamento original permanece intacto. */
export async function reversePayment(input: ReversePaymentInput, actorId: string): Promise<{ reversalId: string; duplicate: boolean; totals?: ContractTotals }> {
  assertAmount(input.amountCents);
  assertEffectiveDate(input.effectiveAt);
  if (input.kind !== "ESTORNO" && input.kind !== "CORRECAO") throw new CommerceError("Tipo de ajuste inválido.");
  const reason = input.reason.trim();
  if (reason.length < 5) throw new CommerceError("Informe a justificativa (mínimo de 5 caracteres).");
  const key = input.idempotencyKey.trim();
  if (key.length < 8) throw new CommerceError("Envio inválido: recarregue a página e tente novamente.");

  const prior = await db.paymentReversal.findUnique({ where: { idempotencyKey: key }, select: { id: true } });
  if (prior) return { reversalId: prior.id, duplicate: true };
  const head = await db.manualPayment.findUnique({ where: { id: input.paymentId }, select: { contractId: true } });
  if (!head) throw new CommerceError("Pagamento não encontrado.");
  try {
    return await db.$transaction(async (tx) => {
      await lockContract(tx, head.contractId);
      const payment = await tx.manualPayment.findUniqueOrThrow({ where: { id: input.paymentId }, include: { reversals: { select: { amount: true } } } });
      const left = toCents(payment.amount) - payment.reversals.reduce((s, r) => s + toCents(r.amount), 0);
      if (input.amountCents > left) throw new CommerceError(`O valor excede o que ainda pode ser estornado deste pagamento (${fromCents(left).replace(".", ",")}).`);
      const reversal = await tx.paymentReversal.create({
        data: {
          paymentId: payment.id,
          contractId: payment.contractId,
          amount: fromCents(input.amountCents),
          kind: input.kind,
          reason,
          effectiveAt: input.effectiveAt,
          createdById: actorId,
          idempotencyKey: key,
        },
      });
      const totals = await recomputeContract(tx, payment.contractId, {
        paymentId: payment.id,
        reversalId: reversal.id,
        sourceKey: `reversal:${reversal.id}`,
        basisCents: input.amountCents,
        paymentPaidAt: payment.paidAt,
      });
      await audit(tx, {
        actorId,
        action: "PAYMENT_REVERSED",
        entityType: "Contract",
        entityId: payment.contractId,
        data: { paymentId: payment.id, reversalId: reversal.id, amount: fromCents(input.amountCents), kind: input.kind, reason, status: totals.status },
      });
      return { reversalId: reversal.id, duplicate: false, totals };
    });
  } catch (err) {
    if (isUniqueViolation(err)) {
      const again = await db.paymentReversal.findUnique({ where: { idempotencyKey: key }, select: { id: true } });
      if (again) return { reversalId: again.id, duplicate: true };
    }
    throw err;
  }
}

/** Confere se os campos materializados batem com os lançamentos (auditoria/reconciliação). */
export async function reconcileContract(contractId: string) {
  const c = await db.contract.findUniqueOrThrow({ where: { id: contractId } });
  const [pay, rev, com] = await Promise.all([
    db.manualPayment.aggregate({ where: { contractId }, _sum: { amount: true } }),
    db.paymentReversal.aggregate({ where: { contractId }, _sum: { amount: true } }),
    db.commissionEntry.aggregate({ where: { contractId }, _sum: { amount: true } }),
  ]);
  const valid = toCents(pay._sum.amount ?? 0) - toCents(rev._sum.amount ?? 0);
  const expectedCommission = c.partnerId ? commissionTarget(valid, toCents(c.finalAmount)) : 0;
  return {
    paidAmountOk: toCents(c.paidAmount) === valid,
    statusOk: c.status === "CANCELLED" || c.status === financialStatus(valid, toCents(c.finalAmount)),
    commissionOk: toCents(com._sum.amount ?? 0) === expectedCommission,
    validReceivedCents: valid,
    commissionCents: toCents(com._sum.amount ?? 0),
  };
}
