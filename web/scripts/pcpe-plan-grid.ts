// Gera uma GRADE de planos do PCPE (horas x nível x Turbo x disciplinas x marcações), roda o verificador e grava tudo em JSON para auditoria.
//   npx tsx scripts/pcpe-plan-test.ts [saida.json]     (padrão: ../pipeline/.cache/pcpe-planos-grade.json)
// Depois: pipeline/.venv/Scripts/python pipeline/pcpe_tools/audit_planos.py
import { readdirSync, readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { generatePlan } from "../src/lib/planner";
import { loadCatalog, loadSegments, loadImportance, loadExamQuestions } from "../src/lib/planner/fixtures";
import { CONTEST_SUBJECTS } from "../src/lib/contests";
import type { Known, Level } from "../src/lib/planner/types";

const out = process.argv[2] ?? resolve(__dirname, "../../pipeline/.cache/pcpe-planos-grade.json");
const catalog = loadCatalog();
const segments = loadSegments();
const importance = loadImportance("PCPE_AGENTE");
const examQuestions = loadExamQuestions("PCPE_AGENTE");
const sumDir = resolve(__dirname, "../../content/summaries");
const summaries: string[] = [];
for (const d of readdirSync(sumDir, { withFileTypes: true }).filter((x) => x.isDirectory())) {
  for (const f of readdirSync(resolve(sumDir, d.name))) {
    const doc = JSON.parse(readFileSync(resolve(sumDir, d.name, f), "utf8")) as { segments: { id: string }[] };
    for (const s of doc.segments) summaries.push(s.id);
  }
}
const ALL = CONTEST_SUBJECTS.PCPE_AGENTE.filter((id) => id !== "lingua-espanhola" && id !== "lingua-inglesa");
const JUR = ["legislacao-pcpe", "direito-constitucional", "direito-administrativo", "direito-penal", "legislacao-penal-especial", "direito-processual-penal"];
const EXAT = ["lingua-portuguesa", "informatica", "contabilidade-geral", "raciocinio-logico", "matematica", "estatistica"];

const aulasOf = (ids: string[]) => catalog.subjects.filter((s) => ids.includes(s.id)).flatMap((s) => s.aulas.filter((a) => a.selectable).map((a) => a.id));
function marks(ids: string[], every: number, v: Known, offset = 0): Record<string, Known> {
  const r: Record<string, Known> = {};
  aulasOf(ids).forEach((a, i) => { if ((i + offset) % every === 0) r[a] = v; });
  return r;
}

const SUBSETS: string[][] = [ALL, JUR, EXAT, [...JUR.slice(0, 3), ...EXAT.slice(0, 3)], [...JUR.slice(3), ...EXAT.slice(3)], ...ALL.map((d) => [d])];
const SC: { name: string; start: string; firstDay: number; exam: string; hours: number; level: Level; subjects: string[]; turbo: boolean; known?: Record<string, Known> }[] = [];
let n = 0;
for (const hours of [6, 10, 15, 20, 30, 40, 55]) {
  for (const level of [0, 1, 2, 3] as Level[]) {
    for (const turbo of [false, true]) {
      const subs = SUBSETS[n % 5];
      SC.push({ name: `g${String(n).padStart(3, "0")} ${hours}h n${level}${turbo ? " T" : ""} s${n % 5}`, start: "2026-10-19", firstDay: 1, exam: "2027-03-07", hours, level, subjects: subs, turbo, known: n % 3 === 0 ? marks(subs, 4, 1, n % 4) : undefined });
      n++;
    }
  }
}
for (const [i, subs] of SUBSETS.slice(5).entries()) {
  for (const [hours, level] of [[8, 0], [20, 2], [35, 3]] as [number, Level][]) {
    SC.push({ name: `d${i} ${hours}h n${level}`, start: "2026-10-19", firstDay: 1, exam: "2027-03-07", hours, level, subjects: subs, turbo: false, known: i % 2 ? marks(subs, 3, 2) : undefined });
  }
}

const result: unknown[] = [];
for (const s of SC) {
  const input = {
    catalog, segments, contest: "PCPE_AGENTE", importance, summaries, examQuestions, startDate: s.start, firstDay: s.firstDay, examDate: s.exam,
    hoursPerWeek: s.hours, subjects: s.subjects.map((id) => ({ id, level: s.level })), known: s.known ?? {}, excludedAulas: [], turbo: s.turbo,
  };
  try {
    const plan = generatePlan(input);
    const acts = plan.weeks.flatMap((w) => w.activities.filter((a) => a.type === "QUESTOES" || a.type === "TEORIA").map((a) => ({ type: a.type, key: a.key, segmentIds: a.segmentIds, quiz: a.quiz, scope: a.scope, subjectId: a.subjectId, ord: (w.index - 1) * 7 + (a.day ?? 0) })));
    result.push({ name: s.name, acts });
  } catch (e) {
    console.log("falhou", s.name, String(e).slice(0, 80));
  }
}
console.log(result.length, "planos");
writeFileSync(out, JSON.stringify(result));
