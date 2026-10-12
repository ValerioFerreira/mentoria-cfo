import "server-only";
import { createHmac, timingSafeEqual } from "node:crypto";

const API = "https://api.mercadopago.com";

export class MercadoPagoError extends Error {
  constructor(readonly status: number) {
    super("Mercado Pago API request failed");
    this.name = "MercadoPagoError";
  }
}

export function mercadoPagoToken(): string {
  // Accept the key currently configured in Vercel as well as the canonical
  // name used by .env.example, so production settings need not be renamed.
  const token = process.env.MERCADOPAGO_ACCESS_TOKEN || process.env.MERCADO_PAGO_ACCESS_TOKEN;
  if (!token) throw new Error("MERCADOPAGO_ACCESS_TOKEN is not configured");
  return token;
}

export function siteUrl(): URL {
  const configured = process.env.APP_URL || process.env.SITE_URL ||
    (process.env.VERCEL_PROJECT_PRODUCTION_URL ? `https://${process.env.VERCEL_PROJECT_PRODUCTION_URL}` : null);
  if (!configured) throw new Error("APP_URL is not configured");
  const url = new URL(configured.startsWith("http") ? configured : `https://${configured}`);
  if (process.env.NODE_ENV === "production" && url.protocol !== "https:") {
    throw new Error("APP_URL must use HTTPS in production");
  }
  return url;
}

export async function mpRequest<T>(path: string, init: RequestInit = {}): Promise<T> {
  const response = await fetch(`${API}${path}`, {
    ...init,
    headers: {
      Authorization: `Bearer ${mercadoPagoToken()}`,
      "Content-Type": "application/json",
      ...(init.headers || {}),
    },
    cache: "no-store",
  });
  if (!response.ok) {
    // Não incluir corpo da resposta: pode conter dados pessoais ou informações operacionais.
    throw new MercadoPagoError(response.status);
  }
  return response.json() as Promise<T>;
}

export function verifyMercadoPagoSignature(input: {
  signature: string | null;
  requestId: string | null;
  dataId: string | null;
}): boolean {
  const secret = process.env.MERCADOPAGO_WEBHOOK_SECRET;
  if (!secret || !input.signature || !input.requestId || !input.dataId) return false;
  const fields = Object.fromEntries(input.signature.split(",").map((part) => {
    const [key, ...value] = part.trim().split("=");
    return [key, value.join("=")];
  }));
  const ts = fields.ts;
  const received = fields.v1;
  if (!ts || !received || !/^[a-f0-9]{64}$/i.test(received)) return false;
  const manifest = `id:${input.dataId.toLowerCase()};request-id:${input.requestId};ts:${ts};`;
  const expected = createHmac("sha256", secret).update(manifest).digest();
  const actual = Buffer.from(received, "hex");
  return actual.length === expected.length && timingSafeEqual(actual, expected);
}

