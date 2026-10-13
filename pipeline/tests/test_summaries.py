"""Regras do validador de resumos (originalidade por trechos, “Para fixar”) e da nota de cobertura. Não dependem de docs/."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from summary_coverage import coverage_of, tokens, verdict  # noqa: E402
from validate_content import SHINGLE_N, shingles, words  # noqa: E402
from validate_summaries import COPY_RUN_ERROR, check_fixar, copied_runs, is_trivial_run  # noqa: E402

SENTENCE = "o direito administrativo regula a atividade da administracao publica e os seus agentes em todas as esferas"


def test_copied_run_is_the_whole_contiguous_copy():
    source = shingles(SENTENCE)
    runs = copied_runs("introducao propria " + SENTENCE + " e depois texto novo", source)
    assert len(runs) == 1 and len(runs[0]) == len(words(SENTENCE))


def test_short_coincidence_is_below_the_error_threshold_but_long_copy_is_not():
    ten = " ".join(words(SENTENCE)[:SHINGLE_N])
    assert len(copied_runs(ten, shingles(SENTENCE))[0]) == SHINGLE_N < COPY_RUN_ERROR
    assert len(copied_runs(SENTENCE, shingles(SENTENCE))[0]) >= COPY_RUN_ERROR


def test_numeric_and_repetitive_runs_do_not_count():
    assert is_trivial_run("1 1 2 3 5 8 13 21 34 55".split())
    assert is_trivial_run("x y x y x y x y x y".split())
    assert not is_trivial_run(words(SENTENCE))


def _fixar(items: int | None, paragraph: bool = False) -> list[str]:
    body = "### Tema\ntexto\n"
    if items is not None:
        body += "### Para fixar\n" + ("um paragrafo corrido sem lista\n" if paragraph else "".join(f"- ponto {i}\n" for i in range(items)))
    errors: list[str] = []
    check_fixar("x/a01/s01", body, errors)
    return errors


def test_para_fixar_needs_five_to_eight_list_items():
    assert _fixar(5) == [] and _fixar(8) == []
    assert _fixar(4) and _fixar(9)
    assert _fixar(0, paragraph=True)
    assert "falta" in _fixar(None)[0]


def test_numbered_items_count():
    errors: list[str] = []
    check_fixar("x", "### Para fixar\n" + "".join(f"{i}. ponto\n" for i in range(1, 6)), errors)
    assert errors == []


def test_coverage_counts_plural_and_missing_terms_by_weight():
    salient = {"licitacao": 5.0, "dispensa": 3.0, "pregao": 1.0}
    score, missing = coverage_of("Licitações e dispensas", salient)  # plural cobre o singular pelos 6 primeiros caracteres
    assert round(score, 2) == round(8 / 9, 2)
    assert missing == ["pregao"]
    assert tokens("Atenção, ÁGUA!") == ["atencao", "agua"]


def test_verdict_uses_position_and_absolute_note_but_not_absolute_for_languages():
    assert verdict("informatica", 0.35, 0.9, 0.5) == "REVISAR"  # nota baixa mesmo no meio da disciplina (lote inteiro fraco)
    assert verdict("informatica", 0.35, 0.9, 0.2) == "REFAÇÃO"  # e curto demais
    assert verdict("informatica", 0.9, 0.05, 0.9) == "REVISAR"  # entre os piores da disciplina
    assert verdict("informatica", 0.9, 0.9, 0.9) == "OK"
    assert verdict("lingua-inglesa", 0.25, 0.6, 0.5) == "OK"  # a nota absoluta não vale em Inglês
    assert verdict("lingua-inglesa", 0.25, 0.05, 0.5) == "REVISAR"
