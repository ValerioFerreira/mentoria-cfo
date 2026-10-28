from pathlib import Path

p = Path("scratch/build_rl/novas_bloco2.py")
text = p.read_text(encoding="utf-8")

# Fix 1: Q#62 (index 18)
old1 = '"stem": "Um argumento dedutivo é considerado formalmente INVÁLIDO quando ocorre qual circunstância técnica?",'
new1 = '"stem": "Um argumento dedutivo é considerado formalmente INVÁLIDO quando ocorre qual circunstância técnica? Assinale a opção correta.",'
assert old1 in text, "old1 not found"
text = text.replace(old1, new1)

# Fix 2: Q#66 (index 22)
old2 = '"stem": "Para verificar a validade de um argumento dedutivo contendo três proposições simples pelo método da tabela-verdade, o analista constrói as colunas das premissas e da conclusão. O argumento será considerado VÁLIDO se:",'
new2 = '"stem": "Para verificar a validade de um argumento dedutivo contendo três proposições simples pelo método da tabela-verdade, o analista constrói as colunas das premissas e da conclusão. Com base nessa técnica, assinale a condição necessária para o argumento ser considerado VÁLIDO:",'
assert old2 in text, "old2 not found"
text = text.replace(old2, new2)

# Fix 3: Q#72 (index 28)
old3 = '"expl": "O Modus Ponens (modo de afirmar pelo antecedente) estabelece que, dada a condicional verdadeira p -> q e a afirmação do seu antecedente p, conclui-se de forma válida e necessária o consequente q. A estrutura da opção B comete a falácia da afirmação do consequente e a opção C comete a negação do antecedente."'
new3 = '"expl": "O Modus Ponens (modo de afirmar pelo antecedente) estabelece que, dada a condicional verdadeira p -> q e a afirmação do seu antecedente p, conclui-se de forma válida e necessária o consequente q. Estruturas que invertem a ordem incorrem na falácia da afirmação do consequente ou na falácia da negação do antecedente."'
assert old3 in text, "old3 not found"
text = text.replace(old3, new3)

# Fix 4: Q#74 (index 30)
old4 = '"stem": "Considere o seguinte raciocínio: \'Regra: Todos os feijões deste saco são brancos. Premissa fática: Estes feijões foram retirados deste saco. Conclusão: Logo, estes feijões são brancos\'. Conforme a classificação de Peirce, esse raciocínio é um exemplo canônico de:",'
new4 = '"stem": "Considere o seguinte raciocínio: \'Regra: Todos os feijões deste saco são brancos. Premissa fática: Estes feijões foram retirados deste saco. Conclusão: Logo, estes feijões são brancos\'. Conforme a classificação de Peirce, assinale a opção que categoriza esse raciocínio:",'
assert old4 in text, "old4 not found"
text = text.replace(old4, new4)

# Fix 5: Q#75 (index 31)
old5 = '"stem": "Considere o raciocínio: \'Premissa fática: Estes feijões foram retirados deste saco. Resultado observado: Estes feijões são brancos. Conclusão: Logo, todos os feijões deste saco são brancos\'. Segundo a conceituação de Peirce, essa modalidade de raciocínio classifica-se como:",'
new5 = '"stem": "Considere o raciocínio: \'Premissa fática: Estes feijões foram retirados deste saco. Resultado observado: Estes feijões são brancos. Conclusão: Logo, todos os feijões deste saco são brancos\'. Segundo a conceituação de Peirce, assinale a modalidade que classifica esse raciocínio:",'
assert old5 in text, "old5 not found"
text = text.replace(old5, new5)

# Fix 6: Q#76 (index 32)
old6 = '"stem": "Considere o raciocínio: \'Regra conhecida: Todos os feijões deste saco são brancos. Fato surpreendente observado: Estes feijões sobre a mesa são brancos. Conclusão: Logo, é plausível supor que estes feijões tenham vindo deste saco\'. Sob a ótica de Peirce, essa inferência exemplifica a:",'
new6 = '"stem": "Considere o raciocínio: \'Regra conhecida: Todos os feijões deste saco são brancos. Fato surpreendente observado: Estes feijões sobre a mesa são brancos. Conclusão: Logo, é plausível supor que estes feijões tenham vindo deste saco\'. Sob a ótica de Peirce, assinale o tipo de inferência exemplificado:",'
assert old6 in text, "old6 not found"
text = text.replace(old6, new6)

p.write_text(text, encoding="utf-8")
print("novas_bloco2.py updated successfully!")
