import json
from pathlib import Path

data = json.loads(Path('scratch/trechos_fracos/informatica.json').read_text(encoding='utf-8'))
print('Total trechos:', len(data))
print('Total faltam:', sum(x['faltam'] for x in data))
for i, x in enumerate(data):
    print(f"{i+1:02d}. {x['trecho']}: faltam {x['faltam']} (alvo={x['alvo']}, atuais={x['atuais']}) | item_arg={x.get('item_arg')}")
