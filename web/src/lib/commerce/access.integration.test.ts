// Acesso às áreas principais (Planejamento, Questões, Simulados...) com banco real: liberação individual do plano
// pelo administrador, parceiro sempre com acesso (e sem vencimento) e plano do parceiro já nascendo liberado.
import { afterAll, beforeAll, beforeEach, describe, expect, it, vi } from "vitest";
import { hasTestDb, makeTestClient, resetTestData } from "./test-support";

vi.mock("server-only", () => ({}));
vi.mock("@/lib/db", async () => {
  const { hasTestDb: ok, makeTestClient: make } = await import("./test-support");
  return { db: ok ? make("vitest_online") : {} };
});
const session = vi.hoisted(() => ({ current: null as null | Record<string, unknown> }));
vi.mock("@/lib/auth/session", () => ({ getCurrentUser: vi.fn(async () => session.current) }));
vi.mock("next/navigation", () => ({
  redirect: (url: string) => {
    throw Object.assign(new Error(`REDIRECT:${url}`), { digest: `NEXT_REDIRECT;${url}` });
  },
}));
vi.mock("next/cache", () => ({ revalidatePath: vi.fn() }));
// a re-elaboração do plano depende do conteúdo semeado; aqui vale o caminho de ativação direta de approvePlan
vi.mock("@/lib/plan/regenerate", () => ({ regeneratePlanForUser: vi.fn(async () => ({ success: false, message: "sem conteúdo no teste" })) }));
vi.mock("@/lib/email", () => ({ sendPlanReadyEmail: vi.fn(async () => ({ success: false })) }));

const PAST = new Date(Date.now() - 30 * 86_400_000);

describe.skipIf(!hasTestDb)("acesso às áreas principais", { timeout: 60_000 }, () => {
  let db: ReturnType<typeof makeTestClient>;
  let admin: { id: string; email: string };

  beforeAll(async () => {
    db = (await import("@/lib/db")).db as unknown as ReturnType<typeof makeTestClient>;
  });
  beforeEach(async () => {
    await resetTestData(db, "vitest_online");
    await db.plan.deleteMany();
    await db.systemSetting.deleteMany();
    admin = await db.user.create({ data: { email: "admin@x.com", passwordHash: "x", role: "ADMIN" } });
    session.current = null;
  });
  afterAll(async () => {
    if (db?.$disconnect) await db.$disconnect();
  });

  const pendingPlan = (userId: string) =>
    db.plan.create({ data: { userId, status: "PENDING_ANALYSIS", version: 1, startDate: new Date("2026-10-19"), examDate: new Date("2027-02-28"), params: {}, coverage: {}, warnings: [] } });

  it("a liberação individual do plano pelo administrador libera o acesso daquele aluno (e só dele)", async () => {
    const { canUserAccessCoreFeatures } = await import("@/lib/system-settings");
    const { approvePlan } = await import("@/lib/admin/cadastros-actions");
    const a = await db.user.create({ data: { email: "a@x.com", passwordHash: "x" } });
    const b = await db.user.create({ data: { email: "b@x.com", passwordHash: "x" } });
    const planA = await pendingPlan(a.id);
    await pendingPlan(b.id);
    expect(await canUserAccessCoreFeatures("USER", a.id)).toBe(false);

    session.current = { ...admin, role: "ADMIN", isPartner: false, accessExpiresAt: null };
    const r = await approvePlan(planA.id);
    expect(r.success).toBe(true);
    expect((await db.plan.findUniqueOrThrow({ where: { id: planA.id } })).status).toBe("ACTIVE");
    expect(await canUserAccessCoreFeatures("USER", a.id)).toBe(true);
    expect(await canUserAccessCoreFeatures("USER", b.id)).toBe(false);
  });

  it("parceiro ativo tem acesso a tudo, com ou sem plano; desativado perde o acesso", async () => {
    const { canUserAccessCoreFeatures } = await import("@/lib/system-settings");
    const { createPartner, setPartnerActive } = await import("./partners");
    const p = await createPartner({ email: "parceiro@x.com", username: "parceiro", password: "senha-inicial-1" }, admin.id);
    const user = await db.user.findUniqueOrThrow({ where: { email: "parceiro@x.com" } });
    expect(await canUserAccessCoreFeatures("USER", user.id)).toBe(true);
    await setPartnerActive(p.partnerId, false, admin.id);
    expect(await canUserAccessCoreFeatures("USER", user.id)).toBe(false);
  });

  it("o acesso do parceiro não vence; o do aluno comum vence", async () => {
    const { requireUser } = await import("@/lib/auth/dal");
    const base = { id: "u1", email: "x@x.com", name: null, username: null, role: "USER", mustChangePassword: false, accessExpiresAt: PAST };
    session.current = { ...base, isPartner: true };
    await expect(requireUser()).resolves.toMatchObject({ id: "u1" });
    session.current = { ...base, isPartner: false };
    await expect(requireUser()).rejects.toThrow("REDIRECT:/pagamentos?status=acesso-expirado");
  });

  it("plano criado por parceiro já nasce ativo; o do aluno comum fica em análise", async () => {
    const { savePlan } = await import("@/lib/plan/persist");
    const { createPartner } = await import("./partners");
    await createPartner({ email: "parceiro2@x.com", username: "parceiro2", password: "senha-inicial-1" }, admin.id);
    const partner = await db.user.findUniqueOrThrow({ where: { email: "parceiro2@x.com" } });
    const student = await db.user.create({ data: { email: "aluno@x.com", passwordHash: "x" } });
    const args = {
      input: { startDate: "2026-10-19", examDate: "2027-02-28", hoursPerWeek: 10, subjects: [], contest: "CBMPE_OFICIAL" },
      result: { params: {}, coverage: {}, warnings: [], weeks: [] },
      diagnostics: {},
      foreignLanguage: null,
      hoursBand: "MODERADO" as const,
    };
    const planOf = async (userId: string) => {
      const id = await savePlan({ userId, ...args } as unknown as Parameters<typeof savePlan>[0]);
      return (await db.plan.findUniqueOrThrow({ where: { id } })).status;
    };
    expect(await planOf(partner.id)).toBe("ACTIVE");
    expect(await planOf(student.id)).toBe("PENDING_ANALYSIS");
  });
});
