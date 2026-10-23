// Rede de segurança do motor: grava um hash/JSON de generatePlan para os concursos individuais.
// Uso: npx tsx scripts/plan-snapshot.ts <arquivo-saida.json>   (rodar antes e depois de mexer no planejador; as saídas devem ser idênticas)
import fs from "node:fs";
import crypto from "node:crypto";
import { CONTEST_SUBJECTS } from "../src/lib/contests";
import { generatePlan } from "../src/lib/planner";
import { loadCatalog, loadExamQuestions, loadImportance, loadSegments } from "../src/lib/planner/fixtures";

const out = process.argv[2];
if (!out) throw new Error("informe o arquivo de saída");
const catalog = loadCatalog();
const segments = loadSegments();
const contests = ["CBMPE_OFICIAL", "CBMPE_SOLDADO", "PMPE_OFICIAL", "PMPE_SOLDADO", "PCPE_AGENTE"] as const;
const summaries = Object.keys(segments).flatMap((a) => segments[a].map((s) => s.id));
const res: Record<string, string> = {};
for (const contest of contests) {
  const subjects = CONTEST_SUBJECTS[contest].filter((id) => id !== "lingua-espanhola");
  const importance = loadImportance(contest);
  const examQuestions = loadExamQuestions(contest);
  for (const hours of [15, 25, 40]) for (const level of [0, 2] as const) for (const turbo of [false, true]) {
    const plan = generatePlan({
      catalog, segments, startDate: "2026-10-26", examDate: "2027-02-28", hoursPerWeek: hours,
      subjects: subjects.map((id) => ({ id, level })), importance, examQuestions, contest, turbo, summaries: turbo ? summaries : undefined,
    });
    res[`${contest}|${hours}|${level}|${turbo}`] = crypto.createHash("sha1").update(JSON.stringify(plan)).digest("hex");
  }
}
fs.writeFileSync(out, JSON.stringify(res, null, 1));
console.log(`${Object.keys(res).length} cenários -> ${out}`);
