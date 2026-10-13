-- CreateEnum
CREATE TYPE "QuestionKind" AS ENUM ('MULTIPLA_ESCOLHA', 'CERTO_ERRADO');

-- CreateEnum
CREATE TYPE "ClassifiedBy" AS ENUM ('AUTO', 'MANUAL');

-- AlterTable
ALTER TABLE "Question" ADD COLUMN     "ano" INTEGER,
ADD COLUMN     "cargo" TEXT,
ADD COLUMN     "classifiedBy" "ClassifiedBy" NOT NULL DEFAULT 'AUTO',
ADD COLUMN     "classifyNote" TEXT,
ADD COLUMN     "classifyScore" DOUBLE PRECISION,
ADD COLUMN     "contentHash" TEXT,
ADD COLUMN     "editalItemId" TEXT,
ADD COLUMN     "externalId" TEXT,
ADD COLUMN     "importedAt" TIMESTAMP(3),
ADD COLUMN     "kind" "QuestionKind" NOT NULL DEFAULT 'MULTIPLA_ESCOLHA',
ADD COLUMN     "orgao" TEXT,
ADD COLUMN     "sourceFile" TEXT,
ADD COLUMN     "tecAssunto" TEXT,
ADD COLUMN     "tecMateria" TEXT;

-- CreateTable
CREATE TABLE "QuestionImage" (
    "id" TEXT NOT NULL,
    "mime" TEXT NOT NULL DEFAULT 'image/png',
    "data" BYTEA NOT NULL,
    "width" INTEGER NOT NULL,
    "height" INTEGER NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "QuestionImage_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "Question_externalId_key" ON "Question"("externalId");

-- CreateIndex
CREATE INDEX "Question_editalItemId_status_idx" ON "Question"("editalItemId", "status");

-- AddForeignKey
ALTER TABLE "Question" ADD CONSTRAINT "Question_editalItemId_fkey" FOREIGN KEY ("editalItemId") REFERENCES "EditalItem"("id") ON DELETE SET NULL ON UPDATE CASCADE;
