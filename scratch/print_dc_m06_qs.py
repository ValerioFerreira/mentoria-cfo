import json

with open('scratch/selected_dc_m06.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

for i, q in enumerate(qs):
    print(f"=== [{i+1}] {q['id']} | Cap: {q['capitulo']} | Gab: {q['gabarito']} ===")
    print("Enunciado:", q['enunciado'][:200])
    for alt in q['alternativas']:
        print(f"  {alt['letra']}: {alt['texto'][:120]}")
    print()
