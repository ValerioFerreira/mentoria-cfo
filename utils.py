import re
import unicodedata
from pathlib import Path


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def safe_name(value: str, fallback: str = "sem título", max_length: int = 100) -> str:
    value = unicodedata.normalize("NFKC", clean_text(value))
    value = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", value)
    value = re.sub(r"\s+", " ", value).strip(" .")
    return (value or fallback)[:max_length]


def valid_pdf(path: Path) -> bool:
    try:
        with path.open("rb") as f:
            return f.read(5) == b"%PDF-"
    except OSError:
        return False

