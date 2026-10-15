// Backup verificável (SOMENTE LEITURA) do acervo de questões e de tudo o que aponta para ele.
//
//   npx tsx scripts/questoes-backup.ts [--remoto] [--saida <pasta>]
//   npx tsx scripts/questoes-backup.ts --verificar <pasta>        # confere um backup já feito
//
// Lê numa única transação READ ONLY / REPEATABLE READ (fotografia consistente) e grava, em
// <pasta> (padrão: ../backups/questoes-<destino>-<AAAAMMDD-HHMMSS>/, fora do git):
//   Question.jsonl, QuestionOption.jsonl, QuestionImage.jsonl (bytes em base64), QuizSession.jsonl,
//   QuizAnswer.jsonl, QuestionReport.jsonl, refs.json (ids de Segment/Aula/Subject/EditalItem) e
//   manifest.json (contagem e sha256 de cada arquivo + checagens de integridade referencial).
// Nada é escrito no banco. Restauração: scripts/questoes-restore.ts (ver o cabeçalho de lá).
import "dotenv/config";
import { createHash } from "node:crypto";
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";

const args = process.argv.slice(2);
const remote = args.includes("--remoto");
const verifyDir = args.includes("--verificar") ? args[args.indexOf("--verificar") + 1] : null;

function remoteUrl(): string {
  const f = resolve(__dirname, "..", ".env.remote");
  if (!existsSync(f)) throw new Error("web/.env.remote não existe");
  const m = readFileSync(f, "utf8").match(/^\s*REMOTE_DATABASE_URL\s*=\s*"?([^"\r\n]+)"?/m);
  if (!m) throw new Error("REMOTE_DATABASE_URL ausente em web/.env.remote");
  return m[1];
}

const TABLES = ["Question", "QuestionOption", "QuestionImage", "QuizSession", "QuizAnswer", "QuestionReport"] as const;
type Table = (typeof TABLES)[number];
const ORDER: Record<Table, string> = {
  Question: `"id"`,
  QuestionOption: `"questionId", "label"`,
  QuestionImage: `"id"`,
  QuizSession: `"id"`,
  QuizAnswer: `"sessionId", "position"`,
  QuestionReport: `"id"`,
};

const sha256 = (b: Buffer | string) => createHash("sha256").update(b).digest("hex");

function toJsonValue(v: unknown): unknown {
  if (v instanceof Uint8Array) return { $bytes: Buffer.from(v).toString("base64") };
  if (v instanceof Date) return { $date: v.toISOString() };
  if (typeof v === "bigint") return Number(v);
  return v;
}

function readJsonl(file: string): Record<string, unknown>[] {
  return readFileSync(file, "utf8")
    .split("\n")
    .filter((l) => l.trim())
    .map((l) => JSON.parse(l));
}

type Manifest = {
  formato: 1;
  destino: string;
  host: string;
  criadoEm: string;
  arquivos: Record<string, { linhas: number; sha256: string }>;
  integridade: Record<string, number>;
};

function integrity(dir: string): Record<string, number> {
  const q = new Set(readJsonl(join(dir, "Question.jsonl")).map((r) => r.id as string));
  const imgs = new Set(readJsonl(join(dir, "QuestionImage.jsonl")).map((r) => r.id as string));
  const sessions = new Set(readJsonl(join(dir, "QuizSession.jsonl")).map((r) => r.id as string));
  const refs = JSON.parse(readFileSync(join(dir, "refs.json"), "utf8")) as Record<string, string[]>;
  const seg = new Set(refs.Segment);
  const edital = new Set(refs.EditalItem);
  const opts = readJsonl(join(dir, "QuestionOption.jsonl"));
  const answers = readJsonl(join(dir, "QuizAnswer.jsonl"));
  const reports = readJsonl(join(dir, "QuestionReport.jsonl"));
  const questions = readJsonl(join(dir, "Question.jsonl"));
  const imgRefs = new Set<string>();
  for (const r of questions) {
    for (const f of ["statement", "support"] as const) {
      for (const m of String(r[f] ?? "").matchAll(/\/q-img\/([0-9a-f]{64})/g)) imgRefs.add(m[1]);
    }
  }
  for (const o of opts) for (const m of String(o.text ?? "").matchAll(/\/q-img\/([0-9a-f]{64})/g)) imgRefs.add(m[1]);
  return {
    opcoesSemQuestao: opts.filter((o) => !q.has(o.questionId as string)).length,
    respostasSemQuestao: answers.filter((a) => !q.has(a.questionId as string)).length,
    respostasSemSessao: answers.filter((a) => !sessions.has(a.sessionId as string)).length,
    denunciasSemQuestao: reports.filter((r) => !q.has(r.questionId as string)).length,
    questoesComTrechoInexistente: questions.filter((r) => !seg.has(r.segmentId as string)).length,
    questoesComItemEditalInexistente: questions.filter((r) => r.editalItemId && !edital.has(r.editalItemId as string)).length,
    figurasReferenciadas: imgRefs.size,
    figurasReferenciadasAusentes: [...imgRefs].filter((s) => !imgs.has(s)).length,
  };
}

