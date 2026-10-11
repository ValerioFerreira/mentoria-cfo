import { describe, expect, it, vi, beforeEach } from "vitest";

vi.mock("server-only", () => ({}));

// Mock do db
vi.mock("@/lib/db", () => {
  let mockValue = "false";
  return {
    db: {
      systemSetting: {
        findUnique: vi.fn(async () => ({ key: "PLATFORM_RELEASED", value: mockValue })),
        upsert: vi.fn(async (args: any) => {
          mockValue = args.update.value;
          return { key: "PLATFORM_RELEASED", value: mockValue };
        }),
      },
    },
  };
});

import { canUserAccessCoreFeatures, isPlatformReleased, setPlatformReleased } from "./system-settings";

describe("Controle de Acesso da Plataforma (SystemSettings)", () => {
  beforeEach(async () => {
    await setPlatformReleased(false);
  });

  it("Usuário ADMIN sempre tem acesso liberado, mesmo quando o sistema está bloqueado", async () => {
    const adminAccess = await canUserAccessCoreFeatures("ADMIN");
    expect(adminAccess).toBe(true);
  });

  it("Usuário comum (USER) tem acesso negado quando o sistema está em modo revisão (bloqueado)", async () => {
    const userAccess = await canUserAccessCoreFeatures("USER");
    expect(userAccess).toBe(false);
  });

  it("Usuário comum (USER) ganha acesso após a liberação geral da plataforma", async () => {
    expect(await canUserAccessCoreFeatures("USER")).toBe(false);

    // Ativa a liberação geral
    await setPlatformReleased(true);
    expect(await isPlatformReleased()).toBe(true);

    // Usuário comum agora tem acesso
    expect(await canUserAccessCoreFeatures("USER")).toBe(true);
  });
});
