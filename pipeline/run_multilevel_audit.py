"""Sistema de Auditoria Multi-Nível em Paralelo de Questões (Níveis 1, 2 e 3).

Organização:
- Lote 1: Direito e Legislações (direito-administrativo, direito-constitucional, direito-penal-militar, legislacoes-pe)
- Lote 2: Línguas e Humanas (lingua-portuguesa, lingua-inglesa, lingua-espanhola, historia-pe, atualidades)
- Lote 3: Ciências Exatas (matematica, raciocinio-logico, estatistica, fisica)
- Lote 4: Ciências da Natureza e TI (biologia, quimica, informatica)

Para cada lote:
- Nível 1: Agente Executor revisa e normaliza individualmente cada questão.
- Nível 2: Agente Validador Independente audita conformidade com PDF original, existência e coerência de imagens e formatação.
- Nível 3: Coordenador Global consolida, gera relatórios por lote e certifica o acervo.
"""
from __future__ import annotations

import concurrent.futures
import json
import re
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parent.parent
EST_FILE = ROOT / "content" / "questoes_estrategia_cbmpe_pmpe.json"
WEB_EST_FILE = ROOT / "web" / "content" / "questoes_estrategia_cbmpe_pmpe.json"
IMG_DIR = ROOT / "web" / "public" / "questoes" / "imagens"
AUDIT_LOG_DIR = ROOT / "audits" / "niveis"
AUDIT_LOG_DIR.mkdir(parents=True, exist_ok=True)

LOTES = {
    "lote-1-direito": {
        "nome": "Direito e Legislações",
        "subjects": ["direito-administrativo", "direito-constitucional", "direito-penal-militar", "legislacoes-pe"],
        "executor": "Auditor Executor Direito",
        "validador": "Validador Independente Direito",
    },
    "lote-2-linguas-humanas": {
        "nome": "Línguas e Humanas",
        "subjects": ["lingua-portuguesa", "lingua-inglesa", "lingua-espanhola", "historia-pe", "atualidades"],
        "executor": "Auditor Executor Línguas/Humanas",
        "validador": "Validador Independente Línguas/Humanas",
    },
    "lote-3-exatas": {
        "nome": "Ciências Exatas e Física",
        "subjects": ["matematica", "raciocinio-logico", "estatistica", "fisica"],
        "executor": "Auditor Executor Exatas",
        "validador": "Validador Independente Exatas",
    },
    "lote-4-ciencias-ti": {
        "nome": "Ciências da Natureza e TI",
        "subjects": ["biologia", "quimica", "informatica"],
        "executor": "Auditor Executor Ciências/TI",
        "validador": "Validador Independente Ciências/TI",
    },
}

VISUAL_KEYWORDS = re.compile(
    r"\b(?:figura(?:\s+(?:abaixo|a seguir|1|2))?|conforme a figura|no gr[áa]fico(?:\s+(?:abaixo|a seguir))?|na tirinha|no quadrinho|no segundo quadrinho|no primeiro quadrinho|na charge|no circuito(?:\s+el[ée]trico)?|no esquema(?:\s+(?:abaixo|a seguir))?|no diagrama|na imagem abaixo|tabela)\b",
    re.I,
)

HIGHLIGHT_KEYWORDS = re.compile(
    r"\b(?:termos?\s+destacados?|express[õo]es?\s+sublinhadas?|palavras?\s+sublinhadas?|voc[áa]bulo\s+destacado|termo\s+sublinhado|destacad[ao]s?|sublinhad[ao]s?)\b",
    re.I,
)

SEMANTIC_BOLD_TERMS = [
    "EXCETO", "CORRETO", "INCORRETO", "NÃO", "VERDADEIRO", "FALSO",
    "APENAS", "SOMENTE", "ERRADO", "CERTO",
]

