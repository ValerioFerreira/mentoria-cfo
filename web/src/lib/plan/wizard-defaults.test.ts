import { describe, expect, it } from "vitest";
import { wizardDefaultsFromPlan, type DefaultsSubject, type SavedPlan } from "./wizard-defaults";

const subjects: DefaultsSubject[] = [
  { id: "portugues", languageGroup: null, items: [{ id: "p1", aulaIds: ["portugues/a01"] }, { id: "p2", aulaIds: ["portugues/a02"] }] },
  { id: "matematica", languageGroup: null, items: [{ id: "m1", aulaIds: ["matematica/a01"] }] },
];
const answer = { experience: 2, self: 4, hitRate: "mid" };

function plan(over: Partial<SavedPlan> = {}): SavedPlan {
  return {
    startDate: "2026-10-12",
    examDate: "2027-02-28",
    params: { hoursPerWeek: 25, firstStudyDate: "2026-10-14", request: { turbo: true, excludedAulas: [] } },
    subjects: [{ subjectId: "portugues", diagnostic: { ...answer, aulas: {} } }],
    ...over,
  };
}

describe("wizardDefaultsFromPlan", () => {
  it("sem plano anterior não há pré-seleção", () => {
    expect(wizardDefaultsFromPlan(null, subjects, "2026-10-14")).toBeNull();
  });

  it("repete disciplinas, horas, prova, Turbo e respostas do plano vigente", () => {
    const r = wizardDefaultsFromPlan(plan(), subjects, "2026-10-20")!;
    expect(r.selected).toEqual(["portugues"]);
    expect(r.hours).toBe(25);
    expect(r.examDate).toBe("2027-02-28");
    expect(r.turbo).toBe(true);
    expect(r.answers.portugues).toEqual(answer);
    expect(r.startMode).toBe("now");
  });

  it("mantém a data de início escolhida quando ela ainda não chegou", () => {
    const r = wizardDefaultsFromPlan(plan({ params: { hoursPerWeek: 20, firstStudyDate: "2026-11-02" } }), subjects, "2026-10-20")!;
    expect(r.startMode).toBe("date");
    expect(r.startPick).toBe("2026-11-02");
  });

  it("planos novos devolvem as marcas e os assuntos desmarcados como foram guardados", () => {
    const r = wizardDefaultsFromPlan(
      plan({ subjects: [{ subjectId: "portugues", diagnostic: { ...answer, aulas: {}, marks: { p1: 2, zzz: 1 }, unselectedTopics: ["p2", "xxx"] } }] }),
      subjects,
      "2026-10-20",
    )!;
    expect(r.marks).toEqual({ p1: 2 });
    expect(r.unselectedTopics).toEqual(["p2"]);
  });

  it("planos antigos deduzem marcas e assuntos desmarcados das aulas", () => {
    const r = wizardDefaultsFromPlan(
      plan({
        params: { hoursPerWeek: 25, request: { excludedAulas: ["portugues/a02"] } },
        subjects: [{ subjectId: "portugues", diagnostic: { aulas: { "portugues/a01": 1 } } }],
      }),
      subjects,
      "2026-10-20",
    )!;
    expect(r.marks).toEqual({ p1: 1 });
    expect(r.unselectedTopics).toEqual(["p2"]);
  });

  it("ignora disciplinas que não existem mais no concurso", () => {
    expect(wizardDefaultsFromPlan(plan({ subjects: [{ subjectId: "extinta", diagnostic: {} }] }), subjects, "2026-10-20")).toBeNull();
  });
});
