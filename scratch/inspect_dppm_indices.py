import json
from pathlib import Path

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
PAGES_DIR = ROOT / "pipeline" / ".cache" / "pages"

for key in sorted(PAGES_DIR.glob("26_*.json"))[:4]:
    data = json.loads(key.read_text(encoding="utf-8"))
    print(f"=== {key.stem} page 2 (Índice) ===")
    print(data["pages"][1]["text"][:1000])
