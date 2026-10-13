import "server-only";
import type { Contest } from "@/generated/prisma/client";
import { db } from "@/lib/db";
import { EXAM_CONFIGS, type SupportedSimuladoContest } from "@/lib/simulado-rules";

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
}

const cache = new Map<Contest, { at: number; data: ContestPlanData }>();
const TTL_MS = 5 * 60_000;

/** Importância dos trechos no concurso e resumos analíticos disponíveis: insumos do planejador (Modo Turbo e filtro do edital). */
export async function loadContestPlanData(contest: Contest): Promise<ContestPlanData> {
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
  };
  cache.set(contest, { at: Date.now(), data });
  return data;
}
