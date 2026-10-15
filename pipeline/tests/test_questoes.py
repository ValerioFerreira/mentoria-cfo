"""Importação dos cadernos do TecConcursos (pipeline/questoes): extrator, marcação e classificação.

Os testes de integração leem os PDFs de docs/questoes (fora do git) e são pulados quando a pasta não
existe. QUESTOES_TODOS=1 roda todos os cadernos (≈ 40 s); por padrão, só os dois menores.
"""
import json
import re
import os
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pipeline"))

from questoes import tec_pdf as T  # noqa: E402
from questoes.classify import Classifier, assunto_key, load_map, stem, tokens  # noqa: E402

DOCS = ROOT / "docs" / "questoes"


def span(text, x0, size=7.2, font="Tahoma", flags=0, base=200.0, color=0):
    w = len(text) * size * 0.5
    chars = []
    x = x0
    for c in text:
        chars.append((c, x, x + size * 0.5))
        x += size * 0.5
    return T.Span(text, font, size, flags, (x0, base - size, x0 + w, base + 2), base, color=color, chars=chars)


def row(*spans):
    f = T.Frag("text", 0, (min(s.bbox[0] for s in spans), min(s.bbox[1] for s in spans), max(s.bbox[2] for s in spans), max(s.bbox[3] for s in spans)), list(spans))
    return T.Row(0, [f])


# ───────────────────────── unidades ─────────────────────────


def test_cabecalho_banca_orgao_ano():
    m = T.parse_banca_line("Instituto AOCP - Tec (UFBA)/UFBA/Tecnologia da Informação/Técnico de Infraestrutura/2017")
    assert m == {"bancaRaw": "Instituto AOCP", "cargo": "Tec (UFBA)", "orgao": "UFBA", "area": "Tecnologia da Informação/Técnico de Infraestrutura", "ano": 2017}
    assert T.normalize_banca("Instituto AOCP") == T.normalize_banca("AOCP") == "AOCP"


def test_markup_negrito_sobrescrito_escape():
    r = row(span("Assinale a ", 28), span("INCORRETA", 70, font="Tahoma-Bold", flags=16), span(" sobre 2 * 3 e x", 110), span("2", 190, size=5.0, base=197.0))
    out = T.row_markup(r)
    assert "**INCORRETA**" in out
    assert "2 \\* 3" in out
    assert out.endswith("x<sup>2</sup>")


def test_markup_destaque_colorido_e_sublinhado():
    s = span("palavra", 28, color=0xFF0000)
    s.ul = set(range(3))
    out = T.row_markup(row(s))
    assert out == "<u><mark>pal</mark></u><mark>avra</mark>" or "<mark>" in out and "<u>" in out


def test_juncao_de_linhas_hifenizadas():
    assert T._join_lines(["tornou-", "se mais"]) == "tornou-se mais"
    assert T._join_lines(["Lei nº 8.069/1990 -", "ECA"]) == "Lei nº 8.069/1990 - ECA"


def test_itens_de_lista_comecam_linha():
    for t in ["• 20% das famílias", "( ) Afirmativa", "II. Segunda", "**I.** Primeira", "a) item"]:
        assert T.ITEM_START_RE.match(t), t
    assert not T.ITEM_START_RE.match("Assinale a alternativa")


def test_linha_com_formula_mathjax_vira_inline():
    r = row(span("intensidade ", 52), span("2.10", 120, font="Type3 (48 0 R)", size=11.1, base=200), span("−3", 140, font="Type3 (48 0 R)", size=7.8, base=196))
    T.classify_row(r)
    assert r.inline and not r.crop


def test_linha_so_de_formula_vira_recorte():
    r = row(span("f(x) =", 200, font="Type3 (22 0 R)", size=11.1))
    T.classify_row(r)
    assert r.crop


def test_tokens_e_radical():
    assert tokens("Ações") == tokens("acao") == ["acao"]  # sem acento, plural -ções -> -ção
    assert tokens("Constituição Federal") == ["constituicao", "federal"]
    assert stem("principais") == "principal"


