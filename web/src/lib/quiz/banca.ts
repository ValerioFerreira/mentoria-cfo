import type { Contest, Prisma, QuestionStatus } from "@/generated/prisma/client";

// Banca dos concursos atendidos. Planejamento (caderno das atividades) e simulados usam só questões dela;
// o banco de questões livre (treino e caderno personalizado) continua aceitando as demais bancas.
export const AOCP_BANCAS = ["AOCP", "Instituto AOCP", "INSTITUTO AOCP"];
export const CEBRASPE_BANCAS = ["CEBRASPE", "Cebraspe", "CESPE", "Cespe / UnB", "CESPE / CEBRASPE", "Cespe"];

export function contestBancas(contest?: Contest | null): string[] {
  if (contest === "PCPE_AGENTE") {
    // Provisório (decisão do dono em 2026-10-19): enquanto os cadernos Cebraspe não são importados, o PCPE também
    // recebe as questões AOCP que cobrem os assuntos do seu edital. Depois, volta a ser só CEBRASPE_BANCAS.
    return [...CEBRASPE_BANCAS, ...AOCP_BANCAS];
  }
  return AOCP_BANCAS;
}

/** Filtro das questões do caderno de uma atividade do plano: só os trechos estudados, banca do concurso. */
export function activityQuizWhere(segmentIds: string[], statuses: QuestionStatus[], contest?: Contest | null) {
  return {
    segmentId: { in: segmentIds },
    status: { in: statuses },
    banca: { in: contestBancas(contest) },
  } satisfies Prisma.QuestionWhereInput;
}
