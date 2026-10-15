import type { Prisma, QuestionStatus } from "@/generated/prisma/client";

// Banca dos concursos atendidos. Planejamento (caderno das atividades) e simulados usam só questões dela;
// o banco de questões livre (treino e caderno personalizado) continua aceitando as demais bancas.
export const AOCP_BANCAS = ["AOCP", "Instituto AOCP", "INSTITUTO AOCP"];

/** Filtro das questões do caderno de uma atividade do plano: só os trechos estudados, só a banca AOCP. */
export function activityQuizWhere(segmentIds: string[], statuses: QuestionStatus[]) {
  return {
    segmentId: { in: segmentIds },
    status: { in: statuses },
    banca: { in: AOCP_BANCAS },
  } satisfies Prisma.QuestionWhereInput;
}
