import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from approval_profiles import parse_aocp, parse_cfo_list, parse_cfo_obj, parse_upe_ranked, summarize  # noqa: E402

AOCP = """NOME
INSCRIÇÃO
Fulano De Tal
3640000001
5.00
4.00
50.00
20.00
70.00
01/01/1990
1
-
Sicrano (Sub
Judice) Autos 0035734-
38.2024.8.17.2001
3640000002
3.00
2.00
40.00
15.00
55.00
02/02/1991
2
1
"""


def test_parse_aocp_le_notas_e_posicao():
    recs = parse_aocp([ln.strip() for ln in AOCP.split("\n")])
    assert [r["id"] for r in recs] == ["3640000001", "3640000002"]
    assert recs[0]["nums"] == [5.0, 4.0, 50.0, 20.0, 70.0]
    assert [r["rank"] for r in recs] == [1, 2]


def test_parse_upe_ranked():
    lines = ["ABEL", "750554", "55,00", "13,50", "68,50", "750º", "ADAM", "755946", "48,00", "3,50", "  ", "  "]
    assert parse_upe_ranked(lines) == [{"id": "750554", "obj": 55.0, "rank": 750}]


def test_cfo2018_cruza_aprovados_e_objetiva():
    obj_lines = ["OFICIAL DA POLÍCIA MILITAR DE PERNAMBUCO (PMPE)", "A", "202137", "53,00", "25,50", "78,50", "B", "207261", "46,00", "24,00", "70,00"]
    ok_lines = ["OFICIAL DA POLÍCIA MILITAR DE PERNAMBUCO (PMPE)", "A", "202137", "1º", "OFICIAL DO CORPO DE BOMBEIROS", "C", "207261", "2º"]
    assert parse_cfo_obj(obj_lines) == {("PM", "202137"): 53.0, ("PM", "207261"): 46.0}
    assert parse_cfo_list(ok_lines) == {"PM": ["202137"], "BM": ["207261"]}


def test_summarize():
    s = summarize([50.0, 40.0], 70)
    assert s["mean"] == 45.0 and s["min"] == 40.0 and s["max"] == 50.0
    assert s["meanPct"] == round(45 / 70, 3) and s["n"] == 2
