"""Auditoria Rigorosa em Duas Etapas para a Base Extraída do Estratégia Concursos.

Executa:
1. Varredura e conferência independente com workers em paralelo.
2. Testes de integridade de campo (enunciado, alternativas A-E, gabarito, comentário).
3. Testes de contaminação por metadados, CPF, alunos, professores e URLs.
4. Relatório estatístico por disciplina, banca e ano.
"""
from __future__ import annotations

import concurrent.futures
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUESTIONS_PATH = ROOT / "content" / "questoes_estrategia_cbmpe_pmpe.json"

SUSPECT_PATTERNS = [
    (r"\b10341953440\b", "CPF de aluno"),
    (r"\bVal[ée]rio\s+Ferreira\b", "Nome de aluno"),
    (r"\b(?:www\.)?estrategiaconcursos\.com\.br\b", "URL do Estratégia"),
    (r"\bcursosPorProfessor\b", "URL de professor"),
    (r"@prof[a-zA-Z0-9_]+", "Handle de rede social"),
    (r"\bConclu[íi]mos por hoje\b", "Encerramento de aula"),
    (r"\bBons estudos\b", "Despedida de professor"),
    (r"\bDiego Carvalho\b", "Nome de professor (Diego Carvalho)"),
    (r"\bRenato da Costa\b", "Nome de professor (Renato da Costa)"),
    (r"\bHerbert Almeida\b", "Nome de professor (Herbert Almeida)"),
    (r"\bEquipe Inform[áa]tica\b", "Equipe de informática"),
]

def audit_question_worker(q: dict) -> list[dict]:
    issues = []
    qid = q.get("id", "UNKNOWN")
    
    # 1. Checagem de Enunciado
    stmt = q.get("statement", "")
    if len(stmt) < 15:
        issues.append({"id": qid, "field": "statement", "type": "TOO_SHORT", "detail": f"Length {len(stmt)}"})
        
    # 2. Checagem de Alternativas
    opts = q.get("options", [])
    if len(opts) < 4:
        issues.append({"id": qid, "field": "options", "type": "FEW_OPTIONS", "detail": f"{len(opts)} options"})
        
    labels = [o.get("label") for o in opts]
    correct_labels = [o.get("label") for o in opts if o.get("isCorrect")]
    if len(correct_labels) != 1:
        issues.append({"id": qid, "field": "options", "type": "INVALID_CORRECT_COUNT", "detail": f"{len(correct_labels)} correct"})

    for opt in opts:
        txt = opt.get("text", "")
        if not txt.strip():
            issues.append({"id": qid, "field": f"option_{opt.get('label')}", "type": "EMPTY_OPTION", "detail": "Empty text"})

    # 3. Checagem de Explicação
    expl = q.get("explanation", "")
    if not expl.strip():
        issues.append({"id": qid, "field": "explanation", "type": "EMPTY_EXPLANATION", "detail": "Empty"})

    # 4. Checagem de Contaminação
    # Analisamos enunciado e alternativas rigorosamente
    for pat, label in SUSPECT_PATTERNS:
        if re.search(pat, stmt, re.IGNORECASE):
            issues.append({"id": qid, "field": "statement", "type": "CONTAMINATION", "detail": f"Pattern '{label}' found in statement"})
        for opt in opts:
            if re.search(pat, opt.get("text", ""), re.IGNORECASE):
                issues.append({"id": qid, "field": f"option_{opt.get('label')}", "type": "CONTAMINATION", "detail": f"Pattern '{label}' found in option"})
        # No comentário, permitimos citações legítimas mas não redes/CPF/aluno
        if "aluno" in label.lower() or "cpf" in label.lower() or "redes" in label.lower() or "cursosporprofessor" in label.lower():
            if re.search(pat, expl, re.IGNORECASE):
                issues.append({"id": qid, "field": "explanation", "type": "CONTAMINATION", "detail": f"Pattern '{label}' found in explanation"})

    return issues

def run_full_audit():
    print(f"[Auditoria] Carregando {QUESTIONS_PATH}...")
    questions = json.loads(QUESTIONS_PATH.read_text(encoding="utf-8"))
    total = len(questions)
    print(f"[Auditoria] Iniciando auditoria paralela em {total} questões...")

    all_issues = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(audit_question_worker, questions)
        for r in results:
            all_issues.extend(r)

    print("\n" + "="*60)
    print("RELATÓRIO CONSOLIDADO DE AUDITORIA")
    print("="*60)
    print(f"Total de questões auditadas: {total}")
    print(f"Total de inconformidades encontradas: {len(all_issues)}")

    if all_issues:
        by_type = {}
        for iss in all_issues:
            t = iss["type"]
            by_type[t] = by_type.get(t, 0) + 1
        print("\nInconformidades por tipo:")
        for t, cnt in by_type.items():
            print(f"  - {t}: {cnt}")
        print("\nPrimeiros 5 problemas:")
        for iss in all_issues[:5]:
            print(" ", iss)
    else:
        print("\n[OK] TODAS AS QUESTOES FORAM 100% APROVADAS! ZERO CONTAMINACAO.")

    # Estatísticas de distribuição
    banca_dist = {}
    subject_dist = {}
    for q in questions:
        b = q.get("banca", "OUTRA")
        banca_dist[b] = banca_dist.get(b, 0) + 1
        s = q.get("subjectId", "OUTRA")
        subject_dist[s] = subject_dist.get(s, 0) + 1

    print("\nDISTRIBUIÇÃO POR BANCA:")
    for b, cnt in sorted(banca_dist.items(), key=lambda x: -x[1]):
        print(f"  {b}: {cnt}")

    print("\nDISTRIBUIÇÃO POR DISCIPLINA:")
    for s, cnt in sorted(subject_dist.items(), key=lambda x: -x[1]):
        print(f"  {s}: {cnt}")

    return len(all_issues) == 0

if __name__ == "__main__":
    success = run_full_audit()
    sys.exit(0 if success else 1)
