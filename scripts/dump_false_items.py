import glob
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

subjects = ['matematica', 'estatistica', 'fisica']
all_items = []

for s in subjects:
    files = sorted(glob.glob(f'content/items/{s}/*.json'))
    for f in files:
        data = json.load(open(f, encoding='utf-8'))
        for seg in data['segments']:
            sid = seg['id']
            for sub in ['teoria', 'revisao']:
                for idx, it in enumerate(seg.get('bizu', {}).get(sub, [])):
                    all_items.append({
                        'id': f'{sid}#{sub}#{idx}',
                        's': s,
                        'st': it['statement'],
                        'exp': it['explanation'],
                        'isTrue': it['isTrue']
                    })

print('Loaded subjects items:', len(all_items))
false_items = [it for it in all_items if not it['isTrue']]
print('False items count:', len(false_items))

with open('verify_false_items.txt', 'w', encoding='utf-8') as out:
    for it in false_items:
        out.write(f"{it['id']}\nST : {it['st']}\nEXP: {it['exp']}\n{'-'*60}\n")

print('Dumped false items to verify_false_items.txt')