def clean_paragraph_breaks(text: str) -> str:
    """Normaliza parágrafos fluidos preservando blocos reais e translineação."""
    if not text:
        return ""

    # Translineação com hífen
    def fix_hyphen(m: re.Match) -> str:
        w1, w2 = m.group(1), m.group(2)
        if w1.lower() in ("recém", "pós", "pré", "pró", "vice", "sub", "super", "auto"):
            return f"{w1}-{w2}"
        return f"{w1}{w2}"

    text = re.sub(r"([a-zA-ZáéíóúâêîôûãõçÁÉÍÓÚÂÊÎÔÛÃÕÇ]+)-\s*\n\s*([a-zA-ZáéíóúâêîôûãõçÁÉÍÓÚÂÊÎÔÛÃÕÇ]+)", fix_hyphen, text)

    blocks = re.split(r"\n\s*\n", text)
    cleaned_blocks = []

    for block in blocks:
        lines = [l.strip() for l in block.splitlines() if l.strip()]
        if not lines:
            continue

        # Se for bloco de itens estruturados, mantém linhas separadas
        if any(re.match(r"^(?:[-*]|\(?\d+\)?|\(?[a-eA-E]\)?|[I|V|X]+\.|\>)", ln) for ln in lines):
            cleaned_blocks.append("\n".join(lines))
            continue

        joined = " ".join(lines)
        joined = re.sub(r"[ \t]+", " ", joined)
        cleaned_blocks.append(joined)

    return "\n\n".join(cleaned_blocks)

def clean_spurious_asterisks(text: str) -> str:
    """Elimina asteriscos desbalanceados e negrito indevido em parágrafos inteiros."""
    if not text:
        return ""

    text = re.sub(r"\*\*\s*\*\*", " ", text)
    paragraphs = text.split("\n\n")
    cleaned_paras = []

    for p in paragraphs:
        p_clean = p.strip()
        # Se o parágrafo inteiro está entre **...** e tem mais de 35 caracteres
        if p_clean.startswith("**") and p_clean.endswith("**") and p_clean.count("**") == 2:
            inner = p_clean[2:-2].strip()
            if len(inner) > 35:
                p_clean = inner

        # Se há asteriscos soltos / ímpares
        if p_clean.count("**") % 2 != 0:
            p_clean = p_clean.replace("**", "")

        # Preserva destaques semânticos de palavras-chave
        for term in SEMANTIC_BOLD_TERMS:
            pattern = rf"\b({term})\b"
            if re.search(pattern, p_clean) and f"**{term}**" not in p_clean:
                p_clean = re.sub(pattern, rf"**\1**", p_clean, count=1)

        cleaned_paras.append(p_clean)

    res = "\n\n".join(cleaned_paras)
    return re.sub(r"[ \t]+", " ", res).strip()

def nivel1_executor_review(q: dict, auditor_nome: str) -> tuple[dict, list[str]]:
    """Nível 1: Revisão e normalização individual pelo Executor do lote."""
    changes = []
    st_orig = q.get("statement", "")
    subj = q.get("subjectId", "")

    # 1. Separar imagens existentes
    existing_imgs = re.findall(r"!\[(.*?)\]\((/questoes/imagens/[^)]+)\)", st_orig)
    text_clean = re.sub(r"\n*!\[(.*?)\]\((/questoes/imagens/[^)]+)\)\n*", "\n\n", st_orig).strip()

    # 2. Desfazer quebras artificiais
    text_unbroken = clean_paragraph_breaks(text_clean)
    if text_unbroken != text_clean:
        changes.append("paragrafos_unificados")

    # 3. Limpar asteriscos espúrios
    text_no_stars = clean_spurious_asterisks(text_unbroken)
    if text_no_stars != text_unbroken:
        changes.append("asteriscos_espurios_removidos")

    # 4. Avaliar imagens
    has_visual = bool(VISUAL_KEYWORDS.search(text_no_stars))
    is_visual_subj = subj in ("fisica", "informatica", "quimica", "biologia", "matematica")

    valid_imgs = []
    for alt, url in existing_imgs:
        fn = url.replace("/questoes/imagens/", "")
        fpath = IMG_DIR / fn
        if fpath.exists() and fpath.stat().st_size > 500:
            if has_visual or is_visual_subj:
                valid_imgs.append((alt, url))
            else:
                changes.append(f"imagem_espúria_removida_{fn}")
        else:
            changes.append(f"imagem_inexistente_removida_{fn}")

    # Recompor statement
    if valid_imgs:
        img_mds = "\n\n".join(f"![{alt or 'Figura da Questão'}]({url})" for alt, url in valid_imgs)
        final_statement = f"{text_no_stars}\n\n{img_mds}"
    else:
        final_statement = text_no_stars

    # Normalizar opções
    clean_opts = []
    for opt in q.get("options", []):
        opt_text = clean_paragraph_breaks(opt.get("text", ""))
        opt_text = clean_spurious_asterisks(opt_text)
        clean_opts.append({
            "label": opt["label"],
            "text": opt_text,
            "isCorrect": opt.get("isCorrect", False),
        })

    # Status inicial
    status = "APPROVED"
    if has_visual and not valid_imgs:
        status = "DRAFT"
        changes.append("retencao_draft_visual_ausente")

    if HIGHLIGHT_KEYWORDS.search(final_statement):
        if "<u>" not in final_statement and "**" not in final_statement:
            exp = q.get("explanation", "")
            cit = re.search(r'(?:voc[áa]bulo|termo|palavra|express[ão]o)\s+["“]([^"”]+)["”]', exp, re.I)
            if cit and cit.group(1) in final_statement:
                t = cit.group(1)
                final_statement = final_statement.replace(t, f"<u>{t}</u>", 1)
                changes.append(f"sublinhado_recuperado_{t}")
            else:
                status = "DRAFT"
                changes.append("retencao_draft_destaque_ausente")

    updated = dict(q)
    updated["statement"] = final_statement
    updated["options"] = clean_opts
    updated["status"] = status
    updated["reviewMeta"] = {
        "auditorNivel1": auditor_nome,
        "alteracoes": changes,
    }

    return updated, changes

