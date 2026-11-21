import json

with open('content/summaries/direito-constitucional/a08.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

with open('scratch/a08_s08_s09_analytic.txt', 'w', encoding='utf-8') as out:
    for seg in d.get('segments', []):
        if seg.get('id') in ['direito-constitucional/a08/s08', 'direito-constitucional/a08/s09']:
            out.write(f"=== {seg.get('id')} ===\n")
            out.write(seg.get('analytic', '') + "\n\n")

print("Done writing scratch/a08_s08_s09_analytic.txt")
