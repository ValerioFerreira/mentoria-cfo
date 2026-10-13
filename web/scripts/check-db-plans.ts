import "dotenv/config";
import { db } from "../src/lib/db";

async function main() {
  const plans = await db.plan.findMany({ select: { id: true, status: true, version: true, userId: true } });
  console.log("Total plans in DB:", plans.length);
  for (const p of plans) {
    const acts = await db.activity.findMany({ where: { planId: p.id }, select: { id: true, type: true, plannedMinutes: true, dayIndex: true, subjectId: true, weekId: true } });
    const under50 = acts.filter(a => a.plannedMinutes < 50);
    const between50_80 = acts.filter(a => a.plannedMinutes >= 50 && a.plannedMinutes <= 80);
    const over80 = acts.filter(a => a.plannedMinutes > 80);
    console.log(`Plan ${p.id} (${p.status}) - Total: ${acts.length} | <50: ${under50.length} | 50-80: ${between50_80.length} | >80: ${over80.length}`);
  }
}

main().catch(console.error).finally(() => db.$disconnect());
