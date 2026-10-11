// Carrega o catálogo/segmentos reais de /content para os testes do planejador.
import fs from "node:fs";
import path from "node:path";
import type { Catalog, SegmentLite, SegmentsByAula } from "./types";

const CONTENT = path.resolve(__dirname, "../../../../content");

export function loadCatalog(): Catalog {
  const c = JSON.parse(fs.readFileSync(path.join(CONTENT, "catalog.json"), "utf-8")) as Catalog;
  return { ...c, gaps: c.gaps.filter((g) => !g.resolved) }; // lacunas já preenchidas por complementos não geram aviso
}

export function loadSegments(): SegmentsByAula {
  const out: SegmentsByAula = {};
  for (const f of fs.readdirSync(path.join(CONTENT, "segments"))) {
    const { segments } = JSON.parse(fs.readFileSync(path.join(CONTENT, "segments", f), "utf-8")) as { segments: SegmentLite[] };
    for (const s of segments) (out[s.aula] ??= []).push(s);
  }
  return out;
}

/** Nota de importância (1–100; null = fora do edital) de cada trecho em um concurso, de content/importance/segments.json. */
export function loadImportance(contest: string): Record<string, number | null> {
  const doc = JSON.parse(fs.readFileSync(path.join(CONTENT, "importance", "segments.json"), "utf-8")) as {
    segments: Record<string, { contests: Record<string, { appears: boolean; score: number | null }> }>;
  };
  return Object.fromEntries(Object.entries(doc.segments).map(([id, r]) => [id, r.contests[contest]?.appears ? r.contests[contest].score : null]));
}

/** Questões por disciplina na prova de um concurso, de content/contests.json. */
export function loadExamQuestions(contest: string): Record<string, number> {
  return (JSON.parse(fs.readFileSync(path.join(CONTENT, "contests.json"), "utf-8")) as Record<string, { exam: Record<string, number> }>)[contest].exam;
}
