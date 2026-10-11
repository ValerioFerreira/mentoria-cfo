import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

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

// Importar adapter e client de web/node_modules
const { PrismaPg } = require(path.resolve(__dirname, "../web/node_modules/@prisma/adapter-pg"));
const { PrismaClient } = require(path.resolve(__dirname, "../web/src/generated/prisma/client"));

const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }) });

async function backup() {
  console.log("Iniciando backup completo das questões e dados relacionados...");
  const startTime = new Date();

  // 1. Extrair todas as questões com opções e relatórios
  console.log("Exportando questões com opções e relatórios...");
  const questions = await db.question.findMany({
    include: {
      options: {
        orderBy: { label: "asc" },
      },
      reports: true,
    },
    orderBy: { id: "asc" },
  });

  // 2. Extrair quiz answers (respostas de simulados/cadernos já gravadas)
  console.log("Exportando respostas de cadernos (QuizAnswer)...");
  const quizAnswers = await db.quizAnswer.findMany({
    orderBy: { id: "asc" },
  });

  // 3. Extrair sessões de quiz
  console.log("Exportando sessões de cadernos (QuizSession)...");
  const quizSessions = await db.quizSession.findMany({
    orderBy: { id: "asc" },
  });

  const totalOptions = questions.reduce((sum: number, q: any) => sum + q.options.length, 0);
  const totalReports = questions.reduce((sum: number, q: any) => sum + q.reports.length, 0);

  const timestamp = startTime.toISOString().replace(/[:.]/g, "-");
  const backupDir = path.resolve(__dirname, "../backups/questoes");
  fs.mkdirSync(backupDir, { recursive: true });

  const backupFileName = `backup_questions_${timestamp}.json`;
  const backupFilePath = path.join(backupDir, backupFileName);

  const backupData = {
    metadata: {
      exportedAt: startTime.toISOString(),
      databaseUrlSource: "web/.env",
      totalQuestions: questions.length,
      totalOptions,
      totalAnswers: quizAnswers.length,
      totalSessions: quizSessions.length,
      totalReports,
    },
    questions,
    quizAnswers,
    quizSessions,
  };

  const jsonString = JSON.stringify(backupData, null, 2);
  fs.writeFileSync(backupFilePath, jsonString, "utf-8");

  // Calcular checksum SHA-256
  const sha256 = crypto.createHash("sha256").update(jsonString, "utf-8").digest("hex");
  const fileStats = fs.statSync(backupFilePath);

  // Criar manifesto
  const manifest = {
    backupFileName,
    backupFilePath: `backups/questoes/${backupFileName}`,
    fileSizeBytes: fileStats.size,
    sha256,
    exportedAt: startTime.toISOString(),
    completedAt: new Date().toISOString(),
    recordCounts: {
      questions: questions.length,
      options: totalOptions,
      quizAnswers: quizAnswers.length,
      quizSessions: quizSessions.length,
      reports: totalReports,
    },
    status: "VERIFIED_CREATED",
    restorationGuide: "Para restaurar, execute: npx tsx scripts/restore_backup.ts backups/questoes/" + backupFileName,
  };

  const manifestPath = path.join(backupDir, "manifest.json");
  fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2), "utf-8");

  console.log("Backup concluído com sucesso!");
  console.log(`Arquivo: ${backupFilePath} (${(fileStats.size / (1024 * 1024)).toFixed(2)} MB)`);
  console.log(`SHA-256: ${sha256}`);
  console.log(`Manifesto salvo em: ${manifestPath}`);
  console.log(`Registros: ${questions.length} questões, ${totalOptions} opções, ${quizAnswers.length} respostas, ${quizSessions.length} sessões`);
}

backup()
  .catch((e) => {
    console.error("Erro ao gerar backup:", e);
    process.exit(1);
  })
  .finally(() => db.$disconnect());
