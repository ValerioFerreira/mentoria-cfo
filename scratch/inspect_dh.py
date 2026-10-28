import json
from pathlib import Path
import re

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
PAGES_DIR = ROOT / "pipeline" / ".cache" / "pages"

# Check DH a02 and a03
for key in ["50_003", "50_004"]: # 50_003 is a02, 50_004 is a03
    p = PAGES_DIR / f"{key}.json"
    data = json.loads(p.read_text(encoding="utf-8"))
    print(f"=== {key} ({data['aula']}) total {len(data['pages'])} pages ===")
    for pg in data["pages"]:
        txt = pg["text"].strip()
        first_lines = [l.strip() for l in txt.split("\n") if l.strip()][:5]
        for l in first_lines:
            if re.search(r"quest[õo]es|gabarito|lista|resumo", l, re.I):
                print(f"  P{pg['n']}: {l}")
