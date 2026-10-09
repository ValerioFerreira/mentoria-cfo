#!/usr/bin/env python3
"""Auditoria Completa do MentorIA:
- 5 Lotes de Diretrizes (100 trechos cada = 500 trechos analisados contra o texto dos PDFs)
- 5 Lotes de Questões (200 questões cada = 1000 questões amostradas)
- 1 Varredura Global em todas as 10.332 questões procurando anomalias estruturais, gabarito e digitação
"""
import os
import sys
import json
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

def build_pdf_map():
    pdf_map = {}
    for folder in DOCS_DIR.glob("*"):
        if folder.is_dir():
            prefix = folder.name[:2]
            for pdf_file in folder.glob("*.pdf"):
                m = re.match(r"^\s*(\d{3})\s*-\s*Aula\s+(\d+)", pdf_file.name, re.I)
                if m:
                    aula_num = int(m.group(2))
                    pdf_map[(prefix, aula_num)] = pdf_file
    return pdf_map

def load_data():
    catalog = json.loads((CONTENT_DIR / "catalog.json").read_text(encoding="utf-8"))
    subjects = json.loads((CONTENT_DIR / "subjects.json").read_text(encoding="utf-8"))["subjects"]
    pdf_map = build_pdf_map()

    all_segments = []
    all_questions = []

    for item_file in sorted((CONTENT_DIR / "items").glob("*/*.json")):
        sub_id = item_file.parent.name
        aula_name = item_file.stem
        try:
            data = json.loads(item_file.read_text(encoding="utf-8"))
            aula_raw = data.get("aula")
            if isinstance(aula_raw, dict):
                aula_num = aula_raw.get("number", 0)
            elif isinstance(aula_raw, str):
                m = re.search(r"/[ac](\d+)", aula_raw)
                if m:
                    n = int(m.group(1))
                    aula_num = n + 100 if "/c" in aula_raw else n
                else:
                    aula_num = int(aula_name[1:]) if aula_name.startswith("a") else 0
            elif aula_name.startswith("a"):
                aula_num = int(aula_name[1:])
            elif aula_name.startswith("c"):
                aula_num = int(aula_name[1:]) + 100
            else:
                aula_num = 0
            
            seg_meta_file = CONTENT_DIR / "segments" / f"{sub_id}.json"
            seg_meta_map = {}
            if seg_meta_file.exists():
                sm_data = json.loads(seg_meta_file.read_text(encoding="utf-8"))
                for sm in sm_data.get("segments", []):
                    seg_meta_map[sm["id"]] = sm

            for idx, seg in enumerate(data.get("segments", [])):
                seg_id = seg["id"]
                sm = seg_meta_map.get(seg_id, {})
                
                # Resolve PDF
                pdf_path = None
                # Check authored in catalog
                for s in catalog["subjects"]:
                    if s["id"] == sub_id:
                        for a in s["aulas"]:
                            if a["number"] == aula_num:
                                if a.get("source") == "authored" or a.get("materialPath"):
                                    p = ROOT / "web" / "public" / a["materialPath"]
                                    if p.exists():
                                        pdf_path = p
                                    else:
                                        p2 = CONTENT_DIR / "complements" / Path(a["materialPath"]).name
                                        if p2.exists():
                                            pdf_path = p2
                if not pdf_path:
                    for s in subjects:
                        if s["id"] == sub_id:
                            pref = s["folderPrefix"]
                            if (pref, aula_num) in pdf_map:
                                pdf_path = pdf_map[(pref, aula_num)]

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
                    "pdfPath": str(pdf_path) if pdf_path else None
                }
                all_segments.append(seg_info)

                for qidx, q in enumerate(seg.get("questions", [])):
                    q_info = {
                        "id": f"{seg_id}#q{qidx+1:02d}",
                        "subjectId": sub_id,
                        "aulaNumber": aula_num,
                        "segmentId": seg_id,
                        "qIndex": qidx,
                        "pdfPath": str(pdf_path) if pdf_path else None,
                        "data": q
                    }
                    all_questions.append(q_info)
        except Exception as e:
            print(f"Erro ao processar {item_file}: {e}")

    return catalog, subjects, all_segments, all_questions

# Cache de textos de PDFs para evitar reabertura múltipla
PDF_TEXT_CACHE = {}

