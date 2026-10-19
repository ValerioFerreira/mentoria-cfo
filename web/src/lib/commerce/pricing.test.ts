import { describe, expect, it } from "vitest";
import { summarizeLedger } from "./ledger";
import { formatBRL, fromCents, parseMoneyInput, toCents } from "./money";
import { allocateDiscountPoints, accessEndForExamDate, commissionOn, commissionTarget, financialStatus, priceCardText, quote } from "./pricing";
import { couponSetKey, parseCouponCodes } from "./coupon-codes";

describe("preços por categoria", () => {
  it("lançamento: Oficial e PCPE R$ 90,00; Praça R$ 60,00", () => {
    expect(quote("OFICIAL")).toMatchObject({ originalCents: 12_000, launchDiscountPoints: 25, partnerDiscountPoints: 0, finalCents: 9_000, discountCents: 3_000 });
    expect(quote("PCPE").finalCents).toBe(9_000);
    expect(quote("PRACA")).toMatchObject({ originalCents: 8_000, finalCents: 6_000 });
  });
  it("cupom de parceiro soma 15 p.p.: R$ 72,00 e R$ 48,00", () => {
    expect(quote("OFICIAL", 15)).toMatchObject({ partnerDiscountPoints: 15, finalCents: 7_200, discountCents: 4_800 });
    expect(quote("PCPE", 15).finalCents).toBe(7_200);
    expect(quote("PRACA", 15).finalCents).toBe(4_800);
  });
  it("preço e desconto do site definidos no concurso substituem o padrão", () => {
    expect(quote("OFICIAL", 0, { priceCents: 15_000, siteDiscountPoints: 20 })).toMatchObject({ originalCents: 15_000, launchDiscountPoints: 20, finalCents: 12_000 });
    expect(quote("OFICIAL", 15, { priceCents: 15_000, siteDiscountPoints: 20 })).toMatchObject({ partnerDiscountPoints: 15, finalCents: 9_750 });
    expect(quote("PRACA", 0, { siteDiscountPoints: 0 }).finalCents).toBe(8_000);
    expect(quote("PRACA", 0, { priceCents: null, siteDiscountPoints: null }).finalCents).toBe(6_000);
    expect(quote("OFICIAL", 0, { priceCents: 9_000 }).pricingRule).toMatch(/CONFIG-CONCURSO/);
    expect(() => quote("OFICIAL", 0, { siteDiscountPoints: 101 })).toThrow();
    expect(() => quote("OFICIAL", 0, { priceCents: 0 })).toThrow();
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
    expect(quote("OFICIAL", 80)).toMatchObject({ partnerDiscountPoints: 75, finalCents: 0 });
  });
  it("textos do card vêm do cálculo do servidor", () => {
    expect(priceCardText(quote("OFICIAL"))).toEqual({ badge: "25% OFF · lançamento", original: "De R$ 120,00", final: "R$ 90,00" });
    expect(priceCardText(quote("PRACA"))).toEqual({ badge: "25% OFF · lançamento", original: "De R$ 80,00", final: "R$ 60,00" });
  });
});

