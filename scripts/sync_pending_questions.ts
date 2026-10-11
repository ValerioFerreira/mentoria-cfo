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

async function syncPending() {
  const pendingFile = path.resolve(__dirname, "../pipeline/.cache/pending_auto_import.json");
  if (!fs.existsSync(pendingFile)) {
    console.log("Nenhuma importação pendente encontrada.");
    return;
  }

  const items = JSON.parse(fs.readFileSync(pendingFile, "utf-8"));
  console.log(`Sincronizando ${items.length} questões com o banco de dados...`);

  let insertedCount = 0;
  let updatedCount = 0;

  for (const item of items) {
    const { tecId, seqNum, options, ...qData } = item;
    const exists = await db.question.findUnique({ where: { id: item.id } });

    if (!exists) {
      await db.question.create({ data: qData });
      if (options && options.length > 0) {
        await db.questionOption.createMany({
          data: options.map((opt: any) => ({
            questionId: item.id,
            label: opt.label,
            text: opt.text,
            isCorrect: opt.isCorrect,
          })),
        });
      }
      insertedCount++;
    } else {
      const { id, ...updateFields } = qData;
      await db.question.update({
        where: { id: item.id },
        data: updateFields,
      });
      updatedCount++;
    }
  }

  // Limpar arquivo de pendências após sucesso
  fs.unlinkSync(pendingFile);
  console.log(`✓ Sincronização concluída! Novas inseridas: ${insertedCount}, Atualizadas: ${updatedCount}`);
}

syncPending()
  .catch((e) => {
    console.error("Erro na sincronização:", e);
    process.exit(1);
  })
  .finally(() => db.$disconnect());
