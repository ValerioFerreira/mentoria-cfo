// Integração com Postgres real (schema `vitest_online`) e um Mercado Pago FALSO em memória: criação de Pix e cartão,
// webhook assinado, conciliação com o livro-caixa (comissão, estorno, acesso até a prova) e idempotência.
// Nenhuma chamada de rede e nenhuma cobrança real.
import { createHmac, randomUUID } from "node:crypto";
import { afterAll, beforeAll, beforeEach, describe, expect, it, vi } from "vitest";
import { hasTestDb, makeTestClient, resetTestData } from "./test-support";

const SCHEMA = "vitest_online";
const SECRET = "segredo-de-teste-do-webhook";

const fake = vi.hoisted(() => ({
  seq: 1000,
  payments: new Map<string, Record<string, unknown>>(),
  keys: new Map<string, string>(),
  calls: [] as { method: string; path: string; body?: Record<string, unknown>; key?: string }[],
  me: { id: 987654, nickname: "MISSAO.MENTORIA", identification: { type: "CNPJ" } } as Record<string, unknown>,
  failNext: false,
  wrongAmount: false,
}));

const mail = vi.hoisted(() => ({ sent: [] as Record<string, unknown>[], ok: true }));
vi.mock("@/lib/email", () => ({
  generateTemporaryPassword: (p: string) => `${p}-TESTE1`,
  sendApprovalEmail: vi.fn(async (args: Record<string, unknown>) => {
    mail.sent.push(args);
    return { success: mail.ok };
  }),
}));
vi.mock("server-only", () => ({}));
vi.mock("@/lib/db", async () => {
  const { hasTestDb: ok, makeTestClient: make } = await import("./test-support");
  return { db: ok ? make("vitest_online") : {} };
});
vi.mock("@/lib/billing/mercado-pago", async (importActual) => {
  const actual = await importActual<typeof import("@/lib/billing/mercado-pago")>();
  const mpRequest = async (path: string, init: RequestInit = {}) => {
    const method = (init.method ?? "GET").toUpperCase();
    const body = init.body ? (JSON.parse(String(init.body)) as Record<string, unknown>) : undefined;
    const key = (init.headers as Record<string, string> | undefined)?.["X-Idempotency-Key"];
    fake.calls.push({ method, path, body, key });
    if (fake.failNext) {
      fake.failNext = false;
      throw new actual.MercadoPagoError(500);
    }
    if (method === "POST" && path === "/v1/payments") {
      if (key && fake.keys.has(key)) return fake.payments.get(fake.keys.get(key)!);
      const id = String(++fake.seq);
      const amount = fake.wrongAmount ? 1 : body!.transaction_amount;
      const p = {
        id,
        status: "pending",
        status_detail: "pending_waiting_transfer",
        transaction_amount: amount,
        currency_id: "BRL",
        external_reference: body!.external_reference,
        metadata: body!.metadata,
        payment_method_id: "pix",
        date_of_expiration: body!.date_of_expiration,
        point_of_interaction: { transaction_data: { qr_code: `00020126-pix-${id}`, qr_code_base64: "iVBORw0KGgo=", ticket_url: `https://mp.test/${id}` } },
      };
      fake.payments.set(id, p);
      if (key) fake.keys.set(key, id);
      return p;
    }
    if (method === "POST" && path === "/checkout/preferences") return { id: `pref-${++fake.seq}`, init_point: "https://mp.test/checkout/start" };
    const one = path.match(/^\/v1\/payments\/(\d+)$/);
    if (one && method === "GET") return fake.payments.get(one[1]);
    if (one && method === "PUT") {
      const p = fake.payments.get(one[1])!;
      Object.assign(p, { status: String(body!.status), status_detail: "by_collector" });
      return p;
    }
    if (path === "/users/me") return fake.me;
    throw new actual.MercadoPagoError(404);
  };
  return {
    ...actual,
    mpRequest,
    mercadoPagoConfigured: () => true,
    mercadoPagoToken: () => "APP_USR-token-de-teste",
    notificationUrl: () => "https://teste.local/api/webhooks/mercadopago",
    siteUrl: () => new URL("https://teste.local"),
  };
});

