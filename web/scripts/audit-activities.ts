import { db } from "../src/lib/db";

async function main() {
  const acts = await db.activity.findMany({
    select: { id: true, type: true, plannedMinutes: true, turbo: true, subjectId: true, aulaId: true },
  });
  console.log("Total activities in DB:", acts.length);
  let under50 = 0, target50to80 = 0, over80 = 0;
  const byType: Record<string, { under: number; target: number; over: number; total: number }> = {};
  const underSamples: any[] = [];
  const overSamples: any[] = [];

  for (const a of acts) {
    byType[a.type] = byType[a.type] || { under: 0, target: 0, over: 0, total: 0 };
    byType[a.type].total++;
    if (a.plannedMinutes < 50) {
      under50++;
      byType[a.type].under++;
      if (underSamples.length < 5) underSamples.push(a);
    } else if (a.plannedMinutes > 80) {
      over80++;
      byType[a.type].over++;
      if (overSamples.length < 5) overSamples.push(a);
    } else {
      target50to80++;
      byType[a.type].target++;
    }
  }

  console.log("All DB activities summary:");
  console.log("  < 50 min:", under50);
  console.log("  50–80 min:", target50to80);
  console.log("  > 80 min:", over80);
  console.log("By type:", JSON.stringify(byType, null, 2));
  if (underSamples.length) console.log("Sample under:", underSamples);
  if (overSamples.length) console.log("Sample over:", overSamples);

  // Check plans
  const plans = await db.plan.findMany({ select: { id: true, status: true, version: true, userId: true } });
  console.log("Total plans in DB:", plans.length);
  for (const p of plans) {
    console.log(`Plan ${p.id}: status=${p.status}, version=${p.version}, user=${p.userId}`);
  }
}

main().catch(console.error).finally(() => db.$disconnect());
