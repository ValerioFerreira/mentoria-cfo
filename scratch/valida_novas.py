import sys
from pathlib import Path

sys.path.insert(0, "pipeline/questoes")
from ineditas_mc_nativas import parse, check, LETTERS
from collections import Counter

p = Path("scratch/novas_questoes/direito-administrativo.txt")
if not p.exists():
    print(f"Arquivo {p} ainda nao existe.")
    sys.exit(0)

qs = parse(p)
errs = check(qs)
c = Counter(q["answer"] for q in qs)

print(f"Total de questoes: {len(qs)}")
print("Gabaritos:", " ".join(f"{l}: {c[l]}" for l in LETTERS))
print(f"Erros encontrados: {len(errs)}")
for e in errs[:20]:
    print("ERRO:", e)
if len(errs) > 20:
    print(f"... e mais {len(errs)-20} erros.")
