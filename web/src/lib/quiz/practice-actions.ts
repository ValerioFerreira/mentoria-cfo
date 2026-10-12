"use server";

import { redirect } from "next/navigation";
import { requireUser } from "@/lib/auth/dal";
import { db } from "@/lib/db";
import { subjectName } from "@/lib/ui-format";
import { canUserAccessCoreFeatures } from "@/lib/system-settings";

function shuffle<T>(arr: T[]): T[] {
  const copy = [...arr];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

// "topic" é o id do item do edital (ou "outros" para as questões sem item); "bancas" vazio = todas.
function topicWhere(topic: string): Record<string, unknown> {
  return topic === "outros" ? { editalItemId: null } : { editalItemId: topic };
}

function topicsWhere(topics: string[]): Record<string, unknown>[] {
  const ids = topics.filter((t) => t !== "outros");
  const out: Record<string, unknown>[] = [];
  if (ids.length) out.push({ editalItemId: { in: ids } });
  if (topics.includes("outros")) out.push({ editalItemId: null });
  return out;
}

export async function startSubjectPracticeQuiz(input: {
  subjectId: string;
  topic?: string;
  limit?: number;
  bancas?: string[];
}): Promise<{ error: string } | never> {
  const user = await requireUser();
  if (!(await canUserAccessCoreFeatures(user.role))) {
    return { error: "O Banco de Questões está em fase final de validação e será liberado em breve." };
  }

  const whereClause: any = {
    subjectId: input.subjectId,
    status: "APPROVED",
  };

  if (input.topic && input.topic.trim()) {
    Object.assign(whereClause, topicWhere(input.topic.trim()));
  }
  if (input.bancas && input.bancas.length > 0) {
    whereClause.banca = { in: input.bancas };
  }

  const questions = await db.question.findMany({
    where: whereClause,
    select: { id: true, segmentId: true },
  });

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
  if (!(await canUserAccessCoreFeatures(user.role))) {
    return { error: "A montagem de cadernos está em fase final de validação e será liberada em breve." };
  }

  if (!input.items || input.items.length === 0) {
    return { error: "Selecione ao menos uma disciplina para montar o caderno." };
  }

  const selectedQuestionIds = new Set<string>();

  if (input.mode === "TOTAL") {
    // Modo Quantidade Total: seleciona aleatoriamente entre o universo dos filtros escolhidos
    const requestedTotal = input.totalCount && input.totalCount > 0 ? input.totalCount : 20;

    // Montar filtros OR para as matérias e seus respectivos tópicos
    const orConditions: any[] = [];
    for (const item of input.items) {
      if (item.topics && item.topics.length > 0) {
        orConditions.push({
          subjectId: item.subjectId,
          OR: topicsWhere(item.topics),
          status: "APPROVED",
        });
      } else {
        orConditions.push({
          subjectId: item.subjectId,
          status: "APPROVED",
        });
      }
    }

    const availableQuestions = await db.question.findMany({
      where: { OR: orConditions },
      select: { id: true, subjectId: true },
    });

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

      const whereClause: any = {
        subjectId: item.subjectId,
        status: "APPROVED",
      };

      if (item.topics && item.topics.length > 0) {
        whereClause.OR = topicsWhere(item.topics);
      }

      const questions = await db.question.findMany({
        where: whereClause,
        select: { id: true },
      });

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
