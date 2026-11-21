import json

for a in ['a01', 'a12']:
    path = f'content/summaries/biologia/{a}.json'
    with open(path, 'r', encoding='utf-8') as f:
        d = json.load(f)
    print(f"=== {a} ===")
    for s in d.get('segments', []):
        print(f"  Segment: {s.get('id')}")
        print(f"  Title: {s.get('title')}")
        print(f"  Topics: {s.get('topics')}")
        print(f"  Analytic length: {len(s.get('analytic', ''))}")
