"""Utilitários de texto e de carregamento do cache compartilhados pelas etapas do pipeline."""
from __future__ import annotations

import json
import re
import unicodedata
from functools import lru_cache
from pathlib import Path

from config import PAGES_DIR

# Marcadores de seção que NÃO são teoria (fim da teoria / seções de prática).
END_MARKER = re.compile(
    r"(quest[õo]es|lista de|gabarito|resumo|mapa mental|f[óo]rmulas|vocabul[áa]rio|quadros? de|"
    r"textos traduz|prova comentada|bateria|simulado|dispositivos mais cobrados|exerc[íi]cios)",
    re.IGNORECASE,
)
# Marcadores de seção de questões COM comentário (alvo da atividade Fixação).
COMMENTED_MARKER = re.compile(r"(quest[õo]es comentadas|exerc[íi]cios comentados|prova comentada|resolu[çc][ãa]o de (provas|quest))", re.IGNORECASE)
# Frontmatter no início da aula (não é conteúdo de estudo).
FRONTMATTER = re.compile(
    r"^(apresenta[çc][ãa]o|como estudar|sum[áa]rio|t[óo]picos da aula|sobre o (professor|curso)|metodologia|cronograma|"
    r"considera[çc][õo]es iniciais|abertura de curso|boas-vindas)",
    re.IGNORECASE,
)


def norm(s: str) -> str:
    """minúsculas, sem acento, só [a-z0-9]."""
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "", s.lower())


@lru_cache(maxsize=32)
def load_pages(key: str) -> dict:
    return json.loads((PAGES_DIR / f"{key}.json").read_text(encoding="utf-8"))


def available_keys() -> list[str]:
    return sorted(p.stem for p in Path(PAGES_DIR).glob("*.json"))


def aula_key_map() -> dict[str, str]:
    """aula_id -> chave do cache (lê só os cabeçalhos dos JSON)."""
    out = {}
    for k in available_keys():
        d = load_pages(k)
        out[d["aula"]] = k
    return out
