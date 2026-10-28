import json
from pathlib import Path

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
PAGES_DIR = ROOT / "pipeline" / ".cache" / "pages"

for key in ["49_010", "49_011", "50_001", "50_002", "50_004", "50_005", "50_006"]:
    data = json.loads((PAGES_DIR / f"{key}.json").read_text(encoding="utf-8"))
    print(f"=== {key} ({data['aula']}) ===")
    for pg in data["pages"][1:6]:
        lines = [l.strip() for l in pg["text"].split("\n") if l.strip()]
        for l in lines[:4]:
            if "sumário" in l.lower() or "sumario" in l.lower() or "aula" in l.lower() or "direitos" in l.lower() or "administração" in l.lower() or "administracao" in l.lower():
                print(f"  P{pg['n']}: {l}")
