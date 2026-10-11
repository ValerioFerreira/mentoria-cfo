import { describe, expect, it } from "vitest";
import { buildBlueprint } from "./blueprint";
import { DAY_WEIGHTS, MAX_SAME_SUBJECT_MINUTES_PER_DAY } from "./constants";
import { calendarCapacity, dayTarget, scheduleCalendar, weekFraction, type CalendarStream } from "./days";
import { buildAulaCycle } from "./schedule";
import { mkAula, mkSeg } from "./testkit";
import type { PlannedActivity, Tier } from "./types";

/** Disciplina sintética com `aulas` aulas de `teorias` Teorias cada (ciclo na camada `tier`). */
function stream(id: string, aulas: number, teorias: number, tier: Tier = 1, order = 1, exam = 10): CalendarStream {
  const queue = Array.from({ length: aulas }, (_, i) => {
    const aulaId = `${id}/a${String(i + 1).padStart(2, "0")}`;
    const segs = Array.from({ length: teorias }, (_, j) => mkSeg(aulaId, j + 1, 12, 12, 1 + j * 12));
    return buildAulaCycle(buildBlueprint(mkAula(aulaId, i + 1, { commentedRuns: [[1, 24]] }), segs, 1), tier);
  }).flat();
  return { subjectId: id, examQuestions: exam, sortOrder: order, queue };
}
const flat = (days: Map<number, PlannedActivity[]>) => [...days.entries()].sort((a, b) => a[0] - b[0]).flatMap(([ord, acts]) => acts.map((a) => ({ ...a, ord })));
const WEEKLY = 1200; // 20 h

describe("alvo diário, capacidade e fração da semana", () => {
  it("o alvo de cada dia segue os pesos e a semana soma a meta", () => {
    const sum = Array.from({ length: 7 }, (_, d) => dayTarget(WEEKLY, d)).reduce((a, b) => a + b, 0);
    expect(sum).toBeCloseTo(WEEKLY);
    expect(dayTarget(WEEKLY, 6)).toBeLessThan(dayTarget(WEEKLY, 0)); // domingo é leve
    expect(dayTarget(WEEKLY, 7)).toBeCloseTo(dayTarget(WEEKLY, 0)); // o ciclo semanal se repete
  });
  it("capacidade entre dois dias soma os alvos de cada dia", () => {
    expect(calendarCapacity(WEEKLY, 0, 6)).toBeCloseTo(WEEKLY);
    expect(calendarCapacity(WEEKLY, 0, 13)).toBeCloseTo(2 * WEEKLY);
    expect(calendarCapacity(WEEKLY, 3, 2)).toBe(0);
  });
  it("weekFraction: 1 a partir de segunda, só o domingo (leve) a partir de domingo", () => {
    expect(weekFraction(0)).toBe(1);
    expect(weekFraction(6)).toBeCloseTo(DAY_WEIGHTS[6] / DAY_WEIGHTS.reduce((a, b) => a + b, 0));
    expect(weekFraction(3)).toBeLessThan(weekFraction(2));
  });
});

