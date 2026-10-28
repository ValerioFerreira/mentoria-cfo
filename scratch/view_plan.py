import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

plan = json.load(open('scratch/plan_dpp.json', encoding='utf-8'))
for p in plan:
    print(f"Q{p['q_num']:03d} | {p['seg']} | Ans: {p['ans']} | {p['topicos'][:50]}")
