import json
from pathlib import Path
import shutil

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
SRC = ROOT / "content"
DST = ROOT / "web" / "content"

subjects = ["administracao", "direitos-humanos", "direito-processual-penal-militar"]

for s in subjects:
    for kind in ["structure", "segments", "edital"]:
        src_f = SRC / kind / f"{s}.json"
        if src_f.exists():
            dst_f = DST / kind / f"{s}.json"
            dst_f.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_f, dst_f)
            print(f"Copied {src_f} -> {dst_f}")

for top in ["catalog.json", "subjects.json", "contests.json", "importance/segments.json"]:
    src_f = SRC / top
    if src_f.exists():
        dst_f = DST / top
        dst_f.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_f, dst_f)
        print(f"Copied {src_f} -> {dst_f}")

print("Mirror para web/content concluído!")
