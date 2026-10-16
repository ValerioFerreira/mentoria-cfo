import { generatePlan } from "../web/src/lib/planner/index";
import {
  loadCatalog,
  loadSegments,
  loadImportance,
  loadExamQuestions,
} from "../web/src/lib/planner/fixtures";
import { CONTEST_SUBJECTS } from "../web/src/lib/contests";

const catalog = loadCatalog();
const segments = loadSegments();

const contest = "PCPE_AGENTE" as const;
const subs = CONTEST_SUBJECTS[contest];
const imp = loadImportance(contest);
const eq = loadExamQuestions(contest);

console.log(`\n================== ${contest} ==================`);
console.log(`Disciplinas (${subs.length}):`, subs.join(", "));

const hoursList = [15, 25, 40];
const profiles = [
  { name: "Iniciante (nível 1)", subjects: subs.map((id) => ({ id, level: 1 })) },
  { name: "Avançado (nível 3)", subjects: subs.map((id) => ({ id, level: 3 })) },
];
const turboOptions = [false, true];

for (const prof of profiles) {
  for (const turbo of turboOptions) {
    for (const h of hoursList) {
      const plan = generatePlan({
        catalog,
        segments,
        startDate: "2026-10-19",
        examDate: "2027-03-07",
        hoursPerWeek: h,
        subjects: prof.subjects,
        importance: imp,
        examQuestions: eq,
        turbo,
      });

      const acts = plan.weeks.flatMap((w) => w.activities);
      const byType: Record<string, number> = {};
      for (const a of acts) byType[a.type] = (byType[a.type] || 0) + 1;

      console.log(
        `[${prof.name} | Turbo: ${turbo ? "SIM" : "NÃO"}] ` +
        `Carga ${h}h/sem: ${plan.weeks.length} sem | ` +
        `Ativ: ${acts.length} (${JSON.stringify(byType)}) | ` +
        `Cobertura: ${(plan.coverage.selected * 100).toFixed(1)}% | ` +
        `Avisos: ${plan.warnings.length}`
      );
    }
  }
}
