// Levantamento (SÓ LEITURA) dos assuntos com menos questões para os cadernos de Questões do CBMPE Oficial e do CFOA.
//   npx tsx scripts/cadernos-deficit.ts [--remoto] [--concurso CBMPE_OFICIAL,CBMPE_CFOA] [--saida pasta]
//
// Mesmas regras do app (lib/quiz/pool.ts + banca.ts): APPROVED; questões da banca do concurso (AOCP; no CFOA só múltipla
// escolha) nos trechos do caderno → completa com os trechos da mesma disciplina já estudados na Teoria → reforço (múltipla
// escolha de outras bancas e inéditas MentorIA) dos trechos do caderno e dos já estudados.
// Três recortes:
//  1. GRADE DE PLANOS: gera planos variados com o motor (horas × nível × Turbo × disciplinas × marcações) e calcula o que
//     cada caderno recebe; lista os cadernos abaixo do que pedem (25, ou 15 no Turbo).
//  2. POR AULA: questões da aula inteira (trechos do edital do concurso). É o piso de um caderno da 1ª aula da disciplina
//     no plano, porque toda a Teoria da aula vem antes dos cadernos dela.
//  3. POR TRECHO: o pior caso (caderno de um trecho só, sem nada estudado antes) e quantas faltam para 25.
import "dotenv/config";
import { mkdirSync, readdirSync, readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient, type Contest } from "../src/generated/prisma/client";
import { AOCP_BANCAS, INEDITA_BANCA } from "../src/lib/quiz/banca";
import { CONTEST_SUBJECTS } from "../src/lib/contests";
import { generatePlan } from "../src/lib/planner";
import { loadCatalog, loadExamQuestions, loadImportance, loadSegments } from "../src/lib/planner/fixtures";
import type { Known, Level } from "../src/lib/planner/types";

const args = process.argv.slice(2);
const remote = args.includes("--remoto");
const arg = (n: string) => (args.includes(n) ? args[args.indexOf(n) + 1] : undefined);
const contests = (arg("--concurso") ?? "CBMPE_OFICIAL,CBMPE_CFOA").split(",") as Contest[];
const stamp = new Date().toISOString().slice(0, 10);
const outDir = resolve(arg("--saida") ?? resolve(__dirname, "../reports", `deficit-${stamp}-${remote ? "remoto" : "local"}`));
const WANT = 25;

function remoteUrl(): string {
  const m = readFileSync(resolve(__dirname, "..", ".env.remote"), "utf8").match(/^\s*REMOTE_DATABASE_URL\s*=\s*"?([^"\r\n]+)"?/m);
  if (!m) throw new Error("REMOTE_DATABASE_URL ausente em web/.env.remote");
  return m[1];
}
const url = (remote ? remoteUrl() : process.env.DATABASE_URL || "").replace(/([?&])pgbouncer=true(&|$)/, (_, a, b) => (b ? a : ""));
if (!url) throw new Error("DATABASE_URL vazio");
const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: url }) });

type Row = Record<string, string | number | boolean | null>;
const csv = (rows: Row[]) => {
  if (!rows.length) return "";
  const h = Object.keys(rows[0]);
  const q = (v: unknown) => `"${String(v ?? "").replace(/"/g, '""')}"`;
  return "﻿" + h.join(";") + "\n" + rows.map((r) => h.map((k) => q(r[k])).join(";")).join("\n") + "\n";
};

interface Supply {
  prim: number; // banca do concurso (o que entra primeiro)
  reinf: number; // reforço: MC de outras bancas + inéditas MC
  ined: number; // parte do reforço que é inédita
  ceAocp: number; // AOCP certo/errado (não serve ao CFOA)
  draft: number; // rascunhos (DRAFT) que serviriam se aprovados
}

