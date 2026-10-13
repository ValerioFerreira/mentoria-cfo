import { describe, expect, it } from "vitest";
import { summarizeLedger } from "./ledger";
import { formatBRL, fromCents, parseMoneyInput, toCents } from "./money";
import { accessEndForExamDate, commissionOn, commissionTarget, financialStatus, priceCardText, quote } from "./pricing";

describe("preços por categoria", () => {
  it("lançamento: Oficial e PCPE R$ 60,00; Praça R$ 40,00", () => {
    expect(quote("OFICIAL")).toMatchObject({ originalCents: 12_000, launchDiscountPoints: 50, partnerDiscountPoints: 0, finalCents: 6_000, discountCents: 6_000 });
    expect(quote("PCPE").finalCents).toBe(6_000);
    expect(quote("PRACA")).toMatchObject({ originalCents: 8_000, finalCents: 4_000 });
  });
  it("cupom de parceiro soma 15 p.p.: R$ 42,00 e R$ 28,00", () => {
    expect(quote("OFICIAL", 15)).toMatchObject({ partnerDiscountPoints: 15, finalCents: 4_200, discountCents: 7_800 });
    expect(quote("PCPE", 15).finalCents).toBe(4_200);
    expect(quote("PRACA", 15).finalCents).toBe(2_800);
  });
  it("categoria ausente ou inválida não tem preço", () => {
    expect(() => quote(null)).toThrow(/revisão administrativa/);
    expect(() => quote(undefined)).toThrow(/revisão administrativa/);
    expect(() => quote("SOLDADO" as never)).toThrow(/revisão administrativa/);
  });
  it("descontos manipulados são recusados e o total nunca passa de 100%", () => {
    expect(() => quote("OFICIAL", -10)).toThrow(/inválido/);
    expect(() => quote("OFICIAL", 101)).toThrow(/inválido/);
    expect(() => quote("OFICIAL", 7.5)).toThrow(/inválido/);
    expect(quote("OFICIAL", 80)).toMatchObject({ partnerDiscountPoints: 50, finalCents: 0 });
  });
  it("textos do card vêm do cálculo do servidor", () => {
    expect(priceCardText(quote("OFICIAL"))).toEqual({ badge: "50% OFF · lançamento", original: "De R$ 120,00", final: "R$ 60,00" });
    expect(priceCardText(quote("PRACA"))).toEqual({ badge: "50% OFF · lançamento", original: "De R$ 80,00", final: "R$ 40,00" });
  });
});

describe("comissão e situação financeira", () => {
  it("30% do valor pago: R$ 12,60 e R$ 8,40", () => {
    expect(commissionOn(4_200)).toBe(1_260);
    expect(commissionOn(2_800)).toBe(840);
    expect(commissionOn(0)).toBe(0);
    expect(commissionOn(-100)).toBe(0);
  });
  it("arredondamento meio para cima ao centavo e soma das parcelas igual ao total", () => {
    expect(commissionOn(1_001)).toBe(300); // 300,3
    expect(commissionOn(5)).toBe(2); // 1,5 -> 2
    const parcels = [1_001, 1_001, 2_198];
    let cum = 0;
    let sum = 0;
    for (const p of parcels) {
      const before = commissionTarget(cum, 4_200);
      cum += p;
      sum += commissionTarget(cum, 4_200) - before;
    }
    expect(sum).toBe(commissionOn(4_200));
  });
  it("excedente não gera comissão", () => {
    expect(commissionTarget(5_000, 4_200)).toBe(1_260);
  });
  it("situação: aberta, parcial, quitada e excedente", () => {
    expect(financialStatus(0, 6_000)).toBe("OPEN");
    expect(financialStatus(1, 6_000)).toBe("PARTIAL");
    expect(financialStatus(6_000, 6_000)).toBe("PAID");
    expect(financialStatus(6_001, 6_000)).toBe("OVERPAID");
  });
  it("acesso vale até 23:59:59 do dia da prova em Recife", () => {
    expect(accessEndForExamDate(new Date("2027-02-28")).toISOString()).toBe("2027-03-01T02:59:59.999Z");
  });
});

describe("dinheiro em centavos", () => {
  it("converte Decimal/texto/número sem erro de ponto flutuante", () => {
    expect(toCents("42")).toBe(4_200);
    expect(toCents("12.6")).toBe(1_260);
    expect(toCents("0.07")).toBe(7);
    expect(toCents(0.1 + 0.2)).toBe(30);
    expect(toCents("-6.3")).toBe(-630);
    expect(fromCents(4_200)).toBe("42.00");
    expect(fromCents(-630)).toBe("-6.30");
    expect(formatBRL(123_456)).toBe("R$ 1.234,56");
  });
  it("entrada do formulário: aceita formatos brasileiros e recusa negativos e lixo", () => {
    expect(parseMoneyInput("42")).toBe(4_200);
    expect(parseMoneyInput("42,5")).toBe(4_250);
    expect(parseMoneyInput("1.234,56")).toBe(123_456);
    expect(parseMoneyInput("R$ 60,00")).toBe(6_000);
    for (const bad of ["-10", "abc", "", "1,234", "10,001", undefined]) expect(parseMoneyInput(bad)).toBeNull();
  });
});

describe("saldo do parceiro", () => {
  const now = new Date("2026-10-20T12:00:00Z");
  const past = new Date("2026-10-01T12:00:00Z");
  const future = new Date("2026-10-25T12:00:00Z");
  it("separa gerado, revertido, pendente, disponível e repassado", () => {
    const b = summarizeLedger([{ amountCents: 1_260, availableAt: past }, { amountCents: 840, availableAt: future }, { amountCents: -630, availableAt: past }], [300], now);
    expect(b).toEqual({ generatedCents: 2_100, reversedCents: 630, paidOutCents: 300, pendingCents: 840, availableCents: 330, negativeCents: 0 });
  });
  it("reversão depois do repasse vira saldo negativo, compensado pelas próximas comissões", () => {
    const after = summarizeLedger([{ amountCents: 1_260, availableAt: past }, { amountCents: -1_260, availableAt: past }], [1_260], now);
    expect(after).toMatchObject({ availableCents: 0, negativeCents: 1_260 });
    const later = summarizeLedger([{ amountCents: 1_260, availableAt: past }, { amountCents: -1_260, availableAt: past }, { amountCents: 2_100, availableAt: past }], [1_260], now);
    expect(later).toMatchObject({ availableCents: 840, negativeCents: 0 });
  });
});
