// Confere (SÓ LEITURA) quais questões TEC de uma lista de números existem no banco. Usado por pipeline/questoes/processar_cadernos.py
// para só liberar a exclusão do PDF depois de a produção ter todas as questões do caderno.
//   npx tsx scripts/questoes-existem.ts ids.json [--remoto]     # ids.json = ["490820", ...] (números do TEC, sem o prefixo tec_)
// Última linha da saída: {"consultadas":N,"presentes":N,"ausentes":["..."]}
import "dotenv/config";
import { existsSync, readFileSync } from "node:fs";
import { resolve } from "node:path";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";

const args = process.argv.slice(2);
const remote = args.includes("--remoto");
const file = args.find((a) => !a.startsWith("--"));
if (!file) throw new Error("uso: questoes-existem.ts ids.json [--remoto]");

function remoteUrl(): string {
  const f = resolve(__dirname, "..", ".env.remote");
  if (!existsSync(f)) throw new Error("web/.env.remote não existe");
  const m = readFileSync(f, "utf8").match(/^\s*REMOTE_DATABASE_URL\s*=\s*"?([^"\r\n]+)"?/m);
  if (!m) throw new Error("REMOTE_DATABASE_URL ausente em web/.env.remote");
  return m[1];
}
const url = (remote ? remoteUrl() : process.env.DATABASE_URL || "").replace(/([?&])pgbouncer=true(&|$)/, (_, a, b) => (b ? a : ""));
const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: url }) });

(async () => {
  const ids = [...new Set(JSON.parse(readFileSync(resolve(file), "utf8")) as string[])];
  const found = new Set<string>();
  for (let i = 0; i < ids.length; i += 5000) {
    const chunk = ids.slice(i, i + 5000).map((x) => `tec_${x}`);
    const rows = await db.question.findMany({ where: { id: { in: chunk } }, select: { id: true } });
    for (const r of rows) found.add(r.id.slice(4));
  }
  const ausentes = ids.filter((x) => !found.has(x));
  console.log(JSON.stringify({ consultadas: ids.length, presentes: found.size, ausentes }));
  await db.$disconnect();
})();
