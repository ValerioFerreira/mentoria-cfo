import subprocess
import os

os.makedirs('scratch/lp_sums', exist_ok=True)
segs = ['a00/s02', 'a00/s03', 'a00/s04', 'a00/s05', 'a04/s04', 'a04/s05']
for s in segs:
    clean_s = s.replace('/', '_')
    res = subprocess.run(['pipeline/.venv/Scripts/python', 'pipeline/pcpe_tools/seg_summary.py', f'lingua-portuguesa/{s}'], capture_output=True, text=True, encoding='utf-8')
    with open(f'scratch/lp_sums/{clean_s}.txt', 'w', encoding='utf-8') as f:
        f.write(res.stdout)
print('Done!')
