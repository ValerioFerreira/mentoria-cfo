"""Sorteio reproduzível da auditoria por amostra dos resumos analíticos e sintéticos.

Conforme pipeline/briefs/auditoria-amostral-resumos.md:
- random.seed(20261027)
- Estratificado por disciplina e aula (máx 2 trechos por aula, salvo disciplina pequena)
- Prioriza trechos de norma/fórmula
- Grava pipeline/.cache/auditoria-resumos/amostra.json
"""

import os
import glob
import json
import random
import re
from collections import defaultdict, Counter

random.seed(20261027)

TARGETS = {
    'direito-administrativo': 18,
    'direito-constitucional': 14,
    'informatica': 14,
    'direito-penal': 11,
    'direito-processual-penal': 8,
    'legislacao-penal-especial': 8,
    'legislacao-pcpe': 8,
    'legislacoes-pe': 8,
    'direitos-humanos': 8,
    'administracao': 8,
    'direito-penal-militar': 6,
    'direito-processual-penal-militar': 6,
    'biologia': 11,
    'quimica': 12,
    'matematica': 12,
    'estatistica': 12,
    'fisica': 8,
    'lingua-portuguesa': 10,
    'lingua-espanhola': 8,
    'lingua-inglesa': 8,
    'contabilidade-geral': 8,
    'raciocinio-logico': 9,
}

DISC_TO_AGENT = {
    'direito-administrativo': 'da',
    'direito-constitucional': 'dc',
    'direito-penal': 'dp-dpp',
    'direito-processual-penal': 'dp-dpp',
    'legislacao-penal-especial': 'leg-esp',
    'legislacao-pcpe': 'leg-esp',
    'legislacoes-pe': 'leg-esp',
    'direitos-humanos': 'dh-adm-mil',
    'administracao': 'dh-adm-mil',
    'direito-penal-militar': 'dh-adm-mil',
    'direito-processual-penal-militar': 'dh-adm-mil',
    'informatica': 'inf',
    'quimica': 'qui',
    'biologia': 'bio-fis',
    'fisica': 'bio-fis',
    'matematica': 'mat-rl',
    'raciocinio-logico': 'mat-rl',
    'estatistica': 'est-cont',
    'contabilidade-geral': 'est-cont',
    'lingua-portuguesa': 'lp',
    'lingua-espanhola': 'esp-ing',
    'lingua-inglesa': 'esp-ing',
}

def score_segment(seg):
    fp = seg.get('fingerprint') or {}
    start_topic = str(fp.get('startTopic') or '')
    analytic = str(seg.get('analytic') or '')
    synth = ' '.join(str(x) for x in (seg.get('synthetic') or []))
    text = f'{analytic} {synth} {start_topic}'.lower()
    norm_count = len(re.findall(r'\b(art\.|artigo|lei|decreto|súmula|código|constituição|parágrafo|inciso|pena|reclusão|detenção|prazo|anos|meses|dias)\b', text))
    formula_count = len(re.findall(r'(\$|=|\\frac|\\times|\\sqrt|\b(fórmula|equação|cálculo|probabilidade|variância|molar|reação|entalpia)\b)', text))
    return norm_count + formula_count

def main():
    data_by_disc = defaultdict(lambda: defaultdict(list))
    for f in sorted(glob.glob('content/summaries/*/*.json')):
        disc = os.path.basename(os.path.dirname(f))
        aula = os.path.splitext(os.path.basename(f))[0]
        with open(f, 'r', encoding='utf-8') as fp:
            content = json.load(fp)
            for seg in content.get('segments', []):
                data_by_disc[disc][aula].append(seg)

    total_sample = []

    for disc, target in sorted(TARGETS.items()):
        aulas = sorted(data_by_disc[disc].keys())
        shuffled_aulas = list(aulas)
        random.shuffle(shuffled_aulas)
        
        aula_counts = defaultdict(int)
        if target <= len(shuffled_aulas):
            for a in shuffled_aulas[:target]:
                aula_counts[a] = 1
        else:
            for a in shuffled_aulas:
                aula_counts[a] = 1
            rem = target - len(shuffled_aulas)
            eligible = [a for a in shuffled_aulas if len(data_by_disc[disc][a]) >= 2]
            for a in eligible[:rem]:
                aula_counts[a] += 1
                
        for aula in sorted(aula_counts.keys()):
            c = aula_counts[aula]
            segs = data_by_disc[disc][aula]
            scored_segs = []
            for s in segs:
                s_score = score_segment(s)
                rnd_val = random.random()
                scored_segs.append((s_score, rnd_val, s))
            scored_segs.sort(key=lambda x: (-x[0], x[1]))
            chosen = [x[2] for x in scored_segs[:c]]
            for s in chosen:
                total_sample.append({
                    'trecho': s['id'],
                    'disciplina': disc,
                    'aula': aula,
                    'agente': DISC_TO_AGENT[disc]
                })

        # Sort total_sample deterministically
    total_sample.sort(key=lambda x: (x['agente'], x['disciplina'], x['aula'], x['trecho']))

    out_dir = os.path.join('pipeline', '.cache', 'auditoria-resumos')
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, 'amostra.json')
    with open(out_file, 'w', encoding='utf-8') as fp:
        json.dump(total_sample, fp, indent=2, ensure_ascii=False)

    print(f'Total amostrado: {len(total_sample)}')
    print(f'Arquivo gravado em: {out_file}')

    aula_counter = Counter(f"{x['disciplina']}/{x['aula']}" for x in total_sample)
    print(f'Máximo trechos por aula: {max(aula_counter.values())}')
    two_segs = [k for k, v in aula_counter.items() if v == 2]
    print(f'Aulas com 2 trechos ({len(two_segs)}): {two_segs}')
    more_segs = [k for k, v in aula_counter.items() if v > 2]
    print(f'Aulas com >2 trechos: {more_segs}')

    by_agent = defaultdict(list)
    for x in total_sample:
        by_agent[x['agente']].append(x['trecho'])

    print('\nPor agente:')
    for ag in sorted(by_agent.keys()):
        print(f'  {ag}: {len(by_agent[ag])} trechos')

if __name__ == '__main__':
    main()
