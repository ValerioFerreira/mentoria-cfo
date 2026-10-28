import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
data = json.load(open(ROOT / "scratch/rotulos_analysis.json", encoding="utf-8"))

for i, item in enumerate(data, 1):
    print(f"[{i:02d}] {item['sid']} (pág. {item['sp']}-{item['ep']}) score={item['score']}")
    print(f"     Atual: {item['current_startTopic']}")
    for p, lines in item['first_lines']:
        preview = " // ".join(l[:60] for l in lines[:4])
        # clean unicode characters that could be problematic
        preview = preview.encode('ascii', errors='replace').decode()
        print(f"     Pág {p}: {preview}")
    print()
