# -*- coding: utf-8 -*-
import os, json, glob, re

AUDITS_DIR = r'C:\Users\Administrador\.gemini\antigravity\brain\94ed5ef5-5793-49ad-b5ab-7577f556a2ab\audits'

def load_json(p):
    with open(p, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(p, data):
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

manual_fixes = {
    'lingua-inglesa/a00/s01#revisao#3': {
        'statement': 'Na língua inglesa, termos como "spy" e "surveillance" guardam relação semântica de proximidade e sinonímia contextual no âmbito da segurança e inteligência.',
        'isTrue': True,
        'explanation': 'Item correto. "Spy" (espião/espionar) e "surveillance" (vigilância/monitoramento) compartilham campo semântico comum referente a atividades de segurança e observação.'
    },
    'lingua-portuguesa/a01/s01#revisao#4': {
        'statement': 'O vocábulo "evidências" recebe acento gráfico pela regra geral das palavras paroxítonas terminadas em ditongo oral crescente.',
        'isTrue': True,
        'explanation': 'Item correto. Pelo Formulário Ortográfico oficial, "e-vi-dên-cias" é acentuada por ser paroxítona terminada em ditongo crescente, admitindo-se na doutrina fonológica a designação de proparoxítona aparente.'
    },
    'lingua-portuguesa/a11/s05#revisao#4': {
        'statement': 'Na estrutura de um texto dissertativo-argumentativo padrão, a tese central situa-se preferencialmente na introdução e na conclusão, enquanto os parágrafos de desenvolvimento organizam-se em torno de tópicos frasais.',
        'isTrue': True,
        'explanation': 'Item correto. A macroestrutura dissertativa organiza a tese nuclear na abertura, retoma-a no desfecho e estrutura os parágrafos argumentativos intermediários mediante tópicos frasais.'
    }
}

segments_meta = {}
for disc in ['raciocinio-logico', 'atualidades', 'historia-pe']:
    p = f'content/segments/{disc}.json'
    if os.path.exists(p):
        d = load_json(p)
        for s in d.get('segments', []):
            segments_meta[s['id']] = s

def parse_summary_facts(summary_lines, topic_name):
    facts = []
    for line in summary_lines:
        line = line.strip()
        if not line or line.startswith('###') or line.startswith('> '):
            continue
        clean = re.sub(r'^[-\*\d\.\s]+', '', line)
        clean = clean.replace('**', '').replace('__', '').strip()
        if len(clean) > 20:
            facts.append(clean)
    if not facts:
        facts.append(f'O domínio conceitual dos princípios de {topic_name} constitui fundamento essencial da matéria.')
    return facts

all_files = sorted(glob.glob('content/items/*/*.json'))
fixed_count = 0

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
            items = bizu.get(kind, [])
            for idx, it in enumerate(items):
                item_id = f'{sid}#{kind}#{idx}'
                
                if item_id in manual_fixes:
                    it['statement'] = manual_fixes[item_id]['statement']
                    it['isTrue'] = manual_fixes[item_id]['isTrue']
                    it['explanation'] = manual_fixes[item_id]['explanation']
                    modified = True
                    fixed_count += 1
                    continue
                
                stmt = it.get('statement', '')
                exp = it.get('explanation', '')
                full = stmt + ' ' + exp
                
                if ('no segmento ' in full.lower()) or ('durante a revisão de' in full.lower()) or ('conceitos estruturantes' in full.lower()):
                    fact_idx = (idx * 3 + (1 if kind == 'revisao' else 0)) % len(facts)
                    fact = facts[fact_idx]
                    
                    if idx % 2 == 0:
                        stmt_new = fact
                        if ':' in stmt_new and len(stmt_new.split(':')[0]) < 40:
                            p = stmt_new.split(':', 1)
                            stmt_new = f'{p[0].strip()}: {p[1].strip()}'
                        if not stmt_new.endswith('.'):
                            stmt_new += '.'
                        exp_new = f'Item correto. Em conformidade com os tópicos de {topic_name}: {fact}.'
                        it['statement'] = stmt_new
                        it['isTrue'] = True
                        it['explanation'] = exp_new
                    else:
                        if ' é ' in fact:
                            stmt_f = fact.replace(' é ', ' não é ', 1)
                        elif ' são ' in fact:
                            stmt_f = fact.replace(' são ', ' não são ', 1)
                        elif ' exige ' in fact:
                            stmt_f = fact.replace(' exige ', ' dispensa integralmente ', 1)
                        elif ' requer ' in fact:
                            stmt_f = fact.replace(' requer ', ' independe de ', 1)
                        elif ' sempre ' in fact:
                            stmt_f = fact.replace(' sempre ', ' nunca ', 1)
                        elif ' exclusivo' in fact:
                            stmt_f = fact.replace(' exclusivo', ' irrestrito a qualquer contexto', 1)
                        else:
                            stmt_f = f'No estudo de {topic_name}, é falso considerar que {fact[:1].lower() + fact[1:]}'
                        
                        if not stmt_f.endswith('.'):
                            stmt_f += '.'
                        exp_new = f'Item incorreto. Na realidade, segundo os fundamentos de {topic_name}: {fact}.'
                        it['statement'] = stmt_f
                        it['isTrue'] = False
                        it['explanation'] = exp_new
                    
                    modified = True
                    fixed_count += 1

    if modified:
        save_json(filepath, data)

print(f'Total de itens corrigidos e saneados nesta rodada: {fixed_count}')
