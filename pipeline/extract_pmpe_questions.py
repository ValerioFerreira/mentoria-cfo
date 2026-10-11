"""Extrator e classificador de questões das aulas da PMPE (Estratégia Concursos).

Lê os PDFs das pastas docs/17-* até docs/41-*, extrai as questões das seções
de 'Questões Comentadas' com enunciado, alternativas, gabarito e explicação,
identifica a banca (AOCP, Instituto AOCP, FGV, CEBRASPE, FCC, etc.) e mapeia
para a disciplina e assunto correspondentes no sistema.
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
from pipeline.corpus import split_item, parse_tag, is_real_tag

DOCS_DIR = ROOT / "docs"

# Mapeamento do nome da pasta para subjectId do sistema
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
    "Direito Penal Militar": "direito-penal-militar",
    "Direito Processual Penal Militar": "direito-penal-militar",
    "Direito Penal": "direito-penal-militar", # Mapeia para direito ou penal se aplicavel
    "Direito Processual Penal": "direito-penal-militar",
    "Informática": "informatica",
    "Informatica": "informatica",
    "Legislação Penal Especial": "legislacoes-pe",
    "Legislacao Penal Especial": "legislacoes-pe",
    "Legislação Extravagante": "legislacoes-pe",
    "Legislacao Extravagante": "legislacoes-pe",
    "História de Pernambuco": "historia-pe",
    "Historia de Pernambuco": "historia-pe",
}

TAG_RE = re.compile(r"^[ \t]*(\d{1,3})[ \t]*\.[ \t]*\n?[ \t]*\(\s*([^()\n]{3,120}?)\s*\)[ \t]*", re.MULTILINE)

def get_subject_from_folder(folder_name: str) -> str:
    # Remove prefixo numérico ex: "17 - PM-PE (Oficial) Direito Administrativo"
    clean = re.sub(r"^\d+\s*-\s*", "", folder_name)
    clean = re.sub(r"^PM-PE\s*(\((?:Oficial|Soldado)\))?\s*", "", clean).strip()
    clean = re.sub(r"\(Prof\..*?\)", "", clean).strip()
    
    for k, v in FOLDER_TO_SUBJECT.items():
        if k.lower() in clean.lower():
            return v
    return "direito-constitucional"

def extract_questions_from_estrategia_pdf(pdf_path: Path, subject_id: str) -> list[dict]:
    doc = fitz.open(pdf_path)
    
    # Procurar páginas de início das Questões Comentadas e Lista de Questões
    sections = []
    for p in range(min(6, len(doc))):
        lines = [l.strip() for l in doc[p].get_text('text').splitlines() if l.strip()]
        for i, l in enumerate(lines):
            if re.search(r'Quest[õo]es', l, re.IGNORECASE):
                m = re.search(r'(\d+)\s*$', l)
                p_num = None
                if m:
                    p_num = int(m.group(1))
                elif i + 1 < len(lines) and lines[i+1].isdigit():
                    p_num = int(lines[i+1])
                if p_num and 1 < p_num <= len(doc):
                    sections.append((l, p_num))
                    
    commented_pages = [p for (l, p) in sections if re.search(r'Quest[õo]es\s+(?:Comentadas|com\s+Coment[áa]rios)', l, re.IGNORECASE)]
    uncommented_pages = [p for (l, p) in sections if re.search(r'Lista\s+de\s+Quest[õo]es', l, re.IGNORECASE)]
    
    start_page = min(commented_pages) - 1 if commented_pages else None
    end_page = min(uncommented_pages) - 1 if uncommented_pages else None
    
    if start_page is None:
        for p in range(len(doc)):
            txt = doc[p].get_text('text')
            if re.search(r'QUEST[ÕO]ES\s+(?:COMENTADAS|COM\s+COMENT[ÁA]RIOS)', txt, re.IGNORECASE):
                start_page = p
                break
                
    if end_page is None and start_page is not None:
        for p in range(start_page, len(doc)):
            txt = doc[p].get_text('text')
            if re.search(r'LISTA\s+DE\s+QUEST[ÕO]ES', txt, re.IGNORECASE):
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
    
    # Extrai tópico do nome do arquivo
    # Ex: "001 - Aula 00 - Prof Herbert Almeida.pdf" ou "002 - Aula 01 Ortografia.pdf"
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
            
        # Hash para deduplicação
        norm_st = re.sub(r"\s+", " ", statement.lower())
        opts_str = "|".join(f"{k}:{re.sub(r'\s+', ' ', v.lower())}" for k, v in sorted(options_dict.items()))
        chash = hashlib.sha256(f"{norm_st}::{opts_str}".encode("utf-8")).hexdigest()
        
        # Montar opções estruturadas
        formatted_options = []
        for k in sorted(options_dict.keys()):
            formatted_options.append({
                "label": k.upper(),
                "text": options_dict[k],
                "isCorrect": (k.upper() == answer.upper())
            })
            
        explanation = comment if comment else f"Gabarito oficial: Letra {answer}."
        
        q_obj = {
            "id": f"pmpe_{chash[:16]}",
            "contentHash": chash,
            "subjectId": subject_id,
            "aulaId": pdf_path.parent.name[:2],
            "segmentId": f"estrategia-{pdf_path.stem[:15]}",
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

def scan_all_pmpe() -> list[dict]:
    all_questions = []
    seen_hashes = set()
    
    folders = sorted(DOCS_DIR.glob("[1-4]*"))
    pmpe_folders = []
    for f in folders:
        m = re.match(r"^(\d+)", f.name)
        if m and int(m.group(1)) >= 17:
            pmpe_folders.append(f)
            
    print(f"Encontradas {len(pmpe_folders)} pastas da PMPE para varredura.")
    
    for folder in pmpe_folders:
        subject_id = get_subject_from_folder(folder.name)
        pdf_files = sorted(folder.glob("*.pdf"))
        print(f"Varrendo {folder.name} ({len(pdf_files)} PDFs) -> Matéria: {subject_id}...")
        
        folder_qs = 0
        for pdf in pdf_files:
            try:
                qs = extract_questions_from_estrategia_pdf(pdf, subject_id)
                for q in qs:
                    if q["contentHash"] in seen_hashes:
                        continue
                    seen_hashes.add(q["contentHash"])
                    all_questions.append(q)
                    folder_qs += 1
            except Exception as e:
                # Log e continua
                pass
        print(f"  -> {folder_qs} questões únicas extraídas desta pasta.")
        
    print(f"\nTOTAL PMPE EXTRAÍDO: {len(all_questions)} questões únicas.")
    return all_questions

if __name__ == "__main__":
    out_file = ROOT / "pipeline" / ".cache" / "pmpe_extracted_questions.json"
    out_file.parent.mkdir(parents=True, exist_ok=True)
    qs = scan_all_pmpe()
    out_file.write_text(json.dumps(qs, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Salvo em {out_file}")
