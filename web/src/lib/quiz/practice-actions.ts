"use server";

import { redirect } from "next/navigation";
import { requireUser } from "@/lib/auth/dal";
import { db } from "@/lib/db";
import { hashSeed } from "./logic";

export async function startSubjectPracticeQuiz(input: {
  subjectId: string;
  topic?: string;
  limit?: number;
}): Promise<{ error: string } | never> {
  const user = await requireUser();

  const whereClause: any = {
    subjectId: input.subjectId,
    status: "APPROVED",
  };

  if (input.topic && input.topic.trim()) {
    whereClause.topic = input.topic.trim();
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

  // Embaralhar com semente aleatória
  const shuffle = <T>(arr: T[]): T[] => {
    const copy = [...arr];
    for (let i = copy.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [copy[i], copy[j]] = [copy[j], copy[i]];
    }
    return copy;
  };

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
      limitSeconds: 7200, // 2 horas de tolerância para praticar sem pressa
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
