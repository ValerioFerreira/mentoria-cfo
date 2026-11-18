// Fila de prioridade dos COMENTÁRIOS das questões (SÓ LEITURA no banco).
//
//   npx tsx scripts/questoes-fila-comentarios.ts [--remoto] [--pacotes P1|P2|P3|P4|todas|nenhum] [--lote-max 50] [--margem 10] [--todas]
//
// Lê numa transação READ ONLY e grava:
//  - content/questoes/comentarios/_fila.json: lotes (um trecho por lote, ~50 questões) com ids, trecho, faixa e contagens
//    agregadas (nenhum dado de aluno);
//  - pipeline/.cache/questoes-comentar/<disciplina>__<lote>.json (fora do git): enunciado, texto-base, alternativas,
//    gabarito e contentHash de cada questão do lote, mais o caminho do capítulo do material MentorIA e do resumo do trecho;
//  - pipeline/.cache/questoes-comentar/img/<sha>.png: figuras citadas nas questões dos pacotes.
//
// Faixas (sem as questões que já têm comentário no banco ou em content/questoes/comentarios):
//  P1. Planos dos alunos (ACTIVE e PENDING_ANALYSIS): questões já sorteadas nos cadernos das atividades e, para cada caderno
//      pendente, só o que falta para ele ter (o que pede + margem) questões comentadas no pool (o sorteio prefere comentadas;
//      `--todas` volta a comentar todo o pool). Antes, todo o pool
//      candidato das atividades de Questões pendentes (camada própria; extra e reforço só quando a própria não basta,
//      como em loadQuizPool). Ordem: data da atividade mais próxima (sorteadas e atrasadas = hoje), depois nº de alunos.
//  P2. CFOA: questões aprovadas que o caderno do CFOA usa nos trechos do edital do CFOA, por importância do trecho.
//  P3. CFO BM (CBMPE_OFICIAL): o mesmo critério.
//  P4. Restante (aprovadas): por trecho, primeiro os usados por mais concursos, depois pela importância.
import "dotenv/config";
import { existsSync, mkdirSync, readdirSync, readFileSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient, type Contest } from "../src/generated/prisma/client";
import { addDaysISO, dateOfPlanDay, todayISO } from "../src/lib/plan-time";
import { COMMENTS_DIR, loadComments } from "./lib/comentarios";
import { DEFAULT_QUIZ_QUESTIONS, activityPool, inActivityPool, loadBank, loadPlans, type BankQuestion } from "./lib/plan-pools";

const args = process.argv.slice(2);
const remote = args.includes("--remoto");
const arg = (n: string) => (args.includes(n) ? args[args.indexOf(n) + 1] : undefined);
const pacotes = (arg("--pacotes") ?? "P1").toUpperCase();
const LOTE_MAX = Number(arg("--lote-max") ?? 50);
const todas = args.includes("--todas"); // comentar todo o pool candidato (sem a redução pelo sorteio que prefere comentadas)
const MARGEM = Number(arg("--margem") ?? 10); // comentadas além do que o caderno pede, para repetições e "fazer outro caderno"

const ROOT = resolve(__dirname, "..", "..");
const CACHE_DIR = join(ROOT, "pipeline", ".cache", "questoes-comentar");

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

/** Ids já comentados (ou descartados, à espera de decisão do dono) nos arquivos versionados. */
function commentedInContent(): Set<string> {
  const { entries, discards } = loadComments();
  return new Set([...entries.keys(), ...discards.map((d) => d.id)]);
}

type Importance = { segments: Record<string, { shared: number; contests: Record<string, { appears: boolean; expected: number; score: number | null }> }> };
const importance = JSON.parse(readFileSync(join(ROOT, "content", "importance", "segments.json"), "utf8")) as Importance;

