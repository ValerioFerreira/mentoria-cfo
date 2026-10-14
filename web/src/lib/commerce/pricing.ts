// Regras comerciais centralizadas (funções puras). Toda contratação usa `quote` no servidor: o navegador nunca
// informa preço nem desconto. Mudar valores aqui não altera contratações já registradas (cada uma guarda os seus).
import type { ContestCategory } from "@/generated/prisma/client";
import { formatBRL } from "./money";

/** Identificador gravado em cada contratação: qual tabela de preços/descontos foi aplicada. */
export const PRICING_RULE = "ACESSO-ATE-PROVA-LANCAMENTO-2026-10";

/** Preço original (centavos) por categoria do concurso. */
export const CATEGORY_PRICE_CENTS: Record<ContestCategory, number> = {
  OFICIAL: 12_000,
  PCPE: 12_000,
  PRACA: 8_000,
};

export const CATEGORY_LABEL: Record<ContestCategory, string> = {
  OFICIAL: "Oficial",
  PCPE: "PCPE",
  PRACA: "Praça",
};

/** Desconto de lançamento, em pontos percentuais sobre o preço original. */
export const LAUNCH_DISCOUNT_POINTS = 25;
/** Desconto adicional do cupom de parceiro (p.p. sobre o preço original, somados ao de lançamento). */
export const PARTNER_COUPON_DISCOUNT_POINTS = 15;
export const MAX_DISCOUNT_POINTS = 100;

/** Comissão do parceiro sobre o valor efetivamente recebido (após descontos, antes de taxas), em pontos-base. */
export const COMMISSION_RATE_BP = 3_000;
/**
 * Dias até a comissão ficar disponível para repasse (alinhado à garantia de 7 dias de devolução).
 * Antes disso ela aparece como "pendente de confirmação".
 */
export const COMMISSION_HOLD_DAYS = 7;

export function isContestCategory(v: unknown): v is ContestCategory {
  return v === "OFICIAL" || v === "PCPE" || v === "PRACA";
}

/** Preço e desconto do site definidos no concurso (Financeiro › Concursos). Campos nulos usam o padrão da categoria. */
export interface PriceOverride {
  priceCents?: number | null;
  siteDiscountPoints?: number | null;
}

export interface Quote {
  category: ContestCategory;
  pricingRule: string;
  originalCents: number;
  launchDiscountPoints: number;
  partnerDiscountPoints: number;
  discountCents: number;
  finalCents: number;
}

/**
 * Preço da contratação. Descontos somam pontos percentuais sobre o preço original (limitados a 100%);
 * o valor final é arredondado ao centavo (meio para cima).
 */
export function quote(category: ContestCategory | null | undefined, partnerDiscountPoints = 0, override?: PriceOverride | null): Quote {
  if (!isContestCategory(category)) throw new PricingError("Concurso sem categoria comercial definida: encaminhado para revisão administrativa.");
  if (!Number.isInteger(partnerDiscountPoints) || partnerDiscountPoints < 0 || partnerDiscountPoints > MAX_DISCOUNT_POINTS) {
    throw new PricingError("Desconto de cupom inválido.");
  }
  const customPrice = override?.priceCents ?? null;
  const customSite = override?.siteDiscountPoints ?? null;
  if (customPrice !== null && (!Number.isSafeInteger(customPrice) || customPrice <= 0 || customPrice > 10_000_000)) throw new PricingError("Preço do concurso inválido.");
  if (customSite !== null && (!Number.isInteger(customSite) || customSite < 0 || customSite > MAX_DISCOUNT_POINTS)) throw new PricingError("Desconto do site inválido.");
  const originalCents = customPrice ?? CATEGORY_PRICE_CENTS[category];
  const siteDiscount = customSite ?? LAUNCH_DISCOUNT_POINTS;
  const points = Math.min(MAX_DISCOUNT_POINTS, siteDiscount + partnerDiscountPoints);
  const partner = points - siteDiscount;
  const finalCents = Math.round((originalCents * (MAX_DISCOUNT_POINTS - points)) / MAX_DISCOUNT_POINTS);
  return {
    category,
    pricingRule: customPrice !== null || customSite !== null ? `${PRICING_RULE}+CONFIG-CONCURSO` : PRICING_RULE,
    originalCents,
    launchDiscountPoints: siteDiscount,
    partnerDiscountPoints: partner,
    discountCents: originalCents - finalCents,
    finalCents,
  };
}

export class PricingError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "PricingError";
  }
}

/** Comissão (centavos) sobre um valor recebido, arredondada meio para cima. */
export function commissionOn(receivedCents: number): number {
  if (receivedCents <= 0) return 0;
  return Math.round((receivedCents * COMMISSION_RATE_BP) / 10_000);
}

/**
 * Comissão total devida numa contratação: 30% do recebido válido, limitado ao valor devido (o excedente
 * pago a mais vai para tratamento administrativo e não gera comissão). Os lançamentos por parcela são a
 * diferença entre este alvo antes e depois de cada pagamento/estorno, então a soma das parcelas é sempre
 * exatamente a comissão sobre o total recebido.
 */
export function commissionTarget(validReceivedCents: number, finalCents: number): number {
  return commissionOn(Math.min(Math.max(0, validReceivedCents), finalCents));
}

/** Situação financeira a partir dos totais. */
export function financialStatus(validReceivedCents: number, finalCents: number): "OPEN" | "PARTIAL" | "PAID" | "OVERPAID" {
  if (validReceivedCents <= 0) return "OPEN";
  if (validReceivedCents < finalCents) return "PARTIAL";
  if (validReceivedCents === finalCents) return "PAID";
  return "OVERPAID";
}

/** Fim do dia da prova no fuso de Recife (UTC−3, sem horário de verão): o acesso vale até 23:59:59 desse dia. */
export function accessEndForExamDate(examDate: Date): Date {
  const iso = examDate.toISOString().slice(0, 10);
  return new Date(`${iso}T23:59:59.999-03:00`);
}

/** Textos do card de preço (servidor calcula; componentes só exibem). */
export function priceCardText(q: Quote) {
  return {
    badge: `${q.launchDiscountPoints + q.partnerDiscountPoints}% OFF · ${q.partnerDiscountPoints ? "lançamento + cupom" : "lançamento"}`,
    original: `De ${formatBRL(q.originalCents)}`,
    final: formatBRL(q.finalCents),
  };
}
