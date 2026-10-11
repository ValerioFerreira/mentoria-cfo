import "dotenv/config";
import { db } from "../src/lib/db";
import * as fs from "node:fs";
import * as path from "node:path";

interface BizuItemJson {
  statement: string;
  isTrue: boolean;
  explanation: string;
}

interface ItemsFile {
  aula: string;
  segments: {
    id: string;
    bizu?: {
      summary: string[];
      teoria: BizuItemJson[];
      revisao: BizuItemJson[];
    };
  }[];
}

async function main() {
  console.log("Iniciando sincronização dos Bizus no banco de dados...");
  const contentDir = path.resolve(__dirname, "../../content/items");
  if (!fs.existsSync(contentDir)) {
    throw new Error(`Diretório ${contentDir} não encontrado.`);
  }

  let totalBizus = 0;
  let totalBizuItems = 0;

  const subjects = fs.readdirSync(contentDir);
  for (const sub of subjects) {
    const subDir = path.join(contentDir, sub);
    if (!fs.statSync(subDir).isDirectory()) continue;

    const files = fs.readdirSync(subDir).filter((x) => x.endsWith(".json"));
    for (const f of files) {
      const doc = JSON.parse(
        fs.readFileSync(path.join(subDir, f), "utf-8")
      ) as ItemsFile;

      for (const seg of doc.segments) {
        if (!seg.bizu) continue;

        const summaryText = seg.bizu.summary
          .map((b) => (b.startsWith("-") ? b : `- ${b}`))
          .join("\n");

        const bizu = await db.bizu.upsert({
          where: { segmentId: seg.id },
          create: { segmentId: seg.id, summary: summaryText },
          update: { summary: summaryText },
        });
        totalBizus++;

        const rows = [
          ...seg.bizu.teoria.map((i, n) => ({ set: "TEORIA" as const, n, i })),
          ...seg.bizu.revisao.map((i, n) => ({ set: "REVISAO" as const, n, i })),
        ];

        for (const r of rows) {
          const id = `${seg.id}/b-${r.set === "TEORIA" ? "t" : "r"}${r.n + 1}`;
          const data = {
            bizuId: bizu.id,
            set: r.set,
            statement: r.i.statement,
            isTrue: r.i.isTrue,
            explanation: r.i.explanation,
            sortOrder: r.n,
          };

          await db.bizuItem.upsert({
            where: { id },
            create: { id, ...data },
            update: data,
          });
          totalBizuItems++;
        }
      }
    }
  }

  console.log(
    `Sincronização concluída com sucesso: ${totalBizus} bizus e ${totalBizuItems} itens C/E atualizados no banco de dados!`
  );
}

main()
  .catch((e) => {
    console.error("Erro na sincronização:", e);
    process.exit(1);
  })
  .finally(async () => {
    await db.$disconnect();
  });
