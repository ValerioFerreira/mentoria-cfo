import { describe, expect, it } from "vitest";
import { attentionPoints, hashSeed, pickQuestions, remainingSeconds, score, type AnswerRow, type Candidate } from "./logic";

const cand = (n: number, segs = 3): Candidate[] =>
  Array.from({ length: n }, (_, i) => ({ id: `q${i}`, segmentId: `s${i % segs}`, seen: 0, lastCorrect: null }));

describe("pickQuestions", () => {
  it("sorteia sem repetir e respeita o tamanho pedido", () => {
    const ids = pickQuestions(cand(60), 25, hashSeed("a"));
    expect(ids).toHaveLength(25);
    expect(new Set(ids).size).toBe(25);
  });
  it("com menos questões que o pedido, devolve todas", () => {
    expect(pickQuestions(cand(10), 25, 1)).toHaveLength(10);
  });
  it("é determinístico para a mesma semente e varia entre sementes", () => {
    const a = pickQuestions(cand(60), 25, 7);
    expect(pickQuestions(cand(60), 25, 7)).toEqual(a);
    expect(pickQuestions(cand(60), 25, 8)).not.toEqual(a);
  });
  it("prioriza inéditas e erradas sobre as já acertadas", () => {
    const c: Candidate[] = [
      ...Array.from({ length: 30 }, (_, i) => ({ id: `ok${i}`, segmentId: `s${i % 3}`, seen: 3, lastCorrect: true })),
      ...Array.from({ length: 10 }, (_, i) => ({ id: `new${i}`, segmentId: `s${i % 3}`, seen: 0, lastCorrect: null })),
    ];
    let fresh = 0;
    for (let seed = 1; seed <= 40; seed++) fresh += pickQuestions(c, 10, seed).filter((id) => id.startsWith("new")).length;
    expect(fresh / (40 * 10)).toBeGreaterThan(0.4); // sem prioridade seria ~0,25 (10 de 40); medido ~0,46
  });
  it("espalha entre os trechos em vez de concentrar", () => {
    const c = cand(90, 3);
    const ids = pickQuestions(c, 24, 3);
    const bySeg = new Map<string, number>();
    for (const id of ids) bySeg.set(c.find((x) => x.id === id)!.segmentId, (bySeg.get(c.find((x) => x.id === id)!.segmentId) ?? 0) + 1);
    for (const n of bySeg.values()) expect(n).toBeGreaterThanOrEqual(5);
  });
});

const row = (over: Partial<AnswerRow>): AnswerRow => ({
  questionId: "q", topic: "T", segmentId: "s1", pageRef: 10, chosen: "A", correctLabel: "A", seconds: 60, ...over,
});

describe("score", () => {
  it("separa acertos, erros e brancos", () => {
    const s = score([row({}), row({ chosen: "B" }), row({ chosen: null }), row({})]);
    expect(s).toEqual({ total: 4, correct: 2, wrong: 1, blank: 1, percent: 50 });
  });
});

describe("attentionPoints", () => {
  it("aponta assuntos com acerto abaixo de 60% e ignora os bons", () => {
    const rows = [
      row({ topic: "Fraco", chosen: "B" }), row({ topic: "Fraco", chosen: "C" }), row({ topic: "Fraco" }),
      row({ topic: "Bom" }), row({ topic: "Bom" }),
    ];
    const pts = attentionPoints(rows);
    expect(pts).toHaveLength(1);
    expect(pts[0]).toMatchObject({ topic: "Fraco", attempts: 3, correct: 1, reason: "acerto baixo" });
  });
  it("marca como lento quem demora muito mais que a média e não domina o assunto", () => {
    const rows = [
      row({ topic: "Rápido", seconds: 30 }), row({ topic: "Rápido", seconds: 30 }), row({ topic: "Rápido", seconds: 30 }),
      row({ topic: "Lento", seconds: 200 }), row({ topic: "Lento", seconds: 200, chosen: "B" }),
    ];
    const pts = attentionPoints(rows);
    expect(pts.some((p) => p.topic === "Lento")).toBe(true);
  });
  it("lista vazia não gera pontos", () => {
    expect(attentionPoints([])).toEqual([]);
  });
});

describe("remainingSeconds", () => {
  it("conta regressivamente e não fica negativo", () => {
    expect(remainingSeconds(0, 3600, 600_000)).toBe(3000);
    expect(remainingSeconds(0, 3600, 4_000_000)).toBe(0);
  });
});
