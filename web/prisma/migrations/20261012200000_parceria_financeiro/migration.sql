-- Sistema de parceiros, preços por concurso e controle financeiro manual.
-- Incremental: só cria tipos, tabelas, índices e restrições; não altera nem remove dados existentes
-- (BillingPurchase/BillingPayment/assinaturas do Mercado Pago ficam preservadas como histórico).

-- CreateEnum
CREATE TYPE "ContestCategory" AS ENUM ('OFICIAL', 'PCPE', 'PRACA');

-- CreateEnum
CREATE TYPE "ContractStatus" AS ENUM ('OPEN', 'PARTIAL', 'PAID', 'OVERPAID', 'CANCELLED');

-- CreateEnum
CREATE TYPE "PaymentMethod" AS ENUM ('PIX', 'TRANSFERENCIA', 'DINHEIRO', 'OUTRO');

-- CreateEnum
CREATE TYPE "ReversalKind" AS ENUM ('ESTORNO', 'CORRECAO');

-- CreateEnum
CREATE TYPE "CommissionKind" AS ENUM ('ACCRUAL', 'REVERSAL');

-- CreateTable
CREATE TABLE "ContestSetting" (
    "contest" "Contest" NOT NULL,
    "category" "ContestCategory",
    "examDate" DATE,
    "updatedById" TEXT,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "ContestSetting_pkey" PRIMARY KEY ("contest")
);

