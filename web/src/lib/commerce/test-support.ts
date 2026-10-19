// Prisma Client dos testes de integração financeiros, apontado para um schema isolado `vitest_*` no Postgres LOCAL
// de desenvolvimento (nunca banco remoto). Sem banco local, esses testes são pulados.
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "@/generated/prisma/client";
import { SAFE_SCHEMA, TEST_SCHEMA, testConnectionString } from "./test-db";

export { hasTestDb, TEST_SCHEMA } from "./test-db";

export function makeTestClient(schema = TEST_SCHEMA): PrismaClient {
  return new PrismaClient({ adapter: new PrismaPg({ connectionString: testConnectionString(schema) }, { schema }) });
}

/** Limpa as tabelas usadas pelos testes — somente dentro do schema de teste. */
export async function resetTestData(client: PrismaClient, schema = TEST_SCHEMA) {
  if (!SAFE_SCHEMA.test(schema)) throw new Error("Schema de teste inválido.");
  const tables = [
    "AuditLog", "CommissionEntry", "PartnerPayout", "PaymentReversal", "ManualPayment", "PartnerReferral",
    "OnlineCharge", "BillingWebhookEvent", "Contract", "Coupon", "PartnerCoupon", "Partner", "Session", "WaitlistEntry", "User",
  ];
  await client.$executeRawUnsafe(`TRUNCATE ${tables.map((t) => `"${schema}"."${t}"`).join(", ")} CASCADE`);
}
