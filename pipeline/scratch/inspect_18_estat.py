import json
from pathlib import Path

f = Path("pipeline/.cache/material/questoes/estatistica__m07.json")
data = json.loads(f.read_text(encoding="utf-8"))["questoes"]
by_id = {q["id"]: q for q in data}

chosen_ids = [
    # s01 (2): 1 AOCP + 1 MentorIA
    "tec_1420405", "mentoria_mcn_estatistica_190_1a139b",
    # s02 (2): 2 MentorIA
    "mentoria_mcn_estatistica_197_ef4e1c", "mentoria_mcn_estatistica_198_076347",
    # s03 (2): 2 MentorIA
    "mentoria_mcn_estatistica_204_bf706e", "mentoria_mcn_estatistica_205_c842a9",
    # s04 (8): 8 AOCP
    "tec_2853875", "tec_2987537", "tec_2987554", "tec_3104084",
    "tec_1674169", "tec_1674230", "tec_1868108", "tec_1868109",
    # s05 (2): 2 MentorIA
    "mentoria_mcn_estatistica_211_b116a2", "mentoria_mcn_estatistica_212_92291a",
    # s06 (2): 2 MentorIA
    "mentoria_mcn_estatistica_218_706c4a", "mentoria_mcn_estatistica_219_60a8bd"
]

print(f"Total escolhidas: {len(chosen_ids)}")
for qid in chosen_ids:
    q = by_id[qid]
    print("=" * 60)
    print(f"ID: {qid} | CAP: {q['capitulo']} | BANCA: {q['banca']} | GAB: {q['gabarito']} | TIPO: {q['tipo']}")
    print(f"Enunciado: {q['enunciado']}")
    if q['tipo'] == 'MULTIPLA_ESCOLHA':
        for a in q['alternativas']:
            print(f"  {a['letra']}) {a['texto']}")
    elif q['tipo'] == 'CERTO_ERRADO':
        print("  Item Certo/Errado")
