import { describe, expect, it } from "vitest";
import { nextQuestionStatus } from "./sync-rules";

describe("nextQuestionStatus (importador de questões)", () => {
  it("questão nova recebe o status da classificação", () => {
    expect(nextQuestionStatus(null, "APPROVED")).toBe("APPROVED");
    expect(nextQuestionStatus(null, "DRAFT")).toBe("DRAFT");
  });

  it("anulada ou fora do edital sempre sai de circulação", () => {
    expect(nextQuestionStatus({ status: "APPROVED", classifiedBy: "AUTO" }, "RETIRED")).toBe("RETIRED");
    expect(nextQuestionStatus({ status: "APPROVED", classifiedBy: "MANUAL" }, "RETIRED")).toBe("RETIRED");
  });

  it("questão retirada automaticamente volta quando a curadoria passa a aceitá-la", () => {
    expect(nextQuestionStatus({ status: "RETIRED", classifiedBy: "AUTO" }, "APPROVED")).toBe("APPROVED");
    expect(nextQuestionStatus({ status: "RETIRED", classifiedBy: "AUTO" }, "DRAFT")).toBe("DRAFT");
  });

  it("decisão do administrador prevalece", () => {
    expect(nextQuestionStatus({ status: "RETIRED", classifiedBy: "MANUAL" }, "APPROVED")).toBe("RETIRED");
    expect(nextQuestionStatus({ status: "APPROVED", classifiedBy: "MANUAL" }, "DRAFT")).toBe("APPROVED");
  });

  it("denúncia aberta mantém a questão fora até a revisão", () => {
    expect(nextQuestionStatus({ status: "FLAGGED", classifiedBy: "AUTO" }, "APPROVED")).toBe("FLAGGED");
  });
});
