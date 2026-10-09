// Popula a estrutura do catálogo (disciplinas, aulas, trechos, tópicos, edital, admin)
// Executado no build da Vercel de forma ultrarrápida (em lote com createMany)
// para garantir que o banco de produção sempre tenha todas as disciplinas.
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

export async function seedStructure() {
  const subjectCount = await db.subject.count();
  const segmentCount = await db.segment.count();

  if (subjectCount >= 13 && segmentCount >= 700) {
    console.log(`[Seed Structure] Banco já possui ${subjectCount} disciplinas e ${segmentCount} trechos. Estrutura pronta!`);
    return;
  }

  const catalog = read<Catalog>("catalog.json");
  console.log(`[Seed Structure] 1/5 Semeando ${catalog.subjects.length} disciplinas...`);

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
  console.log(`[Seed Structure] 2/5 Semeando ${aulas.length} aulas em lote...`);
  const aulaRows = aulas.map(({ s, a }) => ({
    id: a.id,
    subjectId: s.id, number: a.number, title: a.title, shortTitle: a.shortTitle,
    kind: a.kind === "practice" ? ("PRACTICE" as const) : ("THEORY" as const),
    edital: a.edital.toUpperCase() as "YES" | "PARTIAL" | "NO",
    selectable: a.selectable, totalPages: a.totalPages, theoryPages: a.theoryPages, segmentCount: a.segmentCount,
    commentedPages: a.commentedPages, listPages: a.listPages, commentedRuns: a.commentedRuns,
    practiceLinks: a.practiceLinks as object[], printedOffset: a.printedOffset, incidence: a.incidence, note: a.note ?? null,
    source: a.source === "authored" ? ("AUTHORED" as const) : ("BASE" as const), materialPath: a.materialPath ?? null,
  }));
  await db.aula.createMany({ data: aulaRows, skipDuplicates: true });

  // 3. Tópicos e Segmentos
  console.log(`[Seed Structure] 3/5 Semeando tópicos e trechos em lote...`);
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

  if (allTopicRows.length) {
    await db.topic.createMany({ data: allTopicRows, skipDuplicates: true });
  }
  if (allSegRows.length) {
    await db.segment.createMany({ data: allSegRows, skipDuplicates: true });
  }

  // 4. Edital
  console.log(`[Seed Structure] 4/5 Semeando itens do edital em lote...`);
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

  if (allEditalRows.length) {
    await db.editalItem.createMany({ data: allEditalRows, skipDuplicates: true });
  }

  // 5. Lacunas
  console.log(`[Seed Structure] 5/5 Semeando lacunas...`);
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
  await db.gap.createMany({ data: gapRows, skipDuplicates: true });

  console.log(`[Seed Structure] Concluído em lote: ${catalog.subjects.length} disciplinas, ${aulas.length} aulas, ${allTopicRows.length} tópicos, ${allSegRows.length} trechos, ${allEditalRows.length} edital, ${gapRows.length} lacunas.`);
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
