CREATE TYPE "BillingDisputeStatus" AS ENUM ('IN_PROGRESS', 'LOST', 'WON');

ALTER TABLE "BillingPayment" ADD COLUMN "accessUntil" TIMESTAMP(3);
CREATE INDEX "BillingPayment_status_accessUntil_idx" ON "BillingPayment"("status", "accessUntil");

CREATE TABLE "BillingDispute" (
    "id" TEXT NOT NULL,
    "billingPaymentId" TEXT NOT NULL,
    "providerChargebackId" TEXT NOT NULL,
    "status" "BillingDisputeStatus" NOT NULL,
    "statusDetail" TEXT,
    "amount" DECIMAL(10,2) NOT NULL,
    "currency" TEXT NOT NULL DEFAULT 'BRL',
    "lastEventAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,
    CONSTRAINT "BillingDispute_pkey" PRIMARY KEY ("id")
);

CREATE UNIQUE INDEX "BillingDispute_providerChargebackId_key" ON "BillingDispute"("providerChargebackId");
CREATE INDEX "BillingDispute_billingPaymentId_status_idx" ON "BillingDispute"("billingPaymentId", "status");

ALTER TABLE "BillingDispute" ADD CONSTRAINT "BillingDispute_billingPaymentId_fkey" FOREIGN KEY ("billingPaymentId") REFERENCES "BillingPayment"("id") ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE "BillingWebhookEvent" ADD COLUMN "resultStatus" TEXT;
ALTER TABLE "BillingWebhookEvent" ADD COLUMN "resultDetail" TEXT;

-- Preserve already-paid monthly access through its paid period, then normalize
-- old chargebacks using the provider detail previously stored by the webhook.
UPDATE "BillingPayment"
SET "status" = CASE lower(COALESCE("statusDetail", ''))
    WHEN 'reimbursed' THEN 'CHARGEBACK_LOST'::"BillingPaymentStatus"
    WHEN 'settled' THEN 'CHARGEBACK_WON'::"BillingPaymentStatus"
    ELSE 'DISPUTED'::"BillingPaymentStatus"
END
WHERE "status" = 'CHARGEBACK';

UPDATE "BillingPayment" payment
SET "accessUntil" = payment."paidAt" + INTERVAL '1 month'
FROM "BillingPurchase" purchase
WHERE purchase."id" = payment."purchaseId"
  AND purchase."product" = 'MONTHLY'
  AND payment."status" IN ('APPROVED', 'PARTIALLY_REFUNDED', 'DISPUTED', 'CHARGEBACK_WON')
  AND payment."paidAt" IS NOT NULL;

UPDATE "BillingPurchase" purchase
SET "status" = 'ACTIVE'
WHERE purchase."product" = 'PERMANENT'
  AND purchase."status" = 'CHARGEBACK'
  AND EXISTS (
      SELECT 1 FROM "BillingPayment" payment
      WHERE payment."purchaseId" = purchase."id"
        AND payment."status" IN ('DISPUTED', 'CHARGEBACK_WON')
  );
