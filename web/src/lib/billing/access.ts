import "server-only";
import type { BillingPaymentStatus, BillingProduct, BillingStatus } from "@/generated/prisma/client";
import { db } from "@/lib/db";

export type BillingEntitlementSnapshot = {
  product: BillingProduct;
  status: BillingStatus;
  payments: { status: BillingPaymentStatus; accessUntil: Date | null }[];
};

const PAYMENT_GRANTS_PERMANENT = new Set<BillingPaymentStatus>([
  "APPROVED", "CHARGEBACK", "PARTIALLY_REFUNDED", "DISPUTED", "CHARGEBACK_WON",
]);
const PAYMENT_GRANTS_MONTHLY = PAYMENT_GRANTS_PERMANENT;

/** Decisão de autorização isolada para que os cenários de cobrança possam ser testados sem DB. */
export function grantsBillingAccess(purchases: BillingEntitlementSnapshot[], now = new Date()): boolean {
  return purchases.some((purchase) => {
    if (purchase.product === "PERMANENT") {
      return purchase.status === "ACTIVE" && purchase.payments.some((payment) => PAYMENT_GRANTS_PERMANENT.has(payment.status));
    }
    return purchase.payments.some((payment) =>
      PAYMENT_GRANTS_MONTHLY.has(payment.status) && payment.accessUntil !== null && payment.accessUntil > now,
    );
  });
}

export async function hasBillingAccess(userId: string, now = new Date()): Promise<boolean> {
  const purchases = await db.billingPurchase.findMany({
    where: { userId },
    select: {
      product: true,
      status: true,
      payments: { select: { status: true, accessUntil: true } },
    },
  });
  return grantsBillingAccess(purchases, now);
}
