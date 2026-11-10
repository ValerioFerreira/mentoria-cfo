import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from validate_material import (  # noqa: E402
    callouts,
    check_grafico,
    check_mermaid,
    check_molecula,
    check_svg,
    eval_expr,
    fences,
    fixacao_target,
    parse_front_matter,
    strip_lei,
    word_count,
)


def test_front_matter_json_values():
    meta, body, errs = parse_front_matter('---\nid: "x/a00/s01"\ncapitulo: 2\nfontes: ["CF/88 — planalto.gov.br — 2026-10-28"]\n---\nTexto.\n')
    assert errs == []
    assert meta == {"id": "x/a00/s01", "capitulo": 2, "fontes": ["CF/88 — planalto.gov.br — 2026-10-28"]}
    assert body == "Texto.\n"


def test_front_matter_rejects_bare_text():
    _, _, errs = parse_front_matter("---\ntitulo: Sem aspas\n---\n")
    assert errs and "JSON" in errs[0]


def test_callouts_and_strip_lei():
    body = "Intro.\n\n> [!lei] CF, art. 5º, LXIX\n> texto literal da norma\n\n> [!bizu]\n> dica\n\nFim."
    cos = callouts(body)
    assert [(c["type"], c["title"]) for c in cos] == [("lei", "CF, art. 5º, LXIX"), ("bizu", "")]
    stripped = strip_lei(body)
    assert "literal" not in stripped and "dica" in stripped


def test_fences_are_removed_from_word_count():
    body = "Um dois três.\n\n```svg Legenda da figura\n<svg viewBox='0 0 1 1'><text>a b c d e f</text></svg>\n```\n\nQuatro."
    text, blocks = fences(body)
    assert blocks[0]["lang"] == "svg" and blocks[0]["caption"] == "Legenda da figura"
    assert word_count(text) == 4


def test_eval_expr_is_safe():
    assert eval_expr("2*x**2 - 3", 2) == 5
    assert abs(eval_expr("sin(pi/2)", 0) - 1) < 1e-9
    with pytest.raises(ValueError):
        eval_expr("__import__('os').system('dir')", 0)
    with pytest.raises(ValueError):
        eval_expr("x.real", 1)


def test_grafico_specs():
    assert check_grafico('{"tipo": "funcao", "titulo": "Parábola", "dominio": [-3, 3], "funcoes": [{"expr": "x**2", "rotulo": "f"}]}') == []
    assert check_grafico('{"tipo": "barras", "titulo": "T", "categorias": ["a", "b"], "series": [{"rotulo": "s", "valores": [1]}]}')
    assert check_grafico('{"tipo": "pizza"}')
    assert check_grafico("{nao e json}")


def test_svg_rules():
    ok = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 50"><rect width="10" height="10" fill="#000"/><text x="1" y="9">F</text></svg>'
    assert check_svg(ok) == []
    assert any("viewBox" in e for e in check_svg('<svg xmlns="http://www.w3.org/2000/svg"><text>x</text></svg>'))
    assert any("proibido" in e for e in check_svg(ok.replace("<rect", "<script>alert(1)</script><rect")))


def test_mermaid_and_molecula():
    assert check_mermaid("flowchart TD\n  A --> B") == []
    assert check_mermaid("A --> B")
    assert check_molecula('{"smiles": "CCO", "rotulo": "etanol"}') == []
    assert check_molecula('{"smiles": "C C O"}')


def test_fixacao_target():
    assert fixacao_target(2) == (12, 20)
    assert fixacao_target(5) == (15, 20)
    assert fixacao_target(8) == (20, 20)
