// Blueprint do ciclo de uma aula: Teoria → Revisão → Fixação → Questões, por camada (tier), com o tempo de cada atividade.
import {
  FIXACAO_MINUTES, FIXACAO_PAGES_PER_HOUR, KNOWN_PACE, LEVEL_PACE, QUESTOES_MINUTES, QUIZ, REVISAO_MINUTES, SEGMENT,
  SUMMARY, TEORIA_MINUTES, TURBO,
} from "./constants";
import type { CatalogAula, FixRange, Known, Level, SegmentLite, Tier } from "./types";

export interface TeoriaUnit {
  segmentIds: string[];
  pages: number;
  load: number;
}

export interface AulaBlueprint {
  aula: CatalogAula;
  /** Unidades de Teoria normais (leitura do material, ~1 h cada). */
  teoria: TeoriaUnit[];
  /** Modo Turbo: unidades de menor importância trocadas pelo resumo analítico (~20 min cada). */
  summary: TeoriaUnit[];
  /** Quantas Teorias uma Revisão cobre (menor = mais revisões; nível baixo revisa mais). */
  reviewGroup: number;
  /** Faixas de páginas das questões comentadas (da própria aula ou de aulas de prática vinculadas). */
  fixRanges: FixRange[];
  fixPages: number;
  fixChunksFull: number;
  /** Multiplicador de tempo pelo nível do aluno na disciplina (1 = referência). */
  pace: number;
  /** Multiplicador de Teoria/Revisão: nível × "já estudei" desta aula. */
  readPace: number;
}

/** Todas as unidades da aula (Teoria normal + resumos), na ordem do curso. */
export function allUnits(bp: AulaBlueprint): TeoriaUnit[] {
  return [...bp.teoria, ...bp.summary].sort((a, b) => a.segmentIds[0].localeCompare(b.segmentIds[0]));
}

/** Passa a unidade `segmentId` de Teoria normal para resumo analítico (devolve um novo blueprint). */
export function withSummaryUnit(bp: AulaBlueprint, unit: TeoriaUnit): AulaBlueprint {
  return { ...bp, teoria: bp.teoria.filter((u) => u !== unit), summary: [...bp.summary, unit] };
}

const MERGE_UNTIL_PAGES = 8; // segmentos curtos são juntados enquanto a unidade tiver < 8 págs.
const MERGE_MAX_LOAD = 15;
const TAIL_MIN_PAGES = 5;

/** Junta segmentos muito curtos (ex.: 2–5 págs.) em uma única atividade de Teoria, respeitando o teto de páginas. */
export function bundleSegments(segs: SegmentLite[]): TeoriaUnit[] {
  const ordered = [...segs].sort((a, b) => a.order - b.order);
  const units: TeoriaUnit[] = [];
  for (const s of ordered) {
    const cur = units[units.length - 1];
    if (cur && cur.pages < MERGE_UNTIL_PAGES && cur.pages + s.pages <= SEGMENT.maxPages && cur.load + s.load <= MERGE_MAX_LOAD) {
      cur.segmentIds.push(s.id);
      cur.pages += s.pages;
      cur.load += s.load;
    } else {
      units.push({ segmentIds: [s.id], pages: s.pages, load: s.load });
    }
  }
  // cauda curta: absorve na unidade anterior se couber
  const last = units[units.length - 1];
  const prev = units[units.length - 2];
  if (last && prev && last.pages < TAIL_MIN_PAGES && prev.pages + last.pages <= SEGMENT.maxPages && prev.load + last.load <= MERGE_MAX_LOAD + 3) {
    prev.segmentIds.push(...last.segmentIds);
    prev.pages += last.pages;
    prev.load += last.load;
    units.pop();
  }
  return units;
}

export function reviewGroupFor(level: Level): number {
  return level === 0 ? 2 : level === 3 ? 4 : 3;
}

function fixRangesOf(aula: CatalogAula): FixRange[] {
  const own = aula.commentedRuns.map(([start, end]) => ({ start, end }));
  const linked = aula.practiceLinks.map((l) => ({ start: l.startPage, end: l.endPage, sourceAula: l.sourceAula }));
  return [...own, ...linked];
}

export function buildBlueprint(aula: CatalogAula, segs: SegmentLite[], level: Level, known: Known = 0): AulaBlueprint {
  const fixRanges = fixRangesOf(aula);
  const fixPages = fixRanges.reduce((n, r) => n + (r.end - r.start + 1), 0);
  const pace = LEVEL_PACE[level];
  return {
    aula,
    teoria: bundleSegments(segs),
    summary: [],
    reviewGroup: reviewGroupFor(level),
    fixRanges,
    fixPages,
    fixChunksFull: Math.ceil(fixPages / FIXACAO_PAGES_PER_HOUR),
    pace,
    readPace: known === 1 ? pace * KNOWN_PACE[1] : pace,
  };
}

