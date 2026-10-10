import fs from "fs";
import path from "path";
import { generatePlan } from "../src/lib/planner";
import type { Catalog, CatalogAula, Level, PlannedActivity, SegmentLite, SegmentsByAula } from "../src/lib/planner/types";

function loadData() {
  const root = path.resolve(__dirname, "../../");
  const catalogRaw = JSON.parse(fs.readFileSync(path.join(root, "content/catalog.json"), "utf8"));
  const segments: SegmentsByAula = {};

  const segFiles = fs.readdirSync(path.join(root, "content/segments")).filter((f) => f.endsWith(".json"));
  for (const f of segFiles) {
    const data = JSON.parse(fs.readFileSync(path.join(root, "content/segments", f), "utf8"));
    for (const s of data.segments || []) {
      const aulaId = s.id.split("/").slice(0, 2).join("/");
      (segments[aulaId] ??= []).push({
        id: s.id,
        aula: aulaId,
        order: s.sortOrder,
        startPage: s.startPage,
        endPage: s.endPage,
        pages: s.pages,
        load: s.load,
      });
    }
  }

  const catalog: Catalog = {
    subjects: catalogRaw.subjects.map((s: any) => ({
      id: s.id,
      name: s.name,
      block: s.block,
      examQuestions: s.examQuestions,
      sortOrder: s.sortOrder,
      aulas: s.aulas.map((a: any) => ({
        id: a.id,
        number: a.number,
        title: a.title,
        shortTitle: a.shortTitle,
        kind: a.kind,
        edital: a.edital,
        selectable: a.selectable,
        theoryPages: a.theoryPages,
        segmentCount: a.segmentCount,
        commentedPages: a.commentedPages,
        listPages: a.listPages,
        commentedRuns: a.commentedRuns,
        practiceLinks: a.practiceLinks,
        incidence: a.incidence,
        printedOffset: a.printedOffset,
        source: a.source,
      })),
    })),
    gaps: catalogRaw.gaps || [],
  };

  return { catalog, segments };
}

async function main() {
  const data = loadData();
  const scenarios = [
    { name: "Plano Normal - 24h/sem - Nível Médio", hours: 24, turbo: false, level: 1 as Level },
    { name: "Plano Leve - 16h/sem - Nível Iniciante", hours: 16, turbo: false, level: 0 as Level },
    { name: "Plano Avançado - 35h/sem - Nível Avançado", hours: 35, turbo: false, level: 2 as Level },
    { name: "Plano Modo Turbo - 18h/sem - Nível Médio", hours: 18, turbo: true, level: 1 as Level },
    { name: "Plano Intensivo - 45h/sem - Nível Misto", hours: 45, turbo: false, level: 1 as Level },
  ];

  console.log("=== TESTANDO GERAÇÃO DE PLANOS COM AS NOVAS REGRAS ===");

  for (const sc of scenarios) {
    const subjects = data.catalog.subjects.map((s) => ({ id: s.id, level: sc.level }));
    const result = generatePlan({
      ...data,
      startDate: "2026-10-12",
      firstDay: 0,
      examDate: "2027-02-28",
      hoursPerWeek: sc.hours,
      subjects,
      known: {},
      turbo: sc.turbo,
    });

    const acts = result.weeks.flatMap((w) => w.activities);
    const under50 = acts.filter((a) => a.minutes < 50);
    const between50_80 = acts.filter((a) => a.minutes >= 50 && a.minutes <= 80);
    const over80 = acts.filter((a) => a.minutes > 80);

    // Checar dias por disciplina
    let dailyViolations = 0;
    for (const w of result.weeks) {
      const byDaySub: Record<string, number> = {};
      for (const a of w.activities) {
        if (a.day != null) {
          const k = `d${a.day}#${a.subjectId}`;
          byDaySub[k] = (byDaySub[k] || 0) + a.minutes;
        }
      }
      for (const [k, mins] of Object.entries(byDaySub)) {
        if (mins > 120) {
          dailyViolations++;
        }
      }
    }

    console.log(`\nCenário: ${sc.name}`);
    console.log(`Total atividades: ${acts.length} | Semanas: ${result.weeks.length}`);
    console.log(`  < 50 min: ${under50.length}`);
    console.log(`  50 a 80 min: ${between50_80.length} (${((between50_80.length / acts.length) * 100).toFixed(1)}%)`);
    console.log(`  > 80 min: ${over80.length}`);
    console.log(`  Violações diárias (>120m/disciplina): ${dailyViolations}`);

    for (let wi = 0; wi < result.weeks.length; wi++) {
      const w = result.weeks[wi];
      const byDaySub: Record<string, PlannedActivity[]> = {};
      for (const a of w.activities) {
        if (a.day != null) {
          const k = `w${wi+1}#d${a.day}#${a.subjectId}`;
          (byDaySub[k] ??= []).push(a);
        }
      }
      for (const [k, list] of Object.entries(byDaySub)) {
        const total = list.reduce((n, a) => n + a.minutes, 0);
        if (total > 120) {
          console.log(`  Violação diária em ${k}: ${total}m (${list.map(a => `${a.type}:${a.minutes}m`).join(", ")})`);
        }
      }
    }

    if (under50.length > 0) {
      console.log("  Exemplos < 50m:", under50.slice(0, 3).map((a) => `${a.type} ${a.minutes}m (${a.key})`));
    }
    if (over80.length > 0) {
      console.log("  Exemplos > 80m:", over80.slice(0, 3).map((a) => `${a.type} ${a.minutes}m (${a.key})`));
    }
  }
}

main().catch(console.error);
