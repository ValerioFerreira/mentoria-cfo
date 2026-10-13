"use server";

import { redirect } from "next/navigation";
import * as z from "zod";
import { getCurrentUser } from "@/lib/auth/session";
import { CONTESTS } from "@/lib/contests";
import { createContract } from "./contracts";
import { cancelPendingCharges } from "./online";
import { type ActionResult, toActionError } from "./errors";

const Schema = z.object({
  contest: z.enum(CONTESTS.map((c) => c.key) as [string, ...string[]], { error: "Escolha o concurso." }),
  coupon: z.string().trim().max(20).optional(),
});

/**
 * Contratação de acesso até a prova por um usuário logado. Só concurso e cupom vêm do formulário: o preço,
 * os descontos e o cliente (a sessão) são definidos no servidor.
 */
export async function startContract(_: ActionResult | null, fd: FormData): Promise<ActionResult> {
  const user = await getCurrentUser();
  if (!user) redirect("/login");
  const parsed = Schema.safeParse(Object.fromEntries(fd));
  if (!parsed.success) return { ok: false, message: parsed.error.issues[0]?.message ?? "Dados inválidos." };
  let contractId: string;
  try {
    const r = await createContract(
      { contest: parsed.data.contest as (typeof CONTESTS)[number]["key"], customerEmail: user.email, customerName: user.name, userId: user.id, couponCode: parsed.data.coupon },
      user.id,
    );
    contractId = r.contractId;
    if (r.replacedId) await cancelPendingCharges(r.replacedId);
  } catch (err) {
    return toActionError(err, "contratação do cliente");
  }
  redirect(`/pagamentos/contratacao/${encodeURIComponent(contractId)}`);
}
