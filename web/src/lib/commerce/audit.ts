import "server-only";
import type { Prisma } from "@/generated/prisma/client";

type Tx = Prisma.TransactionClient;

/** Registra uma alteração administrativa/financeira. Nunca incluir senhas, tokens ou dados de pagamento sensíveis. */
export async function audit(
  tx: Tx,
  entry: { actorId: string | null; action: string; entityType: string; entityId: string; data?: Prisma.InputJsonValue },
): Promise<void> {
  await tx.auditLog.create({ data: entry });
}
