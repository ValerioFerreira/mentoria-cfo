import json, sys

sys.stdout.reconfigure(encoding='utf-8')

for aula in ['a14', 'a15', 'a16', 'a17']:
    with open(f'content/summaries/fisica/{aula}.json', encoding='utf-8') as f:
        d = json.load(f)
    print(f"=== AULA {aula} ({len(d.get('segments', []))} segmentos) ===")
    for s in d.get('segments', []):
        print(f"  {s['id']} (págs {s.get('fingerprint', {}).get('startPage')}-{s.get('fingerprint', {}).get('endPage')}): {s.get('fingerprint', {}).get('startTopic')}")
        synth = s.get('synthetic', [])
        if isinstance(synth, list) and len(synth) > 0:
            print("    Synth:", synth[:2])
