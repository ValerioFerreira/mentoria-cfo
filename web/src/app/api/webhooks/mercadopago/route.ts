import { db } from "@/lib/db";
import { mpRequest, verifyMercadoPagoSignature } from "@/lib/billing/mercado-pago";

type Notification = { id?: string | number; type?: string; topic?: string; action?: string; data?: { id?: string | number } };
type MpPayment = {
  id: number | string;
  status: string;
  status_detail?: string;
  transaction_amount: number;
  currency_id: string;
  external_reference?: string;
  preapproval_id?: string;
  metadata?: { purchase_id?: string };
  date_approved?: string | null;
};
type MpSubscription = {
  id: string;
  status: string;
  external_reference?: string;
  auto_recurring?: { next_payment_date?: string | null; end_date?: string | null };
};
type AuthorizedPayment = { id: string; preapproval_id?: string; payment?: { id?: number | string; status?: string } };

const PAYMENT_STATUS = {
  approved: "APPROVED",
  pending: "PENDING",
  in_process: "PENDING",
  rejected: "REJECTED",
  cancelled: "CANCELLED",
  refunded: "REFUNDED",
  charged_back: "CHARGEBACK",
} as const;

async function findPurchase(payment: MpPayment, preapprovalId?: string) {
  const subscriptionId = payment.preapproval_id ?? preapprovalId;
  if (subscriptionId) {
    const bySubscription = await db.billingPurchase.findUnique({ where: { mpPreapprovalId: subscriptionId } });
    if (bySubscription) return bySubscription;
  }
  if (payment.metadata?.purchase_id) {
    const byMetadata = await db.billingPurchase.findUnique({ where: { id: payment.metadata.purchase_id } });
    if (byMetadata) return byMetadata;
  }
  if (payment.external_reference) {
    return db.billingPurchase.findUnique({ where: { externalReference: payment.external_reference } });
  }
  return null;
}

async function syncPayment(paymentId: string, preapprovalId?: string) {
  const payment = await mpRequest<MpPayment>(`/v1/payments/${encodeURIComponent(paymentId)}`);
  const purchase = await findPurchase(payment, preapprovalId);
  if (!purchase) throw new Error("Payment does not match a local purchase");
  const expectedAmount = purchase.product === "MONTHLY" ? 30 : 50;
  if (Number(payment.transaction_amount) !== expectedAmount || payment.currency_id !== "BRL") {
    throw new Error("Payment amount or currency does not match the local purchase");
  }
  const status = PAYMENT_STATUS[payment.status as keyof typeof PAYMENT_STATUS];
  if (!status) throw new Error("Unsupported Mercado Pago payment status");

  await db.$transaction(async (tx) => {
    await tx.billingPayment.upsert({
      where: { providerPaymentId: String(payment.id) },
      create: {
        purchaseId: purchase.id,
        providerPaymentId: String(payment.id),
        status,
        amount: payment.transaction_amount,
        currency: payment.currency_id,
        statusDetail: payment.status_detail,
        paidAt: status === "APPROVED" && payment.date_approved ? new Date(payment.date_approved) : null,
      },
      update: {
        status,
        statusDetail: payment.status_detail,
        paidAt: status === "APPROVED" && payment.date_approved ? new Date(payment.date_approved) : null,
      },
    });

    if (purchase.product === "PERMANENT") {
      const permanentStatus = status === "APPROVED" ? "ACTIVE" : status === "REFUNDED" ? "REFUNDED" : status === "CHARGEBACK" ? "CHARGEBACK" : purchase.status;
      if (permanentStatus !== purchase.status) await tx.billingPurchase.update({ where: { id: purchase.id }, data: { status: permanentStatus } });
    } else if (status === "APPROVED") {
      const next = purchase.mpPreapprovalId
        ? await mpRequest<MpSubscription>(`/preapproval/${encodeURIComponent(purchase.mpPreapprovalId)}`)
        : null;
      const isCancelled = next?.status === "cancelled" || next?.status === "paused";
      await tx.billingPurchase.update({
        where: { id: purchase.id },
        data: {
          status: isCancelled ? "CANCELLED" : "ACTIVE",
          currentPeriodEnd: next?.auto_recurring?.next_payment_date ? new Date(next.auto_recurring.next_payment_date) : purchase.currentPeriodEnd,
        },
      });
    } else if (status === "REFUNDED" || status === "CHARGEBACK") {
      await tx.billingPurchase.update({ where: { id: purchase.id }, data: { status } });
    } else if (status === "REJECTED") {
      await tx.billingPurchase.update({ where: { id: purchase.id }, data: { status: "PAST_DUE" } });
    }
  });
}

