"""PyMuPDF: marcadores (outline), metadados, páginas de cada capítulo, carimbo de exemplo e conferências do PDF."""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

import pymupdf
from validate_material import FORBIDDEN

from .assemble import MM, band_rect_pt
from .load import DESIGN_DIR, Volume

ALLOWED_FONTS = re.compile(r"Barlow|PublicSans|Public-?Sans|IBMPlex|NotoSans", re.I)  # Noto: só grego, índices e símbolos que a Public Sans não tem
SAMPLE_STAMP = ("LICENCIADO PARA ", "FULANO DE TAL DA SILVA", " · CPF 123.456.789-09")
MAX_MB, WARN_MB = 15, 10
PDF_COMMON_WORDS = {"professor", "professora", "pessoal,", "preencher", "todo:", "a completar", "estratégia", "estrategia", "do curso", "no material", "na aula", "chatgpt", "tbd", "texto de apoio", "texto-base"}


def page_map(info: dict, pages: dict) -> dict:
    """Páginas do volume. Por capítulo (trecho): abertura/fim do capítulo, corpo, Mapa do capítulo, bloco no Mapa de revisão
    do volume e as questões dele (é daqui que a diretriz das atividades tira as páginas do material próprio)."""
    ids = pages["ids"]
    total = pages["total"]
    chapters = info["chapters"]
    after = ids.get("questoes") or ids.get("mapa") or total + 1
    out = {"total": total, "capitulos": {}, "secoes": {}}
    qstarts = [(c["trecho"], ids.get(f"qgrp-{c['anchor']}")) for c in chapters]
    qstarts = [(t, p) for t, p in qstarts if p]
    for i, c in enumerate(chapters):
        start = ids.get(c["anchor"])
        nxt = ids.get(chapters[i + 1]["anchor"]) if i + 1 < len(chapters) else after
        mapa = next((ids.get(a) for _, t, a in reversed(c["sections"]) if t.lower().startswith("mapa do cap")), None)
        q = None
        for j, (t, p) in enumerate(qstarts):
            if t == c["trecho"]:
                # o grupo seguinte pode começar no meio da página: ela entra nos dois intervalos
                end = qstarts[j + 1][1] if j + 1 < len(qstarts) else (ids.get("mapa") or total + 1) - 1
                q = {"pagina": p, "ate": max(p, end)}
        out["capitulos"][c["trecho"]] = {"numero": c["number"], "titulo": c["title"],
                                         "pagina": start, "ate": (nxt - 1) if (start and nxt) else None,
                                         "corpo": ids.get(f"{c['anchor']}-corpo"), "mapa": mapa,
                                         "revisao": ids.get(f"rev-{c['anchor']}"), "questoes": q}
        for _, _, a in c["sections"]:
            out["secoes"][a] = ids.get(a)
    for k in ("apresentacao", "questoes", "mapa", "fim"):
        out[k] = ids.get(k)
    return out


