import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('content/summaries/estatistica/a08.json', encoding='utf-8') as f:
    d = json.load(f)

for s in d['segments']:
    print(f"=== {s['id']} ===")
    print(f"Fingerprint: {s['fingerprint']}")
    print(f"Synthetic: {s.get('synthetic')}")
    print()
