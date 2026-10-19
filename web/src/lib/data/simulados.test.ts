import { describe, expect, it } from "vitest";
import { EXAM_CONFIGS } from "../simulado-rules";

describe("Configurações dos Simulados Oficiais CBMPE 2026", () => {
  it("CBMPE Oficial (CFO) possui exatamente 70 questões e duração de 270 minutos (4h30min)", () => {
    const config = EXAM_CONFIGS.CBMPE_OFICIAL;
    expect(config.totalQuestions).toBe(70);
    expect(config.durationMinutes).toBe(270);
    expect(config.durationSeconds).toBe(270 * 60);

    // Soma das questões dos blocos
    const blockTotal =
      config.blocks.I.totalQuestions +
      config.blocks.II.totalQuestions +
      config.blocks.III!.totalQuestions;
    expect(blockTotal).toBe(70);

    // Mínimo por bloco (30%)
    expect(config.blocks.I.minQuestions).toBe(6);
    expect(config.blocks.II.minQuestions).toBe(6);
    expect(config.blocks.III!.minQuestions).toBe(9);

    // Soma das matérias
    const subjectTotal = config.subjects.reduce((sum, s) => sum + s.count, 0);
    expect(subjectTotal).toBe(70);
  });

  it("CBMPE Soldado (CFSd) possui exatamente 60 questões e duração de 240 minutos (4h00min)", () => {
    const config = EXAM_CONFIGS.CBMPE_SOLDADO;
    expect(config.totalQuestions).toBe(60);
    expect(config.durationMinutes).toBe(240);
    expect(config.durationSeconds).toBe(240 * 60);

    // Soma das questões dos blocos
    const blockTotal =
      config.blocks.I.totalQuestions +
      config.blocks.II.totalQuestions +
      config.blocks.III!.totalQuestions;
    expect(blockTotal).toBe(60);

    // Mínimo por bloco (30%)
    expect(config.blocks.I.minQuestions).toBe(9);
    expect(config.blocks.II.minQuestions).toBe(6);
    expect(config.blocks.III!.minQuestions).toBe(3);

    // Soma das matérias
    const subjectTotal = config.subjects.reduce((sum, s) => sum + s.count, 0);
    expect(subjectTotal).toBe(60);
  });

  it("PCPE Agente de Polícia possui exatamente 60 questões em 2 blocos (P1=20, P2=40) e corte de 50%", () => {
    const config = EXAM_CONFIGS.PCPE_AGENTE;
    expect(config.totalQuestions).toBe(60);
    expect(config.durationMinutes).toBe(240);
    expect(config.durationSeconds).toBe(240 * 60);
    expect(config.minPercentPerBlock).toBe(0);
    expect(config.minPercentTotal).toBe(50);
    expect(config.noZeroInAnyArea).toBe(false);

    // Blocos P1 e P2
    expect(config.blocks.I.totalQuestions).toBe(20);
    expect(config.blocks.I.minQuestions).toBe(0);
    expect(config.blocks.II.totalQuestions).toBe(40);
    expect(config.blocks.II.minQuestions).toBe(0);
    expect(config.blocks.III).toBeUndefined();

    // Soma das matérias
    const subjectTotal = config.subjects.reduce((sum, s) => sum + s.count, 0);
    expect(subjectTotal).toBe(60);

    // Contagem por bloco
    const p1Count = config.subjects.filter((s) => s.block === "I").reduce((sum, s) => sum + s.count, 0);
    const p2Count = config.subjects.filter((s) => s.block === "II").reduce((sum, s) => sum + s.count, 0);
    expect(p1Count).toBe(20);
    expect(p2Count).toBe(40);
  });
});
