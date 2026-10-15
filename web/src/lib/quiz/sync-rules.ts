// Regras puras da gravação das questões importadas (web/scripts/questoes-sync.ts). Ficam aqui para
// poderem ser testadas sem banco.
import type { QuestionStatus } from "@/generated/prisma/client";

export interface ExistingQuestionState {
  status: QuestionStatus;
  classifiedBy: "AUTO" | "MANUAL";
}

/**
 * Status final de uma questão que o importador está regravando.
 * - Anulada ou fora do edital (incoming RETIRED): sai de circulação.
 * - Denunciada (FLAGGED): continua denunciada até a revisão.
 * - Decisão do administrador (classifiedBy MANUAL): o status dele prevalece, inclusive RETIRED.
 * - Retirada AUTOMATICAMENTE (classificador ou curadoria antiga): volta com a classificação nova.
 *   Antes, RETIRED era definitivo e uma correção do mapa de assuntos nunca trazia a questão de volta.
 */
export function nextQuestionStatus(existing: ExistingQuestionState | null, incoming: QuestionStatus): QuestionStatus {
  if (incoming === "RETIRED" || !existing) return incoming;
  if (existing.status === "FLAGGED") return "FLAGGED";
  if (existing.classifiedBy === "MANUAL") return existing.status;
  return incoming;
}
