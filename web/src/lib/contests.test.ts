import { describe, expect, it } from "vitest";
import { CONTEST_SUBTITLES, CONTESTS, contestBySlug, contestTitle, editalItemApplies } from "./contests";

describe("concursos", () => {
  it("concursos disponíveis (inclui os combos e o Agente da PCPE)", () => {
    expect(CONTESTS.filter((c) => c.available).map((c) => c.key)).toEqual([
      "CBMPE_SOLDADO",
      "CBMPE_OFICIAL",
      "PMPE_SOLDADO",
      "PMPE_OFICIAL",
      "CBMPE_COMBO",
      "PMPE_COMBO",
      "PCPE_AGENTE",
    ]);
  });
  it("slugs e chaves são únicos e toda chave tem subtítulo", () => {
    expect(new Set(CONTESTS.map((c) => c.slug)).size).toBe(CONTESTS.length);
    expect(new Set(CONTESTS.map((c) => c.key)).size).toBe(CONTESTS.length);
    for (const c of CONTESTS) expect(CONTEST_SUBTITLES[c.key], c.key).toBeTruthy();
    expect(Object.keys(CONTEST_SUBTITLES).sort()).toEqual(CONTESTS.map((c) => c.key).sort());
  });
  it("contestBySlug encontra pelo slug e devolve undefined se não existir", () => {
    expect(contestBySlug("cbmpe-oficial")?.key).toBe("CBMPE_OFICIAL");
    expect(contestBySlug("cbmpe-cfoa")?.key).toBe("CBMPE_CFOA");
    expect(contestBySlug("cbmpe-soldado")?.key).toBe("CBMPE_SOLDADO");
    expect(contestBySlug("pcpe-agente")?.org).toBe("PCPE");
    expect(contestBySlug("inexistente")).toBeUndefined();
    expect(contestBySlug("")).toBeUndefined();
  });
  it("título inclui a categoria entre parênteses só quando ela existe", () => {
    expect(contestTitle(contestBySlug("cbmpe-oficial")!)).toBe("CBMPE · Cargo: 2º Tenente (Oficial)");
    expect(contestTitle(contestBySlug("cbmpe-cfoa")!)).toBe("CBMPE · Cargo: 2º Tenente CFOA (Quadro de Administração)");
    expect(contestTitle(contestBySlug("cbmpe-soldado")!)).toBe("CBMPE · Cargo: Soldado (Praça)");
    expect(contestTitle(contestBySlug("pcpe-agente")!)).toBe("PCPE · Cargo: Agente de Polícia");
  });
  it("todo card tem imagem em /public", () => {
    for (const c of CONTESTS) expect(c.image.startsWith("/images/")).toBe(true);
  });
});

describe("editalItemApplies", () => {
  it("assunto sem restrição vale para todos os concursos", () => {
    expect(editalItemApplies({ onlyContests: [], excludeContests: [] }, "CBMPE_OFICIAL")).toBe(true);
    expect(editalItemApplies({ onlyContests: [], excludeContests: [] }, "PCPE_AGENTE")).toBe(true);
    expect(editalItemApplies({ onlyContests: [], excludeContests: [] }, "CBMPE_CFOA")).toBe(true);
  });
  it("assunto padrão sai do concurso que tem edital próprio", () => {
    const padrao = { onlyContests: [], excludeContests: ["PCPE_AGENTE", "CBMPE_CFOA"] };
    expect(editalItemApplies(padrao, "PCPE_AGENTE")).toBe(false);
    expect(editalItemApplies(padrao, "CBMPE_CFOA")).toBe(false);
    expect(editalItemApplies(padrao, "CBMPE_OFICIAL")).toBe(true);
    expect(editalItemApplies(padrao, null)).toBe(true);
  });
  it("assunto restrito vale só para o concurso indicado", () => {
    const proprio = { onlyContests: ["PCPE_AGENTE"], excludeContests: [] };
    expect(editalItemApplies(proprio, "PCPE_AGENTE")).toBe(true);
    expect(editalItemApplies(proprio, "CBMPE_OFICIAL")).toBe(false);
    expect(editalItemApplies(proprio, "CBMPE_CFOA")).toBe(false);
    expect(editalItemApplies(proprio, undefined)).toBe(false);
    const cfoaProprio = { onlyContests: ["CBMPE_CFOA"], excludeContests: [] };
    expect(editalItemApplies(cfoaProprio, "CBMPE_CFOA")).toBe(true);
    expect(editalItemApplies(cfoaProprio, "CBMPE_OFICIAL")).toBe(false);
  });
});

