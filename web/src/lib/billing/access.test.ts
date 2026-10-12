import { describe, expect, it, vi } from "vitest";

vi.mock("server-only", () => ({}));

import { grantsBillingAccess, type BillingEntitlementSnapshot } from "./access";

const now = new Date("2026-10-12T12:00:00.000Z");
const future = new Date("2026-11-12T12:00:00.000Z");
const past = new Date("2026-10-11T12:00:00.000Z");

function purchase(
  product: BillingEntitlementSnapshot["product"],
  status: BillingEntitlementSnapshot["status"],
  paymentStatuses: BillingEntitlementSnapshot["payments"][number]["status"][],
  accessUntil: Date | null = null,
): BillingEntitlementSnapshot {
  return { product, status, payments: paymentStatuses.map((paymentStatus) => ({ status: paymentStatus, accessUntil })) };
}

describe("billing access policy", () => {
  it("grants permanent access only for an active, paid permanent purchase", () => {
    expect(grantsBillingAccess([purchase("PERMANENT", "ACTIVE", ["APPROVED"])], now)).toBe(true);
    expect(grantsBillingAccess([purchase("PERMANENT", "PENDING", ["APPROVED"])], now)).toBe(false);
    expect(grantsBillingAccess([purchase("PERMANENT", "REFUNDED", ["REFUNDED"])], now)).toBe(false);
    expect(grantsBillingAccess([purchase("PERMANENT", "CHARGEBACK", ["CHARGEBACK_LOST"])], now)).toBe(false);
  });

  it("keeps a permanent purchase valid while its contestation is unresolved or won", () => {
    expect(grantsBillingAccess([purchase("PERMANENT", "ACTIVE", ["CHARGEBACK"])], now)).toBe(true);
    expect(grantsBillingAccess([purchase("PERMANENT", "ACTIVE", ["DISPUTED"])], now)).toBe(true);
    expect(grantsBillingAccess([purchase("PERMANENT", "ACTIVE", ["CHARGEBACK_WON"])], now)).toBe(true);
  });

  it("grants monthly access only through a confirmed paid period", () => {
    expect(grantsBillingAccess([purchase("MONTHLY", "ACTIVE", ["APPROVED"], future)], now)).toBe(true);
    expect(grantsBillingAccess([purchase("MONTHLY", "PENDING", ["REJECTED"], future)], now)).toBe(false);
    expect(grantsBillingAccess([purchase("MONTHLY", "ACTIVE", ["APPROVED"], past)], now)).toBe(false);
    expect(grantsBillingAccess([purchase("MONTHLY", "ACTIVE", ["APPROVED"], null)], now)).toBe(false);
  });

  it("retains monthly access through the paid period after cancellation or renewal failure", () => {
    expect(grantsBillingAccess([purchase("MONTHLY", "CANCELLED", ["APPROVED"], future)], now)).toBe(true);
    expect(grantsBillingAccess([purchase("MONTHLY", "PAST_DUE", ["APPROVED", "REJECTED"], future)], now)).toBe(true);
    expect(grantsBillingAccess([purchase("MONTHLY", "PAST_DUE", ["APPROVED", "REJECTED"], past)], now)).toBe(false);
  });

  it("preserves access during a dispute and when resolved for the user, but removes the affected payment after a loss", () => {
    expect(grantsBillingAccess([purchase("MONTHLY", "ACTIVE", ["DISPUTED"], future)], now)).toBe(true);
    expect(grantsBillingAccess([purchase("MONTHLY", "ACTIVE", ["CHARGEBACK_WON"], future)], now)).toBe(true);
    expect(grantsBillingAccess([purchase("MONTHLY", "CHARGEBACK", ["CHARGEBACK_LOST"], future)], now)).toBe(false);
  });

  it("partial refunds preserve the paid entitlement; full refunds remove only the affected purchase", () => {
    expect(grantsBillingAccess([purchase("PERMANENT", "ACTIVE", ["PARTIALLY_REFUNDED"])], now)).toBe(true);
    expect(grantsBillingAccess([purchase("MONTHLY", "ACTIVE", ["PARTIALLY_REFUNDED"], future)], now)).toBe(true);
    expect(grantsBillingAccess([
      purchase("MONTHLY", "REFUNDED", ["REFUNDED"], future),
      purchase("PERMANENT", "ACTIVE", ["APPROVED"]),
    ], now)).toBe(true);
    expect(grantsBillingAccess([purchase("MONTHLY", "REFUNDED", ["REFUNDED"], future)], now)).toBe(false);
  });

  it("does not let monthly cancellation or delinquency revoke a separate permanent grant", () => {
    expect(grantsBillingAccess([
      purchase("MONTHLY", "PAST_DUE", ["REJECTED"], null),
      purchase("PERMANENT", "ACTIVE", ["APPROVED"]),
    ], now)).toBe(true);
  });
});
