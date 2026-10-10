// Fábricas de dados sintéticos para os testes unitários do planejador (sem depender do catálogo real em /content).
import type { Catalog, CatalogAula, CatalogSubject, PlannedActivity, SegmentLite, SegmentsByAula } from "./types";

export function mkSeg(aulaId: string, order: number, pages = 12, load = 12, start = 1): SegmentLite {
  return { id: `${aulaId}/s${String(order).padStart(2, "0")}`, aula: aulaId, order, startPage: start, endPage: start + pages - 1, pages, load };
}

export function mkAula(id: string, number: number, over: Partial<CatalogAula> = {}): CatalogAula {
  return {
    id, number, title: `Aula ${number}`, shortTitle: `Aula ${number}`, kind: "theory", edital: "yes", selectable: true,
    theoryPages: 24, segmentCount: 2, commentedPages: 0, listPages: 0, commentedRuns: [], practiceLinks: [], incidence: 1, printedOffset: 0,
    ...over,
  };
}

/** Aula com `n` trechos consecutivos de `pages` páginas e carga `load`. */
export function mkAulaWithSegs(id: string, number: number, n: number, pages = 12, load = 12, over: Partial<CatalogAula> = {}) {
  const segs: SegmentLite[] = [];
  let start = 1;
  for (let i = 1; i <= n; i++) {
    segs.push(mkSeg(id, i, pages, load, start));
    start += pages;
  }
  return { aula: mkAula(id, number, { theoryPages: n * pages, segmentCount: n, ...over }), segs };
}

export function mkSubject(id: string, aulas: CatalogAula[], over: Partial<CatalogSubject> = {}): CatalogSubject {
  return { id, name: id, block: "I", examQuestions: 10, sortOrder: 1, aulas, ...over };
}

export function mkCatalog(subjects: CatalogSubject[]): Catalog {
  return { subjects, gaps: [] };
}

export function mkSegments(...groups: SegmentLite[][]): SegmentsByAula {
  const out: SegmentsByAula = {};
  for (const g of groups) for (const s of g) (out[s.aula] ??= []).push(s);
  return out;
}

export function mkAct(key: string, type: PlannedActivity["type"], subjectId: string, minutes: number, over: Partial<PlannedActivity> = {}): PlannedActivity {
  return { key, type, subjectId, aulaId: `${subjectId}/a01`, minutes, segmentIds: [], refKeys: [], scope: "AULA", ...over };
}