/** Capítulo do material MentorIA por trecho: primeiro o índice dos PDFs (aprovados), depois qualquer capítulo escrito. */
function chapterMap(): Map<string, { path: string; noIndice: boolean }> {
  const out = new Map<string, { path: string; noIndice: boolean }>();
  const idx = JSON.parse(readFileSync(join(ROOT, "content", "material", "index.json"), "utf8")) as { volumes: Record<string, { capitulos: Record<string, unknown> }> };
  for (const [vol, v] of Object.entries(idx.volumes)) {
    for (const trecho of Object.keys(v.capitulos)) {
      const [, aula, seg] = trecho.split("/");
      const p = join("content", "material", vol, `${aula}-${seg}.md`);
      if (existsSync(join(ROOT, p))) out.set(trecho, { path: p.replace(/\\/g, "/"), noIndice: true });
    }
  }
  const matDir = join(ROOT, "content", "material");
  for (const disc of readdirSync(matDir, { withFileTypes: true })) {
    if (!disc.isDirectory() || disc.name.startsWith("_")) continue;
    for (const vol of readdirSync(join(matDir, disc.name), { withFileTypes: true })) {
      if (!vol.isDirectory() || !/^m\d+$/.test(vol.name)) continue;
      for (const f of readdirSync(join(matDir, disc.name, vol.name))) {
        const m = f.match(/^a(\d+)-s(\d+)\.md$/);
        if (!m) continue;
        const trecho = `${disc.name}/a${m[1]}/s${m[2]}`;
        if (!out.has(trecho)) out.set(trecho, { path: `content/material/${disc.name}/${vol.name}/${f}`, noIndice: false });
      }
    }
  }
  return out;
}

const summaryPath = (trecho: string): string | null => {
  const [disc, aula] = trecho.split("/");
  const p = join("content", "summaries", disc, `${aula}.json`);
  if (!existsSync(join(ROOT, p))) return null;
  const j = JSON.parse(readFileSync(join(ROOT, p), "utf8")) as { segments?: { id: string; analytic?: string }[] };
  return j.segments?.some((s) => s.id === trecho && (s.analytic ?? "").trim()) ? p.replace(/\\/g, "/") : null;
};

type Band = "P1" | "P2" | "P3" | "P4";
interface Item {
  id: string;
  segmentId: string;
  band: Band;
  /** P1: data mais próxima em que a questão pode cair (AAAA-MM-DD) */
  date?: string;
  /** P1: nº de alunos cujos cadernos podem trazer a questão */
  students?: number;
  /** P1: já sorteada num caderno */
  drawn?: boolean;
  rank: number;
}

const contestsOfSegment = (segId: string): Contest[] =>
  Object.entries(importance.segments[segId]?.contests ?? {})
    .filter(([c, v]) => v.appears && !c.includes("COMBO"))
    .map(([c]) => c as Contest);
const scoreOf = (segId: string, contest: string): number => importance.segments[segId]?.contests[contest]?.score ?? 0;

