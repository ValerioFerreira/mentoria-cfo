import json, subprocess
from pathlib import Path

data = json.load(open('scratch/trechos_fracos/direito-penal.json', encoding='utf-8'))
out_dir = Path('scratch/summaries_fracos')
out_dir.mkdir(parents=True, exist_ok=True)

for d in data:
    seg = d['seg']
    fname = out_dir / (seg.replace('/', '_') + '.md')
    if not fname.exists():
        cmd = ['pipeline/.venv/Scripts/python', 'pipeline/pcpe_tools/seg_summary.py', f"direito-penal/{seg}"]
        res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        fname.write_text(res.stdout, encoding='utf-8')
        print(f"Dumped {seg}")
print("Done dumping summaries.")
