// Aplicador dos comentários das questões: content/questoes/comentarios/<disciplina>/<lote>.json → banco
// (Question.explanation e QuestionOption.comment). É o ÚNICO caminho que grava comentário (o importador não grava).
//
//   npx tsx scripts/questoes-comentarios.ts [--remoto] [--aplicar] [--confirmo-producao] [--so <disciplina|disciplina/lote.json>]
//
// Padrão: SIMULAÇÃO (só lê e relata). Com --aplicar grava apenas o que confere com a questão do banco: mesmo contentHash
// (texto + gabarito), mesmo gabarito e as mesmas letras. O que não confere sai no relatório como "desatualizado",
// "gabarito", "alternativas" ou "ausente" e não é gravado. Arquivos com "revisao": "pendente" (comentários aproveitados da
// Fixação ainda não conferidos) ficam de fora até a revisão. Relatório: web/reports/comentarios-<destino>-<data>.json.
//
// Produção (--remoto): gravar mais de 300 questões exige backup íntegro de menos de 24 h
// (npx tsx scripts/questoes-backup.ts --remoto) e --confirmo-producao.
import "dotenv/config";
import { execFileSync } from "node:child_process";
import { existsSync, mkdirSync, readdirSync, readFileSync, statSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";
import { checkComment, loadComments, type DbQuestion } from "./lib/comentarios";

const args = process.argv.slice(2);
const remote = args.includes("--remoto");
const apply = args.includes("--aplicar");
const confirmed = args.includes("--confirmo-producao");
const only = args.includes("--so") ? args[args.indexOf("--so") + 1] : null;
const MASS = 300;
const BACKUP_MAX_H = 24;

function remoteUrl(): string {
  const f = resolve(__dirname, "..", ".env.remote");
  if (!existsSync(f)) throw new Error("web/.env.remote não existe");
  const m = readFileSync(f, "utf8").match(/^\s*REMOTE_DATABASE_URL\s*=\s*"?([^"\r\n]+)"?/m);
  if (!m) throw new Error("REMOTE_DATABASE_URL ausente em web/.env.remote");
  return m[1];
}
const url = (remote ? remoteUrl() : process.env.DATABASE_URL || "").replace(/([?&])pgbouncer=true(&|$)/, (_, a, b) => (b ? a : ""));
if (!url) throw new Error("DATABASE_URL vazio");
const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: url }) });

/** Backup remoto mais recente: íntegro (questoes-backup.ts --verificar) e com menos de 24 h. */
function recentRemoteBackup(): string | null {
  const dir = resolve(__dirname, "..", "..", "backups");
  if (!existsSync(dir)) return null;
  const last = readdirSync(dir).filter((d) => d.startsWith("questoes-remoto-")).sort().pop();
  if (!last) return null;
  const man = join(dir, last, "manifest.json");
  if (!existsSync(man) || (Date.now() - statSync(man).mtimeMs) / 3_600_000 > BACKUP_MAX_H) return null;
  try {
    execFileSync("npx", ["tsx", "scripts/questoes-backup.ts", "--verificar", join(dir, last)], { cwd: resolve(__dirname, ".."), stdio: "pipe", shell: process.platform === "win32" });
  } catch {
    return null;
  }
  return join(dir, last);
}

async function runPool(tasks: (() => Promise<unknown>)[], size: number): Promise<void> {
  let next = 0;
  const worker = async () => {
    while (next < tasks.length) await tasks[next++]();
  };
  await Promise.all(Array.from({ length: Math.min(size, tasks.length) }, worker));
}

