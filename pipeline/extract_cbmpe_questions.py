"""Extrator unificado de questões das aulas do CBMPE e PMPE (Estratégia Concursos).

Lê os PDFs das pastas docs/01-* até docs/16-* (CBMPE) e docs/17-* até docs/41-* (PMPE),
extrai todas as questões comentadas com enunciado, alternativas, gabarito e comentário,
identifica a banca oficial e vincula de forma segura às disciplinas e aulas válidas.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from pipeline.corpus import split_item, parse_tag
from pipeline.edital_classifier import EditalClassifier

DOCS_DIR = ROOT / "docs"

FOLDER_TO_SUBJECT: dict[str, str] = {
    "Direito Administrativo": "direito-administrativo",
    "Direito Constitucional": "direito-constitucional",
    "Direitos e Garantias Fundamentais": "direito-constitucional",
    "Direitos Humanos": "direito-constitucional",
    "Língua Portuguesa": "lingua-portuguesa",
    "Lingua Portuguesa": "lingua-portuguesa",
    "Língua Inglesa": "lingua-inglesa",
    "Lingua Inglesa": "lingua-inglesa",
    "Língua Espanhola": "lingua-espanhola",
    "Lingua Espanhola": "lingua-espanhola",
    "Raciocínio Lógico": "raciocinio-logico",
    "Raciocinio Logico": "raciocinio-logico",
    "Estatística": "estatistica",
    "Estatistica": "estatistica",
    "Matemática": "matematica",
    "Matematica": "matematica",
    "Física": "fisica",
    "Fisica": "fisica",
    "Química": "quimica",
    "Quimica": "quimica",
    "Biologia": "biologia",
    "Direito Penal Militar": "direito-penal-militar",
    "Direito Processual Penal Militar": "direito-penal-militar",
    "Direito Penal": "direito-penal-militar",
    "Direito Processual Penal": "direito-penal-militar",
    "Informática": "informatica",
    "Informatica": "informatica",
    "Legislação Penal Especial": "legislacoes-pe",
    "Legislacao Penal Especial": "legislacoes-pe",
    "Legislação Extravagante": "legislacoes-pe",
    "Legislacao Extravagante": "legislacoes-pe",
    "Legislações Pertinentes aos Militares": "legislacoes-pe",
    "Legislacoes Pertinentes aos Militares": "legislacoes-pe",
    "História de Pernambuco": "historia-pe",
    "Historia de Pernambuco": "historia-pe",
    "Atualidades": "atualidades",
}

TAG_RE = re.compile(r"^[ \t]*(\d{1,3})[ \t]*\.[ \t]*\n?[ \t]*\(\s*([^()\n]{3,120}?)\s*\)[ \t]*", re.MULTILINE)

def get_subject_from_folder(folder_name: str) -> str:
    clean = re.sub(r"^\d+\s*-\s*", "", folder_name)
    clean = re.sub(r"^(?:CBM-PE|CBMP-PE|PM-PE)\s*(\((?:Oficial|Praça|Soldado)\))?\s*", "", clean).strip()
    clean = re.sub(r"\(Prof\..*?\)", "", clean).strip()
    
    for k, v in FOLDER_TO_SUBJECT.items():
        if k.lower() in clean.lower():
            return v
    return "direito-constitucional"

def extract_questions_from_pdf(pdf_path: Path, subject_id: str, prefix: str) -> list[dict]:
    doc = fitz.open(pdf_path)
    
    sections = []
    for p in range(min(6, len(doc))):
        lines = [l.strip() for l in doc[p].get_text("text").splitlines() if l.strip()]
        for i, l in enumerate(lines):
            if re.search(r"Quest[õo]es", l, re.IGNORECASE):
                m = re.search(r"(\d+)\s*$", l)
                p_num = None
                if m:
                    p_num = int(m.group(1))
                elif i + 1 < len(lines) and lines[i+1].isdigit():
                    p_num = int(lines[i+1])
                if p_num and 1 < p_num <= len(doc):
                    sections.append((l, p_num))
                    
    commented_pages = [p for (l, p) in sections if re.search(r"Quest[õo]es\s+(?:Comentadas|com\s+Coment[áa]rios)", l, re.IGNORECASE)]
    uncommented_pages = [p for (l, p) in sections if re.search(r"Lista\s+de\s+Quest[õo]es", l, re.IGNORECASE)]
    
    start_page = min(commented_pages) - 1 if commented_pages else None
    end_page = min(uncommented_pages) - 1 if uncommented_pages else None
    
    if start_page is None:
        for p in range(len(doc)):
            txt = doc[p].get_text("text")
            if re.search(r"QUEST[ÕO]ES\s+(?:COMENTADAS|COM\s+COMENT[ÁA]RIOS)", txt, re.IGNORECASE):
                start_page = p
                break
                
    if end_page is None and start_page is not None:
        for p in range(start_page, len(doc)):
            txt = doc[p].get_text("text")
            if re.search(r"LISTA\s+DE\s+QUEST[ÕO]ES", txt, re.IGNORECASE):
                end_page = p
                break
                
    if start_page is None:
        return []
    if end_page is None or end_page <= start_page:
        end_page = len(doc)
        
    full_text = ""
    for p in range(start_page, end_page):
        full_text += "\n" + doc[p].get_text("text")
        
    matches = list(TAG_RE.finditer(full_text))
    questions = []
    
    file_stem = pdf_path.stem
    topic_match = re.search(r"Aula\s+\d+\s*(?:-\s*)?(.*)", file_stem, re.IGNORECASE)
    default_topic = topic_match.group(1).strip() if topic_match and topic_match.group(1).strip() else file_stem
    
    for i, m in enumerate(matches):
        next_pos = matches[i + 1].start() if i + 1 < len(matches) else len(full_text)
        tag_str = m.group(2)
        body = full_text[m.end():next_pos]
        
        parsed = split_item(body)
        if not parsed:
            continue
            
        tag_meta = parse_tag(tag_str)
        banca = tag_meta.get("banca", "AOCP")
        if "AOCP" in banca.upper():
            banca = "AOCP"
            
        statement = parsed.get("statement", "").strip()
        options_dict = parsed.get("options", {})
        answer = parsed.get("answer")
        comment = parsed.get("comment", "").strip()
        
        if not statement or not options_dict or not answer:
            continue
            
        norm_st = re.sub(r"\s+", " ", statement.lower())
        opts_str = "|".join(f"{k}:{re.sub(r'\s+', ' ', v.lower())}" for k, v in sorted(options_dict.items()))
        chash = hashlib.sha256(f"{norm_st}::{opts_str}".encode("utf-8")).hexdigest()
        
        formatted_options = []
        for k in sorted(options_dict.keys()):
            formatted_options.append({
                "label": k.upper(),
                "text": options_dict[k],
                "isCorrect": (k.upper() == answer.upper())
            })
            
        explanation = comment if comment else f"Gabarito oficial: Letra {answer}."
        
        q_obj = {
            "id": f"{prefix}_{chash[:16]}",
            "contentHash": chash,
            "subjectId": subject_id,
            "topic": default_topic,
            "statement": statement,
            "explanation": explanation,
            "difficulty": 2,
            "pattern": banca,
            "banca": banca,
            "orgao": tag_meta.get("orgao", ""),
            "ano": tag_meta.get("ano"),
            "status": "APPROVED",
            "options": formatted_options,
            "sourcePdf": str(pdf_path.name),
        }
        questions.append(q_obj)
        
    return questions

def extract_all_cbmpe() -> list[dict]:
    all_questions = []
    seen_hashes = set()
    
    classifier = EditalClassifier()
    subject_fallbacks = {}
    for subj, segs in classifier.segments_cache.items():
        if segs:
            s0 = segs[0]
            subject_fallbacks[subj] = (s0["aula"], s0["id"])
            
    folders = sorted(DOCS_DIR.glob("[0-1][0-6]*"))
    cbmpe_folders = [f for f in folders if int(f.name[:2]) <= 16]
    
    print(f"Iniciando extração do CBMPE em {len(cbmpe_folders)} pastas...")
    
    class DummyQ:
        def __init__(self, raw_subject, raw_topic, statement):
            self.raw_subject = raw_subject
            self.raw_topic = raw_topic
            self.statement = statement

    for folder in cbmpe_folders:
        subject_id = get_subject_from_folder(folder.name)
        pdf_files = sorted(folder.glob("*.pdf"))
        print(f"Processando {folder.name} ({len(pdf_files)} PDFs) -> {subject_id}...")
        
        count = 0
        for pdf in pdf_files:
            try:
                qs = extract_questions_from_pdf(pdf, subject_id, "cbmpe")
                for q in qs:
                    if q["contentHash"] in seen_hashes:
                        continue
                    seen_hashes.add(q["contentHash"])
                    
                    # Classificação com EditalClassifier
                    dq = DummyQ(subject_id, q["topic"], q["statement"])
                    res = classifier.classify_question(dq)
                    if res.subject_id == subject_id:
                        q["subjectId"] = res.subject_id
                        q["aulaId"] = res.aula_id
                        q["segmentId"] = res.segment_id
                    else:
                        q["subjectId"] = subject_id
                        fb_aula, fb_seg = subject_fallbacks.get(subject_id, (f"{subject_id}/a00", f"{subject_id}/a00/s01"))
                        q["aulaId"] = fb_aula
                        q["segmentId"] = fb_seg
                        
                    all_questions.append(q)
                    count += 1
            except Exception:
                pass
        print(f"  -> {count} questões únicas extraídas de {folder.name}.")
        
    print(f"\nTOTAL CBMPE EXTRAÍDO: {len(all_questions)} questões únicas.")
    return all_questions

if __name__ == "__main__":
    out_file = ROOT / "pipeline" / ".cache" / "cbmpe_extracted_questions.json"
    out_file.parent.mkdir(parents=True, exist_ok=True)
    qs = extract_all_cbmpe()
    out_file.write_text(json.dumps(qs, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Arquivo salvo com sucesso em {out_file}!")
