"""Caminhos e metadados compartilhados pelo pipeline de conteúdo."""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
CONTENT_DIR = ROOT / "content"
CACHE_DIR = ROOT / "pipeline" / ".cache"
PAGES_DIR = CACHE_DIR / "pages"
XLSX_PATH = DOCS_DIR / "indice_topicos_curso.xlsx"
INDEX_JSON = CACHE_DIR / "index.json"


@dataclass(frozen=True)
class Subject:
    id: str
    name: str
    block: str
    exam_questions: int
    folder_prefix: str
    sort_order: int
    language_group: str | None = None


def load_subjects() -> list[Subject]:
    raw = json.loads((CONTENT_DIR / "subjects.json").read_text(encoding="utf-8"))
    return [
        Subject(
            id=s["id"],
            name=s["name"],
            block=s["block"],
            exam_questions=s["examQuestions"],
            folder_prefix=s["folderPrefix"],
            sort_order=s["sortOrder"],
            language_group=s.get("languageGroup"),
        )
        for s in raw["subjects"]
    ]


def subject_by_prefix() -> dict[str, Subject]:
    return {s.folder_prefix: s for s in load_subjects()}


_AULA_RE = re.compile(r"^\s*(\d{3})\s*-\s*Aula\s+(\d+)", re.IGNORECASE)


def parse_pdf_name(filename: str) -> tuple[int, int] | None:
    """'002 - Aula 01 Substantivos...pdf' -> (ordem=2, aula=1)."""
    m = _AULA_RE.match(filename)
    return (int(m.group(1)), int(m.group(2))) if m else None


def aula_id(subject_id: str, aula_number: int) -> str:
    return f"{subject_id}/a{aula_number:02d}"


def pdf_key(folder_name: str, filename: str) -> str:
    """Chave estável do PDF no cache: '<prefixo-pasta>_<ordem>' (ex.: '02_004')."""
    return f"{folder_name[:2]}_{filename[:3]}"
