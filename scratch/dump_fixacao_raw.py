import json

with open('pipeline/.cache/material/questoes/biologia__m03.json', encoding='utf-8') as f:
    data = json.load(f)

selected_ids = [
    'tec_3449711', 'tec_2567967', 'tec_2031729',
    'tec_3554863', 'tec_3140656', 'tec_2031727',
    'tec_3140607', 'tec_3140609', 'tec_1721061',
    'tec_3449701', 'tec_3140599', 'tec_3140605',
    'tec_3449703', 'tec_3449706',
    'tec_3554866', 'tec_1721026',
    'tec_2031746', 'tec_3100287',
    'tec_2920294', 'tec_3140615'
]

bank = {q['id']: q for q in data['questoes']}
with open('scratch/fixacao_raw_data.json', 'w', encoding='utf-8') as out:
    json.dump({qid: bank[qid] for qid in selected_ids}, out, indent=2, ensure_ascii=False)

print('Dumped raw data for 20 questions.')
