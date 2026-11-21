# -*- coding: utf-8 -*-
import json

d = json.load(open('pipeline/.cache/material/questoes/fisica__m06.json', encoding='utf-8'))
sel_ids = [
    'tec_3452042', 'tec_3555330', 'tec_3558573',
    'tec_3452107', 'tec_2982225', 'tec_2982226',
    'tec_3141001', 'tec_3141020', 'tec_3508367',
    'mentoria_mcn_fisica_090_4e6b78', 'mentoria_mcn_fisica_091_2a2b0b', 'mentoria_mcn_fisica_092_5f15c5',
    'mentoria_mcn_fisica_097_9882ab', 'mentoria_mcn_fisica_098_21a537', 'mentoria_mcn_fisica_099_8c447c',
    'tec_1674290', 'tec_1430760', 'mentoria_mcn_fisica_140_b378a4'
]

for q in d['questoes']:
    if q['id'] in sel_ids:
        print(f"ID: {q['id']} | Cap: {q['capitulo']} | Gabarito: {q['gabarito']}")
        print(f"Enunciado: {q['enunciado']}")
        for a in q['alternativas']:
            print(f"  {a['letra']}: {a['texto']}")
        print("-" * 60)
