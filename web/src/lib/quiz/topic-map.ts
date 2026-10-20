import { editalItemApplies } from "@/lib/contests";

/** id do "assunto" das questões sem assunto do edital (o mesmo de `data/questoes.ts`) */
export const OTHER_TOPIC = "outros";

export interface TopicItem {
  id: string;
  subjectId: string;
  onlyContests?: readonly string[] | null;
  excludeContests?: readonly string[] | null;
  aulaIds: readonly string[];
}

/**
 * Assunto do edital DO CONCURSO do aluno para cada questão.
 * A questão guarda um único assunto (`editalItemId`), e os concursos que dividem a disciplina (CBMPE/PMPE × PCPE) têm
 * assuntos diferentes. Se o assunto gravado vale para o concurso, ele é mantido; senão, a questão vai para o assunto do
 * concurso que trata da mesma aula (o mais específico, isto é, com menos aulas); sem nenhum, para "outros".
 * Para CBMPE e PMPE o resultado é sempre o assunto gravado, como antes.
 */
export function makeTopicResolver(items: readonly TopicItem[], contest: string | null | undefined) {
  const byId = new Map(items.map((i) => [i.id, i]));
  const bySubject = new Map<string, TopicItem[]>();
  for (const i of items) {
    if (!editalItemApplies(i, contest)) continue;
    const list = bySubject.get(i.subjectId) ?? [];
    list.push(i);
    bySubject.set(i.subjectId, list);
  }
  const cache = new Map<string, string>();
  return (q: { editalItemId: string | null; subjectId: string; aulaId: string }): string => {
    const key = `${q.editalItemId ?? ""}|${q.subjectId}|${q.aulaId}`;
    const hit = cache.get(key);
    if (hit) return hit;
    const cur = q.editalItemId ? byId.get(q.editalItemId) : undefined;
    let out = OTHER_TOPIC;
    if (cur && editalItemApplies(cur, contest)) out = cur.id;
    else {
      const cands = (bySubject.get(q.subjectId) ?? []).filter((i) => i.aulaIds.includes(q.aulaId));
      if (cands.length) out = [...cands].sort((a, b) => a.aulaIds.length - b.aulaIds.length)[0].id;
    }
    cache.set(key, out);
    return out;
  };
}

/** Filtra questões pelos assuntos escolhidos ("outros" = sem assunto no concurso); lista vazia = todas. */
export function filterByTopics<Q extends { editalItemId: string | null; subjectId: string; aulaId: string }>(
  questions: Q[],
  topics: readonly string[] | undefined,
  resolve: ReturnType<typeof makeTopicResolver>,
): Q[] {
  if (!topics || topics.length === 0) return questions;
  const set = new Set(topics);
  return questions.filter((q) => set.has(resolve(q)));
}
