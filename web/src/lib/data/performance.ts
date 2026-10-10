import "server-only";
import { db } from "@/lib/db";
import {
  projectExam, quizBySubject, secondsByDay, secondsBySubject, secondsByWeek, secondsThisWeek, streakDays, totalSeconds, weakTopics,
  type QuizRow, type SubjectMeta, type TimeRow,
} from "@/lib/metrics";

export interface CommunityComparison {
  minQuestions: number;
  qualifiedUsersCount: number;
  communityAvgAccuracy: number | null;
  top10Accuracy: number | null;
  userPercentile: number | null;
  userAccuracy: number | null;
  userQuestionsTotal: number;

  minStudyHours: number;
  qualifiedStudyUsersCount: number;
  communityAvgHours: number | null;
  userStudyHours: number | null;

  subjectStats: Array<{
    subjectId: string;
    subjectName: string;
    userAccuracy: number | null;
    userTotal: number;
    communityAccuracy: number | null;
    qualifiedCount: number;
  }>;
}

export async function getPerformance(userId: string, planStart: Date | null, totalWeeks: number, planSubjectIds: string[]) {
  const [logs, answers, subjects, sessions, bizu, allCommunityAnswers, allCommunityLogs] = await Promise.all([
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
    // Agregação anônima de respostas finalizadas de todos os usuários
    db.quizAnswer.findMany({
      where: { session: { finishedAt: { not: null } } },
      select: { isCorrect: true, question: { select: { subjectId: true } }, session: { select: { userId: true } } },
    }),
    // Agregação anônima de tempo registrado
    db.timeLog.findMany({
      select: { userId: true, seconds: true },
    }),
  ]);

  const timeRows: TimeRow[] = logs.map((l) => ({ seconds: l.seconds, startedAt: l.startedAt, subjectId: l.activity?.subjectId ?? null }));
  const quizRows: QuizRow[] = answers.map((a) => ({
    subjectId: a.question.subjectId, topic: a.question.topic, chosen: a.chosenLabel, isCorrect: a.isCorrect, seconds: a.secondsSpent, finishedAt: a.session.finishedAt!,
  }));
  const stats = quizBySubject(quizRows);
  const mine: SubjectMeta[] = subjects.filter((s) => planSubjectIds.includes(s.id));
  const totalAnswered = quizRows.filter((r) => r.chosen !== null).length;
  const totalCorrect = quizRows.filter((r) => r.isCorrect).length;
  const myTotalSeconds = totalSeconds(timeRows);
  const myAccuracy = quizRows.length ? totalCorrect / quizRows.length : null;

  // ─── COMPARAÇÃO COM A COMUNIDADE (ANONIMIZADA E COM CRITÉRIOS DE CORTE) ───
  const MIN_QUESTIONS_COMMUNITY = 15; // Mínimo de 15 questões respondidas
  const MIN_QUESTIONS_SUBJECT = 6;    // Mínimo de 6 questões na disciplina
  const MIN_STUDY_HOURS = 2;          // Mínimo de 2 horas de estudo

  // 1. Agrupar questões por usuário e por disciplina
  const userMap = new Map<string, { total: number; correct: number; bySubject: Map<string, { total: number; correct: number }> }>();
  for (const a of allCommunityAnswers) {
    const uid = a.session.userId;
    let u = userMap.get(uid);
    if (!u) {
      u = { total: 0, correct: 0, bySubject: new Map() };
      userMap.set(uid, u);
    }
    u.total++;
    if (a.isCorrect) u.correct++;

    const sid = a.question.subjectId;
    let s = u.bySubject.get(sid);
    if (!s) {
      s = { total: 0, correct: 0 };
      u.bySubject.set(sid, s);
    }
    s.total++;
    if (a.isCorrect) s.correct++;
  }

  // Filtrar usuários qualificados (geral)
  const qualifiedAccuracies: number[] = [];
  for (const u of userMap.values()) {
    if (u.total >= MIN_QUESTIONS_COMMUNITY) {
      qualifiedAccuracies.push(u.correct / u.total);
    }
  }

  let communityAvgAccuracy: number | null = null;
  let top10Accuracy: number | null = null;
  let userPercentile: number | null = null;

  if (qualifiedAccuracies.length > 0) {
    qualifiedAccuracies.sort((a, b) => a - b);
    const sum = qualifiedAccuracies.reduce((a, b) => a + b, 0);
    communityAvgAccuracy = sum / qualifiedAccuracies.length;
    // Top 10% da plataforma (percentil 90 ou melhor)
    const top10Index = Math.floor(qualifiedAccuracies.length * 0.9);
    top10Accuracy = qualifiedAccuracies[Math.min(top10Index, qualifiedAccuracies.length - 1)];

    if (myAccuracy !== null && quizRows.length >= MIN_QUESTIONS_COMMUNITY) {
      const belowCount = qualifiedAccuracies.filter((acc) => acc <= myAccuracy).length;
      userPercentile = Math.round((belowCount / qualifiedAccuracies.length) * 100);
    }
  }

  // 2. Comparativo por Disciplina
  const subjectComparisons: CommunityComparison["subjectStats"] = [];
  for (const s of subjects) {
    const mySub = stats.get(s.id);
    const userSubAcc = mySub && mySub.total > 0 ? mySub.correct / mySub.total : null;
    const userSubTotal = mySub ? mySub.total : 0;

    const subAccuracies: number[] = [];
    for (const u of userMap.values()) {
      const uSub = u.bySubject.get(s.id);
      if (uSub && uSub.total >= MIN_QUESTIONS_SUBJECT) {
        subAccuracies.push(uSub.correct / uSub.total);
      }
    }

    const commSubAcc = subAccuracies.length > 0 ? subAccuracies.reduce((a, b) => a + b, 0) / subAccuracies.length : null;

    if (userSubTotal > 0 || commSubAcc !== null) {
      subjectComparisons.push({
        subjectId: s.id,
        subjectName: s.name,
        userAccuracy: userSubAcc,
        userTotal: userSubTotal,
        communityAccuracy: commSubAcc,
        qualifiedCount: subAccuracies.length,
      });
    }
  }

  // 3. Tempo de estudo acumulado
  const timeByUser = new Map<string, number>();
  for (const l of allCommunityLogs) {
    timeByUser.set(l.userId, (timeByUser.get(l.userId) ?? 0) + l.seconds);
  }

  const qualifiedHours: number[] = [];
  for (const sec of timeByUser.values()) {
    const hrs = sec / 3600;
    if (hrs >= MIN_STUDY_HOURS) {
      qualifiedHours.push(hrs);
    }
  }

  const communityAvgHours = qualifiedHours.length > 0 ? qualifiedHours.reduce((a, b) => a + b, 0) / qualifiedHours.length : null;
  const userStudyHours = myTotalSeconds / 3600;

  const community: CommunityComparison = {
    minQuestions: MIN_QUESTIONS_COMMUNITY,
    qualifiedUsersCount: qualifiedAccuracies.length,
    communityAvgAccuracy,
    top10Accuracy,
    userPercentile,
    userAccuracy: myAccuracy,
    userQuestionsTotal: quizRows.length,
    minStudyHours: MIN_STUDY_HOURS,
    qualifiedStudyUsersCount: qualifiedHours.length,
    communityAvgHours,
    userStudyHours,
    subjectStats: subjectComparisons,
  };

  return {
    totalSeconds: myTotalSeconds,
    bySubjectSeconds: secondsBySubject(timeRows),
    thisWeekSeconds: secondsThisWeek(timeRows, new Date()),
    byWeekSeconds: planStart ? secondsByWeek(timeRows, planStart, totalWeeks) : [],
    streak: streakDays(timeRows, new Date()),
    daily: secondsByDay(timeRows, new Date(), 7 * 15),
    quizStats: stats,
    questionsAnswered: totalAnswered,
    questionsTotal: quizRows.length,
    accuracy: myAccuracy,
    weak: weakTopics(quizRows),
    projection: projectExam(mine, stats),
    recentSessions: sessions.slice(0, 8),
    trend: [...sessions].reverse().filter((x) => x.total > 0).map((x) => ({ id: x.id, ratio: (x.score ?? 0) / x.total, at: x.finishedAt!, subjectId: x.activity?.subjectId ?? null })),
    avgSecondsPerQuestion: quizRows.length ? Math.round(quizRows.reduce((n, r) => n + r.seconds, 0) / quizRows.length) : null,
    questionsCorrect: totalCorrect,
    subjects,
    bizuAnswered: bizu.reduce((n, b) => n + b._count, 0),
    bizuCorrect: bizu.find((b) => b.isCorrect)?._count ?? 0,
    community,
  };
}
