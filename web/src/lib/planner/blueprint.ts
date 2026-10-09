// Blueprint do ciclo de uma aula: Teoria → Revisão → Fixação → Questões, por camada (tier), com o tempo de cada atividade.
import {
  FIXACAO_MINUTES, FIXACAO_PAGES_PER_HOUR, KNOWN_PACE, LEVEL_PACE, MIN_ACTIVITY_MINUTES, QUESTOES_MINUTES, QUIZ,
  REVISAO_MINUTES, SEGMENT, TEORIA_MINUTES,
} from "./constants";
import type { CatalogAula, FixRange, Known, Level, SegmentLite, Tier } from "./types";

export interface TeoriaUnit {
  segmentIds: string[];
  pages: number;
  load: number;
}

export interface AulaBlueprint {
  aula: CatalogAula;
  teoria: TeoriaUnit[];
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
    reviewGroup: reviewGroupFor(level),
    fixRanges,
    fixPages,
    fixChunksFull: Math.ceil(fixPages / FIXACAO_PAGES_PER_HOUR),
    pace,
    readPace: known === 1 ? pace * KNOWN_PACE[1] : pace,
  };
}

// ───────────────────────── Tempo de cada atividade ─────────────────────────
/** Arredonda para múltiplos de 5 min, com piso. */
export function roundMinutes(m: number): number {
  return Math.max(MIN_ACTIVITY_MINUTES, Math.round(m / 5) * 5);
}

/** Teoria: ~1 h para cada 12 de carga (10–17 págs., conforme a densidade), ajustada pelo ritmo do aluno. */
export function teoriaMinutes(u: TeoriaUnit, bp: AulaBlueprint): number {
  const base = Math.min(Math.max(u.load * TEORIA_MINUTES.perLoadUnit, TEORIA_MINUTES.min), TEORIA_MINUTES.max);
  return roundMinutes(base * bp.readPace);
}

/** Revisão de `n` Teorias. */
export function revisaoMinutes(n: number, bp: AulaBlueprint): number {
  const base = Math.min(Math.max(REVISAO_MINUTES.base + REVISAO_MINUTES.perTeoria * n, REVISAO_MINUTES.min), REVISAO_MINUTES.max);
  return roundMinutes(base * bp.readPace);
}

export function fixacaoMinutes(bp: AulaBlueprint): number {
  return roundMinutes(FIXACAO_MINUTES * bp.pace);
}

/** O caderno tem 60 min de limite; quem domina o assunto termina antes, mas ainda corrige os erros (piso de 45 min). */
export function questoesMinutes(bp: AulaBlueprint): number {
  return roundMinutes(QUESTOES_MINUTES * Math.max(bp.pace, 0.75));
}

export interface TierShape {
  reviews: number; // nº de atividades de Revisão
  fixChunks: number; // nº de horas de Fixação
  quizzes: number; // nº de cadernos de Questões
}

/**
 * Forma do ciclo por camada. Essencial = só o necessário para VER o edital inteiro: toda a teoria + cadernos enxutos
 * (sem Revisão nem Fixação, que são opcionais para responder "consegui estudar todo o edital?"). Completo acrescenta as
 * Revisões espaçadas e a Fixação; Aprofundamento amplia a prática.
 */
export function tierShape(bp: AulaBlueprint, tier: Tier): TierShape {
  const t = bp.teoria.length;
  // Essencial: sem Revisão (entra no Completo); Completo/Aprofundamento: o agrupamento do nível do aluno (2 a 4)
  const reviews = t === 0 || tier === 1 ? 0 : Math.ceil(t / bp.reviewGroup);
  const full = bp.fixChunksFull;
  let fix = 0;
  if (full > 0) {
    fix = tier === 1 ? 0 : tier === 2 ? clamp(Math.round(full * 0.35), 1, 4) : Math.min(full, 10);
    fix = Math.min(fix, full);
  }
  let quizzes = 0;
  if (t > 0) {
    quizzes = tier === 1 ? (t >= 6 ? Math.ceil(t / 8) : 0) : tier === 2 ? Math.max(1, Math.ceil(t / 3)) : Math.max(1, Math.ceil((2 * t) / 3));
  }
  return { reviews, fixChunks: fix, quizzes };
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
  const teoria = bp.teoria.reduce((n, u) => n + teoriaMinutes(u, bp), 0);
  const groups = splitEven(bp.teoria.length, s.reviews);
  const revisao = groups.reduce((n, g) => n + revisaoMinutes(g.length, bp), 0);
  const fixacao = s.fixChunks * fixacaoMinutes(bp);
  const questoes = s.quizzes * questoesMinutes(bp);
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

export const QUIZ_DEFAULT = { questions: QUIZ.questions, limitSeconds: QUIZ.limitSeconds, mixed: false };
