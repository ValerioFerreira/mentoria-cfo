import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
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

async function migrateQuestions() {
  console.log("==================================================");
  console.log("INICIANDO MIGRAÇÃO OFICIAL DO BANCO DE QUESTÕES");
  console.log("Fonte oficial: docs/questoes (PDFs TecConcursos)");
  console.log("==================================================");

  // 1. CHECAGEM DE SEGURANÇA: Verificar existência e integridade do backup prévio
  const backupDir = path.resolve(__dirname, "../backups/questoes");
  const manifestPath = path.join(backupDir, "manifest.json");

  if (!fs.existsSync(manifestPath)) {
    throw new Error("BLOQUEIO DE SEGURANÇA: Manifesto de backup não encontrado em " + manifestPath);
  }

  const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf-8"));
  const backupFile = path.join(backupDir, manifest.backupFileName);

  if (!fs.existsSync(backupFile)) {
    throw new Error("BLOQUEIO DE SEGURANÇA: Arquivo de backup não encontrado em " + backupFile);
  }

  const fileBytes = fs.readFileSync(backupFile);
  const hash = crypto.createHash("sha256").update(fileBytes).digest("hex");
  if (hash !== manifest.sha256) {
    throw new Error("BLOQUEIO DE SEGURANÇA: Checksum SHA-256 do backup não confere com o manifesto!");
  }
  console.log("✓ Verificação de segurança aprovada: Backup verificado e íntegro!");

  // 2. Carregar dataset de questões gerado a partir de docs/questoes
  const datasetPath = path.resolve(__dirname, "../pipeline/.cache/imported_questions.json");
  if (!fs.existsSync(datasetPath)) {
    throw new Error("Dataset de questões não encontrado em " + datasetPath);
  }

  const newQuestions = JSON.parse(fs.readFileSync(datasetPath, "utf-8"));
  console.log(`✓ Dataset carregado: ${newQuestions.length} questões prontas para importação.`);

  // 3. Remover com segurança as questões antigas do banco
  console.log("\nRemovendo registros antigos com preservação da integridade referencial...");

  // Excluir respostas de testes anteriores (já salvas no backup de segurança)
  const delAnswers = await db.quizAnswer.deleteMany({});
  console.log(`  - Respostas antigas limpas: ${delAnswers.count}`);

  const delReports = await db.questionReport.deleteMany({});
  console.log(`  - Relatórios de questões limpos: ${delReports.count}`);

  const delOptions = await db.questionOption.deleteMany({});
  console.log(`  - Opções antigas limpas: ${delOptions.count}`);

  const delQuestions = await db.question.deleteMany({});
  console.log(`  - Questões antigas deletadas: ${delQuestions.count}`);

  // 4. Inserir as novas questões em lotes
  console.log("\nInserindo novas questões no banco de dados...");
  const batchSize = 100;
  const questionRows = newQuestions.map((q: any) => ({
    id: q.id,
    subjectId: q.subjectId,
    aulaId: q.aulaId,
    segmentId: q.segmentId,
    topic: q.topic,
    statement: q.statement,
    explanation: q.explanation,
    difficulty: q.difficulty,
    pattern: q.pattern,
    status: q.status,
    batch: "tecconcursos-migracao-oficial",
  }));

  for (let i = 0; i < questionRows.length; i += batchSize) {
    const chunk = questionRows.slice(i, i + batchSize);
    await db.question.createMany({ data: chunk });
    console.log(`  Inseridas ${Math.min(i + batchSize, questionRows.length)} / ${questionRows.length} questões...`);
  }

  // 5. Inserir as opções das novas questões
  console.log("\nInserindo opções das questões...");
  const optionRows: any[] = [];
  for (const q of newQuestions) {
    for (const opt of q.options) {
      optionRows.push({
        questionId: q.id,
        label: opt.label,
        text: opt.text,
        isCorrect: opt.isCorrect,
      });
    }
  }

  for (let i = 0; i < optionRows.length; i += 500) {
    const chunk = optionRows.slice(i, i + 500);
    await db.questionOption.createMany({ data: chunk });
  }
  console.log(`✓ ${optionRows.length} opções inseridas com sucesso.`);

  // 6. Verificação final pós-migração
  const finalQ = await db.question.count();
  const finalOpt = await db.questionOption.count();
  const finalApproved = await db.question.count({ where: { status: "APPROVED" } });
  const finalRetired = await db.question.count({ where: { status: "RETIRED" } });

  console.log("\n==================================================");
  console.log("MIGRAÇÃO CONCLUÍDA COM SUCESSO!");
  console.log(`Total de Questões no Banco: ${finalQ}`);
  console.log(`  - Aprovadas (Ativas nos Cadernos): ${finalApproved}`);
  console.log(`  - Aposentadas (Anuladas pela Banca): ${finalRetired}`);
  console.log(`Total de Opções no Banco: ${finalOpt}`);
  console.log("==================================================");
}

migrateQuestions()
  .catch((e) => {
    console.error("ERRO CRÍTICO NA MIGRAÇÃO:", e);
    process.exit(1);
  })
  .finally(() => db.$disconnect());
