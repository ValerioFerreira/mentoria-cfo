import json
from pathlib import Path
import re
import unicodedata
import sys

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
sys.path.insert(0, str(ROOT / "pipeline"))
from textutil import aula_key_map, load_pages, norm

SUS_FILE = ROOT / "pipeline/.cache/pcpe-rotulos-suspeitos.json"
sus = json.loads(SUS_FILE.read_text(encoding="utf-8"))
keymap = aula_key_map()

results = []
for sid, (score, start_topic, sp) in sorted(sus.items()):
    disc, aula, s_num = sid.split("/")
    aula_id = f"{disc}/{aula}"
    seg_file = ROOT / f"content/segments/{disc}.json"
    struct_file = ROOT / f"content/structure/{disc}.json"
    
    seg_data = json.loads(seg_file.read_text(encoding="utf-8"))
    seg = next((s for s in seg_data["segments"] if s["id"] == sid), None)
    
    struct_data = json.loads(struct_file.read_text(encoding="utf-8"))
    aula_struct = next((a for a in struct_data["aulas"] if a["id"] == aula_id), None)
    
    # topics on startPage or startPage+1
    topics_around = []
    if aula_struct:
        for t in aula_struct.get("topics", []):
            if sp - 1 <= t["pdfPage"] <= sp + 2:
                topics_around.append((t["pdfPage"], t["level"], t["title"]))
                
    p_texts = []
    k = keymap.get(aula_id)
    if k:
        p_data = load_pages(k)
        for p in p_data.get("pages", []):
            if p["n"] in (sp, sp + 1):
                lines = [l.strip() for l in p["text"].splitlines() if l.strip()]
                p_texts.append((p["n"], lines[:6]))
                
    results.append({
        "sid": sid,
        "sp": sp,
        "ep": seg["endPage"] if seg else None,
        "score": score,
        "current_startTopic": start_topic,
        "topics_around": topics_around,
        "first_lines": p_texts
    })

(ROOT / "scratch/rotulos_analysis.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Gravado em scratch/rotulos_analysis.json com {len(results)} trechos.")
