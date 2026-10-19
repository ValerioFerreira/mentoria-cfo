import json, os, sys, collections, re
ROOT = sys.argv[1]
C = os.path.join(ROOT, 'content')
W = os.path.join(ROOT, 'web', 'content')
K = 'PCPE_AGENTE'

imp = json.load(open(os.path.join(C, 'importance', 'segments.json'), encoding='utf-8'))['segments']
cat = json.load(open(os.path.join(C, 'catalog.json'), encoding='utf-8'))
aulas = {}
def walk(o):
    if isinstance(o, dict):
        if 'id' in o and ('onlyContests' in o or 'excludeContests' in o or 'number' in o):
            aulas[o['id']] = o
        for v in o.values(): walk(v)
    elif isinstance(o, list):
        for v in o: walk(v)
walk(cat)

def aula_ok(aid):
    a = aulas.get(aid, {})
    oc = a.get('onlyContests') or []
    ec = a.get('excludeContests') or []
    if oc and K not in oc: return False
    if K in ec: return False
    return True

segs = [s for s, v in imp.items() if v['contests'].get(K, {}).get('appears')]
segs_ok = [s for s in segs if aula_ok('/'.join(s.split('/')[:2]))]
print('appears=true:', len(segs), ' after aula filters:', len(segs_ok))

def load(base, kind, aid):
    p = os.path.join(base, kind, *aid.split('/')) + '.json'
    if not os.path.exists(p): return None
    return json.load(open(p, encoding='utf-8'))

stats = collections.defaultdict(lambda: collections.Counter())
status = collections.Counter()
missing = collections.defaultdict(list)
for s in segs_ok:
    d = s.split('/')[0]; aid = '/'.join(s.split('/')[:2])
    st = stats[d]; st['trechos'] += 1
    for base, tag in ((C, ''), (W, 'web_')):
        it = load(base, 'items', aid)
        seg = next((x for x in (it or {}).get('segments', []) if x['id'] == s), None)
        b = (seg or {}).get('bizu') or {}
        if b.get('summary'): st[tag + 'bizu'] += 1
        else: missing[tag + 'bizu'].append(s)
        ce = 0
        for k, v in b.items():
            if isinstance(v, list) and k != 'summary':
                ce += len(v)
        st[tag + 'ce'] += ce
        if tag == '' and it: status['items:' + str(it.get('status'))] += 1
        sm = load(base, 'summaries', aid)
        sseg = next((x for x in (sm or {}).get('segments', []) if x['id'] == s), None)
        if sseg and sseg.get('analytic'):
            st[tag + 'resumo'] += 1
            if tag == '':
                st['palavras'] += len(sseg['analytic'].split())
        else:
            missing[tag + 'resumo'].append(s)
        if tag == '' and sm: status['summ:' + str(sm.get('status'))] += 1

tot = collections.Counter()
print(f"{'disc':28} trech bizu wbizu ce   resumo wres palavras")
for d, st in sorted(stats.items()):
    tot.update(st)
    print(f"{d:28} {st['trechos']:5} {st['bizu']:4} {st['web_bizu']:5} {st['ce']:5} {st['resumo']:5} {st['web_resumo']:4} {st['palavras']:7}")
print('TOTAL', dict(tot))
print('status (por trecho):', dict(status))
for k, v in missing.items():
    print('MISSING', k, len(v), v[:15])
