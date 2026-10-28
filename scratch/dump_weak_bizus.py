import os, json, subprocess

os.makedirs('scratch/lp_weak_sums', exist_ok=True)
data = json.load(open('scratch/trechos_fracos/lingua-portuguesa.json', encoding='utf-8'))
for d in data:
    seg = d['seg']
    clean_seg = seg.replace('/', '_')
    res = subprocess.run(['pipeline/.venv/Scripts/python', 'pipeline/pcpe_tools/seg_bizu.py', f'lingua-portuguesa/{seg}'], capture_output=True, text=True, encoding='utf-8')
    with open(f'scratch/lp_weak_sums/{clean_seg}.txt', 'w', encoding='utf-8') as f:
        f.write(res.stdout)
print("Bizus dumped successfully for 23 segments.")
