import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

data = json.load(open('scratch/trechos_fracos/direito-processual-penal.json', encoding='utf-8'))
total = 0
for i, x in enumerate(data):
    total += x['faltam']
    print(f"{i+1:02d}. {x['seg']} ({x['faltam']}q) p.{x['paginas']} | {x['topicos']}")
print(f"Total: {total}")
