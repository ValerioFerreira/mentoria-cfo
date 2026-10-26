import type { Contest } from "@/generated/prisma/client";
import type { ContestPlanData } from "@/lib/data/contest-data";
import type { PlannerData } from "@/lib/data/planner-data";
import type { Known, Level, PlanInput } from "@/lib/planner/types";

/** Monta a entrada do planejador a partir dos dados do catálogo, do concurso (ou combo) e das escolhas do aluno. */
export function buildPlanInput(args: {
  data: PlannerData;
  contest: Contest;
  contestData: ContestPlanData;
  startDate: string;
  firstDay: number;
  examDate: string;
  hoursPerWeek: number;
  subjects: { id: string; level: Level }[];
  known: Record<string, Known>;
  excludedAulas: string[];
  turbo: boolean;
}): PlanInput {
  const { data, contest, contestData, ...rest } = args;
  return {
    ...data,
    contest,
    importance: contestData.importance,
    summaries: contestData.summaries,
    examQuestions: contestData.examQuestions,
    ...(contestData.examTotalQuestions ? { examTotalQuestions: contestData.examTotalQuestions } : {}),
    ...(contestData.combo ? { combo: contestData.combo } : {}),
    ...rest,
  };
}
