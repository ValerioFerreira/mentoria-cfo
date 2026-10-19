"""Mostra o sintético (Bizu) dos trechos: base factual curta para escrever questões inéditas.
Uso: python pipeline/pcpe_tools/seg_bizu.py <trecho> [...]"""
import json, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
C = Path(__file__).resolve().parents[2] / "content" / "summaries"
for sid in sys.argv[1:]:
    disc, aula, _ = sid.split("/")
    doc = json.loads((C / disc / f"{aula}.json").read_text(encoding="utf-8"))
    for s in doc["segments"]:
        if s["id"] == sid:
            print(f"##### {sid}")
            for x in s["synthetic"]:
                print("-", x)
            print()
