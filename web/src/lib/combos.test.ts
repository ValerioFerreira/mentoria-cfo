import { describe, expect, it } from "vitest";
import { COMBOS, comboMembers, comboWeights, defaultPriority, isCombo, isValidPriority, mergeComboImportance, mergeComboQuestions } from "./combos";
import { CONTEST_SUBJECTS, editalItemApplies, packageFor } from "./contests";
import { contestBancas, usesReinforcement } from "./quiz/banca";
import { quote } from "./commerce/pricing";

describe("combos", () => {
  it("reconhece os combos e seus membros (Oficial primeiro)", () => {
    expect(isCombo("CBMPE_COMBO")).toBe(true);
    expect(isCombo("CBMPE_OFICIAL")).toBe(false);
    expect(comboMembers("PMPE_COMBO")).toEqual(["PMPE_OFICIAL", "PMPE_SOLDADO"]);
    expect(comboMembers("CBMPE_OFICIAL")).toEqual(["CBMPE_OFICIAL"]);
    expect(defaultPriority("CBMPE_COMBO")).toBe("CBMPE_OFICIAL");
  });

  it("peso 2:1: o prioritário vale 1 e o outro 0,5; prioridade inválida cai no Oficial", () => {
    expect(comboWeights("CBMPE_COMBO", "CBMPE_SOLDADO")).toEqual([
      { contest: "CBMPE_OFICIAL", weight: 0.5 },
      { contest: "CBMPE_SOLDADO", weight: 1 },
    ]);
    expect(comboWeights("CBMPE_COMBO", "PMPE_SOLDADO")[0].weight).toBe(1);
    expect(isValidPriority("PMPE_COMBO", "PMPE_SOLDADO")).toBe(true);
    expect(isValidPriority("PMPE_COMBO", "CBMPE_SOLDADO")).toBe(false);
  });

  it("disciplinas do combo = união dos membros", () => {
    for (const key of Object.keys(COMBOS) as (keyof typeof COMBOS)[]) {
      const union = new Set([...CONTEST_SUBJECTS[COMBOS[key].oficial], ...CONTEST_SUBJECTS[COMBOS[key].praca]]);
      expect(new Set(CONTEST_SUBJECTS[key])).toEqual(union);
    }
  });

  it("peso combinado W = Σ peso × questões", () => {
    const w = mergeComboQuestions([
      { weight: 1, examQuestions: { a: 5, b: 5 } },
      { weight: 0.5, examQuestions: { a: 10, c: 10 } },
    ]);
    expect(w).toEqual({ a: 10, b: 5, c: 5 });
  });

  it("edital da união: fora só quando não aparece em nenhum; nota é percentil das questões esperadas ponderadas", () => {
    const merged = mergeComboImportance([
      { weight: 1, importance: { x: 10, y: 20, z: null, w: null }, expected: { x: 0.1, y: 0.4, z: 0.9, w: 0 } },
      { weight: 0.5, importance: { x: 5, y: null, z: 7, w: null }, expected: { x: 0.1, y: 0.9, z: 0.2, w: 0 } },
    ]);
    expect(merged.w).toBeNull();
    // valores: x = 0,1 + 0,05 = 0,15 · y = 0,4 · z = 0,1 (só o 2º membro conta)
    expect(merged.y).toBe(100);
    expect(merged.z!).toBeLessThan(merged.x!);
    expect(merged.x!).toBeLessThan(merged.y!);
    for (const v of Object.values(merged)) if (v !== null) expect(v).toBeGreaterThanOrEqual(1);
  });

  it("assunto do edital vale no combo se vale para qualquer membro", () => {
    expect(editalItemApplies({ onlyContests: ["CBMPE_SOLDADO"] }, "CBMPE_COMBO")).toBe(true);
    expect(editalItemApplies({ onlyContests: ["PCPE_AGENTE"] }, "CBMPE_COMBO")).toBe(false);
  });

  it("material de referência pelo membro que tem a disciplina (Oficial primeiro)", () => {
    expect(packageFor("CBMPE_COMBO", "lingua-portuguesa")?.name).toContain("Oficial");
    expect(packageFor("CBMPE_COMBO", "atualidades")?.name).toContain("Soldado");
    expect(packageFor(null, "informatica")?.name).toContain("Oficial");
  });

  it("bancas e reforço: combo CBMPE usa reforço (o Oficial usa); combo PMPE não", () => {
    expect(contestBancas("CBMPE_COMBO")).toEqual(contestBancas("CBMPE_OFICIAL"));
    expect(usesReinforcement("CBMPE_COMBO")).toBe(true);
    expect(usesReinforcement("PMPE_COMBO")).toBe(false);
  });

  it("preço: R$ 160 → R$ 120 no lançamento → R$ 96 com cupom de parceiro", () => {
    expect(quote("COMBO").finalCents).toBe(12_000);
    expect(quote("COMBO", 15).finalCents).toBe(9_600);
  });
});
