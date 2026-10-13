import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "@/generated/prisma/client";

const globalForPrisma = globalThis as unknown as { prisma?: PrismaClient };

function getConnectionString(): string {
  let url = process.env.DATABASE_URL || process.env.POSTGRES_URL || process.env.POSTGRES_PRISMA_URL || "";
  if (url.includes("pgbouncer=true")) {
    url = url.replace(/([?&])pgbouncer=true(&|$)/, (_, p1, p2) => (p2 ? p1 : ""));
  }
  return url;
}

export const db =
  globalForPrisma.prisma ??
  new PrismaClient({
    adapter: new PrismaPg({ connectionString: getConnectionString() }),
  });

globalForPrisma.prisma = db;
