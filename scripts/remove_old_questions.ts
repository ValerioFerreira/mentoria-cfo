import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");

// Ler DATABASE_URL
const envPath = path.resolve(ROOT, "web/.env");
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

const { PrismaPg } = require(path.resolve(ROOT, "web/node_modules/@prisma/adapter-pg"));
const { PrismaClient } = require(path.resolve(ROOT, "web/src/generated/prisma/client"));

const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }) });

async function cleanJsonDir(dirPath: string) {
  if (!fs.existsSync(dirPath)) return 0;
  let removedCount = 0;
  for (const sub of fs.readdirSync(dirPath)) {
    const subPath = path.join(dirPath, sub);
    if (!fs.statSync(subPath).isDirectory()) continue;
    for (const file of fs.readdirSync(subPath)) {
      if (!file.endsWith(".json")) continue;
      const filePath = path.join(subPath, file);
      const data = JSON.parse(fs.readFileSync(filePath, "utf-8"));
      let modified = false;
      for (const seg of data.segments || []) {
        if (seg.questions && seg.questions.length > 0) {
          removedCount += seg.questions.length;
          delete seg.questions;
          modified = true;
        }
      }
      if (modified) {
        fs.writeFileSync(filePath, JSON.stringify(data, null, 2), "utf-8");
      }
    }
  }
  return removedCount;
}

async function main() {
  console.log("==================================================");
  console.log("REMOÇÃO DAS QUESTÕES ANTIGAS CRIADAS POR NÓS");
  console.log("==================================================");

  // 1. Limpar arquivos JSON
  console.log("\n1. Limpando questões antigas em content/items...");
  const c1 = await cleanJsonDir(path.resolve(ROOT, "content/items"));
  console.log(`✓ Removidas ${c1} questões de content/items.`);

  console.log("\n2. Limpando questões antigas em web/content/items...");
  const c2 = await cleanJsonDir(path.resolve(ROOT, "web/content/items"));
  console.log(`✓ Removidas ${c2} questões de web/content/items.`);

  // 2. Limpar banco de dados (remover qualquer questão que não comece com 'tec_')
  console.log("\n3. Verificando e limpando banco de dados...");
  const oldInDb = await db.question.count({
    where: {
      NOT: {
        id: { startsWith: "tec_" },
      },
    },
  });

  if (oldInDb > 0) {
    console.log(`Encontradas ${oldInDb} questões antigas no banco. Deletando...`);
    // Excluir opções
    await db.questionOption.deleteMany({
      where: {
        question: {
          NOT: { id: { startsWith: "tec_" } },
        },
      },
    });
    // Excluir respostas vinculadas
    await db.quizAnswer.deleteMany({
      where: {
        question: {
          NOT: { id: { startsWith: "tec_" } },
        },
      },
    });
    // Excluir as questões
    await db.question.deleteMany({
      where: {
        NOT: { id: { startsWith: "tec_" } },
      },
    });
    console.log(`✓ ${oldInDb} questões antigas removidas com sucesso do banco!`);
  } else {
    console.log("✓ O banco de dados já não contém questões antigas sem prefixo tec_.");
  }

  const totalTec = await db.question.count();
  console.log(`\nAcervo oficial final no banco: ${totalTec} questões reais do TecConcursos (AOCP / Instituto AOCP).`);
  console.log("==================================================");
}

main()
  .catch((e) => {
    console.error("Erro na limpeza:", e);
    process.exit(1);
  })
  .finally(() => db.$disconnect());
