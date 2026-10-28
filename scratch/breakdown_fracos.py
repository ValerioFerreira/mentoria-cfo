import csv
from collections import defaultdict
from pathlib import Path

csv_path = Path("pipeline/briefs/ineditas-fracos.csv")
with open(csv_path, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f, delimiter=";")
    rows = list(reader)

by_disc = defaultdict(lambda: {"trechos": 0, "faltam": 0, "segs": []})
for r in rows:
    disc = r["disciplina"]
    by_disc[disc]["trechos"] += 1
    by_disc[disc]["faltam"] += int(r["faltam"])
    by_disc[disc]["segs"].append(r)

print(f"Total deficient segments: {len(rows)}")
total_faltam = sum(int(r["faltam"]) for r in rows)
print(f"Total questions needed: {total_faltam}\n")

# Order of disciplines according to weight in exam (edital PCPE / briefing)
priority = [
    "contabilidade-geral",
    "informatica",
    "lingua-portuguesa",
    "estatistica",
    "legislacao-pcpe",
    "direito-processual-penal",
    "direito-constitucional",
    "matematica",
    "raciocinio-logico",
    "legislacao-penal-especial",
    "direito-administrativo",
    "direito-penal",
]

for d in priority:
    info = by_disc[d]
    print(f"{d:<27} | {info['trechos']:>2} trechos | {info['faltam']:>3} questões")
