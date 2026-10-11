import "server-only";
import { db } from "@/lib/db";
import { subjectName } from "@/lib/ui-format";

export interface TopicOverview {
  name: string;
  totalQuestions: number;
  userAnswered: number;
  userCorrect: number;
  userAccuracy: number | null;
}

export interface SubjectOverview {
  id: string;
  name: string;
  block: "I" | "II" | "III";
  totalQuestions: number;
  userAnswered: number;
  userCorrect: number;
  userAccuracy: number | null;
  topics: TopicOverview[];
}

export interface QuestoesOverview {
  globalStats: {
    totalQuestions: number;
    userAnswered: number;
    userCorrect: number;
    userAccuracy: number | null;
    subjectsCount: number;
  };
  subjects: SubjectOverview[];
}

export async function getQuestoesOverview(userId: string): Promise<QuestoesOverview> {
  // 1. Buscar todas as questões aprovadas com seu assunto e disciplina
  const [questions, userAnswers, dbSubjects] = await Promise.all([
    db.question.findMany({
      where: { status: "APPROVED" },
      select: {
        id: true,
        subjectId: true,
        topic: true,
      },
    }),
    db.quizAnswer.findMany({
      where: {
        session: { userId },
        chosenLabel: { not: null },
      },
      select: {
        questionId: true,
        isCorrect: true,
      },
    }),
    db.subject.findMany({
      orderBy: { sortOrder: "asc" },
      select: { id: true, name: true, block: true },
    }),
  ]);

  // Mapa das respostas do usuário
  // Como o usuário pode responder mais de uma vez ao longo do tempo,
  // guardamos o total de respostas e se a última/predominante foi correta
  const answerMap = new Map<string, { answered: number; correct: number; lastCorrect: boolean | null }>();
  for (const a of userAnswers) {
    const cur = answerMap.get(a.questionId) ?? { answered: 0, correct: 0, lastCorrect: null };
    cur.answered++;
    if (a.isCorrect) cur.correct++;
    cur.lastCorrect = a.isCorrect;
    answerMap.set(a.questionId, cur);
  }

  // Agrupar questões por disciplina e por assunto
  const subjectMap = new Map<string, {
    total: number;
    topics: Map<string, { total: number; answeredQ: Set<string>; correctQ: Set<string> }>;
    answeredQ: Set<string>;
    correctQ: Set<string>;
  }>();

  for (const q of questions) {
    const sId = q.subjectId;
    const topicName = q.topic?.trim() || "Geral";

    let sData = subjectMap.get(sId);
    if (!sData) {
      sData = { total: 0, topics: new Map(), answeredQ: new Set(), correctQ: new Set() };
      subjectMap.set(sId, sData);
    }
    sData.total++;

    let tData = sData.topics.get(topicName);
    if (!tData) {
      tData = { total: 0, answeredQ: new Set(), correctQ: new Set() };
      sData.topics.set(topicName, tData);
    }
    tData.total++;

    const ans = answerMap.get(q.id);
    if (ans && ans.answered > 0) {
      sData.answeredQ.add(q.id);
      tData.answeredQ.add(q.id);
      if (ans.lastCorrect) {
        sData.correctQ.add(q.id);
        tData.correctQ.add(q.id);
      }
    }
  }

  // Construir o retorno estruturado
  const subjectBlockMap = new Map(dbSubjects.map((s) => [s.id, s.block as "I" | "II" | "III"]));
  const subjectsList: SubjectOverview[] = [];

  for (const s of dbSubjects) {
    const sData = subjectMap.get(s.id);
    if (!sData || sData.total === 0) continue;

    const topics: TopicOverview[] = [];
    for (const [tName, tData] of sData.topics.entries()) {
      const tAnswered = tData.answeredQ.size;
      const tCorrect = tData.correctQ.size;
      topics.push({
        name: tName,
        totalQuestions: tData.total,
        userAnswered: tAnswered,
        userCorrect: tCorrect,
        userAccuracy: tAnswered > 0 ? Math.round((tCorrect / tAnswered) * 100) : null,
      });
    }

    // Ordenar tópicos por quantidade de questões decrescente
    topics.sort((a, b) => b.totalQuestions - a.totalQuestions);

    const sAnswered = sData.answeredQ.size;
    const sCorrect = sData.correctQ.size;

    subjectsList.push({
      id: s.id,
      name: subjectName(s.id),
      block: subjectBlockMap.get(s.id) ?? "I",
      totalQuestions: sData.total,
      userAnswered: sAnswered,
      userCorrect: sCorrect,
      userAccuracy: sAnswered > 0 ? Math.round((sCorrect / sAnswered) * 100) : null,
      topics,
    });
  }

  // Estatísticas globais
  const totalQuestions = questions.length;
  const uniqueAnswered = new Set(userAnswers.map((a) => a.questionId)).size;
  const uniqueCorrect = new Set(userAnswers.filter((a) => a.isCorrect).map((a) => a.questionId)).size;
  const globalAccuracy = uniqueAnswered > 0 ? Math.round((uniqueCorrect / uniqueAnswered) * 100) : null;

  return {
    globalStats: {
      totalQuestions,
      userAnswered: uniqueAnswered,
      userCorrect: uniqueCorrect,
      userAccuracy: globalAccuracy,
      subjectsCount: subjectsList.length,
    },
    subjects: subjectsList,
  };
}
