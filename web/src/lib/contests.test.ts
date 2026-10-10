import { describe, expect, it } from "vitest";
import { CONTEST_SUBTITLES, CONTESTS, contestBySlug, contestTitle } from "./contests";

describe("concursos", () => {
  it("Oficial e Soldado CBMPE estão disponíveis (Agente PCPE em desenvolvimento)", () => {
    expect(CONTESTS.filter((c) => c.available).map((c) => c.key)).toEqual(["CBMPE_SOLDADO", "CBMPE_OFICIAL"]);
  });
  it("slugs e chaves são únicos e toda chave tem subtítulo", () => {
    expect(new Set(CONTESTS.map((c) => c.slug)).size).toBe(CONTESTS.length);
    expect(new Set(CONTESTS.map((c) => c.key)).size).toBe(CONTESTS.length);
    for (const c of CONTESTS) expect(CONTEST_SUBTITLES[c.key], c.key).toBeTruthy();
    expect(Object.keys(CONTEST_SUBTITLES).sort()).toEqual(CONTESTS.map((c) => c.key).sort());
  });
  it("contestBySlug encontra pelo slug e devolve undefined se não existir", () => {
    expect(contestBySlug("cbmpe-oficial")?.key).toBe("CBMPE_OFICIAL");
    expect(contestBySlug("cbmpe-soldado")?.key).toBe("CBMPE_SOLDADO");
    expect(contestBySlug("pcpe-agente")?.org).toBe("PCPE");
    expect(contestBySlug("inexistente")).toBeUndefined();
    expect(contestBySlug("")).toBeUndefined();
  });
  it("título inclui a categoria entre parênteses só quando ela existe", () => {
    expect(contestTitle(contestBySlug("cbmpe-oficial")!)).toBe("CBMPE · Cargo: 2º Tenente (Oficial)");
    expect(contestTitle(contestBySlug("cbmpe-soldado")!)).toBe("CBMPE · Cargo: Soldado (Praça)");
    expect(contestTitle(contestBySlug("pcpe-agente")!)).toBe("PCPE · Cargo: Agente de Polícia");
  });
  it("todo card tem imagem em /public", () => {
    for (const c of CONTESTS) expect(c.image.startsWith("/images/")).toBe(true);
  });
});
