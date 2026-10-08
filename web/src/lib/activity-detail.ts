// Detalhe curto do que fazer em uma atividade (para listas): páginas, questões comentadas ou tamanho do caderno.
interface Input {
  type: string;
  scope: string;
  fixRanges?: unknown;
  quizQuestions?: number | null;
  segments?: { segment: { startPage: number; endPage: number } }[];
}

const span = (a: number, b: number) => (a === b ? `pág. ${a}` : `págs. ${a}–${b}`);

export function activityDetail(a: Input): string | null {
  if (a.scope === "FINAL") return a.type === "QUESTOES" ? `${a.quizQuestions ?? 25} questões misturadas` : null;
  if (a.type === "TEORIA" || a.type === "REVISAO") {
    const segs = a.segments?.map((s) => s.segment) ?? [];
    if (segs.length === 0) return null;
    const start = Math.min(...segs.map((s) => s.startPage));
    const end = Math.max(...segs.map((s) => s.endPage));
    return a.type === "TEORIA" ? span(start, end) : `revisar ${span(start, end)}`;
  }
  if (a.type === "FIXACAO") {
    const r = (a.fixRanges as { start: number; end: number }[] | null | undefined) ?? [];
    if (r.length === 0) return null;
    return `questões comentadas, ${r.map((x) => span(x.start, x.end)).join(" e ")}`;
  }
  if (a.type === "QUESTOES") return `caderno de ${a.quizQuestions ?? 25} questões`;
  return null;
}
