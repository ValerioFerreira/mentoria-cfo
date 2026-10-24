import "server-only";
import { db } from "@/lib/db";
import { subjectName } from "@/lib/ui-format";
import { hideInedita } from "@/lib/quiz/banca";
import { makeTopicResolver, type TopicItem } from "@/lib/quiz/topic-map";
import { EXAM_CONFIGS, usesOwnExamBlocks, type SupportedSimuladoContest } from "@/lib/simulado-rules";
import type { Contest } from "@/generated/prisma/client";

// "Assunto" = item do edital (Question.editalItemId). Questões sem item ficam em OTHER_TOPIC_ID.
export const OTHER_TOPIC_ID = "outros";

export interface TopicOverview {
  id: string; // editalItemId ou OTHER_TOPIC_ID (é o que vai para os filtros do treino/caderno)
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
  /** nomes dos blocos da prova do concurso (no PCPE: P1 e P2); ausente = "Bloco I/II/III" */
  blockNames?: Partial<Record<"I" | "II" | "III", string>>;
  availableBancas: string[];
  bancaCounts: Record<string, number>;
}

/** `subjectIds`: disciplinas do edital do aluno; as demais não aparecem nem entram nas contagens. */
export async function getQuestoesOverview(userId: string, subjectIds: string[], contest?: Contest | null): Promise<QuestoesOverview> {
  // 1. Buscar as questões aprovadas do edital com seu assunto, disciplina e banca
  const [questions, userAnswers, dbSubjects] = await Promise.all([
    db.question.findMany({
      where: { status: "APPROVED", subjectId: { in: subjectIds }, ...hideInedita(contest) },
      select: {
        id: true,
        subjectId: true,
        aulaId: true,
        editalItemId: true,
        banca: true,
      },
    }),
    db.quizAnswer.findMany({
      where: {
        session: { userId },
        chosenLabel: { not: null },
        question: { subjectId: { in: subjectIds } },
      },
      select: {
        questionId: true,
        isCorrect: true,
      },
    }),
    db.subject.findMany({
      where: { id: { in: subjectIds } },
      orderBy: { sortOrder: "asc" },
      select: { id: true, name: true, block: true },
    }),
  ]);
  const editalItems = await db.editalItem.findMany({ select: { id: true, subjectId: true, code: true, title: true, sortOrder: true, aulaIds: true, onlyContests: true, excludeContests: true } });
  const itemInfo = new Map(editalItems.map((e) => [e.id, e]));
  // cada questão cai no assunto do edital do concurso do aluno (no PCPE, os assuntos próprios dele)
  const resolveTopic = makeTopicResolver(editalItems.map((e): TopicItem => ({ ...e, aulaIds: (e.aulaIds as string[]) ?? [] })), contest);

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
    const topicName = resolveTopic(q);
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
  const exam = usesOwnExamBlocks(contest) ? EXAM_CONFIGS[contest as SupportedSimuladoContest] : undefined;
  const examBlock = new Map((exam?.subjects ?? []).map((x) => [x.subjectId, x.block]));
  const subjectBlockMap = new Map(dbSubjects.map((s) => [s.id, (examBlock.get(s.id) ?? s.block) as "I" | "II" | "III"]));
  const subjectsList: SubjectOverview[] = [];

  for (const s of dbSubjects) {
    const sData = subjectMap.get(s.id);

    const topics: TopicOverview[] = [];
    if (sData) {
      for (const [tId, tData] of sData.topics.entries()) {
        const tAnswered = tData.answeredQ.size;
        const tCorrect = tData.correctQ.size;
        const info = itemInfo.get(tId);
        topics.push({
          id: tId,
          name: info ? `${info.code}. ${info.title}` : "Outros assuntos",
          totalQuestions: tData.total,
          userAnswered: tAnswered,
          userCorrect: tCorrect,
          userAccuracy: tAnswered > 0 ? Math.round((tCorrect / tAnswered) * 100) : null,
          bancas: Array.from(tData.bancas),
          bancaCounts: tData.bancaCounts,
        });
      }
      // ordem do edital; "Outros assuntos" por último
      const order = (t: TopicOverview) => itemInfo.get(t.id)?.sortOrder ?? Number.MAX_SAFE_INTEGER;
      topics.sort((a, b) => order(a) - order(b));
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
      subjectsCount: subjectsList.filter((s) => s.totalQuestions > 0).length,
    },
    subjects: subjectsList,
    blockNames: exam ? { I: exam.blocks.I.name, II: exam.blocks.II.name } : undefined,
    availableBancas: availableBancas.length > 0 ? availableBancas : ["AOCP"],
    bancaCounts,
  };
}