const DAY = 86_400_000;
const key = () => randomUUID();
const money = (d: { toString(): string }) => d.toString();

/** Marca o pagamento falso como aprovado (o que o Mercado Pago faria depois do Pix pago). */
function settle(id: string, extra: Record<string, unknown> = {}) {
  Object.assign(fake.payments.get(id)!, { status: "approved", status_detail: "accredited", date_approved: new Date().toISOString(), date_last_updated: new Date().toISOString(), ...extra });
}

function signed(paymentId: string, opts: { requestId?: string; secret?: string; notificationId?: string; topic?: string } = {}) {
  const requestId = opts.requestId ?? "req-1";
  const ts = "1760000000";
  const v1 = createHmac("sha256", opts.secret ?? SECRET).update(`id:${paymentId};request-id:${requestId};ts:${ts};`).digest("hex");
  return new Request(`https://teste.local/api/webhooks/mercadopago?data.id=${paymentId}&type=payment`, {
    method: "POST",
    headers: { "content-type": "application/json", "x-signature": `ts=${ts},v1=${v1}`, "x-request-id": requestId },
    body: JSON.stringify({ id: opts.notificationId ?? randomUUID(), type: opts.topic ?? "payment", action: "payment.updated", data: { id: paymentId } }),
  });
}

describe.skipIf(!hasTestDb)("pagamento online (Mercado Pago da empresa)", { timeout: 60_000 }, () => {
  let db: ReturnType<typeof makeTestClient>;
  let adminId: string;
  let svc: {
    contracts: typeof import("./contracts");
    online: typeof import("./online");
    partners: typeof import("./partners");
    payments: typeof import("./payments");
  };
  let POST: (r: Request) => Promise<Response>;

  beforeAll(async () => {
    process.env.MERCADOPAGO_WEBHOOK_SECRET = SECRET;
    db = (await import("@/lib/db")).db as unknown as ReturnType<typeof makeTestClient>;
    svc = { contracts: await import("./contracts"), online: await import("./online"), partners: await import("./partners"), payments: await import("./payments") };
    POST = (await import("@/app/api/webhooks/mercadopago/route")).POST;
  });

  beforeEach(async () => {
    fake.payments.clear();
    fake.keys.clear();
    fake.calls.length = 0;
    fake.failNext = false;
    fake.wrongAmount = false;
    mail.sent.length = 0;
    mail.ok = true;
    fake.me = { id: 987654, nickname: "MISSAO.MENTORIA", identification: { type: "CNPJ" } };
    delete process.env.MERCADOPAGO_SELLER_ID;
    svc.online.resetAccountCheck();
    await resetTestData(db, SCHEMA);
    await db.contestSetting.upsert({ where: { contest: "CBMPE_OFICIAL" }, create: { contest: "CBMPE_OFICIAL", category: "OFICIAL", examDate: new Date("2027-02-28") }, update: { category: "OFICIAL", examDate: new Date("2027-02-28") } });
    await db.contestSetting.upsert({ where: { contest: "CBMPE_SOLDADO" }, create: { contest: "CBMPE_SOLDADO", category: "PRACA", examDate: null }, update: { category: "PRACA", examDate: null } });
    adminId = (await db.user.create({ data: { email: "admin@teste.local", passwordHash: "x", role: "ADMIN" } })).id;
  });

  afterAll(async () => {
    if (db?.$disconnect) await db.$disconnect();
  });

  async function student(email = "aluno@teste.local") {
    return db.user.create({ data: { email, passwordHash: "x", accessExpiresAt: new Date(Date.now() - DAY) } });
  }
  async function partner() {
    return svc.partners.createPartner({ email: "parceira@teste.local", username: "parceira", password: "senha-inicial-1" }, adminId);
  }
  /** contratação Oficial (com ou sem cupom) já ligada a uma conta */
  async function contractFor(opts: { coupon?: string; withUser?: boolean; contest?: "CBMPE_OFICIAL" | "CBMPE_SOLDADO" } = {}) {
    const user = opts.withUser === false ? null : await student();
    const r = await svc.contracts.createContract(
      { contest: opts.contest ?? "CBMPE_OFICIAL", customerEmail: user?.email ?? "lista@teste.local", userId: user?.id, couponCode: opts.coupon },
      user?.id ?? null,
    );
    return { id: r.contractId, user };
  }
  const reload = (id: string) => db.contract.findUniqueOrThrow({ where: { id } });
  async function pixPaid(contractId: string) {
    const charge = await svc.online.startPixCharge(contractId);
    const paymentId = (await db.onlineCharge.findUniqueOrThrow({ where: { id: charge.id } })).providerPaymentId!;
    settle(paymentId);
    return paymentId;
  }

  describe("criação da cobrança (valor sempre do servidor)", () => {
    it("Pix: valor, referência e URL de aviso vêm do servidor; repetir reaproveita o mesmo Pix", async () => {
      const p = await partner();
      const { id } = await contractFor({ coupon: p.couponCode });
      const a = await svc.online.startPixCharge(id);
      const b = await svc.online.startPixCharge(id);
      expect(b.id).toBe(a.id);
      expect(a).toMatchObject({ kind: "PIX", status: "PENDING", amountCents: 4200 });
      expect(a.qrCode).toContain("00020126-pix");
      const posts = fake.calls.filter((c) => c.method === "POST" && c.path === "/v1/payments");
      expect(posts).toHaveLength(1);
      expect(posts[0].body).toMatchObject({ transaction_amount: 42, payment_method_id: "pix", external_reference: id, notification_url: "https://teste.local/api/webhooks/mercadopago", payer: { email: "aluno@teste.local" } });
      expect(posts[0].key).toBe(a.id); // chave de idempotência = id local da cobrança
      expect(await db.manualPayment.count()).toBe(0); // criar a cobrança não é receber dinheiro
    });

    it("cartão (Checkout Pro): preferência à vista com o saldo da contratação", async () => {
      const { id } = await contractFor({ contest: "CBMPE_SOLDADO" });
      const c = await svc.online.startCardCheckout(id);
      expect(c.checkoutUrl).toBe("https://mp.test/checkout/start");
      const pref = fake.calls.find((x) => x.path === "/checkout/preferences")!.body!;
      expect(pref).toMatchObject({ external_reference: id, auto_return: "approved" });
      expect((pref.items as { unit_price: number }[])[0].unit_price).toBe(40);
      expect((pref.payment_methods as { installments: number }).installments).toBe(1);
      expect(String((pref.back_urls as { success: string }).success)).toContain(`contrato=${id}`);
    });

    it("com pagamento parcial já recebido, a nova cobrança é só do saldo", async () => {
      const { id } = await contractFor();
      await svc.payments.registerPayment({ contractId: id, amountCents: 2000, paidAt: new Date(Date.now() - DAY), method: "PIX", idempotencyKey: key() }, adminId);
      const c = await svc.online.startPixCharge(id);
      expect(c.amountCents).toBe(4000);
    });

    it("contratação cancelada ou quitada não gera cobrança", async () => {
      const { id } = await contractFor();
      await svc.contracts.cancelContract(id, "cancelada no teste", adminId);
      await expect(svc.online.startPixCharge(id)).rejects.toThrow(/cancelada/);
      const other = await contractFor({ contest: "CBMPE_SOLDADO", withUser: false });
      await svc.payments.registerPayment({ contractId: other.id, amountCents: 4000, paidAt: new Date(Date.now() - DAY), method: "PIX", idempotencyKey: key() }, adminId);
      await expect(svc.online.startPixCharge(other.id)).rejects.toThrow(/quitada/);
    });

    it("falha do provedor ou valor divergente: cobrança cancelada e erro seguro (sem vazar detalhes)", async () => {
      const warm = await contractFor({ contest: "CBMPE_SOLDADO", withUser: false });
      await svc.online.startPixCharge(warm.id); // conferência da conta já feita
      const { id } = await contractFor();
      fake.failNext = true;
      await expect(svc.online.startPixCharge(id)).rejects.toThrow(/Não foi possível gerar o pagamento/);
      fake.wrongAmount = true;
      await expect(svc.online.startPixCharge(id)).rejects.toThrow(/Não foi possível gerar o pagamento/);
      expect(await db.onlineCharge.count({ where: { status: "PENDING" } })).toBe(1); // só a do contrato aquecido
      expect(await db.onlineCharge.count({ where: { status: "CANCELLED" } })).toBe(2);
    });

    it("trava de conta: token de outra conta (ID do vendedor) ou de pessoa física (CPF) não abre cobrança", async () => {
      const { id } = await contractFor();
      process.env.MERCADOPAGO_SELLER_ID = "555"; // o token é da conta 987654
      await expect(svc.online.startPixCharge(id)).rejects.toThrow(/indisponível/);
      await expect(svc.online.startCardCheckout(id)).rejects.toThrow(/indisponível/);
      process.env.MERCADOPAGO_SELLER_ID = "987654";
      fake.me = { id: 987654, nickname: "JOAO", identification: { type: "CPF" } };
      svc.online.resetAccountCheck();
      await expect(svc.online.startPixCharge(id)).rejects.toThrow(/indisponível/);
      expect(fake.calls.filter((c) => c.method === "POST")).toHaveLength(0); // nada foi criado no provedor
      expect(await db.onlineCharge.count()).toBe(0);
      // conta da empresa e ID conferindo: libera
      fake.me = { id: 987654, nickname: "MISSAO.MENTORIA", identification: { type: "CNPJ" } };
      svc.online.resetAccountCheck();
      await expect(svc.online.startPixCharge(id)).resolves.toMatchObject({ status: "PENDING" });
    });
  });

  describe("webhook assinado e conciliação com o livro-caixa", () => {
    it("Pix aprovado: recebimento automático, contratação quitada, comissão de 30% e acesso até a prova", async () => {
      const p = await partner();
      const { id, user } = await contractFor({ coupon: p.couponCode });
      const paymentId = await pixPaid(id);

      const res = await POST(signed(paymentId));
      expect(res.status).toBe(200);

      const payments = await db.manualPayment.findMany({ where: { contractId: id } });
      expect(payments).toHaveLength(1);
      expect(payments[0]).toMatchObject({ source: "MERCADO_PAGO", method: "PIX", createdById: null, providerPaymentId: paymentId, receiptRef: `MP-${paymentId}` });
      expect(money(payments[0].amount)).toBe("42");
      const c = await reload(id);
      expect(c).toMatchObject({ status: "PAID" });
      expect(money(c.paidAmount)).toBe("42");
      const commission = await db.commissionEntry.findMany({ where: { contractId: id } });
      expect(commission.map((x) => money(x.amount))).toEqual(["12.6"]);
      // acesso até o fim do dia da prova (Recife)
      expect((await db.user.findUniqueOrThrow({ where: { id: user!.id } })).accessExpiresAt?.toISOString()).toBe("2027-03-01T02:59:59.999Z");
      expect(await db.onlineCharge.count({ where: { status: "APPROVED" } })).toBe(1);
      expect(await db.auditLog.count({ where: { action: "ACCESS_GRANTED", entityId: id } })).toBe(1);
    });

    it("o mesmo aviso (ou avisos diferentes do mesmo pagamento) não duplica recebimento nem comissão", async () => {
      const p = await partner();
      const { id } = await contractFor({ coupon: p.couponCode });
      const paymentId = await pixPaid(id);
      const same = randomUUID();
      expect((await POST(signed(paymentId, { notificationId: same }))).status).toBe(200);
      expect((await POST(signed(paymentId, { notificationId: same }))).status).toBe(200);
      expect((await POST(signed(paymentId, { notificationId: randomUUID() }))).status).toBe(200);
      await Promise.all([POST(signed(paymentId)), POST(signed(paymentId))]);
      expect(await db.manualPayment.count({ where: { contractId: id } })).toBe(1);
      expect(await db.commissionEntry.count({ where: { contractId: id } })).toBe(1);
      expect(await db.auditLog.count({ where: { action: "PAYMENT_REGISTERED", entityId: id } })).toBe(1);
    });

    it("assinatura inválida é recusada (401) e nada é registrado", async () => {
      const { id } = await contractFor();
      const paymentId = await pixPaid(id);
      const res = await POST(signed(paymentId, { secret: "outro-segredo" }));
      expect(res.status).toBe(401);
      expect(await db.manualPayment.count()).toBe(0);
      expect(await db.billingWebhookEvent.count()).toBe(0);
    });

    it("pendente ou recusado não vira dinheiro recebido", async () => {
      const { id } = await contractFor();
      const charge = await svc.online.startPixCharge(id);
      const paymentId = (await db.onlineCharge.findUniqueOrThrow({ where: { id: charge.id } })).providerPaymentId!;
      expect((await POST(signed(paymentId))).status).toBe(200);
      expect(await db.manualPayment.count()).toBe(0);
      expect((await db.onlineCharge.findUniqueOrThrow({ where: { id: charge.id } })).status).toBe("PENDING");
      Object.assign(fake.payments.get(paymentId)!, { status: "cancelled", status_detail: "expired" });
      expect((await POST(signed(paymentId))).status).toBe(200);
      expect((await db.onlineCharge.findUniqueOrThrow({ where: { id: charge.id } })).status).toBe("EXPIRED");
      expect(await db.manualPayment.count()).toBe(0);
    });

    it("cartão aprovado vira recebimento CARTAO; uma tentativa recusada não fecha o checkout", async () => {
      const { id } = await contractFor({ contest: "CBMPE_SOLDADO" });
      const checkout = await svc.online.startCardCheckout(id);
      const meta = { contract_id: id, charge_id: checkout.id };
      fake.payments.set("2001", { id: "2001", status: "rejected", status_detail: "cc_rejected_other_reason", transaction_amount: 40, currency_id: "BRL", external_reference: id, metadata: meta, payment_method_id: "visa" });
      expect((await POST(signed("2001"))).status).toBe(200);
      expect((await db.onlineCharge.findUniqueOrThrow({ where: { id: checkout.id } })).status).toBe("PENDING");
      fake.payments.set("2002", { id: "2002", status: "approved", status_detail: "accredited", transaction_amount: 40, currency_id: "BRL", external_reference: id, metadata: meta, payment_method_id: "master", date_approved: new Date().toISOString() });
      expect((await POST(signed("2002"))).status).toBe(200);
      const [pay] = await db.manualPayment.findMany({ where: { contractId: id } });
      expect(pay).toMatchObject({ method: "CARTAO", source: "MERCADO_PAGO" });
      expect((await reload(id)).status).toBe("PAID");
      expect((await db.onlineCharge.findUniqueOrThrow({ where: { id: checkout.id } })).status).toBe("APPROVED");
    });

    it("inscrição da lista de espera (ainda sem conta): recebe, mas o acesso continua com a aprovação do cadastro", async () => {
      const { id } = await contractFor({ withUser: false });
      const paymentId = await pixPaid(id);
      await POST(signed(paymentId));
      expect((await reload(id)).status).toBe("PAID");
      expect((await reload(id)).accessGrantedAt).toBeNull();
    });

    it("prova sem data cadastrada: recebe, registra a pendência e não libera o acesso", async () => {
      const { id } = await contractFor({ contest: "CBMPE_SOLDADO" });
      const paymentId = await pixPaid(id);
      expect((await POST(signed(paymentId))).status).toBe(200);
      expect((await reload(id)).status).toBe("PAID");
      expect((await reload(id)).accessGrantedAt).toBeNull();
      expect(await db.auditLog.count({ where: { action: "ACCESS_GRANT_PENDING", entityId: id } })).toBe(1);
    });

    it("pagamento aprovado em contratação cancelada: aviso para devolução, sem lançar nem repetir o evento", async () => {
      const { id } = await contractFor();
      const paymentId = await pixPaid(id);
      await db.contract.update({ where: { id }, data: { status: "CANCELLED", cancelledAt: new Date(), cancelReason: "teste" } });
      expect((await POST(signed(paymentId))).status).toBe(200);
      expect(await db.manualPayment.count()).toBe(0);
      expect(await db.auditLog.count({ where: { action: "PAYMENT_ON_CANCELLED_CONTRACT", entityId: id } })).toBe(1);
      await POST(signed(paymentId));
      expect(await db.auditLog.count({ where: { action: "PAYMENT_ON_CANCELLED_CONTRACT", entityId: id } })).toBe(1);
    });

    it("pagamento que não é de nenhuma contratação segue para o fluxo antigo (e nunca vira recebimento novo)", async () => {
      fake.payments.set("3001", { id: "3001", status: "approved", transaction_amount: 60, currency_id: "BRL", external_reference: "compra-antiga", date_approved: new Date().toISOString() });
      expect(await svc.online.syncProviderPayment("3001")).toBeNull();
      expect(await db.manualPayment.count()).toBe(0);
    });

    it("moeda diferente de BRL é recusada", async () => {
      const { id } = await contractFor();
      const paymentId = await pixPaid(id);
      Object.assign(fake.payments.get(paymentId)!, { currency_id: "USD" });
      await expect(svc.online.syncProviderPayment(paymentId)).rejects.toThrow(/currency/);
      expect(await db.manualPayment.count()).toBe(0);
    });
  });

  describe("liberação automática do acesso ao confirmar o pagamento", () => {
    /** inscrição da lista de espera (sem conta) com a contratação ligada a ela */
    async function waitlisted(contest: "CBMPE_OFICIAL" | "CBMPE_SOLDADO" = "CBMPE_OFICIAL", email = "lista@teste.local") {
      const entry = await db.waitlistEntry.create({ data: { contest, name: "Cliente da Lista", email, username: "lista1", plan: "UNTIL_EXAM" } });
      const r = await svc.contracts.createContract({ contest, customerEmail: email, customerName: entry.name, waitlistEntryId: entry.id }, null);
      return { entry, contractId: r.contractId };
    }

    it("inscrição quitada: cria a conta, libera até a prova e envia a senha por e-mail, uma única vez", async () => {
      const { entry, contractId } = await waitlisted();
      const paymentId = await pixPaid(contractId);
      expect((await POST(signed(paymentId))).status).toBe(200);
      await POST(signed(paymentId));
      await Promise.all([POST(signed(paymentId)), POST(signed(paymentId))]);

      const user = await db.user.findUniqueOrThrow({ where: { email: "lista@teste.local" } });
      expect(user).toMatchObject({ role: "USER", mustChangePassword: true, name: "Cliente da Lista" });
      expect(user.accessExpiresAt?.toISOString()).toBe("2027-03-01T02:59:59.999Z");
      expect(user.passwordHash).not.toContain("TESTE1"); // a senha temporária só existe no e-mail, nunca em texto puro
      expect(await db.user.count({ where: { email: "lista@teste.local" } })).toBe(1);
      expect((await reload(contractId)).userId).toBe(user.id);
      expect(await db.waitlistEntry.findUniqueOrThrow({ where: { id: entry.id } })).toMatchObject({ status: "APPROVED", accessDuration: "UNTIL_EXAM" });
      expect(mail.sent).toHaveLength(1);
      expect(mail.sent[0]).toMatchObject({ to: "lista@teste.local", accessDuration: "UNTIL_EXAM", tempPassword: "MTR-TESTE1" });
      expect(await db.auditLog.count({ where: { action: "AUTO_APPROVED", entityId: contractId } })).toBe(1);
    });

    it("prova sem data cadastrada: nada é criado e a inscrição segue pendente para o administrador", async () => {
      const { entry, contractId } = await waitlisted("CBMPE_SOLDADO");
      const paymentId = await pixPaid(contractId);
      expect((await POST(signed(paymentId))).status).toBe(200);
      expect((await reload(contractId)).status).toBe("PAID");
      expect(await db.user.count({ where: { email: "lista@teste.local" } })).toBe(0);
      expect((await db.waitlistEntry.findUniqueOrThrow({ where: { id: entry.id } })).status).toBe("PENDING");
      expect(await db.auditLog.count({ where: { action: "ACCESS_GRANT_PENDING", entityId: contractId } })).toBe(1);
      expect(mail.sent).toHaveLength(0);
    });

    it("e-mail de parceiro não é tocado (a senha dele é da administração): fica para decisão manual", async () => {
      await partner();
      const { entry, contractId } = await waitlisted("CBMPE_OFICIAL", "parceira@teste.local");
      const before = (await db.user.findUniqueOrThrow({ where: { email: "parceira@teste.local" } })).passwordHash;
      const paymentId = await pixPaid(contractId);
      expect((await POST(signed(paymentId))).status).toBe(200);
      expect((await db.user.findUniqueOrThrow({ where: { email: "parceira@teste.local" } })).passwordHash).toBe(before);
      expect((await db.waitlistEntry.findUniqueOrThrow({ where: { id: entry.id } })).status).toBe("PENDING");
      expect(await db.auditLog.count({ where: { action: "ACCESS_GRANT_PENDING", entityId: contractId } })).toBe(1);
      expect(mail.sent).toHaveLength(0);
    });

    it("se o e-mail não sair, o acesso é liberado mesmo assim e o administrador é avisado para reenviar a senha", async () => {
      mail.ok = false;
      const { contractId } = await waitlisted();
      const paymentId = await pixPaid(contractId);
      expect((await POST(signed(paymentId))).status).toBe(200);
      expect(await db.user.count({ where: { email: "lista@teste.local" } })).toBe(1);
      expect(await db.auditLog.count({ where: { action: "AUTO_APPROVAL_EMAIL_FAILED", entityId: contractId } })).toBe(1);
    });

    it("inscrição já aprovada ou rejeitada pelo administrador não é refeita pelo pagamento", async () => {
      const { entry, contractId } = await waitlisted();
      await db.waitlistEntry.update({ where: { id: entry.id }, data: { status: "REJECTED" } });
      const paymentId = await pixPaid(contractId);
      await POST(signed(paymentId));
      expect(await db.user.count({ where: { email: "lista@teste.local" } })).toBe(0);
      expect(mail.sent).toHaveLength(0);
    });
  });

  describe("estornos e contestações", () => {
    it("reembolso parcial reverte a comissão proporcionalmente e mantém o acesso; o total encerra o acesso", async () => {
      const p = await partner();
      const { id, user } = await contractFor({ coupon: p.couponCode });
      const paymentId = await pixPaid(id);
      await POST(signed(paymentId));

      Object.assign(fake.payments.get(paymentId)!, { transaction_amount_refunded: 14, date_last_updated: new Date().toISOString() });
      await POST(signed(paymentId));
      let c = await reload(id);
      expect(money(c.paidAmount)).toBe("28");
      expect(c.status).toBe("PARTIAL");
      const sum = async () => (await db.commissionEntry.findMany({ where: { contractId: id } })).reduce((s, x) => s + Number(x.amount), 0);
      expect((await sum()).toFixed(2)).toBe("8.40");
      expect(c.accessGrantedAt).not.toBeNull(); // parcial mantém o acesso
      const reversal = await db.paymentReversal.findFirstOrThrow({ where: { contractId: id } });
      expect(reversal).toMatchObject({ source: "MERCADO_PAGO", createdById: null, kind: "ESTORNO" });

      // avisos repetidos não estornam de novo
      await POST(signed(paymentId));
      expect(await db.paymentReversal.count({ where: { contractId: id } })).toBe(1);

      Object.assign(fake.payments.get(paymentId)!, { status: "refunded", status_detail: "refunded", transaction_amount_refunded: 42 });
      await POST(signed(paymentId));
      c = await reload(id);
      expect(money(c.paidAmount)).toBe("0");
      expect(Math.abs(Math.round((await sum()) * 100))).toBe(0);
      expect(c.accessGrantedAt).toBeNull();
      const u = await db.user.findUniqueOrThrow({ where: { id: user!.id } });
      expect(u.accessExpiresAt!.getTime()).toBeLessThanOrEqual(Date.now());
      expect(await db.auditLog.count({ where: { action: "ACCESS_REVOKED", entityId: id } })).toBe(1);
      expect(await db.onlineCharge.count({ where: { status: "REFUNDED" } })).toBe(1);
    });

    it("contestação em análise mantém tudo; contestação perdida reverte; ganha não reverte", async () => {
      const { id } = await contractFor();
      const paymentId = await pixPaid(id);
      await POST(signed(paymentId));
      Object.assign(fake.payments.get(paymentId)!, { status: "in_mediation", status_detail: "in_process" });
      await POST(signed(paymentId));
      expect(money((await reload(id)).paidAmount)).toBe("60");
      Object.assign(fake.payments.get(paymentId)!, { status: "charged_back", status_detail: "settled" });
      await POST(signed(paymentId));
      expect(money((await reload(id)).paidAmount)).toBe("60");
      Object.assign(fake.payments.get(paymentId)!, { status: "charged_back", status_detail: "reimbursed" });
      await POST(signed(paymentId));
      expect(money((await reload(id)).paidAmount)).toBe("0");
      expect((await db.paymentReversal.findFirstOrThrow({ where: { contractId: id } })).reason).toMatch(/Contestação/);
      expect(await db.onlineCharge.count({ where: { status: "CHARGED_BACK" } })).toBe(1);
    });
  });

  describe("recuperação de avisos perdidos e diagnóstico", () => {
    it("a reconciliação encontra o Pix pago sem ter recebido o webhook", async () => {
      const { id } = await contractFor();
      const paymentId = await pixPaid(id);
      expect(await db.manualPayment.count()).toBe(0);
      const r = await svc.online.reconcilePendingCharges({ contractId: id });
      expect(r).toMatchObject({ checked: 1, received: 1, errors: 0 });
      expect((await reload(id)).status).toBe("PAID");
      expect((await db.manualPayment.findFirstOrThrow()).providerPaymentId).toBe(paymentId);
      // nada a refazer depois de quitado
      expect((await svc.online.reconcilePendingCharges({ contractId: id })).checked).toBe(0);
    });

    it("cancelar a contratação cancela o Pix aberto no provedor", async () => {
      const { id } = await contractFor();
      const charge = await svc.online.startPixCharge(id);
      await svc.online.cancelPendingCharges(id);
      const paymentId = (await db.onlineCharge.findUniqueOrThrow({ where: { id: charge.id } })).providerPaymentId!;
      expect(fake.payments.get(paymentId)!.status).toBe("cancelled");
      expect((await db.onlineCharge.findUniqueOrThrow({ where: { id: charge.id } })).status).toBe("CANCELLED");
    });

    it("o diagnóstico detecta endereço de webhook que redireciona (o Mercado Pago não segue redirecionamento)", async () => {
      const spy = vi.spyOn(globalThis, "fetch");
      try {
        spy.mockResolvedValueOnce(new Response(null, { status: 308, headers: { location: "https://www.teste.local/api/webhooks/mercadopago" } }));
        const redirected = await svc.online.mercadoPagoAccountStatus();
        expect(redirected.webhook).toEqual({ status: 308, redirectTo: "https://www.teste.local/api/webhooks/mercadopago" });
        expect(spy.mock.calls[0][1]).toMatchObject({ method: "POST", redirect: "manual" });
        spy.mockResolvedValueOnce(new Response("{}", { status: 401 }));
        expect((await svc.online.mercadoPagoAccountStatus()).webhook).toEqual({ status: 401, redirectTo: null });
      } finally {
        spy.mockRestore();
      }
    });

    it("o diagnóstico distingue conta de empresa (CNPJ) de pessoa física (CPF) e confere o ID do vendedor, sem expor segredos", async () => {
      process.env.MERCADOPAGO_SELLER_ID = "987654";
      const company = await svc.online.mercadoPagoAccountStatus();
      expect(company.account).toMatchObject({ id: "987654", documentType: "CNPJ", matchesSellerId: true });
      expect(company.mode).toBe("producao");
      fake.me = { id: 111, nickname: "JOAO", identification: { type: "CPF" } };
      const person = await svc.online.mercadoPagoAccountStatus();
      expect(person.account).toMatchObject({ documentType: "CPF", matchesSellerId: false });
      expect(JSON.stringify(person)).not.toContain("APP_USR");
      delete process.env.MERCADOPAGO_SELLER_ID;
    });
  });
});
