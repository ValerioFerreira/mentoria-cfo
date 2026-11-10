// Amostra (somente leitura) das diretrizes dos planos, para conferir se apontam o lugar certo nos dois materiais.
// População: cada atividade de Teoria, Revisão ou Fixação × material (material-base sempre; material MentorIA quando
// todos os trechos da atividade têm capítulo no índice). Amostra estratificada por tipo e material, com o tamanho para
// 95% de confiança e ±5% de margem (n = 385 / (1 + 384/N)). A conferência das páginas é feita por
// pipeline/directive_check.py, que lê os PDFs.
//   npx tsx scripts/directive-audit.ts [--remoto] [--semente 7]
import "dotenv/config";
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";
import {
  withAnchor, fixacaoMentoria, fixacaoSteps, revisaoMentoria, teoriaDirective, teoriaMentoria, turboDirective,
  type AulaRef, type SegmentAnchor, type FixRange, type MaterialChapter, type SegmentRef,
} from "../src/lib/directive";

const anchors = JSON.parse(readFileSync(resolve(__dirname, "..", "content", "directive", "anchors.json"), "utf8")) as Record<string, SegmentAnchor>;

function url(): string {
  if (!process.argv.includes("--remoto")) return process.env.DATABASE_URL || "";
  const f = resolve(__dirname, "..", ".env.remote");
  if (!existsSync(f)) throw new Error("web/.env.remote não existe");
  const m = readFileSync(f, "utf8").match(/^\s*REMOTE_DATABASE_URL\s*=\s*"?([^"\r\n]+)"?/m);
  if (!m) throw new Error("REMOTE_DATABASE_URL ausente em web/.env.remote");
  return m[1];
}
const arg = (k: string) => { const i = process.argv.indexOf(k); return i >= 0 ? process.argv[i + 1] : undefined; };
const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: url().replace(/([?&])pgbouncer=true(&|$)/, (_, a, b) => (b ? a : "")) }) });

function loadChapters(): Map<string, MaterialChapter> {
  const idx = JSON.parse(readFileSync(resolve(__dirname, "..", "content", "material", "index.json"), "utf8"));
  const map = new Map<string, MaterialChapter>();
  for (const [volumeId, v] of Object.entries<any>(idx.volumes)) {
    for (const [trecho, c] of Object.entries<any>(v.capitulos)) {
      if (!c.pagina || !c.ate) continue;
      map.set(trecho, { trecho, volumeId, volumeNumber: v.numero, volumeTitle: v.titulo, subjectName: v.disciplina, chapter: c.numero, title: c.titulo,
        start: c.pagina, end: c.ate, mapPage: c.mapa, reviewPage: c.revisao, questions: c.questoes });
    }
  }
  return map;
}

