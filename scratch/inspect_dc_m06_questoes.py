import json

with open('pipeline/.cache/material/questoes/direito-constitucional__m06.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for cap, count in data['porCapitulo'].items():
    print(f"Cap: {cap} -> {count}")

questoes_por_cap = {}
for q in data['questoes']:
    cap = q['capitulo']
    questoes_por_cap.setdefault(cap, []).append(q)

for cap, qs in questoes_por_cap.items():
    print(f"\nCapitulo: {cap} (Total: {len(qs)})")
    for q in qs:
        print(f"  [{q['id']}] {q['banca']} {q['ano']} - {q['orgao']} / {q['cargo']} - Gab: {q['gabarito']} - Fig: {q['temFigura']}")
