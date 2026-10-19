-- Categoria e data da prova para PCPE Agente de Polícia conforme edital
-- (Portaria Conjunta SAD/SDS nº 306/2026, Anexo I - Cronograma Previsto: 07/03/2027, turno da tarde; item 7.2).
-- Preenche apenas onde estiver vazio, preservando ajustes manuais de preço e data do administrador.

INSERT INTO "ContestSetting" ("contest", "category", "examDate", "updatedAt")
VALUES ('PCPE_AGENTE', 'PCPE', DATE '2027-03-07', NOW())
ON CONFLICT ("contest") DO UPDATE
SET "category" = COALESCE("ContestSetting"."category", EXCLUDED."category"),
    "examDate" = COALESCE("ContestSetting"."examDate", EXCLUDED."examDate");
