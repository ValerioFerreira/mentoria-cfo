import sys, json
sys.path.insert(0, '.')
from pipeline.questoes.ineditas import item_for_segment

data = json.load(open('scratch/trechos_fracos/lingua-portuguesa.json', encoding='utf-8'))
for d in data:
    seg = d['seg']
    full_seg = f"lingua-portuguesa/{seg}"
    res = item_for_segment('lingua-portuguesa', full_seg, d.get('item_arg'))
    print(f"{seg:10s} -> {res}")
