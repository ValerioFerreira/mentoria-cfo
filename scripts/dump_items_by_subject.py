import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('audit_exatas_all_items.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for d in ['matematica', 'raciocinio-logico', 'estatistica', 'fisica']:
    sub_items = [it for it in items if it['disciplina'] == d]
    with open(f'items_{d}.txt', 'w', encoding='utf-8') as out:
        for it in sub_items:
            ans = 'C' if it['isTrue'] else 'E'
            out.write(f"ID: {it['id']}\n")
            out.write(f"GABARITO: {ans}\n")
            out.write(f"STATEMENT: {it['statement']}\n")
            out.write(f"EXPLANATION: {it['explanation']}\n")
            out.write("-" * 60 + "\n")
    print(f"Dumped {len(sub_items)} items for {d} into items_{d}.txt")
