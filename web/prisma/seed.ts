// Carrega o conteúdo versionado em /content no banco. Idempotente (upsert): pode ser reexecutado
// sem apagar planos, tempos ou respostas dos usuários.
//   1) estrutura: disciplinas, aulas, tópicos, segmentos, lacunas, assuntos do edital  (content/catalog.json, structure/, segments/, edital/)
//   2) autoral:  bizus e questões                                   (content/items/<disciplina>/<aula>.json)
import "dotenv/config";
import fs from "node:fs";
import path from "node:path";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";

const CONTENT = path.resolve(__dirname, "../../content");
const read = <T>(...p: string[]) => JSON.parse(fs.readFileSync(path.join(CONTENT, ...p), "utf-8")) as T;
const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }) });

const chunk = <T>(xs: T[], n: number) => Array.from({ length: Math.ceil(xs.length / n) }, (_, i) => xs.slice(i * n, i * n + n));

interface CatalogAula {
  id: string; number: number; title: string; shortTitle: string; kind: "theory" | "practice";
  edital: "yes" | "partial" | "no"; selectable: boolean; note?: string | null;
  totalPages: number; theoryPages: number; segmentCount: number; commentedPages: number; listPages: number;
  commentedRuns: number[][]; practiceLinks: unknown[]; printedOffset: number; incidence: number;
  source?: "base" | "authored"; materialPath?: string;
}
interface Catalog {
  subjects: { id: string; name: string; block: "I" | "II" | "III"; examQuestions: number; sortOrder: number;
    languageGroup?: string; materialCompleteness?: number; aulas: CatalogAula[] }[];
  gaps: { id: string; subject: string; item: string; evidence: string; severity: string; remedy: string; resolved?: boolean; resolution?: string }[];
}
interface SegJson {
  id: string; aula: string; order: number; startPage: number; endPage: number; startPrinted: number | null;
  endPrinted: number | null; pages: number; load: number; startTopic: string | null; startsMidTopic: boolean;
  stopBeforeTopic: string | null; endsMidTopic: boolean; endTopic: string | null; endsTheory: boolean;
  topicsCovered: string[]; minutes: number;
}
interface EditalFile {
  subject: string;
  items: { id: string; item: string; where?: { aula: string }[] }[];
}
interface BizuItemJson { statement: string; isTrue: boolean; explanation: string }
interface QuestionJson {
  topic?: string; pattern: string; difficulty: number; pageRef?: number; support?: string | null;
  statement: string; options: string[]; answer: string; explanation: string; literal?: boolean;
}
interface ItemsFile {
  aula: string; batch: string; status?: "DRAFT" | "APPROVED";
  segments: { id: string; bizu?: { summary: string[]; teoria: BizuItemJson[]; revisao: BizuItemJson[] }; questions?: QuestionJson[] }[];
}

