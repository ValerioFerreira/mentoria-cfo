import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

data = json.load(open('pipeline/.cache/preliminary_bizu_flaws.json', encoding='utf-8'))
items = data.get('inicia_com_minuscula', [])
print(f"Total: {len(items)}")
for it in items:
    print(f"[{it['id']}] {it['statement']}")
