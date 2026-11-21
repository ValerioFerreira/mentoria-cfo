"""Acompanha as inéditas do balanço de 20/11/2026 (pipeline/briefs/ineditas-balanco-2026-11.md).

Base: pipeline/briefs/ineditas-balanco-base.json = por trecho, quantas questões já estavam em content/questoes/ineditas/mc/ em 20/11/2026 (`txt`)
e quantas devem ser escritas (`escrever`). O que passar de `txt` nos arquivos .txt conta como escrito.

    python pipeline/questoes/lacunas_balanco.py                  # resumo por matéria
    python pipeline/questoes/lacunas_balanco.py --lista atualidades   # trechos da matéria ainda abaixo da quota
    python pipeline/questoes/lacunas_balanco.py --check          # sai com 1 se ainda faltar
"""
import json, re, sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.stdout.reconfigure(encoding="utf-8")


def main() -> None:
    base = json.loads((ROOT / "pipeline/briefs/ineditas-balanco-base.json").read_text(encoding="utf-8"))
    now = Counter()
    for f in (ROOT / "content/questoes/ineditas/mc").glob("*.txt"):
        for m in re.finditer(r"^@@\s*(\S+)\s*\|", f.read_text(encoding="utf-8"), re.M):
            now[f"{f.stem}/{m.group(1)}"] += 1
    por = defaultdict(lambda: {"quota": 0, "feitas": 0, "pendentes": 0})
    falta = {}
    for seg, b in base.items():
        feitas = max(0, now[seg] - b["txt"])
        d = por[seg.split("/")[0]]
        d["quota"] += b["escrever"]
        d["feitas"] += min(feitas, b["escrever"])
        if feitas < b["escrever"]:
            d["pendentes"] += 1
            falta[seg] = (b["escrever"] - feitas, feitas, b["escrever"])
    if "--lista" in sys.argv:
        disc = sys.argv[sys.argv.index("--lista") + 1]
        for seg, (f, feitas, quota) in sorted(falta.items()):
            if seg.startswith(disc + "/"):
                print(f"{seg}: escritas {feitas} de {quota}, faltam {f}")
        print(f"{sum(f for s, (f, _, _) in falta.items() if s.startswith(disc + '/'))} questões pendentes em {disc}")
    else:
        for d, v in sorted(por.items(), key=lambda x: -(x[1]["quota"] - x[1]["feitas"])):
            print(f"{d}: {v['feitas']}/{v['quota']} escritas, {v['pendentes']} trechos pendentes")
        q = sum(v["quota"] for v in por.values())
        e = sum(v["feitas"] for v in por.values())
        print(f"TOTAL: {e}/{q} escritas, faltam {q - e}")
    sys.exit(1 if falta and "--check" in sys.argv else 0)


if __name__ == "__main__":
    main()
