import json

with open('pipeline/.cache/material/questoes/direito-penal-militar__m05.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for cap in sorted(data['porCapitulo'].keys()):
    qs = [q for q in data['questoes'] if q['capitulo'] == cap]
    print(f'=== {cap} ({len(qs)} qs) ===')
    for q in qs[:5]:
        alts = [a['letra'] for a in q.get('alternativas', [])]
        print(f"  ID: {q['id']} | Banca: {q.get('banca')} | Tipo: {q.get('tipo')} | Gab: {q.get('gabarito')} | Alts: {alts}")
