"""Invariantes do conteúdo estrutural versionado em content/ (rodam na CI, sem precisar de docs/)."""
import json
from pathlib import Path

import pytest

CONTENT = Path(__file__).resolve().parents[2] / "content"


@pytest.fixture(scope="module")
def catalog():
    return json.loads((CONTENT / "catalog.json").read_text(encoding="utf-8"))


def _segments(subject_id):
    return json.loads((CONTENT / "segments" / f"{subject_id}.json").read_text(encoding="utf-8"))["segments"]


OFICIAL_IDS = {
    "lingua-portuguesa", "lingua-inglesa", "informatica", "matematica", "estatistica",
    "fisica", "quimica", "biologia", "direito-constitucional", "direito-administrativo",
    "direito-penal-militar", "legislacoes-pe"
}
PRACA_IDS = {
    "lingua-portuguesa", "raciocinio-logico", "historia-pe", "atualidades",
    "informatica", "biologia", "direito-constitucional", "legislacoes-pe"
}


def test_exam_weights_match_edital(catalog):
    # CFO-BM Oficial: Inglês e Espanhol são mutuamente exclusivos (70 questões no total do edital)
    subjects = [s for s in catalog["subjects"] if s["id"] in OFICIAL_IDS]
    assert sum(s["examQuestions"] for s in subjects) == catalog["exam"]["totalQuestions"] == 70
    by_block = {}
    for s in subjects:
        by_block[s["block"]] = by_block.get(s["block"], 0) + s["examQuestions"]
    assert by_block == {"I": 20, "II": 20, "III": 30}


def test_all_213_aulas_present(catalog):
    # 190 aulas de Oficial + 23 aulas de Praça do Estratégia = 213 aulas base
    assert sum(1 for s in catalog["subjects"] for a in s["aulas"] if a.get("source") != "authored") == 213


def test_segments_never_exceed_17_pages_and_cover_theory_exactly(catalog):
    for subj in catalog["subjects"]:
        segs = _segments(subj["id"])
        ids = [s["id"] for s in segs]
        assert len(ids) == len(set(ids)), f"ids duplicados em {subj['id']}"
        by_aula = {}
        for s in segs:
            assert 1 <= s["pages"] <= 17, s["id"]
            assert s["endPage"] - s["startPage"] + 1 == s["pages"]
            by_aula.setdefault(s["aula"], []).append(s)
        for aula in subj["aulas"]:
            pages = []
            for s in sorted(by_aula.get(aula["id"], []), key=lambda x: x["order"]):
                pages.extend(range(s["startPage"], s["endPage"] + 1))
            assert len(pages) == len(set(pages)), f"segmentos sobrepostos em {aula['id']}"
            assert len(pages) == aula["theoryPages"], f"cobertura da teoria em {aula['id']}"
            assert len(by_aula.get(aula["id"], [])) == aula["segmentCount"]


def test_out_of_edital_aulas_have_zero_incidence(catalog):
    for subj in catalog["subjects"]:
        for a in subj["aulas"]:
            assert (a["incidence"] == 0) == (not a["selectable"])
            if a["edital"] == "no":
                assert not a["selectable"]


def test_incidence_sums_to_one_per_subject(catalog):
    for subj in catalog["subjects"]:
        total = sum(a["incidence"] for a in subj["aulas"])
        assert 0.4 < total <= 1.0001, (subj["id"], total)


def test_language_group_is_exclusive_pair(catalog):
    langs = [s["id"] for s in catalog["subjects"] if s.get("languageGroup") == "lingua-estrangeira"]
    assert sorted(langs) == ["lingua-espanhola", "lingua-inglesa"]


def test_authored_items_pass_validator():
    """Bizus e questões autorais: esquema, gabarito, mínimos e duplicatas (a originalidade só roda com o cache local)."""
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from validate_content import ITEMS_DIR, validate_file

    seen: dict[str, list] = {}
    problems = []
    for f in sorted(ITEMS_DIR.glob("*/*.json")):
        errs, _warns, _st = validate_file(f, seen.setdefault(f.parent.name, []))
        problems += [f"{f.parent.name}/{f.name}: {e}" for e in errs]
    assert not problems, "\n".join(problems[:30])


def _bizu_doc(pointers):
    ce = lambda n, t: {"statement": f"Afirmação autoral número {n} sobre o tema do trecho, escrita com palavras próprias.", "isTrue": t, "explanation": f"Explicação autoral {n} do porquê o item está certo ou errado."}  # noqa: E731
    return {
        "aula": "legislacoes-pe/a01", "batch": "teste", "status": "DRAFT", "stage": "bizu",
        "segments": [{"id": "legislacoes-pe/a01/s01", "bizu": {
            "summary": [f"**Tópico autoral {i}** com redação própria e sem relação com o material de origem." for i in range(7)],
            "teoria": [ce(1, True), ce(2, False), ce(3, True)], "revisao": [ce(4, False), ce(5, True), ce(6, False)],
            "pointers": pointers}}],
    }


def test_bizu_stage_needs_pointers_and_no_questions(tmp_path):
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from validate_content import validate_file

    good = _bizu_doc([{"topic": f"Ponto {i}", "pageRef": 5 + i} for i in range(4)])
    f = tmp_path / "a01.json"
    f.write_text(json.dumps(good), encoding="utf-8")
    errs, _, _ = validate_file(f)
    assert not errs, errs

    bad = _bizu_doc([{"topic": "Só um", "pageRef": 5}])
    f.write_text(json.dumps(bad), encoding="utf-8")
    assert any("pointers" in e for e in validate_file(f)[0])

    out = _bizu_doc([{"topic": f"Ponto {i}", "pageRef": 99} for i in range(4)])
    f.write_text(json.dumps(out), encoding="utf-8")
    assert any("fora do trecho" in e for e in validate_file(f)[0])
