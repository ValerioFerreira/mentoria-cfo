// Seleção de conteúdo: decide quais aulas entram no plano e em qual camada (tier), dado o tempo disponível (em minutos).
import { buildBlueprint, tierMinutes, type AulaBlueprint } from "./blueprint";
import type { CatalogSubject, Known, Level, SegmentsByAula, Tier } from "./types";

/** Retornos decrescentes por disciplina: V(c) côncavo, com V(0)=0 e V(1)=1. */
export const CONCAVITY = 2;
export function valueCurve(c: number): number {
  const x = Math.min(Math.max(c, 0), 1);
  return (1 - Math.exp(-CONCAVITY * x)) / (1 - Math.exp(-CONCAVITY));
}
/** Quanto mais fraco o aluno, maior o valor de estudar o assunto. */
export const LEVEL_MULT: Record<Level, number> = { 0: 1.4, 1: 1.2, 2: 1.0, 3: 0.7 };
/** Fração acumulada do valor de uma aula ao concluir cada camada (ver a primeira vez já vale a maior parte). */
export const CUM_GAIN: Record<Tier, number> = { 1: 0.7, 2: 0.9, 3: 1 };
const FLOOR_START = 0.25; // cobertura mínima almejada por disciplina
const FLOOR_BUDGET = 0.5; // pisos podem usar até 50% da capacidade

export interface SelectedSubject {
  subject: CatalogSubject;
  level: Level;
}

export interface Selection {
  tierByAula: Map<string, Tier>;
  blueprints: Map<string, AulaBlueprint>;
  /** Aulas que o aluno disse dominar na anamnese: contam como cobertas e não geram atividades. */
  mastered: Set<string>;
  usedMinutes: number;
  /** Minutos para cobrir todas as aulas no nível Essencial (tudo do edital). */
  fullMinutes: number;
  floorFraction: number;
  floorShortfall: boolean;
}

interface Item {
  aulaId: string;
  subjectId: string;
  examQuestions: number;
  number: number;
  /** Incidência da aula normalizada pelo total da disciplina (soma ≈ 1). */
  share: number;
}

/** Ganho esperado (em questões) de subir a aula da camada `tier-1` para `tier`, dado o que a disciplina já cobre. */
export function itemGain(examQuestions: number, share: number, tier: Tier, level: Level, covered: number): number {
  const delta = share * (CUM_GAIN[tier] - (tier > 1 ? CUM_GAIN[(tier - 1) as Tier] : 0));
  return examQuestions * (valueCurve(covered + delta) - valueCurve(covered)) * LEVEL_MULT[level];
}

