import { describe, expect, it } from "vitest";
import { cpfDigits, formatCpf, isValidCpf, maskCpf } from "./cpf";

describe("cpf", () => {
  it("valida os dígitos verificadores", () => {
    expect(isValidCpf("123.456.789-09")).toBe(true);
    expect(isValidCpf("12345678909")).toBe(true);
    expect(isValidCpf("123.456.789-00")).toBe(false);
    expect(isValidCpf("111.111.111-11")).toBe(false);
    expect(isValidCpf("123")).toBe(false);
  });
  it("formata e oculta", () => {
    expect(cpfDigits("123.456.789-09")).toBe("12345678909");
    expect(formatCpf("12345678909")).toBe("123.456.789-09");
    expect(maskCpf("12345678909")).toBe("***.456.789-**");
  });
});
