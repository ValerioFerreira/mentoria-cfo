import "dotenv/config";
import { db } from "../src/lib/db";

async function main() {
  const acts = await db.activity.findMany({
    where: { planId: "cmv0dsvt40008lggsj28fk3ll", plannedMinutes: { lt: 50 } },
    select: { id: true, type: true, plannedMinutes: true, turbo: true, subjectId: true },
  });
  const byType: Record<string, number> = {};
  for (const a of acts) {
    const k = `${a.type}${a.turbo ? " (turbo)" : ""} - ${a.plannedMinutes}m`;
    byType[k] = (byType[k] || 0) + 1;
  }
  console.log("Breakdown <50m:", byType);

  // também checar as maiores durações
  const over80 = await db.activity.findMany({
    where: { planId: "cmv0dsvt40008lggsj28fk3ll", plannedMinutes: { gt: 80 } },
    select: { id: true, type: true, plannedMinutes: true, turbo: true },
  });
  console.log("Total >80m:", over80.length);
}

main().catch(console.error).finally(() => db.$disconnect());
