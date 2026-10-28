import "dotenv/config";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../web/src/generated/prisma/client";

const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }) });

async function main() {
  const subjects = await db.subject.findMany({
    where: { id: { in: ["administracao", "direitos-humanos", "direito-processual-penal-militar"] } },
    select: { id: true, name: true, examQuestions: true, sortOrder: true }
  });
  console.log("=== Disciplinas no Banco de Dados ===");
  for (const s of subjects) {
    const aulasCount = await db.aula.count({ where: { subjectId: s.id } });
    const segmentsCount = await db.segment.count({ where: { aula: { subjectId: s.id } } });
    const topicsCount = await db.topic.count({ where: { aula: { subjectId: s.id } } });
    console.log(`- ${s.id} (${s.name}): ${aulasCount} aulas, ${segmentsCount} trechos/segmentos, ${topicsCount} tópicos`);
  }

  const totalSubjects = await db.subject.count();
  const totalAulas = await db.aula.count();
  const totalSegments = await db.segment.count();
  console.log(`\nTotal Geral no Banco: ${totalSubjects} disciplinas, ${totalAulas} aulas, ${totalSegments} segmentos.`);
  await db.$disconnect();
}

main().catch(console.error);