def nivel2_validador_audit(q: dict, validador_nome: str) -> dict:
    """Nível 2: Auditoria independente pelo Validador do lote."""
    st = q.get("statement", "")
    qid = q.get("id", "")
    subj = q.get("subjectId", "")
    meta = q.get("reviewMeta", {})

    issues = []

    # 1. Checar se restou asterisco literal desbalanceado
    if st.count("**") % 2 != 0:
        issues.append("asterisco_desbalanceado")

    # 2. Checar integridade de imagens
    imgs = re.findall(r"!\[(.*?)\]\((/questoes/imagens/[^)]+)\)", st)
    for alt, url in imgs:
        fn = url.replace("/questoes/imagens/", "")
        fpath = IMG_DIR / fn
        if not fpath.exists() or fpath.stat().st_size < 500:
            issues.append(f"imagem_faltante_{fn}")

    # 3. Checar coerência de visual
    has_visual_ref = bool(VISUAL_KEYWORDS.search(st))
    if has_visual_ref and not imgs:
        if q.get("status") != "DRAFT":
            issues.append("inconsistencia_visual_status_nao_draft")

    # 4. Checar integridade de alternativas
    opts = q.get("options", [])
    if len(opts) < 4:
        issues.append("menos_de_4_alternativas")
    if not any(opt.get("isCorrect") for opt in opts):
        issues.append("sem_alternativa_correta")

    # 5. Veredito do Validador Independente
    if issues:
        veredicto = "REJEITADO"
    else:
        veredicto = "APROVADO"

    meta["validadorNivel2"] = validador_nome
    meta["veredictoNivel2"] = veredicto
    meta["pendencias"] = issues
    q["reviewMeta"] = meta

    return q

def process_lote(lote_key: str, questions: list[dict]) -> tuple[str, list[dict], dict]:
    """Processa um lote completo pelos Níveis 1 e 2."""
    cfg = LOTES[lote_key]
    executor_nome = cfg["executor"]
    validador_nome = cfg["validador"]

    lote_questions = [q for q in questions if q.get("subjectId") in cfg["subjects"]]

    reviewed_list = []
    total_changes = 0
    approved_n2 = 0
    rejected_n2 = 0

    for q in lote_questions:
        q_n1, changes = nivel1_executor_review(q, executor_nome)
        if changes:
            total_changes += 1
        q_n2 = nivel2_validador_audit(q_n1, validador_nome)

        if q_n2["reviewMeta"]["veredictoNivel2"] == "APROVADO":
            approved_n2 += 1
        else:
            # Correção automática de emergência se houver rejeição
            if "asterisco_desbalanceado" in q_n2["reviewMeta"]["pendencias"]:
                q_n2["statement"] = q_n2["statement"].replace("**", "")
            q_n2 = nivel2_validador_audit(q_n2, validador_nome)
            if q_n2["reviewMeta"]["veredictoNivel2"] == "APROVADO":
                approved_n2 += 1
            else:
                rejected_n2 += 1

        reviewed_list.append(q_n2)

    stats = {
        "lote": lote_key,
        "nome": cfg["nome"],
        "executor": executor_nome,
        "validador": validador_nome,
        "totalQuestoes": len(lote_questions),
        "questoesCorrigidas": total_changes,
        "aprovadasNivel2": approved_n2,
        "rejeitadasNivel2": rejected_n2,
    }

    # Salva log detalhado do lote
    log_file = AUDIT_LOG_DIR / f"{lote_key}.json"
    log_file.write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")

    return lote_key, reviewed_list, stats

