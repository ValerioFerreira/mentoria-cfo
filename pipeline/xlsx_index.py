"""Etapa 2 — Lê docs/indice_topicos_curso.xlsx (sem openpyxl) e normaliza em pipeline/.cache/index.json.

Cada tópico: {subject, aula, aulaNumber, title, level, number, pdfPage, printedPage, origin, file}
Linhas sem título (páginas de sumário) são descartadas.
"""
from __future__ import annotations

import json
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(__file__))
from config import INDEX_JSON, XLSX_PATH, aula_id, subject_by_prefix, parse_pdf_name  # noqa: E402

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
_T = "{%s}t" % NS["m"]


def _shared_strings(z: zipfile.ZipFile) -> list[str]:
    root = ET.fromstring(z.read("xl/sharedStrings.xml"))
    return ["".join(t.text or "" for t in si.iter(_T)) for si in root.findall("m:si", NS)]


def _read_sheet(z: zipfile.ZipFile, name: str, shared: list[str]) -> list[dict[str, str]]:
    root = ET.fromstring(z.read(name))
    rows: list[dict[str, str]] = []
    for row in root.find("m:sheetData", NS).findall("m:row", NS):
        vals: dict[str, str] = {}
        for c in row.findall("m:c", NS):
            col = "".join(ch for ch in c.get("r") if ch.isalpha())
            v = c.find("m:v", NS)
            if v is None:
                inline = c.find("m:is", NS)
                vals[col] = "".join(x.text or "" for x in inline.iter(_T)) if inline is not None else ""
            elif c.get("t") == "s":
                vals[col] = shared[int(v.text)]
            else:
                vals[col] = v.text or ""
        rows.append(vals)
    return rows


def _to_int(s: str | None) -> int | None:
    return int(float(s)) if s not in (None, "") else None


def build_index() -> dict:
    subjects = subject_by_prefix()
    with zipfile.ZipFile(XLSX_PATH) as z:
        shared = _shared_strings(z)
        topics_rows = _read_sheet(z, "xl/worksheets/sheet2.xml", shared)[1:]
        cov_rows = _read_sheet(z, "xl/worksheets/sheet3.xml", shared)[1:]

    def locate(fonte: str) -> tuple[str, int, str] | None:
        # 'downloads/01 - CBM-PE (Oficial) Língua Inglesa/001 - Aula 00 ....pdf'
        parts = fonte.replace("\\", "/").split("/")
        if len(parts) < 2:
            return None
        subj = subjects.get(parts[-2][:2])
        parsed = parse_pdf_name(parts[-1])
        if subj is None or parsed is None:
            return None
        return subj.id, parsed[1], parts[-1]

    topics = []
    for r in topics_rows:
        title = (r.get("C") or "").strip()
        loc = locate(r.get("I", ""))
        pdf_page = _to_int(r.get("G"))
        if not title or loc is None or pdf_page is None:
            continue
        subj_id, aula_n, fname = loc
        topics.append(
            {
                "subject": subj_id,
                "aula": aula_id(subj_id, aula_n),
                "aulaNumber": aula_n,
                "title": re.sub(r"\s+", " ", title),
                "level": _to_int(r.get("D")) or 1,
                "number": r.get("E") or "",
                "pdfPage": pdf_page,
                "printedPage": _to_int(r.get("H")),
                "origin": r.get("J", ""),
                "file": fname,
            }
        )

    coverage = []
    for r in cov_rows:
        loc = locate(r.get("C", ""))
        if loc is None:
            continue
        subj_id, aula_n, fname = loc
        coverage.append(
            {
                "aula": aula_id(subj_id, aula_n),
                "subject": subj_id,
                "aulaNumber": aula_n,
                "file": fname,
                "pdfPages": _to_int(r.get("D")),
                "tocPages": r.get("E", ""),  # texto livre, ex.: "2, 3"
                "topicsIndexed": _to_int(r.get("F")),
                "status": r.get("I", ""),
            }
        )
    return {"topics": topics, "coverage": coverage}


def main() -> int:
    idx = build_index()
    INDEX_JSON.parent.mkdir(parents=True, exist_ok=True)
    INDEX_JSON.write_text(json.dumps(idx, ensure_ascii=False), encoding="utf-8")
    print(f"{len(idx['topics'])} tópicos, {len(idx['coverage'])} aulas -> {INDEX_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
