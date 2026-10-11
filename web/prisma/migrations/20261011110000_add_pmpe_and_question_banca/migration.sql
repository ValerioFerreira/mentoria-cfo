-- AlterEnum
ALTER TYPE "Contest" ADD VALUE IF NOT EXISTS 'PMPE_SOLDADO';
ALTER TYPE "Contest" ADD VALUE IF NOT EXISTS 'PMPE_OFICIAL';

-- AlterTable Question
ALTER TABLE "Question" ADD COLUMN IF NOT EXISTS "banca" TEXT NOT NULL DEFAULT 'AOCP';

-- CreateIndex
CREATE INDEX IF NOT EXISTS "Question_banca_idx" ON "Question"("banca");
