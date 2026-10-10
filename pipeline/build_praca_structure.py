import glob
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = ROOT / "pipeline" / ".cache"
PAGES_DIR = CACHE_DIR / "pages"
HEADINGS_DIR = CACHE_DIR / "headings"
CONTENT_DIR = ROOT / "content"
STRUCTURE_DIR = CONTENT_DIR / "structure"
SEGMENTS_DIR = CONTENT_DIR / "segments"
ITEMS_DIR = CONTENT_DIR / "items"
EDITAL_DIR = CONTENT_DIR / "edital"

STRUCTURE_DIR.mkdir(parents=True, exist_ok=True)
SEGMENTS_DIR.mkdir(parents=True, exist_ok=True)
EDITAL_DIR.mkdir(parents=True, exist_ok=True)


def clean_title(t: str) -> str:
    t = re.sub(r"^\s*(\d+[.\-–\s]*)+", "", t) # Remove numeração inicial
    t = re.sub(r"\s+", " ", t).strip()
    return t


def find_sections(pages: list[dict]):
    """Classifica as páginas da aula."""
    total = len(pages)
    commented_start = None
    list_start = None
    gabarito_page = None
    summary_page = None
    
    # 1. Procurar marcadores padrão no final
    for p in pages:
        n = p["n"]
        txt = p["text"]
        lines = [ln.strip() for ln in txt.splitlines() if ln.strip()]
        for line in lines[:8]:
            norm = line.lower().replace(" ", "")
            if norm in ("questoescomentadas", "questõescomentadas", "questoesparafixacao", "questõesparafixação", "resolucaodequestoes") and not commented_start:
                if n > 5:
                    commented_start = n
            elif norm in ("listadequestoes", "listadequestões", "questoessemcomentarios", "questõessemcomentários", "listadeexercicios") and not list_start:
                if n > 10:
                    list_start = n
            elif norm in ("gabarito", "gabaritos") and not gabarito_page:
                if n > 10:
                    gabarito_page = n
            elif norm in ("resumo", "resumodaaula", "resumodostemas", "mapasmentais", "mapamental") and not summary_page:
                if n > 15: # Evita pegar sumário na pág 2/3
                    summary_page = n

    # Determinar fim da teoria
    markers = [x for x in [commented_start, list_start, summary_page] if x is not None and x > 4]
    theory_end = min(markers) - 1 if markers else total
    
    # Se a aula for apenas questões/retrospectiva sem bloco comentado formal, teoria cobre até a última pág
    if theory_end < 4:
        theory_end = total
        
    return {
        "totalPages": total,
        "theoryPages": theory_end,
        "theoryRuns": [[1, theory_end]],
        "commentedStart": commented_start,
        "listStart": list_start,
        "gabaritoPage": gabarito_page,
    }


