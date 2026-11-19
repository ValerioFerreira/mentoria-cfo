// Cobertura dos comentários nos cadernos dos planos ativos (SÓ LEITURA, não grava nada: nem banco nem arquivos).
//
//   npx tsx scripts/comentarios-cobertura.ts [--remoto] [--margem 10]
//
// "Pronta" = a questão tem comentário geral no banco OU entrada válida em content/questoes/comentarios (que o aplicador
// grava depois). Para cada caderno de Questões dos planos ACTIVE e PENDING_ANALYSIS responde:
//  - cadernos já sorteados: quantas das questões sorteadas estão comentadas;
//  - cadernos pendentes: quantas questões comentadas há no pool e se bastam para o sorteio que prefere comentadas
//    (`pickPreferCommented`): o caderno pede `quizQuestions`; com a margem, também cobre repetições e "fazer outro caderno".
import "dotenv/config";
import { existsSync, readFileSync } from "node:fs";
import { resolve } from "node:path";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";
import { loadComments } from "./lib/comentarios";
import { DEFAULT_QUIZ_QUESTIONS, activityPool, loadBank, loadPlans } from "./lib/plan-pools";

const args = process.argv.slice(2);
const remote = args.includes("--remoto");
const MARGEM = Number(args.includes("--margem") ? args[args.indexOf("--margem") + 1] : 10);

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

const pct = (a: number, b: number) => (b ? `${((100 * a) / b).toFixed(1)}%` : "-");

(async () => {
  const { entries } = loadComments();
  const { bank, plans } = await db.$transaction(
    async (tx) => {
      await tx.$executeRawUnsafe("SET TRANSACTION ISOLATION LEVEL REPEATABLE READ, READ ONLY");
      return { bank: await loadBank(tx), plans: await loadPlans(tx) };
    },
    { timeout: 600_000, maxWait: 60_000 },
  );
  const byId = new Map<string, { commented: boolean }>();
  for (const list of bank.values()) for (const q of list) byId.set(q.id, q);
  const ready = (id: string) => !!byId.get(id) && (byId.get(id)!.commented || entries.has(id));
  const inDbOnly = (id: string) => byId.get(id)?.commented ?? false;

  let acts = 0, closed = 0, drawnActs = 0, pendingActs = 0;
  let drawnQs = 0, drawnReady = 0, drawnDb = 0;
  const drawnSeen = new Set<string>();
  const rows: { plan: string; need: number; pool: number; ready: number }[] = [];
  const uncoveredQs = new Set<string>();
  for (const p of plans) {
    const teorias = p.activities.filter((a) => a.type === "TEORIA");
    for (const a of p.activities.filter((x) => x.type === "QUESTOES")) {
      acts++;
      const drawn = p.drawn.get(a.id);
      if (drawn?.length) {
        drawnActs++;
        for (const id of drawn) {
          if (drawnSeen.has(id)) continue;
          drawnSeen.add(id);
          drawnQs++;
          if (ready(id)) drawnReady++;
          if (inDbOnly(id)) drawnDb++;
        }
        continue;
      }
      if (a.status === "DONE" || a.status === "SKIPPED") {
        closed++;
        continue;
      }
      pendingActs++;
      const pool = activityPool(a, teorias, bank, p.contest);
      const ids = [...new Set([...pool.primary, ...pool.extra, ...pool.reinforcement])];
      const need = a.quizQuestions ?? DEFAULT_QUIZ_QUESTIONS;
      const r = ids.filter(ready).length;
      rows.push({ plan: p.id, need, pool: ids.length, ready: r });
      if (r < Math.min(ids.length, need + MARGEM)) for (const id of ids) if (!ready(id)) uncoveredQs.add(id);
    }
  }
  const okFull = rows.filter((r) => r.ready >= Math.min(r.pool, r.need)); // o caderno inteiro sai comentado
  const okMargin = rows.filter((r) => r.ready >= Math.min(r.pool, r.need + MARGEM));
  const short = rows.filter((r) => r.ready < Math.min(r.pool, r.need));
  const missing = short.reduce((s, r) => s + (Math.min(r.pool, r.need) - r.ready), 0);
  const hist = new Map<string, number>();
  for (const r of short) {
    const k = r.ready === 0 ? "0 comentadas" : r.ready < r.need / 2 ? "menos da metade" : "mais da metade";
    hist.set(k, (hist.get(k) ?? 0) + 1);
  }
  console.log(
    JSON.stringify(
      {
        destino: remote ? "remoto" : "local",
        planos: plans.length,
        cadernosDePlano: acts,
        cadernosEncerradosSemSorteio: closed,
        cadernosJaSorteados: drawnActs,
        cadernosPendentes: pendingActs,
        sorteadas: { questoesDistintas: drawnQs, comentadasProntas: drawnReady, pct: pct(drawnReady, drawnQs), jaNoBanco: drawnDb },
        pendentes: {
          cadernoInteiroComentado: okFull.length,
          pct: pct(okFull.length, rows.length),
          comMargemDe: MARGEM,
          cobertosComMargem: okMargin.length,
          cadernosComQuestaoSemComentario: short.length,
          questoesSemComentarioQueSairiam: missing,
          faltaPorGravidade: Object.fromEntries(hist),
          questoesDistintasParaFecharMargem: uncoveredQs.size,
        },
        comentariosNosArquivos: entries.size,
      },
      null,
      1,
    ),
  );
  await db.$disconnect();
})().catch((e) => {
  console.error(e);
  process.exit(1);
});
