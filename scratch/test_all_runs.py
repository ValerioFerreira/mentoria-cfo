import json
from pathlib import Path
import re
import unicodedata

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
PAGES_DIR = ROOT / "pipeline" / ".cache" / "pages"

def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "", s.lower())

def analyze_pdf_structure(pages_data):
    pages = pages_data["pages"]
    tot = len(pages)
    
    # 1. Detect TOC pages (front)
    toc_pages = []
    for p in pages[:8]:
        t_norm = norm(p["text"])
        if "sumario" in t_norm or "indice" in t_norm:
            toc_pages.append(p["n"])
    
    front_end = max(toc_pages) if toc_pages else 1
    # Check if there are presentation pages between front_end and theory
    # For instance, if TOC is at page 2, but pages 3-7 are "Apresentação do curso"
    theory_start = front_end + 1
    for p in pages[front_end:min(front_end + 8, tot)]:
        lines = [ln.strip() for ln in p["text"].split("\n") if ln.strip()]
        for ln in lines[:4]:
            nl = norm(ln)
            if nl.startswith("apresentacaodocurso") or nl.startswith("formasdecontato") or nl.startswith("forumdeduvidas"):
                theory_start = p["n"] + 1

    # 2. Detect commented questions, list, and gabarito
    comm_start = None
    list_start = None
    gab_start = None

    for p in pages:
        p_num = p["n"]
        if p_num < theory_start:
            continue
        lines = [ln.strip() for ln in p["text"].split("\n") if ln.strip()]
        for ln in lines[:6]:
            nl = norm(ln)
            if not comm_start:
                if ("questoescomentadas" in nl or 
                    "questoescomcomentarios" in nl or 
                    "listadequestoescomcomentarios" in nl or
                    "exercicioscomentados" in nl):
                    comm_start = p_num
                    break
            if not list_start and comm_start and p_num > comm_start:
                if ("listadequestoes" in nl or 
                    "questoessemcomentarios" in nl or 
                    "questoespropostas" in nl):
                    if "comcomentarios" not in nl:
                        list_start = p_num
                        break
            if not gab_start and (list_start or comm_start):
                if nl == "gabarito" or nl.startswith("gabaritodasquestoes") or nl.startswith("gabaritofinal"):
                    gab_start = p_num
                    break

    # If list_start was not found, check if gab_start exists
    # Determine runs
    theory_end = (comm_start - 1) if comm_start else ((list_start - 1) if list_start else ((gab_start - 1) if gab_start else tot))
    comm_end = (list_start - 1) if list_start else ((gab_start - 1) if gab_start else tot) if comm_start else None
    list_end = (gab_start - 1) if gab_start else tot if list_start else None

    return {
        "aula": pages_data["aula"],
        "tot": tot,
        "front": f"1-{theory_start - 1}",
        "theory": f"{theory_start}-{theory_end} ({theory_end - theory_start + 1}p)",
        "comm": f"{comm_start}-{comm_end} ({comm_end - comm_start + 1 if comm_start else 0}p)" if comm_start else None,
        "list": f"{list_start}-{list_end} ({list_end - list_start + 1 if list_start else 0}p)" if list_start else None,
        "gab": f"{gab_start}-{tot} ({tot - gab_start + 1 if gab_start else 0}p)" if gab_start else None,
    }

for prefix in ["49", "50", "26"]:
    print(f"\n=================== PREFIX {prefix} ===================")
    for p in sorted(PAGES_DIR.glob(f"{prefix}_*.json")):
        data = json.loads(p.read_text(encoding="utf-8"))
        res = analyze_pdf_structure(data)
        print(f"{p.stem:7s} {res['aula']:35s} tot={res['tot']:3d} | front={res['front']} | th={res['theory']} | comm={res['comm']} | list={res['list']} | gab={res['gab']}")
