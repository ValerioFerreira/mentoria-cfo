import "server-only";
import type { Contest, ContestCategory, PaymentMethod } from "@/generated/prisma/client";
import { db } from "@/lib/db";
import { audit } from "./audit";
import { lockCustomer } from "./contracts";
import { CommerceError } from "./errors";
import { fromCents } from "./money";
import { registerPayment } from "./payments";

/** Regra gravada nas contratações importadas de quem pagou antes do preço atual: o valor pago é o devido. */
export const LEGACY_PRICING_RULE = "LEGADO-PAGANTE-ANTERIOR";

const DEFAULT_CATEGORY: Record<Contest, ContestCategory> = {
  CBMPE_OFICIAL: "OFICIAL",
  PMPE_OFICIAL: "OFICIAL",
  CBMPE_SOLDADO: "PRACA",
  PMPE_SOLDADO: "PRACA",
  PCPE_AGENTE: "PCPE",
};

/**
 * Inscrições da lista de espera com pagamento conferido (`paidAt`) e sem contratação no financeiro:
 * quem pagou antes do valor atual não aparece nas tabelas, que só têm contratações novas.
 */
export async function listLegacyPayers() {
  const entries = await db.waitlistEntry.findMany({
    where: { paidAt: { not: null }, status: { not: "REJECTED" } },
    orderBy: { paidAt: "asc" },
  });
  if (entries.length === 0) return [];
  const contracts = await db.contract.findMany({
    where: { customerEmail: { in: entries.map((e) => e.email) }, status: { not: "CANCELLED" } },
    select: { customerEmail: true, contest: true, status: true, pricingRule: true, _count: { select: { payments: true } } },
  });
  const done = new Set(contracts.filter((c) => c._count.payments > 0 || c.pricingRule !== LEGACY_PRICING_RULE).map((c) => `${c.customerEmail}|${c.contest}`));
  return entries.filter((e) => !done.has(`${e.email}|${e.contest}`));
}

export interface LegacyPayerInput {
  waitlistEntryId: string;
  amountCents: number;
  paidAt: Date;
  method: PaymentMethod;
  note?: string | null;
}

/**
 * Inclui no financeiro quem já tinha pago: cria a contratação com o valor efetivamente pago como valor devido
 * (sem desconto, sem parceiro) e lança o pagamento, que a deixa quitada. Não mexe no acesso, que já foi concedido.
 */
export async function importLegacyPayer(input: LegacyPayerInput, actorId: string): Promise<{ contractId: string }> {
  if (!Number.isSafeInteger(input.amountCents) || input.amountCents <= 0) throw new CommerceError("Informe o valor pago, maior que zero.");
  const entry = await db.waitlistEntry.findUnique({ where: { id: input.waitlistEntryId } });
  if (!entry) throw new CommerceError("Inscrição não encontrada.");
  const email = entry.email.toLowerCase();

  const contractId = await db.$transaction(async (tx) => {
    await lockCustomer(tx, email);
    const existing = await tx.contract.findFirst({
      where: { customerEmail: email, contest: entry.contest, status: { not: "CANCELLED" } },
      include: { _count: { select: { payments: true } } },
    });
    if (existing) {
      if (existing.pricingRule === LEGACY_PRICING_RULE && existing._count.payments === 0) return existing.id; // tentativa anterior sem pagamento
      throw new CommerceError("Este cliente já tem contratação para o concurso: lance o pagamento nela, na tela da contratação.", "CONTRACT_EXISTS");
    }
    const [setting, user] = await Promise.all([
      tx.contestSetting.findUnique({ where: { contest: entry.contest } }),
      tx.user.findUnique({ where: { email }, select: { id: true } }),
    ]);
    const amount = fromCents(input.amountCents);
    const contract = await tx.contract.create({
      data: {
        userId: user?.id ?? null,
        customerEmail: email,
        customerName: entry.name,
        waitlistEntryId: entry.id,
        contest: entry.contest,
        category: setting?.category ?? DEFAULT_CATEGORY[entry.contest],
        examDateAtContract: setting?.examDate ?? null,
        pricingRule: LEGACY_PRICING_RULE,
        originalAmount: amount,
        launchDiscountPoints: 0,
        partnerDiscountPoints: 0,
        discountAmount: "0.00",
        finalAmount: amount,
      },
    });
    await audit(tx, {
      actorId,
      action: "CONTRACT_IMPORTED",
      entityType: "Contract",
      entityId: contract.id,
      data: { waitlistEntryId: entry.id, contest: entry.contest, amount, paidAt: input.paidAt.toISOString() },
    });
    return contract.id;
  });

  await registerPayment(
    { contractId, amountCents: input.amountCents, paidAt: input.paidAt, method: input.method, note: input.note ?? "Pagamento anterior à cobrança atual (importado)", idempotencyKey: `legacy:${input.waitlistEntryId}` },
    actorId,
  );
  return { contractId };
}
