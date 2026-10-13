
-- CreateEnum
CREATE TYPE "Contest" AS ENUM ('CBMPE_SOLDADO', 'CBMPE_OFICIAL', 'PCPE_AGENTE');

-- AlterTable
ALTER TABLE "User" ADD COLUMN     "username" TEXT;

-- CreateTable
CREATE TABLE "WaitlistEntry" (
    "id" TEXT NOT NULL,
    "contest" "Contest" NOT NULL,
    "name" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "username" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "paidAt" TIMESTAMP(3),
    "note" TEXT,

    CONSTRAINT "WaitlistEntry_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "WaitlistEntry_username_key" ON "WaitlistEntry"("username");

-- CreateIndex
CREATE INDEX "WaitlistEntry_createdAt_idx" ON "WaitlistEntry"("createdAt");

-- CreateIndex
CREATE UNIQUE INDEX "WaitlistEntry_contest_email_key" ON "WaitlistEntry"("contest", "email");

-- CreateIndex
CREATE UNIQUE INDEX "User_username_key" ON "User"("username");

