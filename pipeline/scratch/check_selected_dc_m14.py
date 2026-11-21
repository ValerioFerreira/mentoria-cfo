import json

data = json.load(open('pipeline/.cache/material/questoes/direito-constitucional__m14.json', encoding='utf-8'))
qs_by_id = {q['id']: q for q in data['questoes']}

selected_ids = [
    # c01-s01 (6 AOCP)
    'tec_3841419', 'tec_3870112', 'tec_3872678', 'tec_3872785', 'tec_4031956', 'tec_4047288',
    # c02-s01 (1 AOCP + 5 Inéditas)
    'tec_2853314', 'mentoria_mcn_direito-constitucional_118_c1c8a7', 'mentoria_mcn_direito-constitucional_119_2cbbe5',
    'mentoria_mcn_direito-constitucional_120_c93b6e', 'mentoria_mcn_direito-constitucional_121_87f4f4', 'mentoria_mcn_direito-constitucional_122_b6adf5',
    # c03-s01 (6 AOCP)
    'tec_3791630', 'tec_3449580', 'tec_3526992', 'tec_3139609', 'tec_1221585', 'tec_628285'
]

print(f"Total selecionadas: {len(selected_ids)}")
for qid in selected_ids:
    q = qs_by_id[qid]
    print(f"\n--- [{q['capitulo']}] {q['id']} - {q.get('banca')} ({q.get('ano')}) - Gab: {q.get('gabarito')} ---")
    print("Enunciado:", q.get('enunciado')[:200].replace('\n', ' '))
    alts = q.get('alternativas', [])
    for a in alts:
        print(f"  {a.get('letra')}: {str(a.get('texto'))[:80]}")
