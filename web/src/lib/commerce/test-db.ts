// Endereço do banco de testes de integração (sem Prisma Client: usado também no globalSetup do Vitest).
// Só aceita o Postgres LOCAL de desenvolvimento; cada arquivo de teste usa um schema próprio `vitest_*`.
import "dotenv/config";
import { execSync } from "node:child_process";

export const TEST_SCHEMA = "vitest_finance";
export const TEST_SCHEMAS = ["vitest_finance", "vitest_actions", "vitest_online"] as const;
export const SAFE_SCHEMA = /^vitest_[a-z_]+$/;

function localUrl(): URL | null {
  const raw = process.env.DATABASE_URL;
  if (!raw) return null;
  try {
    const url = new URL(raw);
    return ["localhost", "127.0.0.1", "[::1]"].includes(url.hostname) ? url : null;
  } catch {
    return null;
  }
}

export const hasTestDb = localUrl() !== null;

export function testConnectionString(schema = TEST_SCHEMA): string {
  if (!SAFE_SCHEMA.test(schema)) throw new Error("Schema de teste inválido.");
  const url = localUrl();
  if (!url) throw new Error("Banco de testes indisponível (DATABASE_URL local ausente).");
  url.searchParams.set("schema", schema);
  return url.toString();
}

/** Aplica as migrações no schema de teste (idempotente). */
export function migrateTestSchema(schema = TEST_SCHEMA) {
  execSync("npx prisma migrate deploy", {
    stdio: "pipe",
    env: { ...process.env, DATABASE_URL: testConnectionString(schema), DATABASE_URL_UNPOOLED: "" },
  });
}
