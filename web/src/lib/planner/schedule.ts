import {
  fixacaoMinutes, pickFixChunks, questoesMinutes, quizConfig, revisaoMinutes, splitEven, summaryMinutes, teoriaMinutes, tierShape,
  type AulaBlueprint, type TeoriaUnit,
} from "./blueprint";
import { CYCLE_GAP_DAYS, SUMMARY } from "./constants";
import type { PlannedActivity, Tier } from "./types";

/** Pré-requisito de uma atividade: `key` precisa estar concluída há pelo menos `gap` dias. */
export interface Dep {
  key: string;
  gap: number;
}
/** Atividade do ciclo com seus pré-requisitos (uso interno do agendador; não vai para o plano final). */
export type CycleActivity = PlannedActivity & { after: Dep[]; cycle: string };

/**
 * Ciclo de uma aula na camada escolhida, sempre na ordem Teoria → Revisão → Fixação → Questões:
 * [T T T R] [T T T R] … F… Q… . Cada atividade carrega o que precisa estar feito antes (e a folga em dias):
 * a Revisão vem ≥ 1 dia depois das Teorias que revê; a Fixação, depois de toda a Teoria/Revisão da aula;
 * as Questões, ≥ 1 dia depois da Fixação (ou da última Revisão, quando a camada não tem Fixação).
 */
export function buildAulaCycle(bp: AulaBlueprint, tier: Tier): CycleActivity[] {
  const aulaId = bp.aula.id;
  const subjectId = aulaId.split("/")[0];
  const shape = tierShape(bp, tier);
  const dep = (key: string, gap = CYCLE_GAP_DAYS): Dep => ({ key, gap });

  const teorias: CycleActivity[] = bp.teoria.map((u, i) => ({
    key: `${aulaId}#T${i + 1}`,
    type: "TEORIA",
    subjectId,
    aulaId,
    minutes: teoriaMinutes(u, bp),
    segmentIds: u.segmentIds,
    refKeys: [],
    scope: "AULA",
    after: i > 0 ? [dep(`${aulaId}#T${i}`, 0)] : [],
    cycle: aulaId,
  }));

  const out: CycleActivity[] = [];
  const reviews: CycleActivity[] = [];
  // sem Revisão na camada: a teoria corre direto
  if (shape.reviews === 0) out.push(...teorias);
  splitEven(teorias.length, shape.reviews).forEach((group, gi) => {
    for (const i of group) out.push(teorias[i]);
    const r: CycleActivity = {
      key: `${aulaId}#R${gi + 1}`,
      type: "REVISAO",
      subjectId,
      aulaId,
      minutes: revisaoMinutes(group.length, bp),
      segmentIds: group.flatMap((i) => teorias[i].segmentIds),
      refKeys: group.map((i) => teorias[i].key),
      scope: "AULA",
      after: group.map((i) => dep(teorias[i].key)),
      cycle: aulaId,
    };
    reviews.push(r);
    out.push(r);
  });

  // a Fixação só começa depois de toda a Teoria/Revisão da aula
  const closing = (reviews.length ? reviews : teorias).map((a) => dep(a.key));
  const fixes: CycleActivity[] = pickFixChunks(bp, shape.fixChunks).map((ranges, i) => ({
    key: `${aulaId}#F${i + 1}`,
    type: "FIXACAO",
    subjectId,
    aulaId,
    minutes: fixacaoMinutes(bp),
    segmentIds: [],
    refKeys: [],
    fixRanges: ranges,
    scope: "AULA",
    after: [...closing, ...(i > 0 ? [dep(`${aulaId}#F${i}`, 0)] : [])],
    cycle: aulaId,
  }));
  out.push(...fixes);

  // os cadernos fecham o ciclo: depois da Fixação (ou da última Revisão/Teoria, quando não há)
  const beforeQuiz = (fixes.length ? fixes : reviews.length ? reviews : teorias).map((a) => dep(a.key));
  splitEven(teorias.length, shape.quizzes).forEach((group, i) => {
    out.push({
      key: `${aulaId}#Q${i + 1}`,
      type: "QUESTOES",
      subjectId,
      aulaId,
      minutes: questoesMinutes(bp),
      segmentIds: group.flatMap((j) => teorias[j].segmentIds),
      refKeys: group.map((j) => teorias[j].key),
      quiz: quizConfig(),
      scope: "AULA",
      after: [...beforeQuiz, ...(i > 0 ? [dep(`${aulaId}#Q${i}`, 0)] : [])],
      cycle: aulaId,
    });
  });
  return out;
}

/** Unidade em resumo que entra num bloco do Turbo (pode vir de aulas diferentes da mesma disciplina). */
export interface BlockUnit {
  aulaId: string;
  unit: TeoriaUnit;
  bp: AulaBlueprint;
  tier: Tier;
}

/**
 * Bloco do Modo Turbo: sequência contígua de unidades em resumo analítico da mesma disciplina (podendo cruzar aulas). Cada
 * atividade de resumo junta até 3 unidades (~20 min cada, ≤ 1 h). O ciclo é flexibilizado: o bloco acumula assuntos e só então
 * recebe a Revisão (metade do tempo, 1 por até 3 atividades de resumo), a Fixação reduzida (30 min, só na camada 3) e o caderno
 * curto de Questões (15 questões, 1 por até 6 unidades), sempre nessa ordem e com um dia de folga entre as etapas.
 */
