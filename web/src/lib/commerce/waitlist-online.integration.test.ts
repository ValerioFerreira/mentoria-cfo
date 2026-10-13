// Lista de espera com o Mercado Pago configurado: o Pix mostrado é o dinâmico da conta da empresa, com o valor do
// servidor; trocar o cupom cancela o Pix antigo; se o provedor falhar, cai no Pix estático. Mercado Pago falso.
import { afterAll, beforeAll, beforeEach, describe, expect, it, vi } from "vitest";
import { hasTestDb, makeTestClient, resetTestData } from "./test-support";

const fake = vi.hoisted(() => ({
  seq: 5000,
  payments: new Map<string, Record<string, unknown>>(),
  posts: [] as Record<string, unknown>[],
  failNext: false,
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
    await resetTestData(db, "vitest_online");
    await db.contestSetting.upsert({ where: { contest: "CBMPE_OFICIAL" }, create: { contest: "CBMPE_OFICIAL", category: "OFICIAL", examDate: new Date("2027-02-28") }, update: { category: "OFICIAL", examDate: new Date("2027-02-28") } });
  });

  afterAll(async () => {
    if (db?.$disconnect) await db.$disconnect();
  });

  it("o QR e o copia e cola são os do Mercado Pago, com o valor calculado no servidor", async () => {
    const { joinWaitlist } = await import("@/app/(public)/lista-de-espera/[concurso]/actions");
    const r = await joinWaitlist("cbmpe-oficial", undefined, fd({ name: "Cliente Online", email: "online@x.com", username: "online1", amount: "1", price: "0.01" }));
    expect(r?.payment).toMatchObject({ amount: "60,00", plan: "Acesso ilimitado até a prova" });
    expect(r?.payment?.payload).toMatch(/^PIX-MP-/);
    expect(r?.payment?.qr).toBe("data:image/png;base64,iVBORw0KGgo=");
    expect(fake.posts).toHaveLength(1);
    expect(fake.posts[0]).toMatchObject({ transaction_amount: 60, payment_method_id: "pix" });
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
    expect(first?.payment?.amount).toBe("60,00");
    const second = await joinWaitlist("cbmpe-oficial", undefined, fd({ name: "Cliente Troca", email: "troca@x.com", username: "troca1", coupon: p.couponCode }));
    expect(second?.payment?.amount).toBe("42,00");
    expect(second?.payment?.payload).not.toBe(first?.payment?.payload);
    const old = [...fake.payments.values()].find((x) => x.transaction_amount === 60)!;
    expect(old.status).toBe("cancelled");
    expect(await db.onlineCharge.count({ where: { status: "CANCELLED" } })).toBe(1);
  });

  it("se o Mercado Pago falhar, mostra o Pix estático (a administração confere)", async () => {
    const { joinWaitlist } = await import("@/app/(public)/lista-de-espera/[concurso]/actions");
    fake.failNext = true;
    const r = await joinWaitlist("cbmpe-oficial", undefined, fd({ name: "Cliente Falha", email: "falha@x.com", username: "falha1" }));
    expect(r?.payment?.payload).toContain("br.gov.bcb.pix");
    expect(r?.payment?.amount).toBe("60,00");
  });
});
