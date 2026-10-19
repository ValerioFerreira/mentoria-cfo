import re, sys, os
sys.path.insert(0, "pipeline")
from summary_source import source_text
sid = sys.argv[1]
keep_nums = len(sys.argv) > 2 and sys.argv[2] == '--nums'
seg, t = source_text(sid)
t = re.sub(r'[ \t]+\n', '\n', t)
t = re.sub(r'\n(Luciano Rosa|Aula \d\d|Equipe|Prof)[^\n]*', '', t)
if not keep_nums:
    out = []
    for ln in t.split('\n'):
        s = ln.strip()
        if re.fullmatch(r'\(?\d{1,3}\)?', s):                      # (1) (12) ...
            continue
        if re.fullmatch(r'\(?-?\d{1,3}(\.\d{3})*(,\d{2})?\)?\s*(\(\d+\))?', s):  # valores de razonete
            continue
        if re.fullmatch(r'[A-Za-zÀ-ÿ.\- /&]+ \((Ativo|Passivo|PL|Resul|Result\.?|Ret\.[^)]*|Res\.|Pass\.|AC|PC|Res)\)', s):
            continue
        out.append(ln)
    t = '\n'.join(out)
t = re.sub(r'\n{2,}', '\n', t)
print(f"# {sid} págs. {seg['startPage']}-{seg['endPage']} | tópicos: {'; '.join(seg.get('topicsCovered', []))}")
print(t)
