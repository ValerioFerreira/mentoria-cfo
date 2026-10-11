import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

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

const { PrismaPg } = require(path.resolve(__dirname, "../web/node_modules/@prisma/adapter-pg"));
const { PrismaClient } = require(path.resolve(__dirname, "../web/src/generated/prisma/client"));

const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }) });

async function exportCleanQuestions() {
  console.log("Lendo questões do banco local...");
  const questions = await db.question.findMany({
    where: { id: { startsWith: "tec_" } },
    include: {
      options: {
        orderBy: { label: "asc" },
      },
    },
    orderBy: { id: "asc" },
  });

  console.log(`Encontradas ${questions.length} questões do TecConcursos no banco local.`);

  const outputPath = path.resolve(__dirname, "../content/questoes_tecconcursos.json");
  fs.writeFileSync(outputPath, JSON.stringify(questions, null, 2), "utf-8");
  console.log(`Salvo em ${outputPath} (${(fs.statSync(outputPath).size / 1024 / 1024).toFixed(2)} MB).`);

  // Também salvar em web/content/questoes_tecconcursos.json para garantir acessibilidade
  const webOutputPath = path.resolve(__dirname, "../web/content/questoes_tecconcursos.json");
  fs.mkdirSync(path.dirname(webOutputPath), { recursive: true });
  fs.copyFileSync(outputPath, webOutputPath);
  console.log(`Copiado para ${webOutputPath}.`);

  await db.$disconnect();
}

exportCleanQuestions().catch((err) => {
  console.error("Erro ao exportar:", err);
  process.exit(1);
});