def test_mapa_assuntos_valido():
    mapa = load_map()
    cat_aulas = {a["id"] for s in json.loads((ROOT / "content" / "catalog.json").read_text(encoding="utf-8"))["subjects"] for a in s["aulas"]}
    subjects = {s["id"] for s in json.loads((ROOT / "content" / "subjects.json").read_text(encoding="utf-8"))["subjects"]}
    for materia, subj in mapa["materias"].items():
        assert (subj if isinstance(subj, str) else subj["subject"]) in subjects, materia
    for key, e in mapa["assuntos"].items():
        assert "|" in key, key
        assert ("skip" in e) != bool(e.get("aulas") or e.get("segments")), key
        for a in e.get("aulas", []):
            assert a in cat_aulas, f"{key}: aula inexistente {a}"


def test_classificador_respeita_skip_e_mapa():
    class FakeCat:
        idf = {}
        aulas = {}
        segments = {}
        vec = {}
        aula_vec = {}
        edital_items = {}

    mapa = {"materias": {"Informática": "informatica"}, "assuntos": {"Informática|Linux / Unix": {"skip": "fora do edital"}}}
    c = Classifier(FakeCat(), mapa)
    r = c.classify({"materia": "Informática", "assunto": "Linux / Unix", "statement": "", "options": []})
    assert r.status == "SKIP" and r.reason == "fora do edital"
    r = c.classify({"materia": "Matéria Nova", "assunto": "X", "statement": "", "options": []})
    assert r.status == "SKIP" and "matéria sem mapa" in r.reason
    assert assunto_key("A", "B") == "A|B"


def test_fundo_branco_invisivel_nao_e_desenho():
    # retângulo branco sem contorno atrás do texto (fundo da página web) não pode virar figura
    assert T.is_invisible_fill({"fill": (1.0, 1.0, 1.0), "color": None})
    assert not T.is_invisible_fill({"fill": (1.0, 1.0, 1.0), "color": (0, 0, 0)})  # caixa com borda
    assert not T.is_invisible_fill({"fill": (0.0, 0.0, 0.0), "color": None})  # traço preto (tabela, sublinhado)
    assert not T.is_invisible_fill({"fill": None, "color": (0, 0, 0)})


def test_lacuna_de_espacos_sublinhados():
    s = span("acesso    e", 28)
    s.ul = {6, 7, 8, 9}  # 4 espaços sublinhados = lacuna
    assert T.row_markup(row(s)) == "acesso ______ e"
    one = span("palavra destacada", 28)
    one.ul = set(range(len("palavra destacada")))  # espaço isolado entre palavras sublinhadas não é lacuna
    assert "_" not in T.row_markup(row(one))
    assert T._join_lines(["garantido o acesso ______", "______ às ações"]) == "garantido o acesso ______ às ações"


def test_assertiva_em_negrito_abre_paragrafo():
    for t in ["**IV**. O pulmão esquerdo", "**III.** Os pulmões", "**2**. Segundo item"]:
        assert T.ITEM_START_RE.match(t), t


def test_item_do_edital_e_da_propria_disciplina():
    from questoes.classify import Catalog, SegInfo

    seg = SegInfo(id="estatistica/a06/s01", aula="estatistica/a06", subject="estatistica", order=1)
    seg.edital = [("matematica/e3.4", "probabilidade"), ("estatistica/e2.1", "probabilidade definicao classica")]
    cat = Catalog({seg.id: seg}, {}, {}, {"estatistica": {}}, {}, {})
    c = Classifier(cat, {"materias": {}, "assuntos": {}})
    assert c.edital_item(seg.id, {}) == "estatistica/e2.1"
    seg.edital = [("matematica/e3.4", "probabilidade")]
    cat.edital_items = {"estatistica/e2.3": {"subject": "estatistica", "aulas": ["estatistica/a06"], "text": "axiomatica"}}
    assert c.edital_item(seg.id, {}) == "estatistica/e2.3"


