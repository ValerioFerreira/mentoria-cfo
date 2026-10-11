# -*- coding: utf-8 -*-
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

print('1. Carregando relatórios de auditoria...')
d1 = load_json(os.path.join(AUDITS_DIR, 'bizu-1-direito.json'))
d2 = load_json(os.path.join(AUDITS_DIR, 'bizu-2-linguas-humanas.json'))
d3 = load_json(os.path.join(AUDITS_DIR, 'bizu-3-exatas.json'))
d4 = load_json(os.path.join(AUDITS_DIR, 'bizu-4-ciencias-tech.json'))

fixes = {}

# Direito (24 itens)
for issue in d1.get('issues', []):
    iid = issue.get('id')
    if '.json/' in iid:
        iid = iid.split('.json/')[1]
    fixes[iid] = {
        'statement': issue['proposta']['statement'].strip(),
        'isTrue': issue['proposta']['isTrue'],
        'explanation': issue['proposta']['explanation'].strip()
    }

# Ciências e TI (13 itens)
for f in d4.get('findings', []):
    iid = f.get('id')
    fixes[iid] = {
        'statement': f['proposed']['statement'].strip(),
        'isTrue': f['proposed']['isTrue'],
        'explanation': f['proposed']['explanation'].strip()
    }

# Línguas e História de PE (d2: 24 historia-pe + 22 linguas)
for sec, items in d2.get('detailed_corrections', {}).items():
    for it in items:
        iid = it.get('id')
        fixes[iid] = {
            'statement': it['proposed']['statement'].strip(),
            'isTrue': it['proposed']['isTrue'],
            'explanation': it['proposed']['explanation'].strip()
        }

# Exatas pontuais (d3: matemática, estatística e pilotos RL a00)
for sec, items in d3.get('detailed_corrections', {}).items():
    for it in items:
        iid = it.get('id')
        fixes[iid] = {
            'statement': it['proposed']['statement'].strip(),
            'isTrue': it['proposed']['isTrue'],
            'explanation': it['proposed']['explanation'].strip()
        }

print(f'Total de correções catalogadas diretamente: {len(fixes)}')

# Função para extrair fatos limpos de um summary
def parse_summary_facts(summary_lines, default_topic):
    facts = []
    for line in summary_lines:
        line = line.strip()
        if not line or line.startswith('###') or line.startswith('> '):
            continue
        # Limpar marcadores de lista e negrito
        clean = re.sub(r'^[-\*\d\.\s]+', '', line)
        clean = clean.replace('**', '').replace('__', '').strip()
        if len(clean) > 20:
            facts.append(clean)
    return facts

def make_affirmative_item(fact_text, topic_name):
    # Transforma uma frase conceitual em proposição C/E clara
    stmt = fact_text
    # Se começar com tópico ex: 'Princípio X: O princípio...', manter ou ajeitar
    if ':' in stmt and len(stmt.split(':')[0]) < 40:
        parts = stmt.split(':', 1)
        stmt = f'{parts[0].strip()}: {parts[1].strip()}'
    if not stmt.endswith('.'):
        stmt += '.'
    exp = f'Item correto. Em conformidade com a doutrina e o conteúdo de {topic_name}: {stmt}'
    return {'statement': stmt, 'isTrue': True, 'explanation': exp}

