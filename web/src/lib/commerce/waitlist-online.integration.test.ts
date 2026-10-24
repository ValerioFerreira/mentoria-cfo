// Lista de espera com o Mercado Pago configurado: o Pix mostrado é o dinâmico da conta da empresa, com o valor do
// servidor; trocar o cupom cancela o Pix antigo; se o provedor falhar, cai no Pix estático. Mercado Pago falso.
import { afterAll, beforeAll, beforeEach, describe, expect, it, vi } from "vitest";
import { hasTestDb, makeTestClient, resetTestData } from "./test-support";

const fake = vi.hoisted(() => ({
  seq: 5000,
  payments: new Map<string, Record<string, unknown>>(),
  posts: [] as Record<string, unknown>[],
  failNext: false,
  me: { id: 987654, identification: { type: "CNPJ" } } as Record<string, unknown>,
}));

vi.mock("server-only", () => ({}));
vi.mock("@/lib/db", async () => {
  const { hasTestDb: ok, makeTestClient: make } = await import("./test-support");
  return { db: ok ? make("vitest_online") : {} };
});
vi.mock("next/headers", () => ({ headers: async () => new Headers({ "x-forwarded-for": `10.1.0.${Math.floor(Math.random() * 250)}` }) }));
vi.mock("@/lib/billing/mercado-pago", async (importActual) => {
  const actual = await importActual<typeof import("@/lib/billing/mercado-pago")>();
  return {
    ...actual,
    mercadoPagoConfigured: () => true,
    mercadoPagoToken: () => "APP_USR-token-de-teste",
    notificationUrl: () => "https://teste.local/api/webhooks/mercadopago",
    siteUrl: () => new URL("https://teste.local"),
    mpRequest: async (path: string, init: RequestInit = {}) => {
      const method = (init.method ?? "GET").toUpperCase();
      const body = init.body ? (JSON.parse(String(init.body)) as Record<string, unknown>) : undefined;
      if (fake.failNext) {
        fake.failNext = false;
        throw new actual.MercadoPagoError(503);
      }
      if (method === "POST" && path === "/v1/payments") {
        fake.posts.push(body!);
        const id = String(++fake.seq);
        const p = {
          id,
          status: "pending",
          transaction_amount: body!.transaction_amount,
          currency_id: "BRL",
          external_reference: body!.external_reference,
          date_of_expiration: body!.date_of_expiration,
          point_of_interaction: { transaction_data: { qr_code: `PIX-MP-${id}`, qr_code_base64: "iVBORw0KGgo=", ticket_url: "https://mp.test/t" } },
        };
        fake.payments.set(id, p);
        return p;
      }
      if (path === "/users/me") return fake.me;
      const one = path.match(/^\/v1\/payments\/(\d+)$/);
      if (one && method === "PUT") {
        Object.assign(fake.payments.get(one[1])!, { status: String(body!.status) });
        return fake.payments.get(one[1]);
      }
      throw new actual.MercadoPagoError(404);
    },
  };
});

const fd = (o: Record<string, string>) => {
  const f = new FormData();
  for (const [k, v] of Object.entries(o)) f.set(k, v);
  return f;
};

