// Grava no banco um lote de questões extraído por pipeline/questoes/importar.py (não rode à mão:
// use o importador). Especificação: pipeline/questoes/EXTRACAO.md.
//
//   npx tsx scripts/questoes-sync.ts <lote.jsonl> [--remoto] [--limpar-estrategia]
//
// Banco local: DATABASE_URL de web/.env. Com --remoto: REMOTE_DATABASE_URL de web/.env.remote
// (arquivo fora do git; o dono coloca ali a URL do Neon de produção).
//
// Regras: upsert por id ("tec_<número TEC>"). Respostas antigas são preservadas (guardam o rótulo).
// Questão com classifiedBy = MANUAL mantém trecho/assunto/status. Questão anulada vira RETIRED.
// Imprime na última linha um JSON com o resumo (lido pelo importador).
import "dotenv/config";
import { readFileSync, existsSync } from "node:fs";
import { resolve, dirname } from "node:path";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient, type QuestionStatus, type QuestionKind } from "../src/generated/prisma/client";

type OptionRow = { label: string; text: string; isCorrect: boolean };
type QuestionRow = {
  type: "question";
  id: string;
  externalId: string;
  subjectId: string;
  aulaId: string;
  segmentId: string;
  editalItemId: string | null;
  topic: string | null;
  support: string | null;
  statement: string;
  explanation: string;
  difficulty: number;
  pattern: string;
  status: QuestionStatus;
  batch: string;
  banca: string;
  kind: QuestionKind;
  tecMateria: string;
  tecAssunto: string;
  orgao: string | null;
  cargo: string | null;
  ano: number | null;
  sourceFile: string;
  contentHash: string;
  classifyScore: number | null;
  classifyNote: string | null;
  options: OptionRow[];
};
type ImageRow = { type: "image"; id: string; path: string; width: number; height: number };
// questão anulada, fora do edital ou sem classificação: se já existir no banco, sai de circulação
type RetireRow = { type: "retire"; id: string };

const args = process.argv.slice(2);
const file = args.find((a) => !a.startsWith("--"));
const remote = args.includes("--remoto");
const purgeLegacy = args.includes("--limpar-estrategia");

function cleanUrl(url: string): string {
  return url.replace(/([?&])pgbouncer=true(&|$)/, (_, p1, p2) => (p2 ? p1 : ""));
}

function remoteUrl(): string {
  const envFile = resolve(__dirname, "..", ".env.remote");
  if (!existsSync(envFile)) throw new Error("web/.env.remote não existe (coloque REMOTE_DATABASE_URL=... nele)");
  for (const line of readFileSync(envFile, "utf8").split(/\r?\n/)) {
    const m = line.match(/^\s*REMOTE_DATABASE_URL\s*=\s*"?([^"]+)"?\s*$/);
    if (m) return m[1];
  }
  throw new Error("REMOTE_DATABASE_URL ausente em web/.env.remote");
}

const url = cleanUrl(remote ? remoteUrl() : process.env.DATABASE_URL || "");
if (!url) throw new Error("DATABASE_URL vazio");
const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: url }) });

function chunk<T>(xs: T[], n: number): T[][] {
  const out: T[][] = [];
  for (let i = 0; i < xs.length; i += n) out.push(xs.slice(i, i + n));
  return out;
}

async function purge(): Promise<{ questions: number; answers: number; sessions: number }> {
  const answers = await db.$executeRawUnsafe(`DELETE FROM "QuizAnswer" WHERE "questionId" NOT LIKE 'tec\\_%'`);
  await db.$executeRawUnsafe(`DELETE FROM "QuestionReport" WHERE "questionId" NOT LIKE 'tec\\_%'`);
  await db.$executeRawUnsafe(`DELETE FROM "QuestionOption" WHERE "questionId" NOT LIKE 'tec\\_%'`);
  const questions = await db.$executeRawUnsafe(`DELETE FROM "Question" WHERE "id" NOT LIKE 'tec\\_%'`);
  const sessions = await db.$executeRawUnsafe(
    `DELETE FROM "QuizSession" s WHERE NOT EXISTS (SELECT 1 FROM "QuizAnswer" a WHERE a."sessionId" = s."id")`,
  );
  return { questions, answers, sessions };
}

