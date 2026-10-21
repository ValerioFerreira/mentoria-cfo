"""Simula os cadernos (QUESTOES) de uma grade de planos do PCPE com a regra de completar por trechos já estudados e diz quantos
ficam abaixo do pedido e quantas questões faltam por trecho.
    cd web && npx tsx scripts/pcpe-plan-grid.ts && npx tsx scripts/pcpe-plan-test.ts   # gera pipeline/.cache/pcpe-planos-grade.json e pcpe-planos.json
    python pipeline/pcpe_tools/cadernos_sim.py [--semfallback] [--so-banco]
Contagem de questões = pipeline/briefs/ineditas-base-segcounts.json (foto da produção) + content/questoes/ineditas/mc/*.txt.
Após importar as reais do TEC, REGENERE a foto da produção antes de simular."""
import json,re,sys,collections
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
avail=collections.Counter()
SO_BANCO='--so-banco' in sys.argv  # contagem = banco de produção já atualizado (pcpe-segcounts.ts --remoto); não soma os .txt
for r in json.load(open('pipeline/.cache/pcpe-segcounts.json' if SO_BANCO else 'pipeline/briefs/ineditas-base-segcounts.json',encoding='utf-8')):
    u=r['banca'].upper()
    if 'CEBRASPE' in u or 'CESPE' in u or 'AOCP' in u or r['banca']=='Inédita MentorIA': avail[r['seg']]+=r['n']
for f in ([] if SO_BANCO else Path('content/questoes/ineditas/mc').glob('*.txt')):
    for m in re.finditer(r'^@@\s*(\S+)\s*\|',f.read_text(encoding='utf-8'),re.M): avail[f.stem+'/'+m.group(1)]+=1
def load():
    out=[]
    for fn in ('pcpe-planos-grade','pcpe-planos'):
        out+= json.load(open(f'pipeline/.cache/{fn}.json',encoding='utf-8'))
    return out
planos=load()
FALL = '--semfallback' not in sys.argv
def cases(cur):
    bad=[]
    for p in planos:
        acts=p['acts']
        studied=[]  # (ord, subject, seg)
        for a in acts:
            if a['type']=='TEORIA':
                for s in a['segmentIds']: studied.append((a['ord'],a['subjectId'],s))
        for a in acts:
            if a['type']!='QUESTOES' or a.get('scope')=='FINAL' or not a.get('quiz'): continue
            need=a['quiz']['questions']; g=a['segmentIds']; sub=g[0].split('/')[0]
            n=sum(cur[s] for s in g)
            if FALL and n<need:
                extra={s for o,sj,s in studied if sj==sub and o<a['ord'] and s not in g}
                n+=sum(cur[s] for s in extra)
            if n<need: bad.append((p['name'],a['ord'],tuple(g),need,n))
    return bad
bad=cases(avail)
print('cadernos curtos (não-FINAL):',len(bad),'de', sum(1 for p in planos for a in p['acts'] if a['type']=='QUESTOES' and a.get('scope')!='FINAL'))
print(collections.Counter(b[2][0].split('/')[0] for b in bad))
d=collections.Counter(b[3]-b[4] for b in bad); print(sorted(d.items())[:20])
json.dump([list(b) for b in bad],open('pipeline/.cache/cad_bad.json','w',encoding='utf-8'),ensure_ascii=False)

import math
def caseN(p,a,cur,studied):
    g=a['segmentIds']; sub=g[0].split('/')[0]; need=a['quiz']['questions']
    n=sum(cur[s] for s in g)
    if n<need:
        extra={s for o,sj,s in studied if sj==sub and o<a['ord'] and s not in g}
        n+=sum(cur[s] for s in extra)
    return need,n
cur=collections.Counter(avail); added=collections.Counter()
pre=[]
for p in planos:
    studied=[(a['ord'],a['subjectId'],s) for a in p['acts'] if a['type']=='TEORIA' for s in a['segmentIds']]
    for a in p['acts']:
        if a['type']=='QUESTOES' and a.get('scope')!='FINAL' and a.get('quiz'): pre.append((p,a,studied))
for rnd in range(10):
    changed=0
    for p,a,studied in pre:
        need,n=caseN(p,a,cur,studied)
        if n<need:
            g=a['segmentIds']
            for _ in range(need-n):
                s=min(g,key=lambda s:cur[s]); cur[s]+=1; added[s]+=1; changed+=1
    print('rodada',rnd,'acrescentadas',changed)
    if not changed: break
print('FINAL: acrescentar',sum(added.values()),'em',len(added),'trechos')
bd=collections.Counter()
for s,v in added.items(): bd[s.split('/')[0]]+=v
print(bd)
json.dump(added,open('pipeline/.cache/cad_added.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
print(sorted(collections.Counter(added.values()).items()))
