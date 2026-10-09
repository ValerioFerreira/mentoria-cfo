import "dotenv/config";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";
import { randomBytes, scrypt as scryptCb } from "node:crypto";
import { promisify } from "node:util";

const scrypt = promisify(scryptCb) as (pw: string, salt: Buffer, keylen: number, opts: { N: number; r: number; p: number }) => Promise<Buffer>;
const PARAMS = { N: 16384, r: 8, p: 1 };
const KEYLEN = 64;

async function hashPassword(password: string): Promise<string> {
  const salt = randomBytes(16);
  const key = await scrypt(password, salt, KEYLEN, PARAMS);
  return ["scrypt", PARAMS.N, PARAMS.r, PARAMS.p, salt.toString("base64"), key.toString("base64")].join("$");
}

const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }) });

async function main() {
  const email = "valerioeducfin@gmail.com";
  const password = "P3rn@mbuco";
  const passwordHash = await hashPassword(password);

  const user = await db.user.upsert({
    where: { email },
    create: {
      email,
      name: "Valério Ferreira (Admin)",
      username: "valerio",
      passwordHash,
      role: "ADMIN",
      mustChangePassword: false,
    },
    update: {
      passwordHash,
      role: "ADMIN",
    },
  });

  console.log(`Sucesso: Usuário ${user.email} está configurado como ADMIN! (ID: ${user.id})`);
}

main().catch(console.error).finally(() => db.$disconnect());
