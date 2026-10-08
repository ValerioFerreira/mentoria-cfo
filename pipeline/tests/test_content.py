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


def test_exam_weights_match_edital(catalog):
    # Inglês e Espanhol são mutuamente exclusivos: o candidato faz só uma (5 questões)
    subjects = [s for s in catalog["subjects"] if s["id"] != "lingua-espanhola"]
    assert sum(s["examQuestions"] for s in subjects) == catalog["exam"]["totalQuestions"] == 70
    by_block = {}
    for s in subjects:
        by_block[s["block"]] = by_block.get(s["block"], 0) + s["examQuestions"]
    assert by_block == {"I": 20, "II": 20, "III": 30}


def test_all_190_aulas_present(catalog):
    # 190 aulas do Estratégia; as demais são complementos autorais do MentorIA (source = authored)
    assert sum(1 for s in catalog["subjects"] for a in s["aulas"] if a.get("source") != "authored") == 190


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
