import { describe, expect, it } from "vitest";
import { AOCP_BANCAS, INEDITA_BANCA, activityQuizWhere, contestBancas, hideInedita } from "./banca";
import type { QuestionStatus } from "@/generated/prisma/client";

// Simula o filtro do Prisma sobre um acervo pequeno para mostrar que o caderno de uma atividade só
// recebe questões dos trechos estudados e da banca AOCP.
type Q = { id: string; segmentId: string; status: QuestionStatus; banca: string };
const matches = (q: Q, w: ReturnType<typeof activityQuizWhere>) =>
  w.segmentId.in.includes(q.segmentId) && w.status.in.includes(q.status) && w.banca.in.includes(q.banca);

const acervo: Q[] = [
  { id: "a", segmentId: "direito-administrativo/a04/s01", status: "APPROVED", banca: "AOCP" },
  { id: "b", segmentId: "direito-administrativo/a04/s01", status: "APPROVED", banca: "CESPE" },
  { id: "c", segmentId: "direito-administrativo/a05/s01", status: "APPROVED", banca: "AOCP" }, // outro assunto
  { id: "d", segmentId: "direito-administrativo/a04/s01", status: "DRAFT", banca: "AOCP" },
  { id: "e", segmentId: "direito-administrativo/a04/s01", status: "RETIRED", banca: "Instituto AOCP" },
  { id: "f", segmentId: "direito-constitucional/a04/s01", status: "APPROVED", banca: "AOCP" }, // outra disciplina
];

describe("activityQuizWhere", () => {
  it("só os trechos da atividade, só servíveis, só AOCP", () => {
    const w = activityQuizWhere(["direito-administrativo/a04/s01"], ["APPROVED"]);
    expect(acervo.filter((q) => matches(q, w)).map((q) => q.id)).toEqual(["a"]);
  });

  it("questão de outro assunto ou de outra disciplina nunca entra, mesmo da mesma aula numerada", () => {
    const w = activityQuizWhere(["direito-administrativo/a04/s01"], ["APPROVED", "DRAFT"]);
    const ids = acervo.filter((q) => matches(q, w)).map((q) => q.id);
    expect(ids).not.toContain("c");
    expect(ids).not.toContain("f");
    expect(ids).toEqual(["a", "d"]);
  });

  it("aceita as grafias da banca", () => {
    expect(AOCP_BANCAS).toEqual(expect.arrayContaining(["AOCP", "Instituto AOCP"]));
  });

  it("no PCPE, enquanto não há cadernos Cebraspe, entram Cebraspe e AOCP", () => {
    const w = activityQuizWhere(["direito-administrativo/a04/s01"], ["APPROVED"], "PCPE_AGENTE");
    expect(acervo.filter((q) => matches(q, w)).map((q) => q.id)).toEqual(["a", "b"]);
  });

  it("garante que planos CBMPE e PMPE buscam só AOCP e PCPE_AGENTE busca Cebraspe e AOCP", () => {
    const wCbmpe = activityQuizWhere(["direito-administrativo/a04/s01"], ["APPROVED"], "CBMPE_OFICIAL");
    expect(wCbmpe.banca.in).toEqual(expect.arrayContaining(["AOCP", "Instituto AOCP"]));
    expect(wCbmpe.banca.in).not.toContain("CEBRASPE");

    const wPmpe = activityQuizWhere(["direito-administrativo/a04/s01"], ["APPROVED"], "PMPE_SOLDADO");
    expect(wPmpe.banca.in).toEqual(expect.arrayContaining(["AOCP", "Instituto AOCP"]));
    expect(wPmpe.banca.in).not.toContain("CEBRASPE");

    const wPcpe = activityQuizWhere(["direito-administrativo/a04/s01"], ["APPROVED"], "PCPE_AGENTE");
    expect(wPcpe.banca.in).toEqual(expect.arrayContaining(["CEBRASPE", "Cebraspe", "CESPE", "Cespe", "AOCP", "Instituto AOCP"]));
  });

  it("as inéditas MentorIA só entram para o PCPE", () => {
    expect(contestBancas("PCPE_AGENTE")).toContain(INEDITA_BANCA);
    expect(contestBancas("CBMPE_OFICIAL")).not.toContain(INEDITA_BANCA);
    expect(hideInedita("PCPE_AGENTE")).toEqual({});
    expect(hideInedita("CBMPE_OFICIAL")).toEqual({ NOT: { banca: INEDITA_BANCA } });
    expect(hideInedita(undefined)).toEqual({ NOT: { banca: INEDITA_BANCA } });
  });
});
