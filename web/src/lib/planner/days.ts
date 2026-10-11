// Calendário do plano: distribui as atividades dos ciclos pelos dias (segunda → domingo), dia a dia, respeitando a ordem pedagógica.
//
// Princípios (com respaldo na literatura de aprendizagem):
//  1. Ordem e espaçamento: cada atividade só entra depois de seus pré-requisitos (Teoria → Revisão → Fixação → Questões) e com ao
//     menos 1 dia de intervalo entre as etapas do ciclo (a Revisão nunca cai no dia da Teoria que revê; as Questões vêm depois
//     da Fixação). (Cepeda et al., 2006; efeito do teste: Roediger & Karpicke)
//  2. Prática distribuída: no máximo ~2 h por disciplina/dia e, de preferência, 1 atividade por disciplina/dia; as disciplinas
//     se revezam em proporção ao que falta de cada uma, em vez de "semanas de foco".
//  3. Intercalação: matérias da mesma família (jurídicas, línguas, exatas, natureza) não ficam coladas no mesmo dia. (Rohrer &
//     Taylor; Brunmair & Richter, 2019)
//  4. Teoria e prática alternadas: a prática pronta (Revisão/Fixação/Questões) tem preferência sobre a Teoria nova da mesma
//     disciplina, e após 2 dias seguidos só de Teoria a prática passa na frente.
//  5. Carga cognitiva: a revisão da véspera abre o dia, o conteúdo novo e pesado (exatas) vem cedo e a prática fecha o dia;
//     domingo é o dia leve.
import { DAY_WEIGHTS, FAMILY, MAX_SAME_SUBJECT_MINUTES_PER_DAY } from "./constants";
import type { CycleActivity } from "./schedule";
import type { PlannedActivity } from "./types";

const WEEK_SUM = DAY_WEIGHTS.reduce<number>((a, b) => a + b, 0);
/** Quantas atividades à frente da fila de uma disciplina podem ser puxadas (para intercalar prática pronta com Teoria nova). */
const LOOKAHEAD = 12;
/** Quantas aulas por disciplina podem estar "abertas" (com ciclo em andamento) ao mesmo tempo. */
const OPEN_AULAS = 2;
const WEEK_OVERSHOOT = 1.05;
/**
 * Limite de aulas "em andamento" ao mesmo tempo: sem ele, todas as disciplinas avançariam em paralelo e a 1ª aula só fecharia
 * (Revisão, Fixação, Questões) muito tarde, com semanas inteiras só de Teoria. Cresce com o ritmo de atividades por dia.
 */
const MIN_WIP_AULAS = 3;
const WIP_PER_DAILY_ACTIVITY = 2.5;
const TYPICAL_ACTIVITY_MINUTES = 55;

/** Minutos de estudo previstos para o dia `ord` (0 = segunda da semana 1). */
export function dayTarget(weeklyMinutes: number, ord: number): number {
  return (weeklyMinutes * DAY_WEIGHTS[ord % 7]) / WEEK_SUM;
}

/** Capacidade (min) entre os dias `firstOrd` e `lastOrd`, inclusive. */
export function calendarCapacity(weeklyMinutes: number, firstOrd: number, lastOrd: number): number {
  let n = 0;
  for (let d = firstOrd; d <= lastOrd; d++) n += dayTarget(weeklyMinutes, d);
  return n;
}

/** Fração da semana que sobra a partir de `firstDay` (pelos pesos dos dias). */
export function weekFraction(firstDay: number): number {
  return DAY_WEIGHTS.slice(Math.max(0, Math.min(6, firstDay))).reduce<number>((a, b) => a + b, 0) / WEEK_SUM;
}

export interface CalendarStream {
  subjectId: string;
  examQuestions: number;
  sortOrder: number;
  /** Atividades da disciplina na ordem do curso (ciclo de cada aula selecionada). */
  queue: CycleActivity[];
}

export interface CalendarResult {
  /** Atividades de cada dia (chave = nº do dia desde a segunda da semana 1), já na ordem em que serão feitas. */
  days: Map<number, PlannedActivity[]>;
  /** Atividades que não couberam até o último dia. */
  leftover: number;
  /** Último dia com conteúdo (-1 se nenhum). */
  lastContentOrd: number;
}

