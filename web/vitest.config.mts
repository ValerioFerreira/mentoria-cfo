import { defineConfig } from "vitest/config";
import { fileURLToPath } from "node:url";

export default defineConfig({
  resolve: { alias: { "@": fileURLToPath(new URL("./src", import.meta.url)) } },
  test: {
    environment: "node",
    projects: [
      { extends: true, test: { name: "unit", include: ["src/**/*.test.ts"], exclude: ["src/**/*.integration.test.ts"] } },
      {
        // banco real (schemas `vitest_*` do Postgres local): migrações uma vez e arquivos em sequência
        extends: true,
        test: {
          name: "integration",
          include: ["src/**/*.integration.test.ts"],
          fileParallelism: false,
          globalSetup: ["./src/lib/commerce/test-global-setup.ts"],
          hookTimeout: 120_000,
        },
      },
    ],
  },
});
