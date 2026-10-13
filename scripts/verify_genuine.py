import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('audit_exatas_all_items.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Inspect every single genuine item across all 4 subjects
# Check:
# 1. Statement truth value vs isTrue
# 2. Explanation consistency
# 3. Precision of mathematical statements

print("Verifying genuine items...")
anomalies = []

for it in items:
    iid = it['id']
    st = it['statement']
    exp = it['explanation']
    ans = it['isTrue']
    d = it['disciplina']
    
    # Check if template
    if any(k in st for k in ['âmbito de', 'Conceitos Estruturantes', 'balizas conceituais', 'critérios normativos']):
        continue
        
    # Check for truncated formulas or text
    if st.endswith('...') or '??' in st or re.search(r'\b[a-zA-Z]\s*=\s*\.', st):
        anomalies.append({
            'id': iid,
            'issue': 'Truncated or malformed formula',
            'item': it
        })

print(f"Syntactic anomalies: {len(anomalies)}")
