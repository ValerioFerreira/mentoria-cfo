import { describe, expect, it } from "vitest";
import { activityDetail } from "./activity-detail";

const seg = (startTopic: string | null, sortOrder: number) => ({ segment: { startTopic, sortOrder } });

describe("detalhe curto da atividade", () => {
  it("Teoria mostra o primeiro tópico (em ordem de trecho), cortado em 48 caracteres", () => {
    expect(activityDetail({ type: "TEORIA", scope: "AULA", segments: [seg("Segundo", 2), seg("Primeiro", 1)] })).toBe("Primeiro");
    const long = "a".repeat(60);
    const out = activityDetail({ type: "TEORIA", scope: "AULA", segments: [seg(long, 1)] })!;
    expect(out.length).toBe(48);
    expect(out.endsWith("…")).toBe(true);
  });
  it("Teoria sem tópicos devolve null; tópicos vazios ou só espaços são ignorados", () => {
    expect(activityDetail({ type: "TEORIA", scope: "AULA", segments: [] })).toBeNull();
    expect(activityDetail({ type: "TEORIA", scope: "AULA" })).toBeNull();
    expect(activityDetail({ type: "TEORIA", scope: "AULA", segments: [seg(null, 1), seg("   ", 2)] })).toBeNull();
  });
  it("Revisão lista o 1º tópico e quantos mais, sem repetir tópicos iguais", () => {
    expect(activityDetail({ type: "REVISAO", scope: "AULA", segments: [seg("A", 1), seg("B", 2), seg("C", 3)] })).toBe("revisar A e mais 2");
    expect(activityDetail({ type: "REVISAO", scope: "AULA", segments: [seg("A", 1), seg("A", 2)] })).toBe("revisar A");
    expect(activityDetail({ type: "REVISAO", scope: "AULA", segments: [] })).toBeNull();
  });
  it("Fixação só diz 'questões comentadas' quando há faixas de páginas", () => {
    expect(activityDetail({ type: "FIXACAO", scope: "AULA", fixRanges: [{ start: 1, end: 2 }] })).toBe("questões comentadas");
    expect(activityDetail({ type: "FIXACAO", scope: "AULA", fixRanges: [] })).toBeNull();
    expect(activityDetail({ type: "FIXACAO", scope: "AULA", fixRanges: null })).toBeNull();
    expect(activityDetail({ type: "FIXACAO", scope: "AULA" })).toBeNull();
  });
  it("Questões mostram o tamanho do caderno (25 por padrão); no escopo FINAL, misturadas", () => {
    expect(activityDetail({ type: "QUESTOES", scope: "AULA", quizQuestions: 20 })).toBe("caderno de 20 questões");
    expect(activityDetail({ type: "QUESTOES", scope: "AULA", quizQuestions: null })).toBe("caderno de 25 questões");
    expect(activityDetail({ type: "QUESTOES", scope: "FINAL", quizQuestions: 25 })).toBe("25 questões misturadas");
    expect(activityDetail({ type: "REVISAO", scope: "FINAL" })).toBeNull();
    expect(activityDetail({ type: "TEORIA", scope: "FINAL" })).toBeNull();
  });
  it("tipo desconhecido não quebra", () => {
    expect(activityDetail({ type: "OUTRO", scope: "AULA" })).toBeNull();
  });
});
