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


_AULA_RE = re.compile(r"^\s*(\d{3})\s*-\s*Aula\s+(\d+|[úu]nica)", re.IGNORECASE)


def parse_pdf_name(filename: str) -> tuple[int, int] | None:
    """'002 - Aula 01 Substantivos...pdf' -> (ordem=2, aula=1)."""
    m = _AULA_RE.match(filename)
    if not m:
        return None
    ordem = int(m.group(1))
    raw_num = m.group(2).lower()
    aula = 0 if raw_num in ("única", "unica") else int(raw_num)
    return (ordem, aula)


def aula_id(subject_id: str, aula_number: int) -> str:
    return f"{subject_id}/a{aula_number:02d}"


def pdf_key(folder_name: str, filename: str) -> str:
    """Chave estável do PDF no cache: '<prefixo-pasta>_<ordem>' (ex.: '02_004')."""
    return f"{folder_name[:2]}_{filename[:3]}"


# Mapeamento explícito para pastas extras/compartilhadas (PCPE): chave '<pasta>_<ordem>' -> (subject_id, aula_number)
PDF_TARGET_OVERRIDES: dict[str, tuple[str, int] | None] = {
    # docs/42 -> novas aulas de Direito Administrativo (a20..a24, preservando a00..a09)
    "42_007": ("direito-administrativo", 20),
    "42_008": ("direito-administrativo", 21),
    "42_009": ("direito-administrativo", 22),
    "42_014": ("direito-administrativo", 23),
    "42_015": ("direito-administrativo", 24),
    # docs/46 -> Aulas 15 e 19 pertencem a legislacao-penal-especial (mantendo numeração do curso PC-PE)
    "46_016": ("legislacao-penal-especial", 15),
    "46_020": ("legislacao-penal-especial", 19),
    # docs/30 -> Aulas 00..10 ignoradas (duplicadas ou fora do edital PCPE); 012..020 mapeadas para Aula 11..21 do curso PC-PE
    "30_001": None,
    "30_002": None,
    "30_003": None,
    "30_004": None,
    "30_005": None,
    "30_006": None,
    "30_007": None,
    "30_008": None,
    "30_009": None,
    "30_010": None,
    "30_011": None,
    "30_014": ("legislacao-penal-especial", 11),  # Lei 8.072/1990 - Crimes Hediondos
    "30_013": ("legislacao-penal-especial", 12),  # Lei 7.716/1989 - Preconceito de Raça ou de Cor
    "30_012": ("legislacao-penal-especial", 13),  # Lei 13.869/2019 - Abuso de Autoridade
    "30_016": ("legislacao-penal-especial", 14),  # Lei 9.455/1997 - Crimes de Tortura
    "30_015": ("legislacao-penal-especial", 16),  # Lei 9.503/1997 - Crimes de Trânsito (CTB)
    "30_019": ("legislacao-penal-especial", 17),  # Lei 11.340/2006 - Lei Maria da Penha
    "30_020": ("legislacao-penal-especial", 18),  # Lei 11.343/2006 - Lei de Drogas
    "30_017": ("legislacao-penal-especial", 20),  # Lei 9.605/1998 - Crimes Ambientais
    "30_018": ("legislacao-penal-especial", 21),  # Lei 10.826/2003 - Estatuto do Desarmamento
    # docs/39 -> Aulas 03 e 06 mapeadas para direito-penal-militar a20 e a21 (CFOA itens 6.2 e 6.3, banca AOCP)
    "39_001": None,
    "39_002": None,
    "39_003": None,
    "39_004": ("direito-penal-militar", 20),  # Lei 13.869/2019 - Abuso de Autoridade
    "39_005": None,
    "39_006": None,
    "39_007": ("direito-penal-militar", 21),  # Lei 7.716/1989 - Crimes de Preconceito de Raça ou de Cor
    "39_008": None,
    "39_009": None,
    "39_010": None,
}


def resolve_pdf_target(folder_name: str, filename: str, subjects_by_pref: dict[str, Subject] | None = None) -> tuple[str, int] | None:
    """Resolve (subject_id, aula_number) para um PDF em docs/, respeitando PDF_TARGET_OVERRIDES."""
    parsed = parse_pdf_name(filename)
    if parsed is None:
        return None
    key = pdf_key(folder_name, filename)
    if key in PDF_TARGET_OVERRIDES:
        return PDF_TARGET_OVERRIDES[key]
    by_pref = subjects_by_pref if subjects_by_pref is not None else subject_by_prefix()
    subj = by_pref.get(folder_name[:2])
    if subj is None:
        return None
    return (subj.id, parsed[1])



def load_overrides() -> dict[str, dict]:
    """Ajustes manuais por aula: content/overrides.json + content/overrides/<disciplina>.json (auditoria por disciplina).
    Chaves do arquivo por disciplina sobrepõem as do arquivo geral, aula a aula."""
    out: dict[str, dict] = json.loads((CONTENT_DIR / "overrides.json").read_text(encoding="utf-8"))["aulas"]
    out = {k: dict(v) for k, v in out.items()}
    d = CONTENT_DIR / "overrides"
    if d.exists():
        for f in sorted(d.glob("*.json")):
            for aula, ov in json.loads(f.read_text(encoding="utf-8")).get("aulas", {}).items():
                out.setdefault(aula, {}).update(ov)
    return out