async function seedStructure() {
  const catalog = read<Catalog>("catalog.json");

  for (const c of chunk(catalog.subjects, 50)) {
    await db.$transaction(
      c.map((s) => {
        const data = {
          name: s.name, block: s.block, examQuestions: s.examQuestions, sortOrder: s.sortOrder,
          languageGroup: s.languageGroup ?? null,
          foreignLanguage: s.id === "lingua-inglesa" ? ("EN" as const) : s.id === "lingua-espanhola" ? ("ES" as const) : null,
          materialCompleteness: s.materialCompleteness ?? 1,
        };
        return db.subject.upsert({ where: { id: s.id }, create: { id: s.id, ...data }, update: data });
      }),
    );
  }

  const aulas = catalog.subjects.flatMap((s) => s.aulas.map((a) => ({ s, a })));
  for (const c of chunk(aulas, 100)) {
    await db.$transaction(
      c.map(({ s, a }) => {
        const data = {
          subjectId: s.id, number: a.number, title: a.title, shortTitle: a.shortTitle,
          kind: a.kind === "practice" ? ("PRACTICE" as const) : ("THEORY" as const),
          edital: a.edital.toUpperCase() as "YES" | "PARTIAL" | "NO",
          selectable: a.selectable, totalPages: a.totalPages, theoryPages: a.theoryPages, segmentCount: a.segmentCount,
          commentedPages: a.commentedPages, listPages: a.listPages, commentedRuns: a.commentedRuns,
          practiceLinks: a.practiceLinks as object[], printedOffset: a.printedOffset, incidence: a.incidence, note: a.note ?? null,
          source: a.source === "authored" ? ("AUTHORED" as const) : ("BASE" as const), materialPath: a.materialPath ?? null,
        };
        return db.aula.upsert({ where: { id: a.id }, create: { id: a.id, ...data }, update: data });
      }),
    );
  }

  let topics = 0;
  let segments = 0;
  for (const s of catalog.subjects) {
    const struct = read<{ aulas: { id: string; topics: { level: number; title: string; pdfPage: number; printedPage: number | null; verified: boolean; auto?: boolean }[] }[] }>("structure", `${s.id}.json`);
    await db.topic.deleteMany({ where: { aula: { subjectId: s.id } } }); // tópicos não são referenciados por dados de usuário
    const topicRows = struct.aulas.flatMap((a) =>
      a.topics.map((t, i) => ({
        id: `${a.id}/t${String(i + 1).padStart(3, "0")}`, aulaId: a.id, level: t.level, title: t.title,
        pdfPage: t.pdfPage, printedPage: t.printedPage, sortOrder: i, verified: t.verified, auto: !!t.auto,
      })),
    );
    for (const c of chunk(topicRows, 1000)) await db.topic.createMany({ data: c });
    topics += topicRows.length;

    const segs = read<{ segments: SegJson[] }>("segments", `${s.id}.json`).segments;
    for (const c of chunk(segs, 100)) {
      await db.$transaction(
        c.map((g) => {
          const data = {
            aulaId: g.aula, sortOrder: g.order, startPage: g.startPage, endPage: g.endPage,
            startPrinted: g.startPrinted, endPrinted: g.endPrinted, pages: g.pages, load: g.load,
            startTopic: g.startTopic, startsMidTopic: g.startsMidTopic, stopBeforeTopic: g.stopBeforeTopic,
            endsMidTopic: g.endsMidTopic, endTopic: g.endTopic, endsTheory: g.endsTheory, topicsCovered: g.topicsCovered,
            estMinutes: g.minutes,
          };
          return db.segment.upsert({ where: { id: g.id }, create: { id: g.id, ...data }, update: data });
        }),
      );
    }
    segments += segs.length;
  }

  // aulas que saíram do catálogo (ex.: complemento removido) ficam no banco — podem ter atividades de usuários — mas saem do plano
  const gone = await db.aula.updateMany({
    where: { id: { notIn: aulas.map(({ a }) => a.id) }, selectable: true },
    data: { selectable: false, edital: "NO", incidence: 0, segmentCount: 0 },
  });
  if (gone.count) console.log(`aulas fora do catálogo desativadas: ${gone.count}`);

  // assuntos do edital: só entram os que têm ao menos uma aula planejável da própria disciplina
  // (assuntos cobertos em outra disciplina não alteram o plano de quem os marca)
  const planavel = new Set(aulas.filter(({ a }) => a.selectable).map(({ a }) => a.id));
  let editalItems = 0;
  for (const s of catalog.subjects) {
    const file = path.join(CONTENT, "edital", `${s.id}.json`);
    if (!fs.existsSync(file)) continue;
    const doc = read<EditalFile>("edital", `${s.id}.json`);
    const rows = doc.items.flatMap((it, i) => {
      const aulaIds = [...new Set((it.where ?? []).map((w) => w.aula).filter((id) => id.startsWith(`${s.id}/`) && planavel.has(id)))];
      return aulaIds.length ? [{ id: `${s.id}/e${it.id}`, subjectId: s.id, code: it.id, title: it.item, aulaIds, sortOrder: i }] : [];
    });
    await db.editalItem.deleteMany({ where: { subjectId: s.id } }); // não é referenciado por dados de usuário
    if (rows.length) await db.editalItem.createMany({ data: rows });
    editalItems += rows.length;
  }

  await db.$transaction(
    catalog.gaps.map((g) => {
      const data = { subjectId: g.subject, item: g.item, evidence: g.evidence, severity: g.severity.toUpperCase() as "HIGH" | "MEDIUM" | "LOW", remedy: g.remedy, resolved: !!g.resolved, resolution: g.resolution ?? null };
      return db.gap.upsert({ where: { id: g.id }, create: { id: g.id, ...data }, update: data });
    }),
  );
  console.log(`estrutura: ${catalog.subjects.length} disciplinas, ${aulas.length} aulas, ${topics} tópicos, ${segments} segmentos, ${editalItems} assuntos do edital, ${catalog.gaps.length} lacunas`);
}

