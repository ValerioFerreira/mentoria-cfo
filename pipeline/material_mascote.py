"""Prepara as imagens do mascote para o motor de PDF: fundo branco -> transparente, mesma escala e mesma linha de base.

Entrada: design/material/prontidao/mascote/originais/{CHAMA|FOCO} <REAÇÃO>.jpg (fundo branco; CHAMA = corpo claro, FOCO = corpo escuro).
Saída:   design/material/prontidao/mascote/chama/<slug>.png e foco/<slug>.png (600 × 600, RGBA).
O motor usa a versão escolhida (build_material.py --mascote chama|foco) nas páginas claras e a CHAMA na faixa escura das aberturas.

Uso: python pipeline/material_mascote.py [--folha]   (--folha grava uma folha de conferência sobre os fundos dos quadros)
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
MASCOT_DIR = ROOT / "design" / "material" / "prontidao" / "mascote"
SRC_DIR = MASCOT_DIR / "originais"
SLUGS = {"atencao", "pegadinha", "bizu", "exemplo", "jurisprudencia", "resolvido", "missao", "cai-na-prova", "praticar", "gabarito",
         "revisao", "missao-cumprida"}
SIZE, FIG_H, BOTTOM = 600, 564, 18  # tela, altura da figura, margem inferior (px); 600 px = 340 dpi no maior uso (45 mm)
WORK = 1400  # lado de trabalho antes do recorte
LOGO_DIR = ROOT / "design" / "material" / "prontidao" / "logo"
LOGO_MAX = 800


def slug_of(name: str) -> tuple[str, str] | None:
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower()
    m = re.match(r"^(chama|foco)\W+(.+)$", s)
    if not m:
        return None
    slug = re.sub(r"[^a-z]+", "-", m.group(2)).strip("-")
    return (m.group(1), slug) if slug in SLUGS else None


def cutout(path: Path) -> Image.Image:
    """Imagem em RGBA com o fundo branco (e a sombra clara ligada a ele) transparente, ainda sem recorte."""
    im = Image.open(path).convert("RGB")
    im.thumbnail((WORK, WORK), Image.LANCZOS)
    a = np.asarray(im).astype(np.float32)
    mn, mx = a.min(2), a.max(2)
    spread = mx - mn
    # fundo: branco neutro ligado à borda
    cand = (mn >= 244) & (spread <= 8)
    lab, _ = ndimage.label(cand)
    edge = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
    bg = np.isin(lab, edge[edge > 0])
    # sombra suave: cinza neutro claro ligado ao fundo (reconstrução geodésica), sem invadir o corpo creme
    soft = (spread <= 8) & (mn >= 170)
    shadow = ndimage.binary_propagation(bg, mask=soft | bg) & ~bg
    # faixa de borda (antisserrilhado): até 2 px do fundo
    band = ndimage.binary_dilation(bg, iterations=2) & ~bg
    region = bg | shadow | band
    # "cor para alfa" contra o branco, só na região de fundo/sombra/borda
    alpha = np.ones(mn.shape, np.float32)
    al = np.clip((255.0 - mn) / 255.0, 0, 1)
    al = np.where(shadow & ~band, al * 1.6, al)  # sombra um pouco mais visível
    alpha[region] = np.clip(al[region], 0, 1)
    rgb = a.copy()
    safe = np.maximum(alpha, 1e-3)[..., None]
    un = (a - 255.0 * (1 - alpha[..., None])) / safe
    rgb[region] = np.clip(un[region], 0, 255)
    rgb[shadow & ~band] = 40.0  # sombra em cinza-escuro translúcido
    out = np.dstack([rgb, alpha * 255]).astype(np.uint8)
    return Image.fromarray(out, "RGBA")


def cut(path: Path) -> Image.Image:
    img = cutout(path)
    # recorte, escala única pela altura da figura e linha de base comum
    bbox = img.getchannel("A").point(lambda v: 255 if v > 10 else 0).getbbox()
    img = img.crop(bbox)
    k = min(FIG_H / img.height, (SIZE - 24) / img.width)
    img = img.resize((max(1, round(img.width * k)), max(1, round(img.height * k))), Image.LANCZOS)
    canvas = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    canvas.paste(img, ((SIZE - img.width) // 2, SIZE - BOTTOM - img.height), img)
    return canvas


def logo() -> list[str]:
    """Logo da empresa (logo/*.png|jpg, fundo branco) -> logo-completo.png (com o nome) e logo-mascote.png (sem o nome)."""
    src = next((p for p in sorted(LOGO_DIR.glob("*")) if p.suffix.lower() in {".png", ".jpg", ".jpeg"}
                and not p.name.startswith("logo-")), None)
    if not src:
        return []
    img = cutout(src)
    img = img.crop(img.getchannel("A").point(lambda v: 255 if v > 10 else 0).getbbox())
    # o nome fica embaixo: a faixa vazia mais alta na metade de baixo separa o mascote do texto
    a = np.asarray(img.getchannel("A")) > 10
    rows = a.any(1)
    h = len(rows)
    gap, best = None, 0
    y = h // 2
    while y < h:
        if not rows[y]:
            y0 = y
            while y < h and not rows[y]:
                y += 1
            if y - y0 > best:
                best, gap = y - y0, (y0, y)
        y += 1
    out = []
    full = img.copy()
    full.thumbnail((LOGO_MAX, LOGO_MAX), Image.LANCZOS)
    full.save(LOGO_DIR / "logo-completo.png", optimize=True)
    out.append("logo-completo.png")
    if gap:
        top = img.crop((0, 0, img.width, gap[0]))
        top = top.crop(top.getchannel("A").point(lambda v: 255 if v > 10 else 0).getbbox())
        top.thumbnail((LOGO_MAX, LOGO_MAX), Image.LANCZOS)
        top.save(LOGO_DIR / "logo-mascote.png", optimize=True)
        out.append("logo-mascote.png")
    return [f"logo/{n}  <-  {src.name}" for n in out]


def sheet(out: Path) -> None:
    bgs = ["#ffffff", "#fdece9", "#fff4d1", "#eaf1fe", "#e6f6f0", "#fdf0e3", "#f2ecfe", "#0e1b2e"]
    slugs = sorted(SLUGS)
    T = 150
    W = Image.new("RGB", (T * len(bgs), T * len(slugs) * 2), "#888")
    for r, slug in enumerate(slugs):
        for v, var in enumerate(("chama", "foco")):
            p = MASCOT_DIR / var / f"{slug}.png"
            if not p.exists():
                continue
            m = Image.open(p).resize((T, T), Image.LANCZOS)
            for c, color in enumerate(bgs):
                tile = Image.new("RGB", (T, T), color)
                tile.paste(m, (0, 0), m)
                W.paste(tile, (c * T, (r * 2 + v) * T))
    W.save(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--folha", metavar="PNG", help="grava a folha de conferência neste arquivo")
    args = ap.parse_args()
    found: dict[tuple[str, str], Path] = {}
    for f in sorted(SRC_DIR.glob("*")):
        if f.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
            continue
        key = slug_of(f.stem)
        if not key:
            print(f"ignorado (nome não reconhecido): {f.name}")
            continue
        if key in found:
            print(f"ERRO: {f.name} repete {found[key].name}")
            return 1
        found[key] = f
    missing = [(v, s) for v in ("chama", "foco") for s in sorted(SLUGS) if (v, s) not in found]
    for (var, slug), f in sorted(found.items()):
        (MASCOT_DIR / var).mkdir(parents=True, exist_ok=True)
        cut(f).save(MASCOT_DIR / var / f"{slug}.png", optimize=True)
        print(f"{var}/{slug}.png  <-  {f.name}")
    for line in logo():
        print(line)
    if missing:
        print("faltam:", ", ".join(f"{v}/{s}" for v, s in missing))
    if args.folha:
        sheet(Path(args.folha))
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