describe("cupons do site: descontos aditivos sobre o valor original", () => {
  // preço original R$ 100,00 e sem desconto de lançamento, para isolar a regra dos cupons
  const base = { priceCents: 10_000, siteDiscountPoints: 0 };
  it("um cupom de 25% sobre R$ 100 resulta em R$ 75", () => {
    expect(quote("OFICIAL", 0, base, [25])).toMatchObject({ originalCents: 10_000, couponDiscountPoints: 25, couponAppliedPoints: [25], discountCents: 2_500, finalCents: 7_500 });
  });
  it("25% + 10% somam 35% do valor original: R$ 65, nunca 10% sobre os R$ 75", () => {
    const q = quote("OFICIAL", 0, base, [25, 10]);
    expect(q).toMatchObject({ couponDiscountPoints: 35, couponAppliedPoints: [25, 10], discountCents: 3_500, finalCents: 6_500 });
    expect(q.finalCents).not.toBe(6_750); // cascata (75 − 10% de 75) seria errado
  });
  it("a ordem dos cupons não muda o resultado", () => {
    expect(quote("OFICIAL", 0, base, [10, 25]).finalCents).toBe(quote("OFICIAL", 0, base, [25, 10]).finalCents);
  });
  it("soma com o desconto de lançamento e com o cupom de parceiro, sempre sobre o original", () => {
    // R$ 120: 25% lançamento + 15% parceiro + 10% cupom = 50% => R$ 60
    expect(quote("OFICIAL", 15, undefined, [10])).toMatchObject({ launchDiscountPoints: 25, partnerDiscountPoints: 15, couponDiscountPoints: 10, finalCents: 6_000, discountCents: 6_000 });
    // sem cupom do site o comportamento anterior continua igual
    expect(quote("OFICIAL", 15).finalCents).toBe(7_200);
    expect(quote("OFICIAL", 15, undefined, []).finalCents).toBe(7_200);
  });
  it("o total de desconto nunca passa de 100% (preço mínimo R$ 0)", () => {
    const q = quote("OFICIAL", 0, base, [60, 60, 30]);
    expect(q).toMatchObject({ couponDiscountPoints: 100, couponAppliedPoints: [60, 40, 0], finalCents: 0, discountCents: 10_000 });
    expect(quote("OFICIAL", 15, undefined, [100]).finalCents).toBe(0);
    expect(quote("OFICIAL", 15, undefined, [100]).partnerDiscountPoints).toBe(15);
    expect(quote("OFICIAL", 0, { siteDiscountPoints: 100 }, [10])).toMatchObject({ couponDiscountPoints: 0, finalCents: 0 });
  });
  it("arredonda ao centavo uma única vez, no total (meio para cima)", () => {
    // R$ 100,01 com 33% => 67,0067 => R$ 67,01
    expect(quote("OFICIAL", 0, { priceCents: 10_001, siteDiscountPoints: 0 }, [33]).finalCents).toBe(6_701);
    expect(quote("OFICIAL", 0, { priceCents: 999, siteDiscountPoints: 0 }, [10, 15]).finalCents).toBe(749); // 749,25
  });
  it("percentuais inválidos são recusados", () => {
    for (const bad of [-1, 101, 7.5, Number.NaN]) expect(() => quote("OFICIAL", 0, base, [bad])).toThrow(/inválido/);
  });
  it("regra gravada e texto do card indicam os cupons", () => {
    expect(quote("OFICIAL", 0, undefined, [10]).pricingRule).toMatch(/\+CUPONS-SITE$/);
    expect(quote("OFICIAL").pricingRule).not.toMatch(/CUPONS/);
    expect(priceCardText(quote("OFICIAL", 0, undefined, [10])).badge).toBe("35% OFF · lançamento + cupom");
    expect(priceCardText(quote("OFICIAL", 15, undefined, [10])).badge).toBe("50% OFF · lançamento + cupons");
    expect(priceCardText(quote("OFICIAL", 0, undefined, [10, 5])).badge).toBe("40% OFF · lançamento + cupons");
  });
  it("allocateDiscountPoints limita a soma a 100 na ordem dada", () => {
    expect(allocateDiscountPoints([25, 10])).toEqual({ applied: [25, 10], total: 35 });
    expect(allocateDiscountPoints([70, 50, 20])).toEqual({ applied: [70, 30, 0], total: 100 });
    expect(allocateDiscountPoints([])).toEqual({ applied: [], total: 0 });
  });
});

describe("códigos de cupom informados pelo cliente", () => {
  it("aceita vários códigos separados por espaço, vírgula, ponto e vírgula ou quebra de linha, em maiúsculas", () => {
    expect(parseCouponCodes(" ab12cd,  XY99 ;novo2027\nfim1 ")).toEqual(["AB12CD", "XY99", "NOVO2027", "FIM1"]);
    expect(parseCouponCodes("")).toEqual([]);
    expect(parseCouponCodes(undefined)).toEqual([]);
    expect(parseCouponCodes(null)).toEqual([]);
  });
  it("recusa código repetido (mesmo com caixa diferente) e mais de 5 cupons", () => {
    expect(() => parseCouponCodes("abcd ABCD")).toThrow(/mais de uma vez/);
    expect(() => parseCouponCodes("AAAA BBBB CCCC DDDD EEEE FFFF")).toThrow(/no máximo 5/);
    expect(parseCouponCodes("AAAA BBBB CCCC DDDD EEEE")).toHaveLength(5);
  });
  it("conjuntos de cupons são comparados sem depender da ordem", () => {
    expect(couponSetKey(["B", "A"])).toBe(couponSetKey(["A", "B"]));
    expect(couponSetKey([null, "A", undefined])).toBe("A");
    expect(couponSetKey([])).toBe("");
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
