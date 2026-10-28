import sys
sys.path.insert(0, 'pipeline')
from textutil import aula_key_map, load_pages

tasks = [
    ('s0259', '01_004', 19, 35),
    ('s0260', '01_001', 9, 23),
    ('s0263', '01_001', 24, 33),
    ('s0264', '01_003', 10, 23),
    ('s0265', '01_007', 34, 50),
    ('s0269', '01_002', 3, 19),
]

for name, key, p_start, p_end in tasks:
    data = load_pages(key)
    matching = [p for p in data['pages'] if p_start <= p.get('n', 0) <= p_end]
    fname = f'temp_{name}.txt'
    with open(fname, 'w', encoding='utf-8') as f:
        for p in matching:
            pg = p.get('n')
            f.write(f'=== PAGINA {pg} ===\n')
            f.write(p.get('text', '') + '\n\n')
    print(f'{fname}: {len(matching)} pages, {sum(len(p.get("text", "")) for p in matching)} chars')
