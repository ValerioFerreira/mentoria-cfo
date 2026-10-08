// Diagnóstico rápido por disciplina: 3 perguntas → nível 0–3 (afeta prioridade, profundidade e revisões).
import type { Level } from "@/lib/planner/types";

export type Experience = 0 | 1 | 2 | 3; // nunca · escola · concurso (>6 m) · concurso (<6 m)
export type SelfRating = 1 | 2 | 3 | 4 | 5;
export type HitRate = "none" | "low" | "mid" | "high"; // não fiz · <50% · 50–70% · >70%

export interface DiagnosticAnswer {
  experience: Experience;
  self: SelfRating;
  hitRate: HitRate;
}

export const EXPERIENCE_OPTIONS: { value: Experience; label: string; hint: string }[] = [
  { value: 0, label: "Nunca estudei", hint: "É assunto novo para mim" },
  { value: 1, label: "Só na escola", hint: "Vi há bastante tempo" },
  { value: 2, label: "Já estudei para concursos", hint: "Há mais de 6 meses" },
  { value: 3, label: "Estudei recentemente", hint: "Nos últimos 6 meses" },
];

export const SELF_OPTIONS: { value: SelfRating; label: string }[] = [
  { value: 1, label: "Zero" },
  { value: 2, label: "Fraco" },
  { value: 3, label: "Razoável" },
  { value: 4, label: "Bom" },
  { value: 5, label: "Domino" },
];

export const HIT_OPTIONS: { value: HitRate; label: string }[] = [
  { value: "none", label: "Não fiz questões" },
  { value: "low", label: "Menos de 50%" },
  { value: "mid", label: "50% a 70%" },
  { value: "high", label: "Mais de 70%" },
];

export const DEFAULT_ANSWER: DiagnosticAnswer = { experience: 0, self: 1, hitRate: "none" };

export function levelFromAnswer(a: DiagnosticAnswer): Level {
  const exp = a.experience / 3;
  const self = (a.self - 1) / 4;
  const hit = a.hitRate === "none" ? null : a.hitRate === "low" ? 0 : a.hitRate === "mid" ? 0.5 : 1;
  const score = hit === null ? 0.45 * exp + 0.55 * self : 0.3 * exp + 0.4 * self + 0.3 * hit;
  return score < 0.2 ? 0 : score < 0.45 ? 1 : score < 0.75 ? 2 : 3;
}

export const LEVEL_LABEL: Record<Level, string> = { 0: "Iniciante", 1: "Básico", 2: "Intermediário", 3: "Avançado" };
