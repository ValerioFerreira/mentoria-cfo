"""Aplica os sintéticos (content/summaries) ao bizu.summary SÓ das disciplinas do PCPE (content/items), como
apply_synthetic.py, sem tocar nas demais nem no espelho web (use mirror_web.py depois). Uso: python apply_synth_pcpe.py [disc ...]"""
import json, sys, re
from pathlib import Path
sys.path.insert(0, 'pipeline')
from apply_synthetic import bullet, dump
from config import CONTENT_DIR
PCPE = "lingua-portuguesa informatica raciocinio-logico matematica estatistica contabilidade-geral legislacao-pcpe direito-constitucional direito-administrativo direito-penal legislacao-penal-especial direito-processual-penal".split()
discs = sys.argv[1:] or PCPE
n = 0
for d in discs:
    for f in sorted((CONTENT_DIR / 'summaries' / d).glob('*.json')):
        doc = json.loads(f.read_text(encoding='utf-8'))
        synth = {s['id']: [bullet(x) for x in s['synthetic']] for s in doc.get('segments', []) if s.get('synthetic')}
        t = CONTENT_DIR / 'items' / d / f.name
        if not synth or not t.exists():
            continue
        it = json.loads(t.read_text(encoding='utf-8'))
        ch = False
        for seg in it.get('segments', []):
            if seg['id'] in synth and seg.get('bizu') and seg['bizu'].get('summary') != synth[seg['id']]:
                seg['bizu']['summary'] = synth[seg['id']]; ch = True; n += 1
        if ch:
            dump(t, it)
print('trechos alterados:', n)
