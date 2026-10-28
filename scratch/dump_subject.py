import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


# Add pipeline/questoes to sys.path
sys.path.insert(0, str(Path("pipeline/questoes").resolve()))
from ineditas import parse

subject = sys.argv[1] if len(sys.argv) > 1 else "legislacao-penal-especial"
path = Path(f"content/questoes/ineditas/{subject}.txt")
qs = parse(path)

start = int(sys.argv[2]) if len(sys.argv) > 2 else 1
end = int(sys.argv[3]) if len(sys.argv) > 3 else len(qs)

for q in qs:
    if start <= q["n"] <= end:
        print(f"=== Q#{q['n']} | {q['segment']} | GAB: {q['answer']} | item={q.get('item')} ===")
        print(q["statement"])
        print(f"// {q['explanation']}")
        print()
