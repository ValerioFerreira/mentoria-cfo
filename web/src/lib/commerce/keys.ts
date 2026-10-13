import "server-only";
import { randomUUID } from "node:crypto";

/**
 * Chave de idempotência gerada no servidor ao renderizar um formulário financeiro: reenviar o mesmo formulário
 * (duplo clique, nova tentativa) reaproveita a chave e não duplica o lançamento; após o sucesso a página é
 * revalidada e o próximo formulário recebe outra chave.
 */
export function newIdempotencyKey(): string {
  return randomUUID();
}
