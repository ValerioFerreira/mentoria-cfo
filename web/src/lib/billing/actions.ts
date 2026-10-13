"use server";

import { redirect } from "next/navigation";
import { getCurrentUser } from "@/lib/auth/session";
import { db } from "@/lib/db";
import { mpRequest } from "./mercado-pago";

// Novas adesões (mensal e checkout do Mercado Pago) foram descontinuadas: a contratação agora é o acesso
// ilimitado até a prova, com Pix conferido e lançado pela administração (lib/commerce). Fica só o cancelamento
// de assinaturas mensais antigas, para que nenhuma cobrança recorrente continue.

export async function cancelMonthlySubscription(formData: FormData): Promise<void> {
  const user = await getCurrentUser();
  if (!user) redirect("/login");
  const purchaseId = formData.get("purchaseId");
  if (typeof purchaseId !== "string") redirect("/pagamentos");
  const purchase = await db.billingPurchase.findFirst({
    where: { id: purchaseId, userId: user.id, product: "MONTHLY", mpPreapprovalId: { not: null }, status: { in: ["ACTIVE", "PENDING", "PAST_DUE"] } },
  });
  if (!purchase?.mpPreapprovalId) redirect("/pagamentos");
  const result = await mpRequest<{ status: string }>(`/preapproval/${encodeURIComponent(purchase.mpPreapprovalId)}`, {
    method: "PUT",
    body: JSON.stringify({ status: "cancelled" }),
  });
  if (result.status !== "cancelled") redirect("/pagamentos?erro=cancelamento");
  await db.billingPurchase.update({ where: { id: purchase.id }, data: { status: "CANCELLED", cancelledAt: new Date() } });
  redirect("/pagamentos?status=cancelada");
}
