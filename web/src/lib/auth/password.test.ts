import { describe, expect, it, vi } from "vitest";

vi.mock("server-only", () => ({}));

describe("hash de senha (scrypt)", () => {
  it("gera o formato scrypt$N$r$p$salt$hash", async () => {
    const { hashPassword } = await import("./password");
    const h = await hashPassword("minha-senha-123");
    const parts = h.split("$");
    expect(parts).toHaveLength(6);
    expect(parts.slice(0, 4)).toEqual(["scrypt", "16384", "8", "1"]);
    expect(Buffer.from(parts[4], "base64")).toHaveLength(16); // sal de 16 bytes
    expect(Buffer.from(parts[5], "base64")).toHaveLength(64); // chave de 64 bytes
    expect(h).not.toContain("minha-senha-123");
  });
  it("a mesma senha gera hashes diferentes (sal aleatório), mas ambos verificam", async () => {
    const { hashPassword, verifyPassword } = await import("./password");
    const a = await hashPassword("segredo!");
    const b = await hashPassword("segredo!");
    expect(a).not.toBe(b);
    expect(await verifyPassword("segredo!", a)).toBe(true);
    expect(await verifyPassword("segredo!", b)).toBe(true);
  });
  it("rejeita senha errada, vazia e com diferença de maiúscula/espaço", async () => {
    const { hashPassword, verifyPassword } = await import("./password");
    const h = await hashPassword("Senha Forte 1");
    expect(await verifyPassword("senha forte 1", h)).toBe(false);
    expect(await verifyPassword("Senha Forte 1 ", h)).toBe(false);
    expect(await verifyPassword("", h)).toBe(false);
  });
  it("aceita senhas com acentos, emojis e muito longas", async () => {
    const { hashPassword, verifyPassword } = await import("./password");
    for (const pw of ["Pernambuco-ação-ç", "🔥🔥🔥senha", "x".repeat(2000)]) {
      const h = await hashPassword(pw);
      expect(await verifyPassword(pw, h)).toBe(true);
      expect(await verifyPassword(pw + "!", h)).toBe(false);
    }
  });
  it("hash em outro esquema é rejeitado sem lançar", async () => {
    const { verifyPassword } = await import("./password");
    expect(await verifyPassword("x", "bcrypt$10$abc$def")).toBe(false);
    expect(await verifyPassword("x", "")).toBe(false);
  });
  it("respeita os parâmetros gravados no hash (compatível com hashes antigos)", async () => {
    const { verifyPassword } = await import("./password");
    const { scryptSync, randomBytes } = await import("node:crypto");
    const salt = randomBytes(16);
    const key = scryptSync("antiga", salt, 32, { N: 1024, r: 8, p: 1 });
    const stored = ["scrypt", 1024, 8, 1, salt.toString("base64"), key.toString("base64")].join("$");
    expect(await verifyPassword("antiga", stored)).toBe(true);
    expect(await verifyPassword("outra", stored)).toBe(false);
  });
  // verifyPassword([scheme,...] = stored.split("$")): se hashB64 vier ausente (registro truncado), Buffer.from(undefined) lança.
  it("registro truncado/corrompido no banco deve falhar fechado (false) em vez de lançar exceção", async () => {
    const { verifyPassword } = await import("./password");
    await expect(verifyPassword("x", "scrypt$16384$8$1")).resolves.toBe(false);
  });
});
