import json
from pathlib import Path
import re
import unicodedata

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
PAGES_DIR = ROOT / "pipeline" / ".cache" / "pages"

def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "", s.lower())

def extract_toc_topics(pages_data, theory_start, theory_end):
    pages = pages_data["pages"]
    topics = []
    
    # Check first 8 pages for TOC
    for p in pages[:8]:
        text = p["text"]
        lines = [ln.strip() for ln in text.split("\n") if ln.strip()]
        for ln in lines:
            # Pattern 1: '1) Topic Name ... 3' or '1 - Topic Name ... 3' or 'Topic Name ........ 14'
            m = re.search(r"^(?:(\d+(?:\.\d+)*)\s*[\)\.-]\s*)?(.+?)\s*\.{3,}\s*(\d+)\s*$", ln)
            if not m:
                # Pattern 2: '1. Topic Name' on one line, number on next? But let's check m first
                m = re.search(r"^(?:(\d+(?:\.\d+)*)\s*[\)\.-]\s*)?(.+?)\s+(\d{1,3})\s*$", ln)
            if m:
                num_part = m.group(1) or ""
                title_part = m.group(2).strip()
                try:
                    pg_num = int(m.group(3))
                except ValueError:
                    continue
                
                # Check if it's theory topic (page between theory_start and theory_end)
                # Note: TOC printed page may have an offset from PDF page
                # We'll see how printed page relates to pdfPage
                title_norm = norm(title_part)
                if any(w in title_norm for w in ["questoes", "gabarito", "lista", "resumo", "apresentacao", "sobreo"]):
                    continue
                full_title = f"{num_part} - {title_part}" if num_part else title_part
                topics.append({"title": full_title, "tocPage": pg_num})
    return topics

for prefix in ["49", "50", "26"]:
    print(f"\n=================== PREFIX {prefix} ===================")
    for p in sorted(PAGES_DIR.glob(f"{prefix}_*.json"))[:3]:
        data = json.loads(p.read_text(encoding="utf-8"))
        topics = extract_toc_topics(data, 1, 999)
        print(f"{p.stem} ({data['aula']}): {len(topics)} TOC topics:")
        for t in topics[:6]:
            print(f"    {t['tocPage']:3d}: {t['title']}")
