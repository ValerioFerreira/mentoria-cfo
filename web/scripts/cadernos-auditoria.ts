// Levantamento (SÓ LEITURA) de quantas questões cada caderno de Questões dos planos tem à disposição, por concurso.
//   npx tsx scripts/cadernos-auditoria.ts [--remoto] [--concurso CBMPE_OFICIAL,PCPE_AGENTE] [--saida pasta]
//
// Dois recortes, ambos com as mesmas regras do app (banca do concurso, só APPROVED, completa com trechos já estudados):
//  1. PLANOS REAIS: cada atividade de Questões dos planos ACTIVE/PENDING_ANALYSIS do concurso, com as questões dos trechos
//     do próprio caderno, as que o app acrescentaria dos trechos já estudados e o total que o aluno recebe (limite = o que o
//     caderno pede: 25, ou 15 no Turbo). Aponta planos antigos sem `dayIndex`, que não completam.
//  2. OFERTA POR TRECHO: questões elegíveis em cada trecho do concurso e o acumulado da disciplina, para saber onde falta
//     material antes mesmo de existir um plano.
import "dotenv/config";
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient, type Contest } from "../src/generated/prisma/client";
import { INEDITA_BANCA, contestBancas } from "../src/lib/quiz/banca";
import { CONTEST_SUBJECTS } from "../src/lib/contests";

const args = process.argv.slice(2);
const remote = args.includes("--remoto");
const arg = (n: string) => (args.includes(n) ? args[args.indexOf(n) + 1] : undefined);
const contests = (arg("--concurso") ?? "CBMPE_OFICIAL,PCPE_AGENTE").split(",") as Contest[];
const stamp = new Date().toISOString().slice(0, 10);
const outDir = resolve(arg("--saida") ?? resolve(__dirname, "../reports", `cadernos-${stamp}-${remote ? "remoto" : "local"}`));

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

async function supplyBySegment(contest: Contest): Promise<Map<string, number>> {
  const g = await db.question.groupBy({
    by: ["segmentId"],
    where: { status: "APPROVED", banca: { in: contestBancas(contest) } },
    _count: true,
  });
  return new Map(g.map((r) => [r.segmentId, r._count]));
}

/** Questões aprovadas de QUALQUER banca (menos as inéditas), para dimensionar o que sobra fora da banca do concurso. */
async function supplyAnyBanca(): Promise<Map<string, number>> {
  const g = await db.question.groupBy({ by: ["segmentId"], where: { status: "APPROVED", banca: { not: INEDITA_BANCA } }, _count: true });
  return new Map(g.map((r) => [r.segmentId, r._count]));
}

async function realPlans(contest: Contest, supply: Map<string, number>, names: Map<string, string>) {
  const plans = await db.plan.findMany({
    where: { status: { in: ["ACTIVE", "PENDING_ANALYSIS"] }, ...(contest === "CBMPE_OFICIAL" ? { OR: [{ contest }, { contest: null }] } : { contest }) },
    select: { id: true, status: true, user: { select: { email: true } } },
  });
  const rows: Row[] = [];
  let semDia = 0;
  for (const p of plans) {
    const acts = await db.activity.findMany({
      where: { planId: p.id, type: { in: ["QUESTOES", "TEORIA"] } },
      select: { id: true, type: true, subjectId: true, dayIndex: true, quizQuestions: true, quizMixed: true, turbo: true, week: { select: { index: true } }, segments: { select: { segmentId: true } }, aula: { select: { title: true } } },
    });
    const teorias = acts.filter((a) => a.type === "TEORIA");
    for (const a of acts.filter((x) => x.type === "QUESTOES")) {
      const want = a.quizQuestions ?? 25;
      const own = [...new Set(a.segments.map((s) => s.segmentId))];
      const primary = own.reduce((s, id) => s + (supply.get(id) ?? 0), 0);
      let extra = 0;
      if (primary < want) {
        if (a.dayIndex === null) semDia++;
        else {
          const prior = new Set(
            teorias
              .filter((t) => t.subjectId === a.subjectId && (t.week.index < a.week.index || (t.week.index === a.week.index && (t.dayIndex ?? 99) < a.dayIndex!)))
              .flatMap((t) => t.segments.map((s) => s.segmentId)),
          );
          for (const id of own) prior.delete(id);
          extra = [...prior].reduce((s, id) => s + (supply.get(id) ?? 0), 0);
        }
      }
      const total = primary >= want ? primary : primary + extra;
      rows.push({
        concurso: contest, plano: p.id, statusPlano: p.status, aluno: p.user.email, disciplina: names.get(a.subjectId) ?? a.subjectId, aula: a.aula.title,
        atividade: a.id, semana: a.week.index, dia: a.dayIndex, turbo: a.turbo, misto: a.quizMixed, pede: want, trechos: own.length,
        dosTrechos: primary, completadoDosJaEstudados: extra, recebe: Math.min(want, total), falta: Math.max(0, want - total),
      });
    }
  }
  return { rows, semDia, plans: plans.length };
}

