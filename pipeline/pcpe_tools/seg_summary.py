"""Mostra o resumo analítico (e o sintético) dos trechos pedidos: base factual para escrever questões inéditas.
Uso: python pipeline/pcpe_tools/seg_summary.py <trecho> [<trecho> ...]"""
import json, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
C = Path(__file__).resolve().parents[2] / "content" / "summaries"
for sid in sys.argv[1:]:
    disc, aula, _ = sid.split("/")
    doc = json.loads((C / disc / f"{aula}.json").read_text(encoding="utf-8"))
    for s in doc["segments"]:
        if s["id"] == sid:
            print(f"##### {sid}\n{s['analytic']}\n")
