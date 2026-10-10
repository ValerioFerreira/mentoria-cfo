// Popula a estrutura do catálogo (disciplinas, aulas, trechos, tópicos, edital, admin, bizus e questões)
// Executado no build da Vercel de forma ultrarrápida (em lote com createMany)
// para garantir que o banco de produção sempre tenha todas as disciplinas, bizus e questões.
import "dotenv/config";
import fs from "node:fs";
import path from "node:path";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";

function findContentDir(): string {
  const candidates = [
    path.resolve(process.cwd(), "content"),
    path.resolve(process.cwd(), "../content"),
    path.resolve(__dirname, "../../content"),
    path.resolve(__dirname, "../content"),
  ];
  for (const c of candidates) {
    if (fs.existsSync(path.join(c, "catalog.json"))) return c;
  }
  return path.resolve(process.cwd(), "content");
}

const CONTENT = findContentDir();
console.log(`[Seed Structure] Diretório de conteúdo: ${CONTENT}`);

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

export async function seedStructure() {
  const catalog = read<Catalog>("catalog.json");
  console.log(`[Seed Structure] 1/6 Sincronizando ${catalog.subjects.length} disciplinas...`);

  // 1. Disciplinas
  for (const s of catalog.subjects) {
    const data = {
      name: s.name, block: s.block, examQuestions: s.examQuestions, sortOrder: s.sortOrder,
      languageGroup: s.languageGroup ?? null,
      foreignLanguage: s.id === "lingua-inglesa" ? ("EN" as const) : s.id === "lingua-espanhola" ? ("ES" as const) : null,
      materialCompleteness: s.materialCompleteness ?? 1,
    };
    await db.subject.upsert({ where: { id: s.id }, create: { id: s.id, ...data }, update: data });
  }

  // 2. Aulas
  const aulas = catalog.subjects.flatMap((s) => s.aulas.map((a) => ({ s, a })));
  console.log(`[Seed Structure] 2/6 Sincronizando ${aulas.length} aulas...`);
  for (const { s, a } of aulas) {
    const data = {
      subjectId: s.id, number: a.number, title: a.title, shortTitle: a.shortTitle,
      kind: a.kind === "practice" ? ("PRACTICE" as const) : ("THEORY" as const),
      edital: a.edital.toUpperCase() as "YES" | "PARTIAL" | "NO",
      selectable: a.selectable, totalPages: a.totalPages, theoryPages: a.theoryPages, segmentCount: a.segmentCount,
      commentedPages: a.commentedPages, listPages: a.listPages, commentedRuns: a.commentedRuns,
      practiceLinks: a.practiceLinks as object[], printedOffset: a.printedOffset, incidence: a.incidence, note: a.note ?? null,
      source: a.source === "authored" ? ("AUTHORED" as const) : ("BASE" as const), materialPath: a.materialPath ?? null,
    };
    await db.aula.upsert({ where: { id: a.id }, create: { id: a.id, ...data }, update: data });
  }

  // 3. Tópicos e Segmentos
  console.log(`[Seed Structure] 3/6 Sincronizando tópicos e trechos...`);
  const allTopicRows: { id: string; aulaId: string; level: number; title: string; pdfPage: number; printedPage: number | null; sortOrder: number; verified: boolean; auto: boolean }[] = [];
  const allSegRows: { id: string; aulaId: string; sortOrder: number; startPage: number; endPage: number; startPrinted: number | null; endPrinted: number | null; pages: number; load: number; startTopic: string | null; startsMidTopic: boolean; stopBeforeTopic: string | null; endsMidTopic: boolean; endTopic: string | null; endsTheory: boolean; topicsCovered: string[]; estMinutes: number }[] = [];

  for (const s of catalog.subjects) {
    const struct = read<{ aulas: { id: string; topics: { level: number; title: string; pdfPage: number; printedPage: number | null; verified: boolean; auto?: boolean }[] }[] }>("structure", `${s.id}.json`);
    for (const a of struct.aulas) {
      for (const [i, t] of a.topics.entries()) {
        allTopicRows.push({
          id: `${a.id}/t${String(i + 1).padStart(3, "0")}`,
          aulaId: a.id, level: t.level, title: t.title,
          pdfPage: t.pdfPage, printedPage: t.printedPage, sortOrder: i, verified: t.verified, auto: !!t.auto,
        });
      }
    }

    const segs = read<{ segments: SegJson[] }>("segments", `${s.id}.json`).segments;
    for (const g of segs) {
      allSegRows.push({
        id: g.id,
        aulaId: g.aula, sortOrder: g.order, startPage: g.startPage, endPage: g.endPage,
        startPrinted: g.startPrinted, endPrinted: g.endPrinted, pages: g.pages, load: g.load,
        startTopic: g.startTopic, startsMidTopic: g.startsMidTopic, stopBeforeTopic: g.stopBeforeTopic,
        endsMidTopic: g.endsMidTopic, endTopic: g.endTopic, endsTheory: g.endsTheory, topicsCovered: g.topicsCovered,
        estMinutes: g.minutes,
      });
    }
  }

  const existingSegCount = await db.segment.count();
  if (existingSegCount < allSegRows.length) {
    for (const c of chunk(allTopicRows, 1000)) await db.topic.createMany({ data: c, skipDuplicates: true });
    for (const c of chunk(allSegRows, 500)) await db.segment.createMany({ data: c, skipDuplicates: true });
  }

  // 4. Edital
  console.log(`[Seed Structure] 4/6 Sincronizando itens do edital...`);
  const planavel = new Set(aulas.filter(({ a }) => a.selectable).map(({ a }) => a.id));
  const allEditalRows: { id: string; subjectId: string; code: string; title: string; aulaIds: string[]; sortOrder: number }[] = [];

  for (const s of catalog.subjects) {
    const doc = read<EditalFile>("edital", `${s.id}.json`);
    for (const [i, it] of doc.items.entries()) {
      const aulaIds = [...new Set((it.where ?? []).map((w) => w.aula).filter((id) => id.startsWith(`${s.id}/`) && planavel.has(id)))];
      if (aulaIds.length) {
        allEditalRows.push({
          id: `${s.id}/e${it.id}`,
          subjectId: s.id,
          code: it.id,
          title: it.item,
          aulaIds,
          sortOrder: i,
        });
      }
    }
  }

  for (const c of chunk(allEditalRows, 500)) {
    await db.editalItem.createMany({ data: c, skipDuplicates: true });
  }

  // 5. Lacunas
  console.log(`[Seed Structure] 5/6 Sincronizando lacunas...`);
  const gapRows = catalog.gaps.map((g) => ({
    id: g.id,
    subjectId: g.subject,
    item: g.item,
    evidence: g.evidence,
    severity: g.severity.toUpperCase() as "HIGH" | "MEDIUM" | "LOW",
    remedy: g.remedy,
    resolved: !!g.resolved,
    resolution: g.resolution ?? null,
  }));
  for (const c of chunk(gapRows, 100)) {
    await db.gap.createMany({ data: c, skipDuplicates: true });
  }

  // 6. Bizus, C/E e Questões em lote
  console.log(`[Seed Structure] 6/6 Sincronizando Bizus e Questões em lote...`);
  await seedItemsBatch();

  console.log(`[Seed Structure] Concluído com sucesso!`);
}

