import json

cat = json.load(open('content/catalog.json', encoding='utf-8'))
for s in cat['subjects']:
    tot = sum(a['incidence'] for a in s['aulas'])
    print(f"{s['id']:32s}: {tot:.5f}")
