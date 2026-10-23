import "dotenv/config";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";

const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }) });

async function main() {
  const targetIds = ["administracao", "direitos-humanos", "direito-processual-penal-militar"];
  const subjects = await db.subject.findMany({
    where: { id: { in: targetIds } },
    select: { id: true, name: true, examQuestions: true, sortOrder: true }
  });
  console.log("=== Disciplinas do CFOA no Banco de Dados ===");
  for (const s of subjects) {
    const aulasCount = await db.aula.count({ where: { subjectId: s.id } });
    const segmentsCount = await db.segment.count({ where: { aula: { subjectId: s.id } } });
    const topicsCount = await db.topic.count({ where: { aula: { subjectId: s.id } } });
    const sampleAula = await db.aula.findFirst({
      where: { subjectId: s.id },
      orderBy: { number: "asc" },
      select: { id: true, number: true, title: true, theoryPages: true }
    });
    console.log(`- ${s.id} (${s.name}):`);
    console.log(`    Aulas: ${aulasCount} | Segmentos: ${segmentsCount} | Tópicos: ${topicsCount}`);
    if (sampleAula) {
      console.log(`    Exemplo: [${sampleAula.id}] Aula ${String(sampleAula.number).padStart(2, "0")}: "${sampleAula.title}" (${sampleAula.theoryPages} págs teoria)`);
    }
  }

  const totalSubjects = await db.subject.count();
  const totalAulas = await db.aula.count();
  const totalSegments = await db.segment.count();
  console.log(`\n=== Totais Gerais no Banco de Dados ===`);
  console.log(`- Disciplinas: ${totalSubjects}`);
  console.log(`- Aulas: ${totalAulas}`);
  console.log(`- Trechos/Segmentos: ${totalSegments}`);
  await db.$disconnect();
}

main().catch(console.error);
