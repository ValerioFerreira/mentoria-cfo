import json
import os
import shutil
import sys
from pathlib import Path

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from material_pdf import figures, render_md  # noqa: E402
from material_pdf.assemble import band_rect_pt, build_html  # noqa: E402
from material_pdf.load import Chapter, ContentError, Question, Volume, _norm_answer, _origin  # noqa: E402
from validate_material import parse_front_matter  # noqa: E402

FIX = Path(__file__).parent / "fixtures" / "material"


def _chapter():
    meta, body, errs = parse_front_matter((FIX / "a01-s01.md").read_text(encoding="utf-8"))
    assert errs == []
    return Chapter(trecho="teste/a01/s01", number=1, title=meta["titulo"], path=FIX / "a01-s01.md", meta=meta, body=body,
                   importance=80, tier="ALTA")


def _volume():
    v = Volume(id="teste/m01", subject="teste", subject_name="Disciplina de Teste", number=1, title="Volume de teste",
               subtitle="Subtítulo", wave=1, contests=["CBMPE_CFOA"], contest_labels=["2º Tenente CFOA · CBMPE"], dir=FIX,
               intro={"Apresentação": "Apresentação inventada.", "O que você vai aprender": "- Uma coisa."})
    v.chapters = [_chapter()]
    v.questions = [
        Question(id="q1", number=1, chapter="teste/a01/s01", kind="MULTIPLA_ESCOLHA", origin="AOCP 2024 · CBMPE", base_text=None,
                 statement="Assinale a **correta** e o <u>sublinhado</u>.", options=[("A", "um"), ("B", "dois")], answer="B",
                 comment="Comentário.", option_comments={"A": "Errada.", "B": "Certa."}),
        Question(id="q2", number=2, chapter="teste/a01/s01", kind="CERTO_ERRADO", origin="Inédita MentorIA", base_text=None,
                 statement="Afirmação.", options=[], answer="Certo", comment="Está certa.", option_comments={}),
    ]
    v.statuses = {"x": "APROVADO"}
    return v


def test_callouts_labels_and_mascot_once_per_section():
    r = render_md.render_chapter(_chapter().body, 1, "cap1", FIX / "a01-s01.md")
    body = r.body_html
    assert body.count('class="co atencao has-m"') == 1  # o segundo [!atencao] seguido não repete o mascote
    assert body.count('class="co atencao"') == 1
    assert "Fique atento!" in body and "Prazo fictício" in body
    assert 'class="co lei"' in body and "Letra da lei · " in body and "has-m" not in body.split('class="co lei')[1][:5]


def test_sections_numbered_and_map():
    r = render_md.render_chapter(_chapter().body, 3, "cap3", FIX / "a01-s01.md")
    assert [s[0] for s in r.sections] == ["3.1", "3.2"]
    assert r.sections[1][1] == "Mapa do capítulo"
    assert r.fixar == ["Primeiro ponto.", "Segundo ponto."]
    assert 'class="sec mapa"' in r.body_html
    assert len(r.objectives) == 2 and "<strong>atenção</strong>" in r.objectives[0]


def test_table_list_bold_italic_formula_and_figure_caption():
    r = render_md.render_chapter(_chapter().body, 1, "cap1", FIX / "a01-s01.md")
    b = r.body_html
    assert '<table class="tb">' in b and "<th>Item</th>" in b
    assert "<ul>" in b and "<strong>negrito</strong>" in b and "<em>itálico</em>" in b
    assert '<div class="formula">x² + y² = r²</div>' in b
    assert "<b>Figura 1.1</b> — Fluxo inventado de teste" in b
    assert 'class="mmd"' in b and "XQBLOCK" not in b


def test_question_html_underline_and_figure(tmp_path, monkeypatch):
    h = render_md.question_html("Texto **forte** e <u>sublinhado</u> <script>x</script>")
    assert "<strong>forte</strong>" in h and "<u>sublinhado</u>" in h and "<script>" not in h
    sha = "a" * 64
    monkeypatch.setattr(render_md, "QIMG_DIR", tmp_path)
    with pytest.raises(ContentError):
        render_md.question_html(f"![Figura](/q-img/{sha})")
    (tmp_path / f"{sha}.png").write_bytes(b"\x89PNG")
    assert 'class="qimg"' in render_md.question_html(f"![Figura](/q-img/{sha})")


@pytest.mark.parametrize("spec", [
    {"tipo": "funcao", "titulo": "f", "dominio": [-2, 2], "funcoes": [{"expr": "x**2", "rotulo": "f"}], "pontos": [{"x": 0, "y": 0, "rotulo": "v"}]},
    {"tipo": "linhas", "titulo": "l", "series": [{"rotulo": "a", "x": [1, 2], "y": [3, 4]}]},
    {"tipo": "dispersao", "titulo": "d", "series": [{"rotulo": "a", "x": [1, 2], "y": [3, 4]}]},
    {"tipo": "barras", "titulo": "b", "categorias": ["x", "y"], "series": [{"rotulo": "a", "valores": [1, 2]}]},
    {"tipo": "setores", "titulo": "s", "categorias": ["x", "y"], "valores": [1, 3]},
    {"tipo": "histograma", "titulo": "h", "classes": [[0, 1], [1, 2]], "frequencias": [2, 5]},
])
def test_grafico_svg(spec):
    svg = figures.grafico(json.dumps(spec))
    assert svg.startswith("<svg") and "Public Sans" in svg