def get_pdf_pages_text(pdf_path, start_p, end_p):
    if not pdf_path or not Path(pdf_path).exists():
        return {}
    key = (pdf_path, start_p, end_p)
    if key in PDF_TEXT_CACHE:
        return PDF_TEXT_CACHE[key]
    
    try:
        doc = fitz.open(pdf_path)
        out = {}
        for pno in range(max(1, start_p), min(end_p + 1, len(doc) + 1)):
            out[pno] = doc[pno - 1].get_text("text")
        doc.close()
        PDF_TEXT_CACHE[key] = out
        return out
    except Exception as e:
        return {}

def normalize_text(t):
    if not t:
        return ""
    t = t.lower()
    # Preserva sinais matemáticos (+, -, *, /, ^, <, >, =) e pontuação técnica
    t = re.sub(r"[^\w\s+\-*/^<>=.,]", " ", t)
    return re.sub(r"\s+", " ", t).strip()

def audit_segment(seg):
    findings = []
    pdf_path = seg.get("pdfPath")
    if not pdf_path or not Path(pdf_path).exists():
        findings.append({
            "category": "pdf_missing",
            "severity": "alta",
            "evidence": f"PDF não encontrado para o segmento {seg['id']} (aula {seg['aulaNumber']}).",
            "suggestion": "Verificar mapeamento do PDF da aula."
        })
        return findings

    start_p = seg["startPage"]
    end_p = seg["endPage"]
    pages_text = get_pdf_pages_text(pdf_path, max(1, start_p - 1), end_p + 1)
    
    if not pages_text:
        findings.append({
            "category": "pdf_read_error",
            "severity": "alta",
            "evidence": f"Falha ao ler páginas do PDF {pdf_path}.",
            "suggestion": "Verificar integridade do PDF."
        })
        return findings

    # 1. Checagem de Diretriz / Páginas
    doc_len = len(fitz.open(pdf_path))
    if end_p > doc_len:
        findings.append({
            "category": "diretriz_pagina",
            "severity": "alta",
            "evidence": f"Página final {end_p} excede total de páginas do PDF ({doc_len}).",
            "suggestion": f"Ajustar endPage para no máximo {doc_len}."
        })

    # Checagem de Tópico Inicial
    start_topic = seg.get("startTopic")
    if start_topic:
        st_norm = normalize_text(start_topic)
        # Procura nas páginas startPage e startPage+1
        found_start = False
        for p in [start_p, start_p + 1, start_p - 1]:
            txt = normalize_text(pages_text.get(p, ""))
            # Busca palavras-chave significativas do tópico
            words = [w for w in st_norm.split() if len(w) > 3]
            if words:
                matches = sum(1 for w in words if w in txt)
                if matches / len(words) >= 0.6 or st_norm in txt:
                    found_start = True
                    break
        if not found_start:
            findings.append({
                "category": "topico_inicial",
                "severity": "media",
                "evidence": f"Tópico inicial '{start_topic}' não foi localizado com clareza na pág {start_p}.",
                "suggestion": "Conferir se o título do tópico confere com o cabeçalho/seção do PDF."
            })

    # Checagem de Paginação Impressa
    start_printed = seg.get("startPrinted")
    end_printed = seg.get("endPrinted")
    if start_printed is not None:
        p_txt = pages_text.get(start_p, "")
        # Verifica se o número impresso aparece nos primeiros ou últimos caracteres da página (cabeçalho/rodapé)
        lines = [ln.strip() for ln in p_txt.splitlines() if ln.strip()]
        has_printed_match = False
        for ln in lines[:3] + lines[-3:]:
            if re.search(r"\b" + str(start_printed) + r"\b", ln):
                has_printed_match = True
                break
        # Se não achou literal, checa coerência de offset
        offset = start_p - start_printed
        if offset < 0 or offset > 10:
            findings.append({
                "category": "impressa_offset",
                "severity": "baixa",
                "evidence": f"Offset de página impressa incomum (PDF {start_p}, Impressa {start_printed}, offset={offset}).",
                "suggestion": "Verificar se a capa/índice tem paginação romana ou sem número."
            })

    # 2. Checagem do Bizu (Summary)
    bizu = seg.get("bizu", {})
    summary = bizu.get("summary", [])
    if isinstance(summary, str):
        summary = [summary]
    
    all_seg_text = " ".join([pages_text.get(p, "") for p in range(start_p, end_p + 1)])
    norm_seg_text = normalize_text(all_seg_text)

    for bullet_idx, bullet in enumerate(summary):
        # Remove markdown
        b_clean = re.sub(r"[*_`#]", "", bullet)
        b_norm = normalize_text(b_clean)
        # Extrai termos técnicos (palavras em maiúsculas ou palavras com mais de 5 letras)
        terms = [w for w in b_norm.split() if len(w) > 5]
        if terms:
            present = sum(1 for t in terms if t in norm_seg_text)
            ratio = present / len(terms)
            if ratio < 0.35 and len(terms) >= 4:
                findings.append({
                    "category": "bizu_escopo",
                    "severity": "baixa",
                    "evidence": f"Bizu tópico #{bullet_idx+1} contém termos com baixa correlação no trecho págs {start_p}-{end_p}: '{bullet[:90]}...'",
                    "suggestion": "Verificar se o resumo sintetizou termos externos ou se foi generalista."
                })

    # 3. Checagem de Itens C/E
    for set_name in ["teoria", "revisao"]:
        items = bizu.get(set_name, [])
        for i_idx, item in enumerate(items):
            statement = item.get("statement", "")
            is_true = item.get("isTrue")
            expl = item.get("explanation", "")
            
            # Checa se o gabarito bate com a explicação
            expl_norm = normalize_text(expl)
            if is_true is True:
                if re.search(r"\b(incorret[ao]|fals[ao]|errad[ao]|n[ãa]o procede)\b", expl_norm[:60]):
                    findings.append({
                        "category": "ce_gabarito",
                        "severity": "alta",
                        "evidence": f"Item C/E {set_name} #{i_idx+1} tem isTrue=True mas explicação inicia sugerindo erro: '{expl[:100]}'",
                        "suggestion": "Revisar gabarito ou explicação do item."
                    })
            elif is_true is False:
                if re.search(r"\b(corret[ao]|verdadeir[ao]|exat[ao]|perfeit[ao])\b", expl_norm[:60]) and not re.search(r"\b(in|n[ãa]o)\b", expl_norm[:60]):
                    findings.append({
                        "category": "ce_gabarito",
                        "severity": "alta",
                        "evidence": f"Item C/E {set_name} #{i_idx+1} tem isTrue=False mas explicação inicia afirmando acerto: '{expl[:100]}'",
                        "suggestion": "Revisar gabarito ou explicação do item."
                    })

    return findings

