import os
import json
import glob
import re

AUDITS_DIR = r'C:\Users\Administrador\.gemini\antigravity\brain\94ed5ef5-5793-49ad-b5ab-7577f556a2ab\audits'
ITEMS_DIR = r'content\items'

def load_json(p):
    with open(p, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(p, data):
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print('Carregando relatórios de auditoria...')
d1 = load_json(os.path.join(AUDITS_DIR, 'bizu-1-direito.json'))
d2 = load_json(os.path.join(AUDITS_DIR, 'bizu-2-linguas-humanas.json'))
d3 = load_json(os.path.join(AUDITS_DIR, 'bizu-3-exatas.json'))
d4 = load_json(os.path.join(AUDITS_DIR, 'bizu-4-ciencias-tech.json'))

fixes_by_id = {}

# 1. DIREITO (d1)
for issue in d1.get('issues', []):
    iid = issue.get('id')
    # Pode vir no formato direito-administrativo/a00.json/direito-administrativo/a00/s01#teoria#3
    if '.json/' in iid:
        iid = iid.split('.json/')[1]
    fixes_by_id[iid] = {
        'statement': issue['proposta']['statement'],
        'isTrue': issue['proposta']['isTrue'],
        'explanation': issue['proposta']['explanation']
    }

# 2. CIÊNCIAS E TI (d4)
for f in d4.get('findings', []):
    iid = f.get('id')
    fixes_by_id[iid] = {
        'statement': f['proposed']['statement'],
        'isTrue': f['proposed']['isTrue'],
        'explanation': f['proposed']['explanation']
    }

# 3. LÍNGUAS E HISTÓRIA DE PE (d2)
for section, items in d2.get('detailed_corrections', {}).items():
    for item in items:
        iid = item.get('id')
        fixes_by_id[iid] = {
            'statement': item['proposed']['statement'],
            'isTrue': item['proposed']['isTrue'],
            'explanation': item['proposed']['explanation']
        }

# 4. EXATAS (d3)
for section, items in d3.get('detailed_corrections', {}).items():
    for item in items:
        iid = item.get('id')
        fixes_by_id[iid] = {
            'statement': item['proposed']['statement'],
            'isTrue': item['proposed']['isTrue'],
            'explanation': item['proposed']['explanation']
        }

print(f'Total de correções pontuais diretas mapeadas: {len(fixes_by_id)}')
