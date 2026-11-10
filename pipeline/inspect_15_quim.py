import sys, json
sys.stdout.reconfigure(encoding="utf-8")

with open("pipeline/.cache/material/questoes/quimica__m01.json", encoding="utf-8") as f:
    data = json.load(f)

bank_qs = {q["id"]: q for q in data["questoes"]}

selected_15 = [
    # a00/s01
    "mentoria_mcn_quimica_021_cbaa75", "mentoria_mcn_quimica_022_1f00d7", "mentoria_mcn_quimica_025_9bdd47",
    # a00/s02
    "mentoria_mcn_quimica_028_4e782b", "mentoria_mcn_quimica_030_bb2274", "mentoria_mcn_quimica_031_396e38",
    # a00/s03
    "mentoria_mcn_quimica_035_97ca36", "mentoria_mcn_quimica_036_1e146d", "mentoria_mcn_quimica_038_2cd1b8",
    # a00/s04
    "mentoria_mcn_quimica_042_d755ba", "mentoria_mcn_quimica_044_1390e6", "mentoria_mcn_quimica_045_35b2da",
    # a00/s05
    "mentoria_mcn_quimica_049_ae1ca0", "mentoria_mcn_quimica_050_2261f2", "mentoria_mcn_quimica_051_877de3"
]

for qid in selected_15:
    q = bank_qs[qid]
    print(f"ID: {qid} | Cap: {q['capitulo']} | Gab: {q['gabarito']}")
    print(f"Enunciado: {q['enunciado']}")
    for a in q['alternativas']:
        print(f"  {a['letra']}: {a['texto']}")
    print("-" * 50)
