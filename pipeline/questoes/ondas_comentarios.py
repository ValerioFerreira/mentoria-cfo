"""Monta as ondas de trabalho dos agentes que comentam as questões (ver pipeline/briefs/questoes-comentarios.md).

    pipeline/.venv/Scripts/python pipeline/questoes/ondas_comentarios.py --status [--faixa P1]
    pipeline/.venv/Scripts/python pipeline/questoes/ondas_comentarios.py --onda 02 --agentes 5 --por-agente 90 [--faixa P1]
    pipeline/.venv/Scripts/python pipeline/questoes/ondas_comentarios.py --conferir 01      # o que cada agente da onda entregou

Lê a fila (content/questoes/comentarios/_fila.json, gerada por web/scripts/questoes-fila-comentarios.ts) e pega, na ordem
da fila, os próximos lotes que ainda não têm arquivo de saída nem estão numa onda anterior sem entrega. Agrupa por
disciplina (cada agente fica com uma ou poucas disciplinas) e grava pipeline/.cache/questoes-comentar/_ondas/onda-NN-<X>.txt
(um pacote por linha).
"""
from __future__ import annotations

import argparse
import json
import string
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FILA = ROOT / "content" / "questoes" / "comentarios" / "_fila.json"
CACHE = ROOT / "pipeline" / ".cache" / "questoes-comentar"
ONDAS = CACHE / "_ondas"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def pkg_path(lote_id: str) -> str:
    return f"pipeline/.cache/questoes-comentar/{lote_id.replace('/', '__')}.json"


def assigned() -> dict[str, str]:
    """pacote -> onda em que foi atribuído."""
    out: dict[str, str] = {}
    for f in sorted(ONDAS.glob("onda-*.txt")):
        for ln in f.read_text(encoding="utf-8").splitlines():
            if ln.strip():
                out[ln.strip()] = f.stem
    return out


def delivered(lote: dict) -> bool:
    return (ROOT / lote["arquivo"]).exists()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--faixa", default="P1")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--onda")
    ap.add_argument("--agentes", type=int, default=5)
    ap.add_argument("--por-agente", type=int, default=90, help="questões por agente (lotes inteiros)")
    ap.add_argument("--conferir")
    a = ap.parse_args()
    fila = json.loads(FILA.read_text(encoding="utf-8"))
    lotes = [l for l in fila["lotes"] if a.faixa == "todas" or l["faixa"] == a.faixa]
    asg = assigned()

    if a.conferir:
        for f in sorted(ONDAS.glob(f"onda-{a.conferir}-*.txt")):
            pk = [ln.strip() for ln in f.read_text(encoding="utf-8").splitlines() if ln.strip()]
            by_pkg = {pkg_path(l["id"]): l for l in fila["lotes"]}
            done = [p for p in pk if p in by_pkg and delivered(by_pkg[p])]
            miss = [p for p in pk if p not in done]
            print(f"{f.stem}: {len(done)}/{len(pk)} entregues" + (f" · faltam: {', '.join(Path(m).stem for m in miss)}" if miss else ""))
        return 0

    done = [l for l in lotes if delivered(l)]
    pend = [l for l in lotes if not delivered(l)]
    if a.status or not a.onda:
        nq = lambda ls: sum(len(l["questoes"]) for l in ls)  # noqa: E731
        print(f"faixa {a.faixa}: {len(lotes)} lotes / {nq(lotes)} questões · entregues {len(done)} / {nq(done)} · pendentes {len(pend)} / {nq(pend)}")
        em_onda = [l for l in pend if pkg_path(l["id"]) in asg]
        print(f"pendentes já atribuídos a uma onda (sem entrega): {len(em_onda)} / {nq(em_onda)}")
        return 0

    free = [l for l in pend if pkg_path(l["id"]) not in asg]
    cap = a.agentes * a.por_agente
    chosen: list[dict] = []
    total = 0
    for l in free:
        if total >= cap:
            break
        chosen.append(l)
        total += len(l["questoes"])
    if not chosen:
        print("nada a atribuir")
        return 0
    by_disc: dict[str, list[dict]] = defaultdict(list)
    for l in chosen:
        by_disc[l["disciplina"]].append(l)
    bins: list[list[dict]] = [[] for _ in range(a.agentes)]
    load = [0] * a.agentes
    # disciplinas maiores primeiro; uma disciplina maior que a cota se divide entre agentes, em ordem de trecho
    for disc, ls in sorted(by_disc.items(), key=lambda kv: -sum(len(l["questoes"]) for l in kv[1])):
        ls = sorted(ls, key=lambda l: l["trecho"])
        size = sum(len(l["questoes"]) for l in ls)
        if size <= a.por_agente * 1.15:
            i = load.index(min(load))
            bins[i] += ls
            load[i] += size
            continue
        for l in ls:
            i = load.index(min(load))
            bins[i].append(l)
            load[i] += len(l["questoes"])
    ONDAS.mkdir(parents=True, exist_ok=True)
    for i, b in enumerate(bins):
        if not b:
            continue
        name = ONDAS / f"onda-{a.onda}-{string.ascii_uppercase[i]}.txt"
        name.write_text("\n".join(pkg_path(l["id"]) for l in b) + "\n", encoding="utf-8")
        discs = sorted({l["disciplina"] for l in b})
        print(f"{name.stem}: {len(b)} lotes, {sum(len(l['questoes']) for l in b)} questões · {', '.join(discs)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