export async function seedItemsBatch() {
  const itemsDir = path.join(CONTENT, "items");
  if (!fs.existsSync(itemsDir)) return;

  const bizuRows: { id: string; segmentId: string; summary: string; version: number }[] = [];
  const bizuItemRows: { id: string; bizuId: string; set: "TEORIA" | "REVISAO"; statement: string; isTrue: boolean; explanation: string; sortOrder: number }[] = [];
  const questionRows: { id: string; subjectId: string; aulaId: string; segmentId: string; topic: string | null; support: string | null; statement: string; explanation: string; difficulty: number; pattern: string; pageRef: number | null; status: "DRAFT" | "APPROVED"; batch: string | null }[] = [];
  const optionRows: { id: string; questionId: string; label: string; text: string; isCorrect: boolean }[] = [];

  const subjects = fs.readdirSync(itemsDir).filter((d) => fs.statSync(path.join(itemsDir, d)).isDirectory());

  for (const sub of subjects) {
    const files = fs.readdirSync(path.join(itemsDir, sub)).filter((f) => f.endsWith(".json"));
    for (const f of files) {
      const doc: ItemsFile = JSON.parse(fs.readFileSync(path.join(itemsDir, sub, f), "utf-8"));
      const subjectId = doc.aula.split("/")[0];
      const status = doc.status ?? "DRAFT";

      for (const seg of doc.segments) {
        if (seg.bizu) {
          const bizuId = `bizu/${seg.id}`;
          const summaryText = seg.bizu.summary.map((b) => (b.startsWith("-") ? b : `- ${b}`)).join("\n");
          bizuRows.push({
            id: bizuId,
            segmentId: seg.id,
            summary: summaryText,
            version: 1,
          });

          for (const [n, item] of seg.bizu.teoria.entries()) {
            bizuItemRows.push({
              id: `${seg.id}/b-t${n + 1}`,
              bizuId,
              set: "TEORIA",
              statement: item.statement,
              isTrue: item.isTrue,
              explanation: item.explanation,
              sortOrder: n,
            });
          }

          for (const [n, item] of seg.bizu.revisao.entries()) {
            bizuItemRows.push({
              id: `${seg.id}/b-r${n + 1}`,
              bizuId,
              set: "REVISAO",
              statement: item.statement,
              isTrue: item.isTrue,
              explanation: item.explanation,
              sortOrder: n,
            });
          }
        }

        for (const [n, q] of (seg.questions ?? []).entries()) {
          const qId = `${seg.id}/q${String(n + 1).padStart(3, "0")}`;
          questionRows.push({
            id: qId,
            subjectId,
            aulaId: doc.aula,
            segmentId: seg.id,
            topic: q.topic ?? null,
            support: q.support ?? null,
            statement: q.statement,
            explanation: q.explanation,
            difficulty: q.difficulty,
            pattern: q.pattern,
            pageRef: q.pageRef ?? null,
            status,
            batch: doc.batch ?? null,
          });

          for (let optIdx = 0; optIdx < q.options.length; optIdx++) {
            const label = "ABCDE"[optIdx];
            optionRows.push({
              id: `${qId}/${label}`,
              questionId: qId,
              label,
              text: q.options[optIdx],
              isCorrect: label === q.answer,
            });
          }
        }
      }
    }
  }

  for (const c of chunk(bizuRows, 500)) {
    await db.bizu.createMany({ data: c, skipDuplicates: true });
  }
  for (const c of chunk(bizuItemRows, 1000)) {
    await db.bizuItem.createMany({ data: c, skipDuplicates: true });
  }
  for (const c of chunk(questionRows, 1000)) {
    await db.question.createMany({ data: c, skipDuplicates: true });
  }
  for (const c of chunk(optionRows, 2000)) {
    await db.questionOption.createMany({ data: c, skipDuplicates: true });
  }
  console.log(`[Seed Items] Sincronizados: ${bizuRows.length} bizus, ${bizuItemRows.length} itens C/E, ${questionRows.length} questões, ${optionRows.length} alternativas.`);
}

export async function seedAdmin() {
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
  console.log(`[Seed Admin] Administrador ${email} assegurado.`);
}

async function main() {
  try {
    await seedStructure();
    await seedAdmin();
  } finally {
    await db.$disconnect();
  }
}

main().catch((err) => {
  console.error("[Seed Structure] Erro fatal:", err);
  process.exit(1);
});
