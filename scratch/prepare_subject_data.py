import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
faltantes = list(csv.DictReader(open(ROOT / 'pipeline/briefs/ineditas-faltantes.csv', encoding='utf-8-sig'), delimiter=';'))

def get_subject_data(subject: str):
    rows = [r for r in faltantes if r['disciplina'] == subject]
    data = []
    for r in rows:
        peso = float(r['peso_prova'])
        min_q = 8 if peso >= 0.20 else 6
        data.append({
            'trecho': r['trecho'],
            'seg': r['trecho'].split('/', 1)[1],
            'aula': r['aula'],
            'paginas': r['paginas'],
            'topicos': r['topicos'],
            'peso': peso,
            'min_q': min_q
        })
    return data

if __name__ == '__main__':
    for subj in [
        'contabilidade-geral', 'informatica', 'lingua-portuguesa',
        'estatistica', 'matematica', 'raciocinio-logico',
        'direito-administrativo', 'direito-constitucional', 'direito-penal'
    ]:
        data = get_subject_data(subj)
        tot_q = sum(d['min_q'] for d in data)
        print(f"{subj}: {len(data)} trechos, {tot_q} questões mínimas")
