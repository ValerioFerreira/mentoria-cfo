// Build do deploy. Migração e seed só rodam em PRODUÇÃO (ou fora da Vercel, no computador do desenvolvedor).
// Em Preview (qualquer branch/PR) o banco NÃO é tocado: um Preview que compartilhe a URL do banco de produção
// aplicaria migrações nele antes de a branch ser aprovada.
import { spawnSync } from "node:child_process";

const vercelEnv = process.env.VERCEL_ENV; // production | preview | development (indefinida fora da Vercel)
const touchesDatabase = !process.env.VERCEL || vercelEnv === "production";

function run(command, args) {
  const r = spawnSync(command, args, { stdio: "inherit", shell: true });
  if (r.status !== 0) process.exit(r.status ?? 1);
}

if (touchesDatabase) {
  run("prisma", ["migrate", "deploy"]);
  run("tsx", ["prisma/seed-structure.ts"]);
} else {
  console.log(`[build] VERCEL_ENV=${vercelEnv ?? "?"}: migração e seed ignorados (o banco não é alterado fora da produção).`);
}
run("next", ["build"]);
