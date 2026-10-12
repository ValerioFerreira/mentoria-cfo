// Contagem (somente leitura) das questões no banco: por origem do id e status, por disciplina e figuras.
//   npx tsx scripts/questoes-contagem.ts            # banco local (web/.env)
//   npx tsx scripts/questoes-contagem.ts --remoto   # produção (web/.env.remote: REMOTE_DATABASE_URL)
import "dotenv/config";
import { readFileSync, existsSync } from "node:fs";
import { resolve } from "node:path";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";

function url(): string {
  if (!process.argv.includes("--remoto")) return process.env.DATABASE_URL || "";
  const f = resolve(__dirname, "..", ".env.remote");
  if (!existsSync(f)) throw new Error("web/.env.remote não existe");
  const m = readFileSync(f, "utf8").match(/^\s*REMOTE_DATABASE_URL\s*=\s*"?([^"\r\n]+)"?/m);
  if (!m) throw new Error("REMOTE_DATABASE_URL ausente em web/.env.remote");
  return m[1];
}

const db = new PrismaClient({
  adapter: new PrismaPg({ connectionString: url().replace(/([?&])pgbouncer=true(&|$)/, (_, a, b) => (b ? a : "")) }),
});

async function main() {
  const byOrigin = await db.$queryRawUnsafe<{ origem: string; status: string; n: bigint }[]>(
    `SELECT split_part(id, '_', 1) AS origem, status::text AS status, count(*) AS n FROM "Question" GROUP BY 1, 2 ORDER BY 1, 2`,
  );
  console.log("Por origem e status:");
  for (const r of byOrigin) console.log(`  ${r.origem.padEnd(8)} ${r.status.padEnd(9)} ${r.n}`);
  const bySubject = await db.$queryRawUnsafe<{ subject: string; kind: string; n: bigint }[]>(
    `SELECT "subjectId" AS subject, kind::text AS kind, count(*) AS n FROM "Question" WHERE status = 'APPROVED' GROUP BY 1, 2 ORDER BY 1, 2`,
  );
  console.log("Aprovadas por disciplina e formato:");
  for (const r of bySubject) console.log(`  ${r.subject.padEnd(24)} ${r.kind.padEnd(17)} ${r.n}`);
  console.log(
    `Respostas: ${await db.quizAnswer.count()} · cadernos/simulados: ${await db.quizSession.count()} · figuras: ${await db.questionImage.count()}`,
  );
}

main().finally(() => db.$disconnect());
