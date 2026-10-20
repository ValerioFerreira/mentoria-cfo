"use server";

import { redirect } from "next/navigation";
import { requireUser } from "@/lib/auth/dal";
import { db } from "@/lib/db";
import { subjectName } from "@/lib/ui-format";
import { canUserAccessCoreFeatures } from "@/lib/system-settings";
import { getUserContest, getUserEditalSubjects } from "@/lib/user-contest";
import { hideInedita } from "@/lib/quiz/banca";
import { filterByTopics, makeTopicResolver } from "@/lib/quiz/topic-map";

const OUTSIDE_EDITAL = "Esta disciplina não faz parte do edital do seu concurso.";

function shuffle<T>(arr: T[]): T[] {
  const copy = [...arr];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

// "topic" é o id do item do edital do concurso do aluno (ou "outros" para as questões sem item); "bancas" vazio = todas.
// O assunto de cada questão é resolvido por `makeTopicResolver` (no PCPE, as questões de aulas que o edital dele trata
// entram nos assuntos próprios dele), então o filtro por assunto é feito aqui, e não no banco.
async function topicResolver(contest: Parameters<typeof makeTopicResolver>[1]) {
  const items = await db.editalItem.findMany({ select: { id: true, subjectId: true, onlyContests: true, excludeContests: true, aulaIds: true } });
  return makeTopicResolver(items.map((i) => ({ ...i, aulaIds: (i.aulaIds as string[]) ?? [] })), contest);
}

export async function startSubjectPracticeQuiz(input: {
  subjectId: string;
  topic?: string;
  limit?: number;
  bancas?: string[];
}): Promise<{ error: string } | never> {
  const user = await requireUser();
  if (!(await canUserAccessCoreFeatures(user.role, user.id))) {
    return { error: "O Banco de Questões está em fase final de validação e será liberado em breve." };
  }
  if (!(await getUserEditalSubjects(user.email)).includes(input.subjectId)) {
    return { error: OUTSIDE_EDITAL };
  }

  const contest = await getUserContest(user.email);
  const whereClause: any = {
    subjectId: input.subjectId,
    status: "APPROVED",
    ...hideInedita(contest),
  };

  if (input.bancas && input.bancas.length > 0) {
    whereClause.banca = { in: input.bancas };
  }

  const candidates = await db.question.findMany({
    where: whereClause,
    select: { id: true, segmentId: true, subjectId: true, aulaId: true, editalItemId: true },
  });
  const topic = input.topic?.trim();
  const questions = topic ? filterByTopics(candidates, [topic], await topicResolver(contest)) : candidates;

  if (questions.length === 0) {
    return { error: "Nenhuma questão disponível para este filtro no momento." };
  }

  // Verificar histórico do usuário para dar prioridade a questões não vistas
  const history = await db.quizAnswer.findMany({
    where: {
      session: { userId: user.id },
      questionId: { in: questions.map((q) => q.id) },
      chosenLabel: { not: null },
    },
    select: { questionId: true },
  });

  const seenIds = new Set(history.map((h) => h.questionId));

  // Separar não respondidas e respondidas
  const unseen = questions.filter((q) => !seenIds.has(q.id));
  const seen = questions.filter((q) => seenIds.has(q.id));

  const pool = [...shuffle(unseen), ...shuffle(seen)];
  const want = input.limit && input.limit > 0 ? Math.min(input.limit, pool.length) : pool.length;
  const selected = pool.slice(0, want);

  const sessionId = crypto.randomUUID();

  await db.quizSession.create({
    data: {
      id: sessionId,
      userId: user.id,
      activityId: null, // Prática livre não atrelada a atividade de semana
      kind: "CADERNO",
      limitSeconds: Math.max(3600, selected.length * 180),
      total: selected.length,
      answers: {
        create: selected.map((q, i) => ({
          questionId: q.id,
          position: i + 1,
        })),
      },
    },
  });

  redirect(`/questoes/pratica/${sessionId}`);
}

export interface CustomNotebookItemInput {
  subjectId: string;
  topics?: string[]; // ids dos itens do edital ("outros" = sem item); se vazio, todos os assuntos da matéria
  count?: number; // quantidade para esta seleção específica (no modo por matéria)
}

export interface CreateCustomNotebookInput {
  title?: string;
  mode: "TOTAL" | "PER_SUBJECT";
  totalCount?: number; // usado quando mode === 'TOTAL'
  items: CustomNotebookItemInput[];
}

/**
 * Cria um caderno personalizado conforme especificações do aluno:
 * - Múltiplas disciplinas
 * - Todos os assuntos ou assuntos específicos
 * - Quantidade total ou por disciplina
 * - Validação estrita de suficiência (sem repetição de questões)
 */
export async function createCustomNotebook(
  input: CreateCustomNotebookInput
): Promise<{ error: string } | never> {
  const user = await requireUser();
  if (!(await canUserAccessCoreFeatures(user.role, user.id))) {
    return { error: "A montagem de cadernos está em fase final de validação e será liberada em breve." };
  }

  if (!input.items || input.items.length === 0) {
    return { error: "Selecione ao menos uma disciplina para montar o caderno." };
  }
  const edital = new Set(await getUserEditalSubjects(user.email));
  if (input.items.some((item) => !edital.has(item.subjectId))) {
    return { error: OUTSIDE_EDITAL };
  }

  const selectedQuestionIds = new Set<string>();
  const contest = await getUserContest(user.email);
  const hide = hideInedita(contest);
  const resolve = await topicResolver(contest);

  if (input.mode === "TOTAL") {
    // Modo Quantidade Total: seleciona aleatoriamente entre o universo dos filtros escolhidos
    const requestedTotal = input.totalCount && input.totalCount > 0 ? input.totalCount : 20;

    // Questões das matérias escolhidas; o filtro por assunto vale por matéria (assunto do edital do concurso do aluno)
    const candidates = await db.question.findMany({
      where: { OR: input.items.map((item) => ({ subjectId: item.subjectId, status: "APPROVED" as const, ...hide })) },
      select: { id: true, subjectId: true, aulaId: true, editalItemId: true },
    });
    const availableQuestions = input.items.flatMap((item) =>
      filterByTopics(candidates.filter((q) => q.subjectId === item.subjectId), item.topics, resolve),
    );

    if (availableQuestions.length === 0) {
      return { error: "Não foram encontradas questões aprovadas para os filtros selecionados." };
    }

    if (requestedTotal > availableQuestions.length) {
      return {
        error: `A quantidade solicitada (${requestedTotal}) é maior do que o total disponível para essa seleção (${availableQuestions.length} questões disponíveis). Ajuste a quantidade ou amplie a seleção.`,
      };
    }

    // Priorizar questões ainda não vistas pelo usuário
    const history = await db.quizAnswer.findMany({
      where: {
        session: { userId: user.id },
        questionId: { in: availableQuestions.map((q) => q.id) },
        chosenLabel: { not: null },
      },
      select: { questionId: true },
    });
    const seenIds = new Set(history.map((h) => h.questionId));

    const unseen = availableQuestions.filter((q) => !seenIds.has(q.id));
    const seen = availableQuestions.filter((q) => seenIds.has(q.id));

    const pool = [...shuffle(unseen), ...shuffle(seen)];
    const picked = pool.slice(0, requestedTotal);
    for (const q of picked) selectedQuestionIds.add(q.id);
  } else {
    // Modo Por Disciplina/Assunto: cada item define sua quantidade
    for (const item of input.items) {
      const want = item.count && item.count > 0 ? item.count : 5;

      const subjectQuestions = await db.question.findMany({
        where: { subjectId: item.subjectId, status: "APPROVED", ...hide },
        select: { id: true, subjectId: true, aulaId: true, editalItemId: true },
      });
      const questions = filterByTopics(subjectQuestions, item.topics, resolve);

      if (questions.length < want) {
        const sName = subjectName(item.subjectId);
        return {
          error: `Não há questões suficientes para ${sName}. Solicitadas: ${want}, disponíveis no acervo: ${questions.length}.`,
        };
      }

      const shuffled = shuffle(questions);
      const picked = shuffled.slice(0, want);
      for (const q of picked) selectedQuestionIds.add(q.id);
    }
  }

  const finalQuestions = Array.from(selectedQuestionIds);
  if (finalQuestions.length === 0) {
    return { error: "Nenhuma questão selecionada para este caderno." };
  }

  const sessionId = crypto.randomUUID();
  const title = input.title?.trim() || `Caderno Personalizado (${finalQuestions.length} questões)`;

  await db.quizSession.create({
    data: {
      id: sessionId,
      userId: user.id,
      activityId: null,
      kind: "CADERNO_PERSONALIZADO",
      title,
      limitSeconds: Math.max(3600, finalQuestions.length * 180),
      total: finalQuestions.length,
      answers: {
        create: finalQuestions.map((questionId, i) => ({
          questionId,
          position: i + 1,
        })),
      },
    },
  });

  redirect(`/questoes/pratica/${sessionId}`);
}
