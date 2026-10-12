// Integração das portas de entrada (server actions) com banco real: autorização no servidor, preço sempre do
// servidor, restrições do parceiro (login, senha) e fluxo da lista de espera/aprovação. Sessão e e-mail simulados.
import { afterAll, beforeAll, beforeEach, describe, expect, it, vi } from "vitest";
import { hasTestDb, makeTestClient, resetTestData } from "./test-support";

vi.mock("server-only", () => ({}));
vi.mock("@/lib/db", async () => {
  const { hasTestDb: ok, makeTestClient: make } = await import("./test-support");
  return { db: ok ? make("vitest_actions") : {} };
});
const session = vi.hoisted(() => ({ current: null as null | Record<string, unknown> }));
vi.mock("@/lib/auth/session", () => ({
  getCurrentUser: vi.fn(async () => session.current),
  createSession: vi.fn(async () => undefined),
  destroySession: vi.fn(async () => undefined),
  SESSION_COOKIE: "cfo_session",
}));
vi.mock("next/navigation", () => ({
  redirect: (url: string) => {
    throw Object.assign(new Error(`REDIRECT:${url}`), { digest: `NEXT_REDIRECT;${url}` });
  },
  notFound: () => {
    throw new Error("NOT_FOUND");
  },
}));
vi.mock("next/cache", () => ({ revalidatePath: vi.fn() }));
vi.mock("next/headers", () => ({
  headers: async () => new Headers({ "x-forwarded-for": `10.0.0.${Math.floor(Math.random() * 250)}` }),
  cookies: async () => ({ get: () => undefined, set: () => undefined, delete: () => undefined }),
}));
vi.mock("@/lib/email", () => ({
  generateTemporaryPassword: (p: string) => `${p}-TESTE1`,
  sendApprovalEmail: vi.fn(async () => ({ success: false })),
  sendResendCredentialsEmail: vi.fn(async () => ({ success: false })),
  sendPasswordResetEmail: vi.fn(async () => ({ success: false })),
  sendPlanReadyEmail: vi.fn(async () => ({ success: false })),
}));

const fd = (o: Record<string, string>) => {
  const f = new FormData();
  for (const [k, v] of Object.entries(o)) f.set(k, v);
  return f;
};
const asUser = (u: { id: string; email: string; role?: string; isPartner?: boolean; name?: string | null }) => {
  session.current = { name: null, username: null, mustChangePassword: false, accessExpiresAt: null, role: "USER", isPartner: false, ...u };
};
const today = () => new Date(Date.now() - 3 * 3_600_000).toISOString().slice(0, 10);

