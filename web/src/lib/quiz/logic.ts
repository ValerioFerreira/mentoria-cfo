// Lógica pura do caderno de questões: seleção, nota e pontos de atenção.

export interface Candidate {
  id: string;
  segmentId: string;
  /** vezes que o aluno já respondeu esta questão */
  seen: number;
  /** resultado da última resposta (null = nunca respondeu) */
  lastCorrect: boolean | null;
}

/** PRNG determinístico (mulberry32) para sorteios reproduzíveis por sessão. */
export function rng(seed: number): () => number {
  let a = seed >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

export function hashSeed(s: string): number {
  let h = 2166136261;
  for (let i = 0; i < s.length; i++) {
    h ^= s.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}

const W_UNSEEN = 3;
const W_WRONG = 2.2;
const W_SEEN = 1;
const SAME_SEGMENT_PENALTY = 0.6;

/** Sorteia `n` questões priorizando as inéditas e as que o aluno errou, e espalhando entre os trechos. */
export function pickQuestions(candidates: Candidate[], n: number, seed: number): string[] {
  const rand = rng(seed);
  const pool = [...candidates];
  const picked: Candidate[] = [];
  const perSegment = new Map<string, number>();
  while (picked.length < Math.min(n, candidates.length)) {
    const weights = pool.map((c) => {
      const base = c.seen === 0 ? W_UNSEEN : c.lastCorrect === false ? W_WRONG : W_SEEN;
      return base * Math.pow(SAME_SEGMENT_PENALTY, perSegment.get(c.segmentId) ?? 0);
    });
    const total = weights.reduce((a, b) => a + b, 0);
    let r = rand() * total;
    let idx = 0;
    for (; idx < weights.length - 1; idx++) {
      r -= weights[idx];
      if (r <= 0) break;
    }
    const [c] = pool.splice(idx, 1);
    picked.push(c);
    perSegment.set(c.segmentId, (perSegment.get(c.segmentId) ?? 0) + 1);
  }
  // embaralha a ordem final
  for (let i = picked.length - 1; i > 0; i--) {
    const j = Math.floor(rand() * (i + 1));
    [picked[i], picked[j]] = [picked[j], picked[i]];
  }
  return picked.map((c) => c.id);
}

export interface AnswerRow {
  questionId: string;
  topic: string | null;
  segmentId: string;
  pageRef: number | null;
  chosen: string | null;
  correctLabel: string;
  seconds: number;
}

export interface Score {
  total: number;
  correct: number;
  wrong: number;
  blank: number;
  percent: number;
}

export function score(rows: AnswerRow[]): Score {
  const correct = rows.filter((r) => r.chosen === r.correctLabel).length;
  const blank = rows.filter((r) => r.chosen === null).length;
  return {
    total: rows.length,
    correct,
    blank,
    wrong: rows.length - correct - blank,
    percent: rows.length ? Math.round((100 * correct) / rows.length) : 0,
  };
}

export interface AttentionPoint {
  topic: string;
  segmentId: string;
  pageRef: number | null;
  attempts: number;
  correct: number;
  accuracy: number;
  avgSeconds: number;
  reason: "acerto baixo" | "muito lento";
}

/** Assuntos com acerto < 60% ou lentos (e com acerto < 80%), do pior para o melhor. */
export function attentionPoints(rows: AnswerRow[], limit = 5): AttentionPoint[] {
  if (rows.length === 0) return [];
  const overall = rows.reduce((n, r) => n + r.seconds, 0) / rows.length;
  const groups = new Map<string, AnswerRow[]>();
  for (const r of rows) {
    const key = `${r.segmentId}::${r.topic ?? "Assunto geral"}`;
    groups.set(key, [...(groups.get(key) ?? []), r]);
  }
  const out: AttentionPoint[] = [];
  for (const [key, rs] of groups) {
    const correct = rs.filter((r) => r.chosen === r.correctLabel).length;
    const accuracy = correct / rs.length;
    const avg = rs.reduce((n, r) => n + r.seconds, 0) / rs.length;
    const slow = overall > 0 && avg > 1.5 * overall && accuracy < 0.8;
    if (accuracy < 0.6 || slow) {
      const wrongRef = rs.find((r) => r.chosen !== r.correctLabel && r.pageRef != null)?.pageRef ?? rs.find((r) => r.pageRef != null)?.pageRef ?? null;
      out.push({
        topic: key.split("::")[1],
        segmentId: key.split("::")[0],
        pageRef: wrongRef,
        attempts: rs.length,
        correct,
        accuracy,
        avgSeconds: Math.round(avg),
        reason: accuracy < 0.6 ? "acerto baixo" : "muito lento",
      });
    }
  }
  return out.sort((a, b) => a.accuracy - b.accuracy || b.avgSeconds - a.avgSeconds).slice(0, limit);
}

export function remainingSeconds(startedAtMs: number, limitSeconds: number, nowMs: number): number {
  return Math.max(0, limitSeconds - Math.floor((nowMs - startedAtMs) / 1000));
}
