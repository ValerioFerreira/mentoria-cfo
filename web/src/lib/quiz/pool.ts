import type { Contest } from "@/generated/prisma/client";
import { db } from "@/lib/db";
import { activityQuizWhere, reinforcementQuizWhere, usesReinforcement } from "./banca";
import { servableStatuses } from "./servable";

export const DEFAULT_QUIZ_QUESTIONS = 25;

export interface QuizPoolActivity {
  planId: string;
  subjectId: string;
  dayIndex: number | null;
  quizQuestions: number | null;
  week: { index: number };
  segments: { segmentId: string }[];
}

export interface PoolQuestion {
  id: string;
  segmentId: string;
}

export interface QuizPool {
  /** questões dos trechos do próprio caderno */
  primary: PoolQuestion[];
  /** questões de trechos da mesma disciplina que o plano já mandou estudar antes (só quando o caderno fica curto) */
  extra: PoolQuestion[];
  /** reforço (só concursos em REFORCO_CONTESTS): outras bancas em múltipla escolha e inéditas, dos trechos do caderno e dos já estudados; só entra quando as duas listas acima não bastam */
  reinforcement: PoolQuestion[];
}

export const poolSize = (p: QuizPool): number => p.primary.length + p.extra.length + p.reinforcement.length;

/** Trechos da mesma disciplina cujas Teorias vêm antes da atividade na ordem do plano (semana e dia). */
async function priorSegmentIds(a: QuizPoolActivity): Promise<string[]> {
  if (a.dayIndex === null) return []; // planos antigos, sem dia: não dá para saber o que veio antes
  const rows = await db.activity.findMany({
    where: {
      planId: a.planId,
      type: "TEORIA",
      subjectId: a.subjectId,
      OR: [{ week: { index: { lt: a.week.index } } }, { week: { index: a.week.index }, dayIndex: { lt: a.dayIndex } }],
    },
    select: { segments: { select: { segmentId: true } } },
  });
  const own = new Set(a.segments.map((s) => s.segmentId));
  return [...new Set(rows.flatMap((r) => r.segments.map((s) => s.segmentId)))].filter((id) => !own.has(id));
}

/**
 * Questões do caderno de uma atividade do plano. O caderno usa os trechos da própria atividade; se eles não somam o que o
 * caderno pede (25, ou 15 no Turbo), completa com questões de trechos da mesma disciplina que o aluno já viu na Teoria,
 * nunca com trecho ainda não estudado.
 */
export async function loadQuizPool(a: QuizPoolActivity, contest: Contest | null): Promise<QuizPool> {
  const select = { id: true, segmentId: true } as const;
  const own = a.segments.map((s) => s.segmentId);
  const primary = await db.question.findMany({ where: activityQuizWhere(own, servableStatuses(), contest), select });
  const want = a.quizQuestions ?? DEFAULT_QUIZ_QUESTIONS;
  if (primary.length >= want) return { primary, extra: [], reinforcement: [] };
  const prior = await priorSegmentIds(a);
  const extra = prior.length > 0 ? await db.question.findMany({ where: activityQuizWhere(prior, servableStatuses(), contest), select }) : [];
  if (primary.length + extra.length >= want || !usesReinforcement(contest)) return { primary, extra, reinforcement: [] };
  const reinforcement = await db.question.findMany({ where: reinforcementQuizWhere([...own, ...prior], servableStatuses()), select });
  return { primary, extra, reinforcement };
}
