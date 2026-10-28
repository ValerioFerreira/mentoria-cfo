import json
from pathlib import Path

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
PAGES_DIR = ROOT / "pipeline" / ".cache" / "pages"

for key in ["49_010", "49_011", "50_001", "50_002", "50_004", "50_005", "50_006"]:
    data = json.loads((PAGES_DIR / f"{key}.json").read_text(encoding="utf-8"))
    print(f"=== {key} ({data['aula']}) ===")
    print(data["pages"][0]["text"])
