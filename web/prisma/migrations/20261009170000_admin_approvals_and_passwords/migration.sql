-- AlterTable User
ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "mustChangePassword" BOOLEAN NOT NULL DEFAULT false;
ALTER TABLE "User" ADD COLUMN IF NOT EXISTS "accessExpiresAt" TIMESTAMP(3);

-- AlterTable WaitlistEntry
ALTER TABLE "WaitlistEntry" ADD COLUMN IF NOT EXISTS "status" TEXT NOT NULL DEFAULT 'PENDING';
ALTER TABLE "WaitlistEntry" ADD COLUMN IF NOT EXISTS "approvedAt" TIMESTAMP(3);
ALTER TABLE "WaitlistEntry" ADD COLUMN IF NOT EXISTS "rejectedAt" TIMESTAMP(3);
ALTER TABLE "WaitlistEntry" ADD COLUMN IF NOT EXISTS "accessDuration" TEXT;
ALTER TABLE "WaitlistEntry" ADD COLUMN IF NOT EXISTS "rejectionReason" TEXT;

-- CreateIndex
CREATE INDEX IF NOT EXISTS "WaitlistEntry_status_idx" ON "WaitlistEntry"("status");
