// Levantamento (SÓ LEITURA, banco local) da base de questões servíveis por trecho elegível do CBMPE_CFOA.
// Grava `pipeline/briefs/ineditas-cfoa-base.json` com:
//   - segs: { [segmentId]: { efetiva, txt } } para todos os trechos com appears: true em CBMPE_CFOA
//   - grupos: { [aulaId]: segmentId[] } com os até 4 primeiros trechos elegíveis de cada aula do CFOA
//
// Uso (a partir de web/):
//   npx tsx scripts/cfoa-cadernos-base.ts
import "dotenv/config";
import { existsSync, readdirSync, readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";
import { activityQuizWhere, reinforcementQuizWhere } from "../src/lib/quiz/banca";
import { servableStatuses } from "../src/lib/quiz/servable";

const ROOT = resolve(__dirname, "../..");
const IMP_PATH = resolve(ROOT, "content/importance/segments.json");
const MC_DIR = resolve(ROOT, "content/questoes/ineditas/mc");
const OUT_PATH = resolve(ROOT, "pipeline/briefs/ineditas-cfoa-base.json");

const url = (process.env.DATABASE_URL || "").replace(/([?&])pgbouncer=true(&|$)/, (_, a, b) => (b ? a : ""));
if (!url) throw new Error("DATABASE_URL vazio em web/.env");
const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: url }) });

function countTxtIneditas(): Map<string, number> {
  const counts = new Map<string, number>();
  if (!existsSync(MC_DIR)) return counts;
  for (const file of readdirSync(MC_DIR)) {
    if (!file.endsWith(".txt")) continue;
    const disc = file.slice(0, -4);
    const content = readFileSync(resolve(MC_DIR, file), "utf8");
    const re = /^@@\s*(\S+)\s*\|/gm;
    let m: RegExpExecArray | null;
    while ((m = re.exec(content)) !== null) {
      const segId = `${disc}/${m[1]}`;
      counts.set(segId, (counts.get(segId) ?? 0) + 1);
    }
  }
  return counts;
}

(async () => {
  const imp = JSON.parse(readFileSync(IMP_PATH, "utf8")) as {
    segments: Record<string, { contests?: Record<string, { appears?: boolean }> }>;
  };

  const cfoaSegs = Object.entries(imp.segments)
    .filter(([, v]) => v.contests?.CBMPE_CFOA?.appears === true)
    .map(([k]) => k)
    .sort();

  const statuses = servableStatuses();
  const primaryRows = await db.question.findMany({
    where: activityQuizWhere(cfoaSegs, statuses, "CBMPE_CFOA"),
    select: { id: true, segmentId: true },
  });
  const reinfRows = await db.question.findMany({
    where: reinforcementQuizWhere(cfoaSegs, statuses),
    select: { id: true, segmentId: true },
  });

  const bySeg = new Map<string, Set<string>>();
  for (const r of [...primaryRows, ...reinfRows]) {
    if (!r.segmentId) continue;
    let set = bySeg.get(r.segmentId);
    if (!set) {
      set = new Set<string>();
      bySeg.set(r.segmentId, set);
    }
    set.add(r.id);
  }

  const txtCounts = countTxtIneditas();
  const segs: Record<string, { efetiva: number; txt: number }> = {};
  const byAula = new Map<string, string[]>();

  for (const segId of cfoaSegs) {
    segs[segId] = {
      efetiva: bySeg.get(segId)?.size ?? 0,
      txt: txtCounts.get(segId) ?? 0,
    };
    const aulaId = segId.split("/").slice(0, 2).join("/");
    const list = byAula.get(aulaId) ?? [];
    list.push(segId);
    byAula.set(aulaId, list);
  }

  const grupos: Record<string, string[]> = {};
  for (const [aulaId, list] of [...byAula.entries()].sort(([a], [b]) => a.localeCompare(b))) {
    grupos[aulaId] = list.slice(0, 4);
  }

  writeFileSync(OUT_PATH, JSON.stringify({ segs, grupos }, null, 2) + "\n", "utf8");
  console.log(
    JSON.stringify({
      trechosCfoa: cfoaSegs.length,
      aulasCfoa: Object.keys(grupos).length,
      arquivo: OUT_PATH,
    }),
  );
  await db.$disconnect();
})();
