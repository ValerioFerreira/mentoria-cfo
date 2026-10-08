// Cria um código de convite. Uso: npx tsx scripts/invite.ts [--admin] [email]
import "dotenv/config";
import { randomBytes } from "node:crypto";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";

const args = process.argv.slice(2);
const makeAdmin = args.includes("--admin");
const email = args.find((a) => a.includes("@"));
const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }) });

async function main() {
  const code = randomBytes(6).toString("base64url");
  await db.invite.create({ data: { code, email: email?.toLowerCase(), makeAdmin } });
  console.log(`Convite criado: ${code}${makeAdmin ? " (administrador)" : ""}${email ? ` · restrito a ${email}` : ""}`);
  console.log(`Link: http://localhost:3000/cadastro?convite=${code}`);
}
main().finally(() => db.$disconnect());
