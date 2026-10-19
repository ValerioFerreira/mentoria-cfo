import json, glob, os, sys
ACC = set('ãçáéíóúâêôõàÃÇÁÉÍÓÚ')
discs = sys.argv[1:]
for disc in discs:
    for f in sorted(glob.glob(f'content/summaries/{disc}/*.json')):
        d = json.load(open(f, encoding='utf-8'))
        for s in d['segments']:
            t = s['analytic']
            r = 1000 * sum(1 for c in t if c in ACC) / max(len(t), 1)
            tag = 'SEM-ACENTO' if r < 12 else ''
            if tag:
                print(s['id'], f"{r:.1f}", len(t.split()), tag)