// ───────────────────────── Tempo de cada atividade ─────────────────────────
/** Arredonda para múltiplos de 5 min e limita à faixa [lo, hi] da atividade. */
export function clampMinutes(m: number, lo: number, hi: number): number {
  return Math.min(hi, Math.max(lo, Math.round(m / 5) * 5));
}

/** Teoria: 50 a 80 min (alvo 60), ajustada pela carga de páginas e ritmo do aluno; unidade curta pode ir a 35 min. */
export function teoriaMinutes(u: TeoriaUnit, bp: AulaBlueprint): number {
  const raw = Math.min(u.load * TEORIA_MINUTES.perLoadUnit, TEORIA_MINUTES.max);
  const lo = u.pages < TEORIA_MINUTES.shortPages ? TEORIA_MINUTES.shortMin : TEORIA_MINUTES.min;
  return clampMinutes(raw * bp.readPace, lo, TEORIA_MINUTES.max);
}

/** Leitura do resumo analítico de uma unidade: ~20 min, menos para quem lê mais rápido (piso de 15 min). */
export function summaryMinutes(bp: Pick<AulaBlueprint, "readPace">): number {
  return Math.min(SUMMARY.minutesPerUnit, Math.max(SUMMARY.minMinutes, Math.round((SUMMARY.minutesPerUnit * bp.readPace) / 5) * 5));
}

/** Revisão de `n` Teorias: 30 a 60 min (reduzida = Turbo: metade do tempo, 25 a 35 min). */
export function revisaoMinutes(n: number, bp: AulaBlueprint, reduced = false): number {
  const base = Math.min(Math.max(REVISAO_MINUTES.base + REVISAO_MINUTES.perTeoria * n, REVISAO_MINUTES.min), REVISAO_MINUTES.max);
  if (reduced) return clampMinutes(base * TURBO.revisaoFactor * bp.readPace, TURBO.revisaoMin, TURBO.revisaoMax);
  return clampMinutes(base * bp.readPace, REVISAO_MINUTES.min, REVISAO_MINUTES.max);
}

export function fixacaoMinutes(bp: AulaBlueprint, reduced = false): number {
  if (reduced) return TURBO.fixacao;
  return clampMinutes(FIXACAO_MINUTES.normal * bp.pace, FIXACAO_MINUTES.min, FIXACAO_MINUTES.max);
}

/** Caderno: 25 questões em 60 min (reduzido = Turbo: 15 questões em 40 min). */
export function questoesMinutes(bp: AulaBlueprint, reduced = false): number {
  if (reduced) return TURBO.questoes;
  return clampMinutes(QUESTOES_MINUTES.normal * Math.max(bp.pace, 0.85), QUESTOES_MINUTES.min, QUESTOES_MINUTES.max);
}

/** Configuração do caderno de uma atividade de Questões. */
export function quizConfig(reduced = false) {
  return reduced
    ? { questions: TURBO.quizQuestions, limitSeconds: TURBO.quizLimitSeconds, mixed: false }
    : { questions: QUIZ.questions, limitSeconds: QUIZ.limitSeconds, mixed: false };
}

export interface TierShape {
  reviews: number; // nº de atividades de Revisão
  fixChunks: number; // nº de horas de Fixação
  quizzes: number; // nº de cadernos de Questões
}

/**
 * Forma do ciclo da PARTE NORMAL da aula (as unidades lidas no material), por camada. Sempre Teoria → Revisão → Fixação → Questões.
 *  1 Mínimo: Teoria + Revisões curtas (até 4 Teorias cada) + 1 hora de Fixação + cadernos (1 por até 4 Teorias).
 *  2 Completo: Revisões no agrupamento do nível (2 a 4), Fixação (hora de questões do material) e mais cadernos.
 *  3 Aprofundamento: amplia Fixação e cadernos.
 * Unidades em resumo (Turbo) não entram aqui: formam blocos com ciclo flexibilizado (ver `summaryShape`).
 */