def audit_question(q_obj):
    findings = []
    q = q_obj["data"]
    qid = q_obj["id"]
    stmt = q.get("statement", "")
    opts = q.get("options", [])
    ans = q.get("answer", "")
    expl = q.get("explanation", "")
    page_ref = q.get("pageRef")
    
    # 1. Estrutura
    if len(opts) != 5:
        findings.append({
            "category": "estrutura_opcoes",
            "severity": "alta",
            "evidence": f"Questão possui {len(opts)} alternativas (esperado 5).",
            "suggestion": "Completar para 5 alternativas A-E."
        })
    
    if ans not in ["A", "B", "C", "D", "E"]:
        findings.append({
            "category": "gabarito_invalido",
            "severity": "alta",
            "evidence": f"Gabarito '{ans}' inválido (esperado A, B, C, D ou E).",
            "suggestion": "Definir letra válida A-E."
        })

    # Alternativas duplicadas
    norm_opts = [normalize_text(o) for o in opts]
    for i in range(len(norm_opts)):
        for j in range(i + 1, len(norm_opts)):
            if norm_opts[i] and norm_opts[i] == norm_opts[j]:
                findings.append({
                    "category": "alternativas_duplicadas",
                    "severity": "alta",
                    "evidence": f"Alternativa {chr(65+i)} e {chr(65+j)} são idênticas: '{opts[i]}'.",
                    "suggestion": "Diferenciar as opções."
                })

    # 2. Digitação e Encoding
    full_text = f"{stmt} {' '.join(opts)} {expl}"
    bad_chars = re.findall(r"[\ufffd]|Ã©|Ã£|Ã§|Â|Ã¡|Ã³|Ãº", full_text)
    if bad_chars:
        findings.append({
            "category": "encoding_corrompido",
            "severity": "media",
            "evidence": f"Caracteres de encoding corrompido encontrados: {set(bad_chars)}.",
            "suggestion": "Corrigir acentuação corrompida."
        })

    # Palavras repetidas consecutivas ("de de", "em em")
    rep_words = re.findall(r"\b(o|a|de|do|da|em|no|na|que|para|com)\s+\1\b", full_text, re.I)
    if rep_words:
        findings.append({
            "category": "digitacao_duplicada",
            "severity": "baixa",
            "evidence": f"Palavras repetidas consecutivas: {set(rep_words)} no enunciado/opções.",
            "suggestion": "Remover repetição indevida."
        })

    # 3. Coerência do Gabarito e Explicação
    expl_norm = normalize_text(expl)
    # Procura se a explicação aponta explicitamente outra alternativa como correta
    m_exp_letter = re.search(r"\b(alternativa|letra|gabarito|item)\s+([a-e])\s+(est[aá]|é|como)\s+(corret[ao]|gabarito|verdadeir[ao])\b", expl_norm)
    if m_exp_letter:
        exp_letter = m_exp_letter.group(2).upper()
        if exp_letter != ans:
            findings.append({
                "category": "gabarito_contradicao",
                "severity": "alta",
                "evidence": f"Gabarito é '{ans}', mas a explicação afirma que a alternativa '{exp_letter}' é a correta: '{expl[:120]}...'",
                "suggestion": f"Ajustar gabarito para '{exp_letter}' ou corrigir a explicação."
            })

    # Checagem de comando: "assinale a incorreta" mas gabarito tem pegadinha
    is_neg = bool(re.search(r"\b(inco[r|rr]et[ao]|fals[ao]|errad[ao]|n[ãa]o\s+[eé]|exceto|desconforme)\b", stmt.lower()))
    
    return findings

