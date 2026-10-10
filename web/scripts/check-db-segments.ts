import "dotenv/config";
import { db } from "../src/lib/db";

async function main() {
  const segs = await db.segment.findMany({ select: { estMinutes: true } });
  const counts: Record<number, number> = {};
  for (const s of segs) {
    counts[s.estMinutes] = (counts[s.estMinutes] || 0) + 1;
  }
  console.log("Total segments in DB:", segs.length, "Distribution:", counts);
}

main().catch(console.error).finally(() => db.$disconnect());
