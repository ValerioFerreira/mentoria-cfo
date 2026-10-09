// Diretrizes: texto que diz ao aluno exatamente ONDE estudar (aula, página, tópico). Funções puras.

export interface SegmentRef {
  id: string;
  startPage: number;
  endPage: number;
  startPrinted: number | null;
  endPrinted: number | null;
  startTopic: string | null;
  startsMidTopic: boolean;
  stopBeforeTopic: string | null;
  endsMidTopic: boolean;
  endTopic: string | null;
  endsTheory: boolean;
}

export interface AulaRef {
  id: string;
  number: number;
  shortTitle: string;
  subjectName: string;
  printedOffset: number;
  /** material complementar do MentorIA (PDF próprio) em vez de aula do material-base */
  authored?: boolean;
  materialPath?: string | null;
}

/** Numeração dos complementos do MentorIA: 101, 102… aparecem como "Complemento 01", "Complemento 02"… */
export const COMPLEMENT_BASE = 100;

export interface FixRange {
  start: number;
  end: number;
  sourceAula?: string;
}

const q = (s: string) => `“${s.trim()}”`;

/** "pág. 12" ou "pág. 12 (impressa 11)" */
export function pageLabel(pdf: number, printed: number | null | undefined): string {
  return printed != null && printed !== pdf ? `pág. ${pdf} (impressa ${printed})` : `pág. ${pdf}`;
}

export function aulaLabel(a: Pick<AulaRef, "number" | "shortTitle">): string {
  if (a.number > COMPLEMENT_BASE) return `Complemento ${String(a.number - COMPLEMENT_BASE).padStart(2, "0")} — ${a.shortTitle}`;
  return `Aula ${String(a.number).padStart(2, "0")} — ${a.shortTitle}`;
}

/** Uma frase por segmento de teoria. */
export function teoriaStep(seg: SegmentRef, authored = false): string {
  const start = seg.startsMidTopic
    ? `Continue na ${pageLabel(seg.startPage, seg.startPrinted)}${seg.startTopic ? `, dentro do tópico ${q(seg.startTopic)}` : ""}`
    : `Comece na ${pageLabel(seg.startPage, seg.startPrinted)}${seg.startTopic ? `, no tópico ${q(seg.startTopic)}` : ""}`;
  let end: string;
  if (seg.stopBeforeTopic) end = `estude até a ${pageLabel(seg.endPage, seg.endPrinted)}, parando antes do tópico ${q(seg.stopBeforeTopic)}`;
  else if (seg.endsTheory && authored) end = `estude até a ${pageLabel(seg.endPage, seg.endPrinted)}, a última do material`;
  else if (seg.endsTheory) end = `estude até a ${pageLabel(seg.endPage, seg.endPrinted)}, que encerra a teoria desta aula (o que vem depois são resumos e questões)`;
  else if (seg.endsMidTopic) end = `estude até o fim da ${pageLabel(seg.endPage, seg.endPrinted)}${seg.endTopic ? ` (você ainda estará dentro de ${q(seg.endTopic)}; a próxima atividade continua dali)` : ""}`;
  else end = `estude até a ${pageLabel(seg.endPage, seg.endPrinted)}`;
  return `${start}, e ${end}.`;
}

export interface TeoriaDirective {
  heading: string;
  steps: string[];
  pages: number;
}

export function teoriaDirective(aula: AulaRef, segs: SegmentRef[]): TeoriaDirective {
  const ordered = [...segs].sort((a, b) => a.startPage - b.startPage);
  return {
    heading: `${aula.subjectName} · ${aulaLabel(aula)}`,
    steps: ordered.map((seg) => teoriaStep(seg, aula.authored)),
    pages: ordered.reduce((n, s) => n + (s.endPage - s.startPage + 1), 0),
  };
}

export function revisaoSteps(): string[] {
  return [
    "Sem consultar o material, escreva em até 10 minutos tudo de que você se lembra sobre os conceitos das atividades de Teoria abaixo — um parágrafo breve para cada conceito.",
    "Releia o seu resumo (campo “Meu resumo” de cada Teoria) e o Bizu desta atividade.",
    "Responda aos itens de Certo/Errado e confira o que ficou fraco.",
  ];
}

export function revisaoFinalSteps(): string[] {
  return [
    "Revisão geral: passe pelos trechos abaixo usando apenas o seu resumo e o Bizu. Só abra o PDF para o que não lembrar.",
    "Anote o que ainda erra: isso vira prioridade nos cadernos finais.",
  ];
}

export function fixacaoSteps(aula: AulaRef, ranges: FixRange[], sourceLabel: (id: string) => string): string[] {
  const parts = ranges.map((r) => {
    const span = r.start === r.end ? `pág. ${r.start}` : `págs. ${r.start} a ${r.end}`;
    return r.sourceAula ? `${span} da ${sourceLabel(r.sourceAula)}` : `${span} desta aula`;
  });
  return [
    `Passe cerca de 1 hora fazendo e estudando as questões comentadas de ${aulaLabel(aula)}: seção “Questões Comentadas”, ${parts.join("; ")}.`,
    "Tente responder antes de ler o comentário. Leia o comentário de todas, inclusive das que acertar.",
  ];
}

export function questoesSteps(mixed: boolean, questions: number, limitMinutes: number): string[] {
  return [
    mixed
      ? `Caderno misto de ${questions} questões no padrão AOCP, sorteadas dos assuntos que você já estudou.`
      : `Caderno de ${questions} questões no padrão AOCP, sorteadas dos trechos de teoria vinculados a esta atividade.`,
    `Tempo limite: ${limitMinutes} minutos. O resultado é salvo e mostra seus pontos de atenção.`,
  ];
}
