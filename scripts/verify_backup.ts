import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

async function verifyBackup() {
  console.log("Iniciando verificação de integridade do backup...");

  const backupDir = path.resolve(__dirname, "../backups/questoes");
  const manifestPath = path.join(backupDir, "manifest.json");

  if (!fs.existsSync(manifestPath)) {
    throw new Error(`Manifesto não encontrado em ${manifestPath}`);
  }

  const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf-8"));
  console.log("Manifesto carregado:", manifest.backupFileName);

  const backupFilePath = path.join(backupDir, manifest.backupFileName);
  if (!fs.existsSync(backupFilePath)) {
    throw new Error(`Arquivo de backup não encontrado em ${backupFilePath}`);
  }

  // 1. Verificar hash SHA-256
  console.log("Calculando SHA-256 do arquivo de backup...");
  const fileContent = fs.readFileSync(backupFilePath);
  const actualHash = crypto.createHash("sha256").update(fileContent).digest("hex");

  if (actualHash !== manifest.sha256) {
    throw new Error(`FALHA DE INTEGRIDADE: SHA-256 não confere!\nEsperado: ${manifest.sha256}\nObtido:   ${actualHash}`);
  }
  console.log("✓ SHA-256 verificado com sucesso:", actualHash);

  // 2. Verificar parsing JSON
  console.log("Analisando estrutura JSON do backup...");
  const data = JSON.parse(fileContent.toString("utf-8"));

  if (!data.metadata || !Array.isArray(data.questions) || !Array.isArray(data.quizAnswers) || !Array.isArray(data.quizSessions)) {
    throw new Error("FALHA DE ESTRUTURA: Campos obrigatórios (metadata, questions, quizAnswers, quizSessions) ausentes!");
  }

  // 3. Verificar contagens
  const qCount = data.questions.length;
  let optCount = 0;
  for (const q of data.questions) {
    if (!q.id || !q.statement || !Array.isArray(q.options)) {
      throw new Error(`Questão malformada encontrada: ID=${q.id}`);
    }
    optCount += q.options.length;
  }

  if (qCount !== manifest.recordCounts.questions) {
    throw new Error(`Divergência de questões: Manifesto=${manifest.recordCounts.questions}, Arquivo=${qCount}`);
  }
  if (optCount !== manifest.recordCounts.options) {
    throw new Error(`Divergência de opções: Manifesto=${manifest.recordCounts.options}, Arquivo=${optCount}`);
  }
  if (data.quizAnswers.length !== manifest.recordCounts.quizAnswers) {
    throw new Error(`Divergência de quiz answers: Manifesto=${manifest.recordCounts.quizAnswers}, Arquivo=${data.quizAnswers.length}`);
  }

  console.log(`✓ Estrutura válida e consistente:`);
  console.log(`  - Questões: ${qCount}`);
  console.log(`  - Opções: ${optCount}`);
  console.log(`  - Respostas de cadernos: ${data.quizAnswers.length}`);
  console.log(`  - Sessões de cadernos: ${data.quizSessions.length}`);
  console.log("==================================================");
  console.log("RESULTADO: BACKUP 100% VÁLIDO E ÍNTEGRO!");
  console.log("==================================================");
}

verifyBackup().catch((e) => {
  console.error(e);
  process.exit(1);
});
