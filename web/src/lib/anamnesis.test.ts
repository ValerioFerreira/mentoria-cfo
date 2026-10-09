import { describe, expect, it } from "vitest";
import { knownFromMarks, type AnamnesisSubject } from "./anamnesis";

const subject: AnamnesisSubject = {
  items: [
    { id: "e1", title: "Interpretação", aulaIds: ["x/a11"] },
    { id: "e2", title: "Tipologia", aulaIds: ["x/a11"] },
    { id: "e3", title: "Crase", aulaIds: ["x/a08"] },
  ],
  aulaIds: ["x/a00", "x/a08", "x/a11"],
};

describe("anamnese por assunto", () => {
  it("sem marcas, nada é conhecido", () => {
    expect(knownFromMarks(subject, {})).toEqual({});
  });
  it("a aula só conta quando todos os assuntos dela foram marcados (vale o menor nível)", () => {
    expect(knownFromMarks(subject, { e1: 2 })).toEqual({});
    expect(knownFromMarks(subject, { e1: 2, e2: 1 })).toEqual({ "x/a11": 1 });
    expect(knownFromMarks(subject, { e1: 2, e2: 2 })).toEqual({ "x/a11": 2 });
  });
  it("aula que nenhum assunto cita só sai do plano quando a disciplina inteira foi marcada", () => {
    expect(knownFromMarks(subject, { e1: 2, e2: 2, e3: 2 })).toEqual({ "x/a00": 2, "x/a08": 2, "x/a11": 2 });
    // enquanto houver assunto sem marca, a aula solta continua no plano
    expect(knownFromMarks(subject, { e1: 2, e2: 2 })["x/a00"]).toBeUndefined();
    // com tudo marcado, ela acompanha o menor nível
    expect(knownFromMarks(subject, { e1: 2, e2: 2, e3: 1 })).toEqual({ "x/a00": 1, "x/a08": 1, "x/a11": 2 });
    expect(knownFromMarks(subject, { e1: 1, e2: 1, e3: 2 })["x/a00"]).toBe(1);
  });
  it("disciplina sem assuntos mapeados não marca nada", () => {
    expect(knownFromMarks({ items: [], aulaIds: ["x/a00"] }, {})).toEqual({});
  });
});
