import json, glob, os, collections, sys
ACC = set('ãçáéíóúâêôõàÃÇÁÉÍÓÚ')
root = sys.argv[1]
res = collections.defaultdict(lambda: [0, 0, 0])
for f in glob.glob(os.path.join(root, 'content', 'summaries', '*', '*.json')):
    d = json.load(open(f, encoding='utf-8'))
    disc = os.path.basename(os.path.dirname(f))
    for s in d['segments']:
        t = s.get('analytic', '')
        res[disc][0] += len(t); res[disc][1] += sum(1 for c in t if c in ACC); res[disc][2] += 1
for k, v in sorted(res.items()):
    print(f"{k:28} trechos={v[2]:4} acentos/1000car={1000*v[1]/max(v[0],1):5.1f}")
print('--- itens (bizu C/E + summary)')
res = collections.defaultdict(lambda: [0, 0])
for f in glob.glob(os.path.join(root, 'content', 'items', '*', '*.json')):
    d = json.load(open(f, encoding='utf-8'))
    disc = os.path.basename(os.path.dirname(f))
    for s in d['segments']:
        b = s.get('bizu') or {}
        t = ' '.join(b.get('summary', [])) + ' '.join(i.get('statement', '') + i.get('explanation', '') for k in ('teoria', 'revisao') for i in b.get(k, []))
        res[disc][0] += len(t); res[disc][1] += sum(1 for c in t if c in ACC)
for k, v in sorted(res.items()):
    print(f"{k:28} acentos/1000car={1000*v[1]/max(v[0],1):5.1f}")
