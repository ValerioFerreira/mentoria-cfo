import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { clearFailures, registerFailure, tooManyAttempts } from "./rate-limit";

let n = 0;
const key = () => `chave-${++n}`; // o mapa é global ao módulo: cada teste usa uma chave própria

describe("limite de tentativas", () => {
  beforeEach(() => {
    vi.useFakeTimers();
    vi.setSystemTime(new Date("2026-10-12T12:00:00Z"));
  });
  afterEach(() => vi.useRealTimers());

  it("sem falhas registradas não bloqueia", () => {
    expect(tooManyAttempts(key())).toBe(false);
  });
  it("bloqueia na 8ª falha (limite de 8 tentativas)", () => {
    const k = key();
    for (let i = 1; i <= 7; i++) {
      registerFailure(k);
      expect(tooManyAttempts(k), `após ${i} falhas`).toBe(false);
    }
    registerFailure(k);
    expect(tooManyAttempts(k)).toBe(true);
    registerFailure(k);
    expect(tooManyAttempts(k)).toBe(true);
  });
  it("as chaves são independentes (e-mails diferentes não se afetam)", () => {
    const a = key();
    const b = key();
    for (let i = 0; i < 8; i++) registerFailure(a);
    expect(tooManyAttempts(a)).toBe(true);
    expect(tooManyAttempts(b)).toBe(false);
  });
  it("a janela de 15 minutos expira e libera a chave", () => {
    const k = key();
    for (let i = 0; i < 8; i++) registerFailure(k);
    expect(tooManyAttempts(k)).toBe(true);
    vi.advanceTimersByTime(15 * 60_000 - 1);
    expect(tooManyAttempts(k)).toBe(true);
    vi.advanceTimersByTime(2);
    expect(tooManyAttempts(k)).toBe(false);
  });
  it("depois que a janela expira, uma nova falha reinicia a contagem em 1", () => {
    const k = key();
    for (let i = 0; i < 8; i++) registerFailure(k);
    vi.advanceTimersByTime(16 * 60_000);
    registerFailure(k);
    expect(tooManyAttempts(k)).toBe(false);
    for (let i = 0; i < 6; i++) registerFailure(k);
    expect(tooManyAttempts(k)).toBe(false); // 7 falhas na nova janela
    registerFailure(k);
    expect(tooManyAttempts(k)).toBe(true);
  });
  it("a janela não é renovada por novas falhas (conta a partir da primeira)", () => {
    const k = key();
    registerFailure(k);
    vi.advanceTimersByTime(14 * 60_000);
    for (let i = 0; i < 7; i++) registerFailure(k);
    expect(tooManyAttempts(k)).toBe(true);
    vi.advanceTimersByTime(61_000); // 15 min + 1 s desde a primeira falha
    expect(tooManyAttempts(k)).toBe(false);
  });
  it("clearFailures zera a contagem (login bem-sucedido)", () => {
    const k = key();
    for (let i = 0; i < 8; i++) registerFailure(k);
    clearFailures(k);
    expect(tooManyAttempts(k)).toBe(false);
    clearFailures("nunca-registrada"); // não quebra
  });
});