describe("scheduleCalendar", () => {
  const streams = () => [stream("direito-constitucional", 3, 3, 2, 1, 10), stream("matematica", 3, 3, 2, 2, 8), stream("lingua-portuguesa", 3, 3, 2, 3, 12)];

  it("agenda tudo quando há dias de sobra, sem perder nem duplicar atividade", () => {
    const s = streams();
    const total = s.reduce((n, x) => n + x.queue.length, 0);
    const r = scheduleCalendar(s, { weeklyMinutes: WEEKLY, firstOrd: 0, lastOrd: 12 * 7 - 1 });
    expect(r.leftover).toBe(0);
    const acts = flat(r.days);
    expect(acts).toHaveLength(total);
    expect(new Set(acts.map((a) => a.key)).size).toBe(total);
    for (const a of acts) expect(a.day).toBe(a.ord % 7);
  });

  it("respeita a ordem do ciclo e as folgas: Revisão depois da Teoria, Questões depois da Fixação (≥ 1 dia)", () => {
    const s = streams();
    const deps = new Map(s.flatMap((x) => x.queue).map((a) => [a.key, a.after]));
    const r = scheduleCalendar(s, { weeklyMinutes: WEEKLY, firstOrd: 0, lastOrd: 12 * 7 - 1 });
    const ord = new Map(flat(r.days).map((a) => [a.key, a.ord]));
    for (const [key, after] of deps) {
      for (const d of after) expect(ord.get(key)! - ord.get(d.key)!, `${key} ← ${d.key}`).toBeGreaterThanOrEqual(d.gap);
    }
  });

  it("nunca passa de 120 min por disciplina/dia e usa uma atividade por disciplina/dia quando há disciplinas de sobra", () => {
    const r = scheduleCalendar(streams(), { weeklyMinutes: WEEKLY, firstOrd: 0, lastOrd: 12 * 7 - 1 });
    const per = new Map<string, PlannedActivity[]>();
    for (const a of flat(r.days)) per.set(`${a.ord}|${a.subjectId}`, [...(per.get(`${a.ord}|${a.subjectId}`) ?? []), a]);
    for (const [k, l] of per) {
      expect(l.reduce((n, a) => n + a.minutes, 0), k).toBeLessThanOrEqual(MAX_SAME_SUBJECT_MINUTES_PER_DAY);
    }
    const multi = [...per.values()].filter((l) => l.length > 1).length;
    expect(multi / per.size).toBeLessThan(0.15);
  });

  it("cada semana respeita a meta com no máximo 5% de folga", () => {
    const r = scheduleCalendar(streams(), { weeklyMinutes: WEEKLY, firstOrd: 0, lastOrd: 12 * 7 - 1 });
    const byWeek = new Map<number, number>();
    for (const a of flat(r.days)) byWeek.set(Math.floor(a.ord / 7), (byWeek.get(Math.floor(a.ord / 7)) ?? 0) + a.minutes);
    for (const [w, m] of byWeek) expect(m, `semana ${w + 1}`).toBeLessThanOrEqual(WEEKLY * 1.05 + 1e-6);
  });

  it("o excedente que não cabe nos dias disponíveis fica de fora (leftover) e nada passa de lastOrd", () => {
    const s = streams();
    const total = s.reduce((n, x) => n + x.queue.length, 0);
    const r = scheduleCalendar(s, { weeklyMinutes: WEEKLY, firstOrd: 0, lastOrd: 13 });
    const acts = flat(r.days);
    expect(r.leftover).toBeGreaterThan(0);
    expect(acts.length + r.leftover).toBe(total);
    expect(Math.max(...acts.map((a) => a.ord))).toBeLessThanOrEqual(13);
  });

  it("começando no meio da semana, nada cai antes do dia de início", () => {
    for (const firstOrd of [1, 3, 6]) {
      const r = scheduleCalendar(streams(), { weeklyMinutes: WEEKLY, firstOrd, lastOrd: 8 * 7 - 1 });
      expect(Math.min(...flat(r.days).map((a) => a.ord))).toBeGreaterThanOrEqual(firstOrd);
    }
  });

  it("a prática pronta passa na frente: poucos dias seguidos só de Teoria", () => {
    const r = scheduleCalendar(streams(), { weeklyMinutes: WEEKLY, firstOrd: 0, lastOrd: 12 * 7 - 1 });
    let run = 0;
    let max = 0;
    for (const [, acts] of [...r.days.entries()].sort((a, b) => a[0] - b[0])) {
      run = acts.every((a) => a.type === "TEORIA") ? run + 1 : 0;
      max = Math.max(max, run);
    }
    expect(max).toBeLessThanOrEqual(3);
  });

  it("dentro do dia, a Revisão aquece (vem antes da Teoria) e a prática fecha (vem depois da Teoria)", () => {
    const r = scheduleCalendar(streams(), { weeklyMinutes: WEEKLY, firstOrd: 0, lastOrd: 12 * 7 - 1 });
    for (const acts of r.days.values()) {
      const firstRev = acts.findIndex((a) => a.type === "REVISAO");
      const firstTheory = acts.findIndex((a) => a.type === "TEORIA");
      if (firstRev >= 0 && firstTheory >= 0) expect(firstRev).toBeLessThan(firstTheory);
      const lastTheory = acts.map((a) => a.type).lastIndexOf("TEORIA");
      const firstQuiz = acts.findIndex((a) => a.type === "FIXACAO" || a.type === "QUESTOES");
      if (firstQuiz >= 0 && lastTheory >= 0) expect(firstQuiz).toBeGreaterThan(lastTheory);
    }
  });

  it("uma única disciplina ocupa a semana respeitando o teto de 120 min por dia", () => {
    const r = scheduleCalendar([stream("lingua-inglesa", 4, 4, 1)], { weeklyMinutes: WEEKLY, firstOrd: 0, lastOrd: 30 * 7 - 1 });
    const per = new Map<number, number>();
    for (const a of flat(r.days)) per.set(a.ord, (per.get(a.ord) ?? 0) + a.minutes);
    for (const m of per.values()) expect(m).toBeLessThanOrEqual(MAX_SAME_SUBJECT_MINUTES_PER_DAY);
    expect(r.leftover).toBe(0);
  });

  it("sem filas não há dias; é determinístico e não altera as filas recebidas", () => {
    expect(scheduleCalendar([], { weeklyMinutes: WEEKLY, firstOrd: 0, lastOrd: 20 }).days.size).toBe(0);
    const s = streams();
    const before = JSON.stringify(s);
    const a = scheduleCalendar(s, { weeklyMinutes: WEEKLY, firstOrd: 0, lastOrd: 12 * 7 - 1 });
    const b = scheduleCalendar(streams(), { weeklyMinutes: WEEKLY, firstOrd: 0, lastOrd: 12 * 7 - 1 });
    expect(JSON.stringify(s)).toBe(before);
    expect(flat(a.days)).toEqual(flat(b.days));
  });

  it("as atividades entregues não carregam os pré-requisitos internos", () => {
    const r = scheduleCalendar(streams(), { weeklyMinutes: WEEKLY, firstOrd: 0, lastOrd: 12 * 7 - 1 });
    for (const a of flat(r.days)) expect("after" in a).toBe(false);
  });

  it("famílias iguais (jurídicas) não ficam coladas no mesmo dia quando há alternativa", () => {
    const s = [
      stream("direito-constitucional", 3, 3, 1, 1), stream("direito-administrativo", 3, 3, 1, 2),
      stream("matematica", 3, 3, 1, 3), stream("lingua-portuguesa", 3, 3, 1, 4),
    ];
    const r = scheduleCalendar(s, { weeklyMinutes: WEEKLY * 1.5, firstOrd: 0, lastOrd: 10 * 7 - 1 });
    let adjacent = 0;
    let pairs = 0;
    for (const acts of r.days.values()) {
      for (let i = 1; i < acts.length; i++) {
        pairs++;
        const j = (id: string) => id.startsWith("direito");
        if (j(acts[i].subjectId) && j(acts[i - 1].subjectId)) adjacent++;
      }
    }
    expect(adjacent / Math.max(1, pairs)).toBeLessThan(0.2);
  });

  it("os tipos agendados respeitam a ordem T→R→F→Q por aula também entre os tipos", () => {
    const r = scheduleCalendar(streams(), { weeklyMinutes: WEEKLY, firstOrd: 0, lastOrd: 12 * 7 - 1 });
    const byAula = new Map<string, ReturnType<typeof flat>>();
    for (const a of flat(r.days)) byAula.set(a.aulaId, [...(byAula.get(a.aulaId) ?? []), a]);
    for (const [aula, l] of byAula) {
      const first = (t: string) => Math.min(...l.filter((a) => a.type === t).map((a) => a.ord));
      const last = (t: string) => Math.max(...l.filter((a) => a.type === t).map((a) => a.ord));
      expect(first("REVISAO"), aula).toBeGreaterThan(first("TEORIA"));
      expect(first("FIXACAO"), aula).toBeGreaterThan(last("REVISAO"));
      expect(first("QUESTOES"), aula).toBeGreaterThan(last("FIXACAO"));
    }
  });
});
