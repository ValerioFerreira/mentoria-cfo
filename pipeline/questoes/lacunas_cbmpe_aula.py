"""Aulas do CBMPE Oficial cujo PRIMEIRO caderno (até 4 primeiros trechos) ainda fica abaixo de 25 questões servíveis.

Base: pipeline/briefs/ineditas-cbmpe2-base.json = por trecho, as questões efetivas na produção (AOCP + reforço, já com as 1.771
inéditas de 21/10) e quantas questões de content/questoes/ineditas/mc/ existiam naquele momento. O que passar disso nos .txt é novo.

    python pipeline/questoes/lacunas_cbmpe_aula.py                    # resumo por disciplina
    python pipeline/questoes/lacunas_cbmpe_aula.py --lista quimica    # aulas ainda abaixo de 25 na disciplina (com o que cada trecho tem)
    python pipeline/questoes/lacunas_cbmpe_aula.py --check            # sai com 1 se ainda faltar
"""
import json, re, sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.stdout.reconfigure(encoding="utf-8")
ALVO = 25


def main() -> None:
    b = json.loads((ROOT / "pipeline/briefs/ineditas-cbmpe2-base.json").read_text(encoding="utf-8"))
    now = Counter()
    for f in (ROOT / "content/questoes/ineditas/mc").glob("*.txt"):
        for m in re.finditer(r"^@@\s*(\S+)\s*\|", f.read_text(encoding="utf-8"), re.M):
            now[f"{f.stem}/{m.group(1)}"] += 1
    falta = {}
    for aula, trechos in b["grupos"].items():
        tem = {t: b["segs"][t]["efetiva"] + max(0, now[t] - b["segs"][t]["txt"]) for t in trechos}
        if sum(tem.values()) < ALVO:
            falta[aula] = (ALVO - sum(tem.values()), tem)
    por = defaultdict(lambda: [0, 0])
    for a, (f, _) in falta.items():
        por[a.split("/")[0]][0] += 1
        por[a.split("/")[0]][1] += f
    if "--lista" in sys.argv:
        disc = sys.argv[sys.argv.index("--lista") + 1]
        for a, (f, tem) in sorted(falta.items()):
            if a.startswith(disc + "/"):
                print(f"{a}: faltam {f} para 25 | " + ", ".join(f"{t.split('/', 2)[2]}={n}" for t, n in tem.items()))
    else:
        for d, (n, q) in sorted(por.items(), key=lambda x: -x[1][1]):
            print(f"{d}: {n} aulas abaixo de {ALVO}, faltam {q} questões")
        print(f"TOTAL: {sum(v[0] for v in por.values())} aulas, faltam {sum(v[1] for v in por.values())} questões")
    sys.exit(1 if falta and "--check" in sys.argv else 0)


if __name__ == "__main__":
    main()
