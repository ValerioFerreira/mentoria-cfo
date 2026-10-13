// Anamnese por assunto: o aluno marca o que já estudou em cada assunto do edital e o planejador (que trabalha por aula)
// recebe as marcas traduzidas. Funções puras.

export type Mark = 0 | 1 | 2; // 0 = nunca vi, 1 = já estudei, 2 = domino

export interface AnamnesisItem {
  id: string;
  title: string;
  /** aulas da disciplina que tratam do assunto */
  aulaIds: string[];
}

export interface AnamnesisSubject {
  items: AnamnesisItem[];
  /** todas as aulas planejáveis da disciplina */
  aulaIds: string[];
}

/**
 * Nível de cada aula a partir das marcas por assunto. Uma aula só conta como estudada (ou dominada) quando TODOS os
 * assuntos que ela cobre foram marcados, então o nível é o menor entre eles. Aulas que nenhum assunto cita acompanham o
 * menor nível da disciplina inteira (só saem do plano quando tudo foi marcado).
 */
export function knownFromMarks(subject: AnamnesisSubject, marks: Record<string, Mark | undefined>): Record<string, 1 | 2> {
  const level = (i: AnamnesisItem): Mark => marks[i.id] ?? 0;
  const floor = subject.items.length ? Math.min(...subject.items.map(level)) : 0;
  const known: Record<string, 1 | 2> = {};
  for (const aulaId of subject.aulaIds) {
    const refs = subject.items.filter((i) => i.aulaIds.includes(aulaId));
    const v = refs.length ? Math.min(...refs.map(level)) : floor;
    if (v > 0) known[aulaId] = v as 1 | 2;
  }
  return known;
}
