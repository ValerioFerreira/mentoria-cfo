"""Extrator de Alta Precisão e Auditoria Integral de Questões Estratégia (CBMPE e PMPE).

Realiza corte geométrico e filtragem semântica estrita para eliminar:
- Cabeçalhos de professores e identificadores de aula (y1 <= 52 e padrões de texto).
- Rodapés com dados de aluno/CPF, números de página, URLs e cursos (y0 >= 740 e padrões de texto).
- Encerramentos com redes sociais, banners e despedidas.

Gera um arquivo JSON auditado com Enunciado, Alternativas A-E, Gabarito, Comentários e Metadados.
"""
from __future__ import annotations

import concurrent.futures
import hashlib
import json
import os
import re
import sys
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

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
ALT_LINE = re.compile(r"^[ \t]*\(?([a-eA-E])\)[ \t]+(.*)$")
GAB_RE = re.compile(
    r"(?:gabarito|resposta|resp\.?)\s*[:\-–]?\s*(?:letra|alternativa|item)?\s*[:\-–]?\s*([A-E]|certo|errado|anulad[ao])\b",
    re.IGNORECASE,
)
COMMENT_RE = re.compile(r"^\s*(?:coment[áa]rios?|resolu[çc][ãa]o|gabarito|resposta|resp\.)\b", re.IGNORECASE | re.MULTILINE)

BANCA_PATTERNS = [
    (r"AOCP", "AOCP"),
    (r"FGV", "FGV"),
    (r"FCC", "FCC"),
    (r"CESPE|CEBRASPE", "CEBRASPE"),
    (r"VUNESP", "VUNESP"),
    (r"QUADRIX", "QUADRIX"),
    (r"IBFC", "IBFC"),
    (r"IDECAN", "IDECAN"),
    (r"CESGRANRIO", "CESGRANRIO"),
    (r"UPENET|IAUPE", "UPENET"),
    (r"CONSULPLAN", "CONSULPLAN"),
    (r"FUNDATEC", "FUNDATEC"),
    (r"FUMARC", "FUMARC"),
    (r"SELECON", "SELECON"),
    (r"NUCEPE", "NUCEPE"),
    (r"IADES", "IADES"),
]

RESIDUAL_LINE_PATTERNS = [
    re.compile(r"\b10341953440\b", re.I),
    re.compile(r"\bVal[ée]rio\s+Ferreira\b", re.I),
    re.compile(r"\b(?:www\.)?estrategiaconcursos\.com\.br\b", re.I),
    re.compile(r"\b(?:CBM-PE|CBMP-PE|PM-PE)\s*\([^\)]+\)", re.I),
    re.compile(r"^Aula\s+\d{1,2}(?:\s*-\s*[^\n]+)?$", re.I),
    re.compile(r"@prof\w+", re.I),
    re.compile(r"/prof\w+", re.I),
    re.compile(r"cursosPorProfessor", re.I),
]

def clean_lines(text: str) -> str:
    """Elimina linhas individuais de metadados que possam ter sobrado dentro de um bloco."""
    lines = text.splitlines()
    cleaned = []
    for ln in lines:
        s = ln.strip()
        if not s:
            cleaned.append(ln)
            continue
        if any(pat.search(s) for pat in RESIDUAL_LINE_PATTERNS):
            continue
        cleaned.append(ln)
    return "\n".join(cleaned)

def parse_banca_and_meta(tag: str) -> tuple[str, str, int | None]:
    banca = "AOCP"
    for pat, name in BANCA_PATTERNS:
        if re.search(r"\b" + pat + r"\b", tag, re.IGNORECASE):
            banca = name
            break
            
    year_m = re.search(r"\b(19\d\d|20\d\d)\b", tag)
    ano = int(year_m.group(1)) if year_m else None
    
    parts = [p.strip() for p in re.split(r"\s*[/–—-]\s*", tag) if p.strip()]
    orgao = ""
    for p in parts[1:]:
        if not re.fullmatch(r"(19|20)\d\d", p):
            orgao = p[:80]
            break
            
    return banca, orgao, ano

def sanitize_comment(comment: str) -> str:
    """Remove assinaturas de professores, despedidas e redes sociais."""
    cut_patterns = [
        r"\n\s*(?:Conclu[íi]mos\s+por\s+hoje|Bons\s+estudos|HERBERT\s+ALMEIDA|Diego\s+Carvalho|Renato\s+da\s+Costa|Siga\s+(?:minhas\s+)?redes|@prof\w+|https?://\S*cursosPorProfessor\S*|Se preferir, basta escanear|Um abraço e até a próxima aula|Grande abraço|Forte abraço).*",
    ]
    for cp in cut_patterns:
        comment = re.sub(cp, "", comment, flags=re.DOTALL | re.IGNORECASE)
    return clean_lines(comment).strip()

