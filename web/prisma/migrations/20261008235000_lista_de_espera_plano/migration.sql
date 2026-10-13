-- CreateEnum
CREATE TYPE "WaitlistPlan" AS ENUM ('MONTHLY', 'UNTIL_EXAM');

-- AlterTable
ALTER TABLE "WaitlistEntry" ADD COLUMN     "plan" "WaitlistPlan";
