// Exporta (SÓ LEITURA) a contagem de questões APROVADAS por trecho e banca, para o auditor dos planos e para o cálculo de lacunas.
//   npx tsx scripts/pcpe-segcounts.ts [saida.json] [--remoto]     (padrão: ../pipeline/.cache/pcpe-segcounts.json; banco local)
import "dotenv/config";
import { readFileSync, writeFileSync, existsSync, mkdirSync } from "node:fs";
import { resolve, dirname } from "node:path";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";

const args = process.argv.slice(2);
const remote = args.includes("--remoto");
const out = args.find((a) => !a.startsWith("--")) ?? resolve(__dirname, "../../pipeline/.cache/pcpe-segcounts.json");
function remoteUrl(): string {
  const m = readFileSync(resolve(__dirname, "..", ".env.remote"), "utf8").match(/^\s*REMOTE_DATABASE_URL\s*=\s*"?([^"\r\n]+)"?/m);
  if (!m) throw new Error("REMOTE_DATABASE_URL ausente em web/.env.remote");
  return m[1];
}
const url = (remote ? remoteUrl() : process.env.DATABASE_URL || "").replace(/([?&])pgbouncer=true(&|$)/, (_, a, b) => (b ? a : ""));
if (!url) throw new Error("DATABASE_URL vazio");
const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: url }) });
(async () => {
  const rows = await db.question.groupBy({ by: ["segmentId", "banca", "kind", "batch"], where: { status: "APPROVED" }, _count: true });
  const dir = dirname(out);
  if (!existsSync(dir)) mkdirSync(dir, { recursive: true });
  writeFileSync(out, JSON.stringify(rows.map((r) => ({ seg: r.segmentId, banca: r.banca, kind: r.kind, batch: r.batch, n: r._count }))));
  console.log(`${rows.length} grupos -> ${out} (${remote ? "remoto" : "local"})`);
  await db.$disconnect();
})();
