import "server-only";
import QRCode from "qrcode";

/**
 * Pix "copia e cola" estático (BR Code / EMV) para recebimento por chave Pix.
 * O e-mail do interessado vai na mensagem (campo de informação adicional, subcampo 02 do campo 26),
 * para que o recebedor veja no extrato de quem veio o pagamento.
 * A chave, o nome e a cidade vêm do ambiente (PIX_KEY, PIX_RECEIVER_NAME, PIX_CITY); o valor vem do plano escolhido (lib/plans.ts).
 */

function field(id: string, value: string): string {
  return `${id}${String(value.length).padStart(2, "0")}${value}`;
}

function crc16(payload: string): string {
  let crc = 0xffff;
  for (let i = 0; i < payload.length; i++) {
    crc ^= payload.charCodeAt(i) << 8;
    for (let b = 0; b < 8; b++) crc = crc & 0x8000 ? ((crc << 1) ^ 0x1021) & 0xffff : (crc << 1) & 0xffff;
  }
  return crc.toString(16).toUpperCase().padStart(4, "0");
}

/** Remove acentos e caracteres fora do ASCII imprimível (o BR Code só aceita ASCII). */
function ascii(s: string, max: number): string {
  return s
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .replace(/[^\x20-\x7e]/g, "")
    .trim()
    .slice(0, max);
}

export interface PixConfig {
  key: string;
  receiverName: string;
  city: string;
  /** valor fixo do QR Code (ex.: "30.00"); sem ele a pessoa digita o valor no app do banco */
  amount?: string;
}

export function pixConfig(): PixConfig | null {
  const key = process.env.PIX_KEY?.trim();
  if (!key) return null;
  return {
    key,
    receiverName: process.env.PIX_RECEIVER_NAME?.trim() || "MENTORIA",
    city: process.env.PIX_CITY?.trim() || "RECIFE",
  };
}

/** Monta o código "copia e cola". `message` é a mensagem do Pix (aqui, o e-mail do interessado). */
export function buildPixPayload(cfg: PixConfig, message: string, txId?: string): string {
  const gui = field("00", "br.gov.bcb.pix");
  const keyField = field("01", cfg.key);
  // o campo 26 inteiro tem no máximo 99 caracteres: sobra espaço para a mensagem depois do GUI e da chave
  const room = 99 - gui.length - keyField.length - 4;
  const msg = ascii(message, Math.max(0, room));
  const merchant = field("26", gui + keyField + (msg ? field("02", msg) : ""));
  // txId deve ter no máximo 25 caracteres alfanuméricos; padrão é ***
  const cleanTxId = (txId || "***").replace(/[^a-zA-Z0-9]/g, "").slice(0, 25) || "***";
  const body =
    field("00", "01") +
    field("01", "11") + // 11 = QR estático, reutilizável
    merchant +
    field("52", "0000") +
    field("53", "986") +
    (cfg.amount ? field("54", cfg.amount) : "") +
    field("58", "BR") +
    field("59", ascii(cfg.receiverName, 25) || "MENTORIA") +
    field("60", ascii(cfg.city, 15) || "RECIFE") +
    field("62", field("05", cleanTxId)) +
    "6304";
  return body + crc16(body);
}

/** QR Code do payload como data URI SVG. */
export async function pixQrDataUri(payload: string): Promise<string> {
  const svg = await QRCode.toString(payload, { type: "svg", errorCorrectionLevel: "M", margin: 1, color: { dark: "#111111", light: "#ffffff" } });
  return `data:image/svg+xml;base64,${Buffer.from(svg).toString("base64")}`;
}
