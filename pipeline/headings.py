"""Etapa 3b — Detecta subtítulos por tamanho de fonte (enriquece o índice, que às vezes tem 1 tópico por aula).

Template do Estratégia: corpo ≈ 11–12 pt; subtítulos 14–16 pt; título de seção 19–24 pt (já está no índice);
cabeçalho/rodapé 9 pt. Aqui só entram linhas com tamanho ∈ [corpo+2, corpo+5].

Saída: pipeline/.cache/headings/<key>.json  ->  [{page, text, size}]
Uso:  python pipeline/headings.py [--only 06] [--force]
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import re
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed

import pymupdf

sys.path.insert(0, os.path.dirname(__file__))
from config import CACHE_DIR, DOCS_DIR, parse_pdf_name, pdf_key, subject_by_prefix  # noqa: E402

HEADINGS_DIR = CACHE_DIR / "headings"
STOP = re.compile(
    r"^(bizu|aten[çc][ãa]o|exemplo|exemplos|dica|importante|observa[çc][ãa]o|gabarito|coment[áa]rio|"
    r"quest[ãa]o|quest[õo]es|mapa mental|resumo|saiba mais|para saber mais|curiosidade|obs\b|nota\b|"
    r"cuidado|jurisprud[êe]ncia|aten[çc][ãa]o!)",
    re.IGNORECASE,
)


def extract_headings(pdf_path: str, out_path: str) -> int:
    doc = pymupdf.open(pdf_path)
    sizes: collections.Counter = collections.Counter()
    pages_lines: list[list[tuple[str, float, float, float]]] = []
    for page in doc:
        lines = []
        for b in page.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                spans = l["spans"]
                txt = "".join(s["text"] for s in spans).strip()
                if not txt:
                    continue
                for s in spans:
                    sizes[round(s["size"], 1)] += len(s["text"])
                mx = max(s["size"] for s in spans)
                mn = min(s["size"] for s in spans)
                if mx - mn > 1.0:  # versaletes/misto: ignora
                    continue
                lines.append((txt, round(mx, 1), l["bbox"][1], l["bbox"][3]))
        pages_lines.append(lines)
    body = sizes.most_common(1)[0][0] if sizes else 12.0

    heads: list[dict] = []
    for pn, lines in enumerate(pages_lines, 1):
        if pn == 1:
            continue
        cur: dict | None = None
        for txt, size, y0, y1 in sorted(lines, key=lambda x: x[2]):
            ok = body + 1.9 <= size <= body + 5.2 and 4 <= len(txt) <= 120 and not txt.isdigit() and not STOP.match(txt)
            if ok and cur and abs(cur["size"] - size) < 0.3 and y0 - cur["y1"] < 0.9 * size:
                cur["text"] += " " + txt
                cur["y1"] = y1
                continue
            if cur:
                heads.append(cur)
                cur = None
            if ok:
                cur = {"page": pn, "text": txt, "size": size, "y1": y1}
        if cur:
            heads.append(cur)

    # descarta rótulos que se repetem muito na aula (caixas "ATENÇÃO", cabeçalhos de tabela)
    cnt = collections.Counter(h["text"].lower() for h in heads)
    heads = [{"page": h["page"], "text": re.sub(r"\s+", " ", h["text"]), "size": h["size"]} for h in heads if cnt[h["text"].lower()] < 4]
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump({"body": body, "headings": heads}, fh, ensure_ascii=False)
    return len(heads)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--workers", type=int, default=min(6, os.cpu_count() or 2))
    args = ap.parse_args()
    HEADINGS_DIR.mkdir(parents=True, exist_ok=True)
    subjects = subject_by_prefix()
    jobs = []
    for folder in sorted(p for p in DOCS_DIR.iterdir() if p.is_dir()):
        if folder.name[:2] not in subjects or (args.only and folder.name[:2] != args.only):
            continue
        for pdf in sorted(folder.glob("*.pdf")):
            if parse_pdf_name(pdf.name) is None:
                continue
            out = HEADINGS_DIR / f"{pdf_key(folder.name, pdf.name)}.json"
            if out.exists() and not args.force and out.stat().st_mtime > pdf.stat().st_mtime:
                continue
            jobs.append((str(pdf), str(out)))
    print(f"{len(jobs)} PDF(s)")
    done = 0
    with ProcessPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(extract_headings, *j): j for j in jobs}
        for f in as_completed(futs):
            done += 1
            print(f"[{done}/{len(jobs)}] {os.path.basename(futs[f][1])}: {f.result()} subtítulos", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
