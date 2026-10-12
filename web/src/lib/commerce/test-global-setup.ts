// globalSetup do projeto "integration" do Vitest: migra os schemas de teste uma vez, em sequência
// (o Postgres embutido do `prisma dev` não aceita duas migrações simultâneas).
import { hasTestDb, migrateTestSchema, TEST_SCHEMAS } from "./test-db";

export default function setup() {
  if (!hasTestDb) return;
  for (const schema of TEST_SCHEMAS) migrateTestSchema(schema);
}
