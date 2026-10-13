import "server-only";
import { db } from "@/lib/db";
import { loadPlannerData } from "@/lib/data/planner-data";
import { loadContestPlanData } from "@/lib/data/contest-data";
import { getUserContest } from "@/lib/user-contest";
import { bandOf, dayIndexOf, generatePlan, mondayOf } from "@/lib/planner";
import { todayISO } from "@/lib/plan-time";
import { savePlan } from "@/lib/plan/persist";
import type { Contest } from "@/generated/prisma/client";
import type { Known, Level, PlanInput } from "@/lib/planner/types";

export interface RegenerateResult {
  success: boolean;
  message: string;
  planId?: string;
  version?: number;
}

/**
 * Reconstrói um planejamento existente nos moldes e regras atuais do sistema,
 * aproveitando integralmente as escolhas e respostas de anamnese fornecidas pelo aluno:
 * - Disciplinas e seus níveis de domínio
 * - Horas semanais de estudo e banca/concurso
 * - Respostas de anamnese por aula (1 = já estudei, 2 = domino)
 * - Modo Turbo e língua estrangeira
 * - Regras novas: importância no concurso, resumos analíticos, ciclo de intercalação e fixação
 */
export async function regeneratePlanForUser(
  userEmailOrPlanId: string,
  options?: { activate?: boolean }
): Promise<RegenerateResult> {
  const isEmail = userEmailOrPlanId.includes("@");

  const plan = isEmail
    ? await db.plan.findFirst({
        where: {
          user: { email: userEmailOrPlanId.toLowerCase().trim() },
          status: { in: ["PENDING_ANALYSIS", "ACTIVE"] },
        },
        orderBy: { version: "desc" },
        include: {
          user: { include: { profile: true } },
          subjects: true,
        },
      })
    : await db.plan.findUnique({
        where: { id: userEmailOrPlanId },
        include: {
          user: { include: { profile: true } },
          subjects: true,
        },
      });

  if (!plan) {
    return {
      success: false,
      message: `Nenhum planejamento pendente ou ativo encontrado para "${userEmailOrPlanId}".`,
    };
  }

  const user = plan.user;
  const userEmail = user.email;

  // 1. Concurso alvo
  const contest: Contest = plan.contest ?? (await getUserContest(userEmail));

  // 2. Horas por semana e perfil
  const params = (plan.params as Record<string, unknown>) ?? {};
  const hoursPerWeek =
    (params.hoursPerWeek as number) ?? user.profile?.hoursPerWeek ?? 20;

  // 3. Disciplinas e níveis
  const subjects: { id: string; level: Level }[] = plan.subjects.map((s) => ({
    id: s.subjectId,
    level: (s.level ?? 1) as Level,
  }));

  if (subjects.length === 0) {
    return {
      success: false,
      message: "O planejamento anterior não possui disciplinas selecionadas.",
    };
  }

  // 4. Anamnese (aulas conhecidas e dominadas)
  const known: Record<string, Known> = {};
  const diagnostics: Record<string, unknown> = {};

  for (const s of plan.subjects) {
    const diag = (s.diagnostic as Record<string, unknown>) ?? {};
    diagnostics[s.subjectId] = diag;
    const aulas = diag.aulas as Record<string, number> | undefined;
    if (aulas && typeof aulas === "object") {
      for (const [aulaId, val] of Object.entries(aulas)) {
        if (val === 1 || val === 2) {
          known[aulaId] = val as Known;
        }
      }
    }
  }

  // 5. Data de início e prova
  const today = todayISO();
  const originalStartStr = plan.startDate.toISOString().slice(0, 10);
  const examDateStr = plan.examDate.toISOString().slice(0, 10);

  // Se a data de início original já passou, inicia na data atual para não perder semanas
  const effectiveStart = originalStartStr < today ? today : originalStartStr;
  const startDate = mondayOf(effectiveStart);
  const firstDay = dayIndexOf(effectiveStart);

  // 6. Modo Turbo e Língua Estrangeira
  const savedRequest = (params.request as { turbo?: boolean; excludedAulas?: string[] } | undefined) ?? undefined;
  const turbo = Boolean(savedRequest?.turbo ?? params.turbo ?? false);
  const foreignLanguage =
    user.profile?.foreignLanguage ??
    (subjects.some((s) => s.id === "lingua-inglesa")
      ? "EN"
      : subjects.some((s) => s.id === "lingua-espanhola")
      ? "ES"
      : null);

  // 7. Carrega dados estruturais atualizados do catálogo e do concurso
  const data = await loadPlannerData();
  const contestData = await loadContestPlanData(contest);

  // 8. Monta a entrada para o gerador de plano atual
  const planInput: PlanInput = {
    ...data,
    contest,
    importance: contestData.importance,
    summaries: contestData.summaries,
    examQuestions: contestData.examQuestions,
    startDate,
    firstDay,
    examDate: examDateStr,
    hoursPerWeek,
    subjects,
    known,
    excludedAulas: savedRequest?.excludedAulas ?? [],
    turbo,
  };

  // 9. Gera o novo plano com todas as regras atualizadas
  const result = generatePlan(planInput);

  // 10. Persiste o novo plano arquivando o anterior
  const targetStatus: "ACTIVE" | "PENDING_ANALYSIS" =
    options?.activate || plan.status === "ACTIVE"
      ? "ACTIVE"
      : "PENDING_ANALYSIS";
  const newPlanId = await savePlan({
    userId: user.id,
    input: planInput,
    result,
    diagnostics,
    foreignLanguage,
    hoursBand:
      bandOf(hoursPerWeek) === "LEVE"
        ? "LEVE"
        : bandOf(hoursPerWeek) === "MODERADO"
        ? "MODERADO"
        : "AVANCADO",
    status: targetStatus,
  });

  return {
    success: true,
    planId: newPlanId,
    version: plan.version + 1,
    message: `Planejamento de ${user.name ?? user.email} re-elaborado com sucesso nas regras novas (Versão ${
      plan.version + 1
    }, status: ${targetStatus}).`,
  };
}
