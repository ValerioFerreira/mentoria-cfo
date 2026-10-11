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

async function check() {
  const total = await db.question.count();
  const tecCount = await db.question.count({ where: { id: { startsWith: "tec_" } } });
  const nonTec = await db.question.count({ where: { NOT: { id: { startsWith: "tec_" } } } });
  const statuses = (await db.question.groupBy({ by: ["status"], _count: { id: true } })).map(s => ({ status: s.status, count: s._count.id }));
  console.log("Status do banco:", { total, tecCount, nonTec, statuses });
  await db.$disconnect();
}

check().catch(console.error);
