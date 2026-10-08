import "server-only";
import { db } from "@/lib/db";
import {
  projectExam, quizBySubject, secondsByDay, secondsBySubject, secondsByWeek, streakDays, totalSeconds, weakTopics,
  type QuizRow, type SubjectMeta, type TimeRow,
} from "@/lib/metrics";

export async function getPerformance(userId: string, planStart: Date | null, totalWeeks: number, planSubjectIds: string[]) {
  const [logs, answers, subjects, sessions, bizu] = await Promise.all([
    db.timeLog.findMany({ where: { userId }, select: { seconds: true, startedAt: true, activity: { select: { subjectId: true } } } }),
    db.quizAnswer.findMany({
      where: { session: { userId, finishedAt: { not: null } } },
      select: { chosenLabel: true, isCorrect: true, secondsSpent: true, question: { select: { subjectId: true, topic: true } }, session: { select: { finishedAt: true } } },
    }),
    db.subject.findMany({ orderBy: { sortOrder: "asc" }, select: { id: true, name: true, block: true, examQuestions: true } }),
    db.quizSession.findMany({
      where: { userId, finishedAt: { not: null } },
      orderBy: { finishedAt: "desc" },
      take: 24,
      select: { id: true, activityId: true, finishedAt: true, score: true, total: true, activity: { select: { subjectId: true, aula: { select: { number: true, shortTitle: true } } } } },
    }),
    db.bizuAnswer.groupBy({ by: ["isCorrect"], where: { userId }, _count: true }),
  ]);

  const timeRows: TimeRow[] = logs.map((l) => ({ seconds: l.seconds, startedAt: l.startedAt, subjectId: l.activity?.subjectId ?? null }));
  const quizRows: QuizRow[] = answers.map((a) => ({
    subjectId: a.question.subjectId, topic: a.question.topic, chosen: a.chosenLabel, isCorrect: a.isCorrect, seconds: a.secondsSpent, finishedAt: a.session.finishedAt!,
  }));
  const stats = quizBySubject(quizRows);
  const mine: SubjectMeta[] = subjects.filter((s) => planSubjectIds.includes(s.id));
  const totalAnswered = quizRows.filter((r) => r.chosen !== null).length;
  const totalCorrect = quizRows.filter((r) => r.isCorrect).length;

  return {
    totalSeconds: totalSeconds(timeRows),
    bySubjectSeconds: secondsBySubject(timeRows),
    byWeekSeconds: planStart ? secondsByWeek(timeRows, planStart, totalWeeks) : [],
    streak: streakDays(timeRows, new Date()),
    daily: secondsByDay(timeRows, new Date(), 7 * 15),
    quizStats: stats,
    questionsAnswered: totalAnswered,
    questionsTotal: quizRows.length,
    accuracy: quizRows.length ? totalCorrect / quizRows.length : null,
    weak: weakTopics(quizRows),
    projection: projectExam(mine, stats),
    recentSessions: sessions.slice(0, 8),
    /** acerto de cada caderno finalizado, do mais antigo ao mais recente (evolução) */
    trend: [...sessions].reverse().filter((x) => x.total > 0).map((x) => ({ id: x.id, ratio: (x.score ?? 0) / x.total, at: x.finishedAt!, subjectId: x.activity?.subjectId ?? null })),
    avgSecondsPerQuestion: quizRows.length ? Math.round(quizRows.reduce((n, r) => n + r.seconds, 0) / quizRows.length) : null,
    questionsCorrect: totalCorrect,
    subjects,
    bizuAnswered: bizu.reduce((n, b) => n + b._count, 0),
    bizuCorrect: bizu.find((b) => b.isCorrect)?._count ?? 0,
  };
}
