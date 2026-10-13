import "dotenv/config";
import { db } from "../src/lib/db";

async function main() {
  const plans = await db.plan.findMany({ select: { id: true, status: true } });
  for (const p of plans) {
    const acts = await db.activity.findMany({
      where: { planId: p.id, dayIndex: { not: null } },
      select: { weekId: true, dayIndex: true, subjectId: true, plannedMinutes: true },
    });
    const byDaySub: Record<string, number> = {};
    for (const a of acts) {
      const k = `${a.weekId}#d${a.dayIndex}#${a.subjectId}`;
      byDaySub[k] = (byDaySub[k] || 0) + a.plannedMinutes;
    }
    const over120 = Object.entries(byDaySub).filter(([_, min]) => min > 120);
    console.log(`Plan ${p.id} - Total week/day/subject slots: ${Object.keys(byDaySub).length} | Slots >120m: ${over120.length}`);
    if (over120.length > 0) {
      console.log("Sample over 120m:", over120.slice(0, 5));
    }
  }
}

main().catch(console.error).finally(() => db.$disconnect());
