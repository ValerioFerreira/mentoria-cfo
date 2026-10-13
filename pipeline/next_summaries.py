"""Mostra as próximas atividades de um lote (resumos-colaboradores/indice.json) que ainda não têm arquivo de entrega.

Uso:  python pipeline/next_summaries.py --lot 1 --agent CLAUDE-L1 [--n 6] [--json]
Considera "feito": status "Feito" no índice, resumo já importado (content/summaries) ou arquivo Sxxxx__AGENTE.md já gravado em
resumos-colaboradores/entregas/resumos_<AGENTE>_<sublote>/. A ordem é a do ID (prioridade). Só leitura.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from config import CONTENT_DIR, ROOT  # noqa: E402
from summary_queue import done_ids  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

COLAB = ROOT / "resumos-colaboradores"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lot", required=True)
    ap.add_argument("--agent", required=True)
    ap.add_argument("--n", type=int, default=6)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    rows = json.loads((COLAB / "indice.json").read_text(encoding="utf-8"))["rows"]
    imported = done_ids()
    delivered = {p.name.split("__")[0] for p in (COLAB / "entregas").rglob("S*__*.md")} if (COLAB / "entregas").exists() else set()
    todo = [r for r in rows if r["lot"] == args.lot and not r["done"]]
    pending = [r for r in todo if r["id"] not in delivered and r["trecho"] not in imported]
    pick = pending[: args.n]
    out = []
    for r in pick:
        out.append({**{k: r[k] for k in ("id", "trecho", "subjectName", "aulaLabel", "activity", "pdf", "startPage", "endPage", "pages", "targetWords", "sublot", "inCbmpe", "authored")},
                    "folder": f"resumos-colaboradores/entregas/resumos_{args.agent}_{r['sublot']}", "file": f"{r['id']}__{args.agent}.md"})
    if args.json:
        print(json.dumps({"lot": args.lot, "total": len(todo), "pending": len(pending), "next": out}, ensure_ascii=False, indent=1))
        return 0
    print(f"Lote {args.lot}: {len(todo)} atividades, {len(todo) - len(pending)} prontas, {len(pending)} pendentes. Próximas {len(out)}:")
    for o in out:
        print(f"- {o['id']} · {o['trecho']} · {o['subjectName']} · {o['aulaLabel']} · págs. {o['startPage']}–{o['endPage']} ({o['pages']}) · alvo {o['targetWords']} palavras")
        print(f"    assuntos: {o['activity']}")
        print(f"    gravar em: {o['folder']}/{o['file']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
