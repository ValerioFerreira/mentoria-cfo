"""Trechos do PCPE com poucas questões servíveis (Cebraspe + AOCP + inéditas) e quanto falta para o mínimo.

Base fixa: pipeline/briefs/ineditas-base-segcounts.json (aprovadas por trecho e banca na produção em 2026-10-20, ANTES das
inéditas de múltipla escolha nativas). A conta "atual" soma a base com as questões de content/questoes/ineditas/mc/*.txt, de modo
que o resultado não depende de gravar nada no banco.

Mínimo por trecho: 6 questões (8 nos trechos de peso_prova >= 0,20). O caderno da atividade junta até 4 trechos; abre com 5 ou mais.

    python pipeline/questoes/lacunas_pcpe.py            # imprime o resumo e regrava pipeline/briefs/ineditas-fracos.csv
    python pipeline/questoes/lacunas_pcpe.py --check    # só confere; sai com código 1 se ainda faltar
"""
import csv, json, re, sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.stdout.reconfigure(encoding="utf-8")
BASE = ROOT / "pipeline/briefs/ineditas-base-segcounts.json"
OUT = ROOT / "pipeline/briefs/ineditas-fracos.csv"
MIN, MIN_ALTO, PESO_ALTO = 6, 8, 0.20


def servivel(b: str) -> bool:
    u = b.upper()
    return "CEBRASPE" in u or "CESPE" in u or "AOCP" in u or b == "Inédita MentorIA"


def main() -> None:
    check = "--check" in sys.argv
    atual = Counter()
    for r in json.loads(BASE.read_text(encoding="utf-8")):
        if servivel(r["banca"]):
            atual[r["seg"]] += r["n"]
    for f in (ROOT / "content/questoes/ineditas/mc").glob("*.txt"):
        for m in re.finditer(r"^@@\s*(\S+)\s*\|", f.read_text(encoding="utf-8"), re.M):
            atual[f"{f.stem}/{m.group(1)}"] += 1
    imp = json.loads((ROOT / "content/importance/segments.json").read_text(encoding="utf-8"))["segments"]
    cat = json.loads((ROOT / "content/catalog.json").read_text(encoding="utf-8"))
    aulas = {a["id"]: a["title"] for s in cat["subjects"] for a in s["aulas"]}
    segs = {}
    for f in (ROOT / "content/segments").glob("*.json"):
        for g in json.loads(f.read_text(encoding="utf-8"))["segments"]:
            segs[g["id"]] = g
    rows = []
    for k, v in imp.items():
        c = v["contests"].get("PCPE_AGENTE")
        if not c or not c["appears"] or k not in segs:
            continue
        alvo = MIN_ALTO if c["expected"] >= PESO_ALTO else MIN
        falta = max(0, alvo - atual[k])
        if falta:
            g = segs[k]
            rows.append([k.split("/")[0], k, aulas.get("/".join(k.split("/")[:2]), "")[:70], f"{g['startPage']}-{g['endPage']}",
                         " ; ".join(t[:60] for t in g.get("topicsCovered", [])[:6]), round(c["expected"], 3), atual[k], alvo, falta])
    rows.sort(key=lambda r: (r[0], r[1]))
    por = defaultdict(lambda: [0, 0])
    for r in rows:
        por[r[0]][0] += 1; por[r[0]][1] += r[8]
    for d, (n, q) in sorted(por.items(), key=lambda x: -x[1][1]):
        print(f"{d}: {n} trechos abaixo do mínimo, faltam {q} questões")
    print(f"TOTAL: {len(rows)} trechos, faltam {sum(r[8] for r in rows)} questões de múltipla escolha")
    if not check:
        with open(OUT, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow(["disciplina", "trecho", "aula", "paginas", "topicos", "peso_prova", "atuais", "alvo", "faltam"])
            w.writerows(rows)
        print("->", OUT)
    sys.exit(1 if (check and rows) else 0)


if __name__ == "__main__":
    main()
