import json

data = json.load(open('pipeline/.cache/material/questoes/direito-constitucional__m14.json', encoding='utf-8'))
qs = data['questoes']

print(f"Total: {len(qs)}")
aocp = [q for q in qs if 'aocp' in q.get('banca', '').lower()]
print(f"Total AOCP: {len(aocp)}")

for q in qs:
    c = q['capitulo']
    qid = q['id']
    b = q.get('banca')
    y = q.get('ano')
    g = q.get('gabarito')
    fig = q.get('temFigura')
    print(f"[{c}] {qid} - {b} ({y}) - gab: {g} - fig: {fig}")
