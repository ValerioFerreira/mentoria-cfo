import json
import re

def audit():
    with open('audit_exatas_all_items.json', 'r', encoding='utf-8') as f:
        items = json.load(f)

    print(f"Loaded {len(items)} items.")
    
    # Check 1: Empty or very short statements / explanations
    suspicious = []
    for it in items:
        st = it['statement'].strip()
        exp = it['explanation'].strip()
        iid = it['id']
        
        # Meta phrases
        meta_phrases = [
            'conforme a questão', 'o examinador', 'a alternativa correta',
            'conforme o texto', 'texto acima', 'figura acima', 'gráfico acima',
            'quadro acima', 'tabela acima', 'assinale a alternativa', 'gabarito oficial'
        ]
        for mp in meta_phrases:
            if mp in st.lower():
                suspicious.append({
                    'id': iid,
                    'issue': f'Meta-language: "{mp}" in statement',
                    'item': it
                })
                
        # Check for truncated statement or missing operator
        # like "+ =" or "= +" or double operators or dangling dots
        if re.search(r'[\+\-\*\/=]{2,}', st) and '==' not in st:
            suspicious.append({
                'id': iid,
                'issue': 'Double operator in statement',
                'item': it
            })
            
        # Check for unclosed parentheses or brackets
        if st.count('(') != st.count(')'):
            suspicious.append({
                'id': iid,
                'issue': 'Unbalanced parentheses in statement',
                'item': it
            })
        if st.count('[') != st.count(']'):
            suspicious.append({
                'id': iid,
                'issue': 'Unbalanced brackets in statement',
                'item': it
            })

    print(f"Suspicious items found by syntactic checks: {len(suspicious)}")
    for s in suspicious:
        print(s['id'], s['issue'])
        print("  St:", s['item']['statement'])

if __name__ == '__main__':
    audit()
