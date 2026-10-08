// Datas em UTC (YYYY-MM-DD) para evitar surpresas de fuso/horário de verão.

const DAY = 86_400_000;

export function parseISO(iso: string): Date {
  const [y, m, d] = iso.split("-").map(Number);
  return new Date(Date.UTC(y, m - 1, d));
}

export function toISO(date: Date): string {
  return date.toISOString().slice(0, 10);
}

export function addDays(iso: string, days: number): string {
  return toISO(new Date(parseISO(iso).getTime() + days * DAY));
}

export function diffDays(fromIso: string, toIso: string): number {
  return Math.round((parseISO(toIso).getTime() - parseISO(fromIso).getTime()) / DAY);
}

/** 0 = domingo … 6 = sábado */
export function weekday(iso: string): number {
  return parseISO(iso).getUTCDay();
}

/** Próxima segunda-feira a partir de `iso` (a própria data se já for segunda). */
export function nextMonday(iso: string): string {
  const wd = weekday(iso);
  return addDays(iso, (8 - wd) % 7);
}

/** Segunda-feira da semana (segunda a domingo) que contém `iso`. */
export function mondayOf(iso: string): string {
  return addDays(iso, -((weekday(iso) + 6) % 7));
}

/** Dia da semana no plano: 0 = segunda … 6 = domingo. */
export function dayIndexOf(iso: string): number {
  return (weekday(iso) + 6) % 7;
}

/** Nº de semanas (segunda a domingo) entre o início e a data da prova, contando a semana da prova. */
export function weeksUntil(startMonday: string, examIso: string): number {
  const days = diffDays(startMonday, examIso) + 1;
  return Math.max(0, Math.ceil(days / 7));
}
