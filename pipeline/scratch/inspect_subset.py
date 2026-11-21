import json
from pathlib import Path

f = Path("pipeline/.cache/material/questoes/biologia__m09.json")
data = json.loads(f.read_text(encoding="utf-8"))["questoes"]
by_id = {q["id"]: q for q in data}

chosen = [
    'tec_3449717', 'tec_3449745', 'tec_3449721', 'tec_3536083',
    'tec_3536079', 'tec_3554832', 'tec_3262093', 'tec_1902627',
    'tec_1225163', 'tec_607670', 'tec_3449681', 'tec_177692', 'tec_177693'
]

for qid in chosen:
    q = by_id[qid]
    print(f"=== {qid} ({q['capitulo']}) gab={q['gabarito']} ===")
    print(q["enunciado"])
    for a in q["alternativas"]:
        print(f"  {a['letra']}) {a['texto']}")
