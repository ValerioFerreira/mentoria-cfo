"""Limpa a saída de aula.sh (remove caracteres invisíveis e junta linhas quebradas) e grava em $TEMP/aula_clean.txt."""
import os, re, sys, unicodedata
src = os.path.join(os.environ.get('TEMP', '.'), 'aula.txt')
t = open(src, encoding='utf-8', errors='replace').read()
t = ''.join(' ' if unicodedata.category(c) == 'Cf' else c for c in t)
t = re.sub(r'[ \t]+', ' ', t)
t = re.sub(r'(?<![.:;?!])\n(?!=====|# |Art\.|§|[IVX]+ )', ' ', t)
out = os.path.join(os.environ.get('TEMP', '.'), 'aula_clean.txt')
open(out, 'w', encoding='utf-8').write(t)
print(len(t), out)