-- CreateTable
CREATE TABLE "Contract" (
    "id" TEXT NOT NULL,
    "userId" TEXT,
    "customerEmail" TEXT NOT NULL,
    "customerName" TEXT,
    "waitlistEntryId" TEXT,
    "contest" "Contest" NOT NULL,
    "category" "ContestCategory" NOT NULL,
    "examDateAtContract" DATE,
    "pricingRule" TEXT NOT NULL,
    "originalAmount" DECIMAL(10,2) NOT NULL,
    "launchDiscountPoints" INTEGER NOT NULL,
    "partnerDiscountPoints" INTEGER NOT NULL DEFAULT 0,
    "discountAmount" DECIMAL(10,2) NOT NULL,
    "finalAmount" DECIMAL(10,2) NOT NULL,
    "couponId" TEXT,
    "couponCode" TEXT,
    "partnerId" TEXT,
    "status" "ContractStatus" NOT NULL DEFAULT 'OPEN',
    "paidAmount" DECIMAL(10,2) NOT NULL DEFAULT 0,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,
    "cancelledAt" TIMESTAMP(3),
    "cancelReason" TEXT,
    "cancelledById" TEXT,
    "accessGrantedAt" TIMESTAMP(3),
    "accessUntil" TIMESTAMP(3),
    "accessGrantedById" TEXT,

    CONSTRAINT "Contract_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "ManualPayment" (
    "id" TEXT NOT NULL,
    "contractId" TEXT NOT NULL,
    "amount" DECIMAL(10,2) NOT NULL,
    "paidAt" TIMESTAMP(3) NOT NULL,
    "method" "PaymentMethod" NOT NULL,
    "receiptRef" TEXT,
    "note" TEXT,
    "createdById" TEXT NOT NULL,
    "idempotencyKey" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "ManualPayment_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "PaymentReversal" (
    "id" TEXT NOT NULL,
    "paymentId" TEXT NOT NULL,
    "contractId" TEXT NOT NULL,
    "amount" DECIMAL(10,2) NOT NULL,
    "kind" "ReversalKind" NOT NULL,
    "reason" TEXT NOT NULL,
    "effectiveAt" TIMESTAMP(3) NOT NULL,
    "createdById" TEXT NOT NULL,
    "idempotencyKey" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "PaymentReversal_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Partner" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "active" BOOLEAN NOT NULL DEFAULT true,
    "createdById" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,
    "deactivatedAt" TIMESTAMP(3),

    CONSTRAINT "Partner_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "PartnerCoupon" (
    "id" TEXT NOT NULL,
    "partnerId" TEXT NOT NULL,
    "code" TEXT NOT NULL,
    "discountPoints" INTEGER NOT NULL,
    "active" BOOLEAN NOT NULL DEFAULT true,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "deactivatedAt" TIMESTAMP(3),
    "replacedAt" TIMESTAMP(3),

    CONSTRAINT "PartnerCoupon_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "PartnerReferral" (
    "id" TEXT NOT NULL,
    "partnerId" TEXT NOT NULL,
    "customerEmail" TEXT NOT NULL,
    "userId" TEXT,
    "couponId" TEXT NOT NULL,
    "couponCode" TEXT NOT NULL,
    "firstContractId" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "PartnerReferral_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "CommissionEntry" (
    "id" TEXT NOT NULL,
    "partnerId" TEXT NOT NULL,
    "contractId" TEXT NOT NULL,
    "paymentId" TEXT NOT NULL,
    "reversalId" TEXT,
    "kind" "CommissionKind" NOT NULL,
    "amount" DECIMAL(10,2) NOT NULL,
    "basisAmount" DECIMAL(10,2) NOT NULL,
    "rateBp" INTEGER NOT NULL,
    "availableAt" TIMESTAMP(3) NOT NULL,
    "sourceKey" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "CommissionEntry_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "PartnerPayout" (
    "id" TEXT NOT NULL,
    "partnerId" TEXT NOT NULL,
    "amount" DECIMAL(10,2) NOT NULL,
    "paidAt" TIMESTAMP(3) NOT NULL,
    "method" TEXT NOT NULL,
    "receiptRef" TEXT,
    "note" TEXT,
    "createdById" TEXT NOT NULL,
    "idempotencyKey" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "PartnerPayout_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "AuditLog" (
    "id" TEXT NOT NULL,
    "actorId" TEXT,
    "action" TEXT NOT NULL,
    "entityType" TEXT NOT NULL,
    "entityId" TEXT NOT NULL,
    "data" JSONB,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "AuditLog_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE INDEX "Contract_userId_idx" ON "Contract"("userId");

-- CreateIndex
CREATE INDEX "Contract_waitlistEntryId_idx" ON "Contract"("waitlistEntryId");

-- CreateIndex
CREATE INDEX "Contract_customerEmail_contest_idx" ON "Contract"("customerEmail", "contest");

-- CreateIndex
CREATE INDEX "Contract_partnerId_createdAt_idx" ON "Contract"("partnerId", "createdAt");

-- CreateIndex
CREATE INDEX "Contract_status_createdAt_idx" ON "Contract"("status", "createdAt");

-- CreateIndex
CREATE INDEX "Contract_contest_createdAt_idx" ON "Contract"("contest", "createdAt");

-- CreateIndex
CREATE UNIQUE INDEX "ManualPayment_idempotencyKey_key" ON "ManualPayment"("idempotencyKey");

-- CreateIndex
CREATE INDEX "ManualPayment_contractId_paidAt_idx" ON "ManualPayment"("contractId", "paidAt");

-- CreateIndex
CREATE INDEX "ManualPayment_paidAt_idx" ON "ManualPayment"("paidAt");

-- CreateIndex
CREATE INDEX "ManualPayment_method_paidAt_idx" ON "ManualPayment"("method", "paidAt");

-- CreateIndex
CREATE INDEX "ManualPayment_receiptRef_idx" ON "ManualPayment"("receiptRef");

-- CreateIndex
CREATE UNIQUE INDEX "PaymentReversal_idempotencyKey_key" ON "PaymentReversal"("idempotencyKey");

-- CreateIndex
CREATE INDEX "PaymentReversal_paymentId_idx" ON "PaymentReversal"("paymentId");

-- CreateIndex
CREATE INDEX "PaymentReversal_contractId_idx" ON "PaymentReversal"("contractId");

-- CreateIndex
CREATE UNIQUE INDEX "Partner_userId_key" ON "Partner"("userId");

-- CreateIndex
CREATE INDEX "Partner_active_idx" ON "Partner"("active");

-- CreateIndex
CREATE UNIQUE INDEX "PartnerCoupon_code_key" ON "PartnerCoupon"("code");

-- CreateIndex
CREATE INDEX "PartnerCoupon_partnerId_active_idx" ON "PartnerCoupon"("partnerId", "active");

-- CreateIndex
CREATE UNIQUE INDEX "PartnerReferral_customerEmail_key" ON "PartnerReferral"("customerEmail");

-- CreateIndex
CREATE UNIQUE INDEX "PartnerReferral_firstContractId_key" ON "PartnerReferral"("firstContractId");

-- CreateIndex
CREATE INDEX "PartnerReferral_partnerId_createdAt_idx" ON "PartnerReferral"("partnerId", "createdAt");

-- CreateIndex
CREATE UNIQUE INDEX "CommissionEntry_sourceKey_key" ON "CommissionEntry"("sourceKey");

-- CreateIndex
CREATE INDEX "CommissionEntry_partnerId_createdAt_idx" ON "CommissionEntry"("partnerId", "createdAt");

-- CreateIndex
CREATE INDEX "CommissionEntry_contractId_idx" ON "CommissionEntry"("contractId");

-- CreateIndex
CREATE UNIQUE INDEX "PartnerPayout_idempotencyKey_key" ON "PartnerPayout"("idempotencyKey");

-- CreateIndex
CREATE INDEX "PartnerPayout_partnerId_paidAt_idx" ON "PartnerPayout"("partnerId", "paidAt");

-- CreateIndex
CREATE INDEX "AuditLog_entityType_entityId_createdAt_idx" ON "AuditLog"("entityType", "entityId", "createdAt");

-- CreateIndex
CREATE INDEX "AuditLog_createdAt_idx" ON "AuditLog"("createdAt");

-- CreateIndex
CREATE INDEX "AuditLog_actorId_createdAt_idx" ON "AuditLog"("actorId", "createdAt");

-- AddForeignKey
ALTER TABLE "Contract" ADD CONSTRAINT "Contract_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Contract" ADD CONSTRAINT "Contract_waitlistEntryId_fkey" FOREIGN KEY ("waitlistEntryId") REFERENCES "WaitlistEntry"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Contract" ADD CONSTRAINT "Contract_couponId_fkey" FOREIGN KEY ("couponId") REFERENCES "PartnerCoupon"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Contract" ADD CONSTRAINT "Contract_partnerId_fkey" FOREIGN KEY ("partnerId") REFERENCES "Partner"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "ManualPayment" ADD CONSTRAINT "ManualPayment_contractId_fkey" FOREIGN KEY ("contractId") REFERENCES "Contract"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "ManualPayment" ADD CONSTRAINT "ManualPayment_createdById_fkey" FOREIGN KEY ("createdById") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "PaymentReversal" ADD CONSTRAINT "PaymentReversal_paymentId_fkey" FOREIGN KEY ("paymentId") REFERENCES "ManualPayment"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "PaymentReversal" ADD CONSTRAINT "PaymentReversal_contractId_fkey" FOREIGN KEY ("contractId") REFERENCES "Contract"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "PaymentReversal" ADD CONSTRAINT "PaymentReversal_createdById_fkey" FOREIGN KEY ("createdById") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Partner" ADD CONSTRAINT "Partner_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "PartnerCoupon" ADD CONSTRAINT "PartnerCoupon_partnerId_fkey" FOREIGN KEY ("partnerId") REFERENCES "Partner"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "PartnerReferral" ADD CONSTRAINT "PartnerReferral_partnerId_fkey" FOREIGN KEY ("partnerId") REFERENCES "Partner"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "PartnerReferral" ADD CONSTRAINT "PartnerReferral_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "PartnerReferral" ADD CONSTRAINT "PartnerReferral_couponId_fkey" FOREIGN KEY ("couponId") REFERENCES "PartnerCoupon"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "PartnerReferral" ADD CONSTRAINT "PartnerReferral_firstContractId_fkey" FOREIGN KEY ("firstContractId") REFERENCES "Contract"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommissionEntry" ADD CONSTRAINT "CommissionEntry_partnerId_fkey" FOREIGN KEY ("partnerId") REFERENCES "Partner"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommissionEntry" ADD CONSTRAINT "CommissionEntry_contractId_fkey" FOREIGN KEY ("contractId") REFERENCES "Contract"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommissionEntry" ADD CONSTRAINT "CommissionEntry_paymentId_fkey" FOREIGN KEY ("paymentId") REFERENCES "ManualPayment"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "CommissionEntry" ADD CONSTRAINT "CommissionEntry_reversalId_fkey" FOREIGN KEY ("reversalId") REFERENCES "PaymentReversal"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "PartnerPayout" ADD CONSTRAINT "PartnerPayout_partnerId_fkey" FOREIGN KEY ("partnerId") REFERENCES "Partner"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "PartnerPayout" ADD CONSTRAINT "PartnerPayout_createdById_fkey" FOREIGN KEY ("createdById") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;


-- Integridade financeira no banco (além da validação no servidor)
ALTER TABLE "Contract" ADD CONSTRAINT "Contract_amounts_check" CHECK (
  "originalAmount" > 0 AND "discountAmount" >= 0 AND "finalAmount" >= 0 AND "paidAmount" >= 0
  AND "finalAmount" = "originalAmount" - "discountAmount"
  AND "launchDiscountPoints" BETWEEN 0 AND 100 AND "partnerDiscountPoints" BETWEEN 0 AND 100
  AND "launchDiscountPoints" + "partnerDiscountPoints" <= 100
);
ALTER TABLE "ManualPayment" ADD CONSTRAINT "ManualPayment_amount_check" CHECK ("amount" > 0);
ALTER TABLE "PaymentReversal" ADD CONSTRAINT "PaymentReversal_amount_check" CHECK ("amount" > 0);
ALTER TABLE "PartnerPayout" ADD CONSTRAINT "PartnerPayout_amount_check" CHECK ("amount" > 0);
ALTER TABLE "PartnerCoupon" ADD CONSTRAINT "PartnerCoupon_discount_check" CHECK ("discountPoints" BETWEEN 0 AND 100);
ALTER TABLE "CommissionEntry" ADD CONSTRAINT "CommissionEntry_sign_check" CHECK (
  ("kind" = 'ACCRUAL' AND "amount" > 0) OR ("kind" = 'REVERSAL' AND "amount" < 0)
);

-- Classificação comercial persistida dos concursos existentes. Data da prova só onde há data oficial no sistema
-- (CBMPE Oficial: 28/02/2027); as demais ficam nulas = pendência administrativa (acesso "até a prova" não é concedido).
INSERT INTO "ContestSetting" ("contest", "category", "examDate", "updatedAt") VALUES
  ('CBMPE_OFICIAL', 'OFICIAL', DATE '2027-02-28', CURRENT_TIMESTAMP),
  ('CBMPE_SOLDADO', 'PRACA', NULL, CURRENT_TIMESTAMP),
  ('PMPE_OFICIAL', 'OFICIAL', NULL, CURRENT_TIMESTAMP),
  ('PMPE_SOLDADO', 'PRACA', NULL, CURRENT_TIMESTAMP),
  ('PCPE_AGENTE', 'PCPE', NULL, CURRENT_TIMESTAMP)
ON CONFLICT ("contest") DO NOTHING;
