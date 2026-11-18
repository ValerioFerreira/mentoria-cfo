"use client";

import { useCallback, useMemo, useSyncExternalStore } from "react";
import { eliminationsKey, isEliminated, parseEliminations, setEliminated, toggleEliminated, type Eliminations } from "@/lib/quiz/eliminations";

/**
 * Alternativas riscadas pelo aluno numa sessão de questões (caderno, treino ou simulado). Ficam em `sessionStorage`
 * (`elim:<sessionId>`), sempre dentro de try/catch; sem storage (janela privada, bloqueio) valem só na memória da página, e
 * a página funciona do mesmo jeito. O valor guardado é lido como "store externo" (useSyncExternalStore), então o HTML do
 * servidor e o primeiro render do cliente coincidem (nada riscado) e o risco aparece logo depois da hidratação.
 */
const memory = new Map<string, string>();
const listeners = new Set<() => void>();

function readRaw(key: string): string {
  if (!memory.has(key)) {
    let raw = "";
    try {
      raw = window.sessionStorage.getItem(key) ?? "";
    } catch {
      /* sem storage */
    }
    memory.set(key, raw);
  }
  return memory.get(key) ?? "";
}

function writeRaw(key: string, raw: string) {
  memory.set(key, raw);
  try {
    if (raw) window.sessionStorage.setItem(key, raw);
    else window.sessionStorage.removeItem(key);
  } catch {
    /* sem storage */
  }
  listeners.forEach((l) => l());
}

const subscribe = (cb: () => void) => {
  listeners.add(cb);
  return () => {
    listeners.delete(cb);
  };
};

export function useEliminations(sessionId: string) {
  const key = eliminationsKey(sessionId);
  const raw = useSyncExternalStore(subscribe, () => readRaw(key), () => "");
  const state = useMemo(() => parseEliminations(raw), [raw]);

  const update = useCallback(
    (fn: (s: Eliminations) => Eliminations) => {
      const cur = parseEliminations(readRaw(key));
      const next = fn(cur);
      if (next !== cur) writeRaw(key, Object.keys(next).length ? JSON.stringify(next) : "");
    },
    [key],
  );

  return {
    /** a letra está riscada na questão `position`? */
    isOut: (position: number, label: string) => isEliminated(state, position, label),
    /** risca se está normal, devolve ao normal se está riscada */
    toggle: (position: number, label: string) => update((s) => toggleEliminated(s, position, label)),
    /** devolve a letra ao normal */
    restore: (position: number, label: string) => update((s) => setEliminated(s, position, label, false)),
    /** define o risco de uma letra (usado para desfazer o primeiro clique de um duplo clique) */
    set: (position: number, label: string, value: boolean) => update((s) => setEliminated(s, position, label, value)),
  };
}