export function selectContent(
  chosen: SelectedSubject[],
  segments: SegmentsByAula,
  capacityMinutes: number,
  known: Record<string, Known> = {},
): Selection {
  const blueprints = new Map<string, AulaBlueprint>();
  const items: Item[] = [];
  const levelOf = new Map<string, Level>();
  const examQ = new Map<string, number>();
  const covered = new Map<string, number>(); // cobertura (0–1) já alcançada por disciplina
  const mastered = new Set<string>();
  let fullMinutes = 0;
  for (const { subject, level } of chosen) {
    levelOf.set(subject.id, level);
    examQ.set(subject.id, subject.examQuestions);
    covered.set(subject.id, 0);
    const totalInc = subject.aulas.filter((a) => a.selectable).reduce((n, a) => n + a.incidence, 0) || 1;
    for (const aula of subject.aulas) {
      if (!aula.selectable) continue;
      const share = aula.incidence / totalInc;
      const k = known[aula.id] ?? 0;
      if (k === 2) {
        mastered.add(aula.id);
        covered.set(subject.id, covered.get(subject.id)! + share * CUM_GAIN[1]);
        continue;
      }
      const bp = buildBlueprint(aula, segments[aula.id] ?? [], level, k);
      if (bp.teoria.length === 0 && bp.fixChunksFull === 0) continue; // nada para fazer
      blueprints.set(aula.id, bp);
      fullMinutes += tierMinutes(bp, 1).total;
      items.push({ aulaId: aula.id, subjectId: subject.id, examQuestions: subject.examQuestions, number: aula.number, share });
    }
  }

  const tierByAula = new Map<string, Tier>();
  let used = 0;

  const incMinutes = (it: Item, tier: Tier) => {
    const bp = blueprints.get(it.aulaId)!;
    return tierMinutes(bp, tier).total - (tier > 1 ? tierMinutes(bp, (tier - 1) as Tier).total : 0);
  };
  const gainOf = (it: Item, tier: Tier) =>
    itemGain(it.examQuestions, it.share, tier, levelOf.get(it.subjectId)!, covered.get(it.subjectId)!);
  const density = (it: Item, tier: Tier) => {
    const m = incMinutes(it, tier);
    return m <= 0 ? Number.POSITIVE_INFINITY : gainOf(it, tier) / m;
  };
  const apply = (it: Item, tier: Tier) => {
    const prev = (tierByAula.get(it.aulaId) ?? 0) as 0 | Tier;
    used += incMinutes(it, tier);
    tierByAula.set(it.aulaId, tier);
    // camadas sem custo extra são promovidas automaticamente
    while (tier < 3 && incMinutes(it, (tier + 1) as Tier) <= 0) {
      tier = (tier + 1) as Tier;
      tierByAula.set(it.aulaId, tier);
    }
    const before = prev === 0 ? 0 : CUM_GAIN[prev];
    covered.set(it.subjectId, covered.get(it.subjectId)! + it.share * (CUM_GAIN[tier] - before));
  };

  // 1) Pisos por disciplina: aulas de maior densidade até cobrir `f` do assunto (reduz f se não couber)
  const bySubject = new Map<string, Item[]>();
  for (const it of items) bySubject.set(it.subjectId, [...(bySubject.get(it.subjectId) ?? []), it]);
  for (const list of bySubject.values()) list.sort((a, b) => density(b, 1) - density(a, 1) || a.number - b.number);

  const floorPick = (f: number): Item[] => {
    const picked: Item[] = [];
    for (const list of bySubject.values()) {
      let acc = covered.get(list[0].subjectId)!; // o que o aluno já domina conta para o piso
      for (const it of list) {
        if (acc >= f) break;
        picked.push(it);
        acc += it.share * CUM_GAIN[1];
      }
    }
    return picked;
  };
  const minutesOf = (arr: Item[]) => arr.reduce((n, it) => n + incMinutes(it, 1), 0);

  let f = FLOOR_START;
  let picked = floorPick(f);
  while (f > 0 && minutesOf(picked) > capacityMinutes * FLOOR_BUDGET) {
    f = Math.max(0, +(f - 0.05).toFixed(2));
    picked = floorPick(f);
  }
  let floorShortfall = false;
  if (minutesOf(picked) > capacityMinutes) {
    // nem uma aula por disciplina cabe: mantém as disciplinas de maior peso que couberem
    floorShortfall = true;
    const firstPerSubject = [...bySubject.values()].map((l) => l[0]).sort((a, b) => b.examQuestions - a.examQuestions);
    picked = [];
    let m = 0;
    for (const it of firstPerSubject) {
      const c = incMinutes(it, 1);
      if (m + c > capacityMinutes) continue;
      picked.push(it);
      m += c;
    }
  }
  for (const it of picked) apply(it, 1);

  // 2) Amplitude primeiro: enquanto houver aula do edital ainda não vista, ela entra (Essencial) antes de qualquer aprofundamento.
  //    Depois, o que sobrar de tempo vira profundidade (Completo → Aprofundamento), sempre pelo maior ganho por minuto.
  for (const breadthOnly of [true, false]) {
    for (;;) {
      let best: { it: Item; tier: Tier; d: number } | null = null;
      for (const it of items) {
        const cur = tierByAula.get(it.aulaId) ?? 0;
        if (cur >= 3 || (breadthOnly && cur >= 1)) continue;
        const tier = (cur + 1) as Tier;
        if (used + incMinutes(it, tier) > capacityMinutes + 1e-9) continue;
        const d = density(it, tier);
        if (!best || d > best.d || (d === best.d && it.number < best.it.number)) best = { it, tier, d };
      }
      if (!best) break;
      apply(best.it, best.tier);
    }
  }

  return { tierByAula, blueprints, mastered, usedMinutes: used, fullMinutes, floorFraction: f, floorShortfall };
}
