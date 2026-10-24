// Revisões fora do ciclo das aulas: (1) revisão geral + cadernos mistos nos dias que sobram depois de todo o conteúdo e
// (2) a revisão única da véspera da prova (D-1).
import { QUIZ, EVE_REVIEW_MINUTES, MAX_SAME_SUBJECT_MINUTES_PER_DAY } from "./constants";
import { dayTarget } from "./days";
import type { PlannedActivity } from "./types";

export interface ReviewSubject {
  subjectId: string;
  examQuestions: number;
  sortOrder: number;
  /** Segmentos cobertos pelo plano (ou já dominados), do mais ao menos relevante. */
  segments: { id: string; aulaId: string }[];
}

const REV_SEGMENTS = 4;
const QUIZ_SEGMENTS = 8;
/** Trechos da revisão da véspera: os mais relevantes da disciplina de maior peso. */
const EVE_SEGMENTS = 8;
const ACTIVITY_MINUTES = 60;

/**
 * Preenche com revisão geral e cadernos mistos os dias `fromOrd`..`toOrd` (os que sobraram depois do conteúdo). As disciplinas
 * se revezam pelo peso na prova; cada uma aparece no máximo uma vez por dia (duas só se houver mais vagas que disciplinas).
 */
export function buildSpareReview(args: {
  fromOrd: number;
  toOrd: number;
  weeklyMinutes: number;
  subjects: ReviewSubject[];
}): Map<number, PlannedActivity[]> {
  const subjects = args.subjects.filter((s) => s.segments.length > 0);
  const days = new Map<number, PlannedActivity[]>();
  if (subjects.length === 0) return days;
  const ptr = new Map(subjects.map((s) => [s.subjectId, 0]));
  const counter = new Map(subjects.map((s) => [s.subjectId, 0]));
  const vt = new Map(subjects.map((s) => [s.subjectId, 0]));

  const take = (s: ReviewSubject, n: number) => {
    const start = ptr.get(s.subjectId)!;
    const picked = Array.from({ length: Math.min(n, s.segments.length) }, (_, i) => s.segments[(start + i) % s.segments.length]);
    ptr.set(s.subjectId, (start + n) % s.segments.length);
    return picked;
  };

  const weekCap = args.weeklyMinutes * 1.05;
  const weekUsed = new Map<number, number>();

  for (let ord = args.fromOrd; ord <= args.toOrd; ord++) {
    const week = Math.floor(ord / 7);
    const dayOfWeek = ord % 7;
    const lastDayOfWeek = Math.min(6, args.toOrd - week * 7);
    const daysRemaining = Math.max(0, lastDayOfWeek - dayOfWeek);
    const usedInWeek = weekUsed.get(week) ?? 0;
    const isEveWeek = Math.floor((args.toOrd + 1) / 7) === week;
    const reservedForRemaining = daysRemaining * ACTIVITY_MINUTES + (isEveWeek ? EVE_REVIEW_MINUTES : 0);
    const rawSlots = Math.max(1, Math.round(dayTarget(args.weeklyMinutes, ord) / ACTIVITY_MINUTES));
    const maxSlotsForCap = Math.max(1, Math.floor((weekCap - usedInWeek - reservedForRemaining) / ACTIVITY_MINUTES));
    const slots = Math.min(rawSlots, maxSlotsForCap);
    const used = new Map<string, number>();
    const acts: PlannedActivity[] = [];
    for (let k = 0; k < slots; k++) {
      const maxPer = k < subjects.length ? 1 : Math.floor(MAX_SAME_SUBJECT_MINUTES_PER_DAY / ACTIVITY_MINUTES);
      const pool = subjects.filter((s) => (used.get(s.subjectId) ?? 0) < maxPer);
      if (pool.length === 0) break;
      pool.sort((a, b) => vt.get(a.subjectId)! - vt.get(b.subjectId)! || b.examQuestions - a.examQuestions || a.sortOrder - b.sortOrder);
      const s = pool[0];
      vt.set(s.subjectId, vt.get(s.subjectId)! + 1 / Math.max(1, s.examQuestions));
      used.set(s.subjectId, (used.get(s.subjectId) ?? 0) + 1);
      const n = counter.get(s.subjectId)!;
      counter.set(s.subjectId, n + 1);
      const isRev = n % 2 === 0;
      const segs = take(s, isRev ? REV_SEGMENTS : QUIZ_SEGMENTS);
      acts.push({
        key: `FINAL#${s.subjectId}#${isRev ? "R" : "Q"}${Math.floor(ord / 7) + 1}-${n + 1}`,
        type: isRev ? "REVISAO" : "QUESTOES",
        subjectId: s.subjectId,
        aulaId: segs[0].aulaId,
        minutes: ACTIVITY_MINUTES,
        segmentIds: segs.map((x) => x.id),
        refKeys: [],
        scope: "FINAL",
        day: ord % 7,
        ...(isRev ? {} : { quiz: { questions: QUIZ.questions, limitSeconds: QUIZ.limitSeconds, mixed: true } }),
      });
    }
    // revisão aquece o dia; caderno fecha
    acts.sort((a, b) => (a.type === b.type ? 0 : a.type === "REVISAO" ? -1 : 1));
    days.set(ord, acts);
    weekUsed.set(week, usedInWeek + acts.length * ACTIVITY_MINUTES);
  }
  return days;
}

/** D-1: uma única Revisão, nos trechos mais relevantes da disciplina de maior peso na prova. */
export function buildEveReview(subjects: ReviewSubject[], ord: number): PlannedActivity | null {
  const s = subjects
    .filter((x) => x.segments.length > 0)
    .sort((a, b) => b.examQuestions - a.examQuestions || a.sortOrder - b.sortOrder)[0];
  if (!s) return null;
  const segs = s.segments.slice(0, EVE_SEGMENTS);
  return {
    key: `FINAL#${s.subjectId}#VESPERA`,
    type: "REVISAO",
    subjectId: s.subjectId,
    aulaId: segs[0].aulaId,
    minutes: EVE_REVIEW_MINUTES,
    segmentIds: segs.map((x) => x.id),
    refKeys: [],
    scope: "FINAL",
    day: ord % 7,
  };
}
