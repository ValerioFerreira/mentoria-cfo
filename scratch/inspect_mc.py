import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, str(Path("pipeline/questoes").resolve()))
import ineditas_mc

rows = ineditas_mc.build()
print(f"Total MC: {len(rows)}")
for i, r in enumerate(rows):
    print(f"=== MC #{i+1}: {r['id']} | Subj: {r['subjectId']} | Gab: {r['answer']} ===")
    print(r["statement"])
    for o in r["options"]:
        marker = " [*]" if o["letter"] == r["answer"] else ""
        print(f"  {o['letter']}) {o['text']}{marker}")
    print("EXPL:", r["explanation"][:120], "...")
    print("-" * 50)
