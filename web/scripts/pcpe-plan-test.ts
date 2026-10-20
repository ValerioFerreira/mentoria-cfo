// Gera 10 planos de teste do PCPE com entradas variadas, roda o verificador e grava tudo em JSON para auditoria.
//   npx tsx scripts/pcpe-plan-test.ts [saida.json]     (padrão: ../pipeline/.cache/pcpe-planos.json)
// Depois: pipeline/.venv/Scripts/python pipeline/pcpe_tools/audit_planos.py
import { readdirSync, readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { generatePlan } from "../src/lib/planner";
import { loadCatalog, loadSegments, loadImportance, loadExamQuestions } from "../src/lib/planner/fixtures";
import { planFromResult, verifyPlan } from "../src/lib/planner/verify";
import { CONTEST_SUBJECTS } from "../src/lib/contests";
import type { Known, Level } from "../src/lib/planner/types";

const out = process.argv[2] ?? resolve(__dirname, "../../pipeline/.cache/pcpe-planos.json");
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

const SC: { name: string; start: string; firstDay: number; exam: string; hours: number; level: Level | "mix"; subjects: string[]; turbo: boolean; known?: Record<string, Known>; excluded?: string[] }[] = [
  { name: "01 iniciante 10h todas", start: "2026-10-19", firstDay: 1, exam: "2027-03-07", hours: 10, level: 0, subjects: ALL, turbo: false },
  { name: "02 iniciante 10h todas Turbo", start: "2026-10-19", firstDay: 1, exam: "2027-03-07", hours: 10, level: 0, subjects: ALL, turbo: true },
  { name: "03 básico 20h todas", start: "2026-10-19", firstDay: 1, exam: "2027-03-07", hours: 20, level: 1, subjects: ALL, turbo: false },
  { name: "04 básico 20h todas Turbo", start: "2026-10-19", firstDay: 1, exam: "2027-03-07", hours: 20, level: 1, subjects: ALL, turbo: true },
  { name: "05 intermediário 30h todas", start: "2026-10-19", firstDay: 1, exam: "2027-03-07", hours: 30, level: 2, subjects: ALL, turbo: false },
  { name: "06 avançado 40h todas", start: "2026-10-19", firstDay: 1, exam: "2027-03-07", hours: 40, level: 3, subjects: ALL, turbo: false },
  { name: "07 só jurídicas 15h básico", start: "2026-10-19", firstDay: 1, exam: "2027-03-07", hours: 15, level: 1, subjects: JUR, turbo: false },
  { name: "08 só exatas/inf/port 25h interm. com já estudei/domino", start: "2026-10-19", firstDay: 1, exam: "2027-03-07", hours: 25, level: 2, subjects: EXAT, turbo: false, known: { ...marks(EXAT, 3, 1), ...marks(EXAT, 7, 2, 1) } },
  { name: "09 início em 16/11, 12h, iniciante, já estudei, Turbo", start: "2026-11-16", firstDay: 0, exam: "2027-03-07", hours: 12, level: 0, subjects: ALL, turbo: true, known: marks(ALL, 4, 1, 2) },
  { name: "10 35h básico, assuntos excluídos e domino", start: "2026-10-19", firstDay: 1, exam: "2027-03-07", hours: 35, level: 1, subjects: ALL, turbo: false, known: marks(ALL, 6, 2), excluded: aulasOf(["informatica"]).slice(0, 4) },
];

const result: unknown[] = [];
for (const s of SC) {
  const level = (s.level === "mix" ? 1 : s.level) as Level;
  const input = {
    catalog, segments, contest: "PCPE_AGENTE", importance, summaries, examQuestions, startDate: s.start, firstDay: s.firstDay, examDate: s.exam,
    hoursPerWeek: s.hours, subjects: s.subjects.map((id) => ({ id, level })), known: s.known ?? {}, excludedAulas: s.excluded ?? [], turbo: s.turbo,
  };
  const plan = generatePlan(input);
  const vp = planFromResult(plan, s.start, s.exam, s.name);
  const rep = verifyPlan(vp, { catalog, segments, importance, summaries: new Set(summaries) });
  const acts = plan.weeks.flatMap((w) => w.activities.map((a) => ({ ...a, week: w.index, ord: (w.index - 1) * 7 + (a.day ?? 0) })));
  console.log(`${s.name}: ${rep.verdict} erros ${rep.errors.length} avisos ${rep.warnings.length} | atividades ${acts.length} | cobertura ${(plan.coverage.selected * 100).toFixed(0)}% edital ${(plan.coverage.edital * 100).toFixed(0)}%`);
  for (const e of rep.errors.slice(0, 5)) console.log("   ERRO", e.code, e.message, e.where ?? "");
  result.push({ name: s.name, input: { ...s, known: s.known ? Object.keys(s.known).length : 0 }, verdict: rep.verdict, errors: rep.errors, warnings: rep.warnings.slice(0, 20), stats: rep.stats, coverage: plan.coverage.selected, warningsPlan: plan.warnings, acts });
}
writeFileSync(out, JSON.stringify(result));
