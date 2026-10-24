import { describe, expect, it } from "vitest";
import { initialPlanStatus } from "./initial-status";

describe("initialPlanStatus", () => {
  it("aluno comum fica em análise", () => {
    expect(initialPlanStatus({ role: "USER", contest: "CBMPE_OFICIAL" })).toBe("PENDING_ANALYSIS");
  });
  it("administrador nasce liberado, inclusive no PCPE e no CFOA", () => {
    expect(initialPlanStatus({ role: "ADMIN", contest: "PCPE_AGENTE" })).toBe("ACTIVE");
    expect(initialPlanStatus({ role: "ADMIN", contest: "CBMPE_CFOA" })).toBe("ACTIVE");
  });
  it("parceiro ativo é liberado nos outros concursos, mas no PCPE e no CFOA também passa pela análise", () => {
    expect(initialPlanStatus({ role: "USER", partnerActive: true, contest: "CBMPE_OFICIAL" })).toBe("ACTIVE");
    expect(initialPlanStatus({ role: "USER", partnerActive: true, contest: "PCPE_AGENTE" })).toBe("PENDING_ANALYSIS");
    expect(initialPlanStatus({ role: "USER", partnerActive: true, contest: "CBMPE_CFOA" })).toBe("PENDING_ANALYSIS");
  });
  it("status explícito (refazer plano já liberado) prevalece", () => {
    expect(initialPlanStatus({ role: "USER", contest: "PCPE_AGENTE", explicit: "ACTIVE" })).toBe("ACTIVE");
    expect(initialPlanStatus({ role: "USER", contest: "CBMPE_CFOA", explicit: "ACTIVE" })).toBe("ACTIVE");
  });
});

