// Envia os PDFs do material próprio (material-pdf/<disciplina>/mNN.pdf) para o Cloudflare R2 e confere o resultado.
// Idempotente: só grava o que ainda não está no bucket com o mesmo conteúdo (MD5 local = ETag do R2).
// As credenciais vêm de web/.env (R2_ACCOUNT_ID, R2_ACCESS_KEY_ID, R2_SECRET_ACCESS_KEY, R2_BUCKET); nada é impresso delas.
//   npx tsx scripts/material-r2.ts --verificar            # só leitura: compara o disco com o bucket
//   npx tsx scripts/material-r2.ts                        # envia o que faltar ou diferir
//   npx tsx scripts/material-r2.ts --only direito-administrativo/m04
import "dotenv/config";
import { createHash } from "node:crypto";
import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import path from "node:path";
import { headMaterialPdf, materialKey, putMaterialPdf, r2Config } from "../src/lib/material-storage";

const DIR = process.env.MATERIAL_DIR ?? path.resolve(__dirname, "..", "..", "material-pdf");
const only = process.argv.includes("--only") ? process.argv[process.argv.indexOf("--only") + 1] : null;
const verifyOnly = process.argv.includes("--verificar");

function localPdfs(): { disc: string; vol: string; file: string }[] {
  if (!existsSync(DIR)) throw new Error(`pasta de PDFs não encontrada: ${DIR}`);
  const out: { disc: string; vol: string; file: string }[] = [];
  for (const disc of readdirSync(DIR)) {
    const dd = path.join(DIR, disc);
    if (!statSync(dd).isDirectory()) continue;
    for (const f of readdirSync(dd)) {
      const m = /^(m\d{2})\.pdf$/.exec(f);
      if (m) out.push({ disc, vol: m[1], file: path.join(dd, f) });
    }
  }
  // só volumes do índice publicado (content/material/index.json): rascunhos e sobras no disco não sobem
  const indexado = new Set(Object.keys((JSON.parse(readFileSync(path.resolve(__dirname, "..", "content", "material", "index.json"), "utf8")) as { volumes: Record<string, unknown> }).volumes));
  return out.filter((p) => indexado.has(`${p.disc}/${p.vol}`) && (!only || `${p.disc}/${p.vol}` === only)).sort((a, b) => `${a.disc}/${a.vol}`.localeCompare(`${b.disc}/${b.vol}`));
}

async function main() {
  const cfg = r2Config();
  if (!cfg) throw new Error("R2 não configurado: preencha R2_ACCOUNT_ID, R2_ACCESS_KEY_ID, R2_SECRET_ACCESS_KEY e R2_BUCKET em web/.env");
  const pdfs = localPdfs();
  if (!pdfs.length) throw new Error("nenhum PDF encontrado");
  let ok = 0;
  let enviados = 0;
  const problemas: string[] = [];
  for (const p of pdfs) {
    const id = `${p.disc}/${p.vol}`;
    const bytes = new Uint8Array(readFileSync(p.file));
    const md5 = createHash("md5").update(bytes).digest("hex");
    const key = materialKey(p.disc, p.vol);
    try {
      let head = await headMaterialPdf(cfg, key);
      const igual = (h: { size: number; etag: string } | null) => !!h && h.size === bytes.length && h.etag.replace(/"/g, "").toLowerCase() === md5;
      if (!igual(head) && !verifyOnly) {
        await putMaterialPdf(cfg, key, bytes);
        enviados++;
        head = await headMaterialPdf(cfg, key);
      }
      if (igual(head)) ok++;
      else problemas.push(`${id}: ${head ? "conteúdo diferente do disco" : "ausente no bucket"}`);
    } catch (e) {
      problemas.push(`${id}: ${e instanceof Error ? e.message : "erro"}`);
    }
  }
  console.log(`${pdfs.length} PDFs no disco · ${ok} conferem no bucket · ${enviados} enviados agora`);
  if (problemas.length) {
    console.log("Problemas:\n- " + problemas.join("\n- "));
    process.exitCode = 1;
  }
}

main().catch((e) => {
  console.error(e instanceof Error ? e.message : e);
  process.exit(1);
});
