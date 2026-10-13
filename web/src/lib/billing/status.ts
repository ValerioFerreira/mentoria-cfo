import type { BillingDisputeStatus, BillingPaymentStatus } from "@/generated/prisma/client";

export function mapMercadoPagoPaymentStatus(statusValue: string, detailValue?: string | null): BillingPaymentStatus | null {
  const status = statusValue.toLowerCase();
  const detail = detailValue?.toLowerCase();
  if (status === "approved" && detail === "partially_refunded") return "PARTIALLY_REFUNDED";
  if (status === "charged_back") {
    if (detail === "reimbursed") return "CHARGEBACK_LOST";
    if (detail === "settled") return "CHARGEBACK_WON";
    return "DISPUTED";
  }
  if (status === "in_mediation") return "DISPUTED";
  const statuses: Record<string, BillingPaymentStatus> = {
    approved: "APPROVED",
    pending: "PENDING",
    in_process: "PENDING",
    authorized: "PENDING",
    rejected: "REJECTED",
    cancelled: "CANCELLED",
    refunded: "REFUNDED",
  };
  return statuses[status] ?? null;
}

export function mapMercadoPagoDisputeStatus(statusValue: string, detailValue?: string | null): BillingDisputeStatus {
  const status = (detailValue || statusValue).toLowerCase();
  if (status === "reimbursed") return "LOST";
  if (status === "settled") return "WON";
  return "IN_PROGRESS";
}
