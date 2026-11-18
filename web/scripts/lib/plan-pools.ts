// Pool candidato dos cadernos de Questões dos planos (SÓ LEITURA), calculado em memória com as mesmas regras do app.
//
// Espelha `loadQuizPool` (src/lib/quiz/pool.ts) e os filtros de src/lib/quiz/banca.ts, mas sem uma consulta por
// atividade: o acervo é lido uma vez (`loadBank`) e cada pool é montado em memória. Usado por
// scripts/questoes-fila-comentarios.ts (prioridade dos comentários). Ao mudar as regras do caderno no app, mude aqui.
import type { Contest, PrismaClient, QuestionKind, QuestionStatus } from "../../src/generated/prisma/client";
import { AOCP_BANCAS, contestBancas, usesReinforcement } from "../../src/lib/quiz/banca";

/** Mesmo valor de DEFAULT_QUIZ_QUESTIONS (src/lib/quiz/pool.ts, que não pode ser importado aqui por abrir o banco do app). */
export const DEFAULT_QUIZ_QUESTIONS = 25;

export interface BankQuestion {
  id: string;
  segmentId: string;
  banca: string;
  kind: QuestionKind;
  status: QuestionStatus;
  /** já tem comentário geral no banco */
  commented: boolean;
}

/** Cliente ou transação do Prisma (os scripts leem dentro de uma transação READ ONLY). */
type Reader = Pick<PrismaClient, "question" | "plan" | "activity" | "quizSession">;

/** Acervo por trecho, só com os status pedidos (produção serve só APPROVED). */
export async function loadBank(db: Reader, statuses: QuestionStatus[] = ["APPROVED"]): Promise<Map<string, BankQuestion[]>> {
  const rows = await db.question.findMany({
    where: { status: { in: statuses } },
    select: { id: true, segmentId: true, banca: true, kind: true, status: true, explanation: true },
  });
  const bySeg = new Map<string, BankQuestion[]>();
  for (const r of rows) {
    const q: BankQuestion = { id: r.id, segmentId: r.segmentId, banca: r.banca, kind: r.kind, status: r.status, commented: r.explanation.trim().length > 0 };
    const list = bySeg.get(r.segmentId);
    if (list) list.push(q);
    else bySeg.set(r.segmentId, [q]);
  }
  return bySeg;
}

/** `activityQuizWhere` em memória: banca do concurso; o CFOA só usa múltipla escolha. */
export function inActivityPool(q: BankQuestion, contest: Contest | null): boolean {
  return contestBancas(contest).includes(q.banca) && (contest !== "CBMPE_CFOA" || q.kind === "MULTIPLA_ESCOLHA");
}

/** `reinforcementQuizWhere` em memória: múltipla escolha de outras bancas (inéditas incluídas). */
export function inReinforcementPool(q: BankQuestion): boolean {
  return q.kind === "MULTIPLA_ESCOLHA" && !AOCP_BANCAS.includes(q.banca);
}

export interface PlanActivity {
  id: string;
  type: string;
  status: string;
  subjectId: string;
  aulaId: string;
  dayIndex: number | null;
  sortOrder: number;
  quizQuestions: number | null;
  weekIndex: number;
  segmentIds: string[];
}

export interface ActivityPool {
  primary: string[];
  extra: string[];
  reinforcement: string[];
}

/** Trechos da mesma disciplina cujas Teorias vêm antes da atividade (semana e dia), fora os do próprio caderno. */
export function priorSegmentIds(a: PlanActivity, teorias: PlanActivity[]): string[] {
  if (a.dayIndex === null) return [];
  const own = new Set(a.segmentIds);
  const out = new Set<string>();
  for (const t of teorias) {
    if (t.subjectId !== a.subjectId) continue;
    const before = t.weekIndex < a.weekIndex || (t.weekIndex === a.weekIndex && t.dayIndex !== null && t.dayIndex < a.dayIndex);
    if (!before) continue;
    for (const s of t.segmentIds) if (!own.has(s)) out.add(s);
  }
  return [...out];
}

/** Pool do caderno de uma atividade de Questões, com as três camadas de `loadQuizPool`. */
export function activityPool(a: PlanActivity, teorias: PlanActivity[], bank: Map<string, BankQuestion[]>, contest: Contest | null): ActivityPool {
  const pick = (segs: string[], ok: (q: BankQuestion) => boolean) => segs.flatMap((s) => (bank.get(s) ?? []).filter(ok).map((q) => q.id));
  const own = [...new Set(a.segmentIds)];
  const primary = pick(own, (q) => inActivityPool(q, contest));
  const want = a.quizQuestions ?? DEFAULT_QUIZ_QUESTIONS;
  if (primary.length >= want) return { primary, extra: [], reinforcement: [] };
  const prior = priorSegmentIds(a, teorias);
  const extra = pick(prior, (q) => inActivityPool(q, contest));
  if (primary.length + extra.length >= want || !usesReinforcement(contest)) return { primary, extra, reinforcement: [] };
  return { primary, extra, reinforcement: pick([...own, ...prior], inReinforcementPool) };
}

export interface PlanSnapshot {
  id: string;
  userId: string;
  status: string;
  contest: Contest | null;
  startIso: string;
  activities: PlanActivity[];
  /** questões já sorteadas por atividade (todas as sessões, abertas ou encerradas) */
  drawn: Map<string, string[]>;
}

/** Planos ACTIVE e PENDING_ANALYSIS com as atividades de Teoria e Questões e as questões já sorteadas. */
export async function loadPlans(db: Reader, statuses: ("ACTIVE" | "PENDING_ANALYSIS")[] = ["ACTIVE", "PENDING_ANALYSIS"]): Promise<PlanSnapshot[]> {
  const plans = await db.plan.findMany({
    where: { status: { in: statuses } },
    select: { id: true, userId: true, status: true, contest: true, startDate: true },
    orderBy: { createdAt: "asc" },
  });
  const out: PlanSnapshot[] = [];
  for (const p of plans) {
    const acts = await db.activity.findMany({
      where: { planId: p.id, type: { in: ["QUESTOES", "TEORIA"] } },
      select: {
        id: true, type: true, status: true, subjectId: true, aulaId: true, dayIndex: true, sortOrder: true, quizQuestions: true,
        week: { select: { index: true } }, segments: { select: { segmentId: true } },
      },
    });
    const activities: PlanActivity[] = acts.map((a) => ({
      id: a.id, type: a.type, status: a.status, subjectId: a.subjectId, aulaId: a.aulaId, dayIndex: a.dayIndex, sortOrder: a.sortOrder,
      quizQuestions: a.quizQuestions, weekIndex: a.week.index, segmentIds: a.segments.map((s) => s.segmentId),
    }));
    const quizIds = activities.filter((a) => a.type === "QUESTOES").map((a) => a.id);
    const sessions = quizIds.length
      ? await db.quizSession.findMany({ where: { activityId: { in: quizIds } }, select: { activityId: true, answers: { select: { questionId: true } } } })
      : [];
    const drawn = new Map<string, string[]>();
    for (const s of sessions) {
      if (!s.activityId) continue;
      drawn.set(s.activityId, [...(drawn.get(s.activityId) ?? []), ...s.answers.map((x) => x.questionId)]);
    }
    out.push({ id: p.id, userId: p.userId, status: p.status, contest: p.contest, startIso: p.startDate.toISOString().slice(0, 10), activities, drawn });
  }
  return out;
}
