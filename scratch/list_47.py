import json

gabs_data = json.loads(open('scratch/plano_gabaritos.json', encoding='utf-8').read())
fracos_data = json.loads(open('scratch/trechos_fracos/direito-administrativo.json', encoding='utf-8').read())

for i, (g, f) in enumerate(zip(gabs_data, fracos_data), 1):
    assert g['seg'] == f['seg']
    item_str = f" | item={f['item_arg']}" if f.get('item_arg') else ''
    gabs_str = ','.join(g['gabs'])
    print(f"{i:02d}. @@ {g['seg']}{item_str} ({g['faltam']}q) -> {gabs_str} | {f['topicos'][:50]}")
