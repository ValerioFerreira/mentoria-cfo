import json

with open('content/summaries/direito-constitucional/a10.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for s in data.get('segments', []):
    sid = s.get('id', '?')
    sec_num = sid.split('/')[-1]
    with open(f'scratch/dc_a10_{sec_num}.txt', 'w', encoding='utf-8') as out:
        out.write(f"ID: {sid}\n")
        out.write(f"Fingerprint: {s.get('fingerprint')}\n")
        out.write(f"NOTES: {s.get('notes')}\n")
        out.write(f"ANALYTIC:\n{s.get('analytic', '')}\n")
print(f"Exported {len(data.get('segments', []))} segments to scratch/dc_a10_*.txt")
