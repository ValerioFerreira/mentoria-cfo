import json

with open('pipeline/.cache/material/questoes/direito-penal-militar__m03.json', encoding='utf-8') as f:
    d = json.load(f)

bank = {q['id']: q for q in d['questoes']}

selected = [
    # s01
    'tec_2524015', 'tec_2189375', 'mentoria_mcn_direito-penal-militar_035_04e954',
    # s02
    'tec_3571167', 'mentoria_mcn_direito-penal-militar_040_1f565f', 'mentoria_mcn_direito-penal-militar_042_05c9a0',
    # s03
    'tec_768357', 'mentoria_mcn_direito-penal-militar_046_ff33b0',
    # s04
    'tec_2130983', 'mentoria_mcn_direito-penal-militar_052_e19061',
    # s05
    'tec_3093029', 'tec_768358', 'mentoria_mcn_direito-penal-militar_059_777508',
    # s06
    'mentoria_mcn_direito-penal-militar_062_1ef71f', 'mentoria_mcn_direito-penal-militar_064_c9e1ae',
    # s07
    'mentoria_mcn_direito-penal-militar_069_99f3ec', 'mentoria_mcn_direito-penal-militar_070_75ce0b',
    # s08
    'tec_3571171', 'tec_2920958', 'tec_2524017'
]

for qid in selected:
    q = bank[qid]
    print(f"=== {qid} ({q['capitulo']}) ===")
    print(f"Gabarito: {q['gabarito']}")
    print(f"Enunciado: {q['enunciado'].strip()[:100]}...")
    for a in q.get('alternativas', []):
        print(f"  [{a['letra']}] {a['texto'].strip()[:70]}...")
    print()
