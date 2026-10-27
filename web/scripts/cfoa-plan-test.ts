// Gera 10 planos de teste do 2º Tenente CFOA com entradas variadas, roda o verificador e grava tudo em JSON para auditoria
// (cada atividade com aula, trecho, páginas, diretriz e se há resumo analítico).
//   npx tsx scripts/cfoa-plan-test.ts [saida.json] [--ciclo]     (padrão: ../pipeline/.cache/cfoa-planos.json)
// O CFOA ainda não tem data de prova: usa 28/03/2027 como hipótese; com --ciclo, gera o 1º ciclo do edital (sem data).
import { readdirSync, readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { generatePlan } from "../src/lib/planner";
import { loadCatalog, loadSegments, loadImportance, loadExamQuestions } from "../src/lib/planner/fixtures";
import { planFromResult, verifyPlan } from "../src/lib/planner/verify";
import { CONTEST_SUBJECTS } from "../src/lib/contests";
import type { Known, Level } from "../src/lib/planner/types";

const CONTEST = "CBMPE_CFOA";
const EXAM = "2027-03-28";
const CYCLE = process.argv.includes("--ciclo");
const out = process.argv.slice(2).find((a) => !a.startsWith("--")) ?? resolve(__dirname, "../../pipeline/.cache/cfoa-planos.json");
const catalog = loadCatalog();
const segments = loadSegments();
const importance = loadImportance(CONTEST);
const examQuestions = loadExamQuestions(CONTEST);
const sumDir = resolve(__dirname, "../../content/summaries");
const summaries: string[] = [];
for (const d of readdirSync(sumDir, { withFileTypes: true }).filter((x) => x.isDirectory())) {
  for (const f of readdirSync(resolve(sumDir, d.name))) {
    const doc = JSON.parse(readFileSync(resolve(sumDir, d.name, f), "utf8")) as { segments: { id: string }[] };
    for (const s of doc.segments) summaries.push(s.id);
  }
}
const ALL = [...CONTEST_SUBJECTS[CONTEST]];
const JUR = ALL.filter((id) => id.startsWith("direito") || id === "legislacoes-pe" || id === "direitos-humanos");
const GER = ALL.filter((id) => !JUR.includes(id));

const aulasOf = (ids: string[]) => catalog.subjects.filter((s) => ids.includes(s.id)).flatMap((s) => s.aulas.filter((a) => a.selectable).map((a) => a.id));
function marks(ids: string[], every: number, v: Known, offset = 0): Record<string, Known> {
  const r: Record<string, Known> = {};
  aulasOf(ids).forEach((a, i) => { if ((i + offset) % every === 0) r[a] = v; });
  return r;
}

const SC: { name: string; start: string; firstDay: number; hours: number; level: Level; subjects: string[]; turbo: boolean; known?: Record<string, Known>; excluded?: string[] }[] = [
  { name: "01 iniciante 10h todas", start: "2026-10-26", firstDay: 0, hours: 10, level: 0, subjects: ALL, turbo: false },
  { name: "02 iniciante 10h todas Turbo", start: "2026-10-26", firstDay: 0, hours: 10, level: 0, subjects: ALL, turbo: true },
  { name: "03 básico 20h todas", start: "2026-10-26", firstDay: 0, hours: 20, level: 1, subjects: ALL, turbo: false },
  { name: "04 básico 20h todas Turbo", start: "2026-10-26", firstDay: 0, hours: 20, level: 1, subjects: ALL, turbo: true },
  { name: "05 intermediário 30h todas", start: "2026-10-26", firstDay: 0, hours: 30, level: 2, subjects: ALL, turbo: false },
  { name: "06 avançado 45h todas", start: "2026-10-26", firstDay: 0, hours: 45, level: 3, subjects: ALL, turbo: false },
  { name: "07 só jurídicas 18h básico", start: "2026-10-26", firstDay: 0, hours: 18, level: 1, subjects: JUR, turbo: false },
  { name: "08 só gerais 15h intermediário com já estudei/domino", start: "2026-10-26", firstDay: 0, hours: 15, level: 2, subjects: GER, turbo: false, known: { ...marks(GER, 3, 1), ...marks(GER, 7, 2, 1) } },
  { name: "09 início em 16/11 (quarta), 12h, iniciante, já estudei, Turbo", start: "2026-11-16", firstDay: 2, hours: 12, level: 0, subjects: ALL, turbo: true, known: marks(ALL, 4, 1, 2) },
  { name: "10 35h básico, assuntos excluídos e domino", start: "2026-10-26", firstDay: 0, hours: 35, level: 1, subjects: ALL, turbo: false, known: marks(ALL, 6, 2), excluded: aulasOf(["administracao"]).slice(0, 2) },
];

const segById = new Map(Object.values(segments).flat().map((s) => [s.id, s as typeof s & { startPage?: number; endPage?: number; startTopic?: string }]));
const aulaById = new Map(catalog.subjects.flatMap((s) => s.aulas.map((a) => [a.id, a] as const)));
const result: unknown[] = [];
for (const s of SC) {
  const input = {
    catalog, segments, contest: CONTEST, importance, summaries, examQuestions, examTotalQuestions: 100, startDate: s.start, firstDay: s.firstDay, examDate: EXAM,
    hoursPerWeek: s.hours, subjects: s.subjects.map((id) => ({ id, level: s.level })), known: s.known ?? {}, excludedAulas: s.excluded ?? [], turbo: s.turbo, ...(CYCLE ? { cycle: 1 } : {}),
  };
  const tGen = Date.now();
  const plan = generatePlan(input);
  const genMs = Date.now() - tGen;
  const vp = planFromResult(plan, s.start, plan.params.examDate, s.name);
  const rep = verifyPlan(vp, { catalog, segments, importance, summaries: new Set(summaries) });
  const acts = plan.weeks.flatMap((w) =>
    w.activities.map((a) => {
      const segIds: string[] = ((a as { segmentIds?: string[] }).segmentIds ?? [(a as { segmentId?: string }).segmentId]).filter(Boolean) as string[];
      const aula = aulaById.get((a as { aulaId?: string }).aulaId ?? "");
      return {
        ...a,
        week: w.index,
        aulaTitle: aula?.title,
        material: (aula as { materialPath?: string } | undefined)?.materialPath ?? null,
        segs: segIds.map((id) => ({ id, pages: [segById.get(id)?.startPage, segById.get(id)?.endPage], topic: segById.get(id)?.startTopic, hasSummary: summaries.includes(id) })),
      };
    }),
  );
  console.log(`${s.name}: ${rep.verdict} [${genMs} ms${CYCLE ? `, fim ${plan.params.examDate}, ${plan.params.totalWeeks} sem.` : ""}] erros ${rep.errors.length} avisos ${rep.warnings.length} | atividades ${acts.length} | cobertura ${(plan.coverage.selected * 100).toFixed(0)}% edital ${(plan.coverage.edital * 100).toFixed(0)}%`);
  for (const e of rep.errors.slice(0, 5)) console.log("   ERRO", e.code, e.message, e.where ?? "");
  result.push({ name: s.name, input: { ...s, known: s.known ? Object.keys(s.known).length : 0 }, verdict: rep.verdict, errors: rep.errors, warnings: rep.warnings.slice(0, 30), stats: rep.stats, coverage: plan.coverage, warningsPlan: plan.warnings, acts });
}
writeFileSync(out, JSON.stringify(result));
console.log("gravado:", out);
