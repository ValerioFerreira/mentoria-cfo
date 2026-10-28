import sys
from pathlib import Path
sys.path.insert(0, str(Path(".").resolve()))
import re

from pipeline.questoes.ineditas_mc_nativas import parse, check

path = Path("scratch/novas_questoes/raciocinio-logico.txt")
qs = parse(path)
print(f"Parsed {len(qs)} questions.")

errs = check(qs)
print(f"Validator check errors: {len(errs)}")
for e in errs:
    print("  ERRO:", e)

text = path.read_text(encoding="utf-8")
for w in ["aula", "curso", "professor", "professora"]:
    m = re.findall(rf"\b{w}\b", text, re.I)
    if m:
        print(f"Forbidden word found: {w} ({len(m)} times)")

comment_letter_errs = []
for q in qs:
    ans = q["answer"]
    expl = q["explanation"]
    other_letters = "".join(l for l in "ABCDE" if l != ans)
    pattern = rf"\b(?:alternativa|opção|opcao|letra|assertiva|item)\s+([{other_letters}])\b"
    m = re.findall(pattern, expl, re.I)
    if m:
        comment_letter_errs.append((q["segment"], q["n"], m, expl[:80]))

print(f"Comment letter errors (wrong option letters cited): {len(comment_letter_errs)}")
for c in comment_letter_errs:
    print("  Comment letter cited:", c)

if not errs and not comment_letter_errs:
    print("\nALL CHECKS PASSED WITH 0 ERRORS!")
