// Cria (ou restaura) o usuário de teste LOCAL: teste@teste.com. Recusa qualquer banco que não seja localhost.
// Uso: npx tsx --conditions=react-server scripts/create-test-user.ts
import "dotenv/config";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";
import { hashPassword } from "../src/lib/auth/password";
import { localDatabase, TEST_USER_EMAIL, TEST_USER_PASSWORD } from "../src/lib/test-user";

async function main() {
  if (!localDatabase()) throw new Error("DATABASE_URL não aponta para localhost: o usuário de teste só existe no banco local.");
  const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }) });
  const passwordHash = await hashPassword(TEST_USER_PASSWORD);
  const data = { passwordHash, name: "Usuário de Teste", role: "USER" as const, mustChangePassword: false, accessExpiresAt: null };
  const u = await db.user.upsert({ where: { email: TEST_USER_EMAIL }, create: { email: TEST_USER_EMAIL, username: "teste", ...data }, update: data });
  console.log(`Usuário de teste pronto: ${u.email}`);
  await db.$disconnect();
}
main().catch((e) => {
  console.error(String(e instanceof Error ? e.message : e));
  process.exit(1);
});
