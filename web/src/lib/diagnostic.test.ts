import { describe, expect, it } from "vitest";
import { DEFAULT_ANSWER, levelFromAnswer } from "./diagnostic";

describe("levelFromAnswer", () => {
  it("quem nunca estudou é iniciante", () => {
    expect(levelFromAnswer(DEFAULT_ANSWER)).toBe(0);
  });
  it("estudou na escola e se acha razoável fica no básico", () => {
    expect(levelFromAnswer({ experience: 1, self: 3, hitRate: "none" })).toBe(1);
  });
  it("concurseiro recente com bom acerto é avançado", () => {
    expect(levelFromAnswer({ experience: 3, self: 5, hitRate: "high" })).toBe(3);
  });
  it("acerto baixo em questões puxa o nível para baixo", () => {
    const withLow = levelFromAnswer({ experience: 2, self: 4, hitRate: "low" });
    const withHigh = levelFromAnswer({ experience: 2, self: 4, hitRate: "high" });
    expect(withLow).toBeLessThanOrEqual(withHigh);
    expect(withLow).toBeLessThan(3);
  });
  it("é monotônico na autoavaliação", () => {
    const levels = [1, 2, 3, 4, 5].map((s) => levelFromAnswer({ experience: 2, self: s as 1 | 2 | 3 | 4 | 5, hitRate: "mid" }));
    for (let i = 1; i < levels.length; i++) expect(levels[i]).toBeGreaterThanOrEqual(levels[i - 1]);
  });
});
