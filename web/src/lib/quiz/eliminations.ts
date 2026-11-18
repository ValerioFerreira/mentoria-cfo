// Alternativas riscadas pelo aluno (dois cliques): lógica pura, sem React nem navegador (testada em eliminations.test.ts).
// O estado é "posição da questão → letras riscadas"; vive na sessão do navegador (sessionStorage), nunca no servidor.

export type Eliminations = Record<number, string[]>;

export const eliminationsKey = (sessionId: string) => `elim:${sessionId}`;

export const isEliminated = (state: Eliminations, position: number, label: string): boolean => (state[position] ?? []).includes(label);

/** Devolve um novo estado com a letra riscada (`value` true) ou devolvida ao normal (`value` false). */
export function setEliminated(state: Eliminations, position: number, label: string, value: boolean): Eliminations {
  const cur = state[position] ?? [];
  if (cur.includes(label) === value) return state;
  const next = value ? [...cur, label].sort() : cur.filter((l) => l !== label);
  const copy = { ...state };
  if (next.length) copy[position] = next;
  else delete copy[position];
  return copy;
}

export const toggleEliminated = (state: Eliminations, position: number, label: string): Eliminations =>
  setEliminated(state, position, label, !isEliminated(state, position, label));

/** Lê o valor guardado; qualquer coisa fora do formato esperado vira "nada riscado". */
export function parseEliminations(raw: string | null | undefined): Eliminations {
  if (!raw) return {};
  try {
    const v: unknown = JSON.parse(raw);
    if (!v || typeof v !== "object" || Array.isArray(v)) return {};
    const out: Eliminations = {};
    for (const [k, labels] of Object.entries(v as Record<string, unknown>)) {
      const pos = Number(k);
      if (!Number.isInteger(pos) || !Array.isArray(labels)) continue;
      const clean = labels.filter((l): l is string => typeof l === "string" && /^[A-E]$/.test(l));
      if (clean.length) out[pos] = [...new Set(clean)].sort();
    }
    return out;
  } catch {
    return {};
  }
}

/**
 * Resultado de um clique numa alternativa, dado o estado ANTES do primeiro clique da sequência (`before`) e o `detail` do
 * evento (1 = clique simples, 2 = segundo clique de um duplo; 3 ou mais não faz nada):
 *  - clique simples: alternativa riscada só é devolvida ao normal; senão é marcada (ou desmarcada, se já estava marcada);
 *  - duplo: desfaz o efeito do primeiro clique e alterna o risco; riscar a alternativa marcada desmarca a escolha.
 */
export interface ClickBefore {
  /** a alternativa estava riscada antes do clique? */
  out: boolean;
  /** letra marcada antes do clique (null = nenhuma) */
  chosen: string | null;
}
export interface ClickResult {
  out: boolean;
  chosen: string | null;
}

export function resolveClick(label: string, detail: number, before: ClickBefore): ClickResult | null {
  if (detail <= 0 || detail === 1) {
    if (before.out) return { out: false, chosen: before.chosen };
    return { out: false, chosen: before.chosen === label ? null : label };
  }
  if (detail === 2) {
    const out = !before.out;
    // riscar a alternativa que estava marcada desmarca a escolha; riscar outra não mexe na marcação
    return { out, chosen: out && before.chosen === label ? null : before.chosen };
  }
  return null;
}
