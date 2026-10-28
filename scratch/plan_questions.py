import json

data = json.load(open('scratch/trechos_fracos/direito-penal.json', encoding='utf-8'))
gabaritos = json.load(open('scratch/gabaritos_123.json', encoding='utf-8'))

plan = []
idx = 0
for d in data:
    seg = d['seg']
    faltam = d['faltam']
    aula = d['aula']
    topicos = d['topicos']
    for _ in range(faltam):
        plan.append({
            "idx": idx + 1,
            "seg": seg,
            "ans": gabaritos[idx],
            "aula": aula,
            "topicos": topicos
        })
        idx += 1

assert len(plan) == 123
print(f"Total planned: {len(plan)}")
with open("scratch/plan_123.json", "w", encoding="utf-8") as f:
    json.dump(plan, f, ensure_ascii=False, indent=2)
print("Plan saved to scratch/plan_123.json")
