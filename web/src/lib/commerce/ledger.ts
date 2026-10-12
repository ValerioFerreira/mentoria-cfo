// Saldo do parceiro a partir dos lançamentos persistidos (função pura, testável sem banco).

export interface LedgerEntry {
  amountCents: number; // + comissão gerada, − comissão revertida
  availableAt: Date;
}

export interface PartnerBalance {
  /** soma das comissões geradas (lançamentos positivos) */
  generatedCents: number;
  /** soma das comissões revertidas (valor positivo) */
  reversedCents: number;
  /** total já repassado ao parceiro */
  paidOutCents: number;
  /** comissões ainda no período de confirmação (garantia) */
  pendingCents: number;
  /** pode ser repassado agora */
  availableCents: number;
  /** repassado a mais (reversões depois do repasse): compensado pelas próximas comissões */
  negativeCents: number;
}

/**
 * saldo maduro = Σ lançamentos já disponíveis − Σ repasses. Positivo: disponível; negativo: a compensar.
 * Como as comissões futuras entram no mesmo somatório, elas compensam primeiro o saldo negativo.
 */
export function summarizeLedger(entries: LedgerEntry[], payoutsCents: number[], now: Date): PartnerBalance {
  let generated = 0;
  let reversed = 0;
  let matured = 0;
  let pending = 0;
  for (const e of entries) {
    if (e.amountCents > 0) generated += e.amountCents;
    else reversed += -e.amountCents;
    if (e.availableAt <= now) matured += e.amountCents;
    else pending += e.amountCents;
  }
  const paidOut = payoutsCents.reduce((s, c) => s + c, 0);
  const balance = matured - paidOut;
  return {
    generatedCents: generated,
    reversedCents: reversed,
    paidOutCents: paidOut,
    pendingCents: Math.max(0, pending),
    availableCents: Math.max(0, balance),
    negativeCents: Math.max(0, -balance),
  };
}
