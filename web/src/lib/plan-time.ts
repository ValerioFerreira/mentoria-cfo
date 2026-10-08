// Calendário do plano (funções puras): em que semana/dia do plano estamos e em que dia cai cada atividade.
// As datas são "dia civil" no fuso do aluno (Recife), em AAAA-MM-DD.

export const APP_TIMEZONE = "America/Recife";
const DAY_MS = 86_400_000;

/** Dia civil de `now` no fuso do aluno. */
export function todayISO(now: Date = new Date()): string {
  return new Intl.DateTimeFormat("en-CA", { timeZone: APP_TIMEZONE, year: "numeric", month: "2-digit", day: "2-digit" }).format(now);
}

const asUTC = (iso: string) => {
  const [y, m, d] = iso.split("-").map(Number);
  return Date.UTC(y, m - 1, d);
};

export function addDaysISO(iso: string, days: number): string {
  return new Date(asUTC(iso) + days * DAY_MS).toISOString().slice(0, 10);
}

export function diffDaysISO(fromIso: string, toIso: string): number {
  return Math.round((asUTC(toIso) - asUTC(fromIso)) / DAY_MS);
}

export interface PlanPosition {
  state: "before" | "during" | "after";
  /** semana do plano (1…N), já limitada ao intervalo */
  week: number;
  /** dia da semana (0 = segunda … 6 = domingo) */
  day: number;
  /** dias desde o início do plano (negativo antes do início) */
  offset: number;
}

/** Dia em que o aluno começa a estudar: a semana 1 sempre começa numa segunda, mas o aluno pode entrar no meio dela. */
export function firstStudyISO(plan: { startDate: Date; params: unknown }): string {
  const startIso = plan.startDate.toISOString().slice(0, 10);
  const p = plan.params as { firstStudyDate?: string } | null;
  return p?.firstStudyDate && /^\d{4}-\d{2}-\d{2}$/.test(p.firstStudyDate) ? p.firstStudyDate : startIso;
}

/** A semana 1 começa numa segunda-feira, então o dia da semana é offset % 7. Antes de `firstStudyIso` o plano ainda não começou. */
export function planPosition(startIso: string, totalWeeks: number, today: string, firstStudyIso: string = startIso): PlanPosition {
  const offset = diffDaysISO(startIso, today);
  if (offset < 0 || today < firstStudyIso) return { state: "before", week: 1, day: 0, offset };
  if (offset >= totalWeeks * 7) return { state: "after", week: totalWeeks, day: 6, offset };
  return { state: "during", week: Math.floor(offset / 7) + 1, day: offset % 7, offset };
}

/** Dia da semana de uma data civil: 0 = segunda … 6 = domingo. */
export function dayOfWeekIndex(iso: string): number {
  return (new Date(asUTC(iso)).getUTCDay() + 6) % 7;
}

/** Data civil de um dia do plano. */
export function dateOfPlanDay(startIso: string, week: number, day: number): string {
  return addDaysISO(startIso, (week - 1) * 7 + day);
}

/**
 * Dia efetivo de cada atividade da semana. Planos antigos (sem `dayIndex`) são espalhados em segunda…sábado
 * seguindo a ordem do plano.
 */
export function effectiveDays<T extends { dayIndex: number | null; sortOrder: number }>(activities: T[]): (T & { day: number })[] {
  const ordered = [...activities].sort((a, b) => a.sortOrder - b.sortOrder);
  return ordered.map((a, i) => ({ ...a, day: a.dayIndex ?? Math.min(5, Math.floor((i * 6) / Math.max(1, ordered.length))) }));
}

const WEEKDAY = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"] as const;
export const weekdayName = (day: number) => WEEKDAY[day] ?? "";

/** "Quarta-feira, 14 de outubro" */
export function longDate(iso: string): string {
  const d = new Date(asUTC(iso));
  const dow = ["domingo", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado"][d.getUTCDay()];
  const rest = new Intl.DateTimeFormat("pt-BR", { day: "numeric", month: "long", timeZone: "UTC" }).format(d);
  return `${dow[0].toUpperCase()}${dow.slice(1)}, ${rest}`;
}

/** "14/10" */
export function shortDate(iso: string): string {
  const [, m, d] = iso.split("-");
  return `${d}/${m}`;
}
