import json

with open('pipeline/.cache/material/questoes/biologia__m02.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

selected_ids = [
    # a01/s01 (3)
    'tec_3548602', 'tec_2031715', 'tec_958565',
    # a01/s02 (3)
    'tec_2031735', 'tec_1721006', 'tec_869205',
    # a01/s03 (3)
    'tec_3554845', 'tec_3262080', 'tec_1453550',
    # a12/s01 (3)
    'tec_3100293', 'tec_3140921', 'tec_1721819',
    # a12/s02 (3)
    'tec_1718947', 'tec_1092460', 'mentoria_mcn_biologia_068_931bb2'
]

selected_qs = [q for q in data['questoes'] if q['id'] in selected_ids]

with open('scratch/selected_bio_m02.json', 'w', encoding='utf-8') as f:
    json.dump(selected_qs, f, ensure_ascii=False, indent=2)

print(f"Salvas {len(selected_qs)} questoes em scratch/selected_bio_m02.json")
