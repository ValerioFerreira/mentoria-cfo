import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('audit_exatas_all_items.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for target_aula in sorted(list(set(it['aula'] for it in items if it['disciplina'] == 'fisica'))):
    cur = [it for it in items if it['disciplina'] == 'fisica' and it['aula'] == target_aula]
    print(f"\n==================== FÍSICA {target_aula} ({len(cur)} items) ====================")
    for it in cur:
        ans = 'C' if it['isTrue'] else 'E'
        print(f"[{ans}] {it['id']}")
        print(f"     ST : {it['statement']}")
        print(f"     EXP: {it['explanation']}")
