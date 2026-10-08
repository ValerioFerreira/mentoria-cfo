-- DropForeignKey
ALTER TABLE "TimerState" DROP CONSTRAINT "TimerState_userId_fkey";

-- DropTable
DROP TABLE "TimerState";

-- DropEnum
DROP TYPE "TimerStatus";