def finish(pdf_path: Path, v: Volume, info: dict, pages: dict, sample_stamp: bool) -> tuple[dict, list[str], list[str]]:
    """Grava outline/metadados (e o carimbo de exemplo) e devolve (mapa de páginas, erros, avisos)."""
    pm = page_map(info, pages)
    doc = pymupdf.open(pdf_path)
    errors: list[str] = []
    warns: list[str] = list(pages.get("warns", []))
    if doc.page_count != pm["total"]:
        errors.append(f"o PDF tem {doc.page_count} páginas e o Paged.js informou {pm['total']}")

    # outline
    toc = [[1, "Capa", 1]]
    if pm.get("apresentacao"):
        toc.append([1, "Apresentação do volume", pm["apresentacao"]])
    for c in info["chapters"]:
        p = pm["capitulos"][c["trecho"]]["pagina"] or 1
        toc.append([1, f"Capítulo {c['number']} · {c['title']}", p])
        for num, title, a in c["sections"]:
            toc.append([2, f"{num} {title}", pm["secoes"].get(a) or p])
    for k, label in (("questoes", "Questões comentadas"), ("mapa", "Mapa de revisão do volume")):
        if pm.get(k):
            toc.append([1, label, pm[k]])
    doc.set_toc(toc)
    doc.set_metadata({
        "title": f"{v.subject_name} · {v.label} · {v.title}", "author": "MentorIA", "subject": v.id,
        "keywords": f"MentorIA; material próprio; {v.subject_name}", "creator": "MentorIA build_material.py",
        "producer": "MentorIA", "creationDate": pymupdf.get_pdf_now(), "modDate": pymupdf.get_pdf_now(),
    })
    try:
        doc.set_language("pt-BR")
    except AttributeError:  # pragma: no cover - versões antigas do PyMuPDF
        pass

    band = pymupdf.Rect(band_rect_pt())
    if sample_stamp:
        font = pymupdf.Font(fontfile=str(DESIGN_DIR / "fonts" / "BarlowCondensed-SemiBold.ttf"))
        bold = pymupdf.Font(fontfile=str(DESIGN_DIR / "fonts" / "BarlowCondensed-ExtraBold.ttf"))
        size = 8.6
        widths = [font.text_length(SAMPLE_STAMP[0], size), bold.text_length(SAMPLE_STAMP[1], size), font.text_length(SAMPLE_STAMP[2], size)]
        for pno in range(1, doc.page_count):  # a capa não leva faixa
            page = doc[pno]
            page.wrap_contents()  # o Chromium deixa a matriz de escala aberta no fluxo da página
            tw = pymupdf.TextWriter(page.rect, color=(14 / 255, 27 / 255, 46 / 255))
            x = band.x0 + (band.width - sum(widths)) / 2
            y = band.y0 + band.height / 2 + size * 0.34
            for txt, f, w in zip(SAMPLE_STAMP, (font, bold, font), widths):
                tw.append((x, y), txt, font=f, fontsize=size)
                x += w
            tw.write_text(page)
    tmp = pdf_path.with_suffix(".tmp.pdf")
    doc.save(tmp, garbage=3, deflate=True)
    doc.close()
    tmp.replace(pdf_path)

    e2, w2 = check(pdf_path, v, info, pm, sample_stamp)
    return pm, errors + e2, warns + w2


def _text_upper(doc) -> list[str]:
    return [doc[i].get_text("text") for i in range(doc.page_count)]


