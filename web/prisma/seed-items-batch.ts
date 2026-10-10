// Semeia Bizus, Itens C/E e Questões em lote ultrarrápido (createMany)
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
const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }) });

interface BizuItemJson { statement: string; isTrue: boolean; explanation: string }
interface QuestionJson {
  topic?: string; pattern: string; difficulty: number; pageRef?: number; support?: string | null;
  statement: string; options: string[]; answer: string; explanation: string; literal?: boolean;
}
interface ItemsFile {
  aula: string; batch: string; status?: "DRAFT" | "APPROVED";
  segments: { id: string; bizu?: { summary: string[]; teoria: BizuItemJson[]; revisao: BizuItemJson[] }; questions?: QuestionJson[] }[];
}

const chunk = <T>(xs: T[], n: number) => Array.from({ length: Math.ceil(xs.length / n) }, (_, i) => xs.slice(i * n, i * n + n));

export async function seedItemsBatch() {
  const itemsDir = path.join(CONTENT, "items");
  if (!fs.existsSync(itemsDir)) {
    console.log(`[Seed Items] Diretório de items não encontrado em ${itemsDir}`);
    return;
  }

  console.log(`[Seed Items] Carregando arquivos de items...`);
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

          // Teoria
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

          // Revisao
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

        // Questões
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

  console.log(`[Seed Items] 1/4 Inserindo ${bizuRows.length} Bizus em lote...`);
  for (const c of chunk(bizuRows, 500)) {
    await db.bizu.createMany({ data: c, skipDuplicates: true });
  }

  console.log(`[Seed Items] 2/4 Inserindo ${bizuItemRows.length} Itens C/E em lote...`);
  for (const c of chunk(bizuItemRows, 1000)) {
    await db.bizuItem.createMany({ data: c, skipDuplicates: true });
  }

  console.log(`[Seed Items] 3/4 Inserindo ${questionRows.length} Questões em lote...`);
  for (const c of chunk(questionRows, 1000)) {
    await db.question.createMany({ data: c, skipDuplicates: true });
  }

  console.log(`[Seed Items] 4/4 Inserindo ${optionRows.length} Alternativas em lote...`);
  for (const c of chunk(optionRows, 2000)) {
    await db.questionOption.createMany({ data: c, skipDuplicates: true });
  }

  console.log(`[Seed Items] Concluído com sucesso: ${bizuRows.length} bizus, ${bizuItemRows.length} itens C/E, ${questionRows.length} questões, ${optionRows.length} opções.`);
}

if (require.main === module) {
  seedItemsBatch()
    .catch((err) => {
      console.error("[Seed Items] Erro fatal:", err);
      process.exit(1);
    })
    .finally(() => db.$disconnect());
}
