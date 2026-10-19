import { execSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { CONTEST_SUBJECTS } from "../src/lib/contests";
import { generatePlan, type Catalog, type PlanInput, type SegmentsByAula } from "../src/lib/planner";

const CONTENT_DIR = path.resolve(__dirname, "../../content");

function loadBranchCatalog(): Catalog {
  const c = JSON.parse(fs.readFileSync(path.join(CONTENT_DIR, "catalog.json"), "utf-8")) as Catalog;
  return { ...c, gaps: c.gaps.filter((g) => !g.resolved) };
}

function loadMainCatalog(): Catalog {
  const raw = execSync("git show main:content/catalog.json", { maxBuffer: 15 * 1024 * 1024 }).toString("utf-8");
  const c = JSON.parse(raw) as Catalog;
  return { ...c, gaps: c.gaps.filter((g) => !g.resolved) };
}

function loadSegments(): SegmentsByAula {
  const out: SegmentsByAula = {};
  for (const f of fs.readdirSync(path.join(CONTENT_DIR, "segments"))) {
    const { segments } = JSON.parse(fs.readFileSync(path.join(CONTENT_DIR, "segments", f), "utf-8"));
    for (const s of segments) (out[s.aula] ??= []).push(s);
  }
  return out;
}

function loadImportance(contest: string): Record<string, number | null> {
  const doc = JSON.parse(fs.readFileSync(path.join(CONTENT_DIR, "importance", "segments.json"), "utf-8")) as {
    segments: Record<string, { contests: Record<string, { appears: boolean; score: number | null }> }>;
  };
  return Object.fromEntries(
    Object.entries(doc.segments).map(([id, r]) => [id, r.contests[contest]?.appears ? r.contests[contest].score : null])
  );
}

function loadExamQuestions(contest: string): Record<string, number> {
  const doc = JSON.parse(fs.readFileSync(path.join(CONTENT_DIR, "contests.json"), "utf-8")) as Record<
    string,
    { exam: Record<string, number> }
  >;
  return doc[contest].exam;
}

const CONTESTS = ["CBMPE_OFICIAL", "CBMPE_SOLDADO", "PMPE_OFICIAL", "PMPE_SOLDADO"] as const;
const HOURS = [15, 25, 40] as const;
const LEVELS = [0, 2] as const;
const TURBOS = [false, true] as const;

const MODES = [
  { name: "fixtures", stripFilters: false },
  { name: "como no banco", stripFilters: true },
] as const;

function stripContestFilters(cat: Catalog): Catalog {
  return {
    ...cat,
    subjects: cat.subjects.map((s) => ({
      ...s,
      aulas: s.aulas.map((a) => {
        const copy = { ...a };
        delete copy.onlyContests;
        delete copy.excludeContests;
        return copy;
      }),
    })),
  };
}

async function main() {
  console.log("=== COMPARAÇÃO DE PLANOS: MAIN vs BRANCH ===");
  const mainCat = loadMainCatalog();
  const rawBranchCat = loadBranchCatalog();
  const segments = loadSegments();

  let grandTotalScenarios = 0;
  let grandTotalDiffs = 0;

  for (const mode of MODES) {
    console.log(`\n--- MODO: ${mode.name.toUpperCase()} ---`);
    const branchCat = mode.stripFilters ? stripContestFilters(rawBranchCat) : rawBranchCat;

    let totalScenarios = 0;
    let diffCount = 0;

    for (const contest of CONTESTS) {
      const subjects = CONTEST_SUBJECTS[contest].filter((id) => id !== "lingua-espanhola");
      const importance = loadImportance(contest);
      const examQuestions = loadExamQuestions(contest);

      for (const hours of HOURS) {
        for (const level of LEVELS) {
          for (const turbo of TURBOS) {
            totalScenarios++;
            grandTotalScenarios++;
            const scenarioLabel = `[${mode.name}] ${contest} | ${hours}h | lvl ${level} | turbo ${turbo}`;

            const baseInput: Omit<PlanInput, "catalog"> = {
              segments,
              startDate: "2026-10-12",
              examDate: "2027-02-28",
              hoursPerWeek: hours,
              subjects: subjects.map((id) => ({ id, level })),
              importance,
              examQuestions,
              contest,
              turbo,
            };

            const planMain = generatePlan({ ...baseInput, catalog: mainCat });
            const planBranch = generatePlan({ ...baseInput, catalog: branchCat });

            const mainActs = planMain.weeks.flatMap((w) => w.activities);
            const branchActs = planBranch.weeks.flatMap((w) => w.activities);

            const mainDAActs = mainActs.filter((a) => a.subjectId === "direito-administrativo");
            const branchDAActs = branchActs.filter((a) => a.subjectId === "direito-administrativo");

            const diffs: string[] = [];

            if (mainActs.length !== branchActs.length) {
              diffs.push(`Total activities: main=${mainActs.length}, branch=${branchActs.length}`);
            }
            if (mainDAActs.length !== branchDAActs.length) {
              diffs.push(`DA activities: main=${mainDAActs.length}, branch=${branchDAActs.length}`);
            }
            if (planMain.params.plannedHours !== planBranch.params.plannedHours) {
              diffs.push(`Planned hours: main=${planMain.params.plannedHours}, branch=${planBranch.params.plannedHours}`);
            }
            if (Math.abs(planMain.coverage.selected - planBranch.coverage.selected) > 1e-6) {
              diffs.push(`Coverage selected: main=${planMain.coverage.selected}, branch=${planBranch.coverage.selected} (diff=${Math.abs(planMain.coverage.selected - planBranch.coverage.selected)})`);
            }
            if (Math.abs(planMain.coverage.edital - planBranch.coverage.edital) > 1e-6) {
              diffs.push(`Coverage edital: main=${planMain.coverage.edital}, branch=${planBranch.coverage.edital} (diff=${Math.abs(planMain.coverage.edital - planBranch.coverage.edital)})`);
            }

            // Check activity-by-activity match
            const minLen = Math.min(mainActs.length, branchActs.length);
            for (let i = 0; i < minLen; i++) {
              const m = mainActs[i];
              const b = branchActs[i];
              if (m.type !== b.type || m.subjectId !== b.subjectId || m.aulaId !== b.aulaId || m.minutes !== b.minutes) {
                diffs.push(`Act ${i}: main=[${m.type} ${m.aulaId} ${m.minutes}m] vs branch=[${b.type} ${b.aulaId} ${b.minutes}m]`);
                break; // report first mismatch
              }
            }

            if (diffs.length > 0) {
              diffCount++;
              grandTotalDiffs++;
              console.error(`FAIL: ${scenarioLabel}`);
              for (const d of diffs) {
                console.error(`  - ${d}`);
              }
            }
          }
        }
      }
    }

    console.log(`Cenários no modo ${mode.name}: ${totalScenarios} (Divergências: ${diffCount})`);
  }

  console.log(`\nTotal geral de cenários testados: ${grandTotalScenarios}`);
  console.log(`Total geral de divergências: ${grandTotalDiffs}`);

  if (grandTotalDiffs > 0) {
    process.exit(1);
  } else {
    console.log("SUCESSO: 0 divergências entre main e branch em ambos os modos (fixtures e como no banco)!");
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
