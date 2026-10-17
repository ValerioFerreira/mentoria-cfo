import "server-only";
import { db } from "@/lib/db";
import { contestBancas } from "@/lib/quiz/banca";
import { EXAM_CONFIGS, type ContestExamConfig, type SupportedSimuladoContest } from "@/lib/simulado-rules";

export * from "@/lib/simulado-rules";

/** Temporarily disables the official simulados module for all users. */
export const SIMULADOS_ENABLED = false;

export interface SubjectReadiness {
  subjectId: string;
  name: string;
  block: "I" | "II" | "III";
  required: number;
  available: number;
  isSufficient: boolean;
}

export interface SimuladoReadiness {
  contest: SupportedSimuladoContest;
  config: ContestExamConfig;
  isReady: boolean;
  totalRequired: number;
  totalAvailable: number;
  foreignLang: "lingua-inglesa" | "lingua-espanhola";
  subjects: SubjectReadiness[];
  insufficientSubjects: SubjectReadiness[];
}

/**
 * Diagnóstico de disponibilidade de acervo para montar o simulado completo conforme edital oficial.
 * Exclusivamente com questões da banca AOCP / Instituto AOCP.
 */
export async function checkSimuladoReadiness(
  contest: SupportedSimuladoContest,
  foreignLang: "lingua-inglesa" | "lingua-espanhola" = "lingua-inglesa"
): Promise<SimuladoReadiness> {
  const config = EXAM_CONFIGS[contest];

  // Contar questões aprovadas da banca AOCP por disciplina
  const counts = await db.question.groupBy({
    by: ["subjectId"],
    where: {
      status: "APPROVED",
      banca: { in: contestBancas(contest) },
      kind: "MULTIPLA_ESCOLHA", // a prova é de múltipla escolha; itens Certo/Errado ficam fora do simulado
    },
    _count: true,
  });

  const countMap = new Map<string, number>();
  for (const c of counts) {
    countMap.set(c.subjectId, c._count);
  }

  const subjects: SubjectReadiness[] = [];
  const insufficientSubjects: SubjectReadiness[] = [];
  let totalAvailable = 0;

  for (const s of config.subjects) {
    const actualSubId = s.subjectId === "FOREIGN_LANG" ? foreignLang : s.subjectId;
    const actualName =
      s.subjectId === "FOREIGN_LANG"
        ? foreignLang === "lingua-inglesa"
          ? "Língua Inglesa"
          : "Língua Espanhola"
        : s.name;

    const available = countMap.get(actualSubId) ?? 0;
    const isSufficient = available >= s.count;

    const item: SubjectReadiness = {
      subjectId: actualSubId,
      name: actualName,
      block: s.block,
      required: s.count,
      available,
      isSufficient,
    };

    subjects.push(item);
    totalAvailable += Math.min(available, s.count);

    if (!isSufficient) {
      insufficientSubjects.push(item);
    }
  }

  const isReady = insufficientSubjects.length === 0;

  return {
    contest,
    config,
    isReady,
    totalRequired: config.totalQuestions,
    totalAvailable,
    foreignLang,
    subjects,
    insufficientSubjects,
  };
}

/**
 * Recupera o histórico de simulados realizados pelo usuário.
 */
export async function getUserSimulados(userId: string) {
  const sessions = await db.quizSession.findMany({
    where: {
      userId,
      kind: "SIMULADO",
    },
    orderBy: { startedAt: "desc" },
    include: {
      answers: {
        select: {
          id: true,
          position: true,
          chosenLabel: true,
          isCorrect: true,
          question: {
            select: {
              subjectId: true,
              subject: { select: { block: true, name: true } },
            },
          },
        },
      },
    },
  });

  return sessions.map((s) => {
    const isFinished = s.finishedAt !== null;
    const contestKey = (s.contest as SupportedSimuladoContest) || "CBMPE_OFICIAL";
    const config = EXAM_CONFIGS[contestKey] || EXAM_CONFIGS.CBMPE_OFICIAL;

    const score = s.score ?? 0;
    const total = s.total ?? config.totalQuestions;

    // Calcular veredito de corte se finalizado
    let passedCutoff = false;
    const cutoffDetails = {
      blockI: { correct: 0, total: config.blocks.I.totalQuestions, passed: false },
      blockII: { correct: 0, total: config.blocks.II.totalQuestions, passed: false },
      blockIII: { correct: 0, total: config.blocks.III?.totalQuestions ?? 0, passed: !config.blocks.III },
      noZeroPassed: true,
    };

    if (isFinished) {
      const answers = s.answers;
      const subCorrect = new Map<string, number>();

      for (const a of answers) {
        const blk = a.question.subject.block;
        const sid = a.question.subjectId;
        if (!subCorrect.has(sid)) subCorrect.set(sid, 0);

        if (a.isCorrect) {
          if (blk === "I") cutoffDetails.blockI.correct++;
          if (blk === "II") cutoffDetails.blockII.correct++;
          if (blk === "III") cutoffDetails.blockIII.correct++;
          subCorrect.set(sid, (subCorrect.get(sid) ?? 0) + 1);
        }
      }

      cutoffDetails.blockI.passed = cutoffDetails.blockI.correct >= config.blocks.I.minQuestions;
      cutoffDetails.blockII.passed = cutoffDetails.blockII.correct >= config.blocks.II.minQuestions;
      cutoffDetails.blockIII.passed = config.blocks.III
        ? cutoffDetails.blockIII.correct >= config.blocks.III.minQuestions
        : true;

      // Verificar se zerou alguma disciplina apenas se a regra exigir
      if (config.noZeroInAnyArea) {
        const distinctSubjects = new Set(answers.map((a) => a.question.subjectId));
        for (const sid of distinctSubjects) {
          if ((subCorrect.get(sid) ?? 0) === 0) {
            cutoffDetails.noZeroPassed = false;
            break;
          }
        }
      }

      const minTotalScore = (config.minPercentTotal / 100) * total;
      passedCutoff =
        cutoffDetails.blockI.passed &&
        cutoffDetails.blockII.passed &&
        cutoffDetails.blockIII.passed &&
        cutoffDetails.noZeroPassed &&
        score >= minTotalScore;
    }

    return {
      id: s.id,
      title: s.title ?? config.title,
      contest: contestKey,
      roleName: config.role,
      startedAt: s.startedAt,
      finishedAt: s.finishedAt,
      isFinished,
      score,
      total,
      percent: total > 0 ? Math.round((score / total) * 100) : 0,
      passedCutoff,
      cutoffDetails,
    };
  });
}
