import random
import json
from pathlib import Path

# Deterministic shuffle
pool = ['A']*26 + ['B']*25 + ['C']*26 + ['D']*25 + ['E']*25
rng = random.Random(20261020)
rng.shuffle(pool)

data = json.loads(Path('scratch/trechos_fracos/informatica.json').read_text(encoding='utf-8'))

plan = []
idx = 0
for trecho_info in data:
    seg = trecho_info['seg']
    trecho = trecho_info['trecho']
    faltam = trecho_info['faltam']
    item_arg = trecho_info.get('item_arg')
    
    for q_in_seg in range(faltam):
        ans = pool[idx]
        plan.append({
            'q_num': idx + 1,
            'trecho': trecho,
            'seg': seg,
            'item_arg': item_arg,
            'ans': ans,
            'topicos': trecho_info['topicos'],
            'aula': trecho_info['aula']
        })
        idx += 1

assert idx == 127
Path('scratch/gabaritos_127.json').write_text(json.dumps(plan, indent=2, ensure_ascii=False), encoding='utf-8')
print('Planned 127 questions successfully.')