async function seedItems() {
  const dir = path.join(CONTENT, "items");
  if (!fs.existsSync(dir)) return;
  let bizus = 0, bizuItems = 0, questions = 0, retired = 0;
  for (const sub of fs.readdirSync(dir)) {
    for (const f of fs.readdirSync(path.join(dir, sub)).filter((x) => x.endsWith(".json"))) {
      const doc = read<ItemsFile>("items", sub, f);
      const subjectId = doc.aula.split("/")[0];
      const status = doc.status ?? "DRAFT";
      for (const seg of doc.segments) {
        if (seg.bizu) {
          const bizu = await db.bizu.upsert({
            where: { segmentId: seg.id },
            create: { segmentId: seg.id, summary: seg.bizu.summary.map((b) => (b.startsWith("-") ? b : `- ${b}`)).join("\n") },
            update: { summary: seg.bizu.summary.map((b) => (b.startsWith("-") ? b : `- ${b}`)).join("\n") },
          });
          bizus++;
          const rows = [
            ...seg.bizu.teoria.map((i, n) => ({ set: "TEORIA" as const, n, i })),
            ...seg.bizu.revisao.map((i, n) => ({ set: "REVISAO" as const, n, i })),
          ];
          for (const r of rows) {
            const id = `${seg.id}/b-${r.set === "TEORIA" ? "t" : "r"}${r.n + 1}`;
            const data = { bizuId: bizu.id, set: r.set, statement: r.i.statement, isTrue: r.i.isTrue, explanation: r.i.explanation, sortOrder: r.n };
            await db.bizuItem.upsert({ where: { id }, create: { id, ...data }, update: data });
            bizuItems++;
          }
        }
        const keep = new Set<string>();
        for (const [n, q] of (seg.questions ?? []).entries()) {
          const id = `${seg.id}/q${String(n + 1).padStart(3, "0")}`;
          keep.add(id);
          const data = {
            subjectId, aulaId: doc.aula, segmentId: seg.id, topic: q.topic ?? null, support: q.support ?? null, statement: q.statement,
            explanation: q.explanation, difficulty: q.difficulty, pattern: q.pattern, pageRef: q.pageRef ?? null, batch: doc.batch,
          };
          const existing = await db.question.findUnique({ where: { id }, select: { status: true } });
          await db.question.upsert({
            where: { id },
            create: { id, ...data, status },
            // não rebaixa uma questão já aprovada/sinalizada por revisão humana
            update: { ...data, ...(existing && existing.status !== "DRAFT" ? {} : { status }) },
          });
          await db.questionOption.deleteMany({ where: { questionId: id } });
          await db.questionOption.createMany({
            data: q.options.map((text, i) => ({ questionId: id, label: "ABCDE"[i], text, isCorrect: "ABCDE"[i] === q.answer })),
          });
          questions++;
        }
        // questões que saíram do arquivo ficam RETIRED (não apagamos: podem ter respostas de usuários)
        const gone = await db.question.updateMany({
          where: { segmentId: seg.id, id: { notIn: [...keep] }, status: { not: "RETIRED" } },
          data: { status: "RETIRED" },
        });
        retired += gone.count;
      }
    }
  }
  console.log(`autoral: ${bizus} bizus, ${bizuItems} itens C/E, ${questions} questões (${retired} aposentadas)`);
}

async function seedAdmin() {
  const { randomBytes, scrypt: scryptCb } = await import("node:crypto");
  const { promisify } = await import("node:util");
  const scrypt = promisify(scryptCb) as (pw: string, salt: Buffer, keylen: number, opts: { N: number; r: number; p: number }) => Promise<Buffer>;
  const salt = randomBytes(16);
  const key = await scrypt("P3rn@mbuco", salt, 64, { N: 16384, r: 8, p: 1 });
  const passwordHash = ["scrypt", 16384, 8, 1, salt.toString("base64"), key.toString("base64")].join("$");
  const email = "valerioeducfin@gmail.com";

  await db.user.upsert({
    where: { email },
    create: {
      email,
      name: "Valério Ferreira (Admin)",
      username: "valerio",
      passwordHash,
      role: "ADMIN",
      mustChangePassword: false,
    },
    update: {
      role: "ADMIN",
      passwordHash,
    },
  });
  console.log(`admin: ${email} assegurado com role ADMIN`);
}

async function main() {
  await seedStructure();
  await seedItems();
  await seedAdmin();
}

main().finally(() => db.$disconnect());
