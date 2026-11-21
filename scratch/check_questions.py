import json
from collections import defaultdict

with open('pipeline/.cache/material/questoes/biologia__m01.json', encoding='utf-8') as f:
    d = json.load(f)

by_cap = defaultdict(list)
for q in d.get('questoes', []):
    if not q.get('temFigura'):
        by_cap[q['capitulo']].append(q)

for cap in sorted(by_cap.keys()):
    print(f"=== {cap} (total sem figura: {len(by_cap[cap])}) ===")
    for q in by_cap[cap]:
        print(f"  {q['id']} | {q.get('banca')} | {q.get('ano')} | Gab: {q['gabarito']} | Alts: {len(q.get('alternativas', []))} | {q.get('enunciado', '')[:60].strip()}...")
