-- AlterEnum
ALTER TYPE "ContentSource" ADD VALUE 'AUTHORED';

-- AlterTable
ALTER TABLE "Activity" ADD COLUMN     "dayIndex" INTEGER;

-- AlterTable
ALTER TABLE "Aula" ADD COLUMN     "materialPath" TEXT;

-- AlterTable
ALTER TABLE "Gap" ADD COLUMN     "resolution" TEXT,
ADD COLUMN     "resolved" BOOLEAN NOT NULL DEFAULT false;

