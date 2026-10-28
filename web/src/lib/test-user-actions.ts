"use server";

import { randomUUID } from "node:crypto";
import { cookies } from "next/headers";
import { redirect } from "next/navigation";
import { getCurrentUser } from "@/lib/auth/session";
import { grantAccessUntilExam } from "@/lib/commerce/contracts";
import { CommerceError, toActionError } from "@/lib/commerce/errors";
import { toCents } from "@/lib/commerce/money";
import { registerPayment } from "@/lib/commerce/payments";
import { db } from "@/lib/db";
import { isTestUser } from "@/lib/test-user";
import { CONTEST_COOKIE } from "@/lib/user-contest";

async function requireTestUser() {
  const user = await getCurrentUser();
  if (!user) redirect("/login");
  if (!isTestUser(user.email)) throw new CommerceError("Ferramenta disponível só para o usuário de teste local.");
  return user;
}

/** Apaga tudo o que o usuário de teste escolheu e gerou (planos, contratações, pagamentos, cadernos…) e volta ao início. */
export async function resetTestUser(): Promise<void> {
  const user = await requireTestUser();
  const email = user.email.toLowerCase();
  await db.$transaction(
    async (tx) => {
      const contracts = await tx.contract.findMany({ where: { OR: [{ userId: user.id }, { customerEmail: email }] }, select: { id: true } });
      const ids = contracts.map((c) => c.id);
      if (ids.length) {
        await tx.commissionEntry.deleteMany({ where: { contractId: { in: ids } } });
        await tx.partnerReferral.deleteMany({ where: { firstContractId: { in: ids } } });
        await tx.paymentReversal.deleteMany({ where: { contractId: { in: ids } } });
        await tx.onlineCharge.deleteMany({ where: { contractId: { in: ids } } });
        await tx.manualPayment.deleteMany({ where: { contractId: { in: ids } } });
        await tx.contract.deleteMany({ where: { id: { in: ids } } });
      }
      await tx.waitlistEntry.deleteMany({ where: { email } });
      await tx.plan.deleteMany({ where: { userId: user.id } });
      await tx.quizSession.deleteMany({ where: { userId: user.id } });
      await tx.timeLog.deleteMany({ where: { userId: user.id } });
      await tx.note.deleteMany({ where: { userId: user.id } });
      await tx.bizuAnswer.deleteMany({ where: { userId: user.id } });
      await tx.questionReport.deleteMany({ where: { userId: user.id } });
      await tx.billingPurchase.deleteMany({ where: { userId: user.id } });
      await tx.profile.deleteMany({ where: { userId: user.id } });
      await tx.user.update({ where: { id: user.id }, data: { accessExpiresAt: null } });
    },
    { timeout: 60_000 },
  );
  (await cookies()).delete(CONTEST_COOKIE);
  redirect("/");
}

/** "Confirmar pagamento" de teste: lança o saldo como recebido e libera o acesso até a prova, como a confirmação real faria. */
export async function confirmTestPayment(contractId: string): Promise<void> {
  const user = await requireTestUser();
  const c = await db.contract.findFirst({ where: { id: contractId, OR: [{ userId: user.id }, { customerEmail: user.email.toLowerCase() }] } });
  if (!c) throw new CommerceError("Contratação não encontrada.");
  const due = toCents(c.finalAmount) - toCents(c.paidAmount);
  try {
    if (due > 0) {
      await registerPayment({ contractId: c.id, amountCents: due, paidAt: new Date(), method: "OUTRO", note: "Pagamento de teste (usuário local)", idempotencyKey: `teste-${randomUUID()}` }, user.id);
    }
    await grantAccessUntilExam(c.id, user.id);
  } catch (err) {
    const r = toActionError(err, "pagamento de teste");
    throw new Error(r.message);
  }
  redirect(`/pagamentos/contratacao/${encodeURIComponent(c.id)}`);
}