export function buildSummaryBlock(units: BlockUnit[]): CycleActivity[] {
  if (units.length === 0) return [];
  const subjectId = units[0].aulaId.split("/")[0];
  const tier = Math.max(1, Math.min(...units.map((u) => u.tier))) as Tier;
  const tag = units[0].unit.segmentIds[0];
  const dep = (key: string, gap = CYCLE_GAP_DAYS): Dep => ({ key, gap });
  const out: CycleActivity[] = [];

  const summaries: CycleActivity[] = [];
  for (let i = 0; i < units.length; i += SUMMARY.maxUnitsPerActivity) {
    const group = units.slice(i, i + SUMMARY.maxUnitsPerActivity);
    const k = summaries.length + 1;
    const a: CycleActivity = {
      key: `${group[0].unit.segmentIds[0]}#S`,
      type: "TEORIA",
      subjectId,
      aulaId: group[0].aulaId,
      minutes: group.reduce((n, u) => n + summaryMinutes(u.bp), 0),
      segmentIds: group.flatMap((u) => u.unit.segmentIds),
      refKeys: [],
      scope: "AULA",
      turbo: true,
      after: k > 1 ? [dep(summaries[k - 2].key, 0)] : [],
      cycle: tag,
    };
    summaries.push(a);
    out.push(a);
  }

  const reviews: CycleActivity[] = [];
  if (tier >= 2) {
    for (let i = 0; i < summaries.length; i += SUMMARY.activitiesPerReview) {
      const g = summaries.slice(i, i + SUMMARY.activitiesPerReview);
      const r: CycleActivity = {
        key: `${g[0].segmentIds[0]}#SR`,
        type: "REVISAO",
        subjectId,
        aulaId: g[0].aulaId,
        minutes: revisaoMinutes(g.length, units[0].bp, true),
        segmentIds: g.flatMap((x) => x.segmentIds),
        refKeys: g.map((x) => x.key),
        scope: "AULA",
        after: g.map((x) => dep(x.key)),
        cycle: tag,
      };
      reviews.push(r);
      out.push(r);
    }
  }

  const fixes: CycleActivity[] = [];
  const withFix = [...units].sort((a, b) => b.bp.fixChunksFull - a.bp.fixChunksFull)[0];
  if (tier >= 3 && withFix.bp.fixChunksFull > 0) {
    const ranges = pickFixChunks(withFix.bp, 1)[0];
    if (ranges) {
      const f: CycleActivity = {
        key: `${tag}#SF`,
        type: "FIXACAO",
        subjectId,
        aulaId: withFix.aulaId,
        minutes: fixacaoMinutes(withFix.bp, true),
        segmentIds: [],
        refKeys: [],
        fixRanges: ranges,
        scope: "AULA",
        after: (reviews.length ? reviews : summaries).map((x) => dep(x.key)),
        cycle: tag,
      };
      fixes.push(f);
      out.push(f);
    }
  }

  const beforeQuiz = (fixes.length ? fixes : reviews.length ? reviews : summaries).map((x) => dep(x.key));
  const nQuiz = Math.max(1, Math.ceil(units.length / SUMMARY.unitsPerQuiz));
  splitEven(summaries.length, nQuiz).forEach((group, qi) => {
    const mine = group.map((j) => summaries[j]);
    out.push({
      key: `${tag}#SQ${qi + 1}`,
      type: "QUESTOES",
      subjectId,
      aulaId: mine[0].aulaId,
      minutes: questoesMinutes(units[0].bp, true),
      segmentIds: mine.flatMap((x) => x.segmentIds),
      refKeys: mine.map((x) => x.key),
      quiz: quizConfig(true),
      scope: "AULA",
      after: [...beforeQuiz, ...(qi > 0 ? [dep(`${tag}#SQ${qi}`, 0)] : [])],
      cycle: tag,
    });
  });
  return out;
}

/**
 * Fila de uma disciplina, na ordem do curso: ciclo normal de cada aula (unidades lidas no material) e blocos de resumo (Turbo).
 * As unidades em resumo de aulas seguidas formam um único bloco; uma aula com Teoria normal fecha o bloco anterior.
 */
export function buildSubjectQueue(items: { bp: AulaBlueprint; tier: Tier }[]): CycleActivity[] {
  const out: CycleActivity[] = [];
  let run: BlockUnit[] = [];
  const flush = () => {
    for (let i = 0; i < run.length; i += SUMMARY.maxUnitsPerBlock) out.push(...buildSummaryBlock(run.slice(i, i + SUMMARY.maxUnitsPerBlock)));
    run = [];
  };
  for (const { bp, tier } of items) {
    for (const unit of [...bp.summary].sort((a, b) => a.segmentIds[0].localeCompare(b.segmentIds[0]))) run.push({ aulaId: bp.aula.id, unit, bp, tier });
    if (bp.teoria.length > 0 || bp.summary.length === 0) {
      flush();
      out.push(...buildAulaCycle(bp, tier));
    }
  }
  flush();
  return out;
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
