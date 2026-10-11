"""Extrator robusto de questões de cadernos PDF exportados do TecConcursos.

Extrai:
- ID único do TecConcursos (via URL)
- Número de sequência no caderno
- Metadados: Banca (AOCP / Instituto AOCP), Órgão/Concurso, Cargo, Ano
- Disciplina e Assunto originais do TecConcursos
- Enunciado completo (incluindo textos de apoio, itens I, II, III etc.)
- Alternativas (A–E ou Certo/Errado)
- Gabarito oficial pareado da página final de gabarito
- Detecção de questões anuladas / descontinuadas
- Hash de conteúdo para deduplicação idempotente
"""
from __future__ import annotations

import hashlib
import os
import re
import unicodedata
from dataclasses import asdict, dataclass
from pathlib import Path
import fitz  # PyMuPDF


@dataclass
class TecOption:
    label: str  # "A", "B", "C", "D", "E" ou "C", "E"
    text: str


@dataclass
class TecQuestion:
    tec_id: str
    seq_num: int
    banca: str
    concurso: str
    cargo: str
    ano: int | None
    raw_subject: str
    raw_topic: str
    statement: str
    options: list[TecOption]
    gabarito: str  # "A".."E", "Certo", "Errado", "Anulada"
    is_certo_errado: bool
    is_anulada: bool
    source_pdf: str
    content_hash: str

    def to_dict(self) -> dict:
        d = asdict(self)
        return d


