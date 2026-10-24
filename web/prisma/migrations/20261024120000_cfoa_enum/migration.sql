-- 2º Tenente CFOA CBMPE: nova chave no enum Contest.
ALTER TYPE "Contest" ADD VALUE IF NOT EXISTS 'CBMPE_CFOA';
