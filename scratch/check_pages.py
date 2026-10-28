import sys
from pathlib import Path

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
sys.path.insert(0, str(ROOT / "pipeline"))
from textutil import aula_key_map, load_pages

k = aula_key_map().get('direito-penal/a04')
data = load_pages(k)
for p in data['pages']:
    if p['n'] in (37, 38):
        print(f"=== PAG {p['n']} ===")
        for l in p['text'].splitlines()[:15]:
            if l.strip():
                print(" ", l.strip()[:80])
