// Meus resumos: agrupa os resumos que o aluno escreveu (campo "Meu resumo" das atividades de Teoria) por disciplina e aula,
// na ordem dos assuntos. Funções puras; a leitura do banco fica em lib/data/summaries.ts.

export interface SummaryRow {
  text: string;
  updatedAt: Date;
  /** posição do trecho dentro da aula (a ordem dos assuntos da atividade a que o resumo está atrelado) */
  segmentOrder: number;
  topic: string | null;
  aula: { id: string; number: number; shortTitle: string };
  segmentId: string;
}

export interface AulaSummaries {
  aula: { id: string; number: number; shortTitle: string };
  items: { segmentId: string; topic: string | null; text: string; updatedAt: Date }[];
}

/** Descarta resumos vazios, agrupa por aula (em ordem de aula) e ordena os resumos de cada aula pela ordem dos trechos. */
export function groupSummaries(rows: SummaryRow[]): AulaSummaries[] {
  type Group = AulaSummaries & { orders: Map<string, number> };
  const byAula = new Map<string, Group>();
  for (const r of rows) {
    if (!r.text.trim()) continue;
    const g: Group = byAula.get(r.aula.id) ?? { aula: r.aula, items: [], orders: new Map() };
    g.items.push({ segmentId: r.segmentId, topic: r.topic, text: r.text.trim(), updatedAt: r.updatedAt });
    g.orders.set(r.segmentId, r.segmentOrder);
    byAula.set(r.aula.id, g);
  }
  return [...byAula.values()]
    .sort((a, b) => a.aula.number - b.aula.number)
    .map(({ aula, items, orders }) => ({ aula, items: items.sort((a, b) => (orders.get(a.segmentId) ?? 0) - (orders.get(b.segmentId) ?? 0)) }));
}
