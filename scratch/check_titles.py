import json
from pathlib import Path
import re

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
PAGES_DIR = ROOT / "pipeline" / ".cache" / "pages"

def clean_title(filename):
    t = re.sub(r"^\s*\d{3}\s*-\s*Aula\s*\d+\s*[-–]?\s*", "", filename)
    t = re.sub(r"^\s*-\s*Prof\..*?-\s*", "", t)
    t = re.sub(r"\.pdf$", "", t).strip()
    return t

for prefix, name in [("49", "administracao"), ("50", "direitos-humanos"), ("26", "direito-processual-penal-militar")]:
    print(f"\n=== {name} ===")
    for p in sorted(PAGES_DIR.glob(f"{prefix}_*.json")):
        data = json.loads(p.read_text(encoding="utf-8"))
        ct = clean_title(data["file"])
        print(f"  {data['aula']}: {ct}")
