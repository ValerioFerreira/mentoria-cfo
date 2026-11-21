import json

data = json.load(open('pipeline/.cache/material/questoes/estatistica__m03.json', encoding='utf-8'))
qs = data['questoes']

for q in qs:
    c = q['capitulo']
    qid = q['id']
    b = q.get('banca')
    y = q.get('ano')
    g = q.get('gabarito')
    fig = q.get('temFigura')
    print(f"[{c}] {qid} - {b} ({y}) - gab: {g} - fig: {fig}")