def extract_pdf_questions(pdf_path: Path, subject_id: str, prefix: str) -> list[dict]:
    try:
        doc = fitz.open(pdf_path)
    except Exception:
        return []
        
    start_page = None
    end_page = None
    
    # 1. Localização no Sumário (primeiras 6 páginas)
    for p in range(min(6, len(doc))):
        try:
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
                        if re.search(r"Quest[õo]es\s+(?:Comentadas|com\s+Coment[áa]rios)", l, re.IGNORECASE):
                            if start_page is None or p_num < start_page:
                                start_page = p_num - 1
                        elif re.search(r"Lista\s+de\s+Quest[õo]es", l, re.IGNORECASE):
                            if end_page is None or p_num < end_page:
                                end_page = p_num - 1
        except Exception:
            pass

    # Fallback varredura direta se necessário
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
        
    # 2. Extração geométrica e semântica estrita
    cleaned_blocks = []
    for p_no in range(start_page, end_page):
        page = doc[p_no]
        for b in page.get_text("blocks"):
            y0, y1, text = b[1], b[3], b[4].strip()
            # Ignora cabeçalhos no topo
            if y1 <= 52:
                continue
            # Ignora rodapés na base
            if y0 >= 740 and ("10341953440" in text or "estrategia" in text.lower() or "cbm-pe" in text.lower() or "pm-pe" in text.lower() or text.isdigit()):
                continue
            # Ignora qualquer bloco contaminante
            if "10341953440" in text or "valério ferreira" in text.lower() or "cursosporprofessor" in text:
                continue
            if not text:
                continue
            # Limpeza preventiva linha a linha
            c_text = clean_lines(text)
            if c_text.strip():
                cleaned_blocks.append(c_text)

    full_text = "\n".join(cleaned_blocks)
    matches = list(TAG_RE.finditer(full_text))
    if not matches:
        return []
        
    # Extrai tópico do nome do arquivo
    file_stem = pdf_path.stem
    topic_match = re.search(r"Aula\s+\d+\s*(?:-\s*)?(?:Prof[^-\n]+-\s*)?(.*)", file_stem, re.IGNORECASE)
    topic_name = topic_match.group(1).strip() if topic_match and topic_match.group(1).strip() else file_stem
    topic_name = re.sub(r"^\d+\.\s*", "", topic_name).strip()
    if not topic_name:
        topic_name = "Geral"

    questions = []
    for i, m in enumerate(matches):
        next_pos = matches[i + 1].start() if i + 1 < len(matches) else len(full_text)
        tag_str = m.group(2)
        body = full_text[m.end():next_pos]
        
        # Se contiver Gabarito no final com assinatura/redes sociais subsequentes, poda o lixo
        gm_body = re.search(r"(Gabarito\s*[:\-–]?\s*(?:Letra|Alternativa|Item)?\s*[A-E]\.?)(.*)", body, flags=re.IGNORECASE | re.DOTALL)
        if gm_body:
            post = gm_body.group(2)
            if any(w in post.lower() for w in ["conclu", "bons estudos", "@prof", "cursosporprofessor", "estrategia", "grande abraço", "forte abraço"]):
                body = body[:gm_body.start() + len(gm_body.group(1))]

        # Parseamento linha a linha de Statement, Alternativas e Comentário
        lines = [ln.rstrip() for ln in body.splitlines()]
        expected = "a"
        alts: list[tuple[str, list[str]]] = []
        stmt_lines: list[str] = []
        after_lines: list[str] = []
        state = "stmt"
        
        for ln in lines:
            m_alt = ALT_LINE.match(ln)
            if state in ("stmt", "alts") and m_alt and m_alt.group(1).lower() == expected:
                state = "alts"
                alts.append((m_alt.group(1).lower(), [m_alt.group(2) or ""]))
                expected = chr(ord(expected) + 1)
                continue
            if state == "alts":
                if COMMENT_RE.match(ln):
                    state = "after"
                    after_lines.append(ln)
                elif ln.strip():
                    alts[-1][1].append(ln.strip())
                continue
            if state == "after":
                after_lines.append(ln)
            else:
                stmt_lines.append(ln)
                
        # Validação de alternativas
        if len(alts) < 4:
            continue
            
        tail = "\n".join(after_lines) if after_lines else ""
        options = {k: clean_lines(re.sub(r"\s+", " ", " ".join(v)).strip()) for k, v in alts}
        
        # Todas as alternativas devem conter texto não-vazio
        if not all(bool(v.strip()) for v in options.values()):
            continue

        # Gabarito oficial
        gm = GAB_RE.search(tail or body)
        if not gm:
            continue
        ans_raw = gm.group(1).upper()
        if ans_raw not in ("A", "B", "C", "D", "E"):
            continue
            
        # O gabarito DEVE pertencer a uma das alternativas existentes
        if ans_raw.lower() not in options:
            continue
            
        statement = clean_lines(re.sub(r"[ \t]+", " ", "\n".join(stmt_lines)).strip())
        if len(statement) < 15:
            continue
            
        # Comentário e explicação
        comment = sanitize_comment(tail)
        explanation = comment if len(comment) > 10 else f"Gabarito oficial: Letra {ans_raw}."
        
        # Banca e metadados
        banca, orgao, ano = parse_banca_and_meta(tag_str)
        
        # Hash de integridade e deduplicação
        norm_st = re.sub(r"\s+", " ", statement.lower())
        opts_str = "|".join(f"{k}:{re.sub(r'\s+', ' ', v.lower())}" for k, v in sorted(options.items()))
        chash = hashlib.sha256(f"{norm_st}::{opts_str}".encode("utf-8")).hexdigest()
        
        formatted_options = []
        for k in sorted(options.keys()):
            formatted_options.append({
                "label": k.upper(),
                "text": options[k],
                "isCorrect": (k.upper() == ans_raw)
            })
            
        questions.append({
            "id": f"{prefix}_{chash[:16]}",
            "contentHash": chash,
            "subjectId": subject_id,
            "topic": topic_name,
            "statement": statement,
            "explanation": explanation,
            "difficulty": 2,
            "pattern": banca,
            "banca": banca,
            "orgao": orgao,
            "ano": ano,
            "status": "APPROVED",
            "options": formatted_options,
            "sourcePdf": pdf_path.name,
        })

    return questions

