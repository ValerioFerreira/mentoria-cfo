import { Pool } from "pg";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "@/generated/prisma/client";

const globalForPrisma = globalThis as unknown as { prisma?: PrismaClient; pool?: Pool };

const connectionString = process.env.POSTGRES_PRISMA_URL || process.env.DATABASE_URL;

function createPrismaClient() {
  const pool =
    globalForPrisma.pool ??
    new Pool({
      connectionString,
      max: 10,
      idleTimeoutMillis: 30000,
      connectionTimeoutMillis: 10000,
    });

  pool.on("error", (err) => {
    // Tratamento de conexões ociosas fechadas pelo Neon/Postgres
    console.warn("[pg Pool] Conexão ociosa descartada pelo provedor:", err.message);
  });

  globalForPrisma.pool = pool;

  const adapter = new PrismaPg(pool);
  return new PrismaClient({ adapter });
}

export const db = globalForPrisma.prisma ?? createPrismaClient();

globalForPrisma.prisma = db;
