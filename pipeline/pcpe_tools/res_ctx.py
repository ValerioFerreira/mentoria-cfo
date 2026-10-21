import sys,json,re,collections
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0,'pipeline')
import summary_coverage as sc
from textutil import aula_key_map, load_pages
tid=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 25
disc,aula,_=tid.split('/')
segs={s['id']:s for s in json.load(open(f'content/segments/{disc}.json',encoding='utf-8'))['segments']}
ref=segs[tid]
doc=json.load(open(f'content/summaries/{disc}/{aula}.json',encoding='utf-8'))
seg=next(s for s in doc['segments'] if s['id']==tid)
r=sc.segment_score(seg,ref)
print('###',tid,'págs',ref['startPage'],'-',ref['endPage'],'| cobertura',round(r['score'],2),'| termos',r['salient'])
print('tópicos:',' ; '.join(t[:50] for t in ref.get('topicsCovered',[])[:12]))
heads=[l for l in seg['analytic'].split('\n') if l.startswith('#')]
print('resumo:',len(seg['analytic'].split()),'palavras; seções:',' | '.join(h.strip('# ') for h in heads))
print('missing:',' '.join(r['missing'][:n]))
key=aula_key_map()[ref['aula']]
pages=[p for p in load_pages(key)['pages'] if ref['startPage']<=p['n']<=ref['endPage']]
txt='\n'.join(f"[p{p['n']}] "+p['text'] for p in pages)
shown=0
for w in r['missing'][:n]:
    m=re.search(re.escape(w[:6]),sc._ascii(txt))
    if not m: continue
    # posição aproximada no texto original (ascii e original têm mesmo tamanho na maioria dos casos)
    i=m.start()
    print(f'-- {w}: …{txt[max(0,i-120):i+160]}…'.replace('\n',' '))
