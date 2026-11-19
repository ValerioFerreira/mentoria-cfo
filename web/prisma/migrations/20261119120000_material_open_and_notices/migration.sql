-- Avisos de novidade já vistos pelo aluno (pop-up) e registro de abertura dos PDFs do material (garantia de 7 dias).
ALTER TABLE "User" ADD COLUMN "seenNotices" TEXT[] DEFAULT ARRAY[]::TEXT[];

CREATE TABLE "MaterialOpen" (
    "userId" TEXT NOT NULL,
    "volumeId" TEXT NOT NULL,
    "firstOpenedAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "lastOpenedAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "opens" INTEGER NOT NULL DEFAULT 1,

    CONSTRAINT "MaterialOpen_pkey" PRIMARY KEY ("userId","volumeId")
);

CREATE INDEX "MaterialOpen_firstOpenedAt_idx" ON "MaterialOpen"("firstOpenedAt");

ALTER TABLE "MaterialOpen" ADD CONSTRAINT "MaterialOpen_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;
