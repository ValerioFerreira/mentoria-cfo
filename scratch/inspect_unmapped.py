import json
import csv

unmapped_segs = [
    'estatistica/a05/s05',
    'lingua-portuguesa/a00/s01'
]

rows = {r['trecho']: r for r in csv.DictReader(open('pipeline/briefs/ineditas-faltantes.csv', encoding='utf-8-sig'), delimiter=';')}

for seg in unmapped_segs:
    r = rows.get(seg, {})
    subj = seg.split('/')[0]
    print(f"Trecho: {seg}")
    print(f"  Aula: {r.get('aula')}")
    print(f"  Topicos: {r.get('topicos')}")
    # Load edital items
    edital_path = f"content/edital/pcpe/{subj}.json"
    doc = json.load(open(edital_path, encoding='utf-8'))
    print("  Opções de items no edital:")
    for it in doc['items']:
        print(f"    id={it['id']}: {it['item']}")
    print("-" * 50)
