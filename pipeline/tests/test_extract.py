import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from config import aula_id, parse_pdf_name, pdf_key  # noqa: E402
from extract import clean_page_text  # noqa: E402

RAW = """Ena Smith Aula 02

CONJUNÇÕES

As conjunções (conjunctions) são palavras que precisam juntar-se a outras. ==39ea13==
Exemplo: She had a headache, but she went.

CBM-PE (Oficial) Língua Inglesa

2

www.estrategiaconcursos.com.br

150

10341953440 - Valério Ferreira de Albuquerque Filho
"""


def test_clean_removes_footer_watermark_header():
    out = clean_page_text(RAW)
    assert "10341953440" not in out
    assert "Valério" not in out
    assert "estrategiaconcursos" not in out
    assert "CBM-PE (Oficial)" not in out
    assert "Ena Smith" not in out
    assert "==39ea13==" not in out
    assert out.startswith("CONJUNÇÕES")
    assert "but she went." in out


def test_clean_keeps_numeric_content_lines():
    raw = "Aula 01\n\n42\n\n3,14\n"
    assert "42" in clean_page_text("Prof Fulano Aula 01\n\n42\n\n3,14\n")
    assert raw  # sanity


def test_parse_pdf_name_and_ids():
    assert parse_pdf_name("002 - Aula 01 Substantivos, Artigos.pdf") == (2, 1)
    assert parse_pdf_name("edital-cfo.pdf") is None
    assert aula_id("dir-administrativo", 0) == "dir-administrativo/a00"
    assert pdf_key("02 - CBM-PE (Oficial) Direito Administrativo", "004 - Aula 03.pdf") == "02_004"
