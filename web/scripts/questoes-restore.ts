// Restauração do acervo de questões a partir de um backup de scripts/questoes-backup.ts.
//
//   npx tsx scripts/questoes-restore.ts <pasta-do-backup>                       # SIMULAÇÃO no banco local (padrão)
//   npx tsx scripts/questoes-restore.ts <pasta-do-backup> --aplicar             # aplica no banco local
//   npx tsx scripts/questoes-restore.ts <pasta-do-backup> --remoto              # simulação na produção (só leitura)
//   npx tsx scripts/questoes-restore.ts <pasta-do-backup> --remoto --aplicar --confirmo-producao
//
// O que a restauração faz (nesta ordem; cada questão na sua transação):
//   1. confere o backup (sha256 e integridade, como `questoes-backup.ts --verificar`); se falhar, para;
//   2. figuras do backup ausentes no banco são recriadas (nunca apaga figura);
//   3. cada questão do backup volta a ter TODOS os campos do backup (cria se faltar) e, se as alternativas
//      diferirem, as alternativas do backup (as respostas guardam o rótulo, não o id da alternativa);
//   4. questão que existe no banco mas não no backup NÃO é apagada: vira RETIRED (preserva respostas);
//   5. nunca toca em QuizSession, QuizAnswer, QuestionReport, planos ou usuários; ao fim confere que as
//      contagens deles não mudaram e que toda resposta continua apontando para uma questão existente.
// Questão cujo trecho/aula/disciplina não existe mais no banco é listada e pulada (rode o seed de estrutura).
import "dotenv/config";
import { createHash } from "node:crypto";
import { existsSync, readFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";

const args = process.argv.slice(2);
const dir = args.find((a) => !a.startsWith("--"));
const remote = args.includes("--remoto");
const apply = args.includes("--aplicar");
if (!dir) throw new Error("informe a pasta do backup");
if (remote && apply && !args.includes("--confirmo-producao")) {
  throw new Error("restaurar a PRODUÇÃO exige --confirmo-producao (e aprovação explícita do dono)");
}

function remoteUrl(): string {
  const f = resolve(__dirname, "..", ".env.remote");
  if (!existsSync(f)) throw new Error("web/.env.remote não existe");
  const m = readFileSync(f, "utf8").match(/^\s*REMOTE_DATABASE_URL\s*=\s*"?([^"\r\n]+)"?/m);
  if (!m) throw new Error("REMOTE_DATABASE_URL ausente em web/.env.remote");
  return m[1];
}

type Row = Record<string, unknown>;
const sha256 = (b: Buffer | string) => createHash("sha256").update(b).digest("hex");

function readJsonl(file: string): Row[] {
  return readFileSync(file, "utf8")
    .split("\n")
    .filter((l) => l.trim())
    .map((l) => JSON.parse(l));
}

function fromJson(v: unknown): unknown {
  if (v && typeof v === "object" && "$date" in (v as object)) return new Date((v as { $date: string }).$date);
  if (v && typeof v === "object" && "$bytes" in (v as object)) return new Uint8Array(Buffer.from((v as { $bytes: string }).$bytes, "base64"));
  return v;
}

function norm(v: unknown): string {
  if (v instanceof Date) return v.toISOString();
  if (v instanceof Uint8Array) return sha256(Buffer.from(v));
  if (v === undefined) return "null";
  return JSON.stringify(v);
}

function checkBackup(d: string): void {
  const man = JSON.parse(readFileSync(join(d, "manifest.json"), "utf8")) as { arquivos: Record<string, { linhas: number; sha256: string }> };
  for (const [name, info] of Object.entries(man.arquivos)) {
    const buf = readFileSync(join(d, name));
    if (sha256(buf) !== info.sha256) throw new Error(`backup corrompido: ${name} (sha256 diferente do manifesto)`);
  }
}