async function loadSupply(contest: Contest): Promise<Map<string, Supply>> {
  const rows = await db.question.groupBy({ by: ["segmentId", "banca", "kind", "status"], _count: true });
  const m = new Map<string, Supply>();
  const get = (id: string) => m.get(id) ?? (m.set(id, { prim: 0, reinf: 0, ined: 0, ceAocp: 0, draft: 0 }), m.get(id)!);
  for (const r of rows) {
    if (!r.segmentId) continue;
    const s = get(r.segmentId);
    const aocp = AOCP_BANCAS.includes(r.banca ?? "");
    const mc = r.kind === "MULTIPLA_ESCOLHA";
    const isPrim = aocp && (contest !== "CBMPE_CFOA" || mc);
    const isReinf = !aocp && mc;
    if (r.status === "DRAFT" && (isPrim || isReinf)) s.draft += r._count;
    if (r.status !== "APPROVED") continue;
    if (isPrim) s.prim += r._count;
    else if (isReinf) {
      s.reinf += r._count;
      if (r.banca === INEDITA_BANCA) s.ined += r._count;
    } else if (aocp && !mc) s.ceAocp += r._count;
  }
  return m;
}

const catalog = loadCatalog();
const segments = loadSegments();
const sumDir = resolve(__dirname, "../../content/summaries");
const summaries: string[] = [];
for (const d of readdirSync(sumDir, { withFileTypes: true }).filter((x) => x.isDirectory())) {
  for (const f of readdirSync(resolve(sumDir, d.name))) {
    const doc = JSON.parse(readFileSync(resolve(sumDir, d.name, f), "utf8")) as { segments: { id: string }[] };
    for (const s of doc.segments) summaries.push(s.id);
  }
}
const subjectName = new Map(catalog.subjects.map((s) => [s.id, s.name]));
const aulaTitle = new Map(catalog.subjects.flatMap((s) => s.aulas.map((a) => [a.id, a.title] as const)));
const segInfo = new Map(Object.values(segments).flat().map((s) => [s.id, s as typeof s & { startPage?: number; endPage?: number; startTopic?: string }]));

interface Sc { name: string; hours: number; level: Level; subjects: string[]; turbo: boolean; known?: Record<string, Known>; excluded?: string[] }

function scenarios(contest: Contest): Sc[] {
  // uma língua estrangeira só (o motor recusa as duas)
  const ALL = (CONTEST_SUBJECTS as Record<string, string[]>)[contest].filter((id) => id !== "lingua-espanhola");
  const ALL_ES = (CONTEST_SUBJECTS as Record<string, string[]>)[contest].filter((id) => id !== "lingua-inglesa");
  const aulasOf = (ids: string[]) => catalog.subjects.filter((s) => ids.includes(s.id)).flatMap((s) => s.aulas.filter((a) => a.selectable).map((a) => a.id));
  const marks = (ids: string[], every: number, v: Known, offset = 0) => {
    const r: Record<string, Known> = {};
    aulasOf(ids).forEach((a, i) => { if ((i + offset) % every === 0) r[a] = v; });
    return r;
  };
  const out: Sc[] = [];
  for (const hours of [5, 8, 12, 16, 20, 25, 30, 40, 50, 65])
    for (const level of [0, 1, 2, 3] as Level[])
      for (const turbo of [false, true]) out.push({ name: `todas ${hours}h n${level}${turbo ? " T" : ""}`, hours, level, subjects: ALL, turbo });
  // marcações "já estudei"/"domino" mudam qual aula abre cada disciplina
  for (const off of [0, 1, 2, 3])
    for (const hours of [10, 25, 45]) {
      out.push({ name: `todas ${hours}h domino/${off}`, hours, level: 1, subjects: ALL, turbo: false, known: { ...marks(ALL, 4, 2, off), ...marks(ALL, 5, 1, off + 1) } });
      out.push({ name: `todas ${hours}h domino/${off} T`, hours, level: 0, subjects: ALL, turbo: true, known: marks(ALL, 3, 2, off) });
    }
  if (ALL_ES.length !== ALL.length || ALL_ES.some((id) => !ALL.includes(id)))
    for (const hours of [10, 30]) out.push({ name: `todas (espanhol) ${hours}h n1`, hours, level: 1, subjects: ALL_ES, turbo: false });
  const subs = [...new Set([...ALL, ...ALL_ES])];
  for (const id of subs)
    for (const [hours, level, turbo] of [[5, 0, false], [6, 1, true], [10, 2, false], [20, 3, false]] as [number, Level, boolean][])
      out.push({ name: `${id} ${hours}h n${level}${turbo ? " T" : ""}`, hours, level, subjects: [id], turbo });
  // PIOR CASO REAL: o aluno marca "domino" em todas as outras aulas da disciplina e a aula fica sozinha no plano
  for (const id of subs) {
    const aulas = aulasOf([id]);
    for (const keep of aulas) {
      const known = Object.fromEntries(aulas.filter((a) => a !== keep).map((a) => [a, 2 as Known]));
      out.push({ name: `isolada ${keep}`, hours: 10, level: 0, subjects: [id], turbo: false, known });
      out.push({ name: `isolada ${keep} T`, hours: 5, level: 0, subjects: [id], turbo: true, known });
    }
  }
  return out;
}

