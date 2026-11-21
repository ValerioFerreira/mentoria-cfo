with open('content/material/estatistica/m01/a00-s02.md', encoding='utf-8') as f:
    body = f.read()

tables, cur = [], []
for i, ln in enumerate(body.splitlines()):
    if ln.strip().startswith('|'):
        cur.append((i+1, ln.strip()))
    elif cur:
        tables.append(cur)
        cur = []
if cur:
    tables.append(cur)

for t_idx, t in enumerate(tables):
    unique_counts = set(r[1].count('|') for r in t)
    print(f'Table {t_idx} (lines {t[0][0]}-{t[-1][0]}): pipe counts = {unique_counts}')
    if len(unique_counts) > 1:
        for line_num, r in t:
            print(f'  line {line_num} (count {r.count("|")}): {r[:50]}')
