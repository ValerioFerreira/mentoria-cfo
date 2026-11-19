import { describe, expect, it } from "vitest";
import { normalizeFullName } from "./person-name";

describe("normalizeFullName", () => {
  it("aceita nome completo e devolve em caixa alta", () => {
    expect(normalizeFullName("maria da silva")).toBe("MARIA DA SILVA");
    expect(normalizeFullName("  João   d'Ávila-Souza ")).toBe("JOÃO D'ÁVILA-SOUZA");
    expect(normalizeFullName("Ângela Pinto")).toBe("ÂNGELA PINTO");
  });
  it("recusa o que não parece um nome completo", () => {
    expect(normalizeFullName("Maria")).toBeNull();
    expect(normalizeFullName("")).toBeNull();
    expect(normalizeFullName("Maria 2 Silva")).toBeNull();
    expect(normalizeFullName("a b")).toBeNull();
    expect(normalizeFullName("x".repeat(130) + " y")).toBeNull();
  });
});
