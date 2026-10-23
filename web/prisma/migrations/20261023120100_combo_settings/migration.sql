-- Configuração dos pacotes combo: categoria COMBO e data da prova (a mesma dos dois concursos de cada corporação).
-- Só cria/preenche onde ainda não há valor (não sobrescreve ajustes do administrador).
INSERT INTO "ContestSetting" ("contest", "category", "examDate", "updatedAt")
VALUES ('CBMPE_COMBO', 'COMBO', DATE '2027-02-28', NOW()), ('PMPE_COMBO', 'COMBO', DATE '2027-02-21', NOW())
ON CONFLICT ("contest") DO UPDATE SET
  "category" = COALESCE("ContestSetting"."category", EXCLUDED."category"),
  "examDate" = COALESCE("ContestSetting"."examDate", EXCLUDED."examDate");
