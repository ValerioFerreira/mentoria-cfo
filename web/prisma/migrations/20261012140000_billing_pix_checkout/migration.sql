ALTER TABLE "BillingPurchase"
    ADD COLUMN "mpPixPaymentId" TEXT,
    ADD COLUMN "pixQrCode" TEXT,
    ADD COLUMN "pixQrCodeBase64" TEXT,
    ADD COLUMN "pixTicketUrl" TEXT,
    ADD COLUMN "pixExpiresAt" TIMESTAMP(3);

CREATE UNIQUE INDEX "BillingPurchase_mpPixPaymentId_key" ON "BillingPurchase"("mpPixPaymentId");
