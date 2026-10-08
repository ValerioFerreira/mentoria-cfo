/** Status de questão que podem ser servidas aos alunos. Em desenvolvimento, SERVE_DRAFT_QUESTIONS=true libera rascunhos. */
export function servableStatuses(): ("APPROVED" | "DRAFT")[] {
  return process.env.SERVE_DRAFT_QUESTIONS === "true" ? ["APPROVED", "DRAFT"] : ["APPROVED"];
}
