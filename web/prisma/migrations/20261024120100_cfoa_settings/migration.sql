-- Configuração do concurso 2º Tenente CFOA CBMPE: categoria de preço OFICIAL e data da prova vazia (NULL) até sair o edital.
INSERT INTO "ContestSetting" ("contest","category","examDate","updatedAt") VALUES ('CBMPE_CFOA','OFICIAL',NULL,NOW()) ON CONFLICT ("contest") DO UPDATE SET "category" = COALESCE("ContestSetting"."category", EXCLUDED."category");
