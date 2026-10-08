"""Inspeção de uma aula para auditoria (estrutura × PDF × segmentos). Só leitura.

Uso:
  python pipeline/inspect_aula.py <aula>                    # mapa de páginas, tópicos e trechos (ex.: direito-administrativo/a00)
  python pipeline/inspect_aula.py <aula> --pages 10-14      # texto das páginas (do cache)
  python pipeline/inspect_aula.py <aula> --heads            # 1ª linha "útil" de cada página (varredura rápida do PDF)
  python pipeline/inspect_aula.py <aula> --grep "regex"     # páginas da aula que casam com a regex (sem acento, minúsculas)
  python pipeline/inspect_aula.py <disciplina> --grep "..." # idem, em todas as aulas da disciplina
Opções: --chars N (corta cada página em N caracteres; padrão 4000 em --pages)

Mapa de páginas (pageMap): T teoria · C questões comentadas · L lista · K gabarito · S resumo · F abertura/sumário · B fechamento · X extra (fora do escopo, duplicada ou opcional).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(__file__))
from config import CONTENT_DIR  # noqa: E402
from textutil import aula_key_map, load_pages  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def fold(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


def runs(page_map: str) -> str:
    out, i = [], 0
    while i < len(page_map):
        j = i
        while j + 1 < len(page_map) and page_map[j + 1] == page_map[i]:
            j += 1
        out.append(f"{page_map[i]}{i + 1}-{j + 1}" if j > i else f"{page_map[i]}{i + 1}")
        i = j + 1
    return " ".join(out)


def load_aula(aula_id: str) -> tuple[dict, list[dict]]:
    subject = aula_id.split("/")[0]
    struct = json.loads((CONTENT_DIR / "structure" / f"{subject}.json").read_text(encoding="utf-8"))["aulas"]
    segs = json.loads((CONTENT_DIR / "segments" / f"{subject}.json").read_text(encoding="utf-8"))["segments"]
    a = next((x for x in struct if x["id"] == aula_id), None)
    if a is None:
        raise SystemExit(f"aula não encontrada: {aula_id}")
    return a, [s for s in segs if s["aula"] == aula_id]


def page_texts(aula_id: str) -> list[dict] | None:
    key = aula_key_map().get(aula_id)
    return load_pages(key)["pages"] if key else None


def first_line(text: str) -> str:
    for ln in text.splitlines():
        ln = ln.strip()
        if len(ln) >= 4 and not re.match(r"^(\d+\s*$|www\.|https?:|aula \d+|prof)", ln, re.I) and "estrategia" not in fold(ln):
            return ln[:110]
    return ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("--pages")
    ap.add_argument("--heads", action="store_true")
    ap.add_argument("--grep")
    ap.add_argument("--chars", type=int, default=4000)
    args = ap.parse_args()

    if "/" not in args.target:  # disciplina inteira (só --grep)
        if not args.grep:
            raise SystemExit("para uma disciplina, use --grep")
        rx = re.compile(args.grep)
        for aid in sorted(k for k in aula_key_map() if k.startswith(args.target + "/")):
            pages = page_texts(aid) or []
            hits = [p["n"] for p in pages if rx.search(fold(p["text"]))]
            if hits:
                print(f"{aid}: {len(hits)} págs. {hits[:40]}")
        return 0

    a, segs = load_aula(args.target)
    pages = page_texts(args.target)

    if args.pages:
        lo, _, hi = args.pages.partition("-")
        lo, hi = int(lo), int(hi or lo)
        if pages is None:
            raise SystemExit("texto da aula não está no cache (complemento autoral? veja content/complements/*.md)")
        pm = a.get("pageMap", "")
        for p in pages[lo - 1 : hi]:
            typ = pm[p["n"] - 1] if p["n"] - 1 < len(pm) else "?"
            print(f"\n===== pág. {p['n']} [{typ}] =====")
            print(p["text"][: args.chars])
        return 0

    if args.grep:
        rx = re.compile(args.grep)
        for p in pages or []:
            if rx.search(fold(p["text"])):
                print(f"pág. {p['n']}: {first_line(p['text'])}")
        return 0

    if args.heads:
        pm = a.get("pageMap", "")
        for p in pages or []:
            typ = pm[p["n"] - 1] if p["n"] - 1 < len(pm) else "?"
            print(f"{p['n']:4d} [{typ}] {p['chars']:5d}c  {first_line(p['text'])}")
        return 0

    print(f"{a['id']} — {a.get('title', '')}")
    print(f"arquivo: {a['file']} · {a['totalPages']} págs. · sumário até {a['tocMax']} · deslocamento impresso {a['printedOffset']}")
    print(f"teoria {a['theoryPages']} págs. em {a['theoryRuns']} · comentadas {a['commentedPages']} {a['commentedRuns']} · lista {a['listPages']}")
    if a.get("pageMap"):
        print("mapa:", runs(a["pageMap"]))
    if a["flags"]:
        print("alertas:", "; ".join(a["flags"]))
    print("\ntópicos (pág · nível · tipo · título):")
    for t in a["topics"]:
        tag = t["kind"] + ("/auto" if t.get("auto") else "") + ("/manual" if t.get("manual") else "") + ("/questão" if t.get("question") else "")
        print(f"  {t['pdfPage']:4d} · {t['level']} · {tag:15s} · {t['title'][:100]}{'' if t['verified'] else '  (não localizado)'}")
    print("\ntrechos:")
    for s in segs:
        mid = ("…" if s["startsMidTopic"] else "") + (" (corta no meio)" if s["endsMidTopic"] else "")
        print(f"  {s['id'].split('/')[-1]}  págs. {s['startPage']}–{s['endPage']} ({s['pages']} p., carga {s['load']})  "
              f"{mid} início: {s['startTopic']} | tópicos: {'; '.join(s['topicsCovered'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
