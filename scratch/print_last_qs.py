import json

with open('scratch/selected_bio_m02.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

with open('scratch/bio_m02_last_qs.txt', 'w', encoding='utf-8') as out:
    for i, q in enumerate(qs[12:], 13):
        out.write(f"=== [{i}] {q['id']} | Cap: {q['capitulo']} | Gab: {q['gabarito']} ===\n")
        out.write(f"Enunciado: {q['enunciado']}\n")
        for alt in q['alternativas']:
            out.write(f"  {alt['letra']}: {alt['texto']}\n")
        out.write("\n")
print("Salvo em scratch/bio_m02_last_qs.txt")
