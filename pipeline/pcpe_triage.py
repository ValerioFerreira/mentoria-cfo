"""Triagem de qualidade dos resumos/bizus de um concurso (padrão: PCPE_AGENTE). Só leitura.

Para cada trecho com `appears=true` no concurso, aponta:
  - acento     : taxa de letras acentuadas por 1000 caracteres do analítico (< 12 = texto sem acento)
  - novos      : números de lei/artigo/súmula/tema que o resumo cita e o texto-fonte NÃO traz (possível invenção ou dado de fora)
  - omitidos   : números citados 2+ vezes no texto-fonte que nenhum texto produzido (resumo, sintético, bizu) menciona
  - palavras   : tamanho do analítico

Uso:  python pipeline/pcpe_triage.py [--contest PCPE_AGENTE] [--subject d] [--csv saida.csv] [--only-flagged]
"""
from __future__ import annotations

import argparse
import collections
import csv
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from config import CONTENT_DIR  # noqa: E402
from summary_source import source_text  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ACC = set("ãçáéíóúâêôõàÃÇÁÉÍÓÚ")
NUM = re.compile(r"(?<![\w.])(\d{1,3}(?:\.\d{3})+|\d{2,4}-[A-Z]|\d{3,4})(?:/(\d{2,4}))?(?![\w])")


def num_tokens(text: str) -> collections.Counter:
    c: collections.Counter = collections.Counter()
    for m in NUM.finditer(text):
        base = m.group(1).replace(".", "")
        if re.fullmatch(r"(19|20)\d\d", base) and not m.group(2):
            continue  # ano solto
        c[base] += 1
    return c


def produced_text(seg_id: str) -> tuple[str, str, str]:
    disc, aula, _ = seg_id.split("/")
    analytic = synth = bizu = ""
    f = CONTENT_DIR / "summaries" / disc / f"{aula}.json"
    if f.exists():
        for s in json.loads(f.read_text(encoding="utf-8"))["segments"]:
            if s["id"] == seg_id:
                analytic = s.get("analytic", "")
                synth = "\n".join(s.get("synthetic", []))
    f = CONTENT_DIR / "items" / disc / f"{aula}.json"
    if f.exists():
        for s in json.loads(f.read_text(encoding="utf-8"))["segments"]:
            if s["id"] == seg_id:
                b = s.get("bizu") or {}
                parts = list(b.get("summary", []))
                for k in ("teoria", "revisao"):
                    for i in b.get(k, []):
                        parts += [i.get("statement", ""), i.get("explanation", "")]
                bizu = "\n".join(parts)
    return analytic, synth, bizu


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--contest", default="PCPE_AGENTE")
    ap.add_argument("--subject")
    ap.add_argument("--csv")
    ap.add_argument("--only-flagged", action="store_true")
    args = ap.parse_args()
    imp = json.loads((CONTENT_DIR / "importance" / "segments.json").read_text(encoding="utf-8"))["segments"]
    ids = [k for k, v in imp.items() if v["contests"].get(args.contest, {}).get("appears")]
    if args.subject:
        ids = [i for i in ids if i.startswith(args.subject + "/")]
    rows = []
    for sid in ids:
        analytic, synth, bizu = produced_text(sid)
        try:
            _, src = source_text(sid)
        except SystemExit:
            continue
        rate = 1000 * sum(1 for c in analytic if c in ACC) / max(len(analytic), 1)
        src_n = num_tokens(src)
        out_n = num_tokens(analytic + "\n" + synth + "\n" + bizu)
        novos = sorted(k for k in out_n if k not in src_n)
        omit = sorted((k for k, n in src_n.items() if n >= 2 and k not in out_n), key=lambda k: -src_n[k])
        rows.append(
            dict(trecho=sid, palavras=len(analytic.split()), acento=round(rate, 1), novos=" ".join(novos), omitidos=" ".join(omit[:12]), n_novos=len(novos), n_omit=len(omit))
        )
    if args.csv:
        with open(args.csv, "w", newline="", encoding="utf-8-sig") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter=";")
            w.writeheader()
            w.writerows(rows)
    by = collections.defaultdict(list)
    for r in rows:
        by[r["trecho"].split("/")[0]].append(r)
    for d, rs in sorted(by.items()):
        sem = sum(1 for r in rs if r["acento"] < 12)
        nv = sum(1 for r in rs if r["n_novos"] >= 2)
        om = sum(1 for r in rs if r["n_omit"] >= 3)
        print(f"{d:28} trechos={len(rs):3} sem-acento={sem:3} novos>=2={nv:3} omitidos>=3={om:3}")
    if not args.only_flagged:
        return
    for r in rows:
        if r["acento"] < 12 or r["n_novos"] >= 2 or r["n_omit"] >= 3:
            print(r["trecho"], r["acento"], "novos:", r["novos"], "| omit:", r["omitidos"])


if __name__ == "__main__":
    main()
