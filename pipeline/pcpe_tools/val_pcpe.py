import sys
sys.path.insert(0,'pipeline')
from pathlib import Path
from validate_content import ITEMS_DIR, validate_file
S="lingua-portuguesa informatica raciocinio-logico matematica estatistica contabilidade-geral legislacao-pcpe direito-constitucional direito-administrativo direito-penal legislacao-penal-especial direito-processual-penal".split()
import collections
c=collections.Counter(); ex=[]
for d in S:
    seen=[]
    for f in sorted((ITEMS_DIR/d).glob('*.json')):
        errs,_w,_s=validate_file(f,seen)
        c[d]+=len(errs); ex+= [f"{d}/{f.name}: {e}" for e in errs][:3]
print(dict(c)); print('\n'.join(ex[:25]))
