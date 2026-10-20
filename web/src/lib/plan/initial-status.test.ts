import { describe, expect, it } from "vitest";
import { initialPlanStatus } from "./initial-status";

describe("initialPlanStatus", () => {
  it("aluno comum fica em análise", () => {
    expect(initialPlanStatus({ role: "USER", contest: "CBMPE_OFICIAL" })).toBe("PENDING_ANALYSIS");
  });
  it("administrador nasce liberado, inclusive no PCPE", () => {
    expect(initialPlanStatus({ role: "ADMIN", contest: "PCPE_AGENTE" })).toBe("ACTIVE");
  });
  it("parceiro ativo é liberado nos outros concursos, mas no PCPE também passa pela análise", () => {
    expect(initialPlanStatus({ role: "USER", partnerActive: true, contest: "CBMPE_OFICIAL" })).toBe("ACTIVE");
    expect(initialPlanStatus({ role: "USER", partnerActive: true, contest: "PCPE_AGENTE" })).toBe("PENDING_ANALYSIS");
  });
  it("status explícito (refazer plano já liberado) prevalece", () => {
    expect(initialPlanStatus({ role: "USER", contest: "PCPE_AGENTE", explicit: "ACTIVE" })).toBe("ACTIVE");
  });
});
