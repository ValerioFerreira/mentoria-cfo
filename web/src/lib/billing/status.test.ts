import { describe, expect, it } from "vitest";
import { mapMercadoPagoDisputeStatus, mapMercadoPagoPaymentStatus } from "./status";

describe("Mercado Pago financial state mapping", () => {
  it("records partial and full refunds distinctly", () => {
    expect(mapMercadoPagoPaymentStatus("approved", "partially_refunded")).toBe("PARTIALLY_REFUNDED");
    expect(mapMercadoPagoPaymentStatus("refunded", "refunded")).toBe("REFUNDED");
  });

  it("keeps a dispute pending until a provider outcome is final", () => {
    expect(mapMercadoPagoDisputeStatus("charged_back", "in_process")).toBe("IN_PROGRESS");
    expect(mapMercadoPagoPaymentStatus("charged_back", "in_process")).toBe("DISPUTED");
  });

  it("maps settled to a favorable outcome and reimbursed to a loss", () => {
    expect(mapMercadoPagoDisputeStatus("charged_back", "settled")).toBe("WON");
    expect(mapMercadoPagoPaymentStatus("charged_back", "settled")).toBe("CHARGEBACK_WON");
    expect(mapMercadoPagoDisputeStatus("charged_back", "reimbursed")).toBe("LOST");
    expect(mapMercadoPagoPaymentStatus("charged_back", "reimbursed")).toBe("CHARGEBACK_LOST");
  });

  it("fails closed on unrecognized payment states and treats an unknown case result as pending", () => {
    expect(mapMercadoPagoPaymentStatus("some_new_state")).toBeNull();
    expect(mapMercadoPagoDisputeStatus("some_new_state")).toBe("IN_PROGRESS");
  });
});
