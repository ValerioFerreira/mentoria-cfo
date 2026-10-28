import json

for s in ['administracao', 'direitos-humanos', 'direito-processual-penal-militar']:
    st = json.load(open(f'content/structure/{s}.json', encoding='utf-8'))
    sg = json.load(open(f'content/segments/{s}.json', encoding='utf-8'))
    print(f'=== {s} ===')
    for a in st['aulas']:
        print(f"  {a['id']}: {a['title']} (totalPages: {a['totalPages']}, theory: {a['theoryPages']}, segs: {a['segments']})")
        for t in a.get('topics', []):
            if any(w in t['title'].lower() for w in ['prof', 'fantini', 'equipe', 'telegram', 'instagram', 'somente', 'estratégia', 'estrategia', 'fórum']):
                print(f"    BAD TOPIC in {a['id']}: {t['title']}")
    for seg in sg['segments']:
        if any(w in seg['startTopic'].lower() for w in ['prof', 'fantini', 'equipe', 'telegram', 'instagram', 'somente', 'estratégia', 'estrategia', 'fórum']):
            print(f"    BAD SEG TOPIC in {seg['id']}: {seg['startTopic']}")
