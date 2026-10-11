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

async function queryStats() {
  const total = await db.question.count();
  const approved = await db.question.count({ where: { status: "APPROVED" } });
  const draft = await db.question.count({ where: { status: "DRAFT" } });
  const retired = await db.question.count({ where: { status: "RETIRED" } });
  const tec = await db.question.count({ where: { id: { startsWith: "tec_" } } });
  const pmpe = await db.question.count({ where: { id: { startsWith: "pmpe_" } } });
  const cbmpe = await db.question.count({ where: { id: { startsWith: "cbmpe_" } } });
  
  const bancas = await db.question.groupBy({
    by: ["banca"],
    _count: { id: true },
    orderBy: { _count: { id: "desc" } },
  });

  console.log(JSON.stringify({
    total,
    approved,
    draft,
    retired,
    tec,
    pmpe,
    cbmpe,
    bancasCount: bancas.length,
    topBancas: bancas.slice(0, 15).map(b => ({ banca: b.banca, count: b._count.id }))
  }, null, 2));
}

queryStats().finally(() => db.$disconnect());