# ───────────────────────── integração (cadernos reais) ─────────────────────────

REF = DOCS / "Caderno Direito Administrativo Atualidades Espanhol Direito Penal Militar Inglês Física 1 .pdf"
FONETICA = DOCS / "Caderno Matemática e Português 5.pdf"


@pytest.mark.skipif(not REF.exists(), reason="caderno de referência ausente")
def test_caderno_de_referencia_regressoes_da_auditoria():
    """Casos da auditoria de 14/10/2026 (docs/questoes/auditoria/2026-10-14)."""
    c = T.read_caderno(REF)
    q = {x.tecId: x for x in c.questions}
    assert len(c.questions) == 200 and not c.anomalies
    assert q["1445847"].statement.count("______") == 3  # lacunas do ECA
    assert "______" in q["2906715"].statement
    assert "\n\n**IV**. O pulmão" in q["1444254"].statement  # assertivas em parágrafos próprios
    assert "a seguir.\n\nO monômero" in q["736572"].statement  # item de C/E depois da virada de página


@pytest.mark.skipif(not FONETICA.exists(), reason="caderno ausente")
def test_letra_destacada_com_sublinhado_curto_nao_vira_marcador():
    c = T.read_caderno(FONETICA)
    q = {x.tecId: x for x in c.questions}
    d = [o["text"] for o in q["863979"].options if o["label"] == "D"][0]
    assert "•" not in d and "<u>" in d
    for x in c.questions:
        txt = " ".join([x.support, x.statement] + [o["text"] for o in x.options])
        assert not re.search(r"[\wÀ-ÿ*]•[\wÀ-ÿ]", txt), x.tecId


@pytest.mark.skipif(not DOCS.joinpath("Caderno Matemática e Português 1.pdf").exists(), reason="caderno ausente")
def test_paragrafo_com_fundo_branco_continua_texto():
    c = T.read_caderno(DOCS / "Caderno Matemática e Português 1.pdf")
    q = {x.tecId: x for x in c.questions}
    assert "460 terawatt-hora" in q["3449630"].support  # antes virava imagem por causa do fundo branco


# Defeitos do próprio PDF (conferidos visualmente na auditoria de 14/10/2026): ficam em quarentena.
DEFEITOS_DA_FONTE = {
    "1437736",  # uma alternativa impressa sem letra (a, b, [sem letra], c, d) e gabarito E
    "2627578",  # o caderno traz só as alternativas, sem o comando da questão
}


def _cadernos():
    if not DOCS.exists():
        return []
    pdfs = sorted(DOCS.glob("*.pdf"), key=lambda p: p.stat().st_size)
    return pdfs if os.environ.get("QUESTOES_TODOS") else pdfs[:2]


@pytest.mark.skipif(not DOCS.exists(), reason="docs/questoes ausente")
@pytest.mark.parametrize("pdf", _cadernos(), ids=lambda p: p.name)
def test_invariantes_do_caderno(pdf):
    c = T.read_caderno(pdf)
    assert not c.anomalies, c.anomalies
    assert c.questions, "caderno sem questões"
    assert len(c.gabarito) == len(c.questions)
    for q in c.questions:
        if q.tecId in DEFEITOS_DA_FONTE:
            assert q.problems, f"{q.tecId} deveria continuar em quarentena"
            continue
        assert not q.problems, (q.tecId, q.problems)
        assert q.tecId.isdigit() and q.numero is not None
        assert q.banca and q.ano and q.materia
        assert q.statement or q.support
        if q.kind == "CERTO_ERRADO":
            assert [o["label"] for o in q.options] == ["C", "E"]
        else:
            assert "".join(o["label"] for o in q.options) in ("ABCD", "ABCDE"), q.tecId
            assert all(o["text"] for o in q.options), q.tecId
        if not q.anulada:
            assert q.answer in {o["label"] for o in q.options}, q.tecId
        for sha in q.assets:
            assert sha in c.assets