def _clean_str(text: str) -> str:
    # Remove caracteres de controle invisíveis e normaliza espaços
    text = re.sub(r"[\xa0\u200b\u200e\u200f]", " ", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def _compute_hash(statement: str, options: list[TecOption]) -> str:
    norm_st = re.sub(r"\s+", " ", statement.strip().lower())
    opts_str = "|".join(f"{o.label}:{re.sub(r'\s+', ' ', o.text.strip().lower())}" for o in options)
    payload = f"{norm_st}::{opts_str}".encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def extract_gabarito_map(doc: fitz.Document) -> tuple[dict[int, str], int]:
    """Localiza a seção de Gabarito nas últimas páginas e extrai o mapa num -> gabarito."""
    gabarito_map: dict[int, str] = {}
    gabarito_start_page: int | None = None

    # Procurar a partir das últimas 6 páginas
    for p_no in range(len(doc) - 1, max(-1, len(doc) - 7), -1):
        txt = doc[p_no].get_text("text")
        if "Gabarito" in txt:
            gabarito_start_page = p_no

    if gabarito_start_page is None:
        # Tentar procurar em todo o documento de trás para frente
        for p_no in range(len(doc) - 1, -1, -1):
            if "Gabarito" in doc[p_no].get_text("text"):
                gabarito_start_page = p_no
                break

    if gabarito_start_page is None:
        return {}, len(doc)

    full_gab_txt = ""
    for p_no in range(gabarito_start_page, len(doc)):
        full_gab_txt += "\n" + doc[p_no].get_text("text")

    # Extrair pares de gabarito: ex. 4008) C, 2468) Errado, 1123) Anulada, 2188) Certo
    for m in re.finditer(r"\b(\d+)\)\s*([A-Za-z]+)", full_gab_txt):
        num = int(m.group(1))
        ans = m.group(2).strip()
        gabarito_map[num] = ans

    return gabarito_map, gabarito_start_page


def extract_lines_from_doc(doc: fitz.Document, end_page: int) -> list[str]:
    """Extrai todas as linhas de texto ordenadas geometricamente até a página de gabarito."""
    all_lines: list[str] = []

    for p_no in range(end_page):
        p = doc[p_no]
        words = p.get_text("words")
        # Ordenar geometricamente: linha y (agrupada em faixas de 3pt) e depois x
        words.sort(key=lambda w: (round(w[1] / 3) * 3, w[0]))

        line_dict: dict[float, list[str]] = {}
        for w in words:
            # Ignorar cabeçalho do PDF no topo (y < 22) e rodapé da página (y > 815)
            if w[1] < 22 or w[1] > 815:
                continue
            line_y = round(w[1] / 3) * 3
            line_dict.setdefault(line_y, []).append(w[4])

        for y in sorted(line_dict.keys()):
            line_str = " ".join(line_dict[y]).strip()
            if line_str:
                all_lines.append(line_str)

    return all_lines


def _parse_metadata(meta_lines: list[str]) -> tuple[str, str, str, int | None, str, str]:
    """Extrai Banca, Concurso, Cargo, Ano, Disciplina e Assunto a partir do bloco de cabeçalho da questão."""
    full_meta = " ".join(meta_lines)

    # Identificar linha de Disciplina - Assunto
    # A linha de disciplina geralmente tem um hífen separando a matéria do assunto
    # e contém palavras como Direito, Português, Matemática, Informática, Biologia, Química etc.
    disc = ""
    assunto = ""
    concurso_str = ""

    # Separar na primeira linha que parece disciplina
    # Padrão: "<Matéria> - <Assunto>"
    found_disc = False
    disc_idx = -1
    for i, line in enumerate(meta_lines):
        if " - " in line:
            # Checar se a primeira parte parece disciplina
            part0 = line.split(" - ")[0].strip()
            # Se não começa com Instituto ou AOCP ou Banca, provavelmente é disciplina
            if not any(part0.startswith(prefix) for prefix in ["Instituto", "AOCP", "FCC", "Cebraspe", "FGV", "Vunesp"]):
                disc = part0
                assunto = " - ".join(line.split(" - ")[1:]).strip()
                disc_idx = i
                found_disc = True
                break

    if not found_disc:
        # Se não achou com " - ", pega a última linha do cabeçalho como assunto
        if len(meta_lines) >= 2:
            disc_idx = len(meta_lines) - 1
            disc = meta_lines[disc_idx]
            assunto = ""
        else:
            disc_idx = -1

    if disc_idx > 0:
        concurso_str = " ".join(meta_lines[:disc_idx])
    elif meta_lines:
        concurso_str = meta_lines[0]

    # Extrair banca de concurso_str
    banca = "AOCP"
    if "instituto aocp" in concurso_str.lower():
        banca = "Instituto AOCP"
    elif "aocp" in concurso_str.lower():
        banca = "AOCP"

    # Extrair ano (4 dígitos)
    ano_match = re.search(r"\b(19\d\d|20\d\d)\b", concurso_str)
    ano = int(ano_match.group(1)) if ano_match else None

    # Cargo e Concurso
    # Formato típico: "Instituto AOCP - Ag (Pref Angra)/Pref Angra/Inclusão Digital/2015"
    cargo = concurso_str
    concurso = concurso_str
    if " - " in concurso_str:
        rest = concurso_str.split(" - ", 1)[1]
        parts = rest.split("/")
        if len(parts) >= 2:
            cargo = parts[0].strip()
            concurso = parts[1].strip()
        else:
            cargo = rest.strip()
            concurso = rest.strip()

    return banca, concurso, cargo, ano, disc, assunto


def parse_question_slice(
    qid: str, lines: list[str], gabarito_map: dict[int, str], source_pdf: str
) -> TecQuestion | None:
    if not lines:
        return None

    # 1. Localizar onde começa a numeração da questão: \b(\d+)\)\s*
    num_line_idx = -1
    seq_num: int | None = None
    statement_start = ""
    for i, l in enumerate(lines):
        m_num = re.match(r"^(\d+)\)\s*(.*)", l)
        if m_num:
            num_line_idx = i
            seq_num = int(m_num.group(1))
            statement_start = m_num.group(2).strip()
            break

    if num_line_idx == -1:
        # Tentar procurar no meio da linha caso o número tenha colado
        for i, l in enumerate(lines):
            m_num = re.search(r"\b(\d+)\)\s*(.*)", l)
            if m_num and int(m_num.group(1)) in gabarito_map:
                num_line_idx = i
                seq_num = int(m_num.group(1))
                statement_start = m_num.group(2).strip()
                break

    if seq_num is None:
        return None

    # Metadados são tudo antes de num_line_idx
    meta_lines = lines[:num_line_idx]
    banca, concurso, cargo, ano, raw_subject, raw_topic = _parse_metadata(meta_lines)

    # 2. Extrair enunciado e alternativas
    body_lines: list[str] = []
    if statement_start:
        body_lines.append(statement_start)

    options_dict: dict[str, list[str]] = {}
    is_ce = False
    opt_started = False
    current_opt_label: str | None = None

    for l in lines[num_line_idx + 1 :]:
        # Checar se é alternativa a), b), c), d), e)
        m_opt = re.match(r"^([a-eA-E])\)\s*(.*)", l)
        if m_opt:
            opt_started = True
            current_opt_label = m_opt.group(1).upper()
            options_dict[current_opt_label] = [m_opt.group(2).strip()]
        elif l.strip() in ["Certo", "Errado"] and not opt_started:
            # Questão do tipo Certo/Errado
            is_ce = True
            opt_started = True
            if l.strip() == "Certo":
                options_dict["C"] = ["Certo"]
            else:
                options_dict["E"] = ["Errado"]
        elif opt_started:
            if is_ce and l.strip() in ["Certo", "Errado"]:
                if l.strip() == "Certo":
                    options_dict["C"] = ["Certo"]
                else:
                    options_dict["E"] = ["Errado"]
            elif current_opt_label:
                options_dict[current_opt_label].append(l.strip())
        else:
            body_lines.append(l)

    # Reconstruir opções em lista ordenada
    options: list[TecOption] = []
    if is_ce:
        # Garantir Certo e Errado como opções
        options = [
            TecOption(label="C", text="Certo"),
            TecOption(label="E", text="Errado"),
        ]
    else:
        for lbl in ["A", "B", "C", "D", "E"]:
            if lbl in options_dict:
                opt_text = " ".join(options_dict[lbl]).strip()
                options.append(TecOption(label=lbl, text=_clean_str(opt_text)))

    statement = _clean_str("\n".join(body_lines))

    # Obter gabarito oficial pareado
    raw_gab = gabarito_map.get(seq_num, "DESCONHECIDO").strip()
    is_anulada = raw_gab.lower() in ["anulada", "desconhecido"]

    # Normalizar gabarito
    gabarito = raw_gab
    if raw_gab.upper() in ["A", "B", "C", "D", "E"]:
        gabarito = raw_gab.upper()
    elif raw_gab.lower() == "certo":
        gabarito = "C" if is_ce else "Certo"
    elif raw_gab.lower() == "errado":
        gabarito = "E" if is_ce else "Errado"

    content_hash = _compute_hash(statement, options)

    return TecQuestion(
        tec_id=qid,
        seq_num=seq_num,
        banca=banca,
        concurso=concurso,
        cargo=cargo,
        ano=ano,
        raw_subject=_clean_str(raw_subject),
        raw_topic=_clean_str(raw_topic),
        statement=statement,
        options=options,
        gabarito=gabarito,
        is_certo_errado=is_ce,
        is_anulada=is_anulada,
        source_pdf=source_pdf,
        content_hash=content_hash,
    )


def extract_questions_from_pdf(pdf_path: str | Path) -> list[TecQuestion]:
    """Extrai todas as questões de um único arquivo PDF do TecConcursos."""
    pdf_path = Path(pdf_path)
    doc = fitz.open(pdf_path)

    gabarito_map, gabarito_start_page = extract_gabarito_map(doc)
    all_lines = extract_lines_from_doc(doc, gabarito_start_page)

    # Segmentar por www.tecconcursos.com.br/questoes/(\d+)
    q_slices: list[tuple[str, list[str]]] = []
    current_q_id: str | None = None
    current_lines: list[str] = []

    for line in all_lines:
        m = re.search(r"www\.tecconcursos\.com\.br/questoes/(\d+)", line)
        if m:
            if current_q_id:
                q_slices.append((current_q_id, current_lines))
            current_q_id = m.group(1)
            current_lines = []
        else:
            if current_q_id:
                current_lines.append(line)

    if current_q_id:
        q_slices.append((current_q_id, current_lines))

    questions: list[TecQuestion] = []
    for qid, lines in q_slices:
        parsed = parse_question_slice(qid, lines, gabarito_map, pdf_path.name)
        if parsed:
            questions.append(parsed)

    return questions


def extract_all_questions_from_dir(directory: str | Path) -> list[TecQuestion]:
    """Extrai todas as questões de todos os PDFs em um diretório com deduplicação por tec_id e content_hash."""
    dir_path = Path(directory)
    pdf_files = sorted(dir_path.glob("*.pdf"))

    seen_tec_ids: set[str] = set()
    seen_hashes: set[str] = set()
    unique_questions: list[TecQuestion] = []

    for pdf in pdf_files:
        qs = extract_questions_from_pdf(pdf)
        for q in qs:
            if q.tec_id in seen_tec_ids or q.content_hash in seen_hashes:
                continue
            seen_tec_ids.add(q.tec_id)
            seen_hashes.add(q.content_hash)
            unique_questions.append(q)

    return unique_questions
