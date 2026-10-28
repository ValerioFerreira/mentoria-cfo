import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, "pipeline/questoes")
from ineditas import item_for_segment, segments

csv_path = Path("pipeline/briefs/ineditas-fracos.csv")
with open(csv_path, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f, delimiter=";")
    rows = list(reader)

items_needed = {}
errors = []

for r in rows:
    disc = r["disciplina"]
    seg = r["trecho"]
    
    # Test without item argument
    try:
        item = item_for_segment(disc, seg, None)
        if not item:
            errors.append(f"{seg}: no item returned")
    except Exception as e:
        # Ambiguous segment mapping: check which items it has in edital
        edital_file = Path(f"content/edital/pcpe/{disc}.json")
        if not edital_file.exists():
            edital_file = Path(f"content/edital/{disc}.json")
        matched = []
        if edital_file.exists():
            data = json.loads(edital_file.read_text(encoding="utf-8"))
            for p in data.get("points", []):
                for sub in p.get("subpoints", []):
                    if seg in sub.get("segments", []):
                        matched.append(sub.get("id") or sub.get("code") or p.get("id"))
        items_needed[seg] = matched
        errors.append(f"{seg}: requires item, candidates: {matched}")

print(f"Total checked: {len(rows)}")
print(f"Ambiguous or error segments: {len(errors)}")
for e in errors:
    print("  ", e)
