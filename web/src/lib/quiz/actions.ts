"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { requireUser } from "@/lib/auth/dal";
import { db } from "@/lib/db";
import { hashSeed, pickQuestions, score, type AnswerRow } from "./logic";
import { servableStatuses } from "./servable";

const MIN_QUESTIONS = 5;

async function ownedQuizActivity(userId: string, activityId: string) {
  const a = await db.activity.findFirst({
    where: { id: activityId, type: "QUESTOES", week: { plan: { userId } } },
    include: { segments: { select: { segmentId: true } } },
  });
  if (!a) throw new Error("Atividade de questões não encontrada.");
  return a;
}

/** Cria (ou retoma) o caderno da atividade e redireciona para ele. */
export async function startQuiz(activityId: string): Promise<{ error: string } | never> {
  const user = await requireUser();
  const a = await ownedQuizActivity(user.id, activityId);

  const open = await db.quizSession.findFirst({ where: { userId: user.id, activityId, finishedAt: null }, orderBy: { startedAt: "desc" } });
  if (open) redirect(`/caderno/${activityId}`);

  const segmentIds = a.segments.map((s) => s.segmentId);
  const questions = await db.question.findMany({
    where: { segmentId: { in: segmentIds }, status: { in: servableStatuses() } },
    select: { id: true, segmentId: true },
  });
  const want = a.quizQuestions ?? 25;
  const n = Math.min(want, questions.length);
  if (n < MIN_QUESTIONS) return { error: "Ainda não há questões suficientes para este caderno." };

  const history = await db.quizAnswer.findMany({
    where: { session: { userId: user.id }, questionId: { in: questions.map((q) => q.id) }, chosenLabel: { not: null } },
    orderBy: { answeredAt: "asc" },
    select: { questionId: true, isCorrect: true },
  });
  const seen = new Map<string, { n: number; last: boolean | null }>();
  for (const h of history) {
    const cur = seen.get(h.questionId) ?? { n: 0, last: null };
    seen.set(h.questionId, { n: cur.n + 1, last: h.isCorrect });
  }

  const sessionId = crypto.randomUUID();
  const ids = pickQuestions(
    questions.map((q) => ({ id: q.id, segmentId: q.segmentId, seen: seen.get(q.id)?.n ?? 0, lastCorrect: seen.get(q.id)?.last ?? null })),
    n,
    hashSeed(sessionId),
  );
  await db.quizSession.create({
    data: {
      id: sessionId, userId: user.id, activityId, kind: a.quizMixed ? "SIMULADO_BLOCO" : "CADERNO",
      limitSeconds: a.quizLimitSec ?? 3600, total: ids.length,
      answers: { create: ids.map((questionId, i) => ({ questionId, position: i + 1 })) },
    },
  });
  await db.activity.updateMany({ where: { id: activityId, status: "PENDING" }, data: { status: "IN_PROGRESS" } });
  redirect(`/caderno/${activityId}`);
}

export async function saveAnswer(input: { sessionId: string; position: number; label: string | null; flagged: boolean; secondsDelta: number }) {
  const user = await requireUser();
  const s = await db.quizSession.findFirst({ where: { id: input.sessionId, userId: user.id, finishedAt: null }, select: { id: true, startedAt: true, limitSeconds: true } });
  if (!s) return { error: "Caderno encerrado." } as const;
  // respostas após o tempo limite (com tolerância de 10 s) não são aceitas
  if (Date.now() > s.startedAt.getTime() + (s.limitSeconds + 10) * 1000) return { error: "Tempo esgotado." } as const;
  const row = await db.quizAnswer.findUnique({ where: { sessionId_position: { sessionId: s.id, position: input.position } }, include: { question: { include: { options: true } } } });
  if (!row) return { error: "Questão inválida." } as const;
  const label = input.label && "ABCDE".includes(input.label) ? input.label : null;
  const correctOption = row.question.options.find((o) => o.isCorrect);
  const correct = label && correctOption ? correctOption.label === label : null;
  await db.quizAnswer.update({
    where: { id: row.id },
    data: {
      chosenLabel: label, isCorrect: correct, flagged: input.flagged,
      secondsSpent: row.secondsSpent + Math.max(0, Math.min(Math.round(input.secondsDelta), 3600)),
      answeredAt: label ? new Date() : null,
    },
  });
  return {
    ok: true,
    isCorrect: correct ?? false,
    correctLabel: correctOption?.label ?? "",
    explanation: row.question.explanation,
  } as const;
}

export async function finishQuiz(sessionId: string, auto: boolean) {
  const user = await requireUser();
  const s = await db.quizSession.findFirst({
    where: { id: sessionId, userId: user.id },
    include: { answers: { include: { question: { include: { options: true } } } } },
  });
  if (!s) throw new Error("Caderno não encontrado.");
  if (s.finishedAt) return { activityId: s.activityId };

  const rows: AnswerRow[] = s.answers.map((a) => ({
    questionId: a.questionId, topic: a.question.topic, segmentId: a.question.segmentId, pageRef: a.question.pageRef,
    chosen: a.chosenLabel, correctLabel: a.question.options.find((o) => o.isCorrect)?.label ?? "", seconds: a.secondsSpent,
  }));
  const sc = score(rows);
  const now = new Date();
  const elapsed = Math.min(s.limitSeconds, Math.max(1, Math.round((now.getTime() - s.startedAt.getTime()) / 1000)));
  await db.$transaction([
    db.quizSession.update({ where: { id: s.id }, data: { finishedAt: now, autoSubmitted: auto, score: sc.correct } }),
    db.timeLog.create({
      data: { userId: user.id, activityId: s.activityId, seconds: elapsed, startedAt: s.startedAt, endedAt: now, source: "TIMER", note: "Caderno de questões" },
    }),
    ...(s.activityId ? [db.activity.update({ where: { id: s.activityId }, data: { status: "DONE", completedAt: now } })] : []),
  ]);
  revalidatePath("/", "layout");
  return { activityId: s.activityId };
}
