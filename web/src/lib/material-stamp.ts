import "server-only";
import { readFileSync } from "node:fs";
import path from "node:path";
import fontkit from "@pdf-lib/fontkit";
import { PDFDocument, rgb } from "pdf-lib";

/**
 * Carimbo do titular: escreve "LICENCIADO PARA <NOME> · CPF <cpf>" (idLabel) na faixa do rodapé de cada página do PDF do material
 * próprio (menos a capa). O retângulo da faixa vem do índice (`faixaTitular`, pontos PDF com origem no canto superior
 * esquerdo), reservado pelo motor de PDF em pipeline/build_material.py. O identificador do titular também vai nos metadados.
 */
const FONT_DIR = path.join(process.cwd(), "src", "assets", "fonts");
let fonts: { regular: Buffer; bold: Buffer } | null = null;
let band: [number, number, number, number] | null = null;

function loadFonts() {
  fonts ??= {
    regular: readFileSync(path.join(FONT_DIR, "BarlowCondensed-SemiBold.ttf")),
    bold: readFileSync(path.join(FONT_DIR, "BarlowCondensed-ExtraBold.ttf")),
  };
  return fonts;
}

function loadBand(): [number, number, number, number] {
  if (band) return band;
  try {
    const idx = JSON.parse(readFileSync(path.join(process.cwd(), "content", "material", "index.json"), "utf8")) as { faixaTitular?: number[] };
    if (idx.faixaTitular?.length === 4) band = idx.faixaTitular as [number, number, number, number];
  } catch {}
  return (band ??= [162.99, 805.04, 432.28, 822.05]);
}

/** Nome em maiúsculas, sem caracteres que a fonte não tenha. */
export function stampName(name: string): string {
  return name.normalize("NFC").replace(/[^\p{L}\p{N} .'’-]/gu, "").replace(/\s+/g, " ").trim().toUpperCase();
}

export async function stampPdf(source: Uint8Array, owner: { id: string; name: string; idLabel: string }): Promise<Uint8Array> {
  const doc = await PDFDocument.load(source, { updateMetadata: false });
  doc.registerFontkit(fontkit);
  const f = loadFonts();
  const regular = await doc.embedFont(f.regular, { subset: true });
  const bold = await doc.embedFont(f.bold, { subset: true });
  const [x0, y0, x1, y1] = loadBand();
  const parts: [string, typeof regular][] = [
    ["LICENCIADO PARA ", regular],
    [stampName(owner.name) || "ALUNO", bold],
    [` · ${owner.idLabel}`, regular],
  ];
  const width = (size: number) => parts.reduce((s, [t, font]) => s + font.widthOfTextAtSize(t, size), 0);
  let size = 8.6;
  while (size > 5.5 && width(size) > x1 - x0) size -= 0.2;
  const ink = rgb(14 / 255, 27 / 255, 46 / 255);
  doc.getPages().forEach((page, i) => {
    if (i === 0) return; // a capa não leva faixa
    const h = page.getHeight();
    let x = x0 + (x1 - x0 - width(size)) / 2;
    const y = h - (y0 + (y1 - y0) / 2) - size * 0.34;
    for (const [t, font] of parts) {
      page.drawText(t, { x, y, size, font, color: ink });
      x += font.widthOfTextAtSize(t, size);
    }
  });
  doc.setKeywords([...(doc.getKeywords()?.split(/;\s*/) ?? []), `titular:${owner.id}`]);
  return doc.save();
}
