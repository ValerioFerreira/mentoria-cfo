"""Aplica a classificação dos agentes (pacotes_rascunhos.py) em content/questoes/overrides-questoes.json.

    pipeline/.venv/Scripts/python pipeline/questoes/aplicar_agentes.py [DIR_DO_LOTE]

Regras: classificar com confiança alta/média vira trecho fixo; skip com confiança alta/média vira skip;
confiança baixa não vira decisão (a questão continua rascunho para /admin/revisao). Decisões já existentes
no arquivo não são sobrescritas.
"""
from __future__ import annotations

import glob
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OV = ROOT / "content" / "questoes" / "overrides-questoes.json"
sys.stdout.reconfigure(encoding="utf-8")


def main() -> None:
    d = Path(sys.argv[1]) if len(sys.argv) > 1 else sorted((ROOT / "docs/questoes/classificacao-agentes").glob("*"))[-1]
    segs = {s["id"] for f in glob.glob(str(ROOT / "content/segments/*.json")) for s in json.loads(Path(f).read_text(encoding="utf-8"))["segments"]}
    data = json.loads(OV.read_text(encoding="utf-8"))
    ov = data["questoes"]
    c: Counter = Counter()
    for f in sorted((d / "resultados").glob("*.jsonl")):
        for ln in f.read_text(encoding="utf-8").splitlines():
            if not ln.strip():
                continue
            r = json.loads(ln)
            t = str(r["tecId"])
            if t in ov:
                c["já decidida"] += 1
                continue
            if r["confianca"] == "baixa":
                c["baixa (continua rascunho)"] += 1
            elif r["acao"] == "skip":
                ov[t] = {"skip": f"sem trecho que ensine / fora do edital (classificação por agente, {d.name}): {r.get('motivo', '')[:120]}"}
                c["skip"] += 1
            elif r.get("segment") in segs:
                ov[t] = {"segment": r["segment"]}
                c["trecho"] += 1
            else:
                c["trecho inválido"] += 1
    OV.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(dict(c), "| total de decisões:", len(ov))


if __name__ == "__main__":
    main()