describe.skipIf(!hasTestDb)("server actions: autorização e preço do servidor", { timeout: 60_000 }, () => {
  let db: ReturnType<typeof makeTestClient>;
  let admin: { id: string; email: string };
  let student: { id: string; email: string };

  beforeAll(async () => {
    db = (await import("@/lib/db")).db as unknown as ReturnType<typeof makeTestClient>;
    process.env.PIX_KEY = "chave-pix-teste@mentoria.local";
  });

  beforeEach(async () => {
    await resetTestData(db, "vitest_actions");
    await db.contestSetting.upsert({ where: { contest: "CBMPE_OFICIAL" }, create: { contest: "CBMPE_OFICIAL", category: "OFICIAL", examDate: new Date("2027-02-28") }, update: { category: "OFICIAL", examDate: new Date("2027-02-28") } });
    await db.contestSetting.upsert({ where: { contest: "CBMPE_SOLDADO" }, create: { contest: "CBMPE_SOLDADO", category: "PRACA", examDate: null }, update: { category: "PRACA", examDate: null } });
    admin = await db.user.create({ data: { email: "admin@x.com", passwordHash: "x", role: "ADMIN" } });
    student = await db.user.create({ data: { email: "aluno@x.com", passwordHash: "x" } });
    session.current = null;
  });

  afterAll(async () => {
    if (db?.$disconnect) await db.$disconnect();
  });

  it("usuário comum e parceiro não executam operações administrativas (nada é gravado)", async () => {
    const actions = await import("./admin-actions");
    const { createContract } = await import("./contracts");
    const c = await createContract({ contest: "CBMPE_OFICIAL", customerEmail: "cli@x.com" }, null);
    asUser(student);
    await expect(actions.adminRegisterPayment(null, fd({ contractId: c.contractId, amount: "60", paidAt: today(), method: "PIX", idempotencyKey: "chave-123456" }))).rejects.toThrow("REDIRECT:/");
    await expect(actions.adminCreatePartner(null, fd({ email: "p@x.com", username: "pp1", password: "12345678" }))).rejects.toThrow("REDIRECT:/");
    await expect(actions.adminUpdateContestSetting(null, fd({ contest: "CBMPE_OFICIAL", category: "PRACA", examDate: "" }))).rejects.toThrow("REDIRECT:/");
    asUser({ ...student, isPartner: true });
    await expect(actions.adminRegisterPayout(null, fd({ partnerId: "x", amount: "10", paidAt: today(), method: "Pix", idempotencyKey: "chave-123456" }))).rejects.toThrow("REDIRECT:/");
    session.current = null;
    await expect(actions.adminRegisterPayment(null, fd({ contractId: c.contractId, amount: "60", paidAt: today(), method: "PIX", idempotencyKey: "chave-654321" }))).rejects.toThrow("REDIRECT:/login");
    expect(await db.manualPayment.count()).toBe(0);
    expect(await db.partner.count()).toBe(0);
    expect((await db.contestSetting.findUniqueOrThrow({ where: { contest: "CBMPE_OFICIAL" } })).category).toBe("OFICIAL");
  });

  it("administrador registra pagamento; campos extras do formulário (status, comissão) são ignorados", async () => {
    const actions = await import("./admin-actions");
    const { createContract } = await import("./contracts");
    const c = await createContract({ contest: "CBMPE_OFICIAL", customerEmail: "cli2@x.com" }, null);
    asUser({ ...admin, role: "ADMIN" });
    const r = await actions.adminRegisterPayment(null, fd({ contractId: c.contractId, amount: "30,00", paidAt: today(), method: "PIX", idempotencyKey: "chave-abcdef", status: "PAID", paidAmount: "60", finalAmount: "1" }));
    expect(r.ok).toBe(true);
    const row = await db.contract.findUniqueOrThrow({ where: { id: c.contractId } });
    expect([row.status, row.paidAmount.toString(), row.finalAmount.toString()]).toEqual(["PARTIAL", "30", "60"]);
    const neg = await actions.adminRegisterPayment(null, fd({ contractId: c.contractId, amount: "-10", paidAt: today(), method: "PIX", idempotencyKey: "chave-negativa" }));
    expect(neg.ok).toBe(false);
  });

  it("cliente logado: preço e desconto enviados pelo navegador não têm efeito", async () => {
    const { startContract } = await import("./customer-actions");
    asUser(student);
    await expect(startContract(null, fd({ contest: "CBMPE_OFICIAL", finalAmount: "1.00", partnerDiscountPoints: "100", price: "0" }))).rejects.toThrow(/REDIRECT:\/pagamentos\/contratacao\//);
    const c = await db.contract.findFirstOrThrow({ where: { userId: student.id } });
    expect([c.finalAmount.toString(), c.partnerDiscountPoints, c.customerEmail]).toEqual(["60", 0, "aluno@x.com"]);
  });

  it("parceiro: login bloqueado ao desativar; não troca a própria senha", async () => {
    const { createPartner, setPartnerActive } = await import("./partners");
    const auth = await import("@/app/(auth)/actions");
    const profile = await import("@/lib/profile/actions");
    const p = await createPartner({ email: "parc@x.com", username: "parc", password: "senha-forte-1" }, admin.id);
    const login = (password: string) => auth.login(undefined, fd({ email: "parc@x.com", password }));
    await expect(login("senha-forte-1")).rejects.toThrow("REDIRECT:/");
    const partnerUser = await db.user.findUniqueOrThrow({ where: { email: "parc@x.com" } });
    asUser({ id: partnerUser.id, email: partnerUser.email, isPartner: true });
    expect(await auth.changePassword(undefined, fd({ password: "nova-senha-123", confirmPassword: "nova-senha-123" }))).toMatchObject({ message: expect.stringMatching(/administração/) });
    expect(await profile.updateUserPassword(undefined, fd({ currentPassword: "senha-forte-1", newPassword: "nova-senha-123", confirmPassword: "nova-senha-123" }))).toMatchObject({ message: expect.stringMatching(/administração/) });
    expect(await profile.sendSelfPasswordReset()).toMatchObject({ success: false });
    expect((await db.user.findUniqueOrThrow({ where: { id: partnerUser.id } })).passwordHash).toBe(partnerUser.passwordHash);
    await setPartnerActive(p.partnerId, false, admin.id);
    expect(await login("senha-forte-1")).toMatchObject({ message: expect.stringMatching(/desativado/) });
  });

  it("painel: só parceiro ativo da sessão; usuário comum é redirecionado", async () => {
    const { requirePartner } = await import("@/lib/auth/dal");
    asUser(student);
    await expect(requirePartner()).rejects.toThrow("REDIRECT:/");
  });

  it("lista de espera com cupom: Pix de R$ 42,00; autoindicação recusada; atribuição pelo cupom", async () => {
    const { createPartner } = await import("./partners");
    const { joinWaitlist } = await import("@/app/(public)/lista-de-espera/[concurso]/actions");
    const p = await createPartner({ email: "div@x.com", username: "divulga", password: "senha-forte-1" }, admin.id);
    const r = await joinWaitlist("cbmpe-oficial", undefined, fd({ name: "Cliente Indicado", email: "novo@x.com", username: "novo1", coupon: p.couponCode.toLowerCase(), amount: "1" }));
    expect(r?.payment).toMatchObject({ amount: "42,00", couponCode: p.couponCode });
    expect(r?.payment?.payload).toContain("540542.00");
    expect(await db.partnerReferral.count({ where: { partnerId: p.partnerId, customerEmail: "novo@x.com" } })).toBe(1);
    const self = await joinWaitlist("cbmpe-oficial", undefined, fd({ name: "O Próprio Parceiro", email: "div@x.com", username: "divulga2", coupon: p.couponCode }));
    expect(self).toMatchObject({ errors: { email: [expect.any(String)] } }); // já tem conta
    const bad = await joinWaitlist("cbmpe-soldado", undefined, fd({ name: "Outra Pessoa", email: "outra@x.com", username: "outra1", coupon: "NAOEXISTE" }));
    expect(bad).toMatchObject({ errors: { coupon: [expect.stringMatching(/Cupom inválido/)] } });
    expect(await db.waitlistEntry.count({ where: { email: "outra@x.com" } })).toBe(0);
    const praca = await joinWaitlist("cbmpe-soldado", undefined, fd({ name: "Outra Pessoa", email: "outra@x.com", username: "outra1" }));
    expect(praca?.payment?.amount).toBe("40,00");
  });

  it("aprovação 'até a prova': exige quitação (ou justificativa), cria a conta e liga a contratação", async () => {
    const { joinWaitlist } = await import("@/app/(public)/lista-de-espera/[concurso]/actions");
    const { approveRegistration } = await import("@/lib/admin/cadastros-actions");
    const { registerPayment } = await import("./payments");
    await joinWaitlist("cbmpe-oficial", undefined, fd({ name: "Aluno Novo", email: "apr@x.com", username: "apr1" }));
    const entry = await db.waitlistEntry.findFirstOrThrow({ where: { email: "apr@x.com" } });
    const contract = await db.contract.findFirstOrThrow({ where: { customerEmail: "apr@x.com" } });
    asUser({ ...admin, role: "ADMIN" });
    const blocked = await approveRegistration(entry.id, "UNTIL_EXAM");
    expect(blocked).toMatchObject({ success: false, message: expect.stringMatching(/saldo pendente/) });
    expect(await db.user.count({ where: { email: "apr@x.com" } })).toBe(0); // nada foi criado pela metade
    await registerPayment({ contractId: contract.id, amountCents: 6000, paidAt: new Date(), method: "PIX", idempotencyKey: "pag-aprovacao-1" }, admin.id);
    const ok = await approveRegistration(entry.id, "UNTIL_EXAM");
    expect(ok.success).toBe(true);
    const user = await db.user.findUniqueOrThrow({ where: { email: "apr@x.com" } });
    expect(user.accessExpiresAt?.toISOString()).toBe("2027-03-01T02:59:59.999Z");
    expect((await db.contract.findUniqueOrThrow({ where: { id: contract.id } })).userId).toBe(user.id);
  });

  it("aprovação com data da prova indefinida não atribui validade incorreta", async () => {
    const { joinWaitlist } = await import("@/app/(public)/lista-de-espera/[concurso]/actions");
    const { approveRegistration } = await import("@/lib/admin/cadastros-actions");
    await joinWaitlist("cbmpe-soldado", undefined, fd({ name: "Aluno Praça", email: "praca@x.com", username: "praca1" }));
    const entry = await db.waitlistEntry.findFirstOrThrow({ where: { email: "praca@x.com" } });
    asUser({ ...admin, role: "ADMIN" });
    const r = await approveRegistration(entry.id, "UNTIL_EXAM", { override: true, justification: "Pagamento conferido no extrato" });
    expect(r).toMatchObject({ success: false, message: expect.stringMatching(/Data da prova/) });
    expect(await db.user.count({ where: { email: "praca@x.com" } })).toBe(0);
  });
});
