import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

disciplinas = ['matematica', 'raciocinio-logico', 'estatistica', 'fisica']
all_genuine = []

for d in disciplinas:
    for f in sorted(glob.glob(f'content/items/{d}/*.json')):
        data = json.load(open(f, encoding='utf-8'))
        aula_name = f.replace('\\', '/').split('/')[-1].replace('.json', '')
        for s in data['segments']:
            sid = s['id']
            for subset in ['teoria', 'revisao']:
                for idx, it in enumerate(s.get('bizu', {}).get(subset, [])):
                    st = it['statement']
                    if any(k in st for k in ['âmbito de', 'Conceitos Estruturantes', 'balizas conceituais', 'critérios normativos']):
                        continue
                    if re.search(r'(=|≠|<|>|≤|≥|igual a|vale |resulta em|é de \d|são \d)', st):
                        all_genuine.append({
                            'id': f'{sid}#{subset}#{idx}',
                            'd': d,
                            'aula': aula_name,
                            'st': st,
                            'isTrue': it['isTrue'],
                            'exp': it['explanation']
                        })

with open('calc_items.txt', 'w', encoding='utf-8') as out:
    for it in all_genuine:
        ans = 'C' if it['isTrue'] else 'E'
        out.write(f"[{ans}] {it['id']}\n")
        out.write(f"ST : {it['st']}\n")
        out.write(f"EXP: {it['exp']}\n")
        out.write("-" * 60 + "\n")

print(f"Dumped {len(all_genuine)} calc items.")
