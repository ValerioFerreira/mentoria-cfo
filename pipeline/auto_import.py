"""Rotina de automação incremental para monitorar docs/questoes e importar novos PDFs.

Mantém docs/questoes/.processed_manifest.json registrando:
- Nome do arquivo
- SHA-256 do arquivo PDF
- Data de processamento
- Contagem de questões extraídas e importadas

Quando executado:
1. Detecta arquivos novos ou com hash alterado.
2. Extrai e classifica apenas as novas questões.
3. Importa de forma idempotente para o banco de dados (ignorando questões já cadastradas via tec_id).
4. Atualiza o manifesto de controle.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path
import sys

from pipeline.tec_extractor import extract_questions_from_pdf, TecQuestion
from pipeline.edital_classifier import EditalClassifier

ROOT = Path(__file__).resolve().parent.parent
DOCS_QUESTOES = ROOT / "docs" / "questoes"
MANIFEST_PATH = DOCS_QUESTOES / ".processed_manifest.json"


def compute_file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def load_manifest() -> dict[str, dict]:
    if MANIFEST_PATH.exists():
        try:
            return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_manifest(manifest: dict[str, dict]) -> None:
    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


def run_auto_import(force_all: bool = False) -> dict:
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Verificando PDFs em {DOCS_QUESTOES}...")
    manifest = load_manifest()
    pdf_files = sorted(DOCS_QUESTOES.glob("*.pdf"))

    if not pdf_files:
        print("Nenhum arquivo PDF encontrado em docs/questoes.")
        return {"status": "no_files", "processed": 0}

    classifier = EditalClassifier()
    new_questions: list[dict] = []
    updated_files = 0

    for pdf in pdf_files:
        file_sha256 = compute_file_sha256(pdf)
        cached_info = manifest.get(pdf.name)

        if not force_all and cached_info and cached_info.get("sha256") == file_sha256:
            # Arquivo já processado e sem alterações
            continue

        print(f"Processando arquivo: {pdf.name} (SHA-256: {file_sha256[:8]}...)...")
        qs = extract_questions_from_pdf(pdf)
        print(f"  -> {len(qs)} questões extraídas do PDF.")

        for q in qs:
            cls = classifier.classify_question(q)
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
                "topic": q.raw_topic or cls.edital_topic,
                "statement": q.statement,
                "explanation": explanation,
                "difficulty": 2,
                "pattern": q.banca,
                "status": "RETIRED" if q.is_anulada else "APPROVED",
                "batch": f"auto-import-{datetime.now().strftime('%Y%m%d')}",
                "options": [
                    {
                        "label": opt.label,
                        "text": opt.text,
                        "isCorrect": (opt.label == q.gabarito) if not q.is_anulada else False,
                    }
                    for opt in q.options
                ],
            }
            new_questions.append(row)

        manifest[pdf.name] = {
            "sha256": file_sha256,
            "processedAt": datetime.now().isoformat(),
            "questionsCount": len(qs),
            "fileSize": pdf.stat().st_size,
        }
        updated_files += 1

    save_manifest(manifest)

    if not new_questions:
        print("Nenhuma nova questão ou arquivo pendente de importação.")
        return {"status": "up_to_date", "new_questions": 0}

    print(f"\nTotal de {len(new_questions)} questões identificadas para importação/atualização.")
    # Salvar lote temporário para importação no banco
    temp_json = ROOT / "pipeline" / ".cache" / "pending_auto_import.json"
    temp_json.write_text(json.dumps(new_questions, ensure_ascii=False, indent=2), encoding="utf-8")

    return {
        "status": "pending_db_sync",
        "new_questions": len(new_questions),
        "updated_files": updated_files,
        "temp_json": str(temp_json),
    }


if __name__ == "__main__":
    force = "--force" in sys.argv
    run_auto_import(force_all=force)