const strip = (a: CycleActivity, day: number): PlannedActivity => {
  const { after: _after, cycle: _cycle, ...rest } = a;
  void _after;
  void _cycle;
  return { ...rest, day };
};

const isPractice = (a: PlannedActivity) => a.type !== "TEORIA";
const isRetrieval = (a: PlannedActivity) => a.type === "REVISAO" || a.type === "QUESTOES";

/** Ordem dentro do dia: revisão (aquece) → conteúdo novo pesado → demais → prática; sem famílias iguais coladas. */
function orderDay(entries: { a: CycleActivity; family: string; seq: number }[]): CycleActivity[] {
  const rank = (e: { a: CycleActivity; family: string }) =>
    e.a.type === "REVISAO" ? 0 : isPractice(e.a) ? 4 : e.family === "EXATAS" ? 1 : e.family === "LINGUAGEM" ? 3 : 2;
  const rest = [...entries];
  const out: CycleActivity[] = [];
  let lastFamily = "";
  while (rest.length) {
    // dentro de uma disciplina, a ordem em que as atividades entraram no dia é a da fila
    const heads = rest.filter((e) => !rest.some((o) => o !== e && o.a.subjectId === e.a.subjectId && o.seq < e.seq));
    heads.sort((a, b) => rank(a) + (a.family === lastFamily ? 1.5 : 0) - (rank(b) + (b.family === lastFamily ? 1.5 : 0)) || a.seq - b.seq);
    const e = heads[0];
    rest.splice(rest.indexOf(e), 1);
    lastFamily = e.family;
    out.push(e.a);
  }
  return out;
}

/**
 * Agenda as filas (uma por disciplina) nos dias de `firstOrd` a `lastOrd`. Cada dia:
 *  - só entram atividades "prontas" (pré-requisitos concluídos e com a folga em dias cumprida);
 *  - as disciplinas se revezam pela que está mais atrasada em relação à própria fila;
 *  - ≤ 120 min por disciplina/dia (1 atividade por disciplina; a 2ª só se o dia ainda estiver vazio);
 *  - a semana nunca passa de 105% da meta.
 */
