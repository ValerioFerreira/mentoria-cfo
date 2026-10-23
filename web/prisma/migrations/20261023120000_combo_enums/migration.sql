-- Pacotes combo (2º Tenente + Soldado): novas chaves de concurso e categoria de preço.
ALTER TYPE "Contest" ADD VALUE IF NOT EXISTS 'CBMPE_COMBO';
ALTER TYPE "Contest" ADD VALUE IF NOT EXISTS 'PMPE_COMBO';
ALTER TYPE "ContestCategory" ADD VALUE IF NOT EXISTS 'COMBO';
