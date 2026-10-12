"use server";

import { redirect } from "next/navigation";
import { getCurrentUser } from "@/lib/auth/session";
import { db } from "@/lib/db";
import { mpRequest, siteUrl } from "./mercado-pago";

type Product = "MONTHLY" | "PERMANENT";
type CheckoutResponse = { id: string; init_point: string };
type SubscriptionResponse = { id: string; init_point: string; status: string };

const PRODUCT_INFO: Record<Product, { amount: number; title: string; reason: string }> = {
  MONTHLY: { amount: 30, title: "Acesso mensal à Missão Mentoria", reason: "Acesso mensal à Missão Mentoria" },
  PERMANENT: { amount: 50, title: "Acesso permanente à Missão Mentoria", reason: "Acesso permanente à Missão Mentoria" },
};

export async function startBillingCheckout(formData: FormData): Promise<void> {
  const user = await getCurrentUser();
  if (!user) redirect("/login");
  const product = formData.get("product");
  if (product !== "MONTHLY" && product !== "PERMANENT") redirect("/pagamentos?erro=plano");

  const existingPermanent = await db.billingPurchase.findFirst({
    where: { userId: user.id, product: "PERMANENT", status: { in: ["ACTIVE", "PENDING"] } },
    orderBy: { createdAt: "desc" },
  });
  if (product === "PERMANENT" && existingPermanent?.status === "ACTIVE") redirect("/pagamentos?status=permanente");
  if (product === "PERMANENT" && existingPermanent?.checkoutUrl) redirect(existingPermanent.checkoutUrl);

  const existingMonthly = await db.billingPurchase.findFirst({
    where: { userId: user.id, product: "MONTHLY", status: { in: ["ACTIVE", "PENDING", "PAST_DUE"] } },
    orderBy: { createdAt: "desc" },
  });
  if (product === "MONTHLY" && existingMonthly?.checkoutUrl) redirect(existingMonthly.checkoutUrl);

  const purchase = await db.billingPurchase.create({
    data: { userId: user.id, product, amount: PRODUCT_INFO[product].amount },
  });
  const base = siteUrl();
  const callback = new URL("/pagamentos/retorno", base).toString();
  const notificationUrl = new URL("/api/webhooks/mercadopago", base).toString();

  try {
    if (product === "MONTHLY") {
      const response = await mpRequest<SubscriptionResponse>("/preapproval", {
        method: "POST",
        headers: { "X-Idempotency-Key": purchase.id },
        body: JSON.stringify({
          reason: PRODUCT_INFO.MONTHLY.reason,
          external_reference: purchase.externalReference,
          payer_email: user.email,
          auto_recurring: {
            frequency: 1,
            frequency_type: "months",
            transaction_amount: PRODUCT_INFO.MONTHLY.amount,
            currency_id: "BRL",
          },
          back_url: callback,
          notification_url: notificationUrl,
          status: "pending",
        }),
      });
      if (!response.init_point || !response.id) throw new Error("Invalid Mercado Pago subscription response");
      await db.billingPurchase.update({
        where: { id: purchase.id },
        data: { mpPreapprovalId: response.id, checkoutUrl: response.init_point },
      });
      redirect(response.init_point);
    }

    const response = await mpRequest<CheckoutResponse>("/checkout/preferences", {
      method: "POST",
      headers: { "X-Idempotency-Key": purchase.id },
      body: JSON.stringify({
        items: [{ id: purchase.id, title: PRODUCT_INFO.PERMANENT.title, quantity: 1, currency_id: "BRL", unit_price: PRODUCT_INFO.PERMANENT.amount }],
        payer: { email: user.email },
        external_reference: purchase.externalReference,
        metadata: { purchase_id: purchase.id },
        notification_url: notificationUrl,
        back_urls: { success: callback, pending: callback, failure: callback },
        auto_return: "approved",
      }),
    });
    if (!response.init_point || !response.id) throw new Error("Invalid Mercado Pago preference response");
    await db.billingPurchase.update({
      where: { id: purchase.id },
      data: { mpPreferenceId: response.id, checkoutUrl: response.init_point },
    });
    redirect(response.init_point);
  } catch (error) {
    // Next redirect throws internally; preserve it and avoid recording a redirect as a failure.
    if (error && typeof error === "object" && "digest" in error) throw error;
    await db.billingPurchase.update({ where: { id: purchase.id }, data: { status: "CANCELLED" } });
    console.error("[billing] Checkout could not be created", { product, status: error instanceof Error && "status" in error ? error.status : undefined });
    redirect("/pagamentos?erro=checkout");
  }
}

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