async function main() {
  const d = resolve(dir!);
  checkBackup(d);
  const url = (remote ? remoteUrl() : process.env.DATABASE_URL || "").replace(/([?&])pgbouncer=true(&|$)/, (_, a, b) => (b ? a : ""));
  const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: url }) });
  const report = {
    destino: remote ? "remoto" : "local",
    modo: apply ? "APLICAR" : "SIMULAÇÃO",
    figurasAusentes: 0,
    questoesAusentes: 0,
    questoesDiferentes: 0,
    camposDiferentes: {} as Record<string, number>,
    alternativasDiferentes: 0,
    questoesForaDoBackup: 0,
    questoesForaDoBackupJaRetiradas: 0,
    puladasSemEstrutura: [] as string[],
    aplicadas: 0,
    dadosDeAlunos: {} as Record<string, unknown>,
  };
  try {
    const bq = readJsonl(join(d, "Question.jsonl"));
    const bo = readJsonl(join(d, "QuestionOption.jsonl"));
    const bi = readJsonl(join(d, "QuestionImage.jsonl"));
    const optsBy = new Map<string, Row[]>();
    for (const o of bo) optsBy.set(o.questionId as string, [...(optsBy.get(o.questionId as string) ?? []), o]);

    const before = {
      sessoes: await db.quizSession.count(),
      respostas: await db.quizAnswer.count(),
      denuncias: await db.questionReport.count(),
    };

    // 1. figuras
    const haveImg = new Set((await db.questionImage.findMany({ select: { id: true } })).map((r) => r.id));
    const missingImg = bi.filter((r) => !haveImg.has(r.id as string));
    report.figurasAusentes = missingImg.length;
    if (apply) {
      for (const r of missingImg) {
        await db.questionImage.create({ data: Object.fromEntries(Object.entries(r).map(([k, v]) => [k, fromJson(v)])) as never });
      }
    }

    // 2. questões e alternativas
    const segIds = new Set((await db.segment.findMany({ select: { id: true } })).map((s) => s.id));
    const aulaIds = new Set((await db.aula.findMany({ select: { id: true } })).map((s) => s.id));
    const editalIds = new Set((await db.editalItem.findMany({ select: { id: true } })).map((s) => s.id));
    const current = new Map<string, Row>();
    for (const r of await db.$queryRawUnsafe<Row[]>(`SELECT * FROM "Question"`)) current.set(r.id as string, r);
    const curOpts = new Map<string, Row[]>();
    for (const o of await db.$queryRawUnsafe<Row[]>(`SELECT * FROM "QuestionOption" ORDER BY "questionId", label`)) {
      curOpts.set(o.questionId as string, [...(curOpts.get(o.questionId as string) ?? []), o]);
    }
    const optKey = (os: Row[] | undefined) =>
      JSON.stringify((os ?? []).map((o) => [o.label, o.text, o.isCorrect]).sort((a, b) => String(a[0]).localeCompare(String(b[0]))));

    for (const raw of bq) {
      const id = raw.id as string;
      const data = Object.fromEntries(Object.entries(raw).map(([k, v]) => [k, fromJson(v)]));
      if (!segIds.has(data.segmentId as string) || !aulaIds.has(data.aulaId as string) || (data.editalItemId && !editalIds.has(data.editalItemId as string))) {
        report.puladasSemEstrutura.push(id);
        continue;
      }
      const cur = current.get(id);
      const diffFields = cur ? Object.keys(data).filter((k) => norm(data[k]) !== norm(cur[k])) : Object.keys(data);
      const optsDiffer = optKey(optsBy.get(id)) !== optKey(curOpts.get(id));
      if (!cur) report.questoesAusentes++;
      else if (diffFields.length) report.questoesDiferentes++;
      for (const k of cur ? diffFields : []) report.camposDiferentes[k] = (report.camposDiferentes[k] ?? 0) + 1;
      if (optsDiffer) report.alternativasDiferentes++;
      if (!apply || (!diffFields.length && !optsDiffer)) continue;
      const { id: _id, ...rest } = data;
      await db.$transaction(async (tx) => {
        if (cur) await tx.question.update({ where: { id }, data: rest as never });
        else await tx.question.create({ data: data as never });
        if (optsDiffer) {
          await tx.questionOption.deleteMany({ where: { questionId: id } });
          await tx.questionOption.createMany({
            data: (optsBy.get(id) ?? []).map((o) => ({ id: o.id as string, questionId: id, label: o.label as string, text: o.text as string, isCorrect: o.isCorrect as boolean })),
          });
        }
      });
      report.aplicadas++;
    }

    // 3. questões fora do backup: retiradas, nunca apagadas
    const inBackup = new Set(bq.map((r) => r.id as string));
    const extra = [...current.values()].filter((r) => !inBackup.has(r.id as string));
    report.questoesForaDoBackup = extra.length;
    report.questoesForaDoBackupJaRetiradas = extra.filter((r) => r.status === "RETIRED").length;
    if (apply) {
      const ids = extra.filter((r) => r.status !== "RETIRED").map((r) => r.id as string);
      for (let i = 0; i < ids.length; i += 500) {
        await db.question.updateMany({ where: { id: { in: ids.slice(i, i + 500) } }, data: { status: "RETIRED" } });
      }
    }

    // 4. dados de alunos intactos
    const after = {
      sessoes: await db.quizSession.count(),
      respostas: await db.quizAnswer.count(),
      denuncias: await db.questionReport.count(),
    };
    const orphan = await db.$queryRawUnsafe<{ n: bigint }[]>(
      `SELECT count(*) AS n FROM "QuizAnswer" a LEFT JOIN "Question" q ON q.id = a."questionId" WHERE q.id IS NULL`,
    );
    report.dadosDeAlunos = { antes: before, depois: after, respostasSemQuestao: Number(orphan[0].n), intactos: JSON.stringify(before) === JSON.stringify(after) && Number(orphan[0].n) === 0 };
  } finally {
    await db.$disconnect();
  }
  console.log(JSON.stringify(report, null, 1));
  if (!(report.dadosDeAlunos as { intactos: boolean }).intactos) process.exitCode = 1;
}

main().catch((e) => {
  console.error(e);
  process.exitCode = 1;
});
