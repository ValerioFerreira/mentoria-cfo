import "dotenv/config";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../web/src/generated/prisma/client";

const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }) });

async function main() {
  const r = await db.question.groupBy({
    by: ["batch", "kind", "banca"],
    _count: true,
  });
  console.log(r);
}

main().catch(console.error).finally(() => db.$disconnect());