(async () => {
  mkdirSync(outDir, { recursive: true });
  const summary: Record<string, unknown> = { destino: remote ? "remoto" : "local", geradoEm: new Date().toISOString() };
  for (const contest of contests) {
    const supply = await loadSupply(contest);
    const sup = (id: string) => supply.get(id) ?? { prim: 0, reinf: 0, ined: 0, ceAocp: 0, draft: 0 };
    const importance = loadImportance(contest);
    const subs = (CONTEST_SUBJECTS as Record<string, string[]>)[contest];
    const cfg = await db.contestSetting.findUnique({ where: { contest } }).catch(() => null);
    const examDate = cfg?.examDate ? cfg.examDate.toISOString().slice(0, 10) : null;

    // ---- 2 e 3: oferta por aula e por trecho (só trechos do edital do concurso)
    const segRows: Row[] = [];
    const aulaRows: Row[] = [];
    for (const s of catalog.subjects.filter((x) => subs.includes(x.id))) {
      for (const a of s.aulas) {
        const only = (a as { onlyContests?: string[] }).onlyContests ?? [];
        if (!a.selectable || (only.length && !only.includes(contest))) continue;
        const segs = (segments[a.id] ?? []).filter((x) => importance[x.id] != null);
        if (!segs.length) continue;
        let p = 0, r = 0, i = 0, d = 0, ce = 0;
        for (const x of segs) {
          const v = sup(x.id);
          p += v.prim; r += v.reinf; i += v.ined; d += v.draft; ce += v.ceAocp;
          const info = segInfo.get(x.id);
          segRows.push({
            disciplina: s.name, aula: a.title, trecho: x.id, topico: info?.startTopic ?? "", nota: importance[x.id], banca: v.prim, reforco: v.reinf,
            ineditas: v.ined, total: v.prim + v.reinf, faltamPara25: Math.max(0, WANT - v.prim - v.reinf), rascunhos: v.draft, certoErradoAocp: contest === "CBMPE_CFOA" ? v.ceAocp : "",
          });
        }
        aulaRows.push({
          disciplina: s.name, aula: a.title, aulaId: a.id, trechos: segs.length, banca: p, reforco: r, ineditas: i, total: p + r,
          faltamPara25: Math.max(0, WANT - p - r), rascunhos: d, certoErradoAocp: contest === "CBMPE_CFOA" ? ce : "",
        });
      }
    }
    segRows.sort((a, b) => Number(a.total) - Number(b.total));
    aulaRows.sort((a, b) => Number(a.total) - Number(b.total));
    writeFileSync(resolve(outDir, `por-trecho-${contest}.csv`), csv(segRows));
    writeFileSync(resolve(outDir, `por-aula-${contest}.csv`), csv(aulaRows));

    // ---- 1: grade de planos
    const sc = scenarios(contest);
    const start = "2026-11-02";
    const shortRows: Row[] = [];
    const bySeg = new Map<string, { vezes: number; menor: number }>();
    let quizzes = 0, planos = 0, falhas = 0;
    for (const s of sc) {
      let plan;
      try {
        plan = generatePlan({
          catalog, segments, contest, importance, summaries, examQuestions: loadExamQuestions(contest),
          ...(contest === "CBMPE_CFOA" ? { examTotalQuestions: 100 } : {}),
          startDate: start, firstDay: 0, examDate: examDate ?? "2027-12-31", ...(examDate ? {} : { cycle: 1 }),
          hoursPerWeek: s.hours, subjects: s.subjects.map((id) => ({ id, level: s.level })), known: s.known ?? {}, excludedAulas: s.excluded ?? [], turbo: s.turbo,
        });
      } catch (e) {
        falhas++;
        console.log("falhou", s.name, String(e).slice(0, 100));
        continue;
      }
      planos++;
      const acts = plan.weeks.flatMap((w) => w.activities.map((a) => ({ ...a, ord: (w.index - 1) * 7 + (a.day ?? 0) })));
      const teorias = acts.filter((a) => a.type === "TEORIA");
      for (const q of acts.filter((a) => a.type === "QUESTOES")) {
        quizzes++;
        const want = q.quiz?.questions ?? WANT;
        const own = [...new Set(q.segmentIds)];
        const prior = [...new Set(teorias.filter((t) => t.subjectId === q.subjectId && t.ord < q.ord).flatMap((t) => t.segmentIds))].filter((id) => !own.includes(id));
        const pOwn = own.reduce((n, id) => n + sup(id).prim, 0);
        const pPrior = pOwn >= want ? 0 : prior.reduce((n, id) => n + sup(id).prim, 0);
        const rf = pOwn + pPrior >= want ? 0 : [...own, ...prior].reduce((n, id) => n + sup(id).reinf, 0);
        const got = Math.min(want, pOwn + pPrior + rf);
        if (got < want) {
          shortRows.push({
            cenario: s.name, disciplina: subjectName.get(q.subjectId) ?? q.subjectId, aula: aulaTitle.get(q.aulaId ?? "") ?? q.aulaId ?? "", caderno: q.key,
            semana: Math.floor(q.ord / 7) + 1, pede: want, dosTrechos: pOwn, dosJaEstudados: pPrior, reforco: rf, recebe: got, falta: want - got, trechos: own.join(" "),
          });
          for (const id of own) {
            const b = bySeg.get(id) ?? { vezes: 0, menor: 99 };
            b.vezes++;
            b.menor = Math.min(b.menor, got);
            bySeg.set(id, b);
          }
        }
      }
    }
    writeFileSync(resolve(outDir, `grade-cadernos-curtos-${contest}.csv`), csv(shortRows));
    const porDisc: Record<string, { curtos: number; menor: number; aulas: string[] }> = {};
    for (const r of shortRows) {
      const x = (porDisc[String(r.disciplina)] ??= { curtos: 0, menor: 99, aulas: [] });
      x.curtos++;
      x.menor = Math.min(x.menor, Number(r.recebe));
      if (!x.aulas.includes(String(r.aula))) x.aulas.push(String(r.aula));
    }
    summary[contest] = {
      dataDaProva: examDate ?? "sem data (ciclo do edital)",
      planosNaGrade: planos, falhas, cadernosNaGrade: quizzes, cadernosCurtos: shortRows.length,
      curtosPorDisciplina: porDisc,
      aulasAbaixoDe25: aulaRows.filter((r) => Number(r.total) < WANT).map((r) => `${r.disciplina} · ${r.aula}: ${r.total} (banca ${r.banca} + reforço ${r.reforco})`),
      trechosAbaixoDe25: segRows.filter((r) => Number(r.total) < WANT).length,
      trechosNoEdital: segRows.length,
      faltamParaTodoTrechoTer25: segRows.reduce((n, r) => n + Number(r.faltamPara25), 0),
      faltamParaTodaAulaTer25: aulaRows.reduce((n, r) => n + Number(r.faltamPara25), 0),
      trechosEmCadernosCurtos: [...bySeg.entries()].sort((a, b) => b[1].vezes - a[1].vezes).slice(0, 40).map(([id, v]) => `${id} (${v.vezes}x, menor ${v.menor})`),
    };
    console.log(contest, JSON.stringify(summary[contest], null, 1));
  }
  writeFileSync(resolve(outDir, "resumo.json"), JSON.stringify(summary, null, 1));
  console.log("saída:", outDir);
  await db.$disconnect();
})();
