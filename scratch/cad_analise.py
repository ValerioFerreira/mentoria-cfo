import json,re,sys,collections
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
ROOT=Path('.')
planos=json.load(open('pipeline/.cache/pcpe-planos.json',encoding='utf-8'))
avail=collections.Counter()
for r in json.load(open('pipeline/briefs/ineditas-base-segcounts.json',encoding='utf-8')):
    u=r['banca'].upper()
    if 'CEBRASPE' in u or 'CESPE' in u or 'AOCP' in u or r['banca']=='Inédita MentorIA': avail[r['seg']]+=r['n']
for f in Path('content/questoes/ineditas/mc').glob('*.txt'):
    for m in re.finditer(r'^@@\s*(\S+)\s*\|',f.read_text(encoding='utf-8'),re.M): avail[f.stem+'/'+m.group(1)]+=1
tot=collections.Counter(); kk=collections.Counter(); short=[]
for p in planos:
    for a in p['acts']:
        if a['type']!='QUESTOES': continue
        need=(a.get('quiz') or {}).get('questions',0); n=sum(avail[s] for s in a['segmentIds'])
        kk[(len(a['segmentIds']),need)]+=1
        if need and n<need: short.append((p['name'][:3],a['segmentIds'],n,need))
print(sorted(kk.items()))
print(len(short))
d=collections.Counter(need-n for _,_,n,need in short); print(sorted(d.items()))
print(short[:5])
# distribution of avail per trecho
vals=[avail[s] for p in planos for a in p['acts'] if a['type']=='TEORIA' for s in a['segmentIds']]
import statistics
print(len(set(vals)), collections.Counter(min(v,30) for v in vals).most_common(12))

# alvo por trecho: distribui o déficit de cada caderno entre seus trechos; fica o maior valor por trecho
import math
extra=collections.defaultdict(int)
for p in planos:
    for a in p['acts']:
        if a['type']!='QUESTOES': continue
        need=(a.get('quiz') or {}).get('questions',0); ids=a['segmentIds']
        n=sum(avail[s] for s in ids)
        if need and n<need:
            share=math.ceil((need-n)/len(ids))
            for s in ids: extra[s]=max(extra[s],share)
print('trechos com déficit:',len(extra),'questões a escrever (aprox, upper bound por trecho):',sum(extra.values()))
bydisc=collections.Counter()
for s,v in extra.items(): bydisc[s.split('/')[0]]+=v
print(bydisc)
# apenas cadernos curtos de grupo 1
solo=[(a['segmentIds'][0],25-avail[a['segmentIds'][0]]) for p in planos for a in p['acts'] if a['type']=='QUESTOES' and len(a['segmentIds'])==1 and (a.get('quiz') or {}).get('questions',0)>avail[a['segmentIds'][0]]]
print('solo',len(solo),len(set(s for s,_ in solo)))
