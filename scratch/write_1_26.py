import json
from pathlib import Path

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
data = json.load(open(ROOT / "scratch/rotulos_analysis.json", encoding="utf-8"))

out = []
for i, item in enumerate(data[:26], 1):
    out.append(f"[{i:02d}] {item['sid']} (pág. {item['sp']}-{item['ep']}) score={item['score']}")
    out.append(f"     Atual: {item['current_startTopic']}")
    for p, lines in item['first_lines']:
        preview = " // ".join(l[:60] for l in lines[:3])
        out.append(f"     Pág {p}: {preview}")
    out.append("")

(ROOT / "scratch/suspects_1_26.txt").write_text("\n".join(out), encoding="utf-8")
print("Escrito scratch/suspects_1_26.txt")
