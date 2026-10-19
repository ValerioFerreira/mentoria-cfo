-- AlterTable
ALTER TABLE "EditalItem" ADD COLUMN "onlyContests" TEXT[] NOT NULL DEFAULT ARRAY[]::TEXT[],
ADD COLUMN "excludeContests" TEXT[] NOT NULL DEFAULT ARRAY[]::TEXT[];
