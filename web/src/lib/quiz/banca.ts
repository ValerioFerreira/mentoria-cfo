import type { Contest, Prisma, QuestionStatus } from "@/generated/prisma/client";
import { comboMembers } from "@/lib/combos";

// Banca dos concursos atendidos. Planejamento (caderno das atividades) e simulados usam só questões dela;
// o banco de questões livre (treino e caderno personalizado) continua aceitando as demais bancas.
export const AOCP_BANCAS = ["AOCP", "Instituto AOCP", "INSTITUTO AOCP"];
// Questões inéditas do MentorIA (padrão Cebraspe), escritas para assuntos do edital do PCPE sem questão real ainda.
// Marcadas no banco com esta banca (e batch "mentoria-inedita-*"); só os alunos do PCPE as recebem.
export const INEDITA_BANCA = "Inédita MentorIA";
export const CEBRASPE_BANCAS = ["CEBRASPE", "Cebraspe", "CESPE", "Cespe / UnB", "CESPE / CEBRASPE", "Cespe", "CEBRASPE (CESPE)"];

export function contestBancas(contest?: Contest | null): string[] {
  // combos: só CBMPE/PMPE (AOCP) por enquanto
  if (contest === "PCPE_AGENTE") {
    // Provisório (decisão do dono em 2026-10-19): enquanto os cadernos Cebraspe não são importados, o PCPE também
    // recebe as questões AOCP que cobrem os assuntos do seu edital. Depois, volta a ser só CEBRASPE_BANCAS.
    return [...CEBRASPE_BANCAS, ...AOCP_BANCAS, INEDITA_BANCA];
  }
  return AOCP_BANCAS;
}

/** Filtro Prisma que esconde as questões inéditas dos alunos de outros concursos (treino livre e cadernos montados). */
export function hideInedita(contest?: Contest | null): { NOT?: { banca: string } } {
  return contest === "PCPE_AGENTE" ? {} : { NOT: { banca: INEDITA_BANCA } };
}

/**
 * Concursos cujo caderno das atividades pode recorrer a REFORÇO quando a banca do concurso não tem questões bastantes:
 * questões de múltipla escolha de outras bancas (já aprovadas no banco) e as inéditas MentorIA, nessa ordem de preferência
 * depois das questões da própria banca. Decisão do dono (2026-10-21) para o CBMPE Oficial; para estender a outro concurso,
 * acrescente-o aqui. Planos antigos sem concurso (null) valem como CBMPE Oficial.
 */
export const REFORCO_CONTESTS: Contest[] = ["CBMPE_OFICIAL"];
export function usesReinforcement(contest?: Contest | null): boolean {
  // no combo, vale se algum dos concursos-membro usa o reforço (o combo CBMPE usa; o PMPE não)
  return comboMembers(contest ?? "CBMPE_OFICIAL").some((m) => REFORCO_CONTESTS.includes(m));
}

/** Filtro das questões de reforço (outras bancas em múltipla escolha, mais as inéditas) para os trechos dados. */
export function reinforcementQuizWhere(segmentIds: string[], statuses: QuestionStatus[]) {
  return {
    segmentId: { in: segmentIds },
    status: { in: statuses },
    kind: "MULTIPLA_ESCOLHA",
    banca: { notIn: AOCP_BANCAS },
  } satisfies Prisma.QuestionWhereInput;
}

/** Filtro das questões do caderno de uma atividade do plano: só os trechos estudados, banca do concurso. */
export function activityQuizWhere(segmentIds: string[], statuses: QuestionStatus[], contest?: Contest | null) {
  return {
    segmentId: { in: segmentIds },
    status: { in: statuses },
    banca: { in: contestBancas(contest) },
  } satisfies Prisma.QuestionWhereInput;
}
