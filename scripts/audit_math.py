import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('audit_exatas_all_items.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Inspect specific topics in Mathematics:
# a00: Conjuntos numéricos
# a01: Aritmética básica e potenciação/radiciação
# a02: Frações, decimais, dízimas
# a03: Razão e proporção
# a04: Regra de três
# a05: Porcentagem
# a06: Juros simples
# a07: Juros compostos
# a08: Equações de 1º e 2º grau, inequações
# a09: Sistemas de equações
# a10: Função afim
# a11: Função quadrática
# a12: Função exponencial e logarítmica
# a13: PA e PG
# a14: Matrizes, determinantes e sistemas lineares
# a15: Análise combinatória
# a16: Probabilidade
# a17: Trigonometria
# c01: Geometria plana
# c02: Geometria espacial

print("Auditing Mathematics...")
math_items = [it for it in items if it['disciplina'] == 'matematica']

for it in math_items:
    iid = it['id']
    st = it['statement']
    exp = it['explanation']
    is_true = it['isTrue']
    
    # Check 1: Inequações / intervalos
    # Check 2: Logaritmos (propriedades, bases, domínios)
    if 'log' in st.lower() or 'logaritmo' in st.lower():
        # verify properties
        pass
    # Check 3: Fórmulas de juros
    if 'juros' in st.lower():
        pass
    # Check 4: Trigonometria
    if any(k in st.lower() for k in ['seno', 'cosseno', 'tangente', 'sen ', 'cos ', 'tg ']):
        pass

print("Math scan complete.")
