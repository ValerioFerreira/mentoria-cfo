import json

for a in ['a01', 'a12']:
    path = f'content/summaries/biologia/{a}.json'
    with open(path, 'r', encoding='utf-8') as f:
        d = json.load(f)
    for s in d.get('segments', []):
        sid = s.get('id').replace('/', '_')
        with open(f'scratch/{sid}.txt', 'w', encoding='utf-8') as out:
            out.write(f"ID: {s.get('id')}\n")
            out.write(f"Fingerprint: {s.get('fingerprint')}\n")
            out.write("ANALYTIC:\n")
            out.write(s.get('analytic', ''))
print("Extraídos resumos analíticos em scratch/biologia_*.txt")
