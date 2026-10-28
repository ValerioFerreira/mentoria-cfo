import json
from pathlib import Path
import re

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
PAGES_DIR = ROOT / "pipeline" / ".cache" / "pages"

for prefix in ["49", "50", "26"]:
    print(f"\n=================== PREFIX {prefix} ===================")
    for p in sorted(PAGES_DIR.glob(f"{prefix}_*.json")):
        data = json.loads(p.read_text(encoding="utf-8"))
        aula = data["aula"]
        total = len(data["pages"])
        print(f"\n--- {p.stem}: {aula} ({total} pages) ---")
        # search for sumário / índice in first 8 pages
        found_toc = False
        for pg in data["pages"][:8]:
            txt = pg["text"]
            if re.search(r"\b(sum[áa]rio|ndice|indice)\b", txt, re.I):
                print(f"  Found TOC on page {pg['n']}:")
                for line in txt.split("\n"):
                    line_s = line.strip()
                    if re.search(r"\d+\s*$", line_s) or re.search(r"^\d+[\)\.-]", line_s) or "..." in line_s:
                        print(f"    {line_s[:100]}")
                found_toc = True
                break
        if not found_toc:
            print("  NO TOC FOUND in first 8 pages!")
