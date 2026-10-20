// Popula a estrutura do catálogo (disciplinas, aulas, trechos, tópicos, edital, admin, bizus e questões)
// Executado no build da Vercel de forma ultrarrápida (em lote com createMany)
// para garantir que o banco de produção sempre tenha todas as disciplinas, bizus e questões.
import "dotenv/config";
import fs from "node:fs";
import path from "node:path";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";
import type { SummaryStatus, Contest } from "../src/generated/prisma/enums";

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
  onlyContests?: string[]; excludeContests?: string[];
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
      onlyContests: a.onlyContests ?? [],
      excludeContests: a.excludeContests ?? [],
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

  // Só insere o que falta. Comparar contagens não serve: trechos órfãos (resegmentação) ficam no banco e fazem a
  // contagem passar do total do conteúdo, e então trechos novos (ex.: complementos) nunca entrariam e o Bizu falharia.
  const existingSegIds = new Set((await db.segment.findMany({ select: { id: true } })).map((s) => s.id));
  const missingSegRows = allSegRows.filter((r) => !existingSegIds.has(r.id));
  if (missingSegRows.length) {
    for (const c of chunk(allTopicRows, 1000)) await db.topic.createMany({ data: c, skipDuplicates: true });
    for (const c of chunk(missingSegRows, 500)) await db.segment.createMany({ data: c, skipDuplicates: true });
  }

  // 4. Edital
  console.log(`[Seed Structure] 4/6 Sincronizando itens do edital...`);
  const planavel = new Set(aulas.filter(({ a }) => a.selectable).map(({ a }) => a.id));
  const allEditalRows: { id: string; subjectId: string; code: string; title: string; aulaIds: string[]; sortOrder: number; onlyContests: string[]; excludeContests: string[] }[] = [];

  // Disciplinas compartilhadas com um concurso de edital próprio (content/edital/<concurso>/<disciplina>.json): os
  // assuntos padrão deixam de valer para ele e os do edital próprio (`<disciplina>/p<código>`) valem só para ele.
  const OWN_EDITAL_DIRS: { dir: string; contest: string }[] = [{ dir: "pcpe", contest: "PCPE_AGENTE" }];
  const ownEditalPath = (dir: string, subjectId: string) => path.join(CONTENT, "edital", dir, `${subjectId}.json`);
  const pushItems = (s: { id: string }, doc: EditalFile, idPrefix: string, onlyContests: string[], excludeContests: string[]) => {
    for (const [i, it] of doc.items.entries()) {
      const aulaIds = [...new Set((it.where ?? []).map((w) => w.aula).filter((id) => id.startsWith(`${s.id}/`) && planavel.has(id)))];
      if (aulaIds.length) {
        allEditalRows.push({ id: `${s.id}/${idPrefix}${it.id}`, subjectId: s.id, code: it.id, title: it.item, aulaIds, sortOrder: i, onlyContests, excludeContests });
      }
    }
  };

  for (const s of catalog.subjects) {
    const own = OWN_EDITAL_DIRS.filter((o) => fs.existsSync(ownEditalPath(o.dir, s.id)));
    pushItems(s, read<EditalFile>("edital", `${s.id}.json`), "e", [], own.map((o) => o.contest));
    for (const o of own) pushItems(s, read<EditalFile>("edital", o.dir, `${s.id}.json`), "p", [o.contest], []);
  }

  for (const c of chunk(allEditalRows, 500)) {
    await db.editalItem.createMany({ data: c, skipDuplicates: true });
  }
  // createMany não atualiza linhas que já existem: sincroniza só o filtro por concurso dos assuntos já semeados
  const withFilters = (pick: (r: (typeof allEditalRows)[number]) => string[]) =>
    Map.groupBy(allEditalRows.filter((r) => pick(r).length), (r) => pick(r).join(","));
  for (const [key, rows] of withFilters((r) => r.excludeContests)) {
    await db.editalItem.updateMany({ where: { id: { in: rows.map((r) => r.id) } }, data: { excludeContests: key.split(",") } });
  }
  for (const [key, rows] of withFilters((r) => r.onlyContests)) {
    await db.editalItem.updateMany({ where: { id: { in: rows.map((r) => r.id) } }, data: { onlyContests: key.split(",") } });
  }

  // createMany também não atualiza título, ordem e aulas de assunto já semeado (o mapa do edital muda): sincroniza, e
  // aposenta os assuntos próprios de um concurso (`/p`) que saíram do mapa (apaga se ninguém usa; senão, inativa)
  const existingItems = await db.editalItem.findMany({ select: { id: true, code: true, title: true, sortOrder: true, aulaIds: true } });
  const existingById = new Map(existingItems.map((e) => [e.id, e]));
  for (const r of allEditalRows) {
    const e = existingById.get(r.id);
    if (e && (e.title !== r.title || e.code !== r.code || e.sortOrder !== r.sortOrder || JSON.stringify(e.aulaIds) !== JSON.stringify(r.aulaIds))) {
      await db.editalItem.update({ where: { id: r.id }, data: { title: r.title, code: r.code, sortOrder: r.sortOrder, aulaIds: r.aulaIds } });
    }
  }
  const liveItemIds = new Set(allEditalRows.map((r) => r.id));
  for (const e of existingItems) {
    if (!/\/p[^/]*$/.test(e.id) || liveItemIds.has(e.id)) continue;
    const used = (await db.question.count({ where: { editalItemId: e.id } })) + (await db.activity.count({ where: { editalItemId: e.id } }));
    if (used === 0) await db.editalItem.delete({ where: { id: e.id } });
    else await db.editalItem.update({ where: { id: e.id }, data: { onlyContests: ["__INATIVO__"] } });
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
  await seedSummaries();
  await seedImportance();

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
          const summaryText = seg.bizu.summary.join("\n\n");
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
      }
    }
  }

  for (const c of chunk(bizuRows, 500)) {
    await db.bizu.createMany({ data: c, skipDuplicates: true });
  }
  // createMany não atualiza: o resumo sintético reescrito (content/summaries → apply_synthetic.py) precisa chegar ao banco
  const existing = new Map((await db.bizu.findMany({ select: { segmentId: true, summary: true } })).map((b) => [b.segmentId, b.summary]));
  // só os trechos com resumo sintético novo (content/summaries): o resto do Bizu em produção não é sobrescrito
  const rewritten = new Set<string>();
  const sumDir = path.join(CONTENT, "summaries");
  if (fs.existsSync(sumDir)) {
    for (const sub of fs.readdirSync(sumDir).filter((d) => fs.statSync(path.join(sumDir, d)).isDirectory())) {
      for (const f of fs.readdirSync(path.join(sumDir, sub)).filter((x) => x.endsWith(".json"))) {
        const doc = JSON.parse(fs.readFileSync(path.join(sumDir, sub, f), "utf-8")) as { segments: { id: string; synthetic?: string[] }[] };
        for (const sg of doc.segments) if (sg.synthetic?.length) rewritten.add(sg.id);
      }
    }
  }
  const changed = bizuRows.filter((b) => rewritten.has(b.segmentId) && existing.has(b.segmentId) && existing.get(b.segmentId) !== b.summary);
  for (const b of changed) await db.bizu.update({ where: { segmentId: b.segmentId }, data: { summary: b.summary, version: { increment: 1 } } });
  if (changed.length) console.log(`[Seed Items] ${changed.length} resumos sintéticos (Bizu) atualizados.`);
  for (const c of chunk(bizuItemRows, 1000)) {
    await db.bizuItem.createMany({ data: c, skipDuplicates: true });
  }
  console.log(`[Seed Items] Sincronizados: ${bizuRows.length} bizus, ${bizuItemRows.length} itens C/E, ${questionRows.length} questões, ${optionRows.length} alternativas.`);
}


