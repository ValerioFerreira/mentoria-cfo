import json, subprocess
raw = subprocess.check_output(['git', 'show', '314cba6:content/catalog.json'], encoding='utf-8')
cat = json.loads(raw)
for s in cat['subjects']:
    tot = sum(a['incidence'] for a in s['aulas'])
    if tot > 1.0001:
        print(f"{s['id']}: {tot}")
