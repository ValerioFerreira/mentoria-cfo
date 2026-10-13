// Agregações de desempenho (funções puras): tempo estudado, questões, acerto e projeção em relação ao edital.
// Todo agrupamento por dia/semana usa o dia civil de Recife (não o UTC, que vira o dia às 21h).
import { addDaysISO, dayOfWeekIndex, diffDaysISO, todayISO } from "./plan-time";

export interface TimeRow {
  seconds: number;
  startedAt: Date;
  subjectId: string | null;
}

export interface QuizRow {
  subjectId: string;
  topic: string | null;
  chosen: string | null;
  isCorrect: boolean | null;
  seconds: number;
  finishedAt: Date;
}

export interface SubjectMeta {
  id: string;
  name: string;
  block: "I" | "II" | "III";
  examQuestions: number;
}

export function totalSeconds(rows: TimeRow[]): number {
  return rows.reduce((n, r) => n + r.seconds, 0);
}

export function secondsBySubject(rows: TimeRow[]): Map<string, number> {
  const m = new Map<string, number>();
  for (const r of rows) m.set(r.subjectId ?? "_none", (m.get(r.subjectId ?? "_none") ?? 0) + r.seconds);
  return m;
}

/** Índice (1-based) da semana do plano em que cai `date` (dia civil de Recife), ou null se fora do intervalo. */
export function weekIndexOf(date: Date, planStart: Date, totalWeeks: number): number | null {
  const days = diffDaysISO(planStart.toISOString().slice(0, 10), todayISO(date));
  if (days < 0) return null;
  const w = Math.floor(days / 7) + 1;
  return w <= totalWeeks ? w : null;
}

export function secondsByWeek(rows: TimeRow[], planStart: Date, totalWeeks: number): number[] {
  const out = Array.from({ length: totalWeeks }, () => 0);
  for (const r of rows) {
    const w = weekIndexOf(r.startedAt, planStart, totalWeeks);
    if (w) out[w - 1] += r.seconds;
  }
  return out;
}

/** Segundos estudados na semana civil (segunda a domingo, Recife) que contém `now`, haja ou não plano. */
export function secondsThisWeek(rows: TimeRow[], now: Date): number {
  const today = todayISO(now);
  const monday = addDaysISO(today, -dayOfWeekIndex(today));
  const sunday = addDaysISO(monday, 6);
  return rows.reduce((n, r) => {
    const day = todayISO(r.startedAt);
    return day >= monday && day <= sunday ? n + r.seconds : n;
  }, 0);
}

/** Dias consecutivos (até hoje ou ontem) com algum estudo registrado. Dias civis de Recife. */
export function streakDays(rows: TimeRow[], now: Date): number {
  const days = new Set(rows.map((r) => todayISO(r.startedAt)));
  let d = todayISO(now);
  if (!days.has(d)) d = addDaysISO(d, -1); // hoje ainda pode estar em aberto
  let n = 0;
  while (days.has(d)) {
    n++;
    d = addDaysISO(d, -1);
  }
  return n;
}

export interface DayTotal {
  date: string; // AAAA-MM-DD (dia civil de Recife)
  seconds: number;
}

/** Segundos estudados por dia nos últimos `days` dias (inclui hoje, do mais antigo ao mais recente). Dias civis de Recife. */
export function secondsByDay(rows: TimeRow[], now: Date, days: number): DayTotal[] {
  const by = new Map<string, number>();
  for (const r of rows) {
    const k = todayISO(r.startedAt);
    by.set(k, (by.get(k) ?? 0) + r.seconds);
  }
  const today = todayISO(now);
  return Array.from({ length: days }, (_, i) => {
    const date = addDaysISO(today, -(days - 1 - i));
    return { date, seconds: by.get(date) ?? 0 };
  });
}

export interface SubjectQuizStats {
  subjectId: string;
  answered: number; // respostas efetivas (não em branco)
  total: number; // questões apresentadas (inclui em branco)
  correct: number;
  accuracy: number | null; // acertos / total (em branco conta como erro, como na prova)
  avgSeconds: number;
}

