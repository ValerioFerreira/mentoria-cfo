import { afterEach, describe, expect, it, vi } from "vitest";
import { servableStatuses } from "./servable";

describe("status de questão servidos aos alunos", () => {
  afterEach(() => vi.unstubAllEnvs());

  it("em produção (padrão) só as APROVADAS", () => {
    vi.stubEnv("SERVE_DRAFT_QUESTIONS", "");
    expect(servableStatuses()).toEqual(["APPROVED"]);
  });
  it("SERVE_DRAFT_QUESTIONS=true libera rascunhos (desenvolvimento)", () => {
    vi.stubEnv("SERVE_DRAFT_QUESTIONS", "true");
    expect(servableStatuses()).toEqual(["APPROVED", "DRAFT"]);
  });
  it("qualquer outro valor (inclusive 'TRUE', '1', 'yes') não libera rascunhos", () => {
    for (const v of ["TRUE", "1", "yes", "false", " true"]) {
      vi.stubEnv("SERVE_DRAFT_QUESTIONS", v);
      expect(servableStatuses(), v).toEqual(["APPROVED"]);
    }
  });
  it("RETIRED e FLAGGED nunca são servidos", () => {
    vi.stubEnv("SERVE_DRAFT_QUESTIONS", "true");
    expect(servableStatuses()).not.toContain("RETIRED");
    expect(servableStatuses()).not.toContain("FLAGGED");
  });
});
