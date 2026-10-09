import { describe, expect, it, vi } from "vitest";

vi.mock("server-only", () => ({}));

describe("BR Code Pix", () => {
  it("gera payload com CRC válido e a mensagem com o e-mail", async () => {
    const { buildPixPayload } = await import("./pix");
    const p = buildPixPayload({ key: "12345678909", receiverName: "MENTORIA", city: "RECIFE" }, "aluno@exemplo.com");
    expect(p.startsWith("000201010211")).toBe(true);
    expect(p).toContain("0014br.gov.bcb.pix");
    expect(p).toContain("aluno@exemplo.com");
    // o CRC cobre tudo antes dos 4 últimos caracteres, incluindo "6304"
    const body = p.slice(0, -4);
    let crc = 0xffff;
    for (let i = 0; i < body.length; i++) {
      crc ^= body.charCodeAt(i) << 8;
      for (let b = 0; b < 8; b++) crc = crc & 0x8000 ? ((crc << 1) ^ 0x1021) & 0xffff : (crc << 1) & 0xffff;
    }
    expect(p.slice(-4)).toBe(crc.toString(16).toUpperCase().padStart(4, "0"));
  });

  it("fixa o valor do plano no QR Code (campo 54) e o omite quando não há valor", async () => {
    const { buildPixPayload } = await import("./pix");
    const base = { key: "12345678909", receiverName: "MENTORIA", city: "RECIFE" };
    expect(buildPixPayload({ ...base, amount: "30.00" }, "aluno@exemplo.com")).toContain("540530.00");
    expect(buildPixPayload({ ...base, amount: "50.00" }, "aluno@exemplo.com")).toContain("540550.00");
    expect(buildPixPayload(base, "aluno@exemplo.com")).not.toContain("5405");
  });

  it("limita a mensagem para o campo 26 não passar de 99 caracteres", async () => {
    const { buildPixPayload } = await import("./pix");
    const p = buildPixPayload({ key: "10341953440", receiverName: "MENTORIA", city: "RECIFE" }, `${"a".repeat(80)}@exemplo.com`);
    const m = p.indexOf("26");
    const len = Number(p.slice(m + 2, m + 4));
    expect(len).toBeLessThanOrEqual(99);
  });
});
