// Armazenamento dos PDFs do material próprio MentorIA.
// Produção: Cloudflare R2 (API compatível com S3), bucket privado, chave "material/<disciplina>/<mNN>.pdf".
// Desenvolvimento sem R2 configurado (ou com MATERIAL_STORAGE=disk): lê de material-pdf/ no disco (MATERIAL_DIR).
// O PDF nunca é público: só esta camada lê o bucket, e a rota o devolve já carimbado por aluno.
import { readFile } from "node:fs/promises";
import path from "node:path";
import { AwsClient } from "aws4fetch";

export type R2Config = { accountId: string; accessKeyId: string; secretAccessKey: string; bucket: string };

/** Lê a configuração do R2 do ambiente; devolve null se faltar qualquer variável (aí vale o disco). */
export function r2Config(env: NodeJS.ProcessEnv = process.env): R2Config | null {
  if (env.MATERIAL_STORAGE === "disk") return null;
  const accountId = env.R2_ACCOUNT_ID?.trim();
  const accessKeyId = env.R2_ACCESS_KEY_ID?.trim();
  const secretAccessKey = env.R2_SECRET_ACCESS_KEY?.trim();
  const bucket = env.R2_BUCKET?.trim();
  if (!accountId || !accessKeyId || !secretAccessKey || !bucket) return null;
  return { accountId, accessKeyId, secretAccessKey, bucket };
}

export function materialKey(disc: string, vol: string): string {
  return `material/${disc}/${vol}.pdf`;
}

function objectUrl(cfg: R2Config, key: string): string {
  return `https://${cfg.accountId}.r2.cloudflarestorage.com/${cfg.bucket}/${key}`;
}

function client(cfg: R2Config): AwsClient {
  return new AwsClient({ accessKeyId: cfg.accessKeyId, secretAccessKey: cfg.secretAccessKey, service: "s3", region: "auto" });
}

/** PDF do volume (bytes), ou null se não existir. Erros de rede ou de credencial viram exceção (não "não encontrado"). */
export async function readMaterialPdf(disc: string, vol: string): Promise<Uint8Array | null> {
  const cfg = r2Config();
  if (!cfg) {
    const dir = process.env.MATERIAL_DIR ?? path.resolve(process.cwd(), "..", "material-pdf");
    try {
      return new Uint8Array(await readFile(path.join(dir, disc, `${vol}.pdf`)));
    } catch {
      return null;
    }
  }
  const res = await client(cfg).fetch(objectUrl(cfg, materialKey(disc, vol)), { method: "GET" });
  if (res.status === 404) return null;
  if (!res.ok) throw new Error(`R2 respondeu ${res.status} ao ler ${materialKey(disc, vol)}`);
  return new Uint8Array(await res.arrayBuffer());
}

/** Grava (ou substitui) o PDF no R2. Devolve o ETag (MD5 do objeto, entre aspas) informado pelo R2. */
export async function putMaterialPdf(cfg: R2Config, key: string, body: Uint8Array): Promise<string> {
  const res = await client(cfg).fetch(objectUrl(cfg, key), {
    method: "PUT",
    body: Buffer.from(body),
    headers: { "Content-Type": "application/pdf" },
  });
  if (!res.ok) throw new Error(`R2 respondeu ${res.status} ao gravar ${key}`);
  return res.headers.get("etag") ?? "";
}

/** Metadados do objeto (tamanho e ETag) sem baixá-lo, ou null se não existir. */
export async function headMaterialPdf(cfg: R2Config, key: string): Promise<{ size: number; etag: string } | null> {
  const res = await client(cfg).fetch(objectUrl(cfg, key), { method: "HEAD" });
  if (res.status === 404) return null;
  if (!res.ok) throw new Error(`R2 respondeu ${res.status} ao consultar ${key}`);
  return { size: Number(res.headers.get("content-length") ?? 0), etag: res.headers.get("etag") ?? "" };
}

/**
 * Entrega os bytes por streaming, em pedaços. Na Vercel, a resposta comum de uma função é limitada a 4,5 MB; a resposta
 * em streaming não tem esse limite, e os PDFs do material passam disso.
 */
export function streamBytes(bytes: Uint8Array, chunkSize = 64 * 1024): ReadableStream<Uint8Array> {
  let offset = 0;
  return new ReadableStream<Uint8Array>({
    pull(controller) {
      if (offset >= bytes.length) {
        controller.close();
        return;
      }
      controller.enqueue(bytes.subarray(offset, offset + chunkSize));
      offset += chunkSize;
    },
  });
}