async function syncSubscription(subscriptionId: string) {
  const subscription = await mpRequest<MpSubscription>(`/preapproval/${encodeURIComponent(subscriptionId)}`);
  const purchase = await db.billingPurchase.findUnique({ where: { mpPreapprovalId: subscription.id } });
  if (!purchase || purchase.product !== "MONTHLY") throw new Error("Subscription does not match a local purchase");
  const hasApprovedPayment = await db.billingPayment.findFirst({ where: { purchaseId: purchase.id, status: "APPROVED" }, select: { id: true } });
  const status = subscription.status === "cancelled" ? "CANCELLED"
    : subscription.status === "paused" ? "PAST_DUE"
      : subscription.status === "authorized" && hasApprovedPayment ? "ACTIVE"
        : "PENDING";
  await db.billingPurchase.update({
    where: { id: purchase.id },
    data: {
      status,
      cancelledAt: status === "CANCELLED" ? purchase.cancelledAt ?? new Date() : purchase.cancelledAt,
      currentPeriodEnd: subscription.auto_recurring?.next_payment_date
        ? new Date(subscription.auto_recurring.next_payment_date)
        : purchase.currentPeriodEnd,
    },
  });
}

export async function POST(request: Request) {
  const url = new URL(request.url);
  const dataId = url.searchParams.get("data.id") ?? url.searchParams.get("id");
  if (!verifyMercadoPagoSignature({
    signature: request.headers.get("x-signature"),
    requestId: request.headers.get("x-request-id"),
    dataId,
  })) return Response.json({ error: "invalid signature" }, { status: 401 });

  let notification: Notification;
  try {
    notification = await request.json() as Notification;
  } catch {
    return Response.json({ error: "invalid payload" }, { status: 400 });
  }
  const bodyDataId = notification.data?.id == null ? null : String(notification.data.id);
  if (!dataId || (bodyDataId && bodyDataId.toLowerCase() !== dataId.toLowerCase())) {
    return Response.json({ error: "resource id mismatch" }, { status: 400 });
  }
  const id = dataId;
  const topic = notification.type ?? notification.topic ?? "";
  if (!id || !["payment", "subscription_preapproval", "subscription_authorized_payment"].includes(topic)) {
    return Response.json({ received: true });
  }

  const eventKey = `${topic}:${String(notification.id ?? `${id}:${notification.action ?? "update"}`)}`;
  try {
    const event = await db.billingWebhookEvent.upsert({
      where: { eventKey },
      create: { eventKey, resourceId: id, topic, action: notification.action },
      update: {},
    });
    if (event.processedAt) return Response.json({ received: true });

    if (topic === "payment") {
      await syncPayment(id);
    } else if (topic === "subscription_preapproval") {
      await syncSubscription(id);
    } else {
      const authorized = await mpRequest<AuthorizedPayment>(`/authorized_payments/${encodeURIComponent(id)}`);
      if (authorized.payment?.id) await syncPayment(String(authorized.payment.id), authorized.preapproval_id);
      else if (authorized.preapproval_id) await syncSubscription(authorized.preapproval_id);
      else throw new Error("Authorized payment has no linked subscription or payment");
    }
    await db.billingWebhookEvent.update({ where: { id: event.id }, data: { processedAt: new Date() } });
    return Response.json({ received: true });
  } catch (error) {
    console.error("[billing-webhook] Event processing failed", {
      topic,
      resourceId: id,
      error: error instanceof Error ? error.message : "unknown error",
    });
    return Response.json({ error: "event processing failed" }, { status: 500 });
  }
}
