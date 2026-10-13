// Integração com Postgres real (schema isolado `vitest_finance`): contratações, pagamentos manuais, saldos,
// cupons, comissões, estornos e repasses persistidos de verdade. Nenhuma cobrança ou transferência real.
import { randomUUID } from "node:crypto";
import { afterAll, beforeAll, beforeEach, describe, expect, it, vi } from "vitest";
import { hasTestDb, makeTestClient, resetTestData } from "./test-support";

vi.mock("server-only", () => ({}));
vi.mock("@/lib/db", async () => {
  const { hasTestDb: ok, makeTestClient: make } = await import("./test-support");
  return { db: ok ? make() : {} };
});

const DAY = 86_400_000;
const key = () => randomUUID();
/** meio-dia de Recife do dia `daysAgo` dias atrás (datas efetivas no passado) */
const daysAgo = (n: number) => new Date(Date.now() - n * DAY);

describe.skipIf(!hasTestDb)("financeiro com persistência real", { timeout: 60_000 }, () => {
  let db: ReturnType<typeof makeTestClient>;
  let adminId: string;
  let svc: {
    contracts: typeof import("./contracts");
    payments: typeof import("./payments");
    partners: typeof import("./partners");
  };

  beforeAll(async () => {
    db = (await import("@/lib/db")).db as unknown as ReturnType<typeof makeTestClient>;
    svc = { contracts: await import("./contracts"), payments: await import("./payments"), partners: await import("./partners") };
  });

  beforeEach(async () => {
    await resetTestData(db);
    await db.contestSetting.upsert({ where: { contest: "CBMPE_OFICIAL" }, create: { contest: "CBMPE_OFICIAL", category: "OFICIAL", examDate: new Date("2027-02-28") }, update: { category: "OFICIAL", examDate: new Date("2027-02-28") } });
    await db.contestSetting.upsert({ where: { contest: "CBMPE_SOLDADO" }, create: { contest: "CBMPE_SOLDADO", category: "PRACA", examDate: null }, update: { category: "PRACA", examDate: null } });
    await db.contestSetting.upsert({ where: { contest: "PCPE_AGENTE" }, create: { contest: "PCPE_AGENTE", category: "PCPE", examDate: new Date("2027-05-10") }, update: { category: "PCPE", examDate: new Date("2027-05-10") } });
    await db.contestSetting.upsert({ where: { contest: "PMPE_OFICIAL" }, create: { contest: "PMPE_OFICIAL", category: null }, update: { category: null, examDate: null } });
    adminId = (await db.user.create({ data: { email: "admin@teste.local", passwordHash: "x", role: "ADMIN" } })).id;
  });

  afterAll(async () => {
    if (db?.$disconnect) await db.$disconnect();
  });

  async function newPartner(username = "parceira", email = "parceira@teste.local") {
    return svc.partners.createPartner({ email, username, password: "senha-inicial-1" }, adminId);
  }
  const contract = (id: string) => db.contract.findUniqueOrThrow({ where: { id } });
  const money = (d: { toString(): string }) => d.toString();

  describe("preços e contratação", () => {
    it("Oficial R$ 90, PCPE R$ 90 e Praça R$ 60 no lançamento, com regra e preço original gravados", async () => {
      const a = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "a@x.com" }, null);
      const b = await svc.contracts.createContract({ contest: "PCPE_AGENTE", customerEmail: "b@x.com" }, null);
      const c = await svc.contracts.createContract({ contest: "CBMPE_SOLDADO", customerEmail: "c@x.com" }, null);
      const [ca, cb, cc] = await Promise.all([contract(a.contractId), contract(b.contractId), contract(c.contractId)]);
      expect([money(ca.finalAmount), money(cb.finalAmount), money(cc.finalAmount)]).toEqual(["90", "90", "60"]);
      expect([money(ca.originalAmount), money(cc.originalAmount)]).toEqual(["120", "80"]);
      expect(ca).toMatchObject({ category: "OFICIAL", launchDiscountPoints: 25, partnerDiscountPoints: 0, status: "OPEN", pricingRule: expect.stringContaining("LANCAMENTO") });
      expect(cc.category).toBe("PRACA");
    });

    it("com cupom: Oficial/PCPE R$ 42 e Praça R$ 28, e o cliente fica atribuído ao parceiro", async () => {
      const p = await newPartner();
      const o = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "o@x.com", couponCode: p.couponCode.toLowerCase() }, null);
      const s = await svc.contracts.createContract({ contest: "CBMPE_SOLDADO", customerEmail: "s@x.com", couponCode: p.couponCode }, null);
      expect(money((await contract(o.contractId)).finalAmount)).toBe("42");
      expect(money((await contract(s.contractId)).finalAmount)).toBe("28");
      expect((await contract(o.contractId))).toMatchObject({ partnerDiscountPoints: 15, partnerId: p.partnerId, couponCode: p.couponCode });
      expect(await db.partnerReferral.count({ where: { partnerId: p.partnerId } })).toBe(2);
    });

    it("concurso sem categoria vai para revisão administrativa (sem preço arbitrário)", async () => {
      await expect(svc.contracts.createContract({ contest: "PMPE_OFICIAL", customerEmail: "z@x.com" }, null)).rejects.toThrow(/revisão administrativa/);
      expect(await db.contract.count()).toBe(0);
    });

    it("data da prova indefinida: a contratação é registrada, mas o acesso até a prova fica pendente", async () => {
      const user = await db.user.create({ data: { email: "praca@x.com", passwordHash: "x", accessExpiresAt: null } });
      const r = await svc.contracts.createContract({ contest: "CBMPE_SOLDADO", customerEmail: user.email, userId: user.id }, null);
      expect((await contract(r.contractId)).examDateAtContract).toBeNull();
      await svc.payments.registerPayment({ contractId: r.contractId, amountCents: 6000, paidAt: daysAgo(1), method: "PIX", idempotencyKey: key() }, adminId);
      await expect(svc.contracts.grantAccessUntilExam(r.contractId, adminId)).rejects.toThrow(/Data da prova/);
      expect((await contract(r.contractId)).accessGrantedAt).toBeNull();
    });

    it("pedido repetido não duplica a obrigação; o preço é sempre o do servidor", async () => {
      const a = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "dup@x.com" }, null);
      const b = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "DUP@x.com" }, null);
      expect(b).toMatchObject({ contractId: a.contractId, created: false });
      expect(await db.contract.count()).toBe(1);
    });

    it("mudar a tabela de preços não altera contratações históricas", async () => {
      const a = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "hist@x.com" }, null);
      const pricing = await import("./pricing");
      const original = pricing.CATEGORY_PRICE_CENTS.OFICIAL;
      pricing.CATEGORY_PRICE_CENTS.OFICIAL = 20_000;
      try {
        const b = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "novo@x.com" }, null);
        expect(money((await contract(b.contractId)).finalAmount)).toBe("150");
        expect(money((await contract(a.contractId)).finalAmount)).toBe("90");
      } finally {
        pricing.CATEGORY_PRICE_CENTS.OFICIAL = original;
      }
    });
  });

  describe("pagamentos manuais e saldo", () => {
    it("pagamento integral quita a obrigação", async () => {
      const r = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "int@x.com" }, null);
      const p = await svc.payments.registerPayment({ contractId: r.contractId, amountCents: 9000, paidAt: daysAgo(0), method: "PIX", receiptRef: "E2E-1", idempotencyKey: key() }, adminId);
      expect(p.totals).toMatchObject({ validReceivedCents: 9000, balanceCents: 0, status: "PAID" });
      const c = await contract(r.contractId);
      expect([money(c.paidAmount), c.status]).toEqual(["90", "PAID"]);
    });

    it("três parcelas em datas diferentes: três registros, saldo recalculado a cada uma", async () => {
      const r = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "parc@x.com" }, null);
      const steps = [
        { cents: 3000, ago: 20, status: "PARTIAL", balance: 6000 },
        { cents: 1500, ago: 10, status: "PARTIAL", balance: 3500 },
        { cents: 3500, ago: 1, status: "PAID", balance: 0 },
      ];
      for (const s of steps) {
        const res = await svc.payments.registerPayment({ contractId: r.contractId, amountCents: s.cents, paidAt: daysAgo(s.ago), method: "TRANSFERENCIA", idempotencyKey: key() }, adminId);
        expect(res.totals).toMatchObject({ status: s.status, balanceCents: s.balance });
      }
      expect(await db.manualPayment.count({ where: { contractId: r.contractId } })).toBe(3);
      expect(await db.auditLog.count({ where: { action: "PAYMENT_REGISTERED", entityId: r.contractId } })).toBe(3);
    });

    it("pagamento excedente é preservado, sinalizado e não deixa saldo negativo silencioso", async () => {
      const r = await svc.contracts.createContract({ contest: "CBMPE_SOLDADO", customerEmail: "exc@x.com" }, null);
      const res = await svc.payments.registerPayment({ contractId: r.contractId, amountCents: 7000, paidAt: daysAgo(0), method: "PIX", idempotencyKey: key() }, adminId);
      expect(res.totals).toMatchObject({ status: "OVERPAID", balanceCents: -1000, validReceivedCents: 7000 });
      expect(await db.auditLog.count({ where: { action: "OVERPAYMENT_DETECTED" } })).toBe(1);
    });

    it("registro duplicado: mesma chave não duplica; mesmo comprovante é recusado", async () => {
      const r = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "dupp@x.com" }, null);
      const k = key();
      const first = await svc.payments.registerPayment({ contractId: r.contractId, amountCents: 1000, paidAt: daysAgo(0), method: "PIX", receiptRef: "E2E-X", idempotencyKey: k }, adminId);
      const again = await svc.payments.registerPayment({ contractId: r.contractId, amountCents: 1000, paidAt: daysAgo(0), method: "PIX", receiptRef: "E2E-X", idempotencyKey: k }, adminId);
      expect(again).toEqual({ paymentId: first.paymentId, duplicate: true });
      await expect(svc.payments.registerPayment({ contractId: r.contractId, amountCents: 1000, paidAt: daysAgo(0), method: "PIX", receiptRef: "e2e-x", idempotencyKey: key() }, adminId)).rejects.toThrow(/comprovante já foi lançado/);
      expect(await db.manualPayment.count()).toBe(1);
      expect(money((await contract(r.contractId)).paidAmount)).toBe("10");
    });

    it("envios simultâneos com a mesma chave geram um único lançamento", async () => {
      const r = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "conc@x.com" }, null);
      const k = key();
      const results = await Promise.allSettled([1, 2, 3].map(() => svc.payments.registerPayment({ contractId: r.contractId, amountCents: 1000, paidAt: daysAgo(0), method: "PIX", idempotencyKey: k }, adminId)));
      expect(results.map((x) => (x.status === "fulfilled" ? "ok" : String(x.reason).slice(0, 160)))).toEqual(["ok", "ok", "ok"]);
      expect(await db.manualPayment.count()).toBe(1);
      expect(money((await contract(r.contractId)).paidAmount)).toBe("10");
    });

    it("valores inválidos, futuros ou em contratação cancelada são recusados", async () => {
      const r = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "inv@x.com" }, null);
      const base = { contractId: r.contractId, paidAt: daysAgo(0), method: "PIX" as const, idempotencyKey: key() };
      await expect(svc.payments.registerPayment({ ...base, amountCents: 0 }, adminId)).rejects.toThrow(/maior que zero/);
      await expect(svc.payments.registerPayment({ ...base, amountCents: -500 }, adminId)).rejects.toThrow(/maior que zero/);
      await expect(svc.payments.registerPayment({ ...base, amountCents: 100, paidAt: new Date(Date.now() + 3 * DAY) }, adminId)).rejects.toThrow(/futuro/);
      await svc.contracts.cancelContract(r.contractId, "Cliente desistiu", adminId);
      await expect(svc.payments.registerPayment({ ...base, amountCents: 100, idempotencyKey: key() }, adminId)).rejects.toThrow(/cancelada/);
      expect(await db.manualPayment.count()).toBe(0);
    });

    it("estorno auditável: lançamento original preservado, saldo recalculado, limite do estorno respeitado", async () => {
      const r = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "est@x.com" }, null);
      const p = await svc.payments.registerPayment({ contractId: r.contractId, amountCents: 9000, paidAt: daysAgo(2), method: "PIX", idempotencyKey: key() }, adminId);
      const k = key();
      const rev = await svc.payments.reversePayment({ paymentId: p.paymentId, amountCents: 2000, kind: "CORRECAO", reason: "Valor lançado a maior", effectiveAt: daysAgo(0), idempotencyKey: k }, adminId);
      expect(rev.totals).toMatchObject({ validReceivedCents: 7000, balanceCents: 2000, status: "PARTIAL" });
      expect((await svc.payments.reversePayment({ paymentId: p.paymentId, amountCents: 2000, kind: "CORRECAO", reason: "Valor lançado a maior", effectiveAt: daysAgo(0), idempotencyKey: k }, adminId)).duplicate).toBe(true);
      await expect(svc.payments.reversePayment({ paymentId: p.paymentId, amountCents: 7001, kind: "ESTORNO", reason: "Devolução", effectiveAt: daysAgo(0), idempotencyKey: key() }, adminId)).rejects.toThrow(/excede/);
      await expect(svc.payments.reversePayment({ paymentId: p.paymentId, amountCents: 100, kind: "ESTORNO", reason: "x", effectiveAt: daysAgo(0), idempotencyKey: key() }, adminId)).rejects.toThrow(/justificativa/);
      expect(money((await db.manualPayment.findUniqueOrThrow({ where: { id: p.paymentId } })).amount)).toBe("90");
      expect(await db.auditLog.count({ where: { action: "PAYMENT_REVERSED" } })).toBe(1);
      expect(await svc.payments.reconcileContract(r.contractId)).toMatchObject({ paidAmountOk: true, statusOk: true, commissionOk: true });
    });

    it("cancelar com valores recebidos exige estorno antes", async () => {
      const r = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "canc@x.com" }, null);
      await svc.payments.registerPayment({ contractId: r.contractId, amountCents: 100, paidAt: daysAgo(0), method: "DINHEIRO", idempotencyKey: key() }, adminId);
      await expect(svc.contracts.cancelContract(r.contractId, "Teste de cancelamento", adminId)).rejects.toThrow(/estorno/);
    });

    it("acesso: pagamento parcial não libera sozinho; quitado libera até o fim do dia da prova", async () => {
      const user = await db.user.create({ data: { email: "aluno@x.com", passwordHash: "x", accessExpiresAt: new Date(Date.now() + DAY) } });
      const r = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: user.email, userId: user.id }, null);
      await svc.payments.registerPayment({ contractId: r.contractId, amountCents: 3000, paidAt: daysAgo(0), method: "PIX", idempotencyKey: key() }, adminId);
      expect((await contract(r.contractId)).accessGrantedAt).toBeNull();
      await expect(svc.contracts.grantAccessUntilExam(r.contractId, adminId)).rejects.toThrow(/saldo pendente/);
      await svc.payments.registerPayment({ contractId: r.contractId, amountCents: 3000, paidAt: daysAgo(0), method: "PIX", idempotencyKey: key() }, adminId);
      const g = await svc.contracts.grantAccessUntilExam(r.contractId, adminId);
      expect(g.until.toISOString()).toBe("2027-03-01T02:59:59.999Z"); // 28/02/2027 23:59:59,999 em Recife
      expect((await db.user.findUniqueOrThrow({ where: { id: user.id } })).accessExpiresAt?.toISOString()).toBe("2027-03-01T02:59:59.999Z");
    });

    it("liberação com saldo pendente só com justificativa (auditada)", async () => {
      const user = await db.user.create({ data: { email: "lib@x.com", passwordHash: "x", accessExpiresAt: new Date(Date.now() - DAY) } });
      const r = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: user.email, userId: user.id }, null);
      await expect(svc.contracts.grantAccessUntilExam(r.contractId, adminId, { override: true, justification: "curta" })).rejects.toThrow(/Justifique/);
      await svc.contracts.grantAccessUntilExam(r.contractId, adminId, { override: true, justification: "Pagamento combinado em duas vezes" });
      const log = await db.auditLog.findFirstOrThrow({ where: { action: "ACCESS_GRANTED", entityId: r.contractId } });
      expect(log.data).toMatchObject({ override: true, justification: "Pagamento combinado em duas vezes" });
    });

    it("saldo consolidado do usuário com mais de um concurso mantém obrigações separadas", async () => {
      const a = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "multi@x.com" }, null);
      const b = await svc.contracts.createContract({ contest: "CBMPE_SOLDADO", customerEmail: "multi@x.com" }, null);
      await svc.payments.registerPayment({ contractId: a.contractId, amountCents: 9000, paidAt: daysAgo(0), method: "PIX", idempotencyKey: key() }, adminId);
      await svc.payments.registerPayment({ contractId: b.contractId, amountCents: 1000, paidAt: daysAgo(0), method: "PIX", idempotencyKey: key() }, adminId);
      const { customerBalance } = await import("./queries");
      expect(await customerBalance("multi@x.com")).toMatchObject({ dueCents: 15_000, receivedCents: 10_000, balanceCents: 5000, contracts: 2 });
    });
  });

  describe("parceiros, cupons e comissões", () => {
    it("cadastro: senha só com hash, cupom exclusivo, e-mail existente tratado sem duplicar conta", async () => {
      const p = await newPartner("joao.s", "joao@x.com");
      const user = await db.user.findUniqueOrThrow({ where: { email: "joao@x.com" }, include: { partner: { include: { coupons: true } } } });
      expect(user.role).toBe("USER");
      expect(user.passwordHash).not.toContain("senha-inicial-1");
      expect(user.passwordHash.startsWith("scrypt$")).toBe(true);
      expect(user.partner?.coupons.map((c) => c.code)).toEqual([p.couponCode]);
      expect(p.couponCode).toBe("JOAOS15");
      const log = await db.auditLog.findFirstOrThrow({ where: { action: "PARTNER_CREATED" } });
      expect(JSON.stringify(log.data)).not.toContain("senha-inicial-1");

      await db.user.create({ data: { email: "aluno.antigo@x.com", passwordHash: "hash-antigo" } });
      await expect(svc.partners.createPartner({ email: "aluno.antigo@x.com", username: "antigo", password: "outra-senha-1" }, adminId)).rejects.toThrow(/já pertence a um usuário/);
      const linked = await svc.partners.createPartner({ email: "aluno.antigo@x.com", username: "antigo", password: "outra-senha-1", linkExisting: true }, adminId);
      expect(linked.linked).toBe(true);
      expect(await db.user.count({ where: { email: "aluno.antigo@x.com" } })).toBe(1);
      expect((await db.user.findUniqueOrThrow({ where: { email: "aluno.antigo@x.com" } })).passwordHash).toBe("hash-antigo");
      await expect(svc.partners.createPartner({ email: "aluno.antigo@x.com", username: "antigo2", password: "x".repeat(10), linkExisting: true }, adminId)).rejects.toThrow(/já está cadastrado como parceiro/);
      await expect(svc.partners.createPartner({ email: "admin@teste.local", username: "adm", password: "x".repeat(10), linkExisting: true }, adminId)).rejects.toThrow(/administrador/);
    });

    it("cupom inválido, desativado, de parceiro desativado e autoindicação são recusados", async () => {
      const p = await newPartner();
      await expect(svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "c1@x.com", couponCode: "NAOEXISTE" }, null)).rejects.toThrow(/Cupom inválido/);
      await expect(svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "parceira@teste.local", couponCode: p.couponCode }, null)).rejects.toThrow(/próprio parceiro/);
      const coupon = await db.partnerCoupon.findFirstOrThrow({ where: { partnerId: p.partnerId } });
      await svc.partners.setCouponActive(coupon.id, false, adminId);
      await expect(svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "c2@x.com", couponCode: p.couponCode }, null)).rejects.toThrow(/Cupom inválido/);
      await svc.partners.setCouponActive(coupon.id, true, adminId);
      await svc.partners.setPartnerActive(p.partnerId, false, adminId);
      await expect(svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "c3@x.com", couponCode: p.couponCode }, null)).rejects.toThrow(/Cupom inválido/);
      expect(await db.contract.count()).toBe(0);
    });

    it("compra sem cupom não gera atribuição nem comissão", async () => {
      await newPartner();
      const r = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "semcupom@x.com" }, null);
      await svc.payments.registerPayment({ contractId: r.contractId, amountCents: 9000, paidAt: daysAgo(0), method: "PIX", idempotencyKey: key() }, adminId);
      expect(await db.partnerReferral.count()).toBe(0);
      expect(await db.commissionEntry.count()).toBe(0);
    });

    it("primeiro vínculo é mantido; cupom trocado antes do pagamento substitui a obrigação sem transferir a indicação", async () => {
      const a = await newPartner("parceiroa", "pa@x.com");
      const b = await newPartner("parceirob", "pb@x.com");
      const r1 = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "cli@x.com", couponCode: a.couponCode }, null);
      const r2 = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "cli@x.com", couponCode: b.couponCode }, null);
      expect(r2.replacedId).toBe(r1.contractId);
      expect((await contract(r1.contractId)).status).toBe("CANCELLED");
      expect((await contract(r2.contractId)).partnerId).toBe(b.partnerId);
      const ref = await db.partnerReferral.findUniqueOrThrow({ where: { customerEmail: "cli@x.com" } });
      expect(ref.partnerId).toBe(a.partnerId);
      await svc.payments.registerPayment({ contractId: r2.contractId, amountCents: 100, paidAt: daysAgo(0), method: "PIX", idempotencyKey: key() }, adminId);
      await expect(svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "cli@x.com", couponCode: a.couponCode }, null)).rejects.toThrow(/não pode mais ser alterado/);
    });

    it("comissão de 30% sobre pagamento integral: R$ 12,60 (Oficial) e R$ 8,40 (Praça)", async () => {
      const p = await newPartner();
      const o = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "o@x.com", couponCode: p.couponCode }, null);
      const s = await svc.contracts.createContract({ contest: "CBMPE_SOLDADO", customerEmail: "s@x.com", couponCode: p.couponCode }, null);
      const po = await svc.payments.registerPayment({ contractId: o.contractId, amountCents: 7200, paidAt: daysAgo(0), method: "PIX", idempotencyKey: key() }, adminId);
      await svc.payments.registerPayment({ contractId: s.contractId, amountCents: 4800, paidAt: daysAgo(0), method: "PIX", idempotencyKey: key() }, adminId);
      const entries = await db.commissionEntry.findMany({ orderBy: { createdAt: "asc" } });
      expect(entries.map((e) => money(e.amount))).toEqual(["21.6", "14.4"]);
      expect(entries[0]).toMatchObject({ kind: "ACCRUAL", paymentId: po.paymentId, contractId: o.contractId, partnerId: p.partnerId, rateBp: 3000 });
    });

    it("comissão proporcional em parcelas: a soma das parcelas é exatamente 30% do recebido", async () => {
      const p = await newPartner();
      const r = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "p3@x.com", couponCode: p.couponCode }, null);
      const parts = [1001, 1001, 5198];
      for (const cents of parts) await svc.payments.registerPayment({ contractId: r.contractId, amountCents: cents, paidAt: daysAgo(0), method: "PIX", idempotencyKey: key() }, adminId);
      const entries = await db.commissionEntry.findMany({ where: { contractId: r.contractId }, orderBy: { createdAt: "asc" } });
      expect(entries).toHaveLength(3);
      expect(entries.map((e) => money(e.amount))).toEqual(["3", "3.01", "15.59"]);
      expect(entries.reduce((s, e) => s + Math.round(Number(e.amount) * 100), 0)).toBe(2160);
      // só o que foi recebido gera comissão: com 1 parcela paga, nada além de 30% dela
      const r2 = await svc.contracts.createContract({ contest: "CBMPE_SOLDADO", customerEmail: "p4@x.com", couponCode: p.couponCode }, null);
      await svc.payments.registerPayment({ contractId: r2.contractId, amountCents: 1000, paidAt: daysAgo(0), method: "PIX", idempotencyKey: key() }, adminId);
      expect(money((await db.commissionEntry.findFirstOrThrow({ where: { contractId: r2.contractId } })).amount)).toBe("3");
    });

    it("excedente pago a mais não gera comissão extra", async () => {
      const p = await newPartner();
      const r = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "ex@x.com", couponCode: p.couponCode }, null);
      await svc.payments.registerPayment({ contractId: r.contractId, amountCents: 9500, paidAt: daysAgo(0), method: "PIX", idempotencyKey: key() }, adminId);
      expect(money((await db.commissionEntry.aggregate({ where: { contractId: r.contractId }, _sum: { amount: true } }))._sum.amount!)).toBe("21.6");
    });

    it("estorno reverte a comissão proporcionalmente, sem reversão duplicada", async () => {
      const p = await newPartner();
      const r = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "rev@x.com", couponCode: p.couponCode }, null);
      const pay = await svc.payments.registerPayment({ contractId: r.contractId, amountCents: 7200, paidAt: daysAgo(30), method: "PIX", idempotencyKey: key() }, adminId);
      const k = key();
      const input = { paymentId: pay.paymentId, amountCents: 3600, kind: "ESTORNO" as const, reason: "Devolução parcial ao cliente", effectiveAt: daysAgo(0), idempotencyKey: k };
      const first = await svc.payments.reversePayment(input, adminId);
      await svc.payments.reversePayment(input, adminId);
      const rev = await db.commissionEntry.findMany({ where: { kind: "REVERSAL" } });
      expect(rev).toHaveLength(1);
      expect(rev[0]).toMatchObject({ reversalId: first.reversalId, paymentId: pay.paymentId });
      expect(money(rev[0].amount)).toBe("-10.8");
      const bal = await svc.partners.partnerBalance(p.partnerId);
      expect(bal).toMatchObject({ generatedCents: 2160, reversedCents: 1080, availableCents: 1080, negativeCents: 0 });
    });

    it("comissão fica pendente durante a garantia e depois disponível", async () => {
      const p = await newPartner();
      const r = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "pend@x.com", couponCode: p.couponCode }, null);
      await svc.payments.registerPayment({ contractId: r.contractId, amountCents: 7200, paidAt: daysAgo(2), method: "PIX", idempotencyKey: key() }, adminId);
      expect(await svc.partners.partnerBalance(p.partnerId)).toMatchObject({ pendingCents: 2160, availableCents: 0 });
      expect(await svc.partners.partnerBalance(p.partnerId, new Date(Date.now() + 6 * DAY))).toMatchObject({ pendingCents: 0, availableCents: 2160 });
    });

    it("repasse válido, repasse acima do saldo recusado e compensação de saldo negativo", async () => {
      const p = await newPartner();
      const r = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "rep@x.com", couponCode: p.couponCode }, null);
      const pay = await svc.payments.registerPayment({ contractId: r.contractId, amountCents: 7200, paidAt: daysAgo(30), method: "PIX", idempotencyKey: key() }, adminId);
      await expect(svc.partners.registerPayout({ partnerId: p.partnerId, amountCents: 2161, paidAt: daysAgo(0), method: "Pix", idempotencyKey: key() }, adminId)).rejects.toThrow(/acima do saldo/);
      const k = key();
      await svc.partners.registerPayout({ partnerId: p.partnerId, amountCents: 2160, paidAt: daysAgo(0), method: "Pix", receiptRef: "REP-1", idempotencyKey: k }, adminId);
      expect((await svc.partners.registerPayout({ partnerId: p.partnerId, amountCents: 2160, paidAt: daysAgo(0), method: "Pix", idempotencyKey: k }, adminId)).duplicate).toBe(true);
      expect(await db.partnerPayout.count()).toBe(1);
      // estorno total depois do repasse: saldo negativo a compensar
      await svc.payments.reversePayment({ paymentId: pay.paymentId, amountCents: 7200, kind: "ESTORNO", reason: "Cliente usou a garantia", effectiveAt: daysAgo(0), idempotencyKey: key() }, adminId);
      expect(await svc.partners.partnerBalance(p.partnerId)).toMatchObject({ availableCents: 0, negativeCents: 2160, paidOutCents: 2160 });
      await expect(svc.partners.registerPayout({ partnerId: p.partnerId, amountCents: 1, paidAt: daysAgo(0), method: "Pix", idempotencyKey: key() }, adminId)).rejects.toThrow(/acima do saldo/);
      // novas comissões compensam primeiro o negativo
      const r2 = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "rep2@x.com", couponCode: p.couponCode }, null);
      await svc.payments.registerPayment({ contractId: r2.contractId, amountCents: 7200, paidAt: daysAgo(30), method: "PIX", idempotencyKey: key() }, adminId);
      const r3 = await svc.contracts.createContract({ contest: "CBMPE_SOLDADO", customerEmail: "rep3@x.com", couponCode: p.couponCode }, null);
      await svc.payments.registerPayment({ contractId: r3.contractId, amountCents: 4800, paidAt: daysAgo(30), method: "PIX", idempotencyKey: key() }, adminId);
      expect(await svc.partners.partnerBalance(p.partnerId)).toMatchObject({ negativeCents: 0, availableCents: 1440 });
    });

    it("desativação bloqueia sessões; o histórico (cupons, indicações, comissões) permanece", async () => {
      const p = await newPartner();
      const partner = await db.partner.findUniqueOrThrow({ where: { id: p.partnerId } });
      await db.session.create({ data: { userId: partner.userId, tokenHash: "hash-sessao", expiresAt: new Date(Date.now() + DAY) } });
      const r = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "hist2@x.com", couponCode: p.couponCode }, null);
      await svc.payments.registerPayment({ contractId: r.contractId, amountCents: 7200, paidAt: daysAgo(0), method: "PIX", idempotencyKey: key() }, adminId);
      await svc.partners.setPartnerActive(p.partnerId, false, adminId);
      expect(await db.session.count({ where: { userId: partner.userId } })).toBe(0);
      expect(await db.partnerCoupon.count({ where: { partnerId: p.partnerId } })).toBe(1);
      expect(await db.partnerReferral.count({ where: { partnerId: p.partnerId } })).toBe(1);
      expect(await db.commissionEntry.count({ where: { partnerId: p.partnerId } })).toBe(1);
    });

    it("substituir o cupom preserva o histórico e não transfere indicações", async () => {
      const p = await newPartner();
      await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "antes@x.com", couponCode: p.couponCode }, null);
      const novo = await svc.partners.replacePartnerCoupon(p.partnerId, "NOVOCUPOM", adminId);
      expect(novo).toBe("NOVOCUPOM");
      await expect(svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "depois@x.com", couponCode: p.couponCode }, null)).rejects.toThrow(/Cupom inválido/);
      const r = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "depois@x.com", couponCode: "novocupom" }, null);
      expect((await contract(r.contractId)).couponCode).toBe("NOVOCUPOM");
      const old = await db.contract.findFirstOrThrow({ where: { customerEmail: "antes@x.com" } });
      expect(old.couponCode).toBe(p.couponCode);
      await expect(svc.partners.replacePartnerCoupon(p.partnerId, p.couponCode, adminId)).rejects.toThrow(/não são reaproveitados/);
    });

    it("isolamento: o painel de cada parceiro só enxerga os próprios números, sem dados pessoais", async () => {
      const a = await newPartner("parca", "a@p.com");
      const b = await newPartner("parcb", "b@p.com");
      const ra = await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "cliente.a@x.com", couponCode: a.couponCode }, null);
      await svc.contracts.createContract({ contest: "CBMPE_OFICIAL", customerEmail: "cliente.b@x.com", couponCode: b.couponCode }, null);
      await svc.contracts.createContract({ contest: "CBMPE_SOLDADO", customerEmail: "cliente.b2@x.com", couponCode: b.couponCode }, null);
      await svc.payments.registerPayment({ contractId: ra.contractId, amountCents: 7200, paidAt: daysAgo(0), method: "PIX", idempotencyKey: key() }, adminId);
      const { partnerDashboard } = await import("./queries");
      const userA = (await db.partner.findUniqueOrThrow({ where: { id: a.partnerId } })).userId;
      const dash = await partnerDashboard(userA);
      expect(dash).toMatchObject({ referredUsers: 1, payingUsers: 1, contracts: 1, receivedCents: 7200, balance: { generatedCents: 2160 } });
      expect(JSON.stringify(dash)).not.toContain("cliente.");
      expect(JSON.stringify(dash)).not.toContain("@");
      const userB = (await db.partner.findUniqueOrThrow({ where: { id: b.partnerId } })).userId;
      expect(await partnerDashboard(userB)).toMatchObject({ referredUsers: 2, payingUsers: 0, receivedCents: 0 });
      // usuário comum (não parceiro) não tem painel
      const common = await db.user.create({ data: { email: "comum@x.com", passwordHash: "x" } });
      expect(await partnerDashboard(common.id)).toBeNull();
    });
  });
});
