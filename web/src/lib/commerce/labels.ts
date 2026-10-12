// Rótulos de exibição (sem lógica de negócio; seguro para componentes de cliente).
import type { Contest, ContractStatus, PaymentMethod, ReversalKind } from "@/generated/prisma/client";
import { CONTESTS } from "@/lib/contests";

export function contestName(key: Contest): string {
  const c = CONTESTS.find((x) => x.key === key);
  return c ? `${c.org} · ${c.role}` : key;
}

export const PAYMENT_METHOD_LABEL: Record<PaymentMethod, string> = { PIX: "Pix", TRANSFERENCIA: "Transferência", DINHEIRO: "Dinheiro", OUTRO: "Outra" };
export const REVERSAL_KIND_LABEL: Record<ReversalKind, string> = { ESTORNO: "Estorno", CORRECAO: "Correção" };

export const CONTRACT_STATUS: Record<ContractStatus, { label: string; tone: "ok" | "warn" | "neutral" | "primary" | "gold" }> = {
  OPEN: { label: "Aguardando pagamento", tone: "warn" },
  PARTIAL: { label: "Pagamento parcial", tone: "warn" },
  PAID: { label: "Quitada", tone: "ok" },
  OVERPAID: { label: "Pagamento excedente", tone: "primary" },
  CANCELLED: { label: "Cancelada", tone: "neutral" },
};

export const AUDIT_LABEL: Record<string, string> = {
  CONTRACT_CREATED: "Contratação registrada",
  CONTRACT_REPLACED: "Contratação substituída (cupom alterado)",
  CONTRACT_CANCELLED: "Contratação cancelada",
  PAYMENT_REGISTERED: "Pagamento registrado",
  PAYMENT_REVERSED: "Estorno/correção",
  OVERPAYMENT_DETECTED: "Pagamento excedente sinalizado",
  ACCESS_GRANTED: "Acesso liberado até a prova",
  CONTEST_SETTING_UPDATED: "Concurso (categoria/data) alterado",
  PARTNER_CREATED: "Parceiro cadastrado",
  PARTNER_UPDATED: "Dados do parceiro alterados",
  PARTNER_ACTIVATED: "Parceiro reativado",
  PARTNER_DEACTIVATED: "Parceiro desativado",
  PARTNER_PASSWORD_RESET: "Senha do parceiro redefinida",
  COUPON_REPLACED: "Cupom substituído",
  COUPON_ACTIVATED: "Cupom ativado",
  COUPON_DEACTIVATED: "Cupom desativado",
  PAYOUT_REGISTERED: "Repasse registrado",
};

/** dd/mm/aaaa no fuso de Recife */
export function dateBR(d: Date | string | null | undefined): string {
  if (!d) return "—";
  return new Date(d).toLocaleDateString("pt-BR", { timeZone: "America/Recife" });
}

/** Data de campo @db.Date (meia-noite UTC) sem deslocar o dia. */
export function dayBR(d: Date | string | null | undefined): string {
  if (!d) return "—";
  return new Date(d).toLocaleDateString("pt-BR", { timeZone: "UTC" });
}
