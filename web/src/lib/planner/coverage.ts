// Relatório de cobertura do plano (transparência: o que entra, o que fica de fora).
import { tierMinutes } from "./blueprint";
import { EXAM_TOTAL_QUESTIONS } from "./constants";
import type { Selection, SelectedSubject } from "./select";
import type { Catalog, Known, SubjectCoverage } from "./types";

const round1 = (n: number) => Math.round(n * 10) / 10;
/** Aula que o aluno disse dominar: conta como prática já bem consolidada (sem exigir atividades novas). */
const DEPTH_MASTERED = 0.6;

/**
 * Cobertura = fatia do edital que o aluno VÊ (aula estudada no plano, ou já dominada na anamnese), ponderada pela
 * incidência em prova e descontada a parte que o material não traz. Profundidade = fração da prática completa (fixação e
 * cadernos do nível Aprofundamento) que foi planejada nessas aulas — é outra dimensão e não entra na cobertura.
 */
export function computeCoverage(chosen: SelectedSubject[], sel: Selection, known: Record<string, Known> = {}) {
  const subjects: SubjectCoverage[] = chosen.map(({ subject, level }) => {
    const selectable = subject.aulas.filter((a) => a.selectable);
    const totalInc = selectable.reduce((n, a) => n + a.incidence, 0) || 1;
    let seenInc = 0;
    let depthInc = 0;
    let pages = 0;
    const mins = { teoria: 0, revisao: 0, fixacao: 0, questoes: 0 };
    const aulas: SubjectCoverage["aulas"] = [];
    for (const a of selectable) {
      if (sel.mastered.has(a.id) || known[a.id] === 2) {
        seenInc += a.incidence;
        depthInc += a.incidence * DEPTH_MASTERED;
        continue;
      }
      if (!sel.blueprints.has(a.id)) {
        seenInc += a.incidence; // aula sem nada a estudar (já está contida em outras): não pesa contra a cobertura
        continue;
      }
      const tier = sel.tierByAula.get(a.id);
      if (!tier) continue;
      const bp = sel.blueprints.get(a.id)!;
      const m = tierMinutes(bp, tier);
      seenInc += a.incidence;
      const full = tierMinutes(bp, 3);
      const fullPractice = full.fixacao + full.questoes;
      depthInc += a.incidence * (fullPractice > 0 ? (m.fixacao + m.questoes) / fullPractice : 1);
      pages += a.theoryPages;
      mins.teoria += m.teoria;
      mins.revisao += m.revisao;
      mins.fixacao += m.fixacao;
      mins.questoes += m.questoes;
      aulas.push({ aulaId: a.id, tier, hours: round1(m.total / 60) });
    }
    const notCovered = selectable
      .filter((a) => sel.blueprints.has(a.id) && !sel.tierByAula.has(a.id) && !sel.mastered.has(a.id))
      .sort((a, b) => b.incidence - a.incidence)
      .slice(0, 6)
      .map((a) => ({ aulaId: a.id, shortTitle: a.shortTitle, incidence: a.incidence }));
    const total = mins.teoria + mins.revisao + mins.fixacao + mins.questoes;
    const full = selectable.reduce((n, a) => {
      const bp = sel.blueprints.get(a.id);
      return bp ? n + tierMinutes(bp, 1).total : n;
    }, 0);
    return {
      subjectId: subject.id,
      level,
      examQuestions: subject.examQuestions,
      plannedHours: round1(total / 60),
      minutes: mins,
      fullMinutes: full,
      aulas,
      theoryPagesCovered: pages,
      theoryPagesEligible: selectable.reduce((n, a) => n + a.theoryPages, 0),
      coverage: Math.min(1, seenInc / totalInc) * (subject.materialCompleteness ?? 1),
      depth: Math.min(1, depthInc / totalInc),
      materialCompleteness: subject.materialCompleteness ?? 1,
      notCovered,
    };
  });
  const pts = chosen.reduce((n, c) => n + c.subject.examQuestions, 0) || 1;
  const covPts = subjects.reduce((n, s) => n + s.examQuestions * s.coverage, 0);
  const depthPts = subjects.reduce((n, s) => n + s.examQuestions * s.depth, 0);
  return { selected: covPts / pts, edital: covPts / EXAM_TOTAL_QUESTIONS, depth: depthPts / pts, subjects };
}

export function gapWarnings(catalog: Catalog, subjectIds: string[]): string[] {
  return catalog.gaps
    .filter((g) => subjectIds.includes(g.subject) && g.severity !== "low")
    .map((g) => `Lacuna no material (${g.severity === "high" ? "alta" : "média"}): ${g.item}. ${g.remedy}`);
}