(async () => {
  mkdirSync(outDir, { recursive: true });
  const subjects = await db.subject.findMany({ select: { id: true, name: true } });
  const names = new Map(subjects.map((s) => [s.id, s.name]));
  const summary: Record<string, unknown> = { destino: remote ? "remoto" : "local", geradoEm: new Date().toISOString() };
  for (const contest of contests) {
    const supply = await supplyBySegment(contest);
    const anyBanca = await supplyAnyBanca();
    const subs = (CONTEST_SUBJECTS as Record<string, string[]>)[contest] ?? [];
    // 2. oferta por trecho
    const segs = await db.segment.findMany({
      where: { aula: { subjectId: { in: subs }, selectable: true, OR: [{ onlyContests: { isEmpty: true } }, { onlyContests: { has: contest } }] } },
      select: { id: true, sortOrder: true, pages: true, aula: { select: { id: true, title: true, subjectId: true, number: true } } },
    });
    segs.sort((a, b) => a.aula.subjectId.localeCompare(b.aula.subjectId) || a.aula.number - b.aula.number || a.sortOrder - b.sortOrder);
    const oferta: Row[] = [];
    const cum = new Map<string, number>();
    for (const s of segs) {
      const n = supply.get(s.id) ?? 0;
      const c = (cum.get(s.aula.subjectId) ?? 0) + n;
      cum.set(s.aula.subjectId, c);
      oferta.push({ concurso: contest, disciplina: names.get(s.aula.subjectId) ?? s.aula.subjectId, aula: s.aula.title, trecho: s.id, questoes: n, outrasBancas: (anyBanca.get(s.id) ?? 0) - n, acumuladoDaDisciplina: c, abaixoDe7: n < 7 });
    }
    writeFileSync(resolve(outDir, `oferta-por-trecho-${contest}.csv`), csv(oferta));
    // 1. planos reais
    const { rows, semDia, plans } = await realPlans(contest, supply, names);
    writeFileSync(resolve(outDir, `planos-reais-${contest}.csv`), csv(rows));
    const curtos = rows.filter((r) => Number(r.falta) > 0);
    writeFileSync(resolve(outDir, `planos-reais-CURTOS-${contest}.csv`), csv(curtos));
    const porDisc: Record<string, { cadernos: number; curtos: number; menor: number }> = {};
    for (const r of rows) {
      const d = String(r.disciplina);
      const x = (porDisc[d] ??= { cadernos: 0, curtos: 0, menor: 99 });
      x.cadernos++;
      if (Number(r.falta) > 0) x.curtos++;
      x.menor = Math.min(x.menor, Number(r.recebe));
    }
    const ofertaPorDisc: Record<string, { trechos: number; semQuestao: number; abaixoDe6: number; total: number }> = {};
    for (const r of oferta) {
      const d = String(r.disciplina);
      const x = (ofertaPorDisc[d] ??= { trechos: 0, semQuestao: 0, abaixoDe6: 0, total: 0 });
      x.trechos++;
      x.total += Number(r.questoes);
      if (Number(r.questoes) === 0) x.semQuestao++;
      if (r.abaixoDe7) x.abaixoDe6++;
    }
    summary[contest] = {
      bancas: contestBancas(contest),
      planosAnalisados: plans, cadernosNosPlanos: rows.length, cadernosCurtos: curtos.length, cadernosCurtosSemDiaNoPlano: semDia,
      porDisciplinaNosPlanos: porDisc, ofertaPorDisciplina: ofertaPorDisc,
    };
  }
  writeFileSync(resolve(outDir, "resumo.json"), JSON.stringify(summary, null, 1));
  console.log(JSON.stringify(summary, null, 1));
  console.log("saída:", outDir);
  await db.$disconnect();
})();