def test_grafico_invalido():
    with pytest.raises(ContentError):
        figures.grafico('{"tipo": "funcao", "titulo": "x", "dominio": [1, 0], "funcoes": []}')


def test_svg_autoral_prefixa_ids():
    s = figures.svg_autoral('<svg viewBox="0 0 10 10"><defs><marker id="ah"/></defs><line marker-end="url(#ah)"/><text>t</text></svg>', "f1")
    assert 'id="f1-ah"' in s and "url(#f1-ah)" in s


def test_origin_and_answers():
    assert _origin({"banca": "AOCP", "ano": 2024, "orgao": "CBMPE"}) == "AOCP 2024 · CBMPE"
    assert _origin({}) == "Inédita MentorIA"
    assert _norm_answer("C", "CERTO_ERRADO") == "Certo" and _norm_answer("c", "MULTIPLA_ESCOLHA") == "C"


def test_band_rect_is_centered_95mm():
    x0, y0, x1, y1 = band_rect_pt()
    assert abs((x0 + x1) / 2 - 595.28 / 2) < 0.1
    assert abs((x1 - x0) - 95 * 72 / 25.4) < 0.1 and abs((y1 - y0) - 6 * 72 / 25.4) < 0.1


def test_build_html_volume():
    html_, info = build_html(_volume())
    assert "Volume 01" in html_ or "VOLUME 01" in html_
    assert 'id="cap1"' in html_ and 'id="questoes"' in html_ and 'id="mapa"' in html_ and 'id="cap1-corpo"' in html_
    assert 'id="comentarios"' not in html_  # o comentário vem logo abaixo de cada questão
    assert "Questão 1 · AOCP 2024 · CBMPE · Múltipla escolha" in html_ and "Certo ou errado" in html_
    assert "Aula " not in html_
    assert info["questions"] == [(1, "B"), (2, "Certo")]
    assert info["chapters"][0]["sections"][0][0] == "1.1"


def test_comment_right_after_each_question():
    html_, _ = build_html(_volume())
    q1, q2 = html_.index('id="q1"'), html_.index('id="q2"')
    assert q1 < html_.index("Gabarito <span class=\"g\">B</span>", q1) < q2
    assert html_.index("Gabarito <span class=\"g\">Certo</span>", q2) > q2


def test_no_contest_mentions_and_site_in_footer():
    html_, _ = build_html(_volume())
    body = html_.split("<body>", 1)[1].split("<script>", 1)[0].lower()
    assert "concurso" not in body and "cbmpe" not in body.replace("aocp 2024 · cbmpe", "")
    assert "www.missaomentoria.com.br" in html_
    assert "class=\"stats\"" not in html_.split('id="fim"', 1)[1]  # página final sem os cards
    assert "Material atualizado em: " in html_.split('id="fim"', 1)[1]


def test_tapes_are_solid_svg_and_breaks_prepass():
    html_, _ = build_html(_volume())
    assert "repeating-linear-gradient" not in html_
    css = (Path(__file__).parents[2] / "design" / "material" / "prontidao" / "prontidao.css").read_text(encoding="utf-8")
    assert "repeating-linear-gradient" not in css
    assert html_.count('class="tape-svg"') >= 2 and "function prepass()" in html_ and "compact-2" in html_


def test_colors_only_from_site_palette():
    import re as _re
    root = Path(__file__).parents[2]
    site = set(_re.findall(r"#[0-9a-f]{6}\b", (root / "web" / "src" / "app" / "globals.css").read_text(encoding="utf-8").lower()))
    site |= {"#ffffff"}
    files = [root / "design" / "material" / "prontidao" / n for n in ("prontidao.css", "template.html.j2")]
    files += [root / "pipeline" / "material_pdf" / n for n in ("assemble.py", "figures.py", "render_md.py")]
    used = {c for f in files for c in _re.findall(r"#[0-9a-f]{6}\b", f.read_text(encoding="utf-8").lower())}
    assert used - site == set()


@pytest.mark.skipif(shutil.which("node") is None and not os.environ.get("CI_CHROMIUM"), reason="sem ambiente")
def test_pdf_integration(tmp_path):
    pw = pytest.importorskip("playwright.sync_api")
    try:
        with pw.sync_playwright() as p:
            p.chromium.launch().close()
    except Exception:  # noqa: BLE001
        pytest.skip("Chromium do Playwright não instalado")
    from material_pdf.postprocess import check, finish
    from material_pdf.printpdf import print_pdf

    v = _volume()
    html_, info = build_html(v)
    hp = tmp_path / "v.html"
    hp.write_text(html_, encoding="utf-8")
    pdf = tmp_path / "v.pdf"
    pages = print_pdf(hp, pdf, timeout_s=120)
    pm, errors, warns = finish(pdf, v, info, pages, sample_stamp=False)
    assert pm["total"] >= 7
    assert not [e for e in errors if "faixa do titular" in e]
    assert not [e for e in errors if "fontes" in e]
    assert errors == [], errors
    errs2, _ = check(pdf, v, info, pm)
    assert errs2 == []
