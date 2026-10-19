// Rótulos de exibição (sem lógica de negócio; seguro para componentes de cliente).
import type { Contest, ContractStatus, PaymentMethod, ReversalKind } from "@/generated/prisma/client";
import { CONTESTS } from "@/lib/contests";

export function contestName(key: Contest): string {
  const c = CONTESTS.find((x) => x.key === key);
  return c ? `${c.org} · ${c.role}` : key;
}

export const PAYMENT_METHOD_LABEL: Record<PaymentMethod, string> = { PIX: "Pix", TRANSFERENCIA: "Transferência", DINHEIRO: "Dinheiro", OUTRO: "Outra", CARTAO: "Cartão (online)" };

/** Quem lançou: o administrador ou a conciliação automática do Mercado Pago. */
export function actorLabel(by: { name: string | null; email: string } | null | undefined): string {
  return by ? (by.name ?? by.email) : "Mercado Pago (automático)";
}
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
  CONTRACT_IMPORTED: "Pagante anterior incluído no financeiro",
  CONTRACT_REPLACED: "Contratação substituída (cupom alterado)",
  CONTRACT_CANCELLED: "Contratação cancelada",
  PAYMENT_REGISTERED: "Pagamento registrado",
  PAYMENT_REVERSED: "Estorno/correção",
  PAYMENT_ON_CANCELLED_CONTRACT: "Pagamento online em contratação cancelada (devolver)",
  AUTO_APPROVED: "Pago online: conta criada e acesso liberado automaticamente",
  AUTO_APPROVAL_EMAIL_FAILED: "Acesso liberado, mas o e-mail com a senha não saiu (reenvie em Cadastros)",
  ACCESS_GRANT_PENDING: "Pago online; acesso aguardando liberação",
  ACCESS_REVOKED: "Acesso encerrado por estorno total",
  ACCESS_REVIEW_NEEDED: "Estorno total: revisar acesso",
  OVERPAYMENT_DETECTED: "Pagamento excedente sinalizado",
  ACCESS_GRANTED: "Acesso liberado até a prova",
  CONTEST_SETTING_UPDATED: "Concurso (categoria/data) alterado",
  PARTNER_CREATED: "Parceiro cadastrado",
  PARTNER_UPDATED: "Dados do parceiro alterados",
  PARTNER_ACTIVATED: "Parceiro reativado",
  PARTNER_DEACTIVATED: "Parceiro desativado",
  PARTNER_DELETED: "Cadastro de parceiro excluído",
  PARTNER_PASSWORD_RESET: "Senha do parceiro redefinida",
  COUPON_REPLACED: "Cupom substituído",
  COUPON_ACTIVATED: "Cupom ativado",
  COUPON_DEACTIVATED: "Cupom desativado",
  PAYOUT_REGISTERED: "Repasse registrado",
  SITE_COUPON_CREATED: "Cupom do site criado",
  SITE_COUPON_UPDATED: "Cupom do site alterado",
  SITE_COUPON_ACTIVATED: "Cupom do site ativado",
  SITE_COUPON_DEACTIVATED: "Cupom do site inativado",
  SITE_COUPON_DELETED: "Cupom do site excluído",
};

/** Descontos de uma contratação em texto (lançamento + cupom de parceiro + cupons do site, todos sobre o valor original). */
export function discountSummary(c: {
  launchDiscountPoints: number;
  partnerDiscountPoints: number;
  couponDiscountPoints: number;
  couponCode: string | null;
  siteCoupons?: { code: string; appliedPoints: number }[];
}): string {
  const parts = [`${c.launchDiscountPoints}% de lançamento`];
  if (c.partnerDiscountPoints) parts.push(`${c.partnerDiscountPoints}% do cupom ${c.couponCode}`);
  for (const s of c.siteCoupons ?? []) parts.push(`${s.appliedPoints}% do cupom ${s.code}`);
  return parts.join(" + ");
}

/** Códigos de cupom usados numa contratação (parceiro e site), para listagens. */
export function couponCodesOf(c: { couponCode: string | null; siteCoupons?: { code: string }[] }): string[] {
  return [...(c.couponCode ? [c.couponCode] : []), ...(c.siteCoupons ?? []).map((s) => s.code)];
}

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
