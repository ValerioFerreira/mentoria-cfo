-- Modo Turbo: atividade de Teoria substituída pelo resumo do trecho
ALTER TABLE "Activity" ADD COLUMN "turbo" BOOLEAN NOT NULL DEFAULT false;
