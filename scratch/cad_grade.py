import json,re,sys,collections,math
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
avail=collections.Counter()
for r in json.load(open('pipeline/briefs/ineditas-base-segcounts.json',encoding='utf-8')):
    u=r['banca'].upper()
    if 'CEBRASPE' in u or 'CESPE' in u or 'AOCP' in u or r['banca']=='Inédita MentorIA': avail[r['seg']]+=r['n']
for f in Path('content/questoes/ineditas/mc').glob('*.txt'):
    for m in re.finditer(r'^@@\s*(\S+)\s*\|',f.read_text(encoding='utf-8'),re.M): avail[f.stem+'/'+m.group(1)]+=1
planos=json.load(open('pipeline/.cache/pcpe-planos-grade.json',encoding='utf-8'))+json.load(open('pipeline/.cache/pcpe-planos.json',encoding='utf-8'))
groups=set()   # (tuple(ids), need)
for p in planos:
    for a in p['acts']:
        if a['type']!='QUESTOES' or not a.get('quiz'): continue
        groups.add((tuple(a['segmentIds']),a['quiz']['questions']))
print('grupos distintos',len(groups))
sizes=collections.Counter((len(g),n) for g,n in groups); print(sorted(sizes.items()))
# alvo por trecho via iteração gulosa: eleva o trecho de menor contagem do grupo até fechar o déficit
cur=collections.Counter(avail)
def deficit():
    return [(g,n) for g,n in groups if sum(cur[s] for s in g)<n]
added=collections.Counter()
for it in range(100000):
    d=deficit()
    if not d: break
    # pega o grupo com maior déficit, soma 1 ao trecho de menor contagem
    g,n=max(d,key=lambda x:x[1]-sum(cur[s] for s in x[0]))
    s=min(g,key=lambda s:cur[s]); cur[s]+=1; added[s]+=1
print('questões a acrescentar',sum(added.values()),'em',len(added),'trechos')
bd=collections.Counter()
for s,v in added.items(): bd[s.split('/')[0]]+=v
print(bd)
json.dump(added,open('scratch/cad_added.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
print(collections.Counter(min(v,20) for v in added.values()))

solo=collections.Counter()
for g,n in groups:
    if len(g)==1: solo[g[0]]+=1
print('trechos que aparecem sozinhos num caderno:',len(solo))
# sozinhos por posição na aula: quantos trechos tem a aula?
segs={}
for f in Path('content/segments').glob('*.json'):
    for s in json.load(open(f,encoding='utf-8'))['segments']: segs[s['id']]=s
bya=collections.Counter(s['id'].rsplit('/',1)[0] for s in segs.values())
print(collections.Counter(bya[s.rsplit('/',1)[0]] for s in solo))
# grupos com FINAL (mistos): chaves
print([ (g,n) for g,n in groups if len(g)==8][:2])
