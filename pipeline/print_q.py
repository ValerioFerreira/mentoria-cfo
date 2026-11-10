import json

d = json.load(open('pipeline/.cache/material/questoes/lingua-portuguesa__m07.json', encoding='utf-8'))
chosen = ['tec_583957', 'tec_1429064', 'tec_3981964', 'tec_1442652', 'tec_3966633', 'mentoria_mcn_lingua-portuguesa_100_58e642', 'tec_3303091', 'tec_623607', 'tec_1398982', 'tec_2646220', 'tec_2097110', 'tec_505743']
qmap = {q['id']: q for q in d['questoes']}
for cid in chosen:
    q = qmap[cid]
    print('='*50)
    print(q['id'], '|', q['capitulo'], '|', q.get('banca'), '| Gab:', q.get('gabarito'))
    print('ENUNCIADO:', q.get('enunciado'))
    if q.get('alternativas'):
        for a in q['alternativas']:
            print(f"  {a['letra']}: {a['texto']}")
