// Dinheiro em centavos inteiros (nunca float). No banco: Decimal(10,2), lido/gravado como texto "42.00".

/** Converte Decimal do Prisma, string ("42", "42.5", "42.00") ou número com até 2 casas para centavos. */
export function toCents(value: { toString(): string } | string | number): number {
  const s = typeof value === "number" ? value.toFixed(2) : value.toString().trim();
  const m = /^(-)?(\d+)(?:\.(\d{1,2})\d*)?$/.exec(s);
  if (!m) throw new Error(`Valor monetário inválido: ${s}`);
  const [, neg, int, frac = ""] = m;
  const cents = Number(int) * 100 + Number(frac.padEnd(2, "0"));
  return neg ? -cents : cents;
}

/** Centavos -> texto aceito pelo Prisma em campos Decimal ("4200" -> "42.00"). */
export function fromCents(cents: number): string {
  if (!Number.isSafeInteger(cents)) throw new Error("Centavos devem ser inteiros.");
  const neg = cents < 0;
  const abs = Math.abs(cents);
  return `${neg ? "-" : ""}${Math.floor(abs / 100)}.${String(abs % 100).padStart(2, "0")}`;
}

/** "R$ 1.234,56" */
export function formatBRL(cents: number): string {
  const neg = cents < 0;
  const abs = Math.abs(cents);
  const int = Math.floor(abs / 100).toLocaleString("pt-BR");
  return `${neg ? "-" : ""}R$ ${int},${String(abs % 100).padStart(2, "0")}`;
}

/**
 * Lê um valor digitado no formulário ("42", "42,00", "1.234,56", "42.5") e devolve centavos.
 * Retorna null para texto inválido, negativo ou com mais de 2 casas decimais.
 */
export function parseMoneyInput(raw: unknown): number | null {
  if (typeof raw !== "string") return null;
  let s = raw.trim().replace(/^R\$\s*/i, "");
  if (!s) return null;
  if (s.includes(",")) s = s.replace(/\./g, "").replace(",", ".");
  if (!/^\d{1,7}(\.\d{1,2})?$/.test(s)) return null;
  return toCents(s);
}
