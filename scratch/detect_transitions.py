import json
from pathlib import Path
import re
import unicodedata

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
PAGES_DIR = ROOT / "pipeline" / ".cache" / "pages"

def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "", s.lower())

RE_COMMENTED = re.compile(
    r"(quest[õo]es\s+(?:comentadas|com\s+coment[áa]rios)|lista\s+de\s+quest[õo]es\s+com\s+coment[áa]rios|exerc[íi]cios\s+comentados)",
    re.I
)
RE_LIST = re.compile(
    r"(lista\s+de\s+quest[õo]es(?:\s+sem\s+coment[áa]rios)?|quest[õo]es\s+sem\s+coment[áa]rios|quest[õo]es\s+propostas)",
    re.I
)
RE_GABARITO = re.compile(r"^\s*(?:\d+[\.\s-]*)?gabarito\b", re.I)
RE_RESUMO = re.compile(r"^\s*(?:\d+[\.\s-]*)?resumo\s+(?:estrat[ée]gico|da\s+aula)\b", re.I)

for prefix in ["49", "50", "26"]:
    for p in sorted(PAGES_DIR.glob(f"{prefix}_*.json")):
        data = json.loads(p.read_text(encoding="utf-8"))
        aula = data["aula"]
        total = len(data["pages"])
        
        # 1. Detect TOC page(s)
        toc_pages = []
        for pg in data["pages"][:8]:
            t_norm = norm(pg["text"])
            if "sumario" in t_norm or "indice" in t_norm:
                toc_pages.append(pg["n"])
        
        last_toc = max(toc_pages) if toc_pages else 1
        
        # 2. Search for transitions ONLY AFTER last_toc
        comm_p = None
        list_p = None
        gab_p = None
        res_p = None
        
        for pg in data["pages"]:
            if pg["n"] <= last_toc:
                continue
            lines = [ln.strip() for ln in pg["text"].split("\n") if ln.strip()]
            for ln in lines[:8]:
                if not comm_p and RE_COMMENTED.search(ln):
                    comm_p = pg["n"]
                    break
                if not list_p and RE_LIST.search(ln):
                    # make sure it's not "lista de questões com comentários"
                    if not RE_COMMENTED.search(ln):
                        list_p = pg["n"]
                        break
                if not gab_p and RE_GABARITO.search(ln):
                    gab_p = pg["n"]
                    break
                if not res_p and RE_RESUMO.search(ln):
                    res_p = pg["n"]
                    break

        print(f"{p.stem:7s} {aula:35s} tot={total:3d} toc={toc_pages} res={res_p} comm={comm_p} list={list_p} gab={gab_p}")
