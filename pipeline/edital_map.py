"""Mapa edital → material: completa content/edital/<disciplina>.json com os trechos (ids) de cada localização e resume a cobertura.

Cada item do edital (auditado à mão, aula por aula) aponta aula + páginas do PDF; aqui as páginas viram ids de trecho
(content/segments), para que o site e o banco de questões saibam onde cada item é estudado e praticado.
Também confere se as aulas citadas existem e se o item tem bizu/questões nos trechos (quando já houver itens).

Uso: python pipeline/edital_map.py [--subject <disc>] [--check]   (--check: só confere, não reescreve)
Saída: pipeline/.cache/reports/edital_map.md
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from config import CACHE_DIR, CONTENT_DIR  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

EDITAL_DIR = CONTENT_DIR / "edital"
STATUSES = ("covered", "partial", "complement", "elsewhere", "gap")


def page_range(spec) -> tuple[int, int] | None:
    if spec in (None, ""):
        return None
    a, _, b = str(spec).replace("–", "-").partition("-")
    try:
        lo = int(a)
        return lo, int(b or a)
    except ValueError:
        return None


def all_segments() -> dict[str, list[dict]]:
    by_aula: dict[str, list[dict]] = collections.defaultdict(list)
    for f in (CONTENT_DIR / "segments").glob("*.json"):
        for s in json.loads(f.read_text(encoding="utf-8"))["segments"]:
            by_aula[s["aula"]].append(s)
    return by_aula


def items_by_segment() -> dict[str, dict]:
    out = {}
    for f in (CONTENT_DIR / "items").glob("*/*.json"):
        for seg in json.loads(f.read_text(encoding="utf-8")).get("segments", []):
            out[seg["id"]] = seg
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--subject")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    segs = all_segments()
    items = items_by_segment()
    catalog = json.loads((CONTENT_DIR / "catalog.json").read_text(encoding="utf-8"))
    aulas = {a["id"]: a for s in catalog["subjects"] for a in s["aulas"]}

    report = ["# Mapa edital → material", "", "| Disciplina | Itens | coberto | parcial | complemento | outra disciplina | lacuna | com prática |", "|---|---:|---:|---:|---:|---:|---:|---:|"]
    problems: list[str] = []
    totals = collections.Counter()
    for f in sorted(EDITAL_DIR.glob("*.json")):
        if args.subject and f.stem != args.subject:
            continue
        doc = json.loads(f.read_text(encoding="utf-8"))
        c = collections.Counter()
        practiced = 0
        for it in doc.get("items", []):
            st = it.get("status")
            if st not in STATUSES:
                problems.append(f"{f.stem} {it.get('id')}: status inválido {st!r}")
            c[st] += 1
            seg_ids: list[str] = []
            for w in it.get("where", []):
                aula = w.get("aula")
                if aula not in aulas:
                    problems.append(f"{f.stem} {it.get('id')}: aula inexistente {aula!r}")
                    continue
                rng = page_range(w.get("pages"))
                cand = segs.get(aula, [])
                if rng:
                    lo, hi = rng
                    hit = [s["id"] for s in cand if s["startPage"] <= hi and s["endPage"] >= lo]
                else:
                    hit = [s["id"] for s in cand]
                w["segments"] = hit
                if not hit and st in ("covered", "partial", "complement") and w.get("pages"):
                    problems.append(f"{f.stem} {it.get('id')}: págs. {w.get('pages')} de {aula} não caem em trecho de teoria")
                seg_ids += hit
            if st in ("covered", "partial", "complement") and not it.get("where"):
                problems.append(f"{f.stem} {it.get('id')}: status {st} sem localização")
            if any(items.get(s, {}).get("questions") for s in seg_ids):
                practiced += 1
        for k, v in c.items():
            totals[k] += v
        totals["items"] += sum(c.values())
        totals["practiced"] += practiced
        report.append(f"| {f.stem} | {sum(c.values())} | {c['covered']} | {c['partial']} | {c['complement']} | {c['elsewhere']} | {c['gap']} | {practiced} |")
        if not args.check:
            f.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    report.append(f"| **TOTAL** | {totals['items']} | {totals['covered']} | {totals['partial']} | {totals['complement']} | {totals['elsewhere']} | {totals['gap']} | {totals['practiced']} |")
    report += ["", f"Problemas: {len(problems)}"] + [f"- {p}" for p in problems]
    (CACHE_DIR / "reports").mkdir(parents=True, exist_ok=True)
    (CACHE_DIR / "reports" / "edital_map.md").write_text("\n".join(report), encoding="utf-8")
    print("\n".join(report))
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
