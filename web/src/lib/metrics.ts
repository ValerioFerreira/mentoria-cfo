// Agregações de desempenho (funções puras): tempo estudado, questões, acerto e projeção em relação ao edital.

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

/** Índice (1-based) da semana do plano em que cai `date`, ou null se fora do intervalo. */
export function weekIndexOf(date: Date, planStart: Date, totalWeeks: number): number | null {
  const days = Math.floor((date.getTime() - planStart.getTime()) / 86_400_000);
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

/** Dias consecutivos (até hoje ou ontem) com algum estudo registrado. Datas em UTC. */
export function streakDays(rows: TimeRow[], now: Date): number {
  const days = new Set(rows.map((r) => r.startedAt.toISOString().slice(0, 10)));
  let d = new Date(Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate()));
  if (!days.has(d.toISOString().slice(0, 10))) d = new Date(d.getTime() - 86_400_000); // hoje ainda pode estar em aberto
  let n = 0;
  while (days.has(d.toISOString().slice(0, 10))) {
    n++;
    d = new Date(d.getTime() - 86_400_000);
  }
  return n;
}

export interface DayTotal {
  date: string; // AAAA-MM-DD (UTC)
  seconds: number;
}

/** Segundos estudados por dia nos últimos `days` dias (inclui hoje, do mais antigo ao mais recente). Datas em UTC. */
export function secondsByDay(rows: TimeRow[], now: Date, days: number): DayTotal[] {
  const by = new Map<string, number>();
  for (const r of rows) {
    const k = r.startedAt.toISOString().slice(0, 10);
    by.set(k, (by.get(k) ?? 0) + r.seconds);
  }
  const today = Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate());
  return Array.from({ length: days }, (_, i) => {
    const date = new Date(today - (days - 1 - i) * 86_400_000).toISOString().slice(0, 10);
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
