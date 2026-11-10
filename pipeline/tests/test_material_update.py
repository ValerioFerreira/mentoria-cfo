import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import material_update_index as mui  # noqa: E402
import material_watch  # noqa: E402
from validate_material import fixacao_range, neutrality  # noqa: E402


def test_neutrality_flags_direction_and_banca_only():
    errs, warns = neutrality("Este volume é voltado para o concurso de Oficiais do CBMPE. O Instituto AOCP costuma cobrar isso.")
    assert any("direciona" in e for e in errs) and any("AOCP" in e for e in errs)
    assert any("CBMPE" in w for w in warns)
    ok, _ = neutrality("O concurso de agentes exige liame subjetivo. Em concurso público, o edital vincula as partes.")
    assert ok == []
    # quadro [!lei] é a letra da lei: fica fora
    assert neutrality("> [!lei] LC 470/2021, art. 7º\n> O ingresso no CFOA dar-se-á por concurso para oficiais.\n")[0] == []
    assert neutrality("Se você está se preparando para a prova, revise.")[0]


def test_fixacao_range_uses_meta_and_bank(tmp_path, monkeypatch):
    import json

    import validate_material as vm

    (tmp_path / "metrics").mkdir()
    (tmp_path / "metrics" / "_fixacao.json").write_text(json.dumps(
        {"volumes": {"x/m01": {"meta": 10, "porCapitulo": {"x/a00/s01": 6, "x/a00/s02": 4}}}}), encoding="utf-8")
    monkeypatch.setattr(vm, "MATERIAL_DIR", tmp_path)
    lo, hi, caps = fixacao_range({"id": "x/m01", "chapters": 2}, {"x/a00/s01": 3, "x/a00/s02": 9})
    assert caps == {"x/a00/s01": 3, "x/a00/s02": 4} and lo == 7 and hi == 12
    assert fixacao_range({"id": "y/m01", "chapters": 2}, None)[:2] == (12, 20)


def test_index_items_norms_juris_and_sensitive(monkeypatch):
    monkeypatch.setattr(mui, "article_text", lambda k, n: f"Art. {n}. texto de {k}")
    text = ("---\ntitulo: \"T\"\n---\nA regra está na CF, art. 5º, LXIX. A Súmula 473 do STF trata da autotutela.\n"
            "A ação está pendente de julgamento no STF (ADI 7881). A unidade opera de modo independente.\n")
    it = mui.chapter_items(text, with_hash=True)
    assert [(n["lei"], n["art"]) for n in it["normas"]] == [("cf", "5")] and it["normas"][0]["sha"]
    assert any("473" in j for j in it["jurisprudencia"]) and any("ADI 7881" in j for j in it["jurisprudencia"])
    assert len(it["sensiveis"]) == 1 and "pendente" in it["sensiveis"][0]


def test_watch_detects_changed_article(monkeypatch):
    idx = {"geradoEm": "2026-11-02T00:00", "normas": {"cf": {}}, "volumes": {"d/m01": {"volatilidade": "ALTA", "capitulos": {
        "d/a00/s01": {"arquivo": "f.md", "titulo": "T", "jurisprudencia": [], "sensiveis": [],
                      "normas": [{"lei": "cf", "art": "5", "sha": mui.sha("Art. 5. antigo")},
                                 {"lei": "cf", "art": "6", "sha": mui.sha("Art. 6. igual")}]}}}}}
    monkeypatch.setattr(mui, "article_text", lambda k, n: {"5": "Art. 5. NOVA REDAÇÃO", "6": "Art. 6. igual"}[n])
    ch = material_watch.diff(idx)
    assert [(c["lei"], c["art"], c["situacao"]) for c in ch] == [("cf", "5", "texto mudou")]
    assert "cf art. 5" in material_watch.report(idx, ch)
