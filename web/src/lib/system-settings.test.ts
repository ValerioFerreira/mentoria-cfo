import { describe, expect, it, vi, beforeEach } from "vitest";

vi.mock("server-only", () => ({}));

const state = {
  platformReleased: "false",
  partner: null as { active: boolean } | null,
  activePlan: null as { id: string } | null,
  billingAccess: false,
};

vi.mock("@/lib/db", () => ({
  db: {
    systemSetting: {
      findUnique: vi.fn(async () => ({ key: "PLATFORM_RELEASED", value: state.platformReleased })),
      upsert: vi.fn(async (args: { update: { value: string } }) => {
        state.platformReleased = args.update.value;
        return { key: "PLATFORM_RELEASED", value: state.platformReleased };
      }),
    },
    partner: {
      findUnique: vi.fn(async () => state.partner),
    },
    plan: {
      findFirst: vi.fn(async () => state.activePlan),
    },
  },
}));

vi.mock("@/lib/billing/access", () => ({
  hasBillingAccess: vi.fn(async () => state.billingAccess),
}));

import { canUserAccessCoreFeatures, isPlatformReleased, setPlatformReleased } from "./system-settings";

describe("Controle de Acesso da Plataforma (SystemSettings)", () => {
  beforeEach(async () => {
    state.platformReleased = "false";
    state.partner = null;
    state.activePlan = null;
    state.billingAccess = false;
    await setPlatformReleased(false);
  });

  it("Usuário ADMIN sempre tem acesso liberado, mesmo quando o sistema está bloqueado", async () => {
    expect(await canUserAccessCoreFeatures("ADMIN")).toBe(true);
  });

  it("Usuário comum (USER) tem acesso negado quando o sistema está em modo revisão (bloqueado)", async () => {
    expect(await canUserAccessCoreFeatures("USER", "u1")).toBe(false);
  });

  it("Usuário comum (USER) ganha acesso após a liberação geral da plataforma", async () => {
    expect(await canUserAccessCoreFeatures("USER", "u1")).toBe(false);
    await setPlatformReleased(true);
    expect(await isPlatformReleased()).toBe(true);
    expect(await canUserAccessCoreFeatures("USER", "u1")).toBe(true);
  });

  it("Parceiro ativo tem acesso acadêmico completo mesmo sem liberação geral", async () => {
    state.partner = { active: true };
    expect(await canUserAccessCoreFeatures("USER", "partner-1")).toBe(true);
  });

  it("Parceiro desativado não ganha acesso só por ter registro de Partner", async () => {
    state.partner = { active: false };
    expect(await canUserAccessCoreFeatures("USER", "partner-1")).toBe(false);
  });

  it("Plano ACTIVE (liberação individual) libera o acesso do aluno", async () => {
    state.activePlan = { id: "plan-1" };
    expect(await canUserAccessCoreFeatures("USER", "aluno-1")).toBe(true);
  });

  it("Direito de pagamento válido libera o acesso do aluno", async () => {
    state.billingAccess = true;
    expect(await canUserAccessCoreFeatures("USER", "aluno-1")).toBe(true);
  });
});
