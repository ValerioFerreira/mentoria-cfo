import "dotenv/config";
import { db } from "../src/lib/db";

async function main() {
  await db.$executeRawUnsafe(`ALTER TYPE "PlanStatus" ADD VALUE IF NOT EXISTS 'PENDING_ANALYSIS' BEFORE 'ACTIVE';`);
  console.log("Enum PlanStatus updated successfully!");
}

main().catch(console.error).finally(() => db.$disconnect());
