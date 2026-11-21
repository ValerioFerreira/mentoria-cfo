import json

with open('scratch/estat_fixacao_raw.json', encoding='utf-8') as f:
    raw = json.load(f)

for qid in raw:
    q = raw[qid]
    print(f"=== {qid} ({q['capitulo']}) Gab: {q['gabarito']} ===")
    print("ENUN:", q['enunciado'].replace('\n', ' ')[:140])
    for alt in q['alternativas']:
        print(f"  {alt['letra']}: {alt['texto'].replace('\n', ' ')[:100]}")
