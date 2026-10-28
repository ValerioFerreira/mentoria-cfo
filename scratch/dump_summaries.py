import subprocess
from pathlib import Path

segs = [
    'a05/s03', 'a06/s06', 'a06/s07', 'a07/s03', 'a07/s04',
    'a08/s01', 'a08/s02', 'a08/s03', 'a08/s04', 'a08/s05',
    'a09/s01', 'a09/s02', 'a09/s03', 'a09/s04', 'a09/s05',
    'a10/s01', 'a10/s02'
]

Path('scratch/summaries').mkdir(parents=True, exist_ok=True)
for s in segs:
    cmd = ['pipeline/.venv/Scripts/python', 'pipeline/pcpe_tools/seg_summary.py', f'direito-penal/{s}']
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    fname = 'scratch/summaries/' + s.replace('/', '_') + '.md'
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(res.stdout)
    print(f'Wrote {fname}')
