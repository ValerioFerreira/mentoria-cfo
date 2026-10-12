import { db } from "@/lib/db";
import { mpRequest, verifyMercadoPagoSignature } from "@/lib/billing/mercado-pago";
import { mapMercadoPagoDisputeStatus, mapMercadoPagoPaymentStatus } from "@/lib/billing/status";

type Notification = {
  id?: string | number;
  type?: string;
  topic?: string;
  action?: string;
  data?: { id?: string | number; payment_id?: string | number };
};
type MpPayment = {
  id: number | string;
  status: string;
  status_detail?: string;
  transaction_amount: number | string;
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
type MpChargeback = {
  id: string;
  status: string;
  status_detail?: string;
  amount: number | string;
  currency: string;
  payments?: { id: string | number }[];
};
type SyncedPayment = { providerPaymentId: string; status: string; statusDetail: string | null };

function addCalendarMonth(date: Date): Date {
  const next = new Date(date);
  const day = next.getUTCDate();
  next.setUTCDate(1);
  next.setUTCMonth(next.getUTCMonth() + 1);
  const lastDay = new Date(Date.UTC(next.getUTCFullYear(), next.getUTCMonth() + 1, 0)).getUTCDate();
  next.setUTCDate(Math.min(day, lastDay));
  return next;
}

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

async function syncPayment(paymentId: string, preapprovalId?: string): Promise<SyncedPayment> {
  const payment = await mpRequest<MpPayment>(`/v1/payments/${encodeURIComponent(paymentId)}`);
  const purchase = await findPurchase(payment, preapprovalId);
  if (!purchase) throw new Error("Payment does not match a local purchase");
  const expectedAmount = purchase.product === "MONTHLY" ? 30 : 50;
  if (Number(payment.transaction_amount) !== expectedAmount || payment.currency_id !== "BRL") {
    throw new Error("Payment amount or currency does not match the local purchase");
  }
  const status = mapMercadoPagoPaymentStatus(payment.status, payment.status_detail);
  if (!status) throw new Error("Unsupported Mercado Pago payment status");

  let subscription: MpSubscription | null = null;
  if (purchase.product === "MONTHLY" && purchase.mpPreapprovalId && ["APPROVED", "PARTIALLY_REFUNDED", "DISPUTED", "CHARGEBACK_WON"].includes(status)) {
    subscription = await mpRequest<MpSubscription>(`/preapproval/${encodeURIComponent(purchase.mpPreapprovalId)}`);
  }
  const paidAt = payment.date_approved ? new Date(payment.date_approved) : null;
  // An entitlement period is anchored to this confirmed payment. The provider's
  // next_payment_date can move ahead after a later event, so it must not extend
  // an older payment when Mercado Pago retries or reorders notifications.
  const accessUntil = purchase.product === "MONTHLY" && paidAt ? addCalendarMonth(paidAt) : null;

  await db.$transaction(async (tx) => {
    await tx.billingPayment.upsert({
      where: { providerPaymentId: String(payment.id) },
      create: {
        purchaseId: purchase.id,
        providerPaymentId: String(payment.id),
        status,
        amount: Number(payment.transaction_amount),
        currency: payment.currency_id,
        statusDetail: payment.status_detail ?? null,
        paidAt,
        accessUntil,
      },
      update: {
        status,
        statusDetail: payment.status_detail ?? null,
        paidAt: paidAt ?? undefined,
        accessUntil: accessUntil ?? undefined,
      },
    });

    if (purchase.product === "PERMANENT") {
      const statusAfterPayment = status === "REFUNDED" ? "REFUNDED"
        : status === "CHARGEBACK_LOST" ? "CHARGEBACK"
          : ["APPROVED", "PARTIALLY_REFUNDED", "DISPUTED", "CHARGEBACK_WON"].includes(status) ? "ACTIVE"
            : purchase.status;
      if (statusAfterPayment !== purchase.status) {
        await tx.billingPurchase.update({ where: { id: purchase.id }, data: { status: statusAfterPayment } });
      }
    } else if (["APPROVED", "PARTIALLY_REFUNDED", "DISPUTED", "CHARGEBACK_WON"].includes(status)) {
      const cancelled = subscription?.status === "cancelled";
      await tx.billingPurchase.update({
        where: { id: purchase.id },
        data: {
          status: status === "CHARGEBACK_WON" || status === "DISPUTED" ? purchase.status : cancelled ? "CANCELLED" : "ACTIVE",
          currentPeriodEnd: accessUntil ?? purchase.currentPeriodEnd,
        },
      });
    } else if (status === "REJECTED") {
      await tx.billingPurchase.update({ where: { id: purchase.id }, data: { status: "PAST_DUE" } });
    }
  });
  return { providerPaymentId: String(payment.id), status, statusDetail: payment.status_detail ?? null };
}

async function syncSubscription(subscriptionId: string) {
  const subscription = await mpRequest<MpSubscription>(`/preapproval/${encodeURIComponent(subscriptionId)}`);
  const purchase = await db.billingPurchase.findUnique({ where: { mpPreapprovalId: subscription.id } });
  if (!purchase || purchase.product !== "MONTHLY") throw new Error("Subscription does not match a local purchase");
  const hasCurrentPaidPeriod = await db.billingPayment.findFirst({
    where: {
      purchaseId: purchase.id,
      status: { in: ["APPROVED", "PARTIALLY_REFUNDED", "DISPUTED", "CHARGEBACK_WON"] },
      accessUntil: { gt: new Date() },
    },
    select: { id: true },
  });
  const status = subscription.status === "cancelled" ? "CANCELLED"
    : subscription.status === "paused" ? "PAST_DUE"
      : subscription.status === "authorized" && hasCurrentPaidPeriod ? "ACTIVE"
        : subscription.status === "authorized" ? "PAST_DUE" : "PENDING";
  const nextEnd = subscription.auto_recurring?.next_payment_date
    ? new Date(subscription.auto_recurring.next_payment_date)
    : purchase.currentPeriodEnd;
  await db.billingPurchase.update({
    where: { id: purchase.id },
    data: {
      status,
      cancelledAt: status === "CANCELLED" ? purchase.cancelledAt ?? new Date() : purchase.cancelledAt,
      currentPeriodEnd: nextEnd,
    },
  });
  return { status, statusDetail: subscription.status };
}

async function syncChargeback(caseId: string, payloadPaymentId?: string) {
  const sellerId = process.env.MERCADOPAGO_SELLER_ID;
  if (!sellerId) throw new Error("MERCADOPAGO_SELLER_ID is not configured");
  const chargeback = await mpRequest<MpChargeback>(`/v1/chargebacks/${encodeURIComponent(caseId)}`, {
    headers: { "X-Caller-Id": sellerId },
  });
  const paymentIds = chargeback.payments?.map((p) => String(p.id)) ?? [];
  const providerPaymentId = payloadPaymentId ?? (paymentIds.length === 1 ? paymentIds[0] : undefined);
  if (!providerPaymentId || (paymentIds.length > 0 && !paymentIds.includes(providerPaymentId))) {
    throw new Error("Chargeback does not match the signed notification");
  }
  const synced = await syncPayment(providerPaymentId);
  const payment = await db.billingPayment.findUnique({ where: { providerPaymentId }, include: { purchase: true } });
  if (!payment) throw new Error("Chargeback payment is not linked to a local purchase");

  const detail = chargeback.status_detail?.toLowerCase() ?? chargeback.status.toLowerCase();
  const disputeStatus = mapMercadoPagoDisputeStatus(chargeback.status, chargeback.status_detail);
  const paymentStatus = disputeStatus === "LOST" ? "CHARGEBACK_LOST" : disputeStatus === "WON" ? "CHARGEBACK_WON" : "DISPUTED";

  await db.$transaction(async (tx) => {
    await tx.billingDispute.upsert({
      where: { providerChargebackId: String(chargeback.id) },
      create: {
        billingPaymentId: payment.id,
        providerChargebackId: String(chargeback.id),
        status: disputeStatus,
        statusDetail: detail,
        amount: Number(chargeback.amount),
        currency: chargeback.currency,
      },
      update: {
        status: disputeStatus,
        statusDetail: detail,
        amount: Number(chargeback.amount),
        currency: chargeback.currency,
        lastEventAt: new Date(),
      },
    });
    await tx.billingPayment.update({ where: { id: payment.id }, data: { status: paymentStatus, statusDetail: detail } });
    if (disputeStatus === "LOST" && payment.purchase.product === "PERMANENT") {
      await tx.billingPurchase.update({
        where: { id: payment.purchaseId },
        data: { status: "CHARGEBACK" },
      });
    } else if (disputeStatus === "WON" && payment.purchase.product === "PERMANENT" && payment.purchase.status === "CHARGEBACK") {
      await tx.billingPurchase.update({ where: { id: payment.purchaseId }, data: { status: "ACTIVE" } });
    }
  });
  return { status: paymentStatus, statusDetail: detail, providerPaymentId: synced.providerPaymentId };
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
  const resourceId = dataId;
  const topic = notification.type ?? notification.topic ?? "";
  const supported = ["payment", "subscription_preapproval", "subscription_authorized_payment", "topic_chargebacks_wh", "chargebacks"];
  if (!resourceId || !supported.includes(topic)) return Response.json({ received: true });

  const eventKey = `${topic}:${String(notification.id ?? `${resourceId}:${notification.action ?? "update"}`)}`;
  try {
    const event = await db.billingWebhookEvent.upsert({
      where: { eventKey },
      create: { eventKey, resourceId, topic, action: notification.action },
      update: {},
    });
    if (event.processedAt) return Response.json({ received: true });

    let result: { status: string; statusDetail: string | null; providerPaymentId?: string };
    if (topic === "payment") {
      result = await syncPayment(resourceId);
    } else if (topic === "subscription_preapproval") {
      result = await syncSubscription(resourceId);
    } else if (topic === "subscription_authorized_payment") {
      const authorized = await mpRequest<AuthorizedPayment>(`/authorized_payments/${encodeURIComponent(resourceId)}`);
      if (authorized.payment?.id) result = await syncPayment(String(authorized.payment.id), authorized.preapproval_id);
      else if (authorized.preapproval_id) result = await syncSubscription(authorized.preapproval_id);
      else throw new Error("Authorized payment has no linked subscription or payment");
    } else {
      result = await syncChargeback(resourceId, notification.data?.payment_id == null ? undefined : String(notification.data.payment_id));
    }
    await db.billingWebhookEvent.update({
      where: { id: event.id },
      data: { processedAt: new Date(), resultStatus: result.status, resultDetail: result.statusDetail },
    });
    return Response.json({ received: true });
  } catch (error) {
    console.error("[billing-webhook] Event processing failed", {
      topic,
      resourceId,
      error: error instanceof Error ? error.message : "unknown error",
    });
    return Response.json({ error: "event processing failed" }, { status: 500 });
  }
}