export function quizBySubject(rows: QuizRow[]): Map<string, SubjectQuizStats> {
  const m = new Map<string, QuizRow[]>();
  for (const r of rows) m.set(r.subjectId, [...(m.get(r.subjectId) ?? []), r]);
  const out = new Map<string, SubjectQuizStats>();
  for (const [id, rs] of m) {
    const correct = rs.filter((r) => r.isCorrect).length;
    out.set(id, {
      subjectId: id,
      answered: rs.filter((r) => r.chosen !== null).length,
      total: rs.length,
      correct,
      accuracy: rs.length ? correct / rs.length : null,
      avgSeconds: rs.length ? Math.round(rs.reduce((n, r) => n + r.seconds, 0) / rs.length) : 0,
    });
  }
  return out;
}

export interface WeakTopic {
  subjectId: string;
  topic: string;
  attempts: number;
  accuracy: number;
}

/** Assuntos com pior acerto (mínimo de `minAttempts` respostas efetivas). */
export function weakTopics(rows: QuizRow[], minAttempts = 3, limit = 8): WeakTopic[] {
  const g = new Map<string, QuizRow[]>();
  for (const r of rows.filter((x) => x.topic && x.chosen !== null)) g.set(`${r.subjectId}::${r.topic}`, [...(g.get(`${r.subjectId}::${r.topic}`) ?? []), r]);
  return [...g.entries()]
    .filter(([, rs]) => rs.length >= minAttempts)
    .map(([k, rs]) => ({ subjectId: k.split("::")[0], topic: k.split("::")[1], attempts: rs.length, accuracy: rs.filter((r) => r.isCorrect).length / rs.length }))
    .filter((t) => t.accuracy < 0.7)
    .sort((a, b) => a.accuracy - b.accuracy || b.attempts - a.attempts)
    .slice(0, limit);
}

export const MIN_QUESTIONS_FOR_PROJECTION = 10;

/** Dados mínimos para desenhar cada gráfico do Desempenho; abaixo disso o gráfico fica em branco e a tela diz o que falta. */
export const MIN_TREND_CADERNOS = 3;
export const MIN_HEAT_DAYS = 3;
export const MIN_WEEKS_WITH_STUDY = 2;

export interface ChartReadiness {
  ready: boolean;
  /** quanto falta para atingir o mínimo (0 quando pronto) */
  missing: number;
}

export function chartReadiness(have: number, min: number): ChartReadiness {
  return { ready: have >= min, missing: Math.max(0, min - have) };
}

/** Semanas do plano com algum tempo lançado. */
export function weeksWithStudy(byWeekSeconds: number[]): number {
  return byWeekSeconds.filter((s) => s > 0).length;
}

export interface BlockProjection {
  block: "I" | "II" | "III";
  points: number; // pontos da prova no bloco (considerando só as disciplinas do aluno)
  projected: number | null; // acertos projetados no bloco (null se faltar dado)
  floorPct: number; // 30 (edital)
  status: "ok" | "risco" | "sem-dados";
  subjects: { id: string; name: string; examQuestions: number; accuracy: number | null; projected: number | null; total: number }[];
}

/**
 * Projeta a nota por bloco: acerto atual da disciplina × questões da disciplina na prova.
 * Regras do edital: ≥30% em cada bloco, nenhuma área zerada, ≥30% no total.
 */
export function projectExam(subjects: SubjectMeta[], stats: Map<string, SubjectQuizStats>): BlockProjection[] {
  return (["I", "II", "III"] as const).map((block) => {
    const subs = subjects.filter((s) => s.block === block);
    const rows = subs.map((s) => {
      const st = stats.get(s.id);
      const enough = st && st.total >= MIN_QUESTIONS_FOR_PROJECTION && st.accuracy !== null;
      return { id: s.id, name: s.name, examQuestions: s.examQuestions, accuracy: enough ? st!.accuracy : null, projected: enough ? s.examQuestions * st!.accuracy! : null, total: st?.total ?? 0 };
    });
    const points = subs.reduce((n, s) => n + s.examQuestions, 0);
    const known = rows.every((r) => r.projected !== null);
    const projected = known ? rows.reduce((n, r) => n + r.projected!, 0) : null;
    const zero = rows.some((r) => r.projected !== null && r.projected === 0);
    const status = projected === null ? "sem-dados" : projected / points < 0.3 || zero ? "risco" : "ok";
    return { block, points, projected, floorPct: 30, status, subjects: rows };
  });
}
