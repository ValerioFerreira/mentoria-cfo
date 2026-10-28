import json
from pathlib import Path
import re

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
PAGES_DIR = ROOT / "pipeline" / ".cache" / "pages"

for key in sorted(PAGES_DIR.glob("26_*.json")):
    data = json.loads(key.read_text(encoding="utf-8"))
    print(f"=== {key.stem} ({data['aula']}) total {len(data['pages'])} pages ===")
    for pg in data["pages"][:10]:
        txt = pg["text"].strip()
        first_lines = [l.strip() for l in txt.split("\n") if l.strip()][:6]
        for l in first_lines:
            if any(w in l.lower() for w in ["sumário", "índice", "sumario", "indice", "aula"]):
                print(f"  P{pg['n']}: {l}")
            m = re.match(r"^(\d+[\.\s-].{4,60})", l)
            if m:
                print(f"  P{pg['n']} heading: {m.group(1)}")
