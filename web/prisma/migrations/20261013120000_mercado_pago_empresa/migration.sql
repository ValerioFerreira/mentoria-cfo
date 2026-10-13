-- Pagamentos online pela conta Mercado Pago da empresa, ligados ao mesmo livro-caixa da parceria.
-- Somente aditiva: nenhuma linha existente é alterada (os recebimentos já lançados continuam MANUAL).
-- ManualPayment/PaymentReversal passam a aceitar lançamentos automáticos (sem usuário), identificados por `source`.
-- CreateEnum
CREATE TYPE "PaymentSource" AS ENUM ('MANUAL', 'MERCADO_PAGO');

-- CreateEnum
CREATE TYPE "OnlineChargeKind" AS ENUM ('PIX', 'CHECKOUT');

-- CreateEnum
CREATE TYPE "OnlineChargeStatus" AS ENUM ('PENDING', 'APPROVED', 'REJECTED', 'CANCELLED', 'EXPIRED', 'REFUNDED', 'CHARGED_BACK');

-- AlterEnum
ALTER TYPE "PaymentMethod" ADD VALUE 'CARTAO';

-- AlterTable
ALTER TABLE "ManualPayment" ADD COLUMN     "providerPaymentId" TEXT,
ADD COLUMN     "source" "PaymentSource" NOT NULL DEFAULT 'MANUAL',
ALTER COLUMN "createdById" DROP NOT NULL;

-- AlterTable
ALTER TABLE "PaymentReversal" ADD COLUMN     "source" "PaymentSource" NOT NULL DEFAULT 'MANUAL',
ALTER COLUMN "createdById" DROP NOT NULL;

-- CreateTable
CREATE TABLE "OnlineCharge" (
    "id" TEXT NOT NULL,
    "contractId" TEXT NOT NULL,
    "kind" "OnlineChargeKind" NOT NULL,
    "amount" DECIMAL(10,2) NOT NULL,
    "status" "OnlineChargeStatus" NOT NULL DEFAULT 'PENDING',
    "providerPaymentId" TEXT,
    "preferenceId" TEXT,
    "checkoutUrl" TEXT,
    "qrCode" TEXT,
    "qrCodeBase64" TEXT,
    "ticketUrl" TEXT,
    "expiresAt" TIMESTAMP(3),
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "OnlineCharge_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "OnlineCharge_providerPaymentId_key" ON "OnlineCharge"("providerPaymentId");

-- CreateIndex
CREATE UNIQUE INDEX "OnlineCharge_preferenceId_key" ON "OnlineCharge"("preferenceId");

-- CreateIndex
CREATE INDEX "OnlineCharge_contractId_status_idx" ON "OnlineCharge"("contractId", "status");

-- CreateIndex
CREATE INDEX "OnlineCharge_status_expiresAt_idx" ON "OnlineCharge"("status", "expiresAt");

-- CreateIndex
CREATE UNIQUE INDEX "ManualPayment_providerPaymentId_key" ON "ManualPayment"("providerPaymentId");

-- AddForeignKey
ALTER TABLE "OnlineCharge" ADD CONSTRAINT "OnlineCharge_contractId_fkey" FOREIGN KEY ("contractId") REFERENCES "Contract"("id") ON DELETE RESTRICT ON UPDATE CASCADE;


-- Integridade (o Prisma não representa CHECK): lançamento manual tem autor; automático tem o id do pagamento no provedor.
ALTER TABLE "ManualPayment" ADD CONSTRAINT "ManualPayment_origin_check"
  CHECK (("source" = 'MANUAL' AND "createdById" IS NOT NULL AND "providerPaymentId" IS NULL)
      OR ("source" = 'MERCADO_PAGO' AND "providerPaymentId" IS NOT NULL));
ALTER TABLE "PaymentReversal" ADD CONSTRAINT "PaymentReversal_origin_check"
  CHECK ("source" = 'MERCADO_PAGO' OR "createdById" IS NOT NULL);
ALTER TABLE "OnlineCharge" ADD CONSTRAINT "OnlineCharge_amount_check" CHECK ("amount" > 0);
ALTER TABLE "OnlineCharge" ADD CONSTRAINT "OnlineCharge_ref_check"
  CHECK (("kind" = 'PIX' AND "preferenceId" IS NULL) OR ("kind" = 'CHECKOUT' AND "providerPaymentId" IS NULL));
