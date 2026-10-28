import sys
from pathlib import Path

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
sys.path.insert(0, str(ROOT / "pipeline"))
from textutil import aula_key_map, load_pages

k = aula_key_map().get('direito-penal/a04')
data = load_pages(k)
for p in data['pages']:
    txt = p['text'].lower()
    if 'suic' in txt and p['n'] in range(35, 45):
        print(f"PAG {p['n']} mentions suicidio")
    if '121-b' in txt and p['n'] in range(35, 45):
        print(f"PAG {p['n']} mentions 121-b")
