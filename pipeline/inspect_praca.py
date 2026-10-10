import glob
import json
import re
from pathlib import Path

PAGES_DIR = Path("pipeline/.cache/pages")
HEADINGS_DIR = Path("pipeline/.cache/headings")

for prefix in ["14_", "15_", "16_"]:
    for f in sorted(PAGES_DIR.glob(f"{prefix}*.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        pages = data["pages"]
        
        # Detecta onde começa a seção de questões
        commented_start = None
        list_start = None
        gabarito_page = None
        resumo_page = None
        
        for p in pages:
            t = p["text"]
            lines = [ln.strip() for ln in t.splitlines() if ln.strip()]
            for line in lines[:8]:
                norm = line.lower().replace(" ", "")
                if ("questoescomentadas" in norm or "questõescomentadas" in norm) and not commented_start:
                    commented_start = p["n"]
                elif ("listadequestoes" in norm or "listadequestões" in norm or "questoessemcomentarios" in norm) and not list_start:
                    list_start = p["n"]
                elif "gabarito" in norm and len(norm) <= 12 and not gabarito_page:
                    gabarito_page = p["n"]
                elif ("resumodaaula" in norm or "resumo" in norm) and len(norm) <= 16 and not resumo_page:
                    resumo_page = p["n"]
        
        theory_end = min(x for x in [commented_start, list_start, resumo_page, len(pages)] if x is not None) - 1
        if theory_end < 1:
            theory_end = len(pages)
            
        h_file = HEADINGS_DIR / f"{data['key']}.json"
        raw_h = json.loads(h_file.read_text(encoding="utf-8")) if h_file.exists() else {}
        heads = raw_h.get("headings", []) if isinstance(raw_h, dict) else raw_h
        theory_heads = [h for h in heads if h["page"] <= theory_end]
        
        print(f"{data['key']}: {data['subject']} a{data['aulaNumber']:02d} | total={len(pages)} págs | teoria=1..{theory_end} ({theory_end}p) | coment={commented_start}..{list_start or len(pages)} | headings_teoria={len(theory_heads)}")
