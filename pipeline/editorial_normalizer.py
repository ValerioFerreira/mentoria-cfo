"""Normalizador Editorial de Alta Precisão para o Acervo de Questões.

Resolve:
1. Eliminação de asteriscos espúrios (** linha a linha, ** desbalanceados, ** ** vazios).
2. Preservação seletiva de negrito semântico (EXCETO, CORRETO, assertivas I/II/III, termos destacados).
3. Desfazimento de quebras de linha artificiais do PDF e junção de translineação com hífen.
4. Desassociação de imagens espúrias (ícones/banners) em questões que não citam figuras.
5. Validação rigorosa de imagens em questões visuais (com marcação DRAFT se faltante).
6. Preservação de tags <u>sublinhado</u> e citações > **Fonte:**.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG_DIR = ROOT / "web" / "public" / "questoes" / "imagens"

VISUAL_KEYWORDS = re.compile(
    r"\b(?:figura|gr[áa]fico|tirinha|quadrinho|charge|circuito|esquema|tabela|diagrama|mapa|imagem|ilustra[çc][ãa]o|foto)\b",
    re.IGNORECASE,
)

HIGHLIGHT_KEYWORDS = re.compile(
    r"\b(?:termos?\s+destacados?|express[õo]es?\s+sublinhadas?|palavras?\s+sublinhadas?|voc[áa]bulo\s+destacado|termo\s+sublinhado|destacad[ao]s?|sublinhad[ao]s?)\b",
    re.IGNORECASE,
)

# Termos que legitimamente devem ter negrito se encontrados
SEMANTIC_BOLD_TERMS = [
    "EXCETO", "CORRETO", "INCORRETO", "NÃO", "VERDADEIRO", "FALSO",
    "APENAS", "SOMENTE", "ERRADO", "CERTO", "I", "II", "III", "IV", "V",
]

def normalize_text_breaks_and_hyphens(text: str) -> str:
    """Desfaz quebras artificiais de linha e resolve hífens de translineação."""
    if not text:
        return ""

    # 1. Unir hífens de translineação: palavra-\ncontinuação
    # Ex: 'recém-\nexpedida' -> 'recém-expedida', 'admi-\nnistrativo' -> 'administrativo'
    def fix_hyphen(m: re.Match) -> str:
        w1 = m.group(1)
        w2 = m.group(2)
        # Se for prefixo clássico com hífen, mantém hífen
        if w1.lower() in ("recém", "pós", "pré", "pró", "vice", "sub", "super", "auto"):
            return f"{w1}-{w2}"
        return f"{w1}{w2}"

    text = re.sub(r"([a-zA-ZáéíóúâêîôûãõçÁÉÍÓÚÂÊÎÔÛÃÕÇ]+)-\s*\n\s*([a-zA-ZáéíóúâêîôûãõçÁÉÍÓÚÂÊÎÔÛÃÕÇ]+)", fix_hyphen, text)

    # 2. Separar em blocos por quebras duplas reais
    blocks = re.split(r"\n\s*\n", text)
    cleaned_blocks = []

    for block in blocks:
        lines = [l.strip() for l in block.splitlines() if l.strip()]
        if not lines:
            continue

        # Se for bloco de lista/assertivas numeradas ou citação, processa linha a linha
        if any(re.match(r"^(?:[-*]|\(?\d+\)?|\(?[a-eA-E]\)?|[I|V|X]+\.|\>)", ln) for ln in lines):
            cleaned_blocks.append("\n".join(lines))
            continue

        # Caso contrário, unifica as linhas do mesmo parágrafo com espaço
        joined_paragraph = " ".join(lines)
        # Normaliza espaços múltiplos
        joined_paragraph = re.sub(r"[ \t]+", " ", joined_paragraph)
        cleaned_blocks.append(joined_paragraph)

    return "\n\n".join(cleaned_blocks)

def clean_spurious_markdown_bold(text: str) -> str:
    """Remove marcações ** que envelopam o texto inteiro ou sobram soltas."""
    if not text:
        return ""

    # Remove asteriscos vazios
    text = re.sub(r"\*\*\s*\*\*", " ", text)

    # Se um parágrafo começa e termina com ** cobrindo mais de 80% do texto
    # (ruído de fonte do PDF onde o parágrafo todo estava em SemiBold)
    paragraphs = text.split("\n\n")
    cleaned_paras = []

    for p in paragraphs:
        p_strip = p.strip()
        # Se o parágrafo inteiro está entre **...**
        if p_strip.startswith("**") and p_strip.endswith("**") and p_strip.count("**") == 2:
            inner = p_strip[2:-2].strip()
            # Se for frase longa (> 40 chars), é texto normal e não destaque semântico
            if len(inner) > 40:
                p_strip = inner

        # Se houver asteriscos no início/fim de linhas individuais
        # Remove asterisco solto no início ou final do parágrafo
        if p_strip.startswith("**") and p_strip.count("**") % 2 != 0:
            p_strip = p_strip[2:].strip()
        if p_strip.endswith("**") and p_strip.count("**") % 2 != 0:
            p_strip = p_strip[:-2].strip()

        # Se ainda houver asteriscos desbalanceados dentro do parágrafo
        if p_strip.count("**") % 2 != 0:
            # Remove todos os asteriscos soltos desse parágrafo
            p_strip = p_strip.replace("**", "")

        # Preserva destaques semânticos de palavras-chave
        for term in SEMANTIC_BOLD_TERMS:
            # Destaca se estiver em caixa alta isolado e não já marcado
            pattern = rf"\b({term})\b"
            # Substitui por **TERM** apenas se for termo isolado sem tags
            if re.search(pattern, p_strip) and f"**{term}**" not in p_strip:
                p_strip = re.sub(pattern, rf"**\1**", p_strip, count=1)

        cleaned_paras.append(p_strip)

    result = "\n\n".join(cleaned_paras)
    # Remove qualquer duplo espaço remanescente
    result = re.sub(r"[ \t]+", " ", result)
    return result.strip()

def process_question_editorial(q: dict) -> tuple[dict, list[str]]:
    """Aplica o fluxo editorial completo a uma questão, registrando alterações."""
    changes = []
    st_orig = q.get("statement", "")
    subj = q.get("subjectId", "")
    qid = q.get("id", "")

    # 1. Separar imagens existentes
    existing_imgs = re.findall(r"!\[(.*?)\]\((/questoes/imagens/[^)]+)\)", st_orig)
    text_without_imgs = re.sub(r"\n*!\[(.*?)\]\((/questoes/imagens/[^)]+)\)\n*", "\n\n", st_orig).strip()

    # 2. Normalizar quebras e hífens
    text_normalized = normalize_text_breaks_and_hyphens(text_without_imgs)
    if text_normalized != text_without_imgs:
        changes.append("normalizacao_quebras_e_hifens")

    # 3. Limpeza de asteriscos espúrios
    text_cleaned = clean_spurious_markdown_bold(text_normalized)
    if text_cleaned != text_normalized:
        changes.append("limpeza_asteriscos_espurios")

    # 4. Avaliação e Filtragem de Imagens
    has_visual_ref = bool(VISUAL_KEYWORDS.search(text_cleaned))
    is_visual_subject = subj in ("fisica", "informatica", "quimica", "biologia", "matematica")

    valid_imgs = []
    removed_imgs = []

    for alt, url in existing_imgs:
        fn = url.replace("/questoes/imagens/", "")
        fpath = IMG_DIR / fn
        file_exists = fpath.exists() and fpath.stat().st_size > 500

        # Para matérias de Direito / Legislação:
        # Se NÃO há menção a figura, descarta imagem espúria
        if subj in ("direito-administrativo", "direito-constitucional", "direito-penal-militar", "legislacoes-pe", "historia-pe"):
            if not has_visual_ref:
                removed_imgs.append(url)
                continue

        if file_exists and (has_visual_ref or is_visual_subject):
            valid_imgs.append((alt, url))
        else:
            removed_imgs.append(url)

    if removed_imgs:
        changes.append(f"removidas_{len(removed_imgs)}_imagens_espurias")

    # 5. Recomposição do Statement
    if valid_imgs:
        img_mds = "\n\n".join(f"![{alt or 'Figura da Questão'}]({url})" for alt, url in valid_imgs)
        final_statement = f"{text_cleaned}\n\n{img_mds}"
    else:
        final_statement = text_cleaned

    # 6. Avaliação de Status (APPROVED vs DRAFT)
    status = "APPROVED"
    if has_visual_ref and not valid_imgs:
        status = "DRAFT"
        changes.append("marcado_draft_visual_ausente")

    # Checar termos destacados
    if HIGHLIGHT_KEYWORDS.search(final_statement):
        if "<u>" not in final_statement and "**" not in final_statement:
            # Tentar recuperar do comentário
            exp = q.get("explanation", "")
            citacao = re.search(r'(?:voc[áa]bulo|termo|palavra|express[ão]o)\s+["“]([^"”]+)["”]', exp, re.IGNORECASE)
            if citacao and citacao.group(1) in final_statement:
                t = citacao.group(1)
                final_statement = final_statement.replace(t, f"<u>{t}</u>", 1)
                changes.append(f"destaque_recuperado_do_comentario_{t}")
            else:
                status = "DRAFT"
                changes.append("marcado_draft_destaque_ausente")

    # 7. Normalizar texto das alternativas
    normalized_options = []
    for opt in q.get("options", []):
        opt_text = opt.get("text", "")
        opt_clean = normalize_text_breaks_and_hyphens(opt_text)
        opt_clean = clean_spurious_markdown_bold(opt_clean)
        normalized_options.append({
            "label": opt["label"],
            "text": opt_clean,
            "isCorrect": opt.get("isCorrect", False),
        })

    # Atualiza questão
    updated_q = dict(q)
    updated_q["statement"] = final_statement
    updated_q["options"] = normalized_options
    updated_q["status"] = status

    return updated_q, changes
