import json

with open('pipeline/.cache/material/questoes/biologia__m02.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Total questoes:", len(data['questoes']))
by_cap = {}
for q in data['questoes']:
    by_cap.setdefault(q['capitulo'], []).append(q)

for cap, qs in by_cap.items():
    print(f"\nCap: {cap} ({len(qs)} questoes)")
    for q in qs:
        print(f"  [{q['id']}] {q['banca']} {q['ano']} - {q.get('orgao','')} / {q.get('cargo','')} - Gab: {q['gabarito']} - Fig: {q.get('temFigura')}")
