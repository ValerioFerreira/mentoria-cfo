import json

data = json.load(open('pipeline/.cache/pages/26_001.json', encoding='utf-8'))
for p in data['pages'][2:17]:
    print(f"=== Page {p['n']} ===")
    for l in [ln.strip() for ln in p['text'].split('\n') if ln.strip()][:5]:
        print('  ', l[:80])
