import json

with open('pipeline/.cache/material/questoes/direito-constitucional__m08.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

selected_ids = [
    # s01
    'tec_2921192', 'tec_3013401', 'tec_2973628',
    # s02
    'tec_3614169', 'tec_2509197', 'tec_2239055',
    # s03
    'tec_4090475', 'tec_3449185', 'tec_2900763',
    # s04
    'tec_2021134', 'tec_390659', 'mentoria_mcn_direito-constitucional_032_d70e7d',
    # s05
    'tec_3258322', 'tec_1223204', 'tec_841586',
    # s06
    'tec_3804310', 'tec_4022888', 'tec_3451187',
    # s07
    'tec_3015991', 'mentoria_mcn_direito-constitucional_035_165f90', 'mentoria_mcn_direito-constitucional_036_785b11'
]

q_map = {q['id']: q for q in data['questoes']}

for qid in selected_ids:
    q = q_map[qid]
    print(f"\n=======================================================")
    print(f"ID: {q['id']} | Cap: {q['capitulo']} | Gabarito: {q['gabarito']}")
    print(f"Enunciado:\n{q['enunciado']}")
    print("Alternativas:")
    for alt in q['alternativas']:
        print(f"  [{alt['letra']}] {alt['texto']}")
