import { describe, expect, it } from "vitest";
import { EVE_REVIEW_MINUTES, MAX_SAME_SUBJECT_MINUTES_PER_DAY } from "./constants";
import { buildEveReview, buildSpareReview, type ReviewSubject } from "./review";

const subj = (id: string, exam: number, order: number, n = 10): ReviewSubject => ({
  subjectId: id,
  examQuestions: exam,
  sortOrder: order,
  segments: Array.from({ length: n }, (_, i) => ({ id: `${id}/a01/s${String(i + 1).padStart(2, "0")}`, aulaId: `${id}/a01` })),
});
const subjects = [subj("lingua-portuguesa", 12, 1), subj("matematica", 8, 2), subj("direito-constitucional", 10, 3)];
const WEEKLY = 1200;
const flatDays = (m: Map<number, ReturnType<typeof buildSpareReview> extends Map<number, infer V> ? V : never>) => [...m.entries()].sort((a, b) => a[0] - b[0]).flatMap(([ord, acts]) => acts.map((a) => ({ ...a, ord })));

describe("buildSpareReview (dias que sobram depois do conteúdo)", () => {
  const run = (from = 14, to = 34, subs = subjects) => buildSpareReview({ fromOrd: from, toOrd: to, weeklyMinutes: WEEKLY, subjects: subs });

  it("preenche cada dia pedido, só com Revisões gerais e cadernos mistos de 60 min no escopo FINAL", () => {
    const m = run();
    expect([...m.keys()].sort((a, b) => a - b)).toEqual(Array.from({ length: 21 }, (_, i) => 14 + i));
    for (const a of flatDays(m)) {
      expect(["REVISAO", "QUESTOES"]).toContain(a.type);
      expect(a.minutes).toBe(60);
      expect(a.scope).toBe("FINAL");
      expect(a.day).toBe(a.ord % 7);
      if (a.type === "QUESTOES") expect(a.quiz).toEqual({ questions: 25, limitSeconds: 3600, mixed: true });
    }
  });
  it("chaves únicas e trechos/aulas da própria disciplina", () => {
    const acts = flatDays(run());
    expect(new Set(acts.map((a) => a.key)).size).toBe(acts.length);
    for (const a of acts) {
      expect(a.aulaId.startsWith(`${a.subjectId}/`)).toBe(true);
      for (const id of a.segmentIds) expect(id.startsWith(`${a.subjectId}/`)).toBe(true);
    }
  });
  it("cada disciplina aparece no máximo uma vez por dia e nunca passa de 120 min", () => {
    const per = new Map<string, number>();
    for (const a of flatDays(run())) per.set(`${a.ord}|${a.subjectId}`, (per.get(`${a.ord}|${a.subjectId}`) ?? 0) + a.minutes);
    for (const m of per.values()) expect(m).toBeLessThanOrEqual(MAX_SAME_SUBJECT_MINUTES_PER_DAY);
  });
  it("alterna Revisão e Questões por disciplina (R, Q, R, Q…); revisões cobrem 4 trechos e cadernos, 8", () => {
    const acts = flatDays(run());
    for (const s of subjects) {
      const mine = acts.filter((a) => a.subjectId === s.subjectId);
      mine.forEach((a, i) => {
        expect(a.type).toBe(i % 2 === 0 ? "REVISAO" : "QUESTOES");
        expect(a.segmentIds).toHaveLength(a.type === "REVISAO" ? 4 : 8);
      });
    }
  });
  it("as disciplinas de maior peso aparecem mais, mas todas aparecem", () => {
    const count = (id: string) => flatDays(run(14, 55)).filter((a) => a.subjectId === id).length;
    expect(count("lingua-portuguesa")).toBeGreaterThanOrEqual(count("matematica"));
    for (const s of subjects) expect(count(s.subjectId)).toBeGreaterThan(0);
  });
  it("percorre os trechos em círculo (nenhum fica de fora quando há atividades suficientes)", () => {
    const used = new Set(flatDays(run(14, 90, [subj("matematica", 8, 1, 10)])).flatMap((a) => a.segmentIds));
    expect(used.size).toBe(10);
  });
  it("disciplinas sem trechos ficam de fora; sem nenhuma disciplina não há dias", () => {
    const m = run(14, 20, [subj("a", 5, 1, 0), subj("b", 5, 2, 6)]);
    expect(new Set(flatDays(m).map((a) => a.subjectId))).toEqual(new Set(["b"]));
    expect(run(14, 20, []).size).toBe(0);
  });
  it("faixa vazia (from > to) não gera nada; é determinístico", () => {
    expect(run(20, 10).size).toBe(0);
    expect(flatDays(run())).toEqual(flatDays(run()));
  });
});

describe("buildEveReview (véspera da prova)", () => {
  it("uma única Revisão FINAL de 60 min na disciplina de maior peso, com os trechos mais relevantes", () => {
    const a = buildEveReview(subjects, 132)!;
    expect(a.type).toBe("REVISAO");
    expect(a.scope).toBe("FINAL");
    expect(a.minutes).toBe(EVE_REVIEW_MINUTES);
    expect(a.subjectId).toBe("lingua-portuguesa");
    expect(a.day).toBe(132 % 7);
    expect(a.segmentIds).toEqual(subjects[0].segments.slice(0, 8).map((s) => s.id));
    expect(a.aulaId).toBe(subjects[0].segments[0].aulaId);
    expect(a.refKeys).toEqual([]);
  });
  it("desempata pela ordem da disciplina e ignora quem não tem trechos", () => {
    const a = buildEveReview([subj("x", 10, 2), subj("y", 10, 1), subj("z", 50, 3, 0)], 10)!;
    expect(a.subjectId).toBe("y");
  });
  it("sem trechos em nenhuma disciplina não há revisão da véspera", () => {
    expect(buildEveReview([subj("x", 10, 1, 0)], 10)).toBeNull();
    expect(buildEveReview([], 10)).toBeNull();
  });
});
