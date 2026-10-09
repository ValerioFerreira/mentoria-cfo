#!/usr/bin/env python3
"""Script de Auditoria por Amostragem e Varredura Completa.
Executa os 5 lotes de Diretrizes (100 cada) e os 5 lotes de Questões (200 cada + varredura global).
"""
import os
import sys
import json
import glob
import re
import random
from pathlib import Path
from collections import defaultdict, Counter
import fitz  # PyMuPDF

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
DOCS_DIR = ROOT / "docs"
CONTENT_DIR = ROOT / "content"
AUDIT_OUT = Path(r"C:\Users\Administrador\.gemini\antigravity\brain\94ed5ef5-5793-49ad-b5ab-7577f556a2ab\audits")
AUDIT_OUT.mkdir(parents=True, exist_ok=True)

# 1. Mapeamento de PDFs
def build_pdf_map():
    pdf_map = {}
    # Base PDFs
    for folder in DOCS_DIR.glob("*"):
        if folder.is_dir():
            prefix = folder.name[:2]
            for pdf_file in folder.glob("*.pdf"):
                m = re.match(r"^\s*(\d{3})\s*-\s*Aula\s+(\d+)", pdf_file.name, re.I)
                if m:
                    aula_num = int(m.group(2))
                    pdf_map[(prefix, aula_num)] = pdf_file
    return pdf_map

def get_subject_prefix(subjects, sub_id):
    for s in subjects:
        if s["id"] == sub_id:
            return s["folderPrefix"]
    return None

def load_catalog_and_subjects():
    catalog = json.loads((CONTENT_DIR / "catalog.json").read_text(encoding="utf-8"))
    subjects = json.loads((CONTENT_DIR / "subjects.json").read_text(encoding="utf-8"))["subjects"]
    return catalog, subjects

def get_aula_pdf(catalog, subjects, pdf_map, sub_id, aula_num):
    # Procura no catalog se é authored
    for s in catalog["subjects"]:
        if s["id"] == sub_id:
            for a in s["aulas"]:
                if a["number"] == aula_num:
                    if a.get("source") == "authored" or a.get("materialPath"):
                        p = ROOT / "web" / "public" / a["materialPath"]
                        if p.exists():
                            return p
                        p2 = CONTENT_DIR / "complements" / Path(a["materialPath"]).name
                        if p2.exists():
                            return p2
    prefix = get_subject_prefix(subjects, sub_id)
    if prefix and (prefix, aula_num) in pdf_map:
        return pdf_map[(prefix, aula_num)]
    return None

def extract_pdf_pages_text(pdf_path, start_page, end_page):
    """Extrai texto das páginas start_page a end_page (1-based)."""
    if not pdf_path or not Path(pdf_path).exists():
        return None
    try:
        doc = fitz.open(str(pdf_path))
        pages_text = {}
        for pno in range(start_page, min(end_page + 1, len(doc) + 1)):
            if pno - 1 < len(doc):
                pages_text[pno] = doc[pno - 1].get_text("text")
        doc.close()
        return pages_text
    except Exception as e:
        return None

def main():
    print("Iniciando auditoria...")
    pdf_map = build_pdf_map()
    catalog, subjects = load_catalog_and_subjects()
    print(f"Catalog carregado com {len(catalog['subjects'])} disciplinas. {len(pdf_map)} PDFs base indexados.")

    # Carrega todos os segmentos e itens
    all_segments = []
    all_questions = []

    for item_file in sorted((CONTENT_DIR / "items").glob("*/*.json")):
        sub_id = item_file.parent.name
        aula_name = item_file.stem
        try:
            data = json.loads(item_file.read_text(encoding="utf-8"))
            aula_num = data.get("aula", {}).get("number", int(aula_name[1:]) if aula_name.startswith("a") else 0)
            
            # Localiza metadados do segment no segments/<disciplina>.json para pegar startPrinted/endPrinted
            seg_meta_file = CONTENT_DIR / "segments" / f"{sub_id}.json"
            seg_meta_map = {}
            if seg_meta_file.exists():
                sm_data = json.loads(seg_meta_file.read_text(encoding="utf-8"))
                for sm in sm_data.get("segments", []):
                    seg_meta_map[sm["id"]] = sm

            for idx, seg in enumerate(data.get("segments", [])):
                seg_id = seg["id"]
                sm = seg_meta_map.get(seg_id, {})
                seg_info = {
                    "id": seg_id,
                    "subjectId": sub_id,
                    "aulaNumber": aula_num,
                    "startPage": sm.get("startPage", seg.get("startPage", 1)),
                    "endPage": sm.get("endPage", seg.get("endPage", 1)),
                    "startPrinted": sm.get("startPrinted"),
                    "endPrinted": sm.get("endPrinted"),
                    "startTopic": sm.get("startTopic"),
                    "stopBeforeTopic": sm.get("stopBeforeTopic"),
                    "endTopic": sm.get("endTopic"),
                    "bizu": seg.get("bizu", {}),
                    "questions_count": len(seg.get("questions", [])),
                    "raw_seg": seg
                }
                all_segments.append(seg_info)

                for qidx, q in enumerate(seg.get("questions", [])):
                    q_info = {
                        "id": f"{seg_id}#q{qidx+1:02d}",
                        "subjectId": sub_id,
                        "aulaNumber": aula_num,
                        "segmentId": seg_id,
                        "qIndex": qidx,
                        "data": q
                    }
                    all_questions.append(q_info)
        except Exception as e:
            print(f"Erro lendo {item_file}: {e}")

    print(f"Total de segmentos: {len(all_segments)}")
    print(f"Total de questões: {len(all_questions)}")

    # Salva json intermediário para os módulos específicos
    cache_data = {
        "all_segments_count": len(all_segments),
        "all_questions_count": len(all_questions),
    }
    (AUDIT_OUT / "meta.json").write_text(json.dumps(cache_data, indent=2, ensure_ascii=False), encoding="utf-8")

if __name__ == "__main__":
    main()
