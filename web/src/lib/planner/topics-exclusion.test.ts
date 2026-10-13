import { describe, expect, it } from "vitest";
import { generatePlan } from "./index";
import { selectContent } from "./select";
import type { Catalog, CatalogSubject, SegmentsByAula } from "./types";

const mockSubject: CatalogSubject = {
  id: "direito-constitucional",
  name: "Direito Constitucional",
  block: "II",
  examQuestions: 10,
  sortOrder: 1,
  materialCompleteness: 1,
  aulas: [
    {
      id: "direito-constitucional/a00",
      number: 0,
      title: "Conceito de Constituição",
      shortTitle: "Conceito",
      kind: "theory",
      edital: "yes",
      selectable: true,
      theoryPages: 20,
      segmentCount: 2,
      commentedPages: 10,
      listPages: 0,
      commentedRuns: [[1, 10]],
      practiceLinks: [],
      incidence: 1.0,
      printedOffset: 0,
      source: "base",
    },
    {
      id: "direito-constitucional/a01",
      number: 1,
      title: "Direitos Fundamentais",
      shortTitle: "Direitos Fundamentais",
      kind: "theory",
      edital: "yes",
      selectable: true,
      theoryPages: 30,
      segmentCount: 2,
      commentedPages: 15,
      listPages: 0,
      commentedRuns: [[1, 15]],
      practiceLinks: [],
      incidence: 1.5,
      printedOffset: 0,
      source: "base",
    },
  ],
};

const mockCatalog: Catalog = {
  subjects: [mockSubject],
  gaps: [],
};

const mockSegments: SegmentsByAula = {
  "direito-constitucional/a00": [
    { id: "direito-constitucional/a00/s01", aula: "direito-constitucional/a00", order: 1, startPage: 1, endPage: 10, pages: 10, load: 10 },
    { id: "direito-constitucional/a00/s02", aula: "direito-constitucional/a00", order: 2, startPage: 11, endPage: 20, pages: 10, load: 10 },
  ],
  "direito-constitucional/a01": [
    { id: "direito-constitucional/a01/s01", aula: "direito-constitucional/a01", order: 1, startPage: 1, endPage: 15, pages: 15, load: 15 },
    { id: "direito-constitucional/a01/s02", aula: "direito-constitucional/a01", order: 2, startPage: 16, endPage: 30, pages: 15, load: 15 },
  ],
};

describe("Exclusão de aulas e assuntos do edital no planejamento", () => {
  it("deve incluir todas as aulas quando nenhuma for excluída", () => {
    const sel = selectContent(
      [{ subject: mockSubject, level: 1 }],
      mockSegments,
      1000,
      {},
      false,
      new Set(),
    );
    expect(sel.tierByAula.has("direito-constitucional/a00")).toBe(true);
    expect(sel.tierByAula.has("direito-constitucional/a01")).toBe(true);
  });

  it("deve excluir a aula e suas atividades quando for informada em excludedAulas", () => {
    const excluded = new Set(["direito-constitucional/a00"]);
    const sel = selectContent(
      [{ subject: mockSubject, level: 1 }],
      mockSegments,
      1000,
      {},
      false,
      excluded,
    );
    expect(sel.tierByAula.has("direito-constitucional/a00")).toBe(false);
    expect(sel.tierByAula.has("direito-constitucional/a01")).toBe(true);

    const plan = generatePlan({
      catalog: mockCatalog,
      segments: mockSegments,
      startDate: "2026-10-12",
      examDate: "2027-02-28",
      hoursPerWeek: 25,
      subjects: [{ id: "direito-constitucional", level: 1 }],
      excludedAulas: ["direito-constitucional/a00"],
    });

    const plannedAulaIds = new Set(plan.weeks.flatMap((w) => w.activities.map((a) => a.aulaId)));
    expect(plannedAulaIds.has("direito-constitucional/a00")).toBe(false);
    expect(plannedAulaIds.has("direito-constitucional/a01")).toBe(true);
  });
});
