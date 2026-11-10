/**
 * Concursos cujos planos NÃO nascem liberados para ninguém além do administrador: ficam "em análise" (o aluno vê a mensagem
 * "Seu planejamento está em análise, em até 24h estará disponível na plataforma") até o dono revisar e liberar em Cadastros
 * (ou por `scripts/verify-plans.ts --apply`). Tirar um concurso daqui o devolve ao fluxo normal.
 */
export const CONTESTS_HELD_FOR_REVIEW: readonly string[] = ["PCPE_AGENTE", "CBMPE_CFOA"];

interface Args {
  role?: string | null;
  partnerActive?: boolean | null;
  contest?: string | null;
  /** status pedido explicitamente por quem chama (ex.: refazer plano já liberado) */
  explicit?: "ACTIVE" | "PENDING_ANALYSIS";
}

/** Status inicial de um plano recém-gerado. */
export function initialPlanStatus({ role, partnerActive, contest, explicit }: Args): "ACTIVE" | "PENDING_ANALYSIS" {
  if (explicit) return explicit;
  if (role === "ADMIN") return "ACTIVE";
  if (contest && CONTESTS_HELD_FOR_REVIEW.includes(contest)) return "PENDING_ANALYSIS";
  return partnerActive ? "ACTIVE" : "PENDING_ANALYSIS";
}
