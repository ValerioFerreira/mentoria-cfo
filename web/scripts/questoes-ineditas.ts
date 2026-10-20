// Grava no banco as questões INÉDITAS MentorIA (padrão Cebraspe, certo/errado), escritas para os assuntos do
// edital do PCPE que ainda não têm questão real. Fonte: content/questoes/ineditas/*.txt (veja
// pipeline/questoes/ineditas.py). São provisórias: quando as questões reais do TecConcursos chegarem, aposente-as.
//
//   pipeline/.venv/Scripts/python pipeline/questoes/ineditas.py --json lote.json     (gera o lote)
//   npx tsx scripts/questoes-ineditas.ts lote.json                  # grava no banco local (web/.env)
//   npx tsx scripts/questoes-ineditas.ts lote.json --remoto         # grava na produção (web/.env.remote)
//   npx tsx scripts/questoes-ineditas.ts --contar [--remoto]        # só leitura: inéditas por assunto
//   npx tsx scripts/questoes-ineditas.ts --aposentar [--minimo 8] [--remoto]
//        # inédita de assunto que já tem ao menos N questões reais aprovadas (de outra origem) vira RETIRED
//
// Marcação no banco: banca = "Inédita MentorIA", batch = "mentoria-inedita-AAAA-MM-DD", id "mentoria_<disciplina>_NNN_<hash>",
// externalId nulo (nunca mexe nas questões "tec_*") e classifiedBy = MANUAL (a reclassificação do importador não as toca).
// Para listar: select * from "Question" where banca = 'Inédita MentorIA'.
import "dotenv/config";
import { readFileSync, existsSync } from "node:fs";
import { resolve } from "node:path";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";

const BANCA = "Inédita MentorIA";
const args = process.argv.slice(2);
const remote = args.includes("--remoto");
const file = args.find((a) => !a.startsWith("--") && a.endsWith(".json"));

function remoteUrl(): string {
  const envFile = resolve(__dirname, "..", ".env.remote");
  if (!existsSync(envFile)) throw new Error("web/.env.remote não existe");
  for (const line of readFileSync(envFile, "utf8").split(/\r?\n/)) {
    const m = line.match(/^\s*REMOTE_DATABASE_URL\s*=\s*"?([^"]+)"?\s*$/);
    if (m) return m[1];
  }
  throw new Error("REMOTE_DATABASE_URL ausente em web/.env.remote");
}
const clean = (u: string) => u.replace(/([?&])pgbouncer=true(&|$)/, (_, a, b) => (b ? a : ""));
const url = clean(remote ? remoteUrl() : process.env.DATABASE_URL || "");
if (!url) throw new Error("DATABASE_URL vazio");
const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: url }) });

type Row = {
  id: string; subjectId: string; aulaId: string; segmentId: string; editalItemId: string | null;
  statement: string; answer: "C" | "E"; explanation: string; banca: string; batch: string;
};

async function contar() {
  const rows = await db.question.groupBy({ by: ["editalItemId", "status"], where: { banca: BANCA }, _count: true });
  const by = new Map<string, Record<string, number>>();
  for (const r of rows) by.set(r.editalItemId ?? "(sem assunto)", { ...(by.get(r.editalItemId ?? "(sem assunto)") ?? {}), [r.status]: r._count });
  let total = 0;
  for (const [k, v] of [...by.entries()].sort()) {
    console.log(k.padEnd(48), JSON.stringify(v));
    total += Object.values(v).reduce((a, b) => a + b, 0);
  }
  console.log("total de inéditas:", total);
}

async function aposentar(min: number) {
  const items = await db.question.groupBy({ by: ["editalItemId"], where: { banca: BANCA, status: "APPROVED", editalItemId: { not: null } } });
  let retired = 0;
  for (const it of items) {
    const reais = await db.question.count({ where: { editalItemId: it.editalItemId, status: "APPROVED", banca: { not: BANCA } } });
    if (reais >= min) {
      const r = await db.question.updateMany({ where: { banca: BANCA, status: "APPROVED", editalItemId: it.editalItemId }, data: { status: "RETIRED" } });
      retired += r.count;
      console.log(`${it.editalItemId}: ${reais} reais → ${r.count} inéditas aposentadas`);
    }
  }
  console.log("aposentadas:", retired);
}

async function gravar(rows: Row[]) {
  const itemIds = new Set((await db.editalItem.findMany({ select: { id: true, title: true } })).map((i) => i.id));
  const titles = new Map((await db.editalItem.findMany({ select: { id: true, title: true } })).map((i) => [i.id, i.title]));
  const segIds = new Set((await db.segment.findMany({ where: { id: { in: rows.map((r) => r.segmentId) } }, select: { id: true } })).map((s) => s.id));
  let created = 0, updated = 0;
  const skipped: string[] = [];
  for (const r of rows) {
    if (!segIds.has(r.segmentId)) { skipped.push(`${r.id}: trecho ${r.segmentId} inexistente no banco`); continue; }
    const editalItemId = r.editalItemId && itemIds.has(r.editalItemId) ? r.editalItemId : null;
    const data = {
      subjectId: r.subjectId, aulaId: r.aulaId, segmentId: r.segmentId, editalItemId,
      topic: editalItemId ? titles.get(editalItemId) ?? null : null,
      support: null, statement: r.statement, explanation: r.explanation, difficulty: 2, pattern: "CEBRASPE",
      status: "APPROVED" as const, batch: r.batch, banca: r.banca, kind: "CERTO_ERRADO" as const,
      tecMateria: "Inédita MentorIA", tecAssunto: editalItemId ? titles.get(editalItemId) ?? null : null,
      classifiedBy: "MANUAL" as const, importedAt: new Date(),
    };
    const exists = await db.question.findUnique({ where: { id: r.id }, select: { id: true } });
    if (exists) await db.question.update({ where: { id: r.id }, data });
    else await db.question.create({ data: { id: r.id, ...data } });
    for (const [label, text] of [["C", "Certo"], ["E", "Errado"]] as const) {
      await db.questionOption.upsert({
        where: { questionId_label: { questionId: r.id, label } },
        create: { questionId: r.id, label, text, isCorrect: r.answer === label },
        update: { text, isCorrect: r.answer === label },
      });
    }
    if (exists) updated++; else created++;
  }
  console.log(JSON.stringify({ target: remote ? "remoto" : "local", total: rows.length, created, updated, skipped }));
}

(async () => {
  if (args.includes("--contar")) await contar();
  else if (args.includes("--aposentar")) await aposentar(Number(args[args.indexOf("--minimo") + 1]) || 8);
  else if (file) await gravar(JSON.parse(readFileSync(file, "utf8")) as Row[]);
  else throw new Error("uso: questoes-ineditas.ts <lote.json> | --contar | --aposentar [--minimo N]  [--remoto]");
  await db.$disconnect();
})();
