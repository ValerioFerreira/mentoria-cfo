import "server-only";
import type { Contest } from "@/generated/prisma/client";
import { db } from "@/lib/db";
import { EXAM_CONFIGS, type SupportedSimuladoContest } from "@/lib/simulado-rules";
import { comboWeights, isCombo, mergeComboImportance, mergeComboQuestions, type ComboKey, type ComboMemberData } from "@/lib/combos";
import type { PlanInput } from "@/lib/planner/types";

/** Questões de cada disciplina na prova do concurso (Língua Estrangeira vale para Inglês e Espanhol). */
export function contestExamQuestions(contest: Contest): Record<string, number> {
  const cfg = (EXAM_CONFIGS as Partial<Record<Contest, (typeof EXAM_CONFIGS)[SupportedSimuladoContest]>>)[contest];
  const out: Record<string, number> = {};
  for (const s of cfg?.subjects ?? []) {
    if (s.subjectId === "FOREIGN_LANG") {
      out["lingua-inglesa"] = s.count;
      out["lingua-espanhola"] = s.count;
    } else out[s.subjectId] = s.count;
  }
  return out;
}

export interface ContestPlanData {
  /** nota 1–100 de cada trecho no concurso; null = fora do edital dele */
  importance: Record<string, number | null>;
  /** trechos com resumo analítico (rascunho ou aprovado) */
  summaries: string[];
  examQuestions: Record<string, number>;
  /** total de questões da prova (base da cobertura do edital); ausente no combo, que usa o total dos membros */
  examTotalQuestions?: number;
  /** pacote combo: concursos-membro com o peso de cada um (dependem da prioridade escolhida) */
  combo?: NonNullable<PlanInput["combo"]>;
}

const cache = new Map<string, { at: number; data: ContestPlanData }>();
const TTL_MS = 5 * 60_000;

/** Importância dos trechos no concurso e resumos analíticos disponíveis: insumos do planejador (Modo Turbo e filtro do edital). */
export async function loadContestPlanData(contest: Contest, priority?: string): Promise<ContestPlanData> {
  if (isCombo(contest)) return loadComboPlanData(contest, priority);
  const hit = cache.get(contest);
  if (hit && Date.now() - hit.at < TTL_MS) return hit.data;
  const [rows, sums] = await Promise.all([
    db.segmentImportance.findMany({ where: { contest }, select: { segmentId: true, appears: true, score: true } }),
    db.analyticSummary.findMany({ select: { segmentId: true } }),
  ]);
  const data: ContestPlanData = {
    // sem linhas de importância (banco ainda não semeado) o planejador não filtra nada
    importance: Object.fromEntries(rows.map((r) => [r.segmentId, r.appears ? r.score : null])),
    summaries: sums.map((s) => s.segmentId),
    examQuestions: contestExamQuestions(contest),
    examTotalQuestions: (EXAM_CONFIGS as Partial<Record<Contest, (typeof EXAM_CONFIGS)[SupportedSimuladoContest]>>)[contest]?.totalQuestions,
  };
  cache.set(contest, { at: Date.now(), data });
  return data;
}

/** Combo: edital pela união dos dois concursos, nota pelo percentil das questões esperadas ponderadas e peso W por disciplina. */
async function loadComboPlanData(combo: ComboKey, priority?: string): Promise<ContestPlanData> {
  const weights = comboWeights(combo, priority ?? "");
  const prio = weights.find((w) => w.weight === 1)!.contest;
  const key = `${combo}|${prio}`;
  const hit = cache.get(key);
  if (hit && Date.now() - hit.at < TTL_MS) return hit.data;
  const [rows, sums] = await Promise.all([
    db.segmentImportance.findMany({ where: { contest: { in: weights.map((w) => w.contest) } }, select: { segmentId: true, contest: true, appears: true, score: true, expected: true } }),
    db.analyticSummary.findMany({ select: { segmentId: true } }),
  ]);
  const members: ComboMemberData[] = weights.map(({ contest: c, weight }) => {
    const mine = rows.filter((r) => r.contest === c);
    return {
      contest: c,
      weight,
      importance: Object.fromEntries(mine.map((r) => [r.segmentId, r.appears ? r.score : null])),
      expected: Object.fromEntries(mine.map((r) => [r.segmentId, r.expected])),
      examQuestions: contestExamQuestions(c),
    };
  });
  const data: ContestPlanData = {
    importance: mergeComboImportance(members),
    summaries: sums.map((s) => s.segmentId),
    examQuestions: mergeComboQuestions(members),
    combo: {
      priority: prio,
      members: members.map((m) => ({
        contest: m.contest,
        weight: m.weight,
        totalQuestions: EXAM_CONFIGS[m.contest as SupportedSimuladoContest].totalQuestions,
        examQuestions: m.examQuestions,
      })),
    },
  };
  cache.set(key, { at: Date.now(), data });
  return data;
}
