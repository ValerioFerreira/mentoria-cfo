import json, sys
sid = sys.argv[1]
what = sys.argv[2] if len(sys.argv) > 2 else 'both'
disc, aula, _ = sid.split('/')
if what in ('both', 'sum'):
    d = json.load(open(f'content/summaries/{disc}/{aula}.json', encoding='utf-8'))
    s = next(x for x in d['segments'] if x['id'] == sid)
    print('### ANALITICO', len(s['analytic'].split()), 'palavras')
    print(s['analytic'])
    print('### SINTETICO')
    print('\n'.join(s.get('synthetic', [])))
if what in ('both', 'bizu'):
    d = json.load(open(f'content/items/{disc}/{aula}.json', encoding='utf-8'))
    s = next(x for x in d['segments'] if x['id'] == sid)
    b = s['bizu']
    print('### BIZU summary')
    print('\n'.join(b['summary']))
    for k in ('teoria', 'revisao'):
        print('###', k)
        for i in b[k]:
            print('-', i['isTrue'], i['statement'])
            print('   ->', i['explanation'])
    print('pointers', b.get('pointers'))
