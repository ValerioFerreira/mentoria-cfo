import { describe, expect, it } from "vitest";
import { materialKey, r2Config, streamBytes } from "./material-storage";

const env = (o: Record<string, string>) => o as unknown as NodeJS.ProcessEnv;
const completo = { R2_ACCOUNT_ID: "conta", R2_ACCESS_KEY_ID: "chave", R2_SECRET_ACCESS_KEY: "segredo", R2_BUCKET: "balde" };

describe("armazenamento do material (R2)", () => {
  it("monta a chave do objeto", () => {
    expect(materialKey("direito-administrativo", "m04")).toBe("material/direito-administrativo/m04.pdf");
  });

  it("usa o R2 só com as quatro variáveis preenchidas", () => {
    expect(r2Config(env(completo))).toEqual({ accountId: "conta", accessKeyId: "chave", secretAccessKey: "segredo", bucket: "balde" });
    expect(r2Config(env({ ...completo, R2_BUCKET: "  " }))).toBeNull();
    expect(r2Config(env({}))).toBeNull();
  });

  it("MATERIAL_STORAGE=disk força o disco mesmo com o R2 configurado", () => {
    expect(r2Config(env({ ...completo, MATERIAL_STORAGE: "disk" }))).toBeNull();
  });

  it("o streaming devolve exatamente os mesmos bytes, em vários pedaços", async () => {
    const bytes = new Uint8Array(200_000).map((_, i) => i % 251);
    const reader = streamBytes(bytes, 64 * 1024).getReader();
    const partes: Uint8Array[] = [];
    for (;;) {
      const { done, value } = await reader.read();
      if (done) break;
      partes.push(value);
    }
    expect(partes.length).toBe(4);
    const junto = new Uint8Array(partes.reduce((n, p) => n + p.length, 0));
    let off = 0;
    for (const p of partes) {
      junto.set(p, off);
      off += p.length;
    }
    expect(junto).toEqual(bytes);
  });
});
