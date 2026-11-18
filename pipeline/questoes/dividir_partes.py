"""Divide os lotes de comentários pendentes em partes equilibradas, uma por agente, sem lote em comum.

    pipeline/.venv/Scripts/python pipeline/questoes/dividir_partes.py [--partes 3] [--faixa P1] [--zerar]
    pipeline/.venv/Scripts/python pipeline/questoes/dividir_partes.py --status

Lê content/questoes/comentarios/_fila.json (gerada por web/scripts/questoes-fila-comentarios.ts) e grava
pipeline/.cache/questoes-comentar/_partes/parte-A.txt, parte-B.txt… (um pacote por linha, como nas ondas). Cada disciplina inteira
fica com uma parte sempre que possível (o agente lê o mesmo material e as mesmas leis); disciplina maior que a cota é dividida
por trecho. Lote já entregue (arquivo de saída existente) não entra. A divisão é estável: lote já atribuído a uma parte fica
nela, e só os lotes novos são distribuídos (use --zerar para refazer tudo).
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
PARTES = ROOT / "pipeline" / ".cache" / "questoes-comentar" / "_partes"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def pkg(lote_id: str) -> str:
    return f"pipeline/.cache/questoes-comentar/{lote_id.replace('/', '__')}.json"


def read_part(path: Path) -> list[str]:
    return [ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()] if path.exists() else []


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--partes", type=int, default=3)
    ap.add_argument("--faixa", default="P1")
    ap.add_argument("--zerar", action="store_true")
    ap.add_argument("--status", action="store_true")
    a = ap.parse_args()
    names = list(string.ascii_uppercase[: a.partes])
    fila = json.loads(FILA.read_text(encoding="utf-8"))
    lotes = [l for l in fila["lotes"] if l["faixa"] == a.faixa and not (ROOT / l["arquivo"]).exists()]
    by_pkg = {pkg(l["id"]): l for l in lotes}
    PARTES.mkdir(parents=True, exist_ok=True)

    if a.status:
        for n in names:
            ls = [by_pkg[p] for p in read_part(PARTES / f"parte-{n}.txt") if p in by_pkg]
            q = sum(len(l["questoes"]) for l in ls)
            print(f"parte-{n}: {len(ls)} lotes pendentes, {q} questões")
        sem = [l for l in lotes if not any(pkg(l['id']) in read_part(PARTES / f'parte-{n}.txt') for n in names)]
        print(f"sem parte: {len(sem)} lotes, {sum(len(l['questoes']) for l in sem)} questões")
        return 0

    parts: dict[str, list[str]] = {n: ([] if a.zerar else [p for p in read_part(PARTES / f"parte-{n}.txt") if p in by_pkg]) for n in names}
    assigned = {p for ps in parts.values() for p in ps}
    load = {n: sum(len(by_pkg[p]["questoes"]) for p in parts[n]) for n in names}
    free = [l for l in lotes if pkg(l["id"]) not in assigned]
    total = sum(load.values()) + sum(len(l["questoes"]) for l in free)
    quota = total / a.partes
    by_disc: dict[str, list[dict]] = defaultdict(list)
    for l in free:
        by_disc[l["disciplina"]].append(l)
    # disciplinas já atribuídas a uma parte voltam para ela (lotes novos da mesma disciplina)
    owner: dict[str, str] = {}
    for n in names:
        for p in parts[n]:
            owner.setdefault(by_pkg[p]["disciplina"], n)
    for disc, ls in sorted(by_disc.items(), key=lambda kv: -sum(len(l["questoes"]) for l in kv[1])):
        ls = sorted(ls, key=lambda l: l["trecho"])
        size = sum(len(l["questoes"]) for l in ls)
        n = owner.get(disc)
        if n is None or load[n] + size > quota * 1.15:
            n = min(names, key=lambda x: load[x])
        if load[n] + size <= quota * 1.15 or size <= quota * 0.5:
            for l in ls:
                parts[n].append(pkg(l["id"]))
            load[n] += size
            owner.setdefault(disc, n)
        else:  # disciplina grande: divide por trecho entre as partes mais vazias
            for l in ls:
                m = min(names, key=lambda x: load[x])
                parts[m].append(pkg(l["id"]))
                load[m] += len(l["questoes"])
    for n in names:
        (PARTES / f"parte-{n}.txt").write_text("\n".join(parts[n]) + "\n", encoding="utf-8")
        discs = sorted({by_pkg[p]["disciplina"] for p in parts[n]})
        print(f"parte-{n}: {len(parts[n])} lotes, {load[n]} questões · {', '.join(discs)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
