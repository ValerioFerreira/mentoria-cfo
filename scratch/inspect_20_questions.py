import json

with open('pipeline/.cache/material/questoes/biologia__m01.json', encoding='utf-8') as f:
    d = json.load(f)

bank = {q['id']: q for q in d['questoes']}

selected_ids = [
    # s01
    'tec_2856844', 'tec_2561949', 'tec_2567963',
    # s02
    'tec_3554761', 'tec_3262082', 'tec_2562698',
    # s03
    'tec_2031745', 'tec_1674284', 'mentoria_mcn_biologia_001_6a09df',
    # s04
    'tec_3558607', 'tec_3262081', 'tec_3262100',
    # s05
    'tec_3100299', 'tec_2178038', 'tec_959859',
    # s06
    'tec_3629174', 'tec_3140589', 'tec_625787',
    # s07
    'tec_3449695', 'tec_3262065'
]

for qid in selected_ids:
    q = bank[qid]
    print(f"=== {qid} ({q['capitulo']}) ===")
    print(f"Gabarito: {q['gabarito']}")
    print(f"Enunciado: {q['enunciado'].strip()[:120]}...")
    alts = q.get('alternativas', [])
    for a in alts:
        print(f"  [{a['letra']}] {a['texto'].strip()[:80]}...")
    print()
