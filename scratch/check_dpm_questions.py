import json
from collections import defaultdict

with open('pipeline/.cache/material/questoes/direito-penal-militar__m03.json', encoding='utf-8') as f:
    d = json.load(f)

by_cap = defaultdict(list)
for q in d.get('questoes', []):
    by_cap[q['capitulo']].append(q)

for cap in sorted(by_cap.keys()):
    print(f"=== {cap} (total: {len(by_cap[cap])}) ===")
    for q in by_cap[cap]:
        fig = " [FIGURA]" if q.get('temFigura') else ""
        print(f"  {q['id']} | {q.get('banca')} | {q.get('ano')} | Gab: {q['gabarito']} | Alts: {len(q.get('alternativas', []))}{fig} | {q.get('enunciado', '')[:60].strip()}...")
