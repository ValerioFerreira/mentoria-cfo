-- O valor do enum citava o provedor do material: passa a ser neutro (BASE)
ALTER TYPE "ContentSource" RENAME VALUE 'ESTRATEGIA' TO 'BASE';

-- Colunas que nunca foram usadas e também citavam o provedor
ALTER TABLE "Subject" DROP COLUMN "estrategiaSection";
ALTER TABLE "Profile" DROP COLUMN "estrategiaUrl";

-- CreateTable
CREATE TABLE "EditalItem" (
    "id" TEXT NOT NULL,
    "subjectId" TEXT NOT NULL,
    "code" TEXT NOT NULL,
    "title" TEXT NOT NULL,
    "aulaIds" JSONB NOT NULL,
    "sortOrder" INTEGER NOT NULL,

    CONSTRAINT "EditalItem_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE INDEX "EditalItem_subjectId_sortOrder_idx" ON "EditalItem"("subjectId", "sortOrder");

-- AddForeignKey
ALTER TABLE "EditalItem" ADD CONSTRAINT "EditalItem_subjectId_fkey" FOREIGN KEY ("subjectId") REFERENCES "Subject"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
