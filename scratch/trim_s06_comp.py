with open('content/material/direito-administrativo/m23/a24-s06.md', encoding='utf-8') as f:
    t = f.read()

p1 = t.find('A sistemática legal organiza-se em pilares fundamentais:')
p2 = t.find('> [!lei] Art. 21, § 1º, da Lei nº 8.429/1992')

new_comp = '''A sistemática legal organiza-se em pilares essenciais:
- **Dedução do ressarcimento (art. 12, § 6º):** abatem-se da condenação indenizatória quantias já pagas nas esferas penal, administrativa ou cível sobre o mesmo fato.
- **Compensação de sanções (art. 21, § 5º):** penalidades pecuniárias de mesma natureza aplicadas em outras instâncias são compensadas com as multas da LIA.
- **Vedação de bis in idem (art. 12, § 7º):** sanções a pessoas jurídicas pela LIA e pela Lei nº 12.846/2013 não podem incidir em duplicidade.
- **Atos de controle (art. 21, § 1º):** pareceres de órgãos de controle que serviram de suporte à conduta do agente devem ser considerados pelo juiz.

'''

t = t[:p1] + new_comp + t[p2:]

with open('content/material/direito-administrativo/m23/a24-s06.md', 'w', encoding='utf-8') as f:
    f.write(t)
print('Successfully trimmed comp')
