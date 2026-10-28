import csv
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
faltantes = list(csv.DictReader(open(ROOT / 'pipeline/briefs/ineditas-faltantes.csv', encoding='utf-8-sig'), delimiter=';'))

explicit_items = {
    'estatistica/a05/s05': '2.1',
    'lingua-portuguesa/a00/s01': '3',
    'lingua-portuguesa/a00/s02': '5.1',
    'lingua-portuguesa/a00/s03': '5.1',
    'lingua-portuguesa/a00/s04': '5.4',
    'matematica/a01/s03': '1',
}

subjects = [
    'contabilidade-geral', 'informatica', 'lingua-portuguesa',
    'estatistica', 'matematica', 'raciocinio-logico',
    'direito-administrativo', 'direito-constitucional', 'direito-penal'
]

out_dir = ROOT / 'scratch' / 'trechos_info'
out_dir.mkdir(parents=True, exist_ok=True)

for subj in subjects:
    rows = [r for r in faltantes if r['disciplina'] == subj]
    subj_data = []
    for r in rows:
        t = r['trecho']
        seg = t.split('/', 1)[1]
        peso = float(r['peso_prova'])
        min_q = 8 if peso >= 0.20 else 6
        item_arg = explicit_items.get(t, None)
        subj_data.append({
            'trecho': t,
            'seg': seg,
            'aula': r['aula'],
            'paginas': r['paginas'],
            'topicos': r['topicos'],
            'peso': peso,
            'min_q': min_q,
            'item_arg': item_arg
        })
    with open(out_dir / f"{subj}.json", 'w', encoding='utf-8') as f:
        json.dump(subj_data, f, ensure_ascii=False, indent=2)
    print(f"Saved {subj}: {len(subj_data)} trechos, {sum(d['min_q'] for d in subj_data)} questions target")
