import json, unicodedata, re

def norm(s):
    return re.sub(r'[^a-z0-9]+', '', unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower())

data = json.load(open('pipeline/.cache/pages/26_001.json', encoding='utf-8'))
for pg in data['pages']:
    for line in pg['text'].split('\n')[:6]:
        n = norm(line)
        if 'questoe' in n or 'gabarito' in n or 'lista' in n:
            print(f"P{pg['n']}: {line} -> norm: {n}")
