import { describe, expect, it } from "vitest";
import { isPlan, PLAN_KEYS, WAITLIST_PLANS } from "./plans";

describe("planos da lista de espera", () => {
  it("define Mensalidade (R$ 30) e Acesso até a prova (R$ 50) com valor no formato do Pix", () => {
    expect([...PLAN_KEYS].sort()).toEqual(["MONTHLY", "UNTIL_EXAM"]);
    expect(WAITLIST_PLANS.MONTHLY.amount).toBe("30.00");
    expect(WAITLIST_PLANS.UNTIL_EXAM.amount).toBe("50.00");
  });
  it("o valor do Pix (ponto) e o de exibição (vírgula) descrevem o mesmo número", () => {
    for (const p of Object.values(WAITLIST_PLANS)) {
      expect(p.amount).toMatch(/^\d+\.\d{2}$/);
      expect(Number(p.amount)).toBe(Number(p.price.replace(",", ".")));
      expect(WAITLIST_PLANS[p.key]).toBe(p);
    }
  });
  it("isPlan aceita só as chaves conhecidas", () => {
    expect(isPlan("MONTHLY")).toBe(true);
    expect(isPlan("UNTIL_EXAM")).toBe(true);
    expect(isPlan("monthly")).toBe(false);
    expect(isPlan("")).toBe(false);
    expect(isPlan(undefined)).toBe(false);
    expect(isPlan(30)).toBe(false);
    expect(isPlan(null)).toBe(false);
  });
  // `v in WAITLIST_PLANS` enxerga o protótipo de Object: nomes herdados passam como se fossem planos
  it("isPlan rejeita nomes herdados do protótipo de Object", () => {
    expect(isPlan("toString")).toBe(false);
    expect(isPlan("constructor")).toBe(false);
    expect(isPlan("__proto__")).toBe(false);
  });
});
