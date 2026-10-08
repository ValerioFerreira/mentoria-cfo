// Semanas finais (e folgas de capacidade): revisão geral + cadernos mistos por disciplina.
import { apportion } from "./schedule";
import { addDays } from "./dates";
import { assignDays, weekFraction } from "./days";
import { QUIZ } from "./constants";
import type { PlannedActivity, PlannedWeek } from "./types";

export interface ReviewSubject {
  subjectId: string;
  examQuestions: number;
  sortOrder: number;
  /** Segmentos cobertos pelo plano (ou já dominados), do mais ao menos relevante. */
  segments: { id: string; aulaId: string }[];
}

const REV_SEGMENTS = 4;
const QUIZ_SEGMENTS = 8;
const EXAM_WEEK_FACTOR = 0.6;
const ACTIVITY_MINUTES = 60;

export function buildReviewWeeks(args: {
  firstIndex: number;
  lastIndex: number;
  startDate: string; // início do plano (segunda da semana 1)
  weeklyMinutes: number;
  subjects: ReviewSubject[];
  /** Dia da semana (0 = segunda) em que o aluno começa, se a semana 1 já for de revisão. */
  firstDay?: number;
}): PlannedWeek[] {
  const subjects = args.subjects.filter((s) => s.segments.length > 0);
  const weeks: PlannedWeek[] = [];
  const ptr = new Map(subjects.map((s) => [s.subjectId, 0]));
  const counter = new Map(subjects.map((s) => [s.subjectId, 0]));
  const slotsPerWeek = Math.max(1, Math.floor(args.weeklyMinutes / ACTIVITY_MINUTES));

  const take = (s: ReviewSubject, n: number) => {
    const start = ptr.get(s.subjectId)!;
    const picked = Array.from({ length: Math.min(n, s.segments.length) }, (_, i) => s.segments[(start + i) % s.segments.length]);
    ptr.set(s.subjectId, (start + n) % s.segments.length);
    return picked;
  };

  for (let w = args.firstIndex; w <= args.lastIndex; w++) {
    const isExamWeek = w === args.lastIndex;
    const firstDay = w === 1 ? args.firstDay ?? 0 : 0;
    const weekMinutes = Math.round(args.weeklyMinutes * (firstDay ? weekFraction(firstDay) : 1));
    const slots = Math.max(1, Math.ceil(slotsPerWeek * (isExamWeek ? EXAM_WEEK_FACTOR : 1) * (firstDay ? weekFraction(firstDay) : 1)));
    const quotas = subjects.length ? apportion(subjects.map((s) => s.examQuestions), slots) : [];
    const perSubject = new Map<string, PlannedActivity[]>();
    const pending = subjects.map((s, i) => ({ s, left: quotas[i] }));
    // intercala as disciplinas para não concentrar o mesmo assunto em sequência
    while (pending.some((p) => p.left > 0)) {
      for (const p of pending) {
        if (p.left <= 0) continue;
        p.left--;
        const n = counter.get(p.s.subjectId)!;
        counter.set(p.s.subjectId, n + 1);
        const isRev = n % 2 === 0;
        const segs = take(p.s, isRev ? REV_SEGMENTS : QUIZ_SEGMENTS);
        const key = `FINAL#${p.s.subjectId}#${isRev ? "R" : "Q"}${w}-${n + 1}`;
        const act: PlannedActivity = {
          key,
          type: isRev ? "REVISAO" : "QUESTOES",
          subjectId: p.s.subjectId,
          aulaId: segs[0].aulaId,
          minutes: ACTIVITY_MINUTES,
          segmentIds: segs.map((x) => x.id),
          refKeys: [],
          scope: "FINAL",
          ...(isRev ? {} : { quiz: { questions: QUIZ.questions, limitSeconds: QUIZ.limitSeconds, mixed: true } }),
        };
        perSubject.set(p.s.subjectId, [...(perSubject.get(p.s.subjectId) ?? []), act]);
      }
    }
    const acts = assignDays(
      subjects.filter((s) => perSubject.has(s.subjectId)).map((s) => ({ subjectId: s.subjectId, sortOrder: s.sortOrder, activities: perSubject.get(s.subjectId)! })),
      weekMinutes,
      firstDay,
    );
    weeks.push({
      index: w,
      startDate: addDays(args.startDate, (w - 1) * 7),
      kind: "FINAL_REVIEW",
      targetMinutes: acts.reduce((n, a) => n + a.minutes, 0),
      activities: acts,
    });
  }
  return weeks;
}
