// Limite simples em memória (suficiente para poucos usuários numa instância): 8 tentativas / 15 min por chave.
const WINDOW_MS = 15 * 60_000;
const MAX = 8;
const hits = new Map<string, { count: number; resetAt: number }>();

export function tooManyAttempts(key: string): boolean {
  const now = Date.now();
  const cur = hits.get(key);
  if (!cur || cur.resetAt < now) return false;
  return cur.count >= MAX;
}

export function registerFailure(key: string): void {
  const now = Date.now();
  const cur = hits.get(key);
  if (!cur || cur.resetAt < now) hits.set(key, { count: 1, resetAt: now + WINDOW_MS });
  else cur.count++;
}

export function clearFailures(key: string): void {
  hits.delete(key);
}
