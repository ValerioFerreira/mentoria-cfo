import json
from pathlib import Path

f = Path("pipeline/.cache/material/questoes/biologia__m09.json")
data = json.loads(f.read_text(encoding="utf-8"))["questoes"]

chosen_ids = [
    # s01 (2)
    "tec_3449724", "tec_3449736",
    # s02 (2)
    "tec_3449691", "tec_3098300",
    # s03 (2)
    "tec_3449717", "tec_3449745",
    # s04 (2)
    "tec_3449721", "tec_3536083",
    # s05 (3)
    "tec_3536079", "tec_3554832", "tec_3262093",
    # s06 (3)
    "tec_1902627", "tec_1225163", "tec_607670",
    # s07 (3)
    "tec_3449681", "tec_177692", "tec_177693",
    # s08 (3)
    "tec_3449683", "tec_3449742", "tec_3554792"
]

by_id = {q["id"]: q for q in data}

for qid in chosen_ids:
    q = by_id[qid]
    print("=" * 60)
    print(f"ID: {q['id']} | CAP: {q['capitulo']} | GAB: {q['gabarito']} | BANCA: {q['banca']} | ANO: {q['ano']}")
    print("ENUNCIADO:")
    print(q["enunciado"])
    print("ALTERNATIVAS:")
    for a in q["alternativas"]:
        print(f"  {a['letra']}) {a['texto']}")
