-- Preço e desconto do site configuráveis por concurso (nulo = padrão da categoria / desconto de lançamento).
ALTER TABLE "ContestSetting" ADD COLUMN "priceCents" INTEGER;
ALTER TABLE "ContestSetting" ADD COLUMN "siteDiscountPoints" INTEGER;

-- Datas das provas conforme os editais de 2026 (Instituto AOCP): CBMPE (Soldado e 2º Tenente) em 28/02/2027;
-- PMPE (Soldado e Oficial) em 21/02/2027. Só preenche onde ainda não há data (não sobrescreve ajustes do administrador).
UPDATE "ContestSetting" SET "examDate" = DATE '2027-02-28' WHERE "contest" IN ('CBMPE_OFICIAL', 'CBMPE_SOLDADO') AND "examDate" IS NULL;
UPDATE "ContestSetting" SET "examDate" = DATE '2027-02-21' WHERE "contest" IN ('PMPE_OFICIAL', 'PMPE_SOLDADO') AND "examDate" IS NULL;
