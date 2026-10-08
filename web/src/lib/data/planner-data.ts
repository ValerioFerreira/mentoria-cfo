import "server-only";
import { db } from "@/lib/db";
import type { Catalog, CatalogAula, SegmentLite, SegmentsByAula } from "@/lib/planner/types";

export interface PlannerData {
  catalog: Catalog;
  segments: SegmentsByAula;
}

let cache: { at: number; data: PlannerData } | null = null;
const TTL_MS = 5 * 60_000; // conteúdo estrutural é estático; recarrega de vez em quando

export async function loadPlannerData(): Promise<PlannerData> {
  if (cache && Date.now() - cache.at < TTL_MS) return cache.data;
  const [subjects, aulas, segs, gaps] = await Promise.all([
    db.subject.findMany({ orderBy: { sortOrder: "asc" } }),
    db.aula.findMany({ orderBy: [{ subjectId: "asc" }, { number: "asc" }] }),
    db.segment.findMany({ orderBy: [{ aulaId: "asc" }, { sortOrder: "asc" }], select: { id: true, aulaId: true, sortOrder: true, startPage: true, endPage: true, pages: true, load: true } }),
    db.gap.findMany(),
  ]);

  const aulasBySubject = new Map<string, CatalogAula[]>();
  for (const a of aulas) {
    const item: CatalogAula = {
      id: a.id, number: a.number, title: a.title, shortTitle: a.shortTitle,
      kind: a.kind === "PRACTICE" ? "practice" : "theory",
      edital: a.edital.toLowerCase() as CatalogAula["edital"],
      selectable: a.selectable, theoryPages: a.theoryPages, segmentCount: a.segmentCount,
      commentedPages: a.commentedPages, listPages: a.listPages,
      commentedRuns: a.commentedRuns as unknown as [number, number][],
      practiceLinks: a.practiceLinks as unknown as CatalogAula["practiceLinks"],
      incidence: a.incidence, printedOffset: a.printedOffset,
      source: a.source === "AUTHORED" ? "authored" : "estrategia",
    };
    aulasBySubject.set(a.subjectId, [...(aulasBySubject.get(a.subjectId) ?? []), item]);
  }
  // ids de trecho são posicionais (s01…sN): após uma resegmentação com menos trechos, os antigos (sortOrder > N) ficam
  // no banco por causa de atividades/questões antigas, mas não fazem mais parte da aula
  const segCount = new Map(aulas.map((a) => [a.id, a.segmentCount]));
  const segments: SegmentsByAula = {};
  for (const s of segs) {
    if (s.sortOrder > (segCount.get(s.aulaId) ?? 0)) continue;
    const lite: SegmentLite = { id: s.id, aula: s.aulaId, order: s.sortOrder, startPage: s.startPage, endPage: s.endPage, pages: s.pages, load: s.load };
    (segments[s.aulaId] ??= []).push(lite);
  }
  const data: PlannerData = {
    catalog: {
      subjects: subjects.map((s) => ({
        id: s.id, name: s.name, block: s.block, examQuestions: s.examQuestions, sortOrder: s.sortOrder,
        ...(s.languageGroup ? { languageGroup: s.languageGroup } : {}),
        materialCompleteness: s.materialCompleteness,
        aulas: aulasBySubject.get(s.id) ?? [],
      })),
      gaps: gaps.filter((g) => !g.resolved).map((g) => ({ id: g.id, subject: g.subjectId, item: g.item, evidence: g.evidence, severity: g.severity.toLowerCase() as "high" | "medium" | "low", remedy: g.remedy })),
    },
    segments,
  };
  cache = { at: Date.now(), data };
  return data;
}
