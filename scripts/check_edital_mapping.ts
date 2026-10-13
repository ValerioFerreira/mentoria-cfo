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

async function run() {
  const items = await db.editalItem.findMany();
  const aulas = await db.aula.findMany({ select: { id: true, subjectId: true, title: true, shortTitle: true, selectable: true } });
  console.log("Total editalItems:", items.length);
  console.log("Total aulas:", aulas.length);
  const aulasWithEdital = new Set(items.flatMap((i: any) => (i.aulaIds as string[]) || []));
  const planavelAulas = aulas.filter((a: any) => a.selectable);
  console.log("Planavel aulas:", planavelAulas.length);
  console.log("Planavel aulas com edital:", planavelAulas.filter((a: any) => aulasWithEdital.has(a.id)).length);
  const semEdital = planavelAulas.filter((a: any) => !aulasWithEdital.has(a.id));
  console.log("Planavel sem edital:", semEdital.map((a: any) => a.id));
  await db.$disconnect();
}

run().catch(console.error);
