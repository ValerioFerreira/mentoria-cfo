import json

with open('pipeline/.cache/material/questoes/direito-constitucional__m06.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

selected_ids = [
    'tec_2063659', 'tec_2189356', 'tec_2609624', 'tec_1717331',
    'tec_3451699', 'tec_3631401', 'tec_3015989', 'tec_3260597',
    'tec_3706315', 'tec_3706331', 'tec_3753611', 'tec_3143751',
    'tec_2984637', 'tec_3260951', 'tec_2509194'
]

selected_qs = [q for q in data['questoes'] if q['id'] in selected_ids]

with open('scratch/selected_dc_m06.json', 'w', encoding='utf-8') as f:
    json.dump(selected_qs, f, ensure_ascii=False, indent=2)

print(f"Salvas {len(selected_qs)} questoes em scratch/selected_dc_m06.json")
