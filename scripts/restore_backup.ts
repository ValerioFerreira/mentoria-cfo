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

async function restoreBackup() {
  const targetFileArg = process.argv[2];
  const backupDir = path.resolve(__dirname, "../backups/questoes");
  let targetFilePath: string;

  if (targetFileArg) {
    targetFilePath = path.isAbsolute(targetFileArg) ? targetFileArg : path.resolve(process.cwd(), targetFileArg);
  } else {
    const manifestPath = path.join(backupDir, "manifest.json");
    if (!fs.existsSync(manifestPath)) {
      throw new Error(`Informe o arquivo de backup ou certifique-se de que manifest.json existe em ${backupDir}`);
    }
    const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf-8"));
    targetFilePath = path.join(backupDir, manifest.backupFileName);
  }

  console.log(`Carregando backup de: ${targetFilePath}`);
  if (!fs.existsSync(targetFilePath)) {
    throw new Error(`Arquivo não encontrado: ${targetFilePath}`);
  }

  const data = JSON.parse(fs.readFileSync(targetFilePath, "utf-8"));
  console.log(`Backup contém ${data.questions.length} questões.`);

  console.log("Restaurando questões...");
  let restoredQ = 0;
  for (const q of data.questions) {
    const { options, reports, ...qData } = q;
    await db.question.upsert({
      where: { id: q.id },
      create: qData,
      update: qData,
    });

    if (Array.isArray(options) && options.length > 0) {
      await db.questionOption.deleteMany({ where: { questionId: q.id } });
      await db.questionOption.createMany({
        data: options.map((opt: any) => ({
          questionId: q.id,
          label: opt.label,
          text: opt.text,
          isCorrect: opt.isCorrect,
        })),
      });
    }
    restoredQ++;
    if (restoredQ % 1000 === 0) {
      console.log(`  Restauradas ${restoredQ}/${data.questions.length}...`);
    }
  }

  console.log(`✓ ${restoredQ} questões restauradas com sucesso!`);
}

restoreBackup()
  .catch((e) => {
    console.error("Erro na restauração:", e);
    process.exit(1);
  })
  .finally(() => db.$disconnect());
