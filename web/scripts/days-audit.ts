import { generatePlan } from "../src/lib/planner";
import { FAMILY } from "../src/lib/planner/constants";
import { loadCatalog, loadSegments } from "../src/lib/planner/fixtures";
const catalog = loadCatalog();
const hours = Number(process.argv[2] ?? 25);
const plan = generatePlan({ catalog, segments: loadSegments(), startDate: "2026-10-12", examDate: "2027-02-28", hoursPerWeek: hours, subjects: catalog.subjects.filter((s) => s.id !== "lingua-inglesa").map((s) => ({ id: s.id, level: 1 as const })) });
const perDay = [0, 0, 0, 0, 0, 0, 0], max = [0, 0, 0, 0, 0, 0, 0];
let sameDayRev = 0, adjFam = 0, subjMax = 0, n = 0;
for (const w of plan.weeks) {
  const dm = [0, 0, 0, 0, 0, 0, 0];
  for (const a of w.activities) dm[a.day!] += a.minutes;
  dm.forEach((m, d) => { perDay[d] += m; max[d] = Math.max(max[d], m); });
  n++;
  const dayOf = new Map(w.activities.map((a) => [a.key, a.day!]));
  for (const a of w.activities) for (const r of a.refKeys) if (dayOf.has(r) && dayOf.get(r) === a.day && a.type === "REVISAO") sameDayRev++;
  for (let d = 0; d < 7; d++) {
    const day = w.activities.filter((a) => a.day === d);
    subjMax = Math.max(subjMax, new Set(day.map((a) => a.subjectId)).size);
    for (let i = 1; i < day.length; i++) if (day[i].subjectId !== day[i - 1].subjectId && FAMILY[day[i].subjectId] === FAMILY[day[i - 1].subjectId]) adjFam++;
  }
}
console.log("min/dia (média):", perDay.map((m) => Math.round(m / n)).join(" "), "| máx:", max.join(" "));
console.log("revisão no mesmo dia da teoria:", sameDayRev, "| famílias coladas:", adjFam, "| máx disciplinas/dia:", subjMax);