async function main() {
  const summary = {
    target: remote ? "remoto" : "local",
    created: 0,
    updated: 0,
    unchanged: 0,
    keptManual: 0,
    retired: 0,
    skippedMissingSegment: [] as string[],
    images: { created: 0, existing: 0 },
    purged: null as null | { questions: number; answers: number; sessions: number },
  };
  if (purgeLegacy) summary.purged = await purge();
  if (!file) {
    console.log(JSON.stringify(summary));
    return;
  }
  const baseDir = dirname(resolve(file));
  const rows = readFileSync(file, "utf8")
    .split(/\r?\n/)
    .filter((l) => l.trim())
    .map((l) => JSON.parse(l) as QuestionRow | ImageRow | RetireRow);
  const questions = rows.filter((r): r is QuestionRow => r.type === "question");
  const images = rows.filter((r): r is ImageRow => r.type === "image");
  const retire = rows.filter((r): r is RetireRow => r.type === "retire").map((r) => r.id);

  // Figuras primeiro (as questões apontam para /q-img/<id>)
  const imgIds = images.map((i) => i.id);
  const have = new Set<string>();
  for (const c of chunk(imgIds, 1000)) {
    for (const r of await db.questionImage.findMany({ where: { id: { in: c } }, select: { id: true } })) have.add(r.id);
  }
  const missing = images.filter((i) => !have.has(i.id));
  summary.images.existing = images.length - missing.length;
  let batch: { id: string; data: Uint8Array<ArrayBuffer>; width: number; height: number }[] = [];
  let size = 0;
  const flush = async () => {
    if (!batch.length) return;
    await db.questionImage.createMany({ data: batch, skipDuplicates: true });
    summary.images.created += batch.length;
    batch = [];
    size = 0;
  };
  for (const im of missing) {
    const buf = readFileSync(resolve(baseDir, im.path));
    batch.push({ id: im.id, data: new Uint8Array(buf), width: im.width, height: im.height });
    size += buf.length;
    if (size > 4_000_000 || batch.length >= 200) await flush();
  }
  await flush();

  // Trechos e itens do edital existentes neste banco
  const segIds = new Set((await db.segment.findMany({ select: { id: true } })).map((s) => s.id));
  const editalIds = new Set((await db.editalItem.findMany({ select: { id: true } })).map((e) => e.id));

  const existing = new Map<string, { classifiedBy: string; status: QuestionStatus; contentHash: string | null; segmentId: string; editalItemId: string | null; batch: string | null }>();
  for (const c of chunk(questions.map((q) => q.id), 1000)) {
    for (const r of await db.question.findMany({
      where: { id: { in: c } },
      select: { id: true, classifiedBy: true, status: true, contentHash: true, segmentId: true, editalItemId: true, batch: true },
    })) existing.set(r.id, r);
  }

  const now = new Date();
  const toCreate: QuestionRow[] = [];
  for (const q of questions) {
    if (!segIds.has(q.segmentId)) {
      summary.skippedMissingSegment.push(q.id);
      continue;
    }
    const editalItemId = q.editalItemId && editalIds.has(q.editalItemId) ? q.editalItemId : null;
    const ex = existing.get(q.id);
    if (!ex) {
      toCreate.push({ ...q, editalItemId });
      continue;
    }
    const manual = ex.classifiedBy === "MANUAL";
    const lockedStatus = ex.status === "FLAGGED" || ex.status === "RETIRED";
    let status: QuestionStatus = q.status;
    if (q.status !== "RETIRED" && (manual || lockedStatus)) status = ex.status;
    if (q.status === "RETIRED" && ex.status !== "RETIRED") summary.retired++;
    const sameContent = ex.contentHash === q.contentHash;
    const sameClass = manual || (ex.segmentId === q.segmentId && ex.editalItemId === editalItemId);
    if (sameContent && sameClass && ex.status === status) {
      summary.unchanged++;
      continue;
    }
    if (manual) summary.keptManual++;
    await db.$transaction(async (tx) => {
      await tx.question.update({
        where: { id: q.id },
        data: {
          externalId: q.externalId,
          ...(manual
            ? {}
            : {
                subjectId: q.subjectId,
                aulaId: q.aulaId,
                segmentId: q.segmentId,
                editalItemId,
                classifyScore: q.classifyScore,
                classifyNote: q.classifyNote,
              }),
          topic: q.topic,
          support: q.support,
          statement: q.statement,
          explanation: q.explanation,
          pattern: q.pattern,
          status,
          batch: q.batch,
          banca: q.banca,
          kind: q.kind,
          tecMateria: q.tecMateria,
          tecAssunto: q.tecAssunto,
          orgao: q.orgao,
          cargo: q.cargo,
          ano: q.ano,
          sourceFile: q.sourceFile,
          contentHash: q.contentHash,
          importedAt: now,
        },
      });
      if (!sameContent) {
        await tx.questionOption.deleteMany({ where: { questionId: q.id } });
        await tx.questionOption.createMany({ data: q.options.map((o) => ({ ...o, questionId: q.id })) });
      }
    });
    summary.updated++;
  }

  for (const c of chunk(toCreate, 300)) {
    await db.$transaction([
      db.question.createMany({
        data: c.map((q) => ({
          id: q.id,
          externalId: q.externalId,
          subjectId: q.subjectId,
          aulaId: q.aulaId,
          segmentId: q.segmentId,
          editalItemId: q.editalItemId,
          topic: q.topic,
          support: q.support,
          statement: q.statement,
          explanation: q.explanation,
          difficulty: q.difficulty,
          pattern: q.pattern,
          status: q.status,
          batch: q.batch,
          banca: q.banca,
          kind: q.kind,
          tecMateria: q.tecMateria,
          tecAssunto: q.tecAssunto,
          orgao: q.orgao,
          cargo: q.cargo,
          ano: q.ano,
          sourceFile: q.sourceFile,
          contentHash: q.contentHash,
          classifyScore: q.classifyScore,
          classifyNote: q.classifyNote,
          importedAt: now,
        })),
        skipDuplicates: true,
      }),
      db.questionOption.createMany({
        data: c.flatMap((q) => q.options.map((o) => ({ ...o, questionId: q.id }))),
        skipDuplicates: true,
      }),
    ]);
    summary.created += c.length;
  }
  for (const c of chunk(retire, 1000)) {
    const r = await db.question.updateMany({ where: { id: { in: c }, status: { not: "RETIRED" } }, data: { status: "RETIRED" } });
    summary.retired += r.count;
  }
  console.log(JSON.stringify(summary));
}

main()
  .catch((e) => {
    console.error(e);
    process.exitCode = 1;
  })
  .finally(() => db.$disconnect());
