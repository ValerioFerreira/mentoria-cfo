// Transforma as aulas selecionadas em atividades e as distribui em semanas (em minutos).
import {
  fixacaoMinutes, pickFixChunks, questoesMinutes, QUIZ_DEFAULT, revisaoMinutes, splitEven, teoriaMinutes, tierShape,
  type AulaBlueprint,
} from "./blueprint";
import { addDays } from "./dates";
import { assignDays, weekFraction } from "./days";
import type { PlannedActivity, PlannedWeek, Tier } from "./types";

/** Ciclo de uma aula na camada escolhida: Essencial = T T T … Q; Completo/Aprofundamento = [T T T R] [T T T R] … F… Q… */
export function buildAulaCycle(bp: AulaBlueprint, tier: Tier): PlannedActivity[] {
  const aulaId = bp.aula.id;
  const subjectId = aulaId.split("/")[0];
  const shape = tierShape(bp, tier);
  const out: PlannedActivity[] = [];

  // Modo Turbo: consolida todas as teorias da aula em uma única atividade com intervalo unificado de páginas
  if (bp.turbo) {
    const allSegmentIds = bp.teoria.flatMap((u) => u.segmentIds);
    const totalMinutes = bp.teoria.reduce((n, u) => n + teoriaMinutes(u, bp), 0);
    return [
      {
        key: `${aulaId}#TURBO`,
        type: "TEORIA",
        subjectId,
        aulaId,
        minutes: totalMinutes,
        segmentIds: allSegmentIds,
        refKeys: [],
        scope: "AULA",
        turbo: true,
      },
    ];
  }

  const teorias: PlannedActivity[] = bp.teoria.map((u, i) => ({
    key: `${aulaId}#T${i + 1}`,
    type: "TEORIA",
    subjectId,
    aulaId,
    minutes: teoriaMinutes(u, bp),
    segmentIds: u.segmentIds,
    refKeys: [],
    scope: "AULA",
  }));

  // sem Revisão (camada Essencial): a teoria corre direto; o caderno vem ao final
  if (shape.reviews === 0) out.push(...teorias);
  const reviewGroups = splitEven(teorias.length, shape.reviews);
  reviewGroups.forEach((group, gi) => {
    for (const i of group) out.push(teorias[i]);
    out.push({
      key: `${aulaId}#R${gi + 1}`,
      type: "REVISAO",
      subjectId,
      aulaId,
      minutes: revisaoMinutes(group.length, bp),
      segmentIds: group.flatMap((i) => teorias[i].segmentIds),
      refKeys: group.map((i) => teorias[i].key),
      scope: "AULA",
    });
  });

  pickFixChunks(bp, shape.fixChunks).forEach((ranges, i) => {
    out.push({
      key: `${aulaId}#F${i + 1}`,
      type: "FIXACAO",
      subjectId,
      aulaId,
      minutes: fixacaoMinutes(bp),
      segmentIds: [],
      refKeys: [],
      fixRanges: ranges,
      scope: "AULA",
    });
  });

  splitEven(teorias.length, shape.quizzes).forEach((group, i) => {
    out.push({
      key: `${aulaId}#Q${i + 1}`,
      type: "QUESTOES",
      subjectId,
      aulaId,
      minutes: questoesMinutes(bp),
      segmentIds: group.flatMap((j) => teorias[j].segmentIds),
      refKeys: group.map((j) => teorias[j].key),
      quiz: { ...QUIZ_DEFAULT },
      scope: "AULA",
    });
  });
  return out;
}

export interface StreamInfo {
  subjectId: string;
  examQuestions: number;
  sortOrder: number;
  queue: PlannedActivity[];
}

/** Reparte `total` entre pesos (maiores restos), garantindo ao menos 1 a cada um quando total >= n. */
export function apportion(weights: number[], total: number): number[] {
  const n = weights.length;
  if (n === 0) return [];
  const sum = weights.reduce((a, b) => a + b, 0) || 1;
  const exact = weights.map((w) => (total * w) / sum);
  const out = exact.map(Math.floor);
  let rest = total - out.reduce((a, b) => a + b, 0);
  const byFrac = exact.map((e, i) => ({ i, f: e - Math.floor(e) })).sort((a, b) => b.f - a.f || a.i - b.i);
  for (let k = 0; rest > 0; k++, rest--) out[byFrac[k % n].i]++;
  if (total >= n) {
    for (let i = 0; i < n; i++) {
      if (out[i] === 0) {
        const donor = out.indexOf(Math.max(...out));
        out[donor]--;
        out[i]++;
      }
    }
  }
  return out;
}

