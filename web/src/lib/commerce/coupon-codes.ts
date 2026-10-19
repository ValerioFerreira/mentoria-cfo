// Regras puras dos códigos de cupom (sem banco): formato, leitura do que o cliente digitou e comparação de conjuntos.
import { CommerceError } from "./errors";

/** Código de cupom (do site ou de parceiro): 4 a 20 letras maiúsculas ou números. */
export const COUPON_CODE = /^[A-Z0-9]{4,20}$/;
/** Máximo de cupons numa mesma contratação (um de parceiro + os do site). */
export const MAX_COUPONS_PER_CONTRACT = 5;

export function normalizeCouponCode(raw: unknown): string | null {
  if (typeof raw !== "string") return null;
  const code = raw.trim().toUpperCase();
  return code ? code : null;
}

/**
 * Lê os códigos informados pelo cliente (separados por espaço, vírgula, ponto e vírgula ou quebra de linha),
 * em maiúsculas. Código repetido é recusado, não ignorado: o cliente vê o que o servidor realmente aplicou.
 */
export function parseCouponCodes(raw: unknown): string[] {
  const list = Array.isArray(raw) ? raw : typeof raw === "string" ? raw.split(/[\s,;]+/) : [];
  const codes: string[] = [];
  for (const item of list) {
    const code = normalizeCouponCode(item);
    if (!code) continue;
    if (codes.includes(code)) throw new CommerceError(`O cupom ${code} foi informado mais de uma vez.`, "COUPON_INVALID");
    codes.push(code);
  }
  if (codes.length > MAX_COUPONS_PER_CONTRACT) {
    throw new CommerceError(`Use no máximo ${MAX_COUPONS_PER_CONTRACT} cupons por contratação.`, "COUPON_INVALID");
  }
  return codes;
}

/** Chave estável de um conjunto de cupons (para comparar pedidos de uma mesma contratação). */
export function couponSetKey(codes: readonly (string | null | undefined)[]): string {
  return codes.filter(Boolean).sort().join("|");
}
