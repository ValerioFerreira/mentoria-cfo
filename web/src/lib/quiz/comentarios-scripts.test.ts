// Testes das funções puras dos scripts de comentários (scripts/lib): conferência do comentário contra a questão e pool
// candidato do caderno (espelho de loadQuizPool, usado na fila de prioridade).
import { describe, expect, it } from "vitest";
import { checkComment, type CommentEntry, type DbQuestion } from "../../../scripts/lib/comentarios";
import { activityPool, type BankQuestion, type PlanActivity } from "../../../scripts/lib/plan-pools";

const entry = (over: Partial<CommentEntry> = {}): CommentEntry => ({
  id: "tec_1", contentHash: "h1", gabarito: "B", comentario: "Comentário.",
  alternativas: { A: "Errada: x", B: "Correta: y", C: "Errada: z" }, autor: "t", data: "2026-11-16", arquivo: "d/l.json", pendente: false, ...over,
});
const question = (over: Partial<DbQuestion> = {}): DbQuestion => ({
  id: "tec_1", contentHash: "h1", kind: "MULTIPLA_ESCOLHA", explanation: "",
  options: [{ label: "A", isCorrect: false, comment: null }, { label: "B", isCorrect: true, comment: null }, { label: "C", isCorrect: false, comment: null }], ...over,
});

describe("checkComment", () => {
  it("grava quando hash, gabarito e letras conferem", () => {
    const v = checkComment(entry(), question());
    expect(v.status).toBe("gravar");
    if (v.status === "gravar") expect(v.optionComments).toEqual({ A: "Errada: x", B: "Correta: y", C: "Errada: z" });
  });
  it("não regrava o que já está igual", () => {
    const q = question({ explanation: "Comentário.", options: [{ label: "A", isCorrect: false, comment: "Errada: x" }, { label: "B", isCorrect: true, comment: "Correta: y" }, { label: "C", isCorrect: false, comment: "Errada: z" }] });
    expect(checkComment(entry(), q).status).toBe("igual");
  });
  it("recusa questão alterada, gabarito diferente, letras diferentes e questão ausente", () => {
    expect(checkComment(entry(), question({ contentHash: "h2" })).status).toBe("desatualizado");
    expect(checkComment(entry({ gabarito: "A" }), question()).status).toBe("gabarito");
    expect(checkComment(entry({ alternativas: { A: "Errada: x", B: "Correta: y" } }), question()).status).toBe("alternativas");
    expect(checkComment(entry(), undefined).status).toBe("ausente");
  });
  it("Certo/Errado não leva nota por alternativa", () => {
    const ce = question({ kind: "CERTO_ERRADO", options: [{ label: "C", isCorrect: true, comment: null }, { label: "E", isCorrect: false, comment: null }] });
    expect(checkComment(entry({ gabarito: "C", alternativas: {} }), ce).status).toBe("gravar");
    expect(checkComment(entry({ gabarito: "C" }), ce).status).toBe("alternativas");
  });
});

describe("activityPool", () => {
  const q = (id: string, segmentId: string, banca = "AOCP", kind: BankQuestion["kind"] = "MULTIPLA_ESCOLHA"): BankQuestion => ({ id, segmentId, banca, kind, status: "APPROVED", commented: false });
  const bank = new Map<string, BankQuestion[]>([
    ["d/a01/s01", [q("p1", "d/a01/s01"), q("p2", "d/a01/s01"), q("ce", "d/a01/s01", "AOCP", "CERTO_ERRADO"), q("fgv", "d/a01/s01", "FGV")]],
    ["d/a00/s01", [q("x1", "d/a00/s01"), q("x2", "d/a00/s01", "Cebraspe")]],
    ["d/a02/s01", [q("later", "d/a02/s01")]],
  ]);
  const act = (over: Partial<PlanActivity>): PlanActivity => ({
    id: "q", type: "QUESTOES", status: "PENDING", subjectId: "d", aulaId: "d/a01", dayIndex: 2, sortOrder: 1, quizQuestions: 25, weekIndex: 2, segmentIds: ["d/a01/s01"], ...over,
  });
  const teorias: PlanActivity[] = [
    act({ id: "t0", type: "TEORIA", weekIndex: 1, segmentIds: ["d/a00/s01"] }),
    act({ id: "t2", type: "TEORIA", weekIndex: 3, segmentIds: ["d/a02/s01"] }),
  ];

  it("só a camada própria quando ela basta", () => {
    expect(activityPool(act({ quizQuestions: 2 }), teorias, bank, "CBMPE_OFICIAL")).toEqual({ primary: ["p1", "p2", "ce"], extra: [], reinforcement: [] });
  });
  it("completa com trechos já estudados (nunca os de depois) e, no CFO BM, com reforço de outras bancas", () => {
    const p = activityPool(act({}), teorias, bank, "CBMPE_OFICIAL");
    expect(p.extra).toEqual(["x1"]);
    expect(p.reinforcement.sort()).toEqual(["fgv", "x2"]);
  });
  it("CFOA só usa múltipla escolha; PMPE não usa reforço", () => {
    expect(activityPool(act({}), teorias, bank, "CBMPE_CFOA").primary).toEqual(["p1", "p2"]);
    expect(activityPool(act({}), teorias, bank, "PMPE_OFICIAL").reinforcement).toEqual([]);
  });
});
