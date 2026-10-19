import sys
# uso: sub.py <draft> <subs.txt>   (linhas "antigo ==> novo"; erro se o antigo não existir)
p, s = sys.argv[1], sys.argv[2]
t = open(p, encoding='utf-8').read()
bad = 0
for ln in open(s, encoding='utf-8').read().splitlines():
    if '==>' not in ln: continue
    a, b = ln.split('==>', 1)
    a, b = a.strip(), b.strip()
    if a not in t:
        print('NAO ACHEI:', a[:70]); bad += 1; continue
    t = t.replace(a, b)
open(p, 'w', encoding='utf-8').write(t)
print('ok' if not bad else f'{bad} pendentes')
