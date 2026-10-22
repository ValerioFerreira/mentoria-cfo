"""Trechos do CBMPE Oficial que ainda ficam abaixo de 7 questões servíveis no caderno, contando as inéditas novas.

Base: pipeline/briefs/ineditas-cbmpe-base.json = por trecho, as questões efetivas na produção em 21/10/2026 (AOCP + reforço:
múltipla escolha de outras bancas e inéditas já gravadas) e quantas questões de content/questoes/ineditas/mc/ já estavam
escritas naquele dia. O que passar disso nos arquivos .txt conta como novo.

    python pipeline/questoes/lacunas_cbmpe.py                  # resumo por disciplina
    python pipeline/questoes/lacunas_cbmpe.py --lista quimica  # trechos ainda abaixo do mínimo da disciplina
    python pipeline/questoes/lacunas_cbmpe.py --check          # sai com 1 se ainda faltar
"""
import json, re, sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.stdout.reconfigure(encoding="utf-8")
MIN = 7


def main() -> None:
    base = json.loads((ROOT / "pipeline/briefs/ineditas-cbmpe-base.json").read_text(encoding="utf-8"))
    now = Counter()
    for f in (ROOT / "content/questoes/ineditas/mc").glob("*.txt"):
        for m in re.finditer(r"^@@\s*(\S+)\s*\|", f.read_text(encoding="utf-8"), re.M):
            now[f"{f.stem}/{m.group(1)}"] += 1
    falta = {}
    for seg, b in base.items():
        atual = b["efetiva"] + max(0, now[seg] - b["txt"])
        if atual < MIN:
            falta[seg] = (MIN - atual, atual)
    por = defaultdict(lambda: [0, 0])
    for seg, (f, _) in falta.items():
        d = por[seg.split("/")[0]]
        d[0] += 1
        d[1] += f
    if "--lista" in sys.argv:
        disc = sys.argv[sys.argv.index("--lista") + 1]
        for seg, (f, a) in sorted(falta.items()):
            if seg.startswith(disc + "/"):
                print(f"{seg}: tem {a}, faltam {f}")
    else:
        for d, (n, q) in sorted(por.items(), key=lambda x: -x[1][1]):
            print(f"{d}: {n} trechos abaixo de {MIN}, faltam {q} questões")
        print(f"TOTAL: {sum(v[0] for v in por.values())} trechos, faltam {sum(v[1] for v in por.values())} questões")
    sys.exit(1 if falta and "--check" in sys.argv else 0)


if __name__ == "__main__":
    main()
