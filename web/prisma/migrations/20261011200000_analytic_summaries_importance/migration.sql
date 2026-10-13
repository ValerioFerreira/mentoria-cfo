-- CreateEnum
CREATE TYPE "SummaryStatus" AS ENUM ('DRAFT', 'APPROVED');

-- AlterTable: concurso do plano (planos antigos ficam nulos = CBMPE_OFICIAL)
ALTER TABLE "Plan" ADD COLUMN IF NOT EXISTS "contest" "Contest";

-- CreateTable
CREATE TABLE "AnalyticSummary" (
    "id" TEXT NOT NULL,
    "segmentId" TEXT NOT NULL,
    "markdown" TEXT NOT NULL,
    "words" INTEGER NOT NULL,
    "readMinutes" INTEGER NOT NULL,
    "status" "SummaryStatus" NOT NULL DEFAULT 'DRAFT',
    "fingerprint" JSONB NOT NULL,
    "version" INTEGER NOT NULL DEFAULT 1,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "AnalyticSummary_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "SegmentImportance" (
    "segmentId" TEXT NOT NULL,
    "contest" "Contest" NOT NULL,
    "appears" BOOLEAN NOT NULL,
    "expected" DOUBLE PRECISION NOT NULL,
    "score" INTEGER,

    CONSTRAINT "SegmentImportance_pkey" PRIMARY KEY ("segmentId","contest")
);

-- CreateIndex
CREATE UNIQUE INDEX "AnalyticSummary_segmentId_key" ON "AnalyticSummary"("segmentId");

-- CreateIndex
CREATE INDEX "SegmentImportance_contest_score_idx" ON "SegmentImportance"("contest", "score");

-- AddForeignKey
ALTER TABLE "AnalyticSummary" ADD CONSTRAINT "AnalyticSummary_segmentId_fkey" FOREIGN KEY ("segmentId") REFERENCES "Segment"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "SegmentImportance" ADD CONSTRAINT "SegmentImportance_segmentId_fkey" FOREIGN KEY ("segmentId") REFERENCES "Segment"("id") ON DELETE CASCADE ON UPDATE CASCADE;
