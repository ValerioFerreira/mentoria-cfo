import json
from pathlib import Path

f = Path("pipeline/.cache/material/questoes/estatistica__m07.json")
data = json.loads(f.read_text(encoding="utf-8"))["questoes"]

from collections import defaultdict
by_cap = defaultdict(list)
for q in data:
    by_cap[q["capitulo"]].append(q)

for cap, qs in sorted(by_cap.items()):
    print("=" * 60)
    print(f"CAPITULO: {cap} ({len(qs)} questões)")
    for q in qs:
        print(f"  ID: {q['id']} | BANCA: {q['banca']} | GAB: {q.get('gabarito')} | TIPO: {q.get('tipo')} | FIG: {q.get('temFigura')}")
        print(f"    Enunciado: {q['enunciado'][:120]}...")