const sumMinutes = (xs: PlannedActivity[]) => xs.reduce((n, a) => n + a.minutes, 0);

/**
 * Distribui as filas (uma por disciplina, ordem interna preservada) em semanas de `weeklyMinutes` minutos.
 * Cada semana tem um foco de poucas disciplinas (menos troca de contexto), com cota proporcional ao que falta;
 * as atividades são retiradas por "déficit": sempre da disciplina mais atrasada em relação à sua cota.
 */
export function scheduleStreams(
  streams: StreamInfo[],
  weeklyMinutes: number,
  maxWeeks: number,
  startDate: string,
  focusSubjects: number,
  firstDay = 0,
): PlannedWeek[] {
  const total = new Map(streams.map((s) => [s.subjectId, sumMinutes(s.queue)]));
  const pos = new Map(streams.map((s) => [s.subjectId, 0]));
  const left = (s: StreamInfo) => sumMinutes(s.queue.slice(pos.get(s.subjectId) ?? 0));
  const next = (s: StreamInfo) => s.queue[pos.get(s.subjectId) ?? 0] as PlannedActivity | undefined;
  const weeks: PlannedWeek[] = [];

  for (let w = 1; w <= maxWeeks; w++) {
    const active = streams.filter((s) => next(s));
    if (active.length === 0) break;
    // na semana em que o aluno começa no meio, só entram os dias que restam
    const weekMinutes = w === 1 ? Math.max(30, Math.round(weeklyMinutes * weekFraction(firstDay))) : weeklyMinutes;

    // foco da semana: disciplinas com maior fração ainda por fazer
    active.sort(
      (a, b) =>
        left(b) / total.get(b.subjectId)! - left(a) / total.get(a.subjectId)! ||
        b.examQuestions - a.examQuestions ||
        a.sortOrder - b.sortOrder,
    );
    const capacity = Math.min(weekMinutes, active.reduce((n, s) => n + left(s), 0));
    const focus = active.slice(0, Math.max(1, Math.min(focusSubjects, active.length)));
    const weights = focus.map((s) => total.get(s.subjectId)!);
    const wsum = weights.reduce((a, b) => a + b, 0) || 1;
    const quota = new Map(focus.map((s, i) => [s.subjectId, (capacity * weights[i]) / wsum]));
    const taken = new Map<string, PlannedActivity[]>();
    let used = 0;

    const hardCap = weekMinutes * 1.05;
    const takenMin = (id: string) => sumMinutes(taken.get(id) ?? []);
    for (let guard = 0; guard < 500; guard++) {
      let pool = focus.filter((s) => next(s) && used + next(s)!.minutes <= hardCap);
      if (pool.length === 0) {
        // o foco acabou antes de fechar a semana: amplia com a próxima disciplina
        const extra = active.find((s) => !focus.includes(s) && next(s) && used + next(s)!.minutes <= hardCap);
        if (!extra || used >= capacity * 0.9) break;
        focus.push(extra);
        quota.set(extra.subjectId, Math.max(0, capacity - used));
        pool = [extra];
      }
      // quem tem maior déficit (cota − já retirado) escolhe a próxima atividade
      pool.sort((a, b) => quota.get(b.subjectId)! - takenMin(b.subjectId) - (quota.get(a.subjectId)! - takenMin(a.subjectId)) || a.sortOrder - b.sortOrder);
      const s = pool[0];
      const act = next(s)!;
      const deficit = quota.get(s.subjectId)! - takenMin(s.subjectId);
      if (deficit < act.minutes / 2 && used >= capacity * 0.9) break;
      taken.set(s.subjectId, [...(taken.get(s.subjectId) ?? []), act]);
      pos.set(s.subjectId, pos.get(s.subjectId)! + 1);
      used += act.minutes;
    }

    const byOrder = new Map(streams.map((s) => [s.subjectId, s]));
    const days = assignDays(
      [...taken].map(([subjectId, acts]) => ({ subjectId, activities: acts, sortOrder: byOrder.get(subjectId)!.sortOrder })),
      weekMinutes,
      w === 1 ? firstDay : 0,
    );
    weeks.push({
      index: w,
      startDate: addDays(startDate, (w - 1) * 7),
      kind: "CONTENT",
      targetMinutes: days.reduce((n, a) => n + a.minutes, 0),
      activities: days,
    });
  }
  return weeks;
}
