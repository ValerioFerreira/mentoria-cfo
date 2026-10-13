import { describe, expect, it, vi, beforeEach } from "vitest";
import { CONTEST_SUBTITLES } from "./contests";

vi.mock("server-only", () => ({}));

const mockFindFirst = vi.fn();
vi.mock("@/lib/db", () => ({
  db: {
    waitlistEntry: {
      findFirst: (...args: unknown[]) => mockFindFirst(...args),
    },
  },
}));

const mockGetCookie = vi.fn();
vi.mock("next/headers", () => ({
  cookies: vi.fn(async () => ({
    get: (key: string) => mockGetCookie(key),
  })),
}));

describe("CONTEST_SUBTITLES", () => {
  it("mapeia os concursos para os subtítulos esperados", () => {
    expect(CONTEST_SUBTITLES.CBMPE_OFICIAL).toBe("OFICIAL - CBMPE");
    expect(CONTEST_SUBTITLES.CBMPE_SOLDADO).toBe("PRAÇA - CBMPE");
    expect(CONTEST_SUBTITLES.PCPE_AGENTE).toBe("AGENTE - PCPE");
  });
});

describe("getUserContest e getUserContestSubtitle", () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it("retorna o subtítulo padrão quando não há cookie nem waitlist", async () => {
    mockGetCookie.mockReturnValue(undefined);
    mockFindFirst.mockResolvedValue(null);

    const { getUserContestSubtitle } = await import("./user-contest");
    const subtitle = await getUserContestSubtitle("aluno@exemplo.com");
    expect(subtitle).toBe("OFICIAL - CBMPE");
  });

  it("retorna o subtítulo vindo do cookie de preferência", async () => {
    mockGetCookie.mockReturnValue({ value: "CBMPE_SOLDADO" });

    const { getUserContestSubtitle } = await import("./user-contest");
    const subtitle = await getUserContestSubtitle("aluno@exemplo.com");
    expect(subtitle).toBe("PRAÇA - CBMPE");
  });

  it("retorna o subtítulo vindo da lista de espera (cadastro)", async () => {
    mockGetCookie.mockReturnValue(undefined);
    mockFindFirst.mockResolvedValue({ contest: "PCPE_AGENTE" });

    const { getUserContestSubtitle } = await import("./user-contest");
    const subtitle = await getUserContestSubtitle("aluno@exemplo.com");
    expect(subtitle).toBe("AGENTE - PCPE");
  });

  it("retorna OFICIAL - CBMPE quando cadastrado como CBMPE_OFICIAL", async () => {
    mockGetCookie.mockReturnValue(undefined);
    mockFindFirst.mockResolvedValue({ contest: "CBMPE_OFICIAL" });

    const { getUserContestSubtitle } = await import("./user-contest");
    const subtitle = await getUserContestSubtitle("aluno@exemplo.com");
    expect(subtitle).toBe("OFICIAL - CBMPE");
  });
});
