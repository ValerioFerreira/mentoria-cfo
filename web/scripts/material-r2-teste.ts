// Teste de ponta a ponta da entrega (sem login): lê um volume do R2, carimba com um titular de teste e confere o resultado.
//   npx tsx scripts/material-r2-teste.ts direito-administrativo/m04
import "dotenv/config";
import { PDFDocument } from "pdf-lib";
import { readMaterialPdf, r2Config, streamBytes } from "../src/lib/material-storage";
import { stampPdf } from "../src/lib/material-stamp";

async function main() {
  const id = process.argv[2] ?? "direito-administrativo/m04";
  const [disc, vol] = id.split("/");
  console.log("origem:", r2Config() ? "Cloudflare R2" : "disco (R2 não configurado)");
  const t0 = Date.now();
  const raw = await readMaterialPdf(disc, vol);
  if (!raw) throw new Error("PDF não encontrado");
  const t1 = Date.now();
  const stamped = await stampPdf(raw, { id: "teste", name: "Aluno de Teste", idLabel: "CPF 000.000.000-00" });
  const t2 = Date.now();
  const paginasAntes = (await PDFDocument.load(raw)).getPageCount();
  const paginasDepois = (await PDFDocument.load(stamped)).getPageCount();
  let recebidos = 0;
  const reader = streamBytes(stamped).getReader();
  for (;;) {
    const { done, value } = await reader.read();
    if (done) break;
    recebidos += value.length;
  }
  const mb = (n: number) => (n / 1024 / 1024).toFixed(2) + " MB";
  console.log(`leitura ${t1 - t0} ms · carimbo ${t2 - t1} ms`);
  console.log(`original ${mb(raw.length)} (${paginasAntes} págs.) · carimbado ${mb(stamped.length)} (${paginasDepois} págs.) · transmitido ${mb(recebidos)}`);
  if (paginasAntes !== paginasDepois || recebidos !== stamped.length) throw new Error("divergência após o carimbo ou o streaming");
  console.log(stamped.length > 4.5 * 1024 * 1024 ? "OK: passa de 4,5 MB e segue por streaming." : "OK (abaixo de 4,5 MB).");
}

main().catch((e) => {
  console.error(e instanceof Error ? e.message : e);
  process.exit(1);
});
