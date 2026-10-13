import { describe, expect, it } from "vitest";
import { groupSummaries, type SummaryRow } from "./summaries";

const row = (aulaNumber: number, segmentOrder: number, text: string, topic: string | null = null): SummaryRow => ({
  text, updatedAt: new Date("2026-10-08T12:00:00Z"), segmentOrder, topic, segmentId: `x/a${aulaNumber}/s${segmentOrder}`,
  aula: { id: `x/a${aulaNumber}`, number: aulaNumber, shortTitle: `Aula ${aulaNumber}` },
});

describe("meus resumos", () => {
  it("separa por aula, na ordem das aulas, e ordena os resumos pela ordem dos trechos", () => {
    const g = groupSummaries([row(11, 2, "segundo"), row(8, 1, "crase"), row(11, 1, "primeiro", "Tipologia")]);
    expect(g.map((x) => x.aula.number)).toEqual([8, 11]);
    expect(g[1].items.map((i) => i.text)).toEqual(["primeiro", "segundo"]);
    expect(g[1].items[0].topic).toBe("Tipologia");
  });
  it("ignora resumos vazios ou só com espaços e aparam o texto", () => {
    const g = groupSummaries([row(1, 1, "   "), row(1, 2, "  ok  "), row(2, 1, "")]);
    expect(g).toHaveLength(1);
    expect(g[0].items.map((i) => i.text)).toEqual(["ok"]);
  });
  it("sem resumos devolve lista vazia", () => {
    expect(groupSummaries([])).toEqual([]);
  });
});
