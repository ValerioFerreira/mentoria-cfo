import { HOURS_BANDS } from "./constants";

export type Band = keyof typeof HOURS_BANDS;

export function bandOf(hoursPerWeek: number): Band {
  if (hoursPerWeek <= HOURS_BANDS.LEVE.max) return "LEVE";
  if (hoursPerWeek <= HOURS_BANDS.MODERADO.max) return "MODERADO";
  return "AVANCADO";
}

function fmt(hours: number): string {
  const h = Math.floor(hours);
  const m = Math.round((hours - h) * 60);
  return m === 0 ? `${h}h` : `${h}h${String(m).padStart(2, "0")}`;
}

/** "≈ 2h a 3h por dia" a partir de horas por semana (7 dias). */
export function hoursPerDayLabel(band: Band): string {
  const { min, max } = HOURS_BANDS[band];
  if (band === "AVANCADO") return `mais de ${fmt((min - 1) / 7)} por dia`;
  return `${fmt(min / 7)} a ${fmt(max / 7)} por dia`;
}
