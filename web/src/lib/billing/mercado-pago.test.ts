import { createHmac } from "node:crypto";
import { afterEach, describe, expect, it, vi } from "vitest";

vi.mock("server-only", () => ({}));

import { mercadoPagoToken, verifyMercadoPagoSignature } from "./mercado-pago";

describe("Mercado Pago webhook signature", () => {
  const previous = process.env.MERCADOPAGO_WEBHOOK_SECRET;
  const previousToken = process.env.MERCADOPAGO_ACCESS_TOKEN;
  const previousLegacyToken = process.env.MERCADO_PAGO_ACCESS_TOKEN;

  afterEach(() => {
    if (previous === undefined) delete process.env.MERCADOPAGO_WEBHOOK_SECRET;
    else process.env.MERCADOPAGO_WEBHOOK_SECRET = previous;
    if (previousToken === undefined) delete process.env.MERCADOPAGO_ACCESS_TOKEN;
    else process.env.MERCADOPAGO_ACCESS_TOKEN = previousToken;
    if (previousLegacyToken === undefined) delete process.env.MERCADO_PAGO_ACCESS_TOKEN;
    else process.env.MERCADO_PAGO_ACCESS_TOKEN = previousLegacyToken;
  });

  it("accepts a valid HMAC manifest", () => {
    const secret = "unit-test-secret";
    process.env.MERCADOPAGO_WEBHOOK_SECRET = secret;
    const manifest = "id:987654321;request-id:request-123;ts:1700000000;";
    const signature = createHmac("sha256", secret).update(manifest).digest("hex");
    expect(verifyMercadoPagoSignature({
      signature: `ts=1700000000,v1=${signature}`,
      requestId: "request-123",
      dataId: "987654321",
    })).toBe(true);
  });

  it("rejects missing headers, missing secret, and a changed resource id", () => {
    process.env.MERCADOPAGO_WEBHOOK_SECRET = "unit-test-secret";
    expect(verifyMercadoPagoSignature({ signature: null, requestId: "r", dataId: "1" })).toBe(false);
    const manifest = "id:1;request-id:r;ts:1;";
    const signature = createHmac("sha256", "unit-test-secret").update(manifest).digest("hex");
    expect(verifyMercadoPagoSignature({ signature: `ts=1,v1=${signature}`, requestId: "r", dataId: "2" })).toBe(false);
    delete process.env.MERCADOPAGO_WEBHOOK_SECRET;
    expect(verifyMercadoPagoSignature({ signature: `ts=1,v1=${signature}`, requestId: "r", dataId: "1" })).toBe(false);
  });

  it("accepts the Mercado Pago token variable already configured in Vercel", () => {
    delete process.env.MERCADOPAGO_ACCESS_TOKEN;
    process.env.MERCADO_PAGO_ACCESS_TOKEN = "test-token";
    expect(mercadoPagoToken()).toBe("test-token");
  });
});
