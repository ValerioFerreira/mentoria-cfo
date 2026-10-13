import { describe, expect, it, vi, beforeEach } from "vitest";

vi.mock("server-only", () => ({}));

const mockFindUnique = vi.fn();
const mockFindFirst = vi.fn();

vi.mock("@/lib/db", () => ({
  db: {
    plan: {
      findUnique: (...args: unknown[]) => mockFindUnique(...args),
      findFirst: (...args: unknown[]) => mockFindFirst(...args),
    },
    waitlistEntry: {
      findFirst: vi.fn(),
    },
  },
}));

describe("regeneratePlanForUser module", () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it("exporta a função regeneratePlanForUser", async () => {
    const { regeneratePlanForUser } = await import("./regenerate");
    expect(typeof regeneratePlanForUser).toBe("function");
  });

  it("retorna erro amigável quando o planejamento/usuário não é encontrado", async () => {
    mockFindFirst.mockResolvedValue(null);
    mockFindUnique.mockResolvedValue(null);

    const { regeneratePlanForUser } = await import("./regenerate");
    const res = await regeneratePlanForUser("inexistente@mentor.test");
    expect(res.success).toBe(false);
    expect(res.message).toContain("Nenhum planejamento pendente ou ativo encontrado");
  });
});
