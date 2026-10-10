import { describe, expect, it } from "vitest";
import { buildReviewWeeks, type ReviewSubject } from "./review";

const subject = (id: string, examQuestions: number, nSegs = 6, sortOrder = 1): ReviewSubject => ({
  subjectId: id,
  examQuestions,
  sortOrder,
  segments: Array.from({ length: nSegs }, (_, i) => ({ id: `${id}/a01/s${String(i + 1).padStart(2, "0")}`, aulaId: `${id}/a01` })),
});
const run = (over: Partial<Parameters<typeof buildReviewWeeks>[0]> = {}) =>
  buildReviewWeeks({
    firstIndex: 19,
    lastIndex: 20,
    startDate: "2026-10-12",
    weeklyMinutes: 1080,
    subjects: [subject("lingua-portuguesa", 10), subject("matematica", 5, 6, 2), subject("direito-constitucional", 10, 6, 3)],
    ...over,
  });

describe("semanas de revisão final", () => {
  it("gera uma semana por índice pedido, com tipo FINAL_REVIEW e data correta", () => {
    const weeks = run();
    expect(weeks.map((w) => w.index)).toEqual([19, 20]);
    expect(weeks.map((w) => w.startDate)).toEqual(["2027-02-15", "2027-02-22"]);
    for (const w of weeks) expect(w.kind).toBe("FINAL_REVIEW");
  });
  it("só há Revisões gerais e cadernos mistos, todos de 60 min e no escopo FINAL", () => {
    for (const w of run())
      for (const a of w.activities) {
        expect(["REVISAO", "QUESTOES"]).toContain(a.type);
        expect(a.minutes).toBe(60);
        expect(a.scope).toBe("FINAL");
        if (a.type === "QUESTOES") expect(a.quiz).toEqual({ questions: 25, limitSeconds: 3600, mixed: true });
        else expect(a.quiz).toBeUndefined();
      }
  });
  it("chaves únicas em todo o conjunto e dia 0–6 em todas as atividades", () => {
    const acts = run().flatMap((w) => w.activities);
    expect(new Set(acts.map((a) => a.key)).size).toBe(acts.length);
    for (const a of acts) {
      expect(a.day).toBeGreaterThanOrEqual(0);
      expect(a.day).toBeLessThanOrEqual(6);
    }
  });
  it("a meta de cada semana é a soma dos minutos das atividades", () => {
    for (const w of run()) expect(w.targetMinutes).toBe(w.activities.reduce((n, a) => n + a.minutes, 0));
  });
  it("a cota é proporcional às questões da prova e a semana da prova é mais leve (60%)", () => {
    const [mid, exam] = run();
    expect(exam.activities.length).toBeLessThan(mid.activities.length);
    const by = (w: typeof mid, id: string) => w.activities.filter((a) => a.subjectId === id).length;
    expect(by(mid, "lingua-portuguesa")).toBeGreaterThan(by(mid, "matematica"));
    expect(by(mid, "direito-constitucional")).toBeGreaterThan(by(mid, "matematica"));
  });
  it("alterna Revisão e Questões por disciplina (R, Q, R, Q…) e revisões cobrem 4 trechos; cadernos, 8", () => {
    const acts = run({ firstIndex: 1, lastIndex: 4 }).flatMap((w) => w.activities).filter((a) => a.subjectId === "lingua-portuguesa");
    expect(acts.map((a) => a.type).slice(0, 4)).toEqual(["REVISAO", "QUESTOES", "REVISAO", "QUESTOES"]);
    for (const a of acts) expect(a.segmentIds.length).toBe(a.type === "REVISAO" ? 4 : 6); // 6 trechos: o caderno de 8 é limitado ao que existe
  });
  it("percorre os trechos em círculo (nenhum fica de fora quando há atividades suficientes)", () => {
    const acts = run({ firstIndex: 1, lastIndex: 6, weeklyMinutes: 2000 }).flatMap((w) => w.activities).filter((a) => a.subjectId === "matematica");
    expect(new Set(acts.flatMap((a) => a.segmentIds)).size).toBe(6);
  });
  it("disciplinas sem trechos cobertos ficam de fora; sem nenhuma disciplina as semanas saem vazias, sem quebrar", () => {
    const weeks = run({ subjects: [subject("a", 5, 0), subject("b", 5, 3)] });
    const ids = new Set(weeks.flatMap((w) => w.activities.map((a) => a.subjectId)));
    expect(ids).toEqual(new Set(["b"]));
    const empty = run({ subjects: [] });
    expect(empty).toHaveLength(2);
    expect(empty.every((w) => w.activities.length === 0 && w.targetMinutes === 0)).toBe(true);
  });
  it("trechos e aulas referenciados existem na própria disciplina", () => {
    for (const w of run())
      for (const a of w.activities) {
        expect(a.segmentIds.length).toBeGreaterThan(0);
        for (const s of a.segmentIds) expect(s.startsWith(`${a.subjectId}/`)).toBe(true);
        expect(a.aulaId).toBe(`${a.subjectId}/a01`);
      }
  });
  it("revisão que começa no meio da semana (firstDay) só usa os dias restantes e tem meta proporcional", () => {
    const full = run({ firstIndex: 1, lastIndex: 1 })[0];
    const part = run({ firstIndex: 1, lastIndex: 1, firstDay: 4 })[0];
    expect(Math.min(...part.activities.map((a) => a.day!))).toBeGreaterThanOrEqual(4);
    expect(part.targetMinutes).toBeLessThan(full.targetMinutes);
  });
  it("o firstDay só vale na semana 1; semanas seguintes ocupam a semana inteira", () => {
    const [w1, w2] = run({ firstIndex: 1, lastIndex: 2, firstDay: 5 });
    expect(Math.min(...w1.activities.map((a) => a.day!))).toBeGreaterThanOrEqual(5);
    expect(Math.min(...w2.activities.map((a) => a.day!))).toBeLessThan(5);
  });
  it("é determinístico", () => {
    expect(run()).toEqual(run());
  });
  it("sempre agenda ao menos uma atividade por semana quando há conteúdo (mesmo com poucas horas)", () => {
    for (const w of run({ weeklyMinutes: 60 })) expect(w.activities.length).toBeGreaterThanOrEqual(1);
  });
});
