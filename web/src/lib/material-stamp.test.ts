import { existsSync, readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import { PDFDocument } from "pdf-lib";
import { describe, expect, it, vi } from "vitest";

vi.mock("server-only", () => ({}));
import { stampName, stampPdf } from "./material-stamp";

describe("carimbo do titular", () => {
  it("limpa e põe o nome em maiúsculas", () => {
    expect(stampName("  Maria  José d'Ávila <b>")).toBe("MARIA JOSÉ D'ÁVILA B");
  });
  it("carimba todas as páginas menos a capa e mantém a contagem", async () => {
    const src = await PDFDocument.create();
    for (let i = 0; i < 3; i++) src.addPage([595.28, 841.89]);
    const out = await stampPdf(await src.save(), { id: "u1", name: "Fulano de Tal", idLabel: "CPF 123.456.789-09" });
    const doc = await PDFDocument.load(out);
    expect(doc.getPageCount()).toBe(3);
    expect(doc.getKeywords()).toContain("titular:u1");
  });
  it("carimba um PDF real do material (saída em pipeline/.cache/tmp para conferência visual)", async () => {
    const f = path.resolve(process.cwd(), "..", "material-pdf", "direito-penal-militar", "m01.pdf");
    if (!existsSync(f)) return;
    const out = await stampPdf(readFileSync(f), { id: "u1", name: "Maria José da Conceição Albuquerque de Sá", idLabel: "CPF 123.456.789-09" });
    writeFileSync(path.resolve(process.cwd(), "..", "pipeline", ".cache", "tmp", "stamped.pdf"), out);
    expect(out.length).toBeGreaterThan(1000);
  }, 60000);
});
