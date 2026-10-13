import json
import glob
import re

def clean_text(s: str) -> str:
    # Remove '(Somente em PDF)' or '(Somente em Vídeo)' and trim extra whitespace or hyphens
    s = re.sub(r'\(Somente em PDF\)\s*', '', s, flags=re.IGNORECASE)
    s = re.sub(r'\(Somente em V[ií]deo\)\s*', '', s, flags=re.IGNORECASE)
    s = re.sub(r'\s{2,}', ' ', s)
    return s.strip()

# 1. Clean content/catalog.json
for cat_path in ['content/catalog.json', 'web/content/catalog.json']:
    cat = json.load(open(cat_path, 'r', encoding='utf-8'))
    changed = False
    for subj in cat['subjects']:
        for aula in subj['aulas']:
            old_t = aula['title']
            old_st = aula['shortTitle']
            new_t = clean_text(old_t)
            new_st = clean_text(old_st)
            if new_t != old_t or new_st != old_st:
                print(f"[{cat_path}] {aula['id']}: '{old_t}' -> '{new_t}' | '{old_st}' -> '{new_st}'")
                aula['title'] = new_t
                aula['shortTitle'] = new_st
                changed = True
    if changed:
        with open(cat_path, 'w', encoding='utf-8') as f:
            json.dump(cat, f, indent=2, ensure_ascii=False)
            f.write('\n')

# 2. Clean structure/*.json
for struct_path in glob.glob('content/structure/*.json') + glob.glob('web/content/structure/*.json'):
    data = json.load(open(struct_path, 'r', encoding='utf-8'))
    changed = False
    for aula in data.get('aulas', []):
        for topic in aula.get('topics', []):
            old_t = topic['title']
            new_t = clean_text(old_t)
            if new_t != old_t:
                print(f"[{struct_path}] topic: '{old_t}' -> '{new_t}'")
                topic['title'] = new_t
                changed = True
    if changed:
        with open(struct_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write('\n')

print("Titles cleaned successfully.")
