import json

with open('pipeline/.cache/material/questoes/direito-penal-militar__m05.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

selected_ids = [
    # s01
    'tec_3093035', 'tec_2983133', 'mentoria_mcn_direito-penal-militar_104_b359be',
    # s02
    'tec_2983106', 'mentoria_mcn_direito-penal-militar_110_831119', 'mentoria_mcn_direito-penal-militar_111_f2dc9a',
    # s03
    'mentoria_mcn_direito-penal-militar_117_6a554d', 'mentoria_mcn_direito-penal-militar_118_4c65dc', 'mentoria_mcn_direito-penal-militar_119_f637ad',
    # s04
    'tec_2723535', 'mentoria_mcn_direito-penal-militar_124_678e65', 'mentoria_mcn_direito-penal-militar_125_59e351',
    # s05
    'mentoria_mcn_direito-penal-militar_131_f46ebc', 'mentoria_mcn_direito-penal-militar_132_1c8283', 'mentoria_mcn_direito-penal-militar_133_c0abc8',
    # s06
    'tec_3464758', 'tec_2782483', 'tec_2782484'
]

by_id = {q['id']: q for q in data['questoes']}

for qid in selected_ids:
    q = by_id[qid]
    print(f"=== {qid} ({q['capitulo']}) ===")
    print(f"Banca: {q.get('banca')} | Gab: {q.get('gabarito')} | Tipo: {q.get('tipo')}")
    print(f"Enunciado: {q.get('enunciado')[:150]}...")
    alts = q.get('alternativas', [])
    for a in alts:
        print(f"  {a['letra']}: {a['texto'][:60]}...")
