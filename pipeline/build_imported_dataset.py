"""Constrói o dataset completo de questões migradas do TecConcursos com metadados e classificação no edital.

Exporta para:
- pipeline/.cache/imported_questions.json
- pipeline/.cache/review_queue.json
- pipeline/.cache/import_report.json
"""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from pipeline.tec_extractor import extract_all_questions_from_dir, TecQuestion
from pipeline.edital_classifier import EditalClassifier

ROOT = Path(__file__).resolve().parent.parent
DOCS_QUESTOES = ROOT / "docs" / "questoes"
CACHE_DIR = ROOT / "pipeline" / ".cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)


def build_dataset() -> dict:
    print(f"Extraindo questões de {DOCS_QUESTOES}...")
    questions = extract_all_questions_from_dir(DOCS_QUESTOES)
    print(f"Total de questões únicas extraídas: {len(questions)}")

    classifier = EditalClassifier()
    imported_rows = []
    review_queue = []

    for q in questions:
        cls = classifier.classify_question(q)

        # Montar explicação / justificativa padrão informando gabarito e dados oficiais
        explanation = (
            f"Questão {q.seq_num} ({q.banca} - {q.cargo}/{q.concurso}"
            + (f"/{q.ano}" if q.ano else "")
            + f"). Assunto: {q.raw_topic or q.raw_subject}. Gabarito oficial: {q.gabarito}."
        )

        row = {
            "id": f"tec_{q.tec_id}",
            "tecId": q.tec_id,
            "seqNum": q.seq_num,
            "subjectId": cls.subject_id,
            "aulaId": cls.aula_id,
            "segmentId": cls.segment_id,
            "editalItemId": cls.edital_item_id,
            "topic": q.raw_topic or cls.edital_topic,
            "statement": q.statement,
            "explanation": explanation,
            "difficulty": 2,
            "pattern": q.banca,
            "isCertoErrado": q.is_certo_errado,
            "isAnulada": q.is_anulada,
            "status": "RETIRED" if q.is_anulada else "APPROVED",
            "sourcePdf": q.source_pdf,
            "contentHash": q.content_hash,
            "confidence": cls.confidence,
            "options": [
                {
                    "label": opt.label,
                    "text": opt.text,
                    "isCorrect": (opt.label == q.gabarito) if not q.is_anulada else False,
                }
                for opt in q.options
            ],
        }

        imported_rows.append(row)

        if cls.needs_review:
            review_queue.append({
                "questionId": row["id"],
                "tecId": q.tec_id,
                "rawSubject": q.raw_subject,
                "rawTopic": q.raw_topic,
                "assignedSubject": cls.subject_id,
                "assignedTopic": cls.edital_topic,
                "confidence": cls.confidence,
                "reason": cls.review_reason,
            })

    report = {
        "generatedAt": datetime.now().isoformat(),
        "totalExtracted": len(questions),
        "totalApproved": sum(1 for r in imported_rows if r["status"] == "APPROVED"),
        "totalRetiredAnuladas": sum(1 for r in imported_rows if r["status"] == "RETIRED"),
        "totalCertoErrado": sum(1 for r in imported_rows if r["isCertoErrado"]),
        "totalMultiplaEscolha": sum(1 for r in imported_rows if not r["isCertoErrado"]),
        "reviewQueueCount": len(review_queue),
        "bySubject": {},
    }

    for r in imported_rows:
        sid = r["subjectId"]
        report["bySubject"][sid] = report["bySubject"].get(sid, 0) + 1

    # Salvar arquivos
    (CACHE_DIR / "imported_questions.json").write_text(json.dumps(imported_rows, ensure_ascii=False, indent=2), encoding="utf-8")
    (CACHE_DIR / "review_queue.json").write_text(json.dumps(review_queue, ensure_ascii=False, indent=2), encoding="utf-8")
    (CACHE_DIR / "import_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print("\nDataset gerado com sucesso!")
    print(f"Salvo em: {CACHE_DIR / 'imported_questions.json'}")
    print(f"Aprovadas: {report['totalApproved']} | Anuladas (aposentadas): {report['totalRetiredAnuladas']}")
    print(f"Itens na fila de revisão: {len(review_queue)}")
    return report


if __name__ == "__main__":
    build_dataset()