(async () => {
  const today = todayISO();
  const done = commentedInContent();
  const report: Record<string, unknown> = { destino: remote ? "remoto" : "local", geradoEm: new Date().toISOString(), hoje: today };
  const { bank, plans, segInfo } = await db.$transaction(
    async (tx) => {
      await tx.$executeRawUnsafe("SET TRANSACTION ISOLATION LEVEL REPEATABLE READ, READ ONLY");
      const bank = await loadBank(tx);
      const plans = await loadPlans(tx);
      const segs = await tx.segment.findMany({ select: { id: true, startTopic: true, aula: { select: { title: true, subjectId: true } } } });
      return { bank, plans, segInfo: new Map(segs.map((s) => [s.id, s])) };
    },
    { timeout: 600_000, maxWait: 60_000 },
  );
  const byId = new Map<string, BankQuestion>();
  for (const list of bank.values()) for (const q of list) byId.set(q.id, q);
  const pending = (id: string) => {
    const q = byId.get(id);
    return !!q && !q.commented && !done.has(id);
  };

  // ---------- P1: planos dos alunos ----------
  const p1 = new Map<string, { date: string; students: Set<string>; drawn: boolean; activities: number }>();
  const touch = (id: string, date: string, userId: string, drawn: boolean) => {
    const cur = p1.get(id) ?? { date, students: new Set<string>(), drawn: false, activities: 0 };
    if (date < cur.date) cur.date = date;
    cur.students.add(userId);
    cur.drawn ||= drawn;
    cur.activities++;
    p1.set(id, cur);
  };
  const pendingPools: { date: string; userId: string; ids: string[]; alvo: number }[] = [];
  const chosen = new Set<string>();
  let drawnTotal = 0;
  let quizActs = 0;
  let pendingActs = 0;
  const allDrawn = new Set<string>();
  const allCandidates = new Set<string>();
  for (const p of plans) {
    const teorias = p.activities.filter((a) => a.type === "TEORIA");
    for (const a of p.activities.filter((x) => x.type === "QUESTOES")) {
      quizActs++;
      const drawn = p.drawn.get(a.id);
      if (drawn?.length) {
        for (const id of drawn) {
          allDrawn.add(id);
          touch(id, today, p.userId, true);
        }
        drawnTotal += drawn.length;
        continue; // caderno já sorteado: o pool não muda mais
      }
      if (a.status === "DONE" || a.status === "SKIPPED") continue;
      pendingActs++;
      const d = dateOfPlanDay(p.startIso, a.weekIndex, a.dayIndex ?? 0);
      const date = d < today ? today : d;
      const pool = activityPool(a, teorias, bank, p.contest);
      const ids = [...pool.primary, ...pool.extra, ...pool.reinforcement];
      for (const id of ids) allCandidates.add(id);
      if (todas) for (const id of ids) touch(id, date, p.userId, false);
      else pendingPools.push({ date, userId: p.userId, ids, alvo: Math.min(ids.length, (a.quizQuestions ?? DEFAULT_QUIZ_QUESTIONS) + MARGEM) });
    }
  }
  // O sorteio do caderno prefere questões comentadas (pickPreferCommented): cada caderno pendente só precisa de `alvo` questões
  // comentadas no seu pool (o que ele pede + margem para repetições). Cobertura gulosa: do caderno mais próximo ao mais distante,
  // completa o que falta com as questões que aparecem em mais cadernos deficitários (um comentário serve a vários alunos).
  if (!todas) {
    const freq = new Map<string, number>();
    for (const pl of pendingPools) for (const id of pl.ids) freq.set(id, (freq.get(id) ?? 0) + 1);
    const have = (id: string) => !pending(id) || chosen.has(id);
    pendingPools.sort((x, y) => x.date.localeCompare(y.date));
    for (const pl of pendingPools) {
      let falta = pl.alvo - pl.ids.filter(have).length;
      if (falta <= 0) continue;
      const cand = pl.ids.filter((id) => !have(id)).sort((x, y) => (freq.get(y) ?? 0) - (freq.get(x) ?? 0) || x.localeCompare(y));
      for (const id of cand) {
        if (falta-- <= 0) break;
        chosen.add(id);
      }
    }
    for (const pl of pendingPools) for (const id of pl.ids) if (chosen.has(id)) touch(id, pl.date, pl.userId, false);
    report.cobertura = { margem: MARGEM, cadernosPendentes: pendingPools.length, questoesNecessarias: chosen.size, semReduzir: allCandidates.size };
  }
  const items: Item[] = [];
  const p1Ids = [...p1.entries()].filter(([id]) => pending(id));
  p1Ids.sort((a, b) => a[1].date.localeCompare(b[1].date) || b[1].students.size - a[1].students.size || a[0].localeCompare(b[0]));
  p1Ids.forEach(([id, v], i) => items.push({ id, segmentId: byId.get(id)!.segmentId, band: "P1", date: v.date, students: v.students.size, drawn: v.drawn, rank: i }));
  const taken = new Set(items.map((i) => i.id));

  // ---------- P2/P3: CFOA e CFO BM ----------
  const contestBand = (contest: Contest, band: Band) => {
    const segs = Object.keys(importance.segments).filter((s) => importance.segments[s].contests[contest]?.appears);
    segs.sort((a, b) => scoreOf(b, contest) - scoreOf(a, contest) || a.localeCompare(b));
    let rank = 0;
    for (const s of segs) {
      for (const q of bank.get(s) ?? []) {
        if (taken.has(q.id) || !pending(q.id) || !inActivityPool(q, contest)) continue;
        items.push({ id: q.id, segmentId: s, band, rank: rank++ });
        taken.add(q.id);
      }
    }
  };
  contestBand("CBMPE_CFOA", "P2");
  contestBand("CBMPE_OFICIAL", "P3");

  // ---------- P4: restante ----------
  const rest = [...bank.keys()];
  const maxScore = (s: string) => Math.max(0, ...contestsOfSegment(s).map((c) => scoreOf(s, c)));
  rest.sort((a, b) => contestsOfSegment(b).length - contestsOfSegment(a).length || maxScore(b) - maxScore(a) || a.localeCompare(b));
  let r4 = 0;
  for (const s of rest) {
    for (const q of bank.get(s) ?? []) {
      if (taken.has(q.id) || !pending(q.id)) continue;
      items.push({ id: q.id, segmentId: s, band: "P4", rank: r4++ });
      taken.add(q.id);
    }
  }

  // ---------- lotes: um trecho por lote, ~LOTE_MAX questões, na ordem da faixa ----------
  type Lote = { id: string; faixa: Band; disciplina: string; trecho: string; arquivo: string; questoes: string[]; primeiraData?: string; alunos?: number; sorteadas?: number };
  const lotes: Lote[] = [];
  const usedNames = new Set<string>();
  const makeLotes = (band: Band, bandItems: Item[], prefix: string) => {
    const bySeg = new Map<string, Item[]>();
    for (const it of bandItems) bySeg.set(it.segmentId, [...(bySeg.get(it.segmentId) ?? []), it]);
    const out: Lote[] = [];
    for (const [seg, its] of bySeg) {
      const [disc, aula, s] = seg.split("/");
      const parts = Math.ceil(its.length / LOTE_MAX);
      const size = Math.ceil(its.length / parts);
      for (let k = 0; k < parts; k++) {
        const chunk = its.slice(k * size, (k + 1) * size);
        let n = 1;
        let name = `${prefix}-${aula}-${s}-${n}`;
        while (usedNames.has(`${disc}/${name}`) || existsSync(join(COMMENTS_DIR, disc, `${name}.json`))) name = `${prefix}-${aula}-${s}-${++n}`;
        usedNames.add(`${disc}/${name}`);
        out.push({
          id: `${disc}/${name}`, faixa: band, disciplina: disc, trecho: seg, arquivo: `content/questoes/comentarios/${disc}/${name}.json`,
          questoes: chunk.map((c) => c.id),
          ...(band === "P1"
            ? { primeiraData: chunk.map((c) => c.date!).sort()[0], alunos: Math.max(...chunk.map((c) => c.students ?? 0)), sorteadas: chunk.filter((c) => c.drawn).length }
            : {}),
        });
      }
    }
    return out;
  };
  const byRank = (b: Band) => items.filter((i) => i.band === b).sort((x, y) => x.rank - y.rank);
  // P1: primeiro as questões já sorteadas (o aluno já as vê no caderno ou no resultado), por trecho; depois as candidatas,
  // com os lotes pela data mais próxima de qualquer questão deles
  const byDate = (a: Lote, b: Lote) => (a.primeiraData ?? "").localeCompare(b.primeiraData ?? "") || (b.alunos ?? 0) - (a.alunos ?? 0) || a.id.localeCompare(b.id);
  const p1Drawn = makeLotes("P1", byRank("P1").filter((i) => i.drawn), "p1s").sort((a, b) => (b.alunos ?? 0) - (a.alunos ?? 0) || a.id.localeCompare(b.id));
  const p1Rest = makeLotes("P1", byRank("P1").filter((i) => !i.drawn), "p1").sort(byDate);
  for (const band of ["P2", "P3", "P4"] as Band[]) lotes.push(...makeLotes(band, byRank(band), band.toLowerCase()));
  const p1Lotes = [...p1Drawn, ...p1Rest];
  lotes.push(...p1Lotes);
  const ordered = [...p1Lotes, ...lotes.filter((l) => l.faixa !== "P1")];

  const count = (b: Band) => items.filter((i) => i.band === b).length;
  const p1Days = (n: number) => items.filter((i) => i.band === "P1" && i.date! <= addDaysISO(today, n)).length;
  report.planos = { analisados: plans.length, cadernos: quizActs, cadernosPendentes: pendingActs, questoesSorteadas: drawnTotal, sorteadasDistintas: allDrawn.size, candidatasDistintas: allCandidates.size };
  report.faixas = {
    P1: { questoes: count("P1"), lotes: p1Lotes.length, ate7dias: p1Days(7), ate14dias: p1Days(14), ate30dias: p1Days(30), jaSorteadas: items.filter((i) => i.band === "P1" && i.drawn).length },
    P2: { questoes: count("P2"), lotes: lotes.filter((l) => l.faixa === "P2").length },
    P3: { questoes: count("P3"), lotes: lotes.filter((l) => l.faixa === "P3").length },
    P4: { questoes: count("P4"), lotes: lotes.filter((l) => l.faixa === "P4").length },
  };
  report.jaComentadas = { noBanco: [...byId.values()].filter((q) => q.commented).length, noConteudo: done.size };
  mkdirSync(COMMENTS_DIR, { recursive: true });
  writeFileSync(join(COMMENTS_DIR, "_fila.json"), JSON.stringify({ ...report, lotes: ordered }, null, 1) + "\n");

  // ---------- pacotes ----------
  const wanted = ordered.filter((l) => pacotes === "TODAS" || l.faixa === pacotes);
  if (pacotes !== "NENHUM" && wanted.length) {
    mkdirSync(join(CACHE_DIR, "img"), { recursive: true });
    const chapters = chapterMap();
    const ids = wanted.flatMap((l) => l.questoes);
    const full = new Map<string, Awaited<ReturnType<typeof fetchFull>>[number]>();
    async function fetchFull(c: string[]) {
      return db.question.findMany({
        where: { id: { in: c } },
        select: { id: true, segmentId: true, statement: true, support: true, kind: true, banca: true, ano: true, orgao: true, cargo: true, topic: true, contentHash: true, options: { select: { label: true, text: true, isCorrect: true }, orderBy: { label: "asc" } } },
      });
    }
    for (let i = 0; i < ids.length; i += 500) for (const q of await fetchFull(ids.slice(i, i + 500))) full.set(q.id, q);
    const imgIds = new Set<string>();
    const imgRe = /\/q-img\/([0-9a-f]{64})/g;
    for (const q of full.values()) {
      for (const t of [q.statement, q.support ?? "", ...q.options.map((o) => o.text)]) for (const m of t.matchAll(imgRe)) imgIds.add(m[1]);
    }
    const missingImgs = [...imgIds].filter((id) => !existsSync(join(CACHE_DIR, "img", `${id}.png`)));
    for (let i = 0; i < missingImgs.length; i += 100) {
      for (const im of await db.questionImage.findMany({ where: { id: { in: missingImgs.slice(i, i + 100) } }, select: { id: true, data: true } })) {
        writeFileSync(join(CACHE_DIR, "img", `${im.id}.png`), Buffer.from(im.data));
      }
    }
    for (const l of wanted) {
      const seg = segInfo.get(l.trecho);
      const cap = chapters.get(l.trecho);
      const pkg = {
        lote: l.id, faixa: l.faixa, trecho: l.trecho, arquivoDeSaida: l.arquivo,
        aula: seg?.aula.title ?? null, topicoInicial: seg?.startTopic ?? null,
        capitulo: cap?.path ?? null, capituloAprovado: cap?.noIndice ?? false, resumo: summaryPath(l.trecho),
        questoes: l.questoes.map((id) => {
          const q = full.get(id)!;
          const figs = [...new Set([q.statement, q.support ?? "", ...q.options.map((o) => o.text)].flatMap((t) => [...t.matchAll(imgRe)].map((m) => `pipeline/.cache/questoes-comentar/img/${m[1]}.png`)))];
          return {
            id: q.id, tipo: q.kind, banca: q.banca, ano: q.ano, assunto: q.topic, contentHash: q.contentHash,
            textoBase: q.support, enunciado: q.statement,
            alternativas: q.kind === "CERTO_ERRADO" ? [] : q.options.map((o) => ({ letra: o.label, texto: o.text })),
            gabarito: q.options.find((o) => o.isCorrect)?.label ?? null,
            figuras: figs,
          };
        }),
      };
      writeFileSync(join(CACHE_DIR, `${l.id.replace("/", "__")}.json`), JSON.stringify(pkg, null, 1));
    }
    report.pacotes = { faixa: pacotes, lotes: wanted.length, questoes: ids.length, figuras: imgIds.size, pasta: CACHE_DIR };
  }
  console.log(JSON.stringify(report, null, 1));
  await db.$disconnect();
})().catch(async (e) => {
  console.error(e);
  await db.$disconnect();
  process.exitCode = 1;
});