// PRNG determinístico (mulberry32), para a amostra poder ser refeita
function rng(seed: number) {
  return () => { seed |= 0; seed = (seed + 0x6d2b79f5) | 0; let t = Math.imul(seed ^ (seed >>> 15), 1 | seed); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
}

async function main() {
  const chapters = loadChapters();
  const acts = await db.activity.findMany({
    where: { type: { in: ["TEORIA", "REVISAO", "FIXACAO"] } },
    select: {
      id: true, type: true, turbo: true, scope: true, aulaId: true, fixRanges: true,
      aula: { select: { id: true, number: true, shortTitle: true, printedOffset: true, source: true, materialPath: true, commentedRuns: true, practiceLinks: true, subject: { select: { name: true } } } },
      segments: { select: { segment: { select: { id: true, aulaId: true, startPage: true, endPage: true, startPrinted: true, endPrinted: true, startTopic: true,
        startsMidTopic: true, stopBeforeTopic: true, endsMidTopic: true, endTopic: true, endsTheory: true } } } },
      week: { select: { plan: { select: { id: true, contest: true } } } },
    },
  });
  type Unit = { stratum: string; material: "base" | "mentoria"; a: (typeof acts)[number] };
  const units: Unit[] = [];
  for (const a of acts) {
    if (a.type !== "FIXACAO" && a.segments.length === 0) continue;
    units.push({ stratum: `${a.type}${a.turbo ? "-TURBO" : ""}·base`, material: "base", a });
    const segIds = a.segments.map((s) => s.segment.id);
    const has = a.type === "FIXACAO"
      ? [...chapters.values()].some((c) => c.trecho.startsWith(a.aulaId + "/") && c.questions)
      : segIds.length > 0 && segIds.every((id) => chapters.has(id));
    if (has) units.push({ stratum: `${a.type}${a.turbo ? "-TURBO" : ""}·mentoria`, material: "mentoria", a });
  }
  const N = units.length;
  const n = Math.min(N, Math.ceil(385 / (1 + 384 / N)));
  const strata = new Map<string, Unit[]>();
  for (const u of units) strata.set(u.stratum, [...(strata.get(u.stratum) ?? []), u]);
  const rand = rng(Number(arg("--semente") ?? 7));
  const sample: Unit[] = [];
  for (const [, list] of [...strata].sort()) {
    const k = Math.max(1, Math.round((n * list.length) / N));
    const pool = [...list];
    for (let i = 0; i < k && pool.length; i++) sample.push(pool.splice(Math.floor(rand() * pool.length), 1)[0]);
  }
  const out = sample.map(({ material, stratum, a }) => {
    const aula: AulaRef = { id: a.aula.id, number: a.aula.number, shortTitle: a.aula.shortTitle, subjectName: a.aula.subject.name,
      printedOffset: a.aula.printedOffset, authored: a.aula.source === "AUTHORED", materialPath: a.aula.materialPath };
    const segs: SegmentRef[] = a.segments.map((s) => withAnchor(s.segment as SegmentRef, anchors[s.segment.id])).sort((x, y) => x.startPage - y.startPage);
    const chs = a.type === "FIXACAO"
      ? [...chapters.values()].filter((c) => c.trecho.startsWith(a.aulaId + "/"))
      : segs.map((s) => chapters.get(s.id)!).filter(Boolean);
    // páginas da Fixação: as do catálogo atual, como a tela da atividade mostra (o plano pode ter gravado páginas velhas)
    const cur: FixRange[] = [
      ...((a.aula.commentedRuns as [number, number][] | null) ?? []).map(([start, end]) => ({ start, end })),
      ...((a.aula.practiceLinks as { startPage: number; endPage: number; sourceAula: string }[] | null) ?? []).map((l) => ({ start: l.startPage, end: l.endPage, sourceAula: l.sourceAula })),
    ];
    const fixRanges = cur.length ? cur : ((a.fixRanges as FixRange[] | null) ?? []);
    let text: string[];
    if (material === "base") {
      text = a.type === "TEORIA" ? (a.turbo ? turboDirective(aula, segs).steps : teoriaDirective(aula, segs).steps)
        : a.type === "FIXACAO" ? fixacaoSteps(aula, fixRanges, (id) => id)
          : segs.map((s) => `págs. ${s.startPage}–${s.endPage}`);
    } else {
      text = a.type === "TEORIA" ? teoriaMentoria(chs).flatMap((b) => b.steps) : a.type === "FIXACAO" ? fixacaoMentoria(chs) : revisaoMentoria(chs);
    }
    return { activity: a.id, plan: a.week.plan.id, contest: a.week.plan.contest, type: a.type, turbo: a.turbo, scope: a.scope, stratum, material,
      aula: { ...aula }, segments: segs, fixRanges, fixRangesGravadas: a.fixRanges, chapters: material === "mentoria" ? chs : [], directive: text };
  });
  const dir = resolve(__dirname, "..", "..", "pipeline", ".cache", "directive-audit");
  mkdirSync(dir, { recursive: true });
  const file = resolve(dir, `amostra-${process.argv.includes("--remoto") ? "remoto" : "local"}.json`);
  writeFileSync(file, JSON.stringify({ geradoEm: new Date().toISOString(), N, n: sample.length, strata: Object.fromEntries([...strata].map(([k, v]) => [k, v.length])), amostra: out }, null, 1));
  console.log(`população N=${N} (atividades: ${acts.length}) · amostra n=${sample.length} -> ${file}`);
  for (const [k, v] of [...strata].sort()) console.log(`  ${k.padEnd(28)} ${v.length}`);
}

main().finally(() => db.$disconnect());
