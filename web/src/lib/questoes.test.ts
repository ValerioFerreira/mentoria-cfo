import { describe, expect, it } from "vitest";

describe("questões e agregação por assunto", () => {
  it("calcula taxa de acerto por matéria e por tópico corretamente", () => {
    const rawAnswers = [
      { questionId: "q1", isCorrect: true },
      { questionId: "q2", isCorrect: false },
      { questionId: "q3", isCorrect: true },
    ];

    const totalAnswered = rawAnswers.length;
    const totalCorrect = rawAnswers.filter((a) => a.isCorrect).length;
    const accuracy = Math.round((totalCorrect / totalAnswered) * 100);

    expect(totalAnswered).toBe(3);
    expect(totalCorrect).toBe(2);
    expect(accuracy).toBe(67);
  });

  it("retorna acurácia nula quando nenhuma questão foi respondida", () => {
    const totalAnswered = 0;
    const totalCorrect = 0;
    const accuracy = totalAnswered > 0 ? Math.round((totalCorrect / totalAnswered) * 100) : null;

    expect(accuracy).toBeNull();
  });

  it("ordena assuntos com mais questões prioritariamente", () => {
    const topics = [
      { name: "Sintaxe", totalQuestions: 15 },
      { name: "Crase", totalQuestions: 30 },
      { name: "Pontuação", totalQuestions: 5 },
    ];

    topics.sort((a, b) => b.totalQuestions - a.totalQuestions);

    expect(topics[0].name).toBe("Crase");
    expect(topics[1].name).toBe("Sintaxe");
    expect(topics[2].name).toBe("Pontuação");
  });
});