interface SummariesFile {
  aula: string;
  status?: SummaryStatus;
  segments: { id: string; fingerprint: unknown; analytic?: string }[];
}

interface ExistingSummaryRow {
  segmentId: string;
  markdown: string;
  status: SummaryStatus;
}

interface ImportanceDoc {
  segments: Record<
    string,
    {
      contests: Record<
        string,
        {
          appears: boolean;
          expected: number;
          score: number | null;
        }
      >;
    }
  >;
}

/** Resumos analíticos (content/summaries/<disc>/<aula>.json): upsert por trecho; só semeia trechos que existem no banco. */
export async function seedSummaries() {
  const dir = path.join(CONTENT, "summaries");
  if (!fs.existsSync(dir)) return;
  const segmentsInDb = await db.segment.findMany({ select: { id: true } });
  const segIds = new Set<string>(segmentsInDb.map((x: { id: string }) => x.id));
  const rows: {
    segmentId: string;
    markdown: string;
    words: number;
    readMinutes: number;
    status: SummaryStatus;
    fingerprint: object;
  }[] = [];
  for (const sub of fs.readdirSync(dir).filter((d) => fs.statSync(path.join(dir, d)).isDirectory())) {
    for (const f of fs.readdirSync(path.join(dir, sub)).filter((x) => x.endsWith(".json"))) {
      const doc: SummariesFile = JSON.parse(fs.readFileSync(path.join(dir, sub, f), "utf-8"));
      for (const s of doc.segments) {
        if (!s.analytic || !segIds.has(s.id)) continue;
        const words = (s.analytic.match(/\p{L}[\p{L}\p{N}'-]*/gu) ?? []).length;
        rows.push({
          segmentId: s.id,
          markdown: s.analytic,
          words,
          readMinutes: Math.max(1, Math.min(20, Math.round(words / 100))),
          status: doc.status ?? "DRAFT",
          fingerprint: (s.fingerprint ?? {}) as object,
        });
      }
    }
  }
  const existingRows: ExistingSummaryRow[] = await db.analyticSummary.findMany({
    select: { segmentId: true, markdown: true, status: true },
  });
  const existing = new Map<string, ExistingSummaryRow>(
    existingRows.map((x: ExistingSummaryRow) => [x.segmentId, x])
  );
  const fresh = rows.filter((r) => !existing.has(r.segmentId));
  for (const c of chunk(fresh, 100)) await db.analyticSummary.createMany({ data: c, skipDuplicates: true });
  const changed = rows.filter((r) => {
    const prev = existing.get(r.segmentId);
    return prev !== undefined && (prev.markdown !== r.markdown || prev.status !== r.status);
  });
  for (const r of changed) {
    await db.analyticSummary.update({
      where: { segmentId: r.segmentId },
      data: { ...r, version: { increment: 1 } },
    });
  }
  console.log(`[Seed Summaries] ${rows.length} resumos analíticos (${fresh.length} novos, ${changed.length} atualizados).`);
}

/** Importância dos trechos por concurso (content/importance/segments.json): substitui a tabela inteira. */
export async function seedImportance() {
  const file = path.join(CONTENT, "importance", "segments.json");
  if (!fs.existsSync(file)) return;
  const doc = JSON.parse(fs.readFileSync(file, "utf-8")) as ImportanceDoc;
  const segmentsInDb = await db.segment.findMany({ select: { id: true } });
  const segIds = new Set<string>(segmentsInDb.map((x: { id: string }) => x.id));
  const rows: {
    segmentId: string;
    contest: Contest;
    appears: boolean;
    expected: number;
    score: number | null;
  }[] = Object.entries(doc.segments).flatMap(([segmentId, rec]) =>
    segIds.has(segmentId)
      ? Object.entries(rec.contests).map(([contest, c]) => ({
          segmentId,
          contest: contest as Contest,
          appears: c.appears,
          expected: c.expected,
          score: c.score,
        }))
      : []
  );
  await db.segmentImportance.deleteMany({});
  for (const c of chunk(rows, 1000)) await db.segmentImportance.createMany({ data: c, skipDuplicates: true });
  console.log(`[Seed Importance] ${rows.length} notas de importância (trecho × concurso).`);
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

// Questões não são semeadas aqui: vêm só dos cadernos de docs/questoes, gravados direto no banco por
// pipeline/questoes/importar.py (local e, com --remoto, produção). Ver pipeline/questoes/EXTRACAO.md.

/**
 * Migra/re-elabora planejamentos que estejam pendentes de análise (ex: almeida.guilherme098@gmail.com),
 * garantindo que sejam recalculados nas regras e diretrizes novas com as respostas originais do aluno.
 */
export async function seedPendingPlans() {
  const pending = await db.plan.findMany({
    where: { status: "PENDING_ANALYSIS" },
    include: {
      user: { select: { id: true, email: true, name: true } },
      subjects: true,
    },
  });

  if (pending.length === 0) return;

  console.log(`[Seed Plans] Encontrados ${pending.length} planejamentos em análise para atualização nas regras novas...`);

  try {
    try {
      require.cache[require.resolve("server-only")] = { exports: {} } as any;
    } catch {}
    const { regeneratePlanForUser } = await import("../src/lib/plan/regenerate");

    for (const p of pending) {
      console.log(`[Seed Plans] Re-elaborando planejamento do usuário ${p.user.email} (plano id: ${p.id})...`);
      const res = await regeneratePlanForUser(p.id, { activate: false });
      console.log(`[Seed Plans] -> ${res.message}`);
    }
  } catch (err: any) {
    console.warn(`[Seed Plans] Aviso ao processar planos pendentes:`, err?.message || err);
  }
}

async function main() {
  try {
    await seedStructure();
    await seedAdmin();
    await seedPendingPlans();
  } finally {
    await db.$disconnect();
  }
}

main().catch((err) => {
  console.error("[Seed Structure] Erro fatal:", err);
  process.exit(1);
});