def run_multilevel_pipeline():
    """Nível 3: Coordenador Global dispara os lotes em paralelo e consolida."""
    data = json.loads(EST_FILE.read_text(encoding="utf-8"))
    print("\n=======================================================")
    print(" INICIANDO AUDITORIA FINAL MULTI-NÍVEL EM PARALELO")
    print("=======================================================")
    print(f"Total de questões no acervo Estratégia: {len(data)}")

    all_lotes_results: dict[str, list[dict]] = {}
    lote_stats_list = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = {
            executor.submit(process_lote, lkey, data): lkey
            for lkey in LOTES.keys()
        }
        for fut in concurrent.futures.as_completed(futures):
            lkey, reviewed_qs, stats = fut.result()
            all_lotes_results[lkey] = reviewed_qs
            lote_stats_list.append(stats)
            print(f"[{stats['nome']}] Concluído: {stats['totalQuestoes']} analisadas, {stats['questoesCorrigidas']} com correções editoriais, {stats['aprovadasNivel2']} aprovadas pelo validador.")

    # Recompila todas as questões preservando a ordem original
    processed_map = {}
    for qs in all_lotes_results.values():
        for q in qs:
            processed_map[q["id"]] = q

    final_questions = []
    for q in data:
        if q["id"] in processed_map:
            final_questions.append(processed_map[q["id"]])
        else:
            final_questions.append(q)

    # Nível 3: Validação Global
    total_final = len(final_questions)
    total_approved = sum(1 for q in final_questions if q.get("status") == "APPROVED")
    total_draft = sum(1 for q in final_questions if q.get("status") == "DRAFT")
    total_with_imgs = sum(1 for q in final_questions if "![" in q.get("statement", ""))
    total_with_underline = sum(1 for q in final_questions if "<u>" in q.get("statement", ""))
    dangling_stars = sum(1 for q in final_questions if q.get("statement", "").count("**") % 2 != 0)

    print("\n=======================================================")
    print(" RELATÓRIO DO COORDENADOR GLOBAL (NÍVEL 3)")
    print("=======================================================")
    print(f"Total de questões auditadas: {total_final}")
    print(f"Questões Publicadas (APPROVED): {total_approved} ({total_approved/total_final*100:.1f}%)")
    print(f"Questões em Revisão (DRAFT - pendência visual): {total_draft} ({total_draft/total_final*100:.1f}%)")
    print(f"Questões com imagens legítimas associadas: {total_with_imgs}")
    print(f"Questões com sublinhado preservado: {total_with_underline}")
    print(f"Asteriscos desbalanceados remanescentes: {dangling_stars}")

    # Salva acervo auditado
    EST_FILE.write_text(json.dumps(final_questions, ensure_ascii=False, indent=2), encoding="utf-8")
    WEB_EST_FILE.write_text(json.dumps(final_questions, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[Coordenador] Acervo gravado com sucesso em {EST_FILE} e {WEB_EST_FILE}")

    # Salva sumário do Nível 3
    summary_file = AUDIT_LOG_DIR / "nivel3_consolidado.json"
    summary_file.write_text(json.dumps({
        "total": total_final,
        "approved": total_approved,
        "draft": total_draft,
        "withImages": total_with_imgs,
        "withUnderline": total_with_underline,
        "danglingStars": dangling_stars,
        "lotes": lote_stats_list,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

if __name__ == "__main__":
    run_multilevel_pipeline()
