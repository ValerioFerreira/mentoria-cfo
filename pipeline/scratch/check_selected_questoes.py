import json

data = json.load(open('pipeline/.cache/material/questoes/estatistica__m03.json', encoding='utf-8'))
qs_by_id = {q['id']: q for q in data['questoes']}

selected_ids = [
    # s01 (3)
    'tec_1415150', 'tec_3863449', 'tec_3598342',
    # s02 (6)
    'tec_3101199', 'tec_1674170', 'tec_1868104', 'tec_624615', 'tec_2629339', 'tec_1000796',
    # s03 (3)
    'tec_624616', 'tec_3616113', 'mentoria_mcn_estatistica_103_8644ad',
    # s04 (2)
    'tec_3318511', 'mentoria_mcn_estatistica_031_b56adb',
    # s05 (3)
    'tec_3836899', 'mentoria_mcn_estatistica_037_98b7f3', 'mentoria_mcn_estatistica_038_0aabbd',
    # s06 (3)
    'tec_3235813', 'tec_3400961', 'tec_2903422'
]

print(f"Total selecionadas: {len(selected_ids)}")
for qid in selected_ids:
    q = qs_by_id[qid]
    print(f"\n--- [{q['capitulo']}] {q['id']} - {q.get('banca')} - Gabarito: {q.get('gabarito')} ---")
    print("Enunciado:", q.get('enunciado')[:200].replace('\n', ' '))
    alts = q.get('alternativas', [])
    print(f"Num alts: {len(alts)}")
    for a in alts:
        print(f"  {a.get('letra')}: {str(a.get('texto'))[:80]}")
