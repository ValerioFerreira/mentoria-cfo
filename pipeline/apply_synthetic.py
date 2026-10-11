"""Aplica os resumos sintéticos (content/summaries) ao Bizu dos trechos (content/items/<disc>/<aula>.json) e espelha o
conteúdo novo (resumos, importância, concursos) em web/content, que é o que o build de produção lê.

O resumo sintético SUBSTITUI o `bizu.summary` anterior (os itens Certo/Errado ficam como estão). Idempotente.
Uso: python pipeline/apply_synthetic.py [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(__file__))
from config import CONTENT_DIR, ROOT  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WEB_CONTENT = ROOT / "web" / "content"
LIST_START = re.compile(r"^\s*(-|\*|\d+[.)]|#|>|\|)")


def bullet(line: str) -> str:
    line = line.strip()
    return line if LIST_START.match(line) else f"- {line}"


def dump(path, doc) -> None:
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    applied = missing = 0
    for f in sorted((CONTENT_DIR / "summaries").glob("*/*.json")):
        doc = json.loads(f.read_text(encoding="utf-8"))
        synth = {s["id"]: [bullet(x) for x in s["synthetic"]] for s in doc.get("segments", []) if s.get("synthetic")}
        if not synth:
            continue
        for base in (CONTENT_DIR, WEB_CONTENT):
            target = base / "items" / f.parent.name / f.name
            if not target.exists():
                if base == CONTENT_DIR:
                    missing += len(synth)
                continue
            items = json.loads(target.read_text(encoding="utf-8"))
            changed = False
            for seg in items.get("segments", []):
                if seg["id"] in synth and seg.get("bizu"):
                    if seg["bizu"].get("summary") != synth[seg["id"]]:
                        seg["bizu"]["summary"] = synth[seg["id"]]
                        changed = True
                    if base == CONTENT_DIR:
                        applied += 1
            if changed and not args.dry_run:
                dump(target, items)
    print(f"sintéticos aplicados ao Bizu: {applied} trechos ({missing} sem arquivo de itens)")

    if args.dry_run:
        return
    # espelho para o build (web/content)
    for sub in ("summaries", "importance"):
        src, dst = CONTENT_DIR / sub, WEB_CONTENT / sub
        if not src.exists():
            continue
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns("_queue.json"))
    shutil.copy2(CONTENT_DIR / "contests.json", WEB_CONTENT / "contests.json")
    print("espelhado em web/content: summaries/, importance/, contests.json")


if __name__ == "__main__":
    main()
