// Manda para RASCUNHO (DRAFT, fora do ar) questões do TEC com defeito de extração apontado pela auditoria
// (perda de texto, enunciado vazio, alternativa duplicada...), sem apagar nada. Marca classifiedBy = MANUAL, então o importador
// não as reativa. Para voltar, aprove em /admin/revisao.
//   npx tsx scripts/questoes-marcar-rascunho.ts <arquivo.csv com coluna tecId;...> [--remoto]   (só grava com --aplicar)
import "dotenv/config";
import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";

const args = process.argv.slice(2);
const remote = args.includes("--remoto");
const aplicar = args.includes("--aplicar");
const file = args.find((a) => !a.startsWith("--"));
if (!file) throw new Error("uso: questoes-marcar-rascunho.ts <arquivo.csv> [--remoto] [--aplicar]");
function remoteUrl(): string {
  const m = readFileSync(resolve(__dirname, "..", ".env.remote"), "utf8").match(/^\s*REMOTE_DATABASE_URL\s*=\s*"?([^"\r\n]+)"?/m);
  if (!m) throw new Error("REMOTE_DATABASE_URL ausente em web/.env.remote");
  return m[1];
}
const url = (remote ? remoteUrl() : process.env.DATABASE_URL || "").replace(/([?&])pgbouncer=true(&|$)/, (_, a, b) => (b ? a : ""));
const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: url }) });
(async () => {
  const ids = readFileSync(resolve(file), "utf8").split(/\r?\n/).slice(1).map((l) => l.split(";")[0].trim()).filter(Boolean).map((n) => `tec_${n}`);
  const found = await db.question.findMany({ where: { id: { in: ids } }, select: { id: true, status: true } });
  const alvo = found.filter((q) => q.status === "APPROVED").map((q) => q.id);
  console.log(`${ids.length} listadas · ${found.length} no banco (${remote ? "remoto" : "local"}) · ${alvo.length} aprovadas a mover para rascunho`);
  if (aplicar && alvo.length) {
    let n = 0;
    for (const id of alvo) {
      await db.question.update({ where: { id }, data: { status: "DRAFT", classifiedBy: "MANUAL", classifyNote: "Defeito de extração apontado pela auditoria de 21/10/2026: conferir no PDF antes de aprovar." } });
      n++;
    }
    console.log("movidas para rascunho:", n);
  }
  await db.$disconnect();
})();