export function scheduleCalendar(
  streams: CalendarStream[],
  opts: { weeklyMinutes: number; firstOrd: number; lastOrd: number },
): CalendarResult {
  const { weeklyMinutes, firstOrd, lastOrd } = opts;
  const st = streams
    .filter((s) => s.queue.length > 0)
    .map((s) => ({
      ...s,
      pending: [...s.queue],
      total: s.queue.reduce((n, a) => n + a.minutes, 0),
      done: 0,
      family: FAMILY[s.subjectId] ?? "OUTRA",
    }));
  const doneOrd = new Map<string, number>();
  const days = new Map<number, PlannedActivity[]>();
  const targets: number[] = [];
  for (let d = firstOrd; d <= lastOrd; d++) targets.push(dayTarget(weeklyMinutes, d));
  const suffix: number[] = new Array(targets.length + 1).fill(0);
  for (let i = targets.length - 1; i >= 0; i--) suffix[i] = suffix[i + 1] + targets[i];
  const weekCap = new Map<number, number>();
  for (let d = firstOrd; d <= lastOrd; d++) weekCap.set(Math.floor(d / 7), (weekCap.get(Math.floor(d / 7)) ?? 0) + targets[d - firstOrd]);
  const weekUsed = new Map<number, number>();

  const wipLimit = Math.max(MIN_WIP_AULAS, Math.ceil((weeklyMinutes / 7 / TYPICAL_ACTIVITY_MINUTES) * WIP_PER_DAILY_ACTIVITY));
  const remaining = new Map<string, number>();
  for (const s of st) for (const a of s.queue) remaining.set(a.cycle, (remaining.get(a.cycle) ?? 0) + 1);
  const started = new Set<string>();
  let wip = 0; // aulas com o ciclo iniciado e ainda não concluído

  let leftMin = st.reduce((n, s) => n + s.total, 0);
  let streak = 0; // dias seguidos só de Teoria
  let lastContentOrd = -1;
  let seq = 0;

  const ready = (a: CycleActivity, ord: number) => a.after.every((d) => {
    const o = doneOrd.get(d.key);
    return o !== undefined && ord >= o + d.gap;
  });
  /** Melhor atividade pronta da disciplina: prática (na ordem da fila) antes de Teoria nova. */
  const pick = (s: (typeof st)[number], ord: number): CycleActivity | null => {
    const open = new Set<string>();
    let firstTheory: CycleActivity | null = null;
    for (let i = 0; i < Math.min(s.pending.length, LOOKAHEAD); i++) {
      const a = s.pending[i];
      if (!open.has(a.cycle)) {
        if (open.size >= OPEN_AULAS) continue;
        open.add(a.cycle);
      }
      if (!ready(a, ord)) continue;
      if (!started.has(a.cycle) && wip >= wipLimit) continue; // só abre um ciclo novo quando há vaga
      if (isPractice(a)) return a;
      firstTheory ??= a;
    }
    return firstTheory;
  };

  for (let ord = firstOrd; ord <= lastOrd; ord++) {
    if (st.every((s) => s.pending.length === 0)) break;
    const week = Math.floor(ord / 7);
    const target = targets[ord - firstOrd];
    const ratio = leftMin / (suffix[ord - firstOrd] || 1);
    const stopAt = target * (ratio > 1 ? Math.min(1.25, ratio * 0.98) : 1); // atrasado: este dia carrega um pouco mais
    const cap = (weekCap.get(week) ?? 0) * WEEK_OVERSHOOT - (weekUsed.get(week) ?? 0);
    const today: { a: CycleActivity; family: string; seq: number }[] = [];
    const per = new Map<string, { min: number; count: number }>();
    let load = 0;

    for (const maxPer of [1, 2]) {
      if (maxPer === 2 && load >= stopAt * 0.7) break;
      for (;;) {
        if (today.length > 0 && load >= stopAt) break;
        const families = new Map<string, number>();
        for (const e of today) families.set(e.family, (families.get(e.family) ?? 0) + 1);
        let best: { s: (typeof st)[number]; a: CycleActivity; score: number } | null = null;
        for (const s of st) {
          if (s.pending.length === 0) continue;
          const u = per.get(s.subjectId) ?? { min: 0, count: 0 };
          if (u.count >= maxPer) continue;
          const a = pick(s, ord);
          if (!a) continue;
          if (u.min + a.minutes > MAX_SAME_SUBJECT_MINUTES_PER_DAY) continue;
          if (load + a.minutes > cap) continue;
          if (today.length > 0 && load + a.minutes > stopAt * 1.25 && load >= stopAt * 0.6) continue; // não estoura o dia
          let score = (1 - s.done / s.total) * 2 + s.examQuestions / 1000 - s.sortOrder * 0.001;
          score -= (families.get(s.family) ?? 0) * 0.4; // evita colar famílias iguais no mesmo dia
          if (isPractice(a)) score += streak >= 2 ? 1 : streak === 1 ? 0.4 : 0.15; // teoria e prática se alternam
          if (started.has(a.cycle)) score += 0.4; // terminar o ciclo já aberto antes de abrir outros
          if (ord % 7 === 6) score += isRetrieval(a) ? 0.3 : -0.3; // domingo: recuperação ativa
          if (!best || score > best.score) best = { s, a, score };
        }
        if (!best) break;
        const { s, a } = best;
        s.pending.splice(s.pending.indexOf(a), 1);
        s.done += a.minutes;
        leftMin -= a.minutes;
        doneOrd.set(a.key, ord);
        if (!started.has(a.cycle)) {
          started.add(a.cycle);
          wip++;
        }
        const left = remaining.get(a.cycle)! - 1;
        remaining.set(a.cycle, left);
        if (left === 0) wip--;
        const u = per.get(s.subjectId) ?? { min: 0, count: 0 };
        per.set(s.subjectId, { min: u.min + a.minutes, count: u.count + 1 });
        today.push({ a, family: s.family, seq: seq++ });
        load += a.minutes;
      }
    }

    if (today.length === 0) continue;
    const ordered = orderDay(today);
    days.set(ord, ordered.map((a) => strip(a, ord % 7)));
    weekUsed.set(week, (weekUsed.get(week) ?? 0) + load);
    streak = ordered.every((a) => a.type === "TEORIA") ? streak + 1 : 0;
    lastContentOrd = ord;
  }
  return { days, leftover: st.reduce((n, s) => n + s.pending.length, 0), lastContentOrd };
}