export function tierShape(bp: AulaBlueprint, tier: Tier): TierShape {
  const t = bp.teoria.length;
  const full = bp.fixChunksFull;
  if (t === 0 && bp.summary.length > 0) return { reviews: 0, fixChunks: 0, quizzes: 0 }; // aula toda em resumo: o bloco cuida do ciclo
  const reviews = t === 0 ? 0 : tier === 1 ? Math.ceil(t / 4) : Math.ceil(t / bp.reviewGroup);
  let fix = 0;
  if (full > 0) {
    fix = tier === 1 ? 1 : tier === 2 ? clamp(Math.round(full * 0.35), 1, 4) : Math.min(full, 10);
    fix = Math.min(fix, full);
  }
  let quizzes = 0;
  if (t > 0) quizzes = tier === 1 ? Math.ceil(t / 4) : tier === 2 ? Math.max(1, Math.ceil(t / 3)) : Math.max(1, Math.ceil((2 * t) / 3));
  return { reviews, fixChunks: fix, quizzes };
}

/**
 * Estimativa (fracionária) do que as unidades em resumo desta aula acrescentam ao ciclo: o bloco real cruza aulas, então o custo
 * é rateado por unidade. Mínimo = resumos + caderno curto; camada 2 acrescenta Revisão (metade do tempo); camada 3, Fixação reduzida.
 */
export function summaryShape(bp: AulaBlueprint, tier: Tier): { reviews: number; fixChunks: number; quizzes: number } {
  const n = bp.summary.length;
  if (n === 0) return { reviews: 0, fixChunks: 0, quizzes: 0 };
  return {
    reviews: tier >= 2 ? n / (SUMMARY.maxUnitsPerActivity * SUMMARY.activitiesPerReview) : 0,
    fixChunks: tier >= 3 && bp.fixChunksFull > 0 ? Math.min(1, n / SUMMARY.unitsPerQuiz) : 0,
    quizzes: n / SUMMARY.unitsPerQuiz,
  };
}

export interface TierMinutes {
  teoria: number;
  revisao: number;
  fixacao: number;
  questoes: number;
  total: number;
}

export function tierMinutes(bp: AulaBlueprint, tier: Tier): TierMinutes {
  const s = tierShape(bp, tier);
  const m = summaryShape(bp, tier);
  const teoria = bp.teoria.reduce((n, u) => n + teoriaMinutes(u, bp), 0) + bp.summary.length * summaryMinutes(bp);
  const groups = splitEven(bp.teoria.length, s.reviews);
  const revisao = groups.reduce((n, g) => n + revisaoMinutes(g.length, bp), 0) + m.reviews * revisaoMinutes(SUMMARY.maxUnitsPerActivity * SUMMARY.activitiesPerReview, bp, true);
  const fixacao = s.fixChunks * fixacaoMinutes(bp) + m.fixChunks * fixacaoMinutes(bp, true);
  const questoes = s.quizzes * questoesMinutes(bp) + m.quizzes * questoesMinutes(bp, true);
  return { teoria, revisao, fixacao, questoes, total: teoria + revisao + fixacao + questoes };
}

/** Escolhe `count` blocos de Fixação espalhados ao longo das questões (cobre temas diferentes). */
export function pickFixChunks(bp: AulaBlueprint, count: number): FixRange[][] {
  const size = FIXACAO_PAGES_PER_HOUR;
  // lista "plana" de páginas, preservando a origem
  const pages: { page: number; src?: string }[] = [];
  for (const r of bp.fixRanges) for (let p = r.start; p <= r.end; p++) pages.push({ page: p, src: r.sourceAula });
  const chunks: FixRange[][] = [];
  for (let i = 0; i < pages.length; i += size) {
    const slice = pages.slice(i, i + size);
    const ranges: FixRange[] = [];
    for (const { page, src } of slice) {
      const last = ranges[ranges.length - 1];
      if (last && last.end === page - 1 && last.sourceAula === src) last.end = page;
      else ranges.push({ start: page, end: page, ...(src ? { sourceAula: src } : {}) });
    }
    chunks.push(ranges);
  }
  if (count >= chunks.length) return chunks;
  const picked: FixRange[][] = [];
  for (let i = 0; i < count; i++) {
    const idx = count === 1 ? 0 : Math.round((i * (chunks.length - 1)) / (count - 1));
    picked.push(chunks[idx]);
  }
  return picked;
}

/** Divide n itens em `groups` blocos contíguos o mais iguais possível. */
export function splitEven(n: number, groups: number): number[][] {
  const out: number[][] = [];
  let idx = 0;
  for (let g = 0; g < groups; g++) {
    const size = Math.floor(n / groups) + (g < n % groups ? 1 : 0);
    out.push(Array.from({ length: size }, (_, k) => idx + k));
    idx += size;
  }
  return out.filter((x) => x.length > 0);
}

function clamp(n: number, lo: number, hi: number): number {
  return Math.min(Math.max(n, lo), hi);
}

