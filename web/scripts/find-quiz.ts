// Lista atividades de Questões (e suas semanas) que cobrem trechos com questões no banco. Uso em dev.
import "dotenv/config";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";
const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }) });
async function main() {
  const withQ = await db.question.groupBy({ by: ["segmentId"], _count: true });
  const segs = withQ.map((s) => s.segmentId);
  const acts = await db.activity.findMany({
    where: { segments: { some: { segmentId: { in: segs } } } },
    include: { week: { select: { index: true } }, segments: { select: { segmentId: true } } },
    orderBy: [{ week: { index: "asc" } }, { sortOrder: "asc" }],
  });
  for (const a of acts) console.log(`sem ${a.week.index} ${a.type.padEnd(8)} ${a.aulaId} ${a.id} segs=${a.segments.map((s) => s.segmentId.split("/").pop()).join(",")}`);
}
main().finally(() => db.$disconnect());
