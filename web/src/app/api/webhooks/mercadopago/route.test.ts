import { beforeEach, describe, expect, it, vi } from "vitest";

const mocks = vi.hoisted(() => ({
  signatureValid: true,
  payment: {
    id: "182791299055",
    status: "approved",
    status_detail: "accredited",
    transaction_amount: 50,
    currency_id: "BRL",
    external_reference: "purchase-reference",
    metadata: { purchase_id: "purchase-1" },
    date_approved: "2026-10-12T19:39:48.000Z",
  } as Record<string, unknown>,
  event: { id: "event-1", processedAt: null } as { id: string; processedAt: Date | null },
  db: {
    billingWebhookEvent: { upsert: vi.fn(), update: vi.fn() },
    billingPurchase: { findUnique: vi.fn(), update: vi.fn() },
    billingPayment: { upsert: vi.fn() },
    billingDispute: { upsert: vi.fn() },
    manualPayment: { findUnique: vi.fn() },
    $transaction: vi.fn(),
  },
  mpRequest: vi.fn(),
}));

vi.mock("@/lib/db", () => ({ db: mocks.db }));
// pagamentos de contratações têm teste próprio (lib/commerce/online.integration.test.ts); aqui vale o fluxo antigo
vi.mock("@/lib/commerce/online", () => ({ syncContractPayment: vi.fn().mockResolvedValue(null) }));
vi.mock("@/lib/billing/mercado-pago", () => ({
  mpRequest: mocks.mpRequest,
  verifyMercadoPagoSignature: () => mocks.signatureValid,
}));

import { POST } from "./route";

const purchase = {
  id: "purchase-1",
  product: "PERMANENT",
  amount: 50,
  status: "PENDING",
  currentPeriodEnd: null,
  mpPreapprovalId: null,
};

function request() {
  const url = new URL("https://missaomentoria.com.br/api/webhooks/mercadopago?data.id=182791299055");
  return new Request(url, {
    method: "POST",
    headers: { "content-type": "application/json", "x-signature": "test", "x-request-id": "request-1" },
    body: JSON.stringify({
      id: "notification-1",
      type: "payment",
      action: "payment.created",
      data: { id: "182791299055" },
    }),
  });
}

function configureSuccessfulPersistence() {
  const tx = {
    billingPayment: { upsert: mocks.db.billingPayment.upsert },
    billingPurchase: { update: mocks.db.billingPurchase.update },
  };
  mocks.db.$transaction.mockImplementation(async (callback: (tx: unknown) => Promise<void>) => callback(tx as never));
}

describe("Mercado Pago payment webhook", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.signatureValid = true;
    mocks.payment = {
      id: "182791299055",
      status: "approved",
      status_detail: "accredited",
      transaction_amount: 50,
      currency_id: "BRL",
      external_reference: "purchase-reference",
      metadata: { purchase_id: "purchase-1" },
      date_approved: "2026-10-12T19:39:48.000Z",
    };
    mocks.event = { id: "event-1", processedAt: null };
    mocks.db.billingWebhookEvent.upsert.mockResolvedValue(mocks.event);
    mocks.db.billingWebhookEvent.update.mockResolvedValue({});
    mocks.db.billingPurchase.findUnique.mockResolvedValue(purchase);
    mocks.db.billingPayment.upsert.mockResolvedValue({ id: "payment-row-1" });
    mocks.db.billingPurchase.update.mockResolvedValue({});
    mocks.mpRequest.mockImplementation(async (path: string) => {
      if (path !== "/v1/payments/182791299055") throw new Error(`Unexpected path: ${path}`);
      return mocks.payment;
    });
    configureSuccessfulPersistence();
  });

  it("fetches the signed data.id from Mercado Pago and grants only its approved matching purchase", async () => {
    const response = await POST(request());

    expect(response.status).toBe(200);
    expect(mocks.mpRequest).toHaveBeenCalledWith("/v1/payments/182791299055");
    expect(mocks.db.billingPayment.upsert).toHaveBeenCalledWith(expect.objectContaining({
      where: { providerPaymentId: "182791299055" },
      create: expect.objectContaining({ status: "APPROVED", amount: 50, currency: "BRL" }),
    }));
    expect(mocks.db.billingPurchase.update).toHaveBeenCalledWith(expect.objectContaining({
      where: { id: "purchase-1" },
      data: { status: "ACTIVE" },
    }));
    expect(mocks.db.billingWebhookEvent.update).toHaveBeenCalledWith(expect.objectContaining({
      where: { id: "event-1" },
      data: expect.objectContaining({ resultStatus: "APPROVED", processedAt: expect.any(Date) }),
    }));
  });

  it("rejects an invalid signature before querying Mercado Pago or writing records", async () => {
    mocks.signatureValid = false;

    const response = await POST(request());

    expect(response.status).toBe(401);
    expect(mocks.mpRequest).not.toHaveBeenCalled();
    expect(mocks.db.billingWebhookEvent.upsert).not.toHaveBeenCalled();
  });

  it.each([
    ["pending", "PENDING"],
    ["in_process", "PENDING"],
    ["rejected", "REJECTED"],
  ])("persists %s without activating permanent access", async (providerStatus, expectedStatus) => {
    mocks.payment.status = providerStatus;
    mocks.payment.date_approved = null;

    const response = await POST(request());

    expect(response.status).toBe(200);
    expect(mocks.db.billingPayment.upsert).toHaveBeenCalledWith(expect.objectContaining({
      create: expect.objectContaining({ status: expectedStatus }),
    }));
    expect(mocks.db.billingPurchase.update).not.toHaveBeenCalled();
  });

  it("acknowledges an already processed duplicate without querying or writing again", async () => {
    mocks.event.processedAt = new Date();

    const response = await POST(request());

    expect(response.status).toBe(200);
    expect(mocks.mpRequest).not.toHaveBeenCalled();
    expect(mocks.db.$transaction).not.toHaveBeenCalled();
  });

  it("returns a retryable error and leaves the event unprocessed when the provider API fails", async () => {
    mocks.mpRequest.mockRejectedValue(new Error("temporary provider failure"));

    const response = await POST(request());

    expect(response.status).toBe(500);
    expect(mocks.db.billingWebhookEvent.update).not.toHaveBeenCalled();
  });

  it("returns a retryable error on persistence failure, then processes the retry", async () => {
    mocks.db.$transaction
      .mockRejectedValueOnce(new Error("temporary database failure"))
      .mockImplementationOnce(async (callback: (tx: unknown) => Promise<void>) => {
        const tx = {
          billingPayment: { upsert: mocks.db.billingPayment.upsert },
          billingPurchase: { update: mocks.db.billingPurchase.update },
        };
        await callback(tx as never);
      });

    const failedResponse = await POST(request());
    expect(failedResponse.status).toBe(500);
    expect(mocks.db.billingWebhookEvent.update).not.toHaveBeenCalled();

    const retryResponse = await POST(request());
    expect(retryResponse.status).toBe(200);
    expect(mocks.db.billingWebhookEvent.update).toHaveBeenCalledTimes(1);
  });

  it("fails closed when the authoritative payment amount does not match the local purchase", async () => {
    mocks.payment.transaction_amount = 49;

    const response = await POST(request());

    expect(response.status).toBe(500);
    expect(mocks.db.$transaction).not.toHaveBeenCalled();
    expect(mocks.db.billingWebhookEvent.update).not.toHaveBeenCalled();
  });
});
