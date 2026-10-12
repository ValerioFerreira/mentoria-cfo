"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";
import { requireUser } from "@/lib/auth/dal";
import { db } from "@/lib/db";
import { EXAM_CONFIGS, SIMULADOS_ENABLED, checkSimuladoReadiness, type SupportedSimuladoContest } from "@/lib/data/simulados";
import { canUserAccessCoreFeatures } from "@/lib/system-settings";

function shuffle<T>(arr: T[]): T[] {
  const copy = [...arr];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

/**
 * Cria e inicia uma nova sessão de Simulado Oficial do Edital.
 * Valida previamente se todas as disciplinas possuem questões suficientes.
 * NÃO gera simulado incompleto se faltar qualquer disciplina.
 */
export async function startSimuladoSession(input: {
  contest: SupportedSimuladoContest;
  foreignLang?: "lingua-inglesa" | "lingua-espanhola";
}): Promise<{ error: string } | never> {
  const user = await requireUser();
  if (!SIMULADOS_ENABLED) {
    return { error: "Os simulados estão temporariamente indisponíveis. Em breve, você poderá acessá-los novamente." };
  }

  if (!(await canUserAccessCoreFeatures(user.role))) {
    return { error: "A realização de simulados oficiais está em fase final de validação e será liberada em breve." };
  }

  const foreignLang = input.foreignLang || "lingua-inglesa";

  // 1. Verificação prévia e rigorosa de suficiência do acervo
  const readiness = await checkSimuladoReadiness(input.contest, foreignLang);
  if (!readiness.isReady) {
    const missingNames = readiness.insufficientSubjects
      .map((s) => `${s.name} (${s.available}/${s.required})`)
      .join(", ");
    return {
      error: `Não é possível gerar o simulado completo: acervo insuficiente nas seguintes disciplinas: ${missingNames}. A plataforma não gera simulados com grade divergente do edital.`,
    };
  }

  const config = EXAM_CONFIGS[input.contest];
  const selectedQuestionIds: string[] = [];

  // 2. Seleção aleatória das questões dentro de cada disciplina sem repetição (apenas banca AOCP)
  for (const s of config.subjects) {
    const actualSubId = s.subjectId === "FOREIGN_LANG" ? foreignLang : s.subjectId;
    const questions = await db.question.findMany({
      where: {
        subjectId: actualSubId,
        status: "APPROVED",
        banca: { in: ["AOCP", "Instituto AOCP", "INSTITUTO AOCP"] },
        kind: "MULTIPLA_ESCOLHA", // a prova é de múltipla escolha; itens Certo/Errado ficam fora do simulado
      },
      select: { id: true },
    });

    const shuffled = shuffle(questions);
    const picked = shuffled.slice(0, s.count);

    if (picked.length < s.count) {
      return {
        error: `Não foi possível selecionar ${s.count} questões para ${s.name}.`,
      };
    }

    for (const q of picked) {
      selectedQuestionIds.push(q.id);
    }
  }

  const sessionId = crypto.randomUUID();

  // 3. Criação da sessão oficial no banco de dados
  await db.quizSession.create({
    data: {
      id: sessionId,
      userId: user.id,
      activityId: null,
      kind: "SIMULADO",
      contest: input.contest,
      title: `Simulado Oficial — ${config.role}`,
      limitSeconds: config.durationSeconds,
      startedAt: new Date(),
      total: selectedQuestionIds.length,
      answers: {
        create: selectedQuestionIds.map((questionId, index) => ({
          questionId,
          position: index + 1,
        })),
      },
    },
  });

  redirect(`/simulados/${sessionId}`);
}

/**
 * Salva a resposta do simulado no servidor em tempo real (resistente a recarregamento F5).
 * NÃO revela gabarito, acerto ou erro para o aluno enquanto o simulado estiver em andamento.
 */
export async function saveSimuladoAnswer(input: {
  sessionId: string;
  position: number;
  chosenLabel: string | null;
  flagged?: boolean;
}): Promise<{ ok: boolean; error?: string }> {
  const user = await requireUser();
  if (!SIMULADOS_ENABLED) {
    return { ok: false, error: "Os simulados estão temporariamente indisponíveis." };
  }

  const session = await db.quizSession.findFirst({
    where: {
      id: input.sessionId,
      userId: user.id,
    },
    select: { id: true, startedAt: true, limitSeconds: true, finishedAt: true },
  });

  if (!session) return { ok: false, error: "Simulado não encontrado." };
  if (session.finishedAt) return { ok: false, error: "Este simulado já foi encerrado." };

  // Tolerância de 30 segundos após o término para envios em rede lenta
  const maxAllowedTime = session.startedAt.getTime() + (session.limitSeconds + 30) * 1000;
  if (Date.now() > maxAllowedTime) {
    return { ok: false, error: "Tempo de prova esgotado." };
  }

  const answer = await db.quizAnswer.findUnique({
    where: {
      sessionId_position: {
        sessionId: session.id,
        position: input.position,
      },
    },
    include: {
      question: {
        include: {
          options: true,
        },
      },
    },
  });

  if (!answer) return { ok: false, error: "Questão não encontrada." };

  const label = input.chosenLabel && "ABCDE".includes(input.chosenLabel) ? input.chosenLabel : null;
  const correctOption = answer.question.options.find((o) => o.isCorrect);
  const isHit = label && correctOption ? correctOption.label === label : null;

  await db.quizAnswer.update({
    where: { id: answer.id },
    data: {
      chosenLabel: label,
      isCorrect: isHit,
      flagged: input.flagged ?? answer.flagged,
      answeredAt: label ? new Date() : null,
    },
  });

  // Retorna apenas sucesso, SEM revelar isCorrect ou explicação!
  return { ok: true };
}

/**
 * Finaliza o simulado oficialmente (por entrega manual ou ao zerar o tempo),
 * calcula o score e gera o registro de tempo oficial.
 */
export async function finishSimulado(sessionId: string): Promise<{ ok: boolean; error?: string }> {
  const user = await requireUser();
  if (!SIMULADOS_ENABLED) {
    return { ok: false, error: "Os simulados estão temporariamente indisponíveis." };
  }

  const session = await db.quizSession.findFirst({
    where: {
      id: sessionId,
      userId: user.id,
    },
    include: {
      answers: {
        include: {
          question: {
            include: { options: true },
          },
        },
      },
    },
  });

  if (!session) return { ok: false, error: "Simulado não encontrado." };
  if (session.finishedAt) return { ok: true }; // Já finalizado

  // Revalidar acertos de todas as respostas
  let totalScore = 0;
  for (const a of session.answers) {
    const correctOpt = a.question.options.find((o) => o.isCorrect);
    const hit = a.chosenLabel && correctOpt ? a.chosenLabel === correctOpt.label : false;
    if (hit) totalScore++;

    await db.quizAnswer.update({
      where: { id: a.id },
      data: { isCorrect: hit },
    });
  }

  const now = new Date();
  const elapsed = Math.min(
    session.limitSeconds,
    Math.max(1, Math.round((now.getTime() - session.startedAt.getTime()) / 1000))
  );

  await db.$transaction([
    db.quizSession.update({
      where: { id: session.id },
      data: {
        finishedAt: now,
        score: totalScore,
      },
    }),
    db.timeLog.create({
      data: {
        userId: user.id,
        activityId: null,
        seconds: elapsed,
        startedAt: session.startedAt,
        endedAt: now,
        source: "TIMER",
        note: `Simulado Oficial (${session.contest ?? "CBMPE"})`,
      },
    }),
  ]);

  revalidatePath("/simulados");
  revalidatePath("/desempenho");

  return { ok: true };
}
