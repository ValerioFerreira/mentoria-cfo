import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Ler DATABASE_URL diretamente de web/.env
const envPath = path.resolve(__dirname, "../web/.env");
if (fs.existsSync(envPath)) {
  const envContent = fs.readFileSync(envPath, "utf-8");
  for (const line of envContent.split("\n")) {
    const match = line.match(/^\s*([\w.-]+)\s*=\s*(.*)?\s*$/);
    if (match) {
      const key = match[1];
      let value = match[2] || "";
      if (value.startsWith('"') && value.endsWith('"')) value = value.slice(1, -1);
      else if (value.startsWith("'") && value.endsWith("'")) value = value.slice(1, -1);
      process.env[key] = value.trim();
    }
  }
}

if (!process.env.DATABASE_URL) {
  throw new Error("DATABASE_URL não encontrada em " + envPath);
}

const { PrismaPg } = require(path.resolve(__dirname, "../web/node_modules/@prisma/adapter-pg"));
const { PrismaClient } = require(path.resolve(__dirname, "../web/src/generated/prisma/client"));

const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }) });

async function ingestPmpe() {
  console.log("==================================================");
  console.log("INICIANDO INGESTÃO INCREMENTAL DE QUESTÕES PMPE");
  console.log("==================================================");

  const datasetPath = path.resolve(__dirname, "../pipeline/.cache/pmpe_extracted_questions.json");
  if (!fs.existsSync(datasetPath)) {
    throw new Error("Dataset PMPE não encontrado: " + datasetPath);
  }

  const rawQuestions = JSON.parse(fs.readFileSync(datasetPath, "utf-8"));
  console.log(`Carregadas ${rawQuestions.length} questões brutas extraídas.`);

  // 1. Obter IDs já existentes no banco para idempotência absoluta
  const existingQuestions = await db.question.findMany({
    select: { id: true },
  });
  const existingIds = new Set(existingQuestions.map((q: any) => q.id));
  console.log(`Questões atualmente no banco: ${existingIds.size}`);

  const toInsert = rawQuestions.filter((q: any) => !existingIds.has(q.id));
  console.log(`Novas questões únicas a inserir: ${toInsert.length}`);

  if (toInsert.length === 0) {
    console.log("Todas as questões já estão cadastradas no banco.");
    return;
  }

  // 2. Inserir em lotes
  const batchSize = 100;
  let insertedQuestions = 0;
  let insertedOptions = 0;

  for (let i = 0; i < toInsert.length; i += batchSize) {
    const batch = toInsert.slice(i, i + batchSize);

    // Preparar question rows
    const questionRows = batch.map((q: any) => ({
      id: q.id,
      subjectId: q.subjectId,
      aulaId: q.aulaId,
      segmentId: q.segmentId,
      topic: q.topic,
      statement: q.statement,
      explanation: q.explanation,
      difficulty: q.difficulty || 2,
      pattern: q.pattern || "AOCP",
      banca: q.banca || "AOCP",
      status: q.status || "APPROVED",
      batch: "pmpe-estrategia-import",
    }));

    await db.question.createMany({
      data: questionRows,
      skipDuplicates: true,
    });
    insertedQuestions += questionRows.length;

    // Preparar option rows
    const optionRows: any[] = [];
    for (const q of batch) {
      if (Array.isArray(q.options)) {
        for (let idx = 0; idx < q.options.length; idx++) {
          const opt = q.options[idx];
          optionRows.push({
            id: `${q.id}_opt_${idx}`,
            questionId: q.id,
            label: opt.label,
            text: opt.text,
            isCorrect: Boolean(opt.isCorrect),
          });
        }
      }
    }

    if (optionRows.length > 0) {
      await db.questionOption.createMany({
        data: optionRows,
        skipDuplicates: true,
      });
      insertedOptions += optionRows.length;
    }

    process.stdout.write(`Progresso: ${Math.min(i + batchSize, toInsert.length)} / ${toInsert.length} questões inseridas...\r`);
  }

  console.log(`\n\n✓ Ingestão concluída com sucesso!`);
  console.log(`  - Questões adicionadas: ${insertedQuestions}`);
  console.log(`  - Opções vinculadas: ${insertedOptions}`);

  const totalNow = await db.question.count();
  const totalBancaAocp = await db.question.count({
    where: { banca: { in: ["AOCP", "Instituto AOCP", "INSTITUTO AOCP"] } },
  });
  console.log(`Total geral de questões no acervo: ${totalNow}`);
  console.log(`Total geral com banca AOCP: ${totalBancaAocp}`);
}

ingestPmpe()
  .catch((err) => {
    console.error("Erro na ingestão:", err);
    process.exit(1);
  })
  .finally(async () => {
    await db.$disconnect();
  });
