import json

path = 'content/summaries/direito-penal-militar/a09.json'
with open(path, 'r', encoding='utf-8') as f:
    d = json.load(f)

print(f"Total segments: {len(d.get('segments', []))}")
for s in d.get('segments', []):
    sid = s.get('id').replace('/', '_')
    with open(f'scratch/{sid}.txt', 'w', encoding='utf-8') as out:
        out.write(f"ID: {s.get('id')}\n")
        out.write(f"Fingerprint: {s.get('fingerprint')}\n")
        out.write("ANALYTIC:\n")
        out.write(s.get('analytic', ''))
    print(f"  {s.get('id')}: {len(s.get('analytic', ''))} chars")

print("Exportados resumos em scratch/direito-penal-militar_a09_*.txt")
