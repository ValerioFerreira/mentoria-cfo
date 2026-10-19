import { generatePlan } from "../web/src/lib/planner/index";
import {
  loadCatalog,
  loadSegments,
  loadImportance,
  loadExamQuestions,
} from "../web/src/lib/planner/fixtures";
import { CONTEST_SUBJECTS } from "../web/src/lib/contests";
import { planFromResult, verifyPlan, type VerifyContext } from "../web/src/lib/planner/verify";
import type { Level } from "../web/src/lib/planner/types";

const catalog = loadCatalog();
const segments = loadSegments();

const contest = "PCPE_AGENTE" as const;
const subs = CONTEST_SUBJECTS[contest];
const imp = loadImportance(contest);
const eq = loadExamQuestions(contest);
const allSummaries = Object.values(segments).flat().map((x) => x.id);
const ctx: VerifyContext = {
  catalog,
  segments,
  importance: imp,
  summaries: new Set(allSummaries),
};

console.log(`\n================== SIMULAÇÃO E VERIFICAÇÃO DE PLANOS: ${contest} ==================`);
console.log(`Disciplinas (${subs.length}):`, subs.join(", "));

const hoursList = [15, 25, 40];
const profiles: { name: string; level: Level }[] = [
  { name: "Iniciante (nível 0)", level: 0 },
  { name: "Básico (nível 1)", level: 1 },
  { name: "Intermediário (nível 2)", level: 2 },
  { name: "Domina (nível 3)", level: 3 },
];
const turboOptions = [false, true];

interface ResultRow {
  Perfil: string;
  Turbo: string;
  Carga: string;
  Semanas: number;
  Teoria: number;
  Fixacao: number;
  Revisao: number;
  Questoes: number;
  Simulado: number;
  Total: number;
  Cobertura: string;
  Erros: number;
  Verdict: string;
}

const tableData: ResultRow[] = [];
let totalErrors = 0;

for (const prof of profiles) {
  for (const turbo of turboOptions) {
    for (const h of hoursList) {
      const plan = generatePlan({
        catalog,
        segments,
        startDate: "2026-10-19",
        examDate: "2027-03-07",
        hoursPerWeek: h,
        subjects: subs.map((id) => ({ id, level: prof.level })),
        importance: imp,
        examQuestions: eq,
        turbo,
        contest,
        summaries: allSummaries,
      });

      const acts = plan.weeks.flatMap((w) => w.activities);
      const byType: Record<string, number> = {};
      for (const a of acts) byType[a.type] = (byType[a.type] || 0) + 1;

      const pForVerify = planFromResult(plan, "2026-10-19", "2027-03-07");
      const report = verifyPlan(pForVerify, ctx);
      totalErrors += report.errors.length;

      if (report.errors.length > 0) {
        console.error(
          `ERRO no cenário [${prof.name} | Turbo: ${turbo} | ${h}h]:`,
          report.errors
        );
      }

      tableData.push({
        Perfil: prof.name,
        Turbo: turbo ? "SIM" : "NÃO",
        Carga: `${h}h/sem`,
        Semanas: plan.weeks.length,
        Teoria: byType["TEORIA"] || 0,
        Fixacao: byType["FIXACAO"] || 0,
        Revisao: byType["REVISAO"] || 0,
        Questoes: byType["QUESTOES"] || 0,
        Simulado: byType["SIMULADO"] || 0,
        Total: acts.length,
        Cobertura: `${(plan.coverage.selected * 100).toFixed(1)}%`,
        Erros: report.errors.length,
        Verdict: report.verdict,
      });
    }
  }
}

console.log("\n");
console.table(tableData);
console.log(`\nTotal de cenários testados: ${tableData.length}`);
console.log(`Total de erros de verificação independente: ${totalErrors}`);

if (totalErrors > 0) {
  process.exit(1);
} else {
  console.log("TODOS OS PLANOS PASSARAM COM VEREDICTO 'LIBERAR' E 0 ERROS!\n");
}
