// Exporta (somente leitura) as figuras das questões usadas na Fixação do material próprio MentorIA.
// Lê as /q-img/<sha256> citadas em pipeline/.cache/material/questoes/*.json e grava cada imagem em
// pipeline/.cache/material/q-img/<sha256>.<ext>, de onde o motor de PDF (pipeline/material_pdf/render_md.py) as lê.
//   npx tsx scripts/material-qimg.ts
import "dotenv/config";
import { existsSync, mkdirSync, readdirSync, readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";

const ROOT = resolve(__dirname, "..", "..");
const IN_DIR = resolve(ROOT, "pipeline", ".cache", "material", "questoes");
const OUT_DIR = resolve(ROOT, "pipeline", ".cache", "material", "q-img");

const EXT: Record<string, string> = { "image/png": "png", "image/jpeg": "jpg", "image/gif": "gif", "image/webp": "webp", "image/svg+xml": "svg" };

const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL || "" }) });

async function main() {
  const shas = new Set<string>();
  for (const f of readdirSync(IN_DIR).filter((n) => n.endsWith(".json") && !n.endsWith(".ref.json"))) {
    const txt = readFileSync(resolve(IN_DIR, f), "utf8");
    for (const m of txt.matchAll(/\/q-img\/([0-9a-f]{64})/g)) shas.add(m[1]);
  }
  mkdirSync(OUT_DIR, { recursive: true });
  let novas = 0;
  let faltam = 0;
  for (const sha of shas) {
    if (readdirSync(OUT_DIR).some((n) => n.startsWith(sha + "."))) continue;
    const img = await db.questionImage.findUnique({ where: { id: sha } });
    if (!img) {
      faltam++;
      console.warn(`figura ${sha} não existe no banco`);
      continue;
    }
    writeFileSync(resolve(OUT_DIR, `${sha}.${EXT[img.mime] ?? "png"}`), Buffer.from(img.data));
    novas++;
  }
  console.log(`${shas.size} figuras citadas · ${novas} gravadas agora · ${faltam} ausentes do banco · pasta ${existsSync(OUT_DIR) ? OUT_DIR : "?"}`);
}

main().finally(() => db.$disconnect());
