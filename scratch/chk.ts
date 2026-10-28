import "dotenv/config";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../web/src/generated/prisma/client";
const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }) });
(async () => {
  console.log(await db.$queryRawUnsafe(`select migration_name from _prisma_migrations order by migration_name desc limit 4`));
  console.log(await db.contestSetting.findMany({ where: { contest: { in: ["CBMPE_COMBO", "PMPE_COMBO"] } } }));
  await db.$disconnect();
})();