def check(pdf_path: Path, v: Volume, info: dict, pm: dict, sample_stamp: bool = False) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warns: list[str] = []
    doc = pymupdf.open(pdf_path)
    band = pymupdf.Rect(band_rect_pt())
    footer_top = doc[0].rect.height - 24 * MM

    # 1. capítulos: âncora, página e ordem
    last = 0
    for c in info["chapters"]:
        cp = pm["capitulos"].get(c["trecho"], {})
        if not cp.get("pagina"):
            errors.append(f"capítulo {c['number']} ({c['trecho']}) sem página")
            continue
        if cp["pagina"] <= last:
            errors.append(f"capítulo {c['number']} fora de ordem (pág. {cp['pagina']})")
        last = cp["pagina"]
        n = (cp["ate"] or cp["pagina"]) - cp["pagina"] + 1
        if n > 30:
            warns.append(f"capítulo {c['number']} com {n} páginas (> 30)")
        if n < 4:
            warns.append(f"capítulo {c['number']} com {n} páginas (< 4)")

    texts = _text_upper(doc)
    fonts: set[str] = set()
    for pno in range(doc.page_count):
        page = doc[pno]
        for f in page.get_fonts(full=True):
            fonts.add(f[3].split("+")[-1])
        if pno == 0:
            continue
        words = page.get_text("words")
        # 2. página em branco e texto fora da área útil
        body_words = [w for w in words if w[3] < footer_top]
        if not body_words and not page.get_images() and len(page.get_drawings()) < 3:
            errors.append(f"página {pno + 1} em branco")
        out = [w[4] for w in words if w[0] < 12 * MM or w[2] > page.rect.width - 12 * MM or w[3] > page.rect.height - 4 * MM]
        if out:
            errors.append(f"página {pno + 1}: texto fora da área útil ({' '.join(out[:5])})")
        # 3. faixa do titular vazia (texto e pixels)
        if not sample_stamp:
            inband = [w[4] for w in words if pymupdf.Rect(w[:4]).intersects(band)]
            if inband:
                errors.append(f"página {pno + 1}: texto na faixa do titular ({' '.join(inband[:5])})")
            pix = page.get_pixmap(clip=band, dpi=48, colorspace=pymupdf.csGRAY)
            if min(pix.samples) < 250:
                errors.append(f"página {pno + 1}: desenho na faixa do titular")
    # 4. fontes embutidas
    bad = sorted(f for f in fonts if f and not ALLOWED_FONTS.search(f))
    if bad:
        errors.append(f"fontes fora do modelo: {', '.join(bad)}")
    # 5 e 6. figuras com erro e termos proibidos
    full = "\n".join(texts)
    low = full.lower()
    for bad_txt in ("syntax error", "```", "flowchart ", "graph td", "graph lr", "xqblock", "[!"):
        if bad_txt in low:
            errors.append(f"texto cru no PDF: {bad_txt!r}")
    # Capítulos, volume.md e comentários já passam pelo validator com a lista completa; no PDF inteiro entram também os enunciados
    # do banco, onde estas palavras comuns são legítimas ("professor", "preencha", "estratégia", "Regime de pessoal, ...").
    for term in (x for x in FORBIDDEN if x not in PDF_COMMON_WORDS):
        t = term.lower()
        if re.search(rf"(?<!\w){re.escape(t)}(?!\w)", low):
            pg = next(i + 1 for i, tx in enumerate(texts) if t in tx.lower())
            errors.append(f"termo proibido no PDF: {term!r} (pág. {pg})")
    # 7. cada questão aparece uma vez, com o comentário logo abaixo e o gabarito certo
    flat = re.sub(r"\s+", " ", full).upper()
    nums = [n for n, _ in info["questions"]]
    for i, (num, ans) in enumerate(info["questions"]):
        hits = [m.start() for m in re.finditer(rf"QUESTÃO {num} ·", flat)]
        if len(hits) != 1:
            errors.append(f"questão {num} aparece {len(hits)} vez(es)")
            continue
        nxt = re.search(rf"QUESTÃO {nums[i + 1]} ·", flat[hits[0]:]) if i + 1 < len(nums) else None
        block = flat[hits[0]: hits[0] + nxt.start()] if nxt else flat[hits[0]:]
        if not re.search(rf"GABARITO {re.escape(str(ans).upper())} ·", block):
            errors.append(f"questão {num}: gabarito {ans} não aparece logo abaixo dela")
    # 9. quebras: abertura numa página só, cabeçalho e rodapé, caixa partida vazia, figura cortada
    openings = {cp["pagina"] for cp in pm["capitulos"].values() if cp.get("pagina")}
    for c in info["chapters"]:
        cp = pm["capitulos"].get(c["trecho"], {})
        if cp.get("pagina") and cp.get("corpo") and cp["corpo"] != cp["pagina"] + 1:
            errors.append(f"abertura do capítulo {c['number']} ocupa {cp['corpo'] - cp['pagina']} páginas (deve ser uma)")
    top, bottom = 21 * MM, doc[0].rect.height - 24 * MM
    for pno in range(1, doc.page_count):
        page = doc[pno]
        words = page.get_text("words")
        if "missaomentoria" not in texts[pno].lower():
            errors.append(f"página {pno + 1} sem rodapé")
        if (pno + 1) not in openings and not [w for w in words if w[3] < 14 * MM]:
            errors.append(f"página {pno + 1} sem cabeçalho")
        if (pno + 1) in openings:
            continue
        for d in page.get_drawings():
            r = d["rect"]
            if r.y1 < top - 0.5 or r.y0 > bottom + 0.5:
                continue  # cabeçalho, régua e rodapé
            if r.y0 < bottom - 1 and r.y1 > bottom + 1 or r.y0 < top - 1 and r.y1 > top + 1:
                errors.append(f"página {pno + 1}: desenho cortado pela margem (y {r.y0 / MM:.0f} a {r.y1 / MM:.0f} mm)")
                continue
            if d.get("fill") is None or r.width < 3 * MM or not (1.2 * MM < r.height < 8 * MM):
                continue
            if r.y0 < top + 2 * MM or r.y1 > bottom - 2 * MM:
                if not [w for w in words if w[1] < r.y1 and w[3] > r.y0 and w[0] < r.x1 and w[2] > r.x0]:
                    errors.append(f"página {pno + 1}: caixa partida vazia ({r.height / MM:.1f} mm) no {'topo' if r.y0 < top + 2 * MM else 'pé'}")
        for im in page.get_image_info():
            b = pymupdf.Rect(im["bbox"])
            if b.y0 < bottom - 1 and b.y1 > bottom + 1 or b.y0 < top - 1 and b.y1 > top + 1:
                errors.append(f"página {pno + 1}: imagem cortada pela margem")
    doc.close()
    # 8. tamanho
    mb = pdf_path.stat().st_size / 2**20
    if mb > MAX_MB:
        errors.append(f"PDF com {mb:.1f} MB (limite {MAX_MB})")
    elif mb > WARN_MB:
        warns.append(f"PDF com {mb:.1f} MB")
    return errors, warns


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()