def process_file_worker(args: tuple[str, str, str]) -> list[dict]:
    pdf_str, subject_id, prefix = args
    return extract_pdf_questions(Path(pdf_str), subject_id, prefix)

def scan_all_materials() -> list[dict]:
    tec_hashes = set()
    tec_path = ROOT / "content" / "questoes_tecconcursos.json"
    if tec_path.exists():
        try:
            tec_data = json.loads(tec_path.read_text(encoding="utf-8"))
            for q in tec_data:
                norm_st = re.sub(r"\s+", " ", q.get("statement", "").lower())
                opts_str = "|".join(f"{opt['label'].lower()}:{re.sub(r'\s+', ' ', opt['text'].lower())}" for opt in sorted(q.get("options", []), key=lambda x: x["label"]))
                thash = hashlib.sha256(f"{norm_st}::{opts_str}".encode("utf-8")).hexdigest()
                tec_hashes.add(thash)
            print(f"[Extrator] {len(tec_hashes)} hashes do TecConcursos carregados para proteção contra duplicatas.")
        except Exception as e:
            print(f"[Extrator] Aviso ao carregar tec hashes: {e}")

    tasks = []
    
    # 1. CBMPE: docs/01-* a docs/16-*
    cbmpe_folders = [f for f in sorted(DOCS_DIR.glob("[0-1]*")) if f.is_dir() and re.match(r"^(0[1-9]|1[0-6])\b", f.name)]
    for folder in cbmpe_folders:
        clean = re.sub(r"^\d+\s*-\s*", "", folder.name)
        clean = re.sub(r"^(?:CBM-PE|CBMP-PE)\s*(\((?:Oficial|Praça)\))?\s*", "", clean).strip()
        subject_id = "direito-constitucional"
        for k, v in FOLDER_TO_SUBJECT.items():
            if k.lower() in clean.lower():
                subject_id = v
                break
        for pdf in sorted(folder.glob("*.pdf")):
            tasks.append((str(pdf), subject_id, "cbmpe"))

    # 2. PMPE: docs/17-* a docs/41-*
    pmpe_folders = [f for f in sorted(DOCS_DIR.glob("[1-4]*")) if f.is_dir() and re.match(r"^(1[7-9]|[2-4]\d)\b", f.name)]
    for folder in pmpe_folders:
        clean = re.sub(r"^\d+\s*-\s*", "", folder.name)
        clean = re.sub(r"^PM-PE\s*(\((?:Oficial|Soldado)\))?\s*", "", clean).strip()
        if "discursiva" in clean.lower():
            continue
        subject_id = "direito-constitucional"
        for k, v in FOLDER_TO_SUBJECT.items():
            if k.lower() in clean.lower():
                subject_id = v
                break
        for pdf in sorted(folder.glob("*.pdf")):
            tasks.append((str(pdf), subject_id, "pmpe"))

    print(f"[Extrator] Disparando extração paralela de {len(tasks)} PDFs...")
    
    all_extracted = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(process_file_worker, tasks)
        for res in results:
            all_extracted.extend(res)
            
    seen_hashes = set(tec_hashes)
    unique_questions = []
    for q in all_extracted:
        chash = q["contentHash"]
        if chash not in seen_hashes:
            seen_hashes.add(chash)
            unique_questions.append(q)

    print(f"[Extrator] Extração concluída:")
    print(f"  -> Total de questões extraídas brutas: {len(all_extracted)}")
    print(f"  -> Total após desduplicação e proteção TecConcursos: {len(unique_questions)}")
    
    return unique_questions

if __name__ == "__main__":
    out_dir = ROOT / "content"
    out_file = out_dir / "questoes_estrategia_cbmpe_pmpe.json"
    qs = scan_all_materials()
    out_file.write_text(json.dumps(qs, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[Extrator] Base salva com sucesso em {out_file}")
