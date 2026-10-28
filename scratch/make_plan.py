import json
import random

def get_letters():
    for seed in range(1000):
        random.seed(seed)
        letters = ['A']*22 + ['B']*22 + ['C']*22 + ['D']*21 + ['E']*21
        random.shuffle(letters)
        max_run = 1
        cur_run = 1
        for i in range(1, len(letters)):
            if letters[i] == letters[i-1]:
                cur_run += 1
                max_run = max(max_run, cur_run)
            else:
                cur_run = 1
        seq = ['ABCDE'.index(x) for x in letters]
        cyclic_count = sum((seq[i+1] - seq[i]) % 5 == 1 for i in range(len(seq)-1))
        if max_run <= 2 and cyclic_count / 107 < 0.20:
            return letters

letters = get_letters()
data = json.load(open('scratch/trechos_fracos/direito-processual-penal.json', encoding='utf-8'))

q_idx = 0
plan = []
for seg_item in data:
    seg = seg_item['seg']
    k = seg_item['faltam']
    for _ in range(k):
        ans = letters[q_idx]
        plan.append({
            'q_num': q_idx + 1,
            'seg': seg,
            'ans': ans,
            'topicos': seg_item['topicos'],
            'paginas': seg_item['paginas']
        })
        q_idx += 1

print(f"Total planned: {len(plan)}")
json.dump(plan, open('scratch/plan_dpp.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print("Saved plan to scratch/plan_dpp.json")
