"""Etapa 1 — Extração de texto por página dos PDFs do Estratégia.

Saída (cache local, nunca versionado): pipeline/.cache/pages/<key>.json
  { key, subject, aula, aulaNumber, file, pageCount, pages: [{n, chars, fffd, text}] }

O texto é limpo de cabeçalho/rodapé e da marca d'água com nome/CPF do aluno,
para que nenhum dado pessoal chegue às etapas seguintes.

Uso:  python pipeline/extract.py [--force] [--only 02]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed

import pymupdf  # PyMuPDF

sys.path.insert(0, os.path.dirname(__file__))
from config import DOCS_DIR, PAGES_DIR, aula_id, parse_pdf_name, pdf_key, subject_by_prefix  # noqa: E402

_CPF_LINE = re.compile(r"^\d{11}\s*-\s*.+$")
_FOOTER_SITE = "www.estrategiaconcursos.com.br"
_FOOTER_COURSE = re.compile(r"^(?:CBM-PE|CBMP-PE)\s+\((?:Oficial|Praça|Praca)\)\s+.+$", re.IGNORECASE)
_HEADER = re.compile(r"^.{3,80}\sAula\s+\d+\s*$")
_HIGHLIGHT = re.compile(r"==[0-9a-fA-F]{6}==")


def clean_page_text(raw: str) -> str:
    """Remove rodapé do Estratégia, marca d'água (nome/CPF), cabeçalho e artefatos de destaque."""
    lines = raw.splitlines()

    # 1) bloco de rodapé: [CBM-PE (Oficial) X] … [site] … [CPF - nome]
    if _FOOTER_SITE in (ln.strip() for ln in lines):
        site_idx = max(i for i, ln in enumerate(lines) if ln.strip() == _FOOTER_SITE)
        start = site_idx
        for i in range(site_idx - 1, max(site_idx - 7, -1), -1):
            s = lines[i].strip()
            if _FOOTER_COURSE.match(s) or s.isdigit() or s == "":
                start = i
            else:
                break
        end = site_idx
        for i in range(site_idx + 1, min(site_idx + 7, len(lines))):
            s = lines[i].strip()
            if _CPF_LINE.match(s) or s.isdigit() or s == "":
                end = i
            else:
                break
        del lines[start : end + 1]

    # 2) qualquer linha de marca d'água remanescente
    lines = [ln for ln in lines if not _CPF_LINE.match(ln.strip())]

    # 3) cabeçalho "<Professor> Aula NN" (primeira linha não vazia)
    for i, ln in enumerate(lines):
        if ln.strip():
            if _HEADER.match(ln.strip()):
                del lines[i]
            break

    text = "\n".join(lines)
    text = _HIGHLIGHT.sub("", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def extract_pdf(pdf_path: str, out_path: str, meta: dict) -> dict:
    doc = pymupdf.open(pdf_path)
    pages = []
    for i, page in enumerate(doc, 1):
        text = clean_page_text(page.get_text())
        pages.append({"n": i, "chars": len(text), "fffd": text.count("�"), "text": text})
    out = {**meta, "pageCount": len(pages), "pages": pages}
    tmp = out_path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False)
    os.replace(tmp, out_path)
    return {"key": meta["key"], "pages": len(pages)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="reextrai mesmo se já existir")
    ap.add_argument("--only", help="prefixo de pasta (ex.: 02) para extrair só uma disciplina")
    ap.add_argument("--workers", type=int, default=min(6, os.cpu_count() or 2))
    args = ap.parse_args()

    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    subjects = subject_by_prefix()
    jobs = []
    for folder in sorted(p for p in DOCS_DIR.iterdir() if p.is_dir()):
        prefix = folder.name[:2]
        subj = subjects.get(prefix)
        if subj is None or (args.only and prefix != args.only):
            continue
        for pdf in sorted(folder.glob("*.pdf")):
            parsed = parse_pdf_name(pdf.name)
            if parsed is None:
                print(f"[aviso] nome fora do padrão, ignorado: {pdf.name}")
                continue
            _, aula_n = parsed
            key = pdf_key(folder.name, pdf.name)
            out = PAGES_DIR / f"{key}.json"
            if out.exists() and not args.force and out.stat().st_mtime > pdf.stat().st_mtime:
                continue
            meta = {
                "key": key,
                "subject": subj.id,
                "aulaNumber": aula_n,
                "aula": aula_id(subj.id, aula_n),
                "file": pdf.name,
            }
            jobs.append((str(pdf), str(out), meta))

    print(f"{len(jobs)} PDF(s) para extrair com {args.workers} processo(s)")
    done = 0
    with ProcessPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(extract_pdf, *j): j for j in jobs}
        for fut in as_completed(futs):
            r = fut.result()
            done += 1
            print(f"[{done}/{len(jobs)}] {r['key']} ({r['pages']} págs.)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
