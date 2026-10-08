import { describe, expect, it } from "vitest";
import { HOURS_BANDS, SEGMENT } from "./constants";

describe("constantes do planejador", () => {
  it("faixas de horas são contíguas e sem sobreposição", () => {
    expect(HOURS_BANDS.MODERADO.min).toBe(HOURS_BANDS.LEVE.max + 1);
    expect(HOURS_BANDS.AVANCADO.min).toBe(HOURS_BANDS.MODERADO.max + 1);
  });
  it("regra de páginas respeita 10–17 págs. por atividade", () => {
    expect(SEGMENT.maxPages).toBe(17);
    expect(SEGMENT.minPages).toBeLessThan(SEGMENT.maxPages);
  });
});
