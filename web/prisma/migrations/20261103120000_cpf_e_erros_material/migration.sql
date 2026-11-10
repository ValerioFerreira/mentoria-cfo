-- CPF do aluno (carimbo no rodapé dos PDFs do material próprio) e erros reportados nos PDFs.
ALTER TABLE "User" ADD COLUMN "cpf" TEXT;

CREATE TABLE "MaterialErrorReport" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "volumeId" TEXT NOT NULL,
    "chapter" TEXT,
    "page" INTEGER NOT NULL,
    "message" TEXT NOT NULL,
    "status" TEXT NOT NULL DEFAULT 'OPEN',
    "adminNote" TEXT,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "resolvedAt" TIMESTAMP(3),

    CONSTRAINT "MaterialErrorReport_pkey" PRIMARY KEY ("id")
);

CREATE INDEX "MaterialErrorReport_status_createdAt_idx" ON "MaterialErrorReport"("status", "createdAt");
CREATE INDEX "MaterialErrorReport_volumeId_idx" ON "MaterialErrorReport"("volumeId");

ALTER TABLE "MaterialErrorReport" ADD CONSTRAINT "MaterialErrorReport_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;
