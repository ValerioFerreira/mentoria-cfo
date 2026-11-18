import { describe, expect, it } from "vitest";
import { isEliminated, parseEliminations, resolveClick, setEliminated, toggleEliminated } from "./eliminations";

describe("estado das alternativas riscadas", () => {
  it("risca, devolve ao normal e não mexe em outras questões", () => {
    let s = toggleEliminated({}, 1, "B");
    s = toggleEliminated(s, 1, "D");
    s = toggleEliminated(s, 2, "A");
    expect(isEliminated(s, 1, "B")).toBe(true);
    expect(s[1]).toEqual(["B", "D"]);
    s = toggleEliminated(s, 1, "B");
    expect(isEliminated(s, 1, "B")).toBe(false);
    expect(s[2]).toEqual(["A"]);
    expect(toggleEliminated(s, 2, "A")[2]).toBeUndefined();
  });
  it("não cria estado novo quando nada muda", () => {
    const s = setEliminated({}, 3, "C", true);
    expect(setEliminated(s, 3, "C", true)).toBe(s);
    expect(setEliminated(s, 3, "A", false)).toBe(s);
  });
  it("lê só o que está no formato esperado", () => {
    expect(parseEliminations('{"1":["B","d","B"],"x":["A"],"2":"A","3":["Z","E"]}')).toEqual({ 1: ["B"], 3: ["E"] });
    expect(parseEliminations("lixo")).toEqual({});
    expect(parseEliminations("[1,2]")).toEqual({});
    expect(parseEliminations(null)).toEqual({});
  });
});

describe("resolveClick", () => {
  it("clique simples numa alternativa normal marca; noutra marcada, desmarca", () => {
    expect(resolveClick("B", 1, { out: false, chosen: null })).toEqual({ out: false, chosen: "B" });
    expect(resolveClick("B", 1, { out: false, chosen: "B" })).toEqual({ out: false, chosen: null });
    expect(resolveClick("B", 1, { out: false, chosen: "C" })).toEqual({ out: false, chosen: "B" });
  });
  it("clique simples numa riscada só a devolve ao normal, sem marcar", () => {
    expect(resolveClick("B", 1, { out: true, chosen: "C" })).toEqual({ out: false, chosen: "C" });
  });
  it("duplo clique desfaz o primeiro e risca", () => {
    expect(resolveClick("B", 2, { out: false, chosen: null })).toEqual({ out: true, chosen: null });
    expect(resolveClick("B", 2, { out: false, chosen: "C" })).toEqual({ out: true, chosen: "C" });
  });
  it("riscar a alternativa marcada desmarca a escolha", () => {
    expect(resolveClick("B", 2, { out: false, chosen: "B" })).toEqual({ out: true, chosen: null });
  });
  it("duplo clique numa riscada a devolve ao normal (igual ao clique simples)", () => {
    expect(resolveClick("B", 2, { out: true, chosen: "C" })).toEqual({ out: false, chosen: "C" });
  });
  it("terceiro clique da sequência é ignorado", () => {
    expect(resolveClick("B", 3, { out: false, chosen: null })).toBeNull();
  });
});
