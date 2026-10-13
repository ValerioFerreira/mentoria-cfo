// Detalhe curto do que fazer em uma atividade (para listas): o assunto do trecho, questões comentadas ou tamanho do caderno.
// Páginas e aulas do material só aparecem na diretriz da própria atividade.
interface Input {
  type: string;
  scope: string;
  fixRanges?: unknown;
  quizQuestions?: number | null;
  segments?: { segment: { startTopic: string | null; sortOrder: number } }[];
}

const short = (s: string, n = 48) => (s.length > n ? `${s.slice(0, n - 1).trimEnd()}…` : s);

/** Assuntos (tópicos de abertura) dos trechos da atividade, na ordem em que aparecem. */
function topics(a: Input): string[] {
  const segs = (a.segments ?? []).map((s) => s.segment).sort((x, y) => x.sortOrder - y.sortOrder);
  return [...new Set(segs.map((s) => s.startTopic?.trim()).filter((t): t is string => Boolean(t)))];
}

export function activityDetail(a: Input): string | null {
  if (a.scope === "FINAL") return a.type === "QUESTOES" ? `${a.quizQuestions ?? 25} questões misturadas` : null;
  if (a.type === "TEORIA") {
    const t = topics(a);
    return t.length ? short(t[0]) : null;
  }
  if (a.type === "REVISAO") {
    const t = topics(a);
    if (!t.length) return null;
    return `revisar ${short(t[0], 40)}${t.length > 1 ? ` e mais ${t.length - 1}` : ""}`;
  }
  if (a.type === "FIXACAO") {
    const r = (a.fixRanges as unknown[] | null | undefined) ?? [];
    return r.length === 0 ? null : "questões comentadas";
  }
  if (a.type === "QUESTOES") return `caderno de ${a.quizQuestions ?? 25} questões`;
  return null;
}
