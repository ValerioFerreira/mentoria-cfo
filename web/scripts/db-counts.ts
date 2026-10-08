// Contagem rápida das tabelas de plano (diagnóstico de desenvolvimento).
import "dotenv/config";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";

const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }) });
async function main() {
  const [plans, weeks, acts, segs, refs, subj] = await Promise.all([
    db.plan.count(), db.week.count(), db.activity.count(), db.activitySegment.count(), db.activityRef.count(), db.planSubject.count(),
  ]);
  console.log({ plans, weeks, activities: acts, activitySegments: segs, activityRefs: refs, planSubjects: subj });
  const byType = await db.activity.groupBy({ by: ["type"], _count: true });
  console.log(byType.map((b) => `${b.type}=${b._count}`).join(" "));
}
main().finally(() => db.$disconnect());