function verify(dir: string): boolean {
  const man = JSON.parse(readFileSync(join(dir, "manifest.json"), "utf8")) as Manifest;
  let ok = true;
  for (const [name, info] of Object.entries(man.arquivos)) {
    const buf = readFileSync(join(dir, name));
    const lines = name.endsWith(".jsonl") ? buf.toString("utf8").split("\n").filter((l) => l.trim()).length : 1;
    const good = sha256(buf) === info.sha256 && lines === info.linhas;
    if (!good) ok = false;
    console.log(`${good ? "ok   " : "FALHA"} ${name.padEnd(22)} ${lines} linhas`);
  }
  const integ = integrity(dir);
  for (const [k, v] of Object.entries(integ)) {
    if (k !== "figurasReferenciadas" && v !== man.integridade[k]) ok = false;
    console.log(`      ${k.padEnd(34)} ${v}${v !== man.integridade[k] ? ` (manifesto: ${man.integridade[k]})` : ""}`);
  }
  // cada imagem: o id é o sha256 do PNG
  const badImg = readJsonl(join(dir, "QuestionImage.jsonl")).filter(
    (r) => sha256(Buffer.from((r.data as { $bytes: string }).$bytes, "base64")) !== r.id,
  ).length;
  console.log(`      figurasComConteudoDivergenteDoId   ${badImg}`);
  console.log(ok ? "BACKUP ÍNTEGRO" : "BACKUP COM PROBLEMA");
  return ok;
}

async function main() {
  if (verifyDir) {
    process.exitCode = verify(resolve(verifyDir)) ? 0 : 1;
    return;
  }
  const url = (remote ? remoteUrl() : process.env.DATABASE_URL || "").replace(/([?&])pgbouncer=true(&|$)/, (_, a, b) => (b ? a : ""));
  if (!url) throw new Error("DATABASE_URL vazio");
  const host = new URL(url).hostname;
  const stamp = new Date().toISOString().replace(/[-:]/g, "").replace("T", "-").slice(0, 15);
  const outArg = args.includes("--saida") ? args[args.indexOf("--saida") + 1] : null;
  const dir = resolve(outArg ?? join(__dirname, "..", "..", "backups", `questoes-${remote ? "remoto" : "local"}-${stamp}`));
  mkdirSync(dir, { recursive: true });

  const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: url }) });
  const man: Manifest = { formato: 1, destino: remote ? "remoto" : "local", host, criadoEm: new Date().toISOString(), arquivos: {}, integridade: {} };
  try {
    await db.$transaction(
      async (tx) => {
        await tx.$executeRawUnsafe("SET TRANSACTION ISOLATION LEVEL REPEATABLE READ, READ ONLY");
        for (const t of TABLES) {
          const rows = await tx.$queryRawUnsafe<Record<string, unknown>[]>(`SELECT * FROM "${t}" ORDER BY ${ORDER[t]}`);
          const body = rows.map((r) => JSON.stringify(Object.fromEntries(Object.entries(r).map(([k, v]) => [k, toJsonValue(v)])))).join("\n") + "\n";
          writeFileSync(join(dir, `${t}.jsonl`), body, "utf8");
          man.arquivos[`${t}.jsonl`] = { linhas: rows.length, sha256: sha256(Buffer.from(body, "utf8")) };
          console.log(`${t.padEnd(16)} ${rows.length}`);
        }
        const refs: Record<string, string[]> = {};
        for (const t of ["Subject", "Aula", "Segment", "EditalItem"]) {
          refs[t] = (await tx.$queryRawUnsafe<{ id: string }[]>(`SELECT id FROM "${t}" ORDER BY id`)).map((r) => r.id);
        }
        const body = JSON.stringify(refs);
        writeFileSync(join(dir, "refs.json"), body, "utf8");
        man.arquivos["refs.json"] = { linhas: 1, sha256: sha256(Buffer.from(body, "utf8")) };
      },
      { timeout: 600_000, maxWait: 60_000 },
    );
  } finally {
    await db.$disconnect();
  }
  man.integridade = integrity(dir);
  writeFileSync(join(dir, "manifest.json"), JSON.stringify(man, null, 1), "utf8");
  console.log(`backup em ${dir}`);
  if (!verify(dir)) process.exitCode = 1;
}

main().catch((e) => {
  console.error(e);
  process.exitCode = 1;
});
