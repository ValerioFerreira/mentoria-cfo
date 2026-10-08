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