def make_negative_item(fact_text, topic_name):
    # Cria uma proposição incorreta plausível invertendo a declaração
    stmt = fact_text
    # Inversões comuns
    if ' é ' in stmt:
        stmt_f = stmt.replace(' é ', ' não é ', 1)
    elif ' são ' in stmt:
        stmt_f = stmt.replace(' são ', ' não são ', 1)
    elif ' exige ' in stmt:
        stmt_f = stmt.replace(' exige ', ' dispensa ', 1)
    elif ' requer ' in stmt:
        stmt_f = stmt.replace(' requer ', ' independe de ', 1)
    elif ' sempre ' in stmt:
        stmt_f = stmt.replace(' sempre ', ' nunca ', 1)
    elif ' apenas ' in stmt:
        stmt_f = stmt.replace(' apenas ', ' em qualquer hipótese, sem exceções, ', 1)
    elif ' exclusivo' in stmt:
        stmt_f = stmt.replace(' exclusivo', ' comum e irrestrito', 1)
    elif ' exclusivamente ' in stmt:
        stmt_f = stmt.replace(' exclusivamente ', ' indiferentemente ', 1)
    else:
        stmt_f = f'É incorreto afirmar que {stmt[:1].lower() + stmt[1:]}'
        if stmt_f.endswith('.'):
            stmt_f = stmt_f[:-1] + ', uma vez que tal postulado carece de amparo técnico.'

    if not stmt_f.endswith('.'):
        stmt_f += '.'
    exp = f'Item incorreto. Na realidade, segundo os fundamentos de {topic_name}: {fact_text}'
    if not exp.endswith('.'):
        exp += '.'
    return {'statement': stmt_f, 'isTrue': False, 'explanation': exp}

# Carregar metadados de tópicos
segments_meta = {}
for disc in ['raciocinio-logico', 'atualidades']:
    p = f'content/segments/{disc}.json'
    if os.path.exists(p):
        d = load_json(p)
        for s in d.get('segments', []):
            segments_meta[s['id']] = s

print('2. Varrendo arquivos de items para aplicar correções...')
all_files = sorted(glob.glob('content/items/*/*.json'))
applied_direct_count = 0
synthesized_rl_count = 0
synthesized_at_count = 0

for filepath in all_files:
    disc = filepath.replace('\\', '/').split('/')[-2]
    data = load_json(filepath)
    modified = False
    
    for seg in data.get('segments', []):
        sid = seg.get('id')
        bizu = seg.get('bizu', {})
        summary = bizu.get('summary', [])
        meta = segments_meta.get(sid, {})
        topic_name = meta.get('startTopic') or sid
        facts = parse_summary_facts(summary, topic_name)
        
        for kind in ['teoria', 'revisao']:
            items_list = bizu.get(kind, [])
            for idx, item in enumerate(items_list):
                item_id = f'{sid}#{kind}#{idx}'
                
                # Caso 1: Correção direta dos relatórios de auditoria
                if item_id in fixes:
                    item['statement'] = fixes[item_id]['statement']
                    item['isTrue'] = fixes[item_id]['isTrue']
                    item['explanation'] = fixes[item_id]['explanation']
                    applied_direct_count += 1
                    modified = True
                    continue
                
                # Caso 2: Placeholder sintético em raciocinio-logico ou atualidades
                stmt = item.get('statement', '')
                is_placeholder = ('No segmento ' in stmt) or ('Conceitos Estruturantes' in stmt) or ('a fundamentação conceitual das variáveis' in stmt)
                
                if is_placeholder and (disc in ['raciocinio-logico', 'atualidades']):
                    # Gerar item real substantivo baseado nos fatos do summary
                    fact_idx = (idx * 2 if kind == 'teoria' else idx * 2 + 1) % max(1, len(facts))
                    fact = facts[fact_idx] if facts else f'Os conceitos fundamentais de {topic_name} estruturam o raciocínio aplicado a este módulo.'
                    
                    # Alternar gabarito: pares V, ímpares F
                    if idx % 2 == 0:
                        gen = make_affirmative_item(fact, topic_name)
                    else:
                        gen = make_negative_item(fact, topic_name)
                    
                    item['statement'] = gen['statement']
                    item['isTrue'] = gen['isTrue']
                    item['explanation'] = gen['explanation']
                    modified = True
                    if disc == 'raciocinio-logico':
                        synthesized_rl_count += 1
                    else:
                        synthesized_at_count += 1

    if modified:
        save_json(filepath, data)

print(f'Correções diretas aplicadas: {applied_direct_count}')
print(f'Itens de Raciocínio Lógico saneados: {synthesized_rl_count}')
print(f'Itens de Atualidades saneados: {synthesized_at_count}')
print('Saneamento de conteúdo concluído!')
