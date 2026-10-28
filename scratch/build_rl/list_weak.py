import json
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")

trechos = json.loads(Path('scratch/trechos_fracos/raciocinio-logico.json').read_text(encoding='utf-8'))
for i, t in enumerate(trechos, 1):
    print(f"{i:02d}. {t['seg']} ({t['aula']}) | faltam {t['faltam']} | {t['topicos']}")
print("Total trechos:", len(trechos))
print("Total faltam:", sum(t['faltam'] for t in trechos))