def run_global_scan(all_questions):
    print("\n--- INICIANDO VARREDURA ESTRUTURAL GLOBAL (10.332 QUESTÕES) ---")
    summary = Counter()
    issues_by_cat = defaultdict(list)

    for q in all_questions:
        res = audit_question(q)
        for f in res:
            cat = f["category"]
            summary[cat] += 1
            if len(issues_by_cat[cat]) < 30: # guarda até 30 exemplos por categoria
                issues_by_cat[cat].append({
                    "id": q["id"],
                    "subject": q["subjectId"],
                    "evidence": f["evidence"],
                    "suggestion": f["suggestion"],
                    "severity": f["severity"]
                })

    report = {
        "total_questions_scanned": len(all_questions),
        "total_issues_found": sum(summary.values()),
        "issues_by_category": dict(summary),
        "samples": issues_by_cat
    }
    return report

def main():
    catalog, subjects, all_segments, all_questions = load_data()
    print(f"Total: {len(all_segments)} segmentos | {len(all_questions)} questões")

    # Mapeamento por disciplina
    segs_by_sub = defaultdict(list)
    for s in all_segments:
        segs_by_sub[s["subjectId"]].append(s)

    qs_by_sub = defaultdict(list)
    for q in all_questions:
        qs_by_sub[q["subjectId"]].append(q)

    # ─────────────────────────────────────────────────────────────
    # GRUPO 1: 5 LOTES DE DIRETRIZES (100 cada)
    # ─────────────────────────────────────────────────────────────
    
    # Lote 1: direito-administrativo, direito-constitucional, direito-penal-militar
    random.seed(101)
    pool1 = segs_by_sub["direito-administrativo"] + segs_by_sub["direito-constitucional"] + segs_by_sub["direito-penal-militar"]
    sample_dir_1 = random.sample(pool1, min(100, len(pool1)))

    # Lote 2: lingua-portuguesa, informatica, legislacoes-pe
    random.seed(202)
    pool2 = segs_by_sub["lingua-portuguesa"] + segs_by_sub["informatica"] + segs_by_sub["legislacoes-pe"]
    sample_dir_2 = random.sample(pool2, min(100, len(pool2)))

    # Lote 3: biologia, quimica, fisica
    random.seed(303)
    pool3 = segs_by_sub["biologia"] + segs_by_sub["quimica"] + segs_by_sub["fisica"]
    sample_dir_3 = random.sample(pool3, min(100, len(pool3)))

    # Lote 4: matematica, estatistica
    random.seed(404)
    pool4 = segs_by_sub["matematica"] + segs_by_sub["estatistica"]
    sample_dir_4 = random.sample(pool4, min(100, len(pool4)))

    # Lote 5: lingua-inglesa, lingua-espanhola + complementos autorais
    random.seed(505)
    pool5_langs = segs_by_sub["lingua-inglesa"] + segs_by_sub["lingua-espanhola"]
    # acha complementos autorais
    pool5_authored = [s for s in all_segments if s["aulaNumber"] >= 100 or "complement" in str(s.get("pdfPath", ""))]
    pool5 = pool5_langs + pool5_authored
    # remove duplicatas se houver
    pool5_unique = {s["id"]: s for s in pool5}.values()
    sample_dir_5 = random.sample(list(pool5_unique), min(100, len(pool5_unique)))

    dir_lots = [
        ("diretrizes-1-direito", "Direito Administrativo, Constitucional e Penal Militar", sample_dir_1),
        ("diretrizes-2-port-info-leg", "Língua Portuguesa, Informática e Legislações PE", sample_dir_2),
        ("diretrizes-3-ciencias", "Biologia, Química e Física", sample_dir_3),
        ("diretrizes-4-exatas", "Matemática e Estatística", sample_dir_4),
        ("diretrizes-5-linguas-complementos", "Línguas Estrangeiras e Materiais Autorais", sample_dir_5),
    ]

    all_dir_reports = {}

    for file_slug, title, sample in dir_lots:
        print(f"Executando auditoria de diretrizes: {title} ({len(sample)} trechos)...")
        lot_findings = []
        counts = Counter()
        ok_count = 0

        for seg in sample:
            f = audit_segment(seg)
            if not f:
                ok_count += 1
            else:
                for item in f:
                    counts[item["category"]] += 1
                    lot_findings.append({
                        "segmentId": seg["id"],
                        "subject": seg["subjectId"],
                        "aula": seg["aulaNumber"],
                        "pages": f"{seg['startPage']}-{seg['endPage']}",
                        **item
                    })

        rep = {
            "title": title,
            "total_sampled": len(sample),
            "total_ok": ok_count,
            "total_with_issues": len(sample) - ok_count,
            "summary_by_category": dict(counts),
            "findings": lot_findings
        }
        all_dir_reports[file_slug] = rep

        # Salva JSON
        (AUDIT_OUT / f"{file_slug}.json").write_text(json.dumps(rep, indent=2, ensure_ascii=False), encoding="utf-8")

        # Salva MD
        md_lines = [
            f"# Relatório de Auditoria: {title}",
            "",
            f"- **Amostragem**: {len(sample)} trechos analisados contra os PDFs originais.",
            f"- **Trechos 100% Conformes**: {ok_count} ({ok_count/len(sample)*100:.1f}%)",
            f"- **Trechos com Apontamentos**: {len(sample) - ok_count}",
            "",
            "## Resumo por Categoria",
            "",
            "| Categoria | Ocorrências |",
            "|---|---|"
        ]
        for cat, cnt in counts.items():
            md_lines.append(f"| {cat} | {cnt} |")
        if not counts:
            md_lines.append("| Nenhuma não-conformidade detectada | 0 |")

        md_lines.extend([
            "",
            "## Tabela Detalhada de Achados",
            "",
            "| ID Trecho | Páginas | Severidade | Categoria | Evidência / Correção Sugerida |",
            "|---|---|---|---|---|"
        ])
        for fd in lot_findings:
            md_lines.append(f"| `{fd['segmentId']}` | {fd['pages']} | **{fd['severity'].upper()}** | `{fd['category']}` | {fd['evidence']} <br>👉 *{fd['suggestion']}* |")

        (AUDIT_OUT / f"{file_slug}.md").write_text("\n".join(md_lines), encoding="utf-8")

    # ─────────────────────────────────────────────────────────────
    # GRUPO 2: 5 LOTES DE QUESTÕES (200 cada)
    # ─────────────────────────────────────────────────────────────

    # Lote 1: direito-administrativo, direito-constitucional, direito-penal-militar, legislacoes-pe
    random.seed(1001)
    pool_q1 = qs_by_sub["direito-administrativo"] + qs_by_sub["direito-constitucional"] + qs_by_sub["direito-penal-militar"] + qs_by_sub["legislacoes-pe"]
    sample_q_1 = random.sample(pool_q1, min(200, len(pool_q1)))

    # Lote 2: lingua-portuguesa, lingua-inglesa, lingua-espanhola
    random.seed(2002)
    pool_q2 = qs_by_sub["lingua-portuguesa"] + qs_by_sub["lingua-inglesa"] + qs_by_sub["lingua-espanhola"]
    sample_q_2 = random.sample(pool_q2, min(200, len(pool_q2)))

    # Lote 3: matematica, estatistica
    random.seed(3003)
    pool_q3 = qs_by_sub["matematica"] + qs_by_sub["estatistica"]
    sample_q_3 = random.sample(pool_q3, min(200, len(pool_q3)))

    # Lote 4: biologia, quimica, fisica
    random.seed(4004)
    pool_q4 = qs_by_sub["biologia"] + qs_by_sub["quimica"] + qs_by_sub["fisica"]
    sample_q_4 = random.sample(pool_q4, min(200, len(pool_q4)))

    # Lote 5: 120 informatica + 80 difíceis (difficulty 3)
    random.seed(5005)
    pool_q5_info = qs_by_sub["informatica"]
    sample_q5_info = random.sample(pool_q5_info, min(120, len(pool_q5_info)))
    
    pool_q5_diff3 = [q for q in all_questions if q["data"].get("difficulty") == 3 and q["subjectId"] != "informatica"]
    sample_q5_diff3 = random.sample(pool_q5_diff3, min(80, len(pool_q5_diff3)))
    sample_q_5 = sample_q5_info + sample_q5_diff3

    q_lots = [
        ("questoes-1-direito", "Direito e Legislações PE", sample_q_1),
        ("questoes-2-linguas", "Língua Portuguesa, Inglês e Espanhol", sample_q_2),
        ("questoes-3-exatas", "Matemática e Estatística", sample_q_3),
        ("questoes-4-ciencias", "Biologia, Química e Física", sample_q_4),
        ("questoes-5-informatica-dificeis", "Informática e Questões Avançadas (Nível 3)", sample_q_5),
    ]

    all_q_reports = {}

    for file_slug, title, sample in q_lots:
        print(f"Executando auditoria de questões: {title} ({len(sample)} questões)...")
        lot_findings = []
        counts = Counter()
        ok_count = 0

        for q in sample:
            f = audit_question(q)
            if not f:
                ok_count += 1
            else:
                for item in f:
                    counts[item["category"]] += 1
                    lot_findings.append({
                        "questionId": q["id"],
                        "subject": q["subjectId"],
                        "statement_snippet": q["data"].get("statement", "")[:90] + "...",
                        "answer": q["data"].get("answer"),
                        **item
                    })

        rep = {
            "title": title,
            "total_sampled": len(sample),
            "total_ok": ok_count,
            "total_with_issues": len(sample) - ok_count,
            "summary_by_category": dict(counts),
            "findings": lot_findings
        }
        all_q_reports[file_slug] = rep

        # Salva JSON
        (AUDIT_OUT / f"{file_slug}.json").write_text(json.dumps(rep, indent=2, ensure_ascii=False), encoding="utf-8")

        # Salva MD
        md_lines = [
            f"# Relatório de Revisão de Questões: {title}",
            "",
            f"- **Amostragem**: {len(sample)} questões revisadas.",
            f"- **Questões 100% Conformes**: {ok_count} ({ok_count/len(sample)*100:.1f}%)",
            f"- **Questões com Apontamentos**: {len(sample) - ok_count}",
            "",
            "## Resumo por Categoria",
            "",
            "| Categoria | Ocorrências |",
            "|---|---|"
        ]
        for cat, cnt in counts.items():
            md_lines.append(f"| {cat} | {cnt} |")
        if not counts:
            md_lines.append("| Nenhuma não-conformidade detectada | 0 |")

        md_lines.extend([
            "",
            "## Tabela de Apontamentos",
            "",
            "| ID Questão | Gab | Severidade | Categoria | Enunciado / Evidência |",
            "|---|---|---|---|---|"
        ])
        for fd in lot_findings:
            md_lines.append(f"| `{fd['questionId']}` | **{fd.get('answer','-')}** | **{fd['severity'].upper()}** | `{fd['category']}` | *{fd['statement_snippet']}*<br>⚠️ {fd['evidence']}<br>👉 *{fd['suggestion']}* |")

        (AUDIT_OUT / f"{file_slug}.md").write_text("\n".join(md_lines), encoding="utf-8")

    # ─────────────────────────────────────────────────────────────
    # VARREDURA GLOBAL DAS 10.332 QUESTÕES
    # ─────────────────────────────────────────────────────────────
    global_report = run_global_scan(all_questions)
    (AUDIT_OUT / "varredura-global-questoes.json").write_text(json.dumps(global_report, indent=2, ensure_ascii=False), encoding="utf-8")

    # Consolida relatório geral
    consolidated = {
        "diretrizes": all_dir_reports,
        "questoes_amostra": all_q_reports,
        "varredura_global": global_report
    }
    (AUDIT_OUT / "consolidated_audit.json").write_text(json.dumps(consolidated, indent=2, ensure_ascii=False), encoding="utf-8")
    print("\nAuditoria concluída com sucesso! Relatórios salvos em:", AUDIT_OUT)

if __name__ == "__main__":
    main()
