/** Erro de regra de negócio com mensagem segura para mostrar ao usuário/administrador. */
export class CommerceError extends Error {
  constructor(message: string, readonly code = "INVALID") {
    super(message);
    this.name = "CommerceError";
  }
}

export type ActionResult<T = undefined> = { ok: true; message: string; data?: T } | { ok: false; message: string };

/** Converte exceções esperadas em resposta; as inesperadas são registradas sem dados sensíveis. */
export function toActionError(err: unknown, context: string): { ok: false; message: string } {
  if (err instanceof CommerceError) return { ok: false, message: err.message };
  if (err && typeof err === "object" && "name" in err && err.name === "PricingError" && "message" in err) {
    return { ok: false, message: String(err.message) };
  }
  console.error(`[commerce] ${context} falhou`, err instanceof Error ? err.message : "erro desconhecido");
  return { ok: false, message: "Não foi possível concluir a operação. Tente novamente." };
}
