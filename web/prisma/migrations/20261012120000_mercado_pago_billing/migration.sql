CREATE TYPE "BillingProduct" AS ENUM ('MONTHLY', 'PERMANENT');
CREATE TYPE "BillingStatus" AS ENUM ('PENDING', 'ACTIVE', 'PAST_DUE', 'CANCELLED', 'EXPIRED', 'REFUNDED', 'CHARGEBACK');
CREATE TYPE "BillingPaymentStatus" AS ENUM ('PENDING', 'APPROVED', 'REJECTED', 'CANCELLED', 'REFUNDED', 'CHARGEBACK');

CREATE TABLE "BillingPurchase" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "product" "BillingProduct" NOT NULL,
    "status" "BillingStatus" NOT NULL DEFAULT 'PENDING',
    "amount" DECIMAL(10,2) NOT NULL,
    "currency" TEXT NOT NULL DEFAULT 'BRL',
    "externalReference" TEXT NOT NULL,
    "mpPreferenceId" TEXT,
    "mpPreapprovalId" TEXT,
    "checkoutUrl" TEXT,
    "currentPeriodEnd" TIMESTAMP(3),
    "cancelledAt" TIMESTAMP(3),
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,
    CONSTRAINT "BillingPurchase_pkey" PRIMARY KEY ("id")
);

CREATE TABLE "BillingPayment" (
    "id" TEXT NOT NULL,
    "purchaseId" TEXT NOT NULL,
    "providerPaymentId" TEXT NOT NULL,
    "status" "BillingPaymentStatus" NOT NULL,
    "amount" DECIMAL(10,2) NOT NULL,
    "currency" TEXT NOT NULL DEFAULT 'BRL',
    "statusDetail" TEXT,
    "paidAt" TIMESTAMP(3),
    "updatedAt" TIMESTAMP(3) NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "BillingPayment_pkey" PRIMARY KEY ("id")
);

CREATE TABLE "BillingWebhookEvent" (
    "id" TEXT NOT NULL,
    "eventKey" TEXT NOT NULL,
    "resourceId" TEXT NOT NULL,
    "topic" TEXT NOT NULL,
    "action" TEXT,
    "processedAt" TIMESTAMP(3),
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "BillingWebhookEvent_pkey" PRIMARY KEY ("id")
);

CREATE UNIQUE INDEX "BillingPurchase_externalReference_key" ON "BillingPurchase"("externalReference");
CREATE UNIQUE INDEX "BillingPurchase_mpPreferenceId_key" ON "BillingPurchase"("mpPreferenceId");
CREATE UNIQUE INDEX "BillingPurchase_mpPreapprovalId_key" ON "BillingPurchase"("mpPreapprovalId");
CREATE INDEX "BillingPurchase_userId_product_status_idx" ON "BillingPurchase"("userId", "product", "status");
CREATE INDEX "BillingPurchase_status_currentPeriodEnd_idx" ON "BillingPurchase"("status", "currentPeriodEnd");
CREATE UNIQUE INDEX "BillingPayment_providerPaymentId_key" ON "BillingPayment"("providerPaymentId");
CREATE INDEX "BillingPayment_purchaseId_status_idx" ON "BillingPayment"("purchaseId", "status");
CREATE UNIQUE INDEX "BillingWebhookEvent_eventKey_key" ON "BillingWebhookEvent"("eventKey");
CREATE INDEX "BillingWebhookEvent_resourceId_topic_idx" ON "BillingWebhookEvent"("resourceId", "topic");

ALTER TABLE "BillingPurchase" ADD CONSTRAINT "BillingPurchase_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "BillingPayment" ADD CONSTRAINT "BillingPayment_purchaseId_fkey" FOREIGN KEY ("purchaseId") REFERENCES "BillingPurchase"("id") ON DELETE CASCADE ON UPDATE CASCADE;
