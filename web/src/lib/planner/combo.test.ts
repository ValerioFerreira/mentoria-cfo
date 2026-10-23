import { describe, expect, it } from "vitest";
import { comboInput } from "../../../scripts/combo-demo";
import { COMBOS, type ComboKey } from "../combos";
import { generatePlan } from "./index";
import { loadCatalog, loadImportance, loadSegments } from "./fixtures";
import { planFromResult, verifyPlan } from "./verify";

const catalog = loadCatalog();
const segments = loadSegments();
type Plan = ReturnType<typeof generatePlan>;
const cov = (p: Plan, contest: string) => p.coverage.contests!.find((c) => c.contest === contest)!;
const minutesBy = (p: Plan, subject: string) => p.weeks.flatMap((w) => w.activities).filter((a) => a.subjectId === subject).reduce((n, a) => n + a.minutes, 0);

describe("planos combo", () => {
  for (const combo of Object.keys(COMBOS) as ComboKey[]) {
    const { oficial, praca } = COMBOS[combo];

    it(`${combo}: a prioridade desloca a cobertura para o concurso escolhido`, () => {
      const a = generatePlan(comboInput(combo, oficial, 15, 0, false).input);
      const b = generatePlan(comboInput(combo, praca, 15, 0, false).input);
      expect(cov(a, oficial).selected).toBeGreaterThan(cov(b, oficial).selected);
      expect(cov(b, praca).selected).toBeGreaterThan(cov(a, praca).selected);
    });

    it(`${combo}: o concurso secundário não perde suas disciplinas exclusivas, mesmo com pouco tempo`, () => {
      for (const priority of [oficial, praca]) {
        const p = generatePlan(comboInput(combo, priority, 15, 0, false).input);
        const other = priority === oficial ? praca : oficial;
        for (const s of cov(p, other).subjects) expect(s.coverage, `${s.subjectId} (${other})`).toBeGreaterThan(0);
      }
    });

    it(`${combo}: passa na verificação de planos (15/25/40 h, com e sem Turbo)`, () => {
      for (const hours of [15, 25, 40]) {
        for (const turbo of [false, true]) {
          for (const priority of [oficial, praca]) {
            const { input, importance } = comboInput(combo, priority, hours, 0, turbo);
            const plan = generatePlan(input);
            const rep = verifyPlan({ ...planFromResult(plan, input.startDate, input.examDate), contest: combo }, { catalog, segments, importance });
            expect(rep.errors, `${combo} ${hours}h turbo=${turbo} prio=${priority}`).toEqual([]);
            expect(plan.params.request.combo).toEqual({ contests: [oficial, praca], priority });
          }
        }
      }
    });

    it(`${combo}: cada aula aparece uma vez só e a Teoria segue a ordem do curso`, () => {
      const p = generatePlan(comboInput(combo, oficial, 40, 0, false).input);
      const teorias = p.weeks.flatMap((w) => w.activities).filter((a) => a.type === "TEORIA");
      const keys = teorias.map((a) => a.key);
      expect(new Set(keys).size).toBe(keys.length);
      for (const subject of new Set(teorias.map((a) => a.subjectId))) {
        const numberOf = new Map(catalog.subjects.flatMap((s) => s.aulas.map((a) => [a.id, a.number] as const)));
        const nums = teorias.filter((a) => a.subjectId === subject).map((a) => numberOf.get(a.aulaId)!);
        expect(nums, subject).toEqual([...nums].sort((x, y) => x - y));
      }
    });

    it(`${combo}: invariante dos dados — uma disciplina comum tem o mesmo edital nos dois concursos`, () => {
      // a seleção pelo peso combinado (W) só é equivalente a somar o ganho de cada prova se o "aparece" for decidido por disciplina
      const a = loadImportance(oficial);
      const b = loadImportance(praca);
      const subjectsOf = (imp: Record<string, number | null>) => {
        const m = new Map<string, Set<string>>();
        for (const [id, v] of Object.entries(imp)) if (v !== null) m.set(id.split("/")[0], (m.get(id.split("/")[0]) ?? new Set()).add(id));
        return m;
      };
      const sa = subjectsOf(a);
      const sb = subjectsOf(b);
      for (const [subject, ids] of sa) if (sb.has(subject)) expect(sb.get(subject), subject).toEqual(ids);
    });
  }

  it("prioridade no Soldado dá à Informática (10 no Soldado, 5 no Oficial) ao menos o mesmo tempo", () => {
    const oficial = generatePlan(comboInput("CBMPE_COMBO", "CBMPE_OFICIAL", 15, 0, false).input);
    const praca = generatePlan(comboInput("CBMPE_COMBO", "CBMPE_SOLDADO", 15, 0, false).input);
    expect(minutesBy(praca, "informatica")).toBeGreaterThanOrEqual(minutesBy(oficial, "informatica"));
  });

  it("combo com prioridade inválida é recusado", () => {
    const { input } = comboInput("CBMPE_COMBO", "CBMPE_OFICIAL", 25, 0, false);
    expect(() => generatePlan({ ...input, combo: { ...input.combo, priority: "PMPE_OFICIAL" } })).toThrow(/prioridade/i);
  });
});
