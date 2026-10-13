import json
import re

with open('audit_exatas_all_items.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Let's write an exhaustive verifier for items in all 4 subjects
# We check:
# 1. Template / placeholder items (raciocinio-logico)
# 2. Mathematical calculations where numbers in statement and explanation can be computed
# 3. Contradictions between statement, isTrue and explanation
# 4. Known issues from previous partial audits (e.g. diretrizes)

findings = []

for it in items:
    iid = it['id']
    st = it['statement']
    exp = it['explanation']
    is_true = it['isTrue']
    d = it['disciplina']
    
    # 1. Template check
    if any(k in st for k in ['no segmento raciocinio-logico', 'no âmbito de raciocinio-logico', 'Conceitos Estruturantes em raciocinio-logico', 'balizas conceituais consagradas', 'critérios normativos sem qualquer amparo legal', 'Diretrizes Gerais em raciocinio-logico', 'Aplicações Práticas no âmbito de raciocinio-logico', 'Fundamentos Teóricos em raciocinio-logico']):
        findings.append({
            'id': iid,
            'subject': d,
            'category': 'meta_linguagem_template',
            'severity': 'Alta',
            'statement': st,
            'isTrue': is_true,
            'explanation': exp,
            'issue': 'Item é um template genérico/place-holder sem conteúdo real da disciplina.',
            'proposal': 'Substituir por item conceitual autêntico de Raciocínio Lógico baseado no resumo do segmento.'
        })

print(f"Total template findings: {len(findings)}")