def main():
    print("=== CONSTRUINDO ESTRUTURA E SEGMENTAÇÃO DE PRAÇA CBMPE ===")
    
    subjects_info = [
        ("raciocinio-logico", "14"),
        ("historia-pe", "15"),
        ("atualidades", "16"),
    ]
    
    for subject_id, prefix in subjects_info:
        page_files = sorted(PAGES_DIR.glob(f"{prefix}_*.json"))
        aulas_structure = []
        subject_segments = []
        
        for pfile in page_files:
            data = json.loads(pfile.read_text(encoding="utf-8"))
            aula_num = data["aulaNumber"]
            aula_id = f"{subject_id}/a{aula_num:02d}"
            pages = data["pages"]
            sec = find_sections(pages)
            
            # Headings da teoria
            h_file = HEADINGS_DIR / f"{data['key']}.json"
            raw_h = json.loads(h_file.read_text(encoding="utf-8")) if h_file.exists() else {}
            heads = raw_h.get("headings", []) if isinstance(raw_h, dict) else raw_h
            
            # Filtra tópicos da teoria
            theory_heads = []
            seen_heads = set()
            for h in heads:
                p = h["page"]
                txt = clean_title(h["text"])
                if 1 <= p <= sec["theoryPages"] and len(txt) > 3 and txt.lower() not in seen_heads:
                    seen_heads.add(txt.lower())
                    theory_heads.append({"level": 1, "title": txt, "pdfPage": p, "printedPage": p, "kind": "heading", "verified": True})
            
            # Se não detectou headings (ex: Aula Única ou aula compacta), cria pelo menos 1 tópico principal
            if not theory_heads:
                title_main = data["file"].split(" - ", 1)[-1].replace(".pdf", "")
                theory_heads.append({"level": 1, "title": title_main, "pdfPage": 1, "printedPage": 1, "kind": "heading", "verified": True})
            
            # Segmentar teoria (alvo: 10–16 págs, max 17 págs)
            theory_total = sec["theoryPages"]
            segment_cuts = []
            cur_start = 1
            
            while cur_start <= theory_total:
                rem = theory_total - cur_start + 1
                if rem <= 16:
                    cur_end = theory_total
                else:
                    # Tenta cortar num heading próximo a cur_start + 12
                    best_cut = min(cur_start + 13, theory_total)
                    for th in theory_heads:
                        hp = th["pdfPage"]
                        if cur_start + 9 <= hp <= cur_start + 16:
                            best_cut = hp - 1
                            break
                    cur_end = min(best_cut, cur_start + 16, theory_total)
                
                segment_cuts.append((cur_start, cur_end))
                cur_start = cur_end + 1
            
            # Montar segmentos
            for s_idx, (st, en) in enumerate(segment_cuts, 1):
                seg_id = f"{aula_id}/s{s_idx:02d}"
                seg_pages = en - st + 1
                
                # Tópico inicial
                matching_th = [th for th in theory_heads if st <= th["pdfPage"] <= en]
                start_topic = matching_th[0]["title"] if matching_th else theory_heads[0]["title"]
                end_topic = matching_th[-1]["title"] if matching_th else start_topic
                topics_covered = [th["title"] for th in matching_th] or [start_topic]
                
                # Próximo tópico para stopBeforeTopic
                next_matching = [th for th in theory_heads if th["pdfPage"] > en]
                stop_before = next_matching[0]["title"] if next_matching else None
                
                seg = {
                    "id": seg_id,
                    "aula": aula_id,
                    "order": s_idx,
                    "startPage": st,
                    "endPage": en,
                    "startPrinted": st,
                    "endPrinted": en,
                    "pages": seg_pages,
                    "load": round(seg_pages * 0.95, 2),
                    "startTopic": start_topic,
                    "startsMidTopic": s_idx > 1 and not any(th["pdfPage"] == st for th in theory_heads),
                    "stopBeforeTopic": stop_before,
                    "endsMidTopic": stop_before is None and s_idx < len(segment_cuts),
                    "endTopic": end_topic,
                    "endsTheory": s_idx == len(segment_cuts),
                    "topicsCovered": topics_covered,
                    "minutes": 60,
                }
                subject_segments.append(seg)
            
            # Aula structure
            commented_pages = (sec["listStart"] - sec["commentedStart"]) if (sec["listStart"] and sec["commentedStart"]) else ((sec["totalPages"] - sec["commentedStart"] + 1) if sec["commentedStart"] else 0)
            list_pages = (sec["totalPages"] - sec["listStart"] + 1) if sec["listStart"] else 0
            
            # Título da aula a partir do nome do arquivo
            raw_title = data["file"].split(" - ", 1)[-1].replace(".pdf", "")
            raw_title = re.sub(r"^Aula\s+(\d+|[úu]nica)\s*", "", raw_title, flags=re.I).strip() or raw_title
            
            aulas_structure.append({
                "id": aula_id,
                "number": aula_num,
                "file": data["file"],
                "title": raw_title,
                "totalPages": sec["totalPages"],
                "tocMax": 2,
                "printedOffset": 0,
                "theoryRuns": sec["theoryRuns"],
                "theoryPages": sec["theoryPages"],
                "commentedRuns": [[sec["commentedStart"], sec["listStart"] - 1]] if (sec["commentedStart"] and sec["listStart"]) else [],
                "commentedPages": max(0, commented_pages),
                "listPages": max(0, list_pages),
                "segments": len(segment_cuts),
                "flags": [],
                "topics": theory_heads,
            })
            
        # Salva structure e segments
        struct_out = STRUCTURE_DIR / f"{subject_id}.json"
        struct_out.write_text(json.dumps({"subject": subject_id, "aulas": aulas_structure}, ensure_ascii=False, indent=2), encoding="utf-8")
        
        seg_out = SEGMENTS_DIR / f"{subject_id}.json"
        seg_out.write_text(json.dumps({"subject": subject_id, "segments": subject_segments}, ensure_ascii=False, indent=2), encoding="utf-8")
        
        print(f"[{subject_id}] {len(aulas_structure)} aulas, {len(subject_segments)} segmentos gerados com sucesso.")

    print("\nEstrutura e Segmentos gerados!")


if __name__ == "__main__":
    main()
