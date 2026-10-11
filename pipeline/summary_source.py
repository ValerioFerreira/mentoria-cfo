"""Imprime o texto-fonte de um trecho (para quem vai escrever o resumo). Só leitura.

Uso:  python pipeline/summary_source.py <disciplina>/aNN/sNN [--max-chars N] [--fingerprint]
  - aulas do material-base: páginas startPage–endPage do cache local (pipeline/.cache/pages)
  - complementos autorais (cNN): o .md em content/complements/ (o trecho cobre o complemento inteiro)
O texto é PROTEGIDO (marca d'água do aluno): leia, entenda e escreva com as SUAS palavras; nunca copie.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from config import CONTENT_DIR  # noqa: E402
from textutil import aula_key_map, load_pages  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def segment(seg_id: str) -> dict:
    subject = seg_id.split("/")[0]
    for s in json.loads((CONTENT_DIR / "segments" / f"{subject}.json").read_text(encoding="utf-8"))["segments"]:
        if s["id"] == seg_id:
            return s
    raise SystemExit(f"trecho inexistente: {seg_id}")


def authored_md(aula_id: str) -> str | None:
    cat = json.loads((CONTENT_DIR / "catalog.json").read_text(encoding="utf-8"))
    for s in cat["subjects"]:
        for a in s["aulas"]:
            if a["id"] == aula_id and a.get("source") == "authored":
                name = os.path.basename(a.get("materialPath", "")).rsplit(".", 1)[0]
                f = CONTENT_DIR / "complements" / f"{name}.md"
                return f.read_text(encoding="utf-8") if f.exists() else None
    return None


def source_text(seg_id: str) -> tuple[dict, str]:
    seg = segment(seg_id)
    md = authored_md(seg["aula"])
    if md is not None:
        return seg, md
    key = aula_key_map().get(seg["aula"])
    if not key:
        raise SystemExit(f"sem cache de texto para {seg['aula']}")
    pages = {p["n"]: p["text"] for p in load_pages(key)["pages"]}
    parts = []
    for n in range(seg["startPage"], seg["endPage"] + 1):
        parts.append(f"\n===== PÁGINA {n} =====\n{pages.get(n, '')}")
    return seg, "".join(parts)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("segment")
    ap.add_argument("--max-chars", type=int, default=0)
    ap.add_argument("--fingerprint", action="store_true", help="só imprime a impressão digital (JSON) do trecho")
    args = ap.parse_args()
    if args.fingerprint:
        seg = segment(args.segment)
        print(json.dumps({"startPage": seg["startPage"], "endPage": seg["endPage"], "startTopic": seg.get("startTopic")}, ensure_ascii=False))
        return
    seg, text = source_text(args.segment)
    text = re.sub(r"\n{3,}", "\n\n", text)
    head = (
        f"# {seg['id']} · págs. {seg['startPage']}–{seg['endPage']} ({seg['pages']} págs.) · {seg.get('minutes', 60)} min de teoria\n"
        f"# tópicos: {'; '.join(seg.get('topicsCovered', []))}\n"
    )
    print(head + (text[: args.max_chars] if args.max_chars else text))


if __name__ == "__main__":
    main()
