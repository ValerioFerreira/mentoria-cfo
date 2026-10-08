// Uso: npx tsx scripts/plan-demo.ts [horasPorSemana=21] [nivel=1] [weeksToShow=3] [subjectIds,...]
import { generatePlan } from "../src/lib/planner";
import { DAY_NAMES } from "../src/lib/planner/constants";
import { loadCatalog, loadSegments } from "../src/lib/planner/fixtures";

const hours = Number(process.argv[2] ?? 21);
const level = Number(process.argv[3] ?? 1) as 0 | 1 | 2 | 3;
const show = Number(process.argv[4] ?? 3);
const catalog = loadCatalog();
const ids = process.argv[5]?.split(",") ?? catalog.subjects.filter((s) => s.id !== "lingua-inglesa").map((s) => s.id);
const plan = generatePlan({
  catalog,
  segments: loadSegments(),
  startDate: "2026-10-12",
  examDate: "2027-02-28",
  hoursPerWeek: hours,
  subjects: ids.map((id) => ({ id, level })),
});
console.log(JSON.stringify(plan.params));
console.log(`cobertura: escolhidas ${(plan.coverage.selected * 100).toFixed(0)}% | edital ${(plan.coverage.edital * 100).toFixed(0)}% | profundidade ${(plan.coverage.depth * 100).toFixed(0)}%`);
for (const s of plan.coverage.subjects) {
  const m = s.minutes;
  console.log(
    `  ${s.subjectId.padEnd(24)} ${String(s.plannedHours).padStart(5)}h (T ${Math.round(m.teoria / 60)} R ${Math.round(m.revisao / 60)} F ${Math.round(m.fixacao / 60)} Q ${Math.round(m.questoes / 60)}) aulas ${String(s.aulas.length).padStart(2)}/${catalog.subjects.find((x) => x.id === s.subjectId)!.aulas.filter((a) => a.selectable).length}  págs ${String(s.theoryPagesCovered).padStart(4)}/${s.theoryPagesEligible}  cobertura ${(s.coverage * 100).toFixed(0)}%  profundidade ${(s.depth * 100).toFixed(0)}%  essencial-tudo ${Math.round(s.fullMinutes / 60)}h`,
  );
}
for (const w of plan.weeks.slice(0, show)) {
  console.log(`\nSemana ${w.index} (${w.startDate}) ${w.kind} — ${(w.targetMinutes / 60).toFixed(1)} h`);
  for (let d = 0; d < 7; d++) {
    const acts = w.activities.filter((a) => a.day === d);
    const mins = acts.reduce((n, a) => n + a.minutes, 0);
    console.log(`  ${DAY_NAMES[d].slice(0, 3)} ${String(mins).padStart(3)}min: ` + acts.map((a) => `${a.type[0]}${a.minutes}:${a.subjectId.slice(0, 5)}${a.aulaId.split("/")[1]}`).join("  "));
  }
}
console.log("\nAvisos:\n- " + plan.warnings.join("\n- "));
