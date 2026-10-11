"""Extrator de Alta Fidelidade e Auditoria Integral de Questões Estratégia (CBMPE e PMPE).

Segunda Auditoria:
1. Recuperação e preservação de destaques visuais:
   - Palavras/termos sublinhados detectados por vetores gráficos (page.get_drawings()) -> <u>termo</u>.
   - Destaques em negrito (flags & 16 / fontes bold) -> **termo**.
   - Destaques em itálico (flags & 2 / fontes italic) -> *termo*.
2. Extração e preservação de figuras, gráficos, tirinhas, circuitos e tabelas:
   - Extrai bounding boxes de imagens (raster ou clips vetoriais em 180 DPI) no intervalo da questão.
   - Salva em web/public/questoes/imagens/<question_id>_<idx>.png.
   - Insere Markdown de imagem: ![Figura da Questão](/questoes/imagens/...).
   - Se questão exige visual indispensável e imagem estiver ausente, marca status: "DRAFT".
3. Separação semântica:
   - Separa referências bibliográficas ("Disponível em:", "Acesso em:", "Fonte:") em bloco de citação `> **Fonte:** ...`.
   - Preserva títulos de texto-base e parágrafos normais.
4. Higienização geométrica estrita:
   - Elimina cabeçalhos (y1 <= 52) e rodapés com CPFs/nomes/URLs no rodapé (y0 >= 730) sem truncar alternativas.
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
IMAGES_DIR = ROOT / "web" / "public" / "questoes" / "imagens"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

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
ALT_LINE = re.compile(r"^[ \t]*(?:\*\*)?\(?([a-eA-E])\)(?:\*\*)?[ \t]+(.*)$")
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
    re.compile(r"(?:Diego\s+Carvalho|Renato\s+da\s+Costa|Equipe\s+Inform[áa]tica|HERBERT\s+ALMEIDA|Vinicius\s+Silva|Darlan\s+Eterno)", re.I),
    re.compile(r"^\d{1,3}\s*$", re.I),
]

VISUAL_REQUIRED_PATTERNS = re.compile(
    r"\b(?:na figura(?:\s+(?:abaixo|a seguir|1|2))?|conforme a figura|no gr[áa]fico(?:\s+(?:abaixo|a seguir))?|na tirinha|no quadrinho|no segundo quadrinho|no primeiro quadrinho|na charge|no circuito(?:\s+el[ée]trico)?|no esquema(?:\s+(?:abaixo|a seguir))?|no diagrama|na imagem abaixo)\b",
    re.IGNORECASE,
)

HIGHLIGHT_REQUIRED_PATTERNS = re.compile(
    r"\b(?:termos?\s+destacados?|express[õo]es?\s+sublinhadas?|palavras?\s+sublinhadas?|voc[áa]bulo\s+destacado|termo\s+sublinhado|destacad[ao]s?|sublinhad[ao]s?)\b",
    re.IGNORECASE,
)

REF_LINE_PATTERN = re.compile(
    r"((?:Dispon[íi]vel\s+em:\s*<?\S+>?\.?\s*)?(?:Acesso\s+em:\s*[^.\n]+(?:\.|$))|Fonte:\s*[^\n]+|\((?:Adaptado|Extra[íi]do|In:)[^)]+\))",
    re.IGNORECASE,
)

def clean_lines(text: str) -> str:
    """Elimina linhas individuais de metadados contaminantes."""
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

def format_rich_page_lines(page: fitz.Page) -> list[dict]:
    """Extrai linhas da página com spans formatados (sublinhado, negrito, itálico) e bboxes."""
    underline_rects = []
    try:
        for d in page.get_drawings():
            r = d["rect"]
            if abs(r.y1 - r.y0) <= 2.8 and (r.x1 - r.x0) >= 5:
                underline_rects.append(r)
    except Exception:
        pass

    try:
        dict_data = page.get_text("dict")
    except Exception:
        return []

    lines_out = []
    for b in dict_data.get("blocks", []):
        if "lines" not in b:
            continue
        by0, by1 = b["bbox"][1], b["bbox"][3]
        if by1 <= 52:
            continue

        # No rodapé (y0 >= 730), só descarta se casar com residual ou dígitos puros
        if by0 >= 730:
            block_text = " ".join(" ".join(s["text"] for s in l["spans"]) for l in b["lines"]).strip()
            if any(pat.search(block_text) for pat in RESIDUAL_LINE_PATTERNS) or block_text.isdigit():
                continue

        for l in b["lines"]:
            ly0, ly1 = l["bbox"][1], l["bbox"][3]
            if ly1 <= 52:
                continue

            # Rodapé por linha
            if ly0 >= 730:
                line_str = " ".join(s["text"] for s in l["spans"]).strip()
                if any(pat.search(line_str) for pat in RESIDUAL_LINE_PATTERNS) or line_str.isdigit():
                    continue

            spans_out = []
            for s in l["spans"]:
                stext = s["text"]
                if not stext:
                    continue

                is_bold = bool(s["flags"] & 16) or any(k in s["font"].lower() for k in ["bold", "black", "heavy", "semibold"])
                is_italic = bool(s["flags"] & 2) or any(k in s["font"].lower() for k in ["italic", "oblique"])

                # Sublinhado por palavra
                words = stext.split(" ")
                total_len = max(len(stext), 1)
                char_w = (s["bbox"][2] - s["bbox"][0]) / total_len
                cur_x = s["bbox"][0]

                word_tokens = []
                for w in words:
                    wx0 = cur_x
                    wx1 = cur_x + len(w) * char_w
                    cur_x = wx1 + char_w

                    w_under = False
                    if len(w) >= 2:
                        for ur in underline_rects:
                            if (s["bbox"][1] - 3 <= ur.y0 <= s["bbox"][3] + 3.5):
                                overlap = max(0, min(wx1, ur.x1) - max(wx0, ur.x0))
                                if overlap >= 0.55 * (wx1 - wx0):
                                    w_under = True
                                    break

                    word_tokens.append((w, w_under, is_bold, is_italic))

                grouped_parts = []
                buf = []
                cur_style = None

                for w, u, b_flag, i_flag in word_tokens:
                    style = ("u" if u else ("b" if b_flag else ("i" if i_flag else "n")))
                    if style != cur_style:
                        if buf:
                            txt = " ".join(buf)
                            if cur_style == "u":
                                grouped_parts.append(f"<u>{txt}</u>")
                            elif cur_style == "b":
                                grouped_parts.append(f"**{txt}**")
                            elif cur_style == "i":
                                grouped_parts.append(f"*{txt}*")
                            else:
                                grouped_parts.append(txt)
                            buf = []
                        cur_style = style
                    buf.append(w)

                if buf:
                    txt = " ".join(buf)
                    if cur_style == "u":
                        grouped_parts.append(f"<u>{txt}</u>")
                    elif cur_style == "b":
                        grouped_parts.append(f"**{txt}**")
                    elif cur_style == "i":
                        grouped_parts.append(f"*{txt}*")
                    else:
                        grouped_parts.append(txt)

                spans_out.append(" ".join(grouped_parts))

            line_text = re.sub(r"[ \t]+", " ", " ".join(spans_out)).strip()
            if line_text:
                lines_out.append({
                    "text": line_text,
                    "bbox": l["bbox"],
                    "y0": ly0,
                    "y1": ly1,
                })

    return lines_out

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
                    if p_num and 3 < p_num <= len(doc):
                        if re.search(r"Quest[õo]es\s+(?:Comentadas|com\s+Coment[áa]rios)", l, re.IGNORECASE):
                            if start_page is None or p_num < start_page:
                                start_page = p_num - 1
                        elif re.search(r"Lista\s+de\s+Quest[õo]es", l, re.IGNORECASE):
                            if end_page is None or p_num < end_page:
                                end_page = p_num - 1
        except Exception:
            pass

    # Fallback varredura direta no texto a partir da pág 4
    if start_page is None:
        for p in range(4, len(doc)):
            txt = doc[p].get_text("text")
            if re.search(r"QUEST[ÕO]ES\s+(?:COMENTADAS|COM\s+COMENT[ÁA]RIOS)", txt, re.IGNORECASE):
                start_page = p
                break

    if end_page is None and start_page is not None:
        for p in range(start_page + 1, len(doc)):
            txt = doc[p].get_text("text")
            if re.search(r"LISTA\s+DE\s+QUEST[ÕO]ES", txt, re.IGNORECASE):
                end_page = p
                break

    if start_page is None:
        return []
    if end_page is None or end_page <= start_page:
        end_page = len(doc)

    # 2. Coleta de páginas e imagens
    page_records = []
    for p_no in range(start_page, end_page):
        page = doc[p_no]
        lines = format_rich_page_lines(page)

        # Imagens da página
        page_imgs = []
        seen_img_rects = set()
        try:
            for img in page.get_images():
                xref = img[0]
                for r in page.get_image_rects(xref):
                    if 52 < r.y0 < 740 and r.width >= 40 and r.height >= 25:
                        rkey = (round(r.x0, 1), round(r.y0, 1), round(r.x1, 1), round(r.y1, 1))
                        if rkey not in seen_img_rects:
                            seen_img_rects.add(rkey)
                            page_imgs.append({"rect": r, "xref": xref})
        except Exception:
            pass

        page_records.append({
            "p_no": p_no,
            "lines": lines,
            "images": page_imgs,
        })

    all_lines: list[dict] = []
    for pr in page_records:
        for ln in pr["lines"]:
            ln["p_no"] = pr["p_no"]
            all_lines.append(ln)

    raw_text_blocks = []
    for ln in all_lines:
        t = clean_lines(ln["text"]).strip()
        if t:
            t_clean = re.sub(r"\*\*\s*\*\*", " ", t)
            t_clean = re.sub(r"^(?:\*\*)?(\d{1,3})\.(?:\*\*)?\s*(?:\*\*)?\(\s*([^()]{3,120}?)\s*\)(?:\*\*)?", r"\1. (\2)", t_clean)
            raw_text_blocks.append(t_clean)

    full_text = "\n".join(raw_text_blocks)
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

        # Poda redes sociais no final
        gm_body = re.search(r"(Gabarito\s*[:\-–]?\s*(?:Letra|Alternativa|Item)?\s*[A-E]\.?)(.*)", body, flags=re.IGNORECASE | re.DOTALL)
        if gm_body:
            post = gm_body.group(2)
            if any(w in post.lower() for w in ["conclu", "bons estudos", "@prof", "cursosporprofessor", "estrategia", "grande abraço", "forte abraço"]):
                body = body[:gm_body.start() + len(gm_body.group(1))]

        # Parseamento linha a linha
        lines = [ln.rstrip() for ln in body.splitlines()]
        expected = "a"
        alts: list[tuple[str, list[str]]] = []
        stmt_lines: list[str] = []
        after_lines: list[str] = []
        state = "stmt"

        for ln in lines:
            clean_ln = re.sub(r"\*+", "", ln).strip()
            m_alt = ALT_LINE.match(ln)
            if state in ("stmt", "alts") and m_alt and m_alt.group(1).lower() == expected:
                state = "alts"
                alts.append((m_alt.group(1).lower(), [m_alt.group(2) or ""]))
                expected = chr(ord(expected) + 1)
                continue
            if state == "alts":
                if COMMENT_RE.match(clean_ln):
                    state = "after"
                    after_lines.append(ln)
                elif ln.strip():
                    alts[-1][1].append(ln.strip())
                continue
            if state == "after":
                after_lines.append(ln)
            else:
                stmt_lines.append(ln)

        if len(alts) < 4:
            continue

        tail = "\n".join(after_lines) if after_lines else ""
        options = {k: clean_lines(re.sub(r"\s+", " ", " ".join(v)).strip()) for k, v in alts}

        if not all(bool(v.strip()) for v in options.values()):
            continue

        clean_search_target = re.sub(r"\*+", "", tail or body)
        gm = GAB_RE.search(clean_search_target)
        if not gm:
            continue
        ans_raw = gm.group(1).upper()
        if ans_raw not in ("A", "B", "C", "D", "E"):
            continue

        if ans_raw.lower() not in options:
            continue

        statement_raw = clean_lines(re.sub(r"[ \t]+", " ", "\n".join(stmt_lines)).strip())
        if len(statement_raw) < 15:
            continue

        # Separação de referências bibliográficas em citação
        ref_match = REF_LINE_PATTERN.search(statement_raw)
        if ref_match:
            ref_text = ref_match.group(1).strip()
            statement_raw = statement_raw.replace(ref_match.group(0), f"\n\n> **Fonte:** {ref_text}\n\n")

        comment = sanitize_comment(tail)
        explanation = comment if len(comment) > 10 else f"Gabarito oficial: Letra {ans_raw}."

        norm_st = re.sub(r"\s+", " ", statement_raw.lower())
        opts_str = "|".join(f"{k}:{re.sub(r'\s+', ' ', v.lower())}" for k, v in sorted(options.items()))
        chash = hashlib.sha256(f"{norm_st}::{opts_str}".encode("utf-8")).hexdigest()
        qid = f"{prefix}_{chash[:16]}"

        # 3. Associação Geométrica de Imagens
        tag_match_str = f"{m.group(1)}. ({tag_str})"
        start_ln = next((ln for ln in all_lines if tag_match_str in ln["text"] or f"{m.group(1)}." in ln["text"]), None)
        
        associated_images = []
        if start_ln:
            q_pno = start_ln["p_no"]
            q_y0 = start_ln["y0"]
            
            next_m = matches[i + 1] if i + 1 < len(matches) else None
            next_pno = page_records[-1]["p_no"]
            next_y0 = 740.0
            if next_m:
                next_tag = f"{next_m.group(1)}. ({next_m.group(2)})"
                next_ln = next((ln for ln in all_lines if next_tag in ln["text"] or f"{next_m.group(1)}." in ln["text"]), None)
                if next_ln:
                    next_pno = next_ln["p_no"]
                    next_y0 = next_ln["y0"]

            for pr in page_records:
                if pr["p_no"] < q_pno or pr["p_no"] > next_pno:
                    continue
                for idx_img, img_item in enumerate(pr["images"]):
                    ir = img_item["rect"]
                    if pr["p_no"] == q_pno and ir.y1 < q_y0 - 5:
                        continue
                    if pr["p_no"] == next_pno and ir.y0 > next_y0 + 5:
                        continue

                    img_filename = f"{qid}_{pr['p_no']}_{idx_img}.png"
                    img_dest = IMAGES_DIR / img_filename
                    if not img_dest.exists():
                        try:
                            p_obj = doc[pr["p_no"]]
                            clip_r = fitz.Rect(max(0, ir.x0 - 2), max(0, ir.y0 - 2), min(p_obj.rect.width, ir.x1 + 2), min(p_obj.rect.height, ir.y1 + 2))
                            pix = p_obj.get_pixmap(clip=clip_r, dpi=180)
                            pix.save(str(img_dest))
                        except Exception:
                            pass

                    if img_dest.exists():
                        associated_images.append(f"/questoes/imagens/{img_filename}")

        statement = statement_raw
        if associated_images:
            img_markdowns = "\n\n".join(f"![Figura da Questão]({url})" for url in associated_images)
            statement = f"{statement}\n\n{img_markdowns}"

        # 4. Avaliação de Status (APPROVED vs DRAFT)
        requires_visual = bool(VISUAL_REQUIRED_PATTERNS.search(statement))
        requires_highlight = bool(HIGHLIGHT_REQUIRED_PATTERNS.search(statement))
        has_highlight = "<u>" in statement or "**" in statement

        status = "APPROVED"
        if requires_visual and not associated_images:
            status = "DRAFT"
        elif requires_highlight and not has_highlight:
            citacao = re.search(r'(?:voc[áa]bulo|termo|palavra|express[ão]o)\s+["“]([^"”]+)["”]', explanation, re.IGNORECASE)
            if citacao and citacao.group(1) in statement:
                termo = citacao.group(1)
                statement = statement.replace(termo, f"<u>{termo}</u>", 1)
                status = "APPROVED"
            else:
                status = "DRAFT"

        banca, orgao, ano = parse_banca_and_meta(tag_str)

        formatted_options = []
        for k in sorted(options.keys()):
            formatted_options.append({
                "label": k.upper(),
                "text": options[k],
                "isCorrect": (k.upper() == ans_raw)
            })

        questions.append({
            "id": qid,
            "contentHash": chash,
            "subjectId": subject_id,
            "topic": topic_name,
            "support": None,
            "statement": statement,
            "explanation": explanation,
            "difficulty": 2,
            "pattern": banca,
            "banca": banca,
            "orgao": orgao,
            "ano": ano,
            "status": status,
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

    print(f"[Extrator] Disparando extração de alta fidelidade de {len(tasks)} PDFs...")

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
    approved_count = sum(1 for q in unique_questions if q["status"] == "APPROVED")
    draft_count = sum(1 for q in unique_questions if q["status"] == "DRAFT")
    with_img_count = sum(1 for q in unique_questions if "![" in q["statement"])
    with_underline = sum(1 for q in unique_questions if "<u>" in q["statement"])
    print(f"  -> Questões APPROVED: {approved_count}")
    print(f"  -> Questões DRAFT (sob revisão/figura faltante): {draft_count}")
    print(f"  -> Questões com Figuras/Imagens associadas: {with_img_count}")
    print(f"  -> Questões com Sublinhado <u> preservado: {with_underline}")

    return unique_questions

if __name__ == "__main__":
    out_dir = ROOT / "content"
    out_file = out_dir / "questoes_estrategia_cbmpe_pmpe.json"
    qs = scan_all_materials()
    out_file.write_text(json.dumps(qs, ensure_ascii=False, indent=2), encoding="utf-8")
    
    web_file = ROOT / "web" / "content" / "questoes_estrategia_cbmpe_pmpe.json"
    if web_file.parent.exists():
        web_file.write_text(json.dumps(qs, ensure_ascii=False, indent=2), encoding="utf-8")
        
    print(f"[Extrator] Base salva com sucesso em {out_file} e {web_file}")
