-- AlterEnum
ALTER TYPE "QuizKind" ADD VALUE IF NOT EXISTS 'SIMULADO';
ALTER TYPE "QuizKind" ADD VALUE IF NOT EXISTS 'CADERNO_PERSONALIZADO';

-- AlterTable Activity
ALTER TABLE "Activity" ADD COLUMN IF NOT EXISTS "editalItemId" TEXT;
ALTER TABLE "Activity" ADD COLUMN IF NOT EXISTS "editalTopic" TEXT;

-- AlterTable QuizSession
ALTER TABLE "QuizSession" ADD COLUMN IF NOT EXISTS "title" TEXT;
ALTER TABLE "QuizSession" ADD COLUMN IF NOT EXISTS "contest" "Contest";

-- CreateTable SystemSetting
CREATE TABLE IF NOT EXISTS "SystemSetting" (
    "key" TEXT NOT NULL,
    "value" TEXT NOT NULL,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "SystemSetting_pkey" PRIMARY KEY ("key")
);

-- CreateIndex
CREATE INDEX IF NOT EXISTS "Activity_editalItemId_idx" ON "Activity"("editalItemId");

-- CreateIndex
CREATE INDEX IF NOT EXISTS "QuizSession_userId_kind_idx" ON "QuizSession"("userId", "kind");

-- AddForeignKey
DO $$ BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint WHERE conname = 'Activity_editalItemId_fkey'
    ) THEN
        ALTER TABLE "Activity" ADD CONSTRAINT "Activity_editalItemId_fkey" FOREIGN KEY ("editalItemId") REFERENCES "EditalItem"("id") ON DELETE SET NULL ON UPDATE CASCADE;
    END IF;
END $$;
