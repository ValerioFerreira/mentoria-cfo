// Demonstração do combo: cobertura de cada prova nas duas prioridades, com 15, 25 e 40 h. Também confere cada plano com verifyPlan.
// Uso: npx tsx scripts/combo-demo.ts   (lê o conteúdo de /content; não usa banco)
import { COMBOS, comboWeights, mergeComboImportance, mergeComboQuestions, type ComboKey, type ComboMemberData } from "../src/lib/combos";
import { CONTEST_SUBJECTS } from "../src/lib/contests";
import { generatePlan } from "../src/lib/planner";
import { loadCatalog, loadExamQuestions, loadImportance, loadSegments } from "../src/lib/planner/fixtures";
import { planFromResult, verifyPlan } from "../src/lib/planner/verify";
import fs from "node:fs";
import path from "node:path";

const catalog = loadCatalog();
const segments = loadSegments();
const doc = JSON.parse(fs.readFileSync(path.resolve(__dirname, "../../content/importance/segments.json"), "utf-8")) as {
  segments: Record<string, { contests: Record<string, { appears: boolean; expected: number }> }>;
};
const contests = JSON.parse(fs.readFileSync(path.resolve(__dirname, "../../content/contests.json"), "utf-8")) as Record<string, { totalQuestions: number }>;
const summaries = Object.values(segments).flat().map((s) => s.id);

export function comboInput(combo: ComboKey, priority: string, hours: number, level: 0 | 2, turbo: boolean) {
  const members: ComboMemberData[] = comboWeights(combo, priority).map(({ contest, weight }) => ({
    contest,
    weight,
    importance: loadImportance(contest),
    expected: Object.fromEntries(Object.entries(doc.segments).map(([id, r]) => [id, r.contests[contest]?.expected ?? 0])),
    examQuestions: loadExamQuestions(contest),
  }));
  const subjects = CONTEST_SUBJECTS[combo].filter((id) => id !== "lingua-espanhola");
  const input = {
    catalog, segments, startDate: "2026-10-26", examDate: combo === "CBMPE_COMBO" ? "2027-02-28" : "2027-02-21", hoursPerWeek: hours,
    subjects: subjects.map((id) => ({ id, level })), turbo, summaries: turbo ? summaries : undefined, contest: combo,
    importance: mergeComboImportance(members), examQuestions: mergeComboQuestions(members),
    combo: { priority, members: members.map((m) => ({ contest: m.contest, weight: m.weight, totalQuestions: contests[m.contest].totalQuestions, examQuestions: m.examQuestions })) },
  };
  return { input, importance: input.importance };
}

if (require.main === module) {
  for (const combo of Object.keys(COMBOS) as ComboKey[]) {
    for (const hours of [15, 25, 40]) {
      for (const priority of Object.values(COMBOS[combo])) {
        const { input, importance } = comboInput(combo, priority, hours, 0, false);
        const plan = generatePlan(input);
        const rep = verifyPlan(planFromResult(plan, input.startDate, input.examDate), { catalog, segments, importance });
        const cov = (plan.coverage.contests ?? []).map((c) => `${c.contest.replace(/^[A-Z]+_/, "")} ${(c.selected * 100).toFixed(0)}%`).join(" · ");
        console.log(`${combo} ${String(hours).padStart(2)}h prioridade=${priority.padEnd(14)} ${cov}  [${rep.verdict}${rep.errors.length ? " " + rep.errors.map((e) => e.code).join(",") : ""}]`);
      }
    }
  }
}
