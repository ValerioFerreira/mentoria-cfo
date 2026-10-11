import "server-only";
import { db } from "@/lib/db";
import { subjectName } from "@/lib/ui-format";

export interface TopicOverview {
  name: string;
  totalQuestions: number;
  userAnswered: number;
  userCorrect: number;
  userAccuracy: number | null;
  bancas: string[];
  bancaCounts: Record<string, number>;
}

export interface SubjectOverview {
  id: string;
  name: string;
  block: "I" | "II" | "III";
  totalQuestions: number;
  userAnswered: number;
  userCorrect: number;
  userAccuracy: number | null;
  bancas: string[];
  bancaCounts: Record<string, number>;
  topics: TopicOverview[];
}

export interface BancaCount {
  name: string;
  count: number;
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
  availableBancas: string[];
  bancaCounts: Record<string, number>;
}

export async function getQuestoesOverview(userId: string): Promise<QuestoesOverview> {
  // 1. Buscar todas as questões aprovadas com seu assunto, disciplina e banca
  const [questions, userAnswers, dbSubjects] = await Promise.all([
    db.question.findMany({
      where: { status: "APPROVED" },
      select: {
        id: true,
        subjectId: true,
        topic: true,
        banca: true,
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

  const bancaCounts: Record<string, number> = {};
  for (const q of questions) {
    const b = q.banca || "AOCP";
    bancaCounts[b] = (bancaCounts[b] || 0) + 1;
  }
  // Ordenar bancas por volume de questões decrescente, mantendo AOCP no topo
  const availableBancas = Object.keys(bancaCounts).sort((a, b) => {
    if (a === "AOCP") return -1;
    if (b === "AOCP") return 1;
    return bancaCounts[b] - bancaCounts[a];
  });

  // Mapa das respostas do usuário
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
    bancas: Set<string>;
    bancaCounts: Record<string, number>;
    topics: Map<string, { total: number; bancas: Set<string>; bancaCounts: Record<string, number>; answeredQ: Set<string>; correctQ: Set<string> }>;
    answeredQ: Set<string>;
    correctQ: Set<string>;
  }>();

  for (const q of questions) {
    const sId = q.subjectId;
    const topicName = q.topic?.trim() || "Geral";
    const qBanca = q.banca || "AOCP";

    let sData = subjectMap.get(sId);
    if (!sData) {
      sData = { total: 0, bancas: new Set(), bancaCounts: {}, topics: new Map(), answeredQ: new Set(), correctQ: new Set() };
      subjectMap.set(sId, sData);
    }
    sData.total++;
    sData.bancas.add(qBanca);
    sData.bancaCounts[qBanca] = (sData.bancaCounts[qBanca] || 0) + 1;

    let tData = sData.topics.get(topicName);
    if (!tData) {
      tData = { total: 0, bancas: new Set(), bancaCounts: {}, answeredQ: new Set(), correctQ: new Set() };
      sData.topics.set(topicName, tData);
    }
    tData.total++;
    tData.bancas.add(qBanca);
    tData.bancaCounts[qBanca] = (tData.bancaCounts[qBanca] || 0) + 1;

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

    const topics: TopicOverview[] = [];
    if (sData) {
      for (const [tName, tData] of sData.topics.entries()) {
        const tAnswered = tData.answeredQ.size;
        const tCorrect = tData.correctQ.size;
        topics.push({
          name: tName,
          totalQuestions: tData.total,
          userAnswered: tAnswered,
          userCorrect: tCorrect,
          userAccuracy: tAnswered > 0 ? Math.round((tCorrect / tAnswered) * 100) : null,
          bancas: Array.from(tData.bancas),
          bancaCounts: tData.bancaCounts,
        });
      }
      topics.sort((a, b) => b.totalQuestions - a.totalQuestions);
    }

    const sAnswered = sData ? sData.answeredQ.size : 0;
    const sCorrect = sData ? sData.correctQ.size : 0;

    subjectsList.push({
      id: s.id,
      name: subjectName(s.id),
      block: subjectBlockMap.get(s.id) ?? "I",
      totalQuestions: sData ? sData.total : 0,
      userAnswered: sAnswered,
      userCorrect: sCorrect,
      userAccuracy: sAnswered > 0 ? Math.round((sCorrect / sAnswered) * 100) : null,
      bancas: sData ? Array.from(sData.bancas) : [],
      bancaCounts: sData ? sData.bancaCounts : {},
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
    availableBancas: availableBancas.length > 0 ? availableBancas : ["AOCP"],
    bancaCounts,
  };
}
