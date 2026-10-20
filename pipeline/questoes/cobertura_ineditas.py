"""Confere se todo trecho de `pipeline/briefs/ineditas-faltantes.csv` já tem o mínimo de inéditas de MÚLTIPLA ESCOLHA
(`content/questoes/ineditas/mc/*.txt`; `--todas` conta também as certo/errado de `content/questoes/ineditas/*.txt`).
    pipeline/.venv/Scripts/python pipeline/questoes/cobertura_ineditas.py [--minimo 6]"""
import csv, re, sys
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.stdout.reconfigure(encoding="utf-8")
minimo = int(sys.argv[sys.argv.index("--minimo") + 1]) if "--minimo" in sys.argv else 6
cnt = Counter()
pastas = [ROOT / "content/questoes/ineditas/mc"] + ([ROOT / "content/questoes/ineditas"] if "--todas" in sys.argv else [])
for f in [x for d in pastas for x in d.glob("*.txt")]:
    for m in re.finditer(r"^@@\s*(\S+)\s*\|", f.read_text(encoding="utf-8"), re.M):
        cnt[f"{f.stem}/{m.group(1)}"] += 1
rows = list(csv.DictReader(open(ROOT / "pipeline/briefs/ineditas-faltantes.csv", encoding="utf-8-sig"), delimiter=";"))
falta = [(r["trecho"], cnt[r["trecho"]]) for r in rows if cnt[r["trecho"]] < minimo]
for t, n in falta: print(f"{t}: {n}/{minimo}")
print(f"{len(rows) - len(falta)}/{len(rows)} trechos com ao menos {minimo} inéditas de múltipla escolha; faltam {sum(minimo - n for _, n in falta)} questões")