(async () => {
  const filter = only ? (arquivo: string) => arquivo === only || arquivo.startsWith(`${only.replace(/\/$/, "")}/`) : undefined;
  const { entries, discards, problems } = loadComments(filter);
  const ids = [...entries.keys()];
  const current = new Map<string, DbQuestion>();
  for (let i = 0; i < ids.length; i += 1000) {
    for (const q of await db.question.findMany({
      where: { id: { in: ids.slice(i, i + 1000) } },
      select: { id: true, contentHash: true, kind: true, explanation: true, options: { select: { label: true, isCorrect: true, comment: true } } },
    })) current.set(q.id, q);
  }
  const toWrite: { id: string; explanation: string; optionComments: Record<string, string | null> }[] = [];
  const counts: Record<string, number> = { gravar: 0, igual: 0, ausente: 0, desatualizado: 0, gabarito: 0, alternativas: 0 };
  const issues: { id: string; status: string; detalhe: string; arquivo: string }[] = [];
  const pending: string[] = [];
  for (const c of entries.values()) {
    if (c.pendente) {
      pending.push(c.id); // aguarda a revisão por agente (arquivo com "revisao": "pendente")
      continue;
    }
    const v = checkComment(c, current.get(c.id));
    counts[v.status]++;
    if (v.status === "gravar") toWrite.push({ id: c.id, explanation: c.comentario, optionComments: v.optionComments });
    else if (v.status !== "igual") issues.push({ id: c.id, status: v.status, detalhe: v.detalhe, arquivo: c.arquivo });
  }
  const report = {
    destino: remote ? "remoto" : "local",
    modo: apply ? "aplicar" : "simulação",
    geradoEm: new Date().toISOString(),
    arquivos: only ?? "todos",
    comentarios: entries.size,
    ...counts,
    aguardandoRevisao: pending.length,
    descartes: discards.length,
    problemasNosArquivos: problems,
    naoGravados: issues,
    gravados: 0,
  };
  if (apply && toWrite.length) {
    if (remote && toWrite.length > MASS) {
      const backup = recentRemoteBackup();
      if (!backup || !confirmed) {
        console.error(
          `Gravação em massa na produção (${toWrite.length} questões > ${MASS}): exige backup íntegro de menos de ${BACKUP_MAX_H} h ` +
            `(npx tsx scripts/questoes-backup.ts --remoto) e --confirmo-producao. Backup encontrado: ${backup ?? "nenhum válido"}.`,
        );
        process.exitCode = 2;
        await db.$disconnect();
        return;
      }
      console.log(`backup remoto válido: ${backup} (reversão: npx tsx scripts/questoes-restore.ts ${backup} --remoto --aplicar --confirmo-producao)`);
    }
    // blocos de 200 questões, cada bloco numa transação com dois UPDATE … FROM unnest(...) (uma questão por transação
    // levava horas no Postgres embutido do `prisma dev`)
    const tasks: (() => Promise<unknown>)[] = [];
    for (let i = 0; i < toWrite.length; i += 200) {
      const block = toWrite.slice(i, i + 200);
      const opts = block.flatMap((w) => Object.entries(w.optionComments).map(([label, comment]) => [w.id, label, comment] as const));
      tasks.push(() =>
        db.$transaction(async (tx) => {
          await tx.$executeRawUnsafe(
            `UPDATE "Question" q SET "explanation" = d.e FROM unnest($1::text[], $2::text[]) AS d(id, e) WHERE q."id" = d.id`,
            block.map((w) => w.id),
            block.map((w) => w.explanation),
          );
          await tx.$executeRawUnsafe(
            `UPDATE "QuestionOption" o SET "comment" = d.c FROM unnest($1::text[], $2::text[], $3::text[]) AS d(qid, label, c) WHERE o."questionId" = d.qid AND o."label" = d.label`,
            opts.map((o) => o[0]),
            opts.map((o) => o[1]),
            opts.map((o) => o[2]),
          );
          report.gravados += block.length;
        }, { timeout: 120_000 }),
      );
    }
    // Neon: 3 blocos em paralelo; o Postgres embutido do `prisma dev` aceita uma conexão por vez
    await runPool(tasks, remote ? 3 : 1);
  }
  const outDir = resolve(__dirname, "..", "reports");
  mkdirSync(outDir, { recursive: true });
  const stamp = new Date().toISOString().replace(/[-:]/g, "").slice(0, 15);
  const out = join(outDir, `comentarios-${remote ? "remoto" : "local"}-${stamp}.json`);
  writeFileSync(out, JSON.stringify(report, null, 1));
  const { naoGravados, problemasNosArquivos, ...head } = report;
  console.log(JSON.stringify({ ...head, naoGravados: naoGravados.length, problemasNosArquivos: problemasNosArquivos.length, relatorio: out }));
  await db.$disconnect();
})().catch(async (e) => {
  console.error(e);
  await db.$disconnect();
  process.exitCode = 1;
});
