"""Uso: split_src.py <disc/aNN>  -> grava $TEMP/<aNN>_<k>.txt por trecho (texto limpo) e lista tamanhos."""
import os, re, subprocess, sys, unicodedata
aula = sys.argv[1]
root = os.path.join(os.path.dirname(__file__), '..', '..')
subprocess.run(['bash', os.path.join(os.path.dirname(__file__), 'aula.sh'), aula], stdout=subprocess.DEVNULL, cwd=root)
tmp = os.environ.get('TEMP', '.')
t = open(os.path.join(tmp, 'aula.txt'), encoding='utf-8', errors='replace').read()
t = ''.join(' ' if unicodedata.category(c) == 'Cf' else c for c in t)
t = re.sub(r'[ \t]+', ' ', t)
t = re.sub(r'(?<![.:;?!])\n(?!=====|# |Art\.|§|[IVX]+ )', ' ', t)
t = re.sub(r'(Herbert Almeida|Renan Araujo|Equipe [A-Za-zç ]+Estratégia Concursos|Equipe Direito [A-Za-z]+)[ ,]*', '', t)
name = aula.split('/')[-1]
for i, p in enumerate(re.split(r'(?m)^# ', t)[1:], 1):
    path = os.path.join(tmp, f'{name}_{i}.txt')
    open(path, 'w', encoding='utf-8').write(p)
    print(i, len(p), path)
