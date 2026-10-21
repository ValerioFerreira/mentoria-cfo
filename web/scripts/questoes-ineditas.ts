// Grava no banco as questões INÉDITAS MentorIA (padrão Cebraspe, certo/errado), escritas para os assuntos do
// edital do PCPE que ainda não têm questão real. Fonte: content/questoes/ineditas/*.txt (veja
// pipeline/questoes/ineditas.py). São provisórias: quando as questões reais do TecConcursos chegarem, aposente-as.
//
//   pipeline/.venv/Scripts/python pipeline/questoes/ineditas.py --json lote.json     (gera o lote certo/errado)
//   pipeline/.venv/Scripts/python pipeline/questoes/ineditas_mc.py --json lote-mc.json   (lote de múltipla escolha, o formato da prova)
//   npx tsx scripts/questoes-ineditas.ts lote.json                  # grava no banco local (web/.env)
//   npx tsx scripts/questoes-ineditas.ts lote.json --remoto         # grava na produção (web/.env.remote)
//   npx tsx scripts/questoes-ineditas.ts lote.json --retirar-ausentes   # grava e aposenta (RETIRED) as inéditas do mesmo batch que não estão mais no lote (texto editado = id novo)
//   npx tsx scripts/questoes-ineditas.ts --contar [--remoto]        # só leitura: inéditas por assunto
//   npx tsx scripts/questoes-ineditas.ts --aposentar [--minimo 8] [--simular] [--remoto]
//        # inédita de um TRECHO que já tem ao menos N questões reais aprovadas das bancas do caderno (Cebraspe e AOCP) vira RETIRED; --simular só lista
//
// Marcação no banco: banca = "Inédita MentorIA", batch = "mentoria-inedita-AAAA-MM-DD", id "mentoria_<disciplina>_NNN_<hash>",
// externalId nulo (nunca mexe nas questões "tec_*") e classifiedBy = MANUAL (a reclassificação do importador não as toca).
// Para listar: select * from "Question" where banca = 'Inédita MentorIA'.
import "dotenv/config";
import { readFileSync, existsSync } from "node:fs";
import { resolve } from "node:path";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";

import { AOCP_BANCAS, CEBRASPE_BANCAS } from "../src/lib/quiz/banca";

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
  statement: string; answer?: "C" | "E"; explanation: string; banca: string; batch: string;
  kind?: "MULTIPLA_ESCOLHA" | "CERTO_ERRADO"; // padrão: CERTO_ERRADO (ineditas.py); múltipla escolha vem de ineditas_mc.py
  options?: { label: string; text: string; isCorrect: boolean }[];
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

async function aposentar(min: number, simular: boolean) {
  // Conta só as reais que o caderno do PCPE realmente usa (Cebraspe e AOCP, ver contestBancas) e por TRECHO,
  // que é o recorte do caderno das atividades; outras bancas só servem ao treino livre e não substituem a inédita.
  const usadas = [...CEBRASPE_BANCAS, ...AOCP_BANCAS];
  const segs = await db.question.groupBy({ by: ["segmentId"], where: { banca: BANCA, status: "APPROVED" } });
  let retired = 0;
  for (const sg of segs) {
    const reais = await db.question.count({ where: { segmentId: sg.segmentId, status: "APPROVED", banca: { in: usadas } } });
    if (reais >= min) {
      const where = { banca: BANCA, status: "APPROVED" as const, segmentId: sg.segmentId };
      const n = simular ? await db.question.count({ where }) : (await db.question.updateMany({ where, data: { status: "RETIRED" } })).count;
      retired += n;
      console.log(`${sg.segmentId}: ${reais} reais (Cebraspe/AOCP) → ${n} inéditas ${simular ? "seriam aposentadas" : "aposentadas"}`);
    }
  }
  console.log(simular ? "seriam aposentadas:" : "aposentadas:", retired);
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
      status: "APPROVED" as const, batch: r.batch, banca: r.banca, kind: (r.kind ?? "CERTO_ERRADO") as "MULTIPLA_ESCOLHA" | "CERTO_ERRADO",
      tecMateria: "Inédita MentorIA", tecAssunto: editalItemId ? titles.get(editalItemId) ?? null : null,
      classifiedBy: "MANUAL" as const, importedAt: new Date(),
    };
    const exists = await db.question.findUnique({ where: { id: r.id }, select: { id: true } });
    if (exists) await db.question.update({ where: { id: r.id }, data });
    else await db.question.create({ data: { id: r.id, ...data } });
    const opts = r.options ?? ([["C", "Certo"], ["E", "Errado"]] as const).map(([label, text]) => ({ label, text, isCorrect: r.answer === label }));
    for (const o of opts) {
      await db.questionOption.upsert({
        where: { questionId_label: { questionId: r.id, label: o.label } },
        create: { questionId: r.id, label: o.label, text: o.text, isCorrect: o.isCorrect },
        update: { text: o.text, isCorrect: o.isCorrect },
      });
    }
    if (exists) updated++; else created++;
  }
  let retired = 0;
  if (args.includes("--retirar-ausentes")) {
    const r = await db.question.updateMany({ where: { banca: BANCA, batch: { in: [...new Set(rows.map((x) => x.batch))] }, id: { notIn: rows.map((x) => x.id) }, status: "APPROVED" }, data: { status: "RETIRED" } });
    retired = r.count;
  }
  console.log(JSON.stringify({ target: remote ? "remoto" : "local", total: rows.length, created, updated, retired, skipped }));
}

(async () => {
  if (args.includes("--contar")) await contar();
  else if (args.includes("--aposentar")) await aposentar(Number(args[args.indexOf("--minimo") + 1]) || 8, args.includes("--simular"));
  else if (file) await gravar(JSON.parse(readFileSync(file, "utf8")) as Row[]);
  else throw new Error("uso: questoes-ineditas.ts <lote.json> | --contar | --aposentar [--minimo N]  [--remoto]");
  await db.$disconnect();
})();
