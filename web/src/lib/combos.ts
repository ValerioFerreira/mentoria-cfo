import type { Contest } from "@/generated/prisma/client";

/**
 * Pacotes combo: um plano único que prepara para as duas provas (2º Tenente + Soldado) da mesma corporação.
 * O combo é uma chave de concurso própria; os dados de edital, importância e pesos vêm dos concursos-membro.
 */
export const COMBOS = {
  CBMPE_COMBO: { oficial: "CBMPE_OFICIAL", praca: "CBMPE_SOLDADO" },
  PMPE_COMBO: { oficial: "PMPE_OFICIAL", praca: "PMPE_SOLDADO" },
} as const satisfies Record<string, { oficial: Contest; praca: Contest }>;

export type ComboKey = keyof typeof COMBOS;

/** Peso fixo 2:1: cada questão do concurso prioritário vale o dobro da do outro na divisão do tempo. */
export const COMBO_PRIORITY_WEIGHT = { priority: 1, other: 0.5 } as const;

export function isCombo(c: string | null | undefined): c is ComboKey {
  return !!c && c in COMBOS;
}

/** Concursos-membro (o próprio concurso, quando não é combo). O Oficial vem primeiro. */
export function comboMembers(c: Contest): Contest[] {
  return isCombo(c) ? [COMBOS[c].oficial, COMBOS[c].praca] : [c];
}

/** Concurso prioritário padrão do combo: o Oficial. */
export function defaultPriority(c: ComboKey): Contest {
  return COMBOS[c].oficial;
}

export function isValidPriority(combo: ComboKey, priority: string): boolean {
  return comboMembers(combo).includes(priority as Contest);
}

/** Peso de cada membro conforme a prioridade escolhida. */
export function comboWeights(combo: ComboKey, priority: string): { contest: Contest; weight: number }[] {
  const p = isValidPriority(combo, priority) ? priority : defaultPriority(combo);
  return comboMembers(combo).map((contest) => ({ contest, weight: contest === p ? COMBO_PRIORITY_WEIGHT.priority : COMBO_PRIORITY_WEIGHT.other }));
}

export interface ComboMemberData {
  contest: string;
  weight: number;
  /** nota 1–100 de cada trecho no concurso; null = fora do edital dele */
  importance: Record<string, number | null>;
  /** questões esperadas de cada trecho no concurso (comparável entre concursos, ao contrário da nota percentil) */
  expected: Record<string, number>;
  /** questões de cada disciplina na prova do membro */
  examQuestions: Record<string, number>;
}

/**
 * Edital da união: o trecho só fica fora (null) quando não aparece em nenhum membro. A nota combinada (1–100) é o
 * percentil de Σ peso × questões esperadas entre os trechos que aparecem.
 */
export function mergeComboImportance(members: Pick<ComboMemberData, "weight" | "importance" | "expected">[]): Record<string, number | null> {
  const ids = new Set<string>();
  for (const m of members) for (const id of Object.keys(m.importance)) ids.add(id);
  const value = new Map<string, number>();
  const out: Record<string, number | null> = {};
  for (const id of ids) {
    const inAny = members.some((m) => m.importance[id] !== null && m.importance[id] !== undefined);
    if (!inAny) {
      out[id] = null;
      continue;
    }
    value.set(id, members.reduce((n, m) => n + (m.importance[id] != null ? m.weight * (m.expected[id] ?? 0) : 0), 0));
  }
  const ranked = [...value.entries()].sort((a, b) => a[1] - b[1] || a[0].localeCompare(b[0]));
  const n = ranked.length;
  ranked.forEach(([id], i) => {
    out[id] = Math.max(1, Math.round((100 * (i + 1)) / n));
  });
  return out;
}

/** Peso combinado por disciplina: W = Σ peso × questões do membro. */
export function mergeComboQuestions(members: Pick<ComboMemberData, "weight" | "examQuestions">[]): Record<string, number> {
  const out: Record<string, number> = {};
  for (const m of members) for (const [id, q] of Object.entries(m.examQuestions)) out[id] = (out[id] ?? 0) + m.weight * q;
  return out;
}
