import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const envPath = path.resolve(__dirname, "../web/.env");
if (fs.existsSync(envPath)) {
  for (const line of fs.readFileSync(envPath, "utf-8").split("\n")) {
    const m = line.match(/^\s*([\w.-]+)\s*=\s*(.*)?\s*$/);
    if (m) {
      let val = (m[2] || "").trim();
      if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) {
        val = val.slice(1, -1);
      }
      process.env[m[1]] = val;
    }
  }
}

const { PrismaPg } = require(path.resolve(__dirname, "../web/node_modules/@prisma/adapter-pg"));
const { PrismaClient } = require(path.resolve(__dirname, "../web/src/generated/prisma/client"));

const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }) });

function chunk<T>(arr: T[], size: number): T[][] {
  const res: T[][] = [];
  for (let i = 0; i < arr.length; i += size) res.push(arr.slice(i, i + size));
  return res;
}

async function run() {
  console.log("[Reset & Seed] Limpando antigas questões do Estratégia...");
  await db.$executeRawUnsafe(`
    DELETE FROM "QuizAnswer" WHERE "questionId" LIKE 'cbmpe_%' OR "questionId" LIKE 'pmpe_%';
    DELETE FROM "QuestionReport" WHERE "questionId" LIKE 'cbmpe_%' OR "questionId" LIKE 'pmpe_%';
    DELETE FROM "QuestionOption" WHERE "questionId" LIKE 'cbmpe_%' OR "questionId" LIKE 'pmpe_%';
    DELETE FROM "Question" WHERE "id" LIKE 'cbmpe_%' OR "id" LIKE 'pmpe_%';
  `);

  const estPath = path.resolve(__dirname, "../content/questoes_estrategia_cbmpe_pmpe.json");
  const estQuestions: any[] = JSON.parse(fs.readFileSync(estPath, "utf-8"));
  console.log(`[Reset & Seed] Inserindo ${estQuestions.length} questões limpas e auditadas...`);

  const qRows = estQuestions.map((q) => {
    const aulaId = q.subjectId === "legislacoes-pe" ? "legislacoes-pe/a01" : `${q.subjectId}/a00`;
    const segmentId = `${aulaId}/s01`;
    return {
      id: q.id,
      subjectId: q.subjectId,
      aulaId,
      segmentId,
      topic: q.topic || null,
      statement: q.statement,
      explanation: q.explanation,
      difficulty: q.difficulty || 2,
      pattern: q.pattern || q.banca || "AOCP",
      banca: q.banca || "AOCP",
      status: q.status || "APPROVED",
      batch: "estrategia-auditado-2026",
    };
  });

  const optRows = estQuestions.flatMap((q) =>
    (q.options || []).map((opt: any, idx: number) => ({
      id: `${q.id}_opt_${idx}`,
      questionId: q.id,
      label: opt.label,
      text: opt.text,
      isCorrect: Boolean(opt.isCorrect),
    }))
  );

  for (const c of chunk(qRows, 500)) await db.question.createMany({ data: c, skipDuplicates: true });
  for (const c of chunk(optRows, 1000)) await db.questionOption.createMany({ data: c, skipDuplicates: true });

  console.log("[Reset & Seed] Ingestão concluída com sucesso!");
}

run().finally(() => db.$disconnect());
