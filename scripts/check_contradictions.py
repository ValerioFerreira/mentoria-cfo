import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('audit_exatas_all_items.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Patterns for contradictions or flaws
issues = []

# Keywords in explanation that suggest the statement was actually False, or True
# When isTrue is True, but explanation says it is False/incorrect/wrong
# When isTrue is False, but explanation says it is True/correct/right
for it in items:
    iid = it['id']
    st = it['statement']
    exp = it['explanation']
    is_true = it['isTrue']
    
    exp_l = exp.lower()
    st_l = st.lower()
    
    # 1. Contradiction between isTrue and explanation
    # If isTrue is True:
    if is_true:
        # Explanations that explicitly say the item or statement is wrong/false
        wrong_triggers = [
            'item falso', 'item incorreto', 'item errado', 'afirmativa incorreta', 'afirmativa falsa',
            'o item é falso', 'o item é incorreto', 'o item é errado', 'o item está incorreto', 'o item está errado',
            'está incorreto', 'está errado', 'é falso', 'é incorreto'
        ]
        for wt in wrong_triggers:
            if wt in exp_l:
                # check if it's not saying "não é falso" or "dizer que ... é falso"
                if not re.search(r'(não|jamais|nunca|nem)\s+' + re.escape(wt), exp_l):
                    issues.append({
                        'id': iid,
                        'category': 'contradicao_gabarito',
                        'severity': 'Alta',
                        'detail': f'isTrue=True mas explicação contém "{wt}"',
                        'item': it
                    })
                    break
    else: # isTrue is False:
        right_triggers = [
            'item correto', 'item verdadeiro', 'afirmativa correta', 'afirmativa verdadeira',
            'o item é correto', 'o item é verdadeiro', 'o item está correto',
            'está correto', 'é correto', 'é verdadeiro'
        ]
        for rt in right_triggers:
            if rt in exp_l:
                if not re.search(r'(não|jamais|nunca|nem)\s+' + re.escape(rt), exp_l):
                    # Be careful if explanation says "o correto seria..." or "o modo correto é..."
                    if 'o correto' not in rt:
                        issues.append({
                            'id': iid,
                            'category': 'contradicao_gabarito',
                            'severity': 'Alta',
                            'detail': f'isTrue=False mas explicação contém "{rt}"',
                            'item': it
                        })
                        break

print(f"Total potential contradiction issues: {len(issues)}")
for iss in issues:
    print(iss['id'], iss['detail'])
    print("  St:", iss['item']['statement'])
    print("  Exp:", iss['item']['explanation'])
    print("-" * 50)
