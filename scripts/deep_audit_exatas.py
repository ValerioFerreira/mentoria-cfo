import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('audit_exatas_all_items.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print("=== VERIFICAÇÃO DETALHADA DE ITENS ===")

findings = []

for it in items:
    iid = it['id']
    st = it['statement']
    exp = it['explanation']
    is_true = it['isTrue']
    disc = it['disciplina']
    aula = it['aula']
    
    # 1. Checagem de Matemática
    # Conjuntos, Potenciação, Radiciação, Funções, Trigonometria, Matrizes, Geometria, Análise Combinatória, PA/PG, Juros
    
    # Detectar erros comuns de digitação de fórmulas ou enunciados
    # Ex: seno, cosseno, tangentes, logaritmos, determinantes, derivadas, integrais
    
    # Vamos verificar se há incoerências específicas
    # Exemplo: fatorial, permutações, arranjos, combinações
    
    # 2. Checagem de Raciocínio Lógico
    # De Morgan, condicional, bicondicional, disjunção, conjunção, tautologia, silogismos
    
    # 3. Checagem de Estatística
    # Média, mediana, moda, variância, desvio padrão, distribuições, hipóteses
    
    # 4. Checagem de Física
    # Cinemática, Newton, Termodinâmica, Ondas, Óptica, Hidrostática, Eletricidade

print("Script inicializado.")