describe.skipIf(!hasTestDb)("lista de espera com Pix dinâmico do Mercado Pago", { timeout: 60_000 }, () => {
  let db: ReturnType<typeof makeTestClient>;

  beforeAll(async () => {
    db = (await import("@/lib/db")).db as unknown as ReturnType<typeof makeTestClient>;
    process.env.PIX_KEY = "chave-estatica@mentoria.local";
  });

  beforeEach(async () => {
    fake.payments.clear();
    fake.posts.length = 0;
    fake.failNext = false;
    fake.me = { id: 987654, identification: { type: "CNPJ" } };
    delete process.env.MERCADOPAGO_SELLER_ID;
    (await import("./online")).resetAccountCheck();
    await resetTestData(db, "vitest_online");
    await db.contestSetting.upsert({ where: { contest: "CBMPE_OFICIAL" }, create: { contest: "CBMPE_OFICIAL", category: "OFICIAL", examDate: new Date("2027-02-28") }, update: { category: "OFICIAL", examDate: new Date("2027-02-28") } });
  });

  afterAll(async () => {
    if (db?.$disconnect) await db.$disconnect();
  });

  it("o QR e o copia e cola são os do Mercado Pago, com o valor calculado no servidor", async () => {
    const { joinWaitlist } = await import("@/app/(public)/lista-de-espera/[concurso]/actions");
    const r = await joinWaitlist("cbmpe-oficial", undefined, fd({ name: "Cliente Online", email: "online@x.com", username: "online1", amount: "1", price: "0.01" }));
    expect(r?.payment).toMatchObject({ amount: "90,00", plan: "Acesso ilimitado até a prova" });
    expect(r?.payment?.payload).toMatch(/^PIX-MP-/);
    expect(r?.payment?.qr).toBe("data:image/png;base64,iVBORw0KGgo=");
    expect(fake.posts).toHaveLength(1);
    expect(fake.posts[0]).toMatchObject({ transaction_amount: 90, payment_method_id: "pix" });
    expect(await db.manualPayment.count()).toBe(0); // gerar o Pix não é receber
  });

  it("quem volta a abrir a inscrição vê o mesmo Pix (sem gerar outro)", async () => {
    const { joinWaitlist } = await import("@/app/(public)/lista-de-espera/[concurso]/actions");
    const a = await joinWaitlist("cbmpe-oficial", undefined, fd({ name: "Cliente Online", email: "volta@x.com", username: "volta1" }));
    const b = await joinWaitlist("cbmpe-oficial", undefined, fd({ name: "Cliente Online", email: "volta@x.com", username: "volta1" }));
    expect(b?.payment?.payload).toBe(a?.payment?.payload);
    expect(b?.payment?.alreadyJoined).toBe(true);
    expect(fake.posts).toHaveLength(1);
  });

  it("trocar o cupom depois da inscrição substitui a contratação e cancela o Pix antigo no provedor", async () => {
    const admin = await db.user.create({ data: { email: "adm@x.com", passwordHash: "x", role: "ADMIN" } });
    const { createPartner } = await import("./partners");
    const p = await createPartner({ email: "par@x.com", username: "parceiro1", password: "senha-inicial-1" }, admin.id);
    const { joinWaitlist } = await import("@/app/(public)/lista-de-espera/[concurso]/actions");
    const first = await joinWaitlist("cbmpe-oficial", undefined, fd({ name: "Cliente Troca", email: "troca@x.com", username: "troca1" }));
    expect(first?.payment?.amount).toBe("90,00");
    const second = await joinWaitlist("cbmpe-oficial", undefined, fd({ name: "Cliente Troca", email: "troca@x.com", username: "troca1", coupon: p.couponCode }));
    expect(second?.payment?.amount).toBe("72,00");
    expect(second?.payment?.payload).not.toBe(first?.payment?.payload);
    const old = [...fake.payments.values()].find((x) => x.transaction_amount === 90)!;
    expect(old.status).toBe("cancelled");
    expect(await db.onlineCharge.count({ where: { status: "CANCELLED" } })).toBe(1);
  });

  it("se o Mercado Pago falhar, NÃO cai no Pix estático (chave antiga): mostra o erro e tenta de novo depois", async () => {
    const { joinWaitlist } = await import("@/app/(public)/lista-de-espera/[concurso]/actions");
    const warm = await joinWaitlist("cbmpe-oficial", undefined, fd({ name: "Cliente Quente", email: "quente@x.com", username: "quente1" }));
    expect(warm?.payment?.payload).toMatch(/^PIX-MP-/); // conferência da conta feita
    fake.failNext = true;
    const r = await joinWaitlist("cbmpe-oficial", undefined, fd({ name: "Cliente Falha", email: "falha@x.com", username: "falha1" }));
    expect(r?.payment).toBeUndefined();
    expect(r?.message).toMatch(/Não foi possível gerar o pagamento/);
    expect(JSON.stringify(r)).not.toContain("br.gov.bcb.pix");
    // a pessoa tenta de novo e recebe o Pix dinâmico
    const again = await joinWaitlist("cbmpe-oficial", undefined, fd({ name: "Cliente Falha", email: "falha@x.com", username: "falha1" }));
    expect(again?.payment?.payload).toMatch(/^PIX-MP-/);
  });

  it("conta do token diferente do ID do vendedor: nenhuma cobrança e nenhum Pix estático", async () => {
    process.env.MERCADOPAGO_SELLER_ID = "111";
    const { joinWaitlist } = await import("@/app/(public)/lista-de-espera/[concurso]/actions");
    const r = await joinWaitlist("cbmpe-oficial", undefined, fd({ name: "Cliente Conta", email: "conta@x.com", username: "conta1" }));
    expect(r?.payment).toBeUndefined();
    expect(JSON.stringify(r)).not.toContain("br.gov.bcb.pix");
    expect(fake.posts).toHaveLength(0);
  });

  it("CFOA sem examDate: inscrição e pagamento funcionam e a pendência de data da prova vai para os pontos de atenção", async () => {
    await db.contestSetting.upsert({
      where: { contest: "CBMPE_CFOA" },
      create: { contest: "CBMPE_CFOA", category: "OFICIAL", examDate: null },
      update: { category: "OFICIAL", examDate: null },
    });
    const { joinWaitlist } = await import("@/app/(public)/lista-de-espera/[concurso]/actions");
    const r = await joinWaitlist("cbmpe-cfoa", undefined, fd({ name: "Cliente CFOA", email: "cfoa@x.com", username: "cfoa1" }));
    expect(r?.payment).toMatchObject({ amount: "90,00", plan: "Acesso ilimitado até a prova" });
    const contract = await db.contract.findFirstOrThrow({ where: { customerEmail: "cfoa@x.com", contest: "CBMPE_CFOA" } });
    expect(contract.examDateAtContract).toBeNull();
    expect(contract.category).toBe("OFICIAL");

    const { syncContractPayment, onlineOverview } = await import("./online");
    const mpPay = [...fake.payments.values()][0]!;
    await syncContractPayment({
      id: Number(mpPay.id),
      status: "approved",
      status_detail: "accredited",
      transaction_amount: 90,
      currency_id: "BRL",
      payment_method_id: "pix",
      date_approved: new Date().toISOString(),
      external_reference: contract.id,
      metadata: { contract_id: contract.id },
    });

    const updated = await db.contract.findUniqueOrThrow({ where: { id: contract.id } });
    expect(updated.status).toBe("PAID");
    expect(updated.accessGrantedAt).toBeNull();
    const overview = await onlineOverview();
    expect(overview.alerts.some((a) => a.entityId === contract.id && a.action === "ACCESS_GRANT_PENDING")).toBe(true);
  });
});

