with open('content/material/direito-constitucional/m08/a10-s01.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove jargon
text = text.replace('consubstancia a Câmara Alta', 'representa a Câmara Alta')
text = text.replace('Sistema Eleitoral de Escolha', 'Sistema Eleitoral Adotado')

# 2. Remove 'pessoal,'
text = text.replace('pessoal,', 'individual,')
text = text.replace('informações pessoais sobre', 'esclarecimentos diretos sobre')

# 3. Add [!lei] callout for art. 57 and art. 45
# Replace literal quotes in prose with paraphrases or put in [!lei]

# Literal quote 1:
# "União: adota o bicameralismo federativo (art. 44). O Poder Legislativo é exercido pelo Congresso Nacional, composto pela Câmara dos Deputados e pelo Senado Federal;"
text = text.replace(
    'União: adota o bicameralismo federativo (art. 44). O Poder Legislativo é exercido pelo Congresso Nacional, composto pela Câmara dos Deputados e pelo Senado Federal;',
    'União: adota a fórmula bicameral federativa prevista no art. 44 da Carta Magna, atuando o parlamento federal por meio da integração harmônica entre deputados federais e senadores;'
)

# Literal quote 2:
# 'O art. 57, § 2º, estabelece uma regra de continuidade financeira: "A sessão legislativa não será interrompida sem a aprovação do projeto de lei de diretrizes orçamentárias".'
text = text.replace(
    'O art. 57, § 2º, estabelece uma regra de continuidade financeira: "A sessão legislativa não será interrompida sem a aprovação do projeto de lei de diretrizes orçamentárias".',
    'O art. 57, § 2º, da Constituição impõe uma condicionante temporal severa ao calendário parlamentar: o recesso legislativo do mês de julho fica terminantemente obstado caso o Congresso não conclua a votação da lei de diretrizes orçamentárias.'
)

# Literal quote 3:
# 'O art. 57, § 4º, estipula que cada Casa reúne-se em sessões preparatórias para a posse dos membros e eleição de suas Mesas "para mandato de 2 (dois) anos, vedada a recondução para o mesmo cargo na eleição imediatamente subsequente".'
text = text.replace(
    'O art. 57, § 4º, estipula que cada Casa reúne-se em sessões preparatórias para a posse dos membros e eleição de suas Mesas "para mandato de 2 (dois) anos, vedada a recondução para o mesmo cargo na eleição imediatamente subsequente".',
    'O texto constitucional prescreve no art. 57, § 4º, que as Casas reunir-se-ão em sessões preparatórias para a posse dos parlamentares e escolha dos integrantes de seus órgãos diretivos, fixando mandato bienal e proibindo expressamente a reeleição contígua para a mesma função diretiva.'
)

# Paraphrase warnings:
text = text.replace(
    'a fiscalização contábil, financeira, orçamentária, operacional e patrimonial do Poder Executivo, bem como a investigação parlamentar de irregularidades mediante Comissões Parlamentares de Inquérito (CPIs).',
    'o controle financeiro, contábil e orçamentário dos atos da administração pública, em conjunto com o Tribunal de Contas, além de apurações promovidas por Comissões Parlamentares de Inquérito.'
)

# Add [!lei] callouts to satisfy minimum quadros (needs >= 6) and provide central law text
lei_callout = '''> [!lei] Art. 57, caput e § 4º, da Constituição Federal
> O Congresso Nacional reunir-se-á, anualmente, na Capital Federal, de 2 de fevereiro a 17 de julho e de 1º de agosto a 22 de dezembro.
> [...]
> § 4º Cada uma das Casas reunir-se-á em sessões preparatórias, a partir de 1º de fevereiro, no primeiro ano da legislatura, para a posse de seus membros e eleição das respectivas Mesas, para mandato de 2 (dois) anos, vedada a recondução para o mesmo cargo na eleição imediatamente subsequente.
'''

text = text.replace('### Sessões preparatórias\n\nRealizam-se em cada Casa', '### Sessões preparatórias\n\n' + lei_callout + '\nRealizam-se em cada Casa')

# Split long sentences to reduce sentenceWords <= 25
text = text.replace('; cada um exercido', '. Cada um é exercido')
text = text.replace('; a autolesão', '. A autolesão')
text = text.replace('; logo, o civil', '. Logo, o civil')
text = text.replace('; a semelhança', '. A semelhança')
text = text.replace(', sendo a imputação falsa', '. A imputação falsa')
text = text.replace('O bicameralismo brasileiro é qualificado pela doutrina como igualitário (ou de equilíbrio relativo): não há subordinação hierárquica entre a Câmara dos Deputados e o Senado Federal. Salvo hipóteses constitucionais expressas de iniciativa ou revisão de projetos, ambas as Casas exercem papéis simétricos no aperfeiçoamento da legislação federal.', 'O bicameralismo brasileiro é qualificado como igualitário. Não existe hierarquia entre a Câmara dos Deputados e o Senado Federal. Ambas as Casas exercem funções simétricas na produção das leis federais.')
text = text.replace('O quantitativo global de cadeiras e a representação de cada Estado e do DF são fixados por lei complementar (Lei Complementar nº 78/1993), observada a proporção da população apurada em censo demográfico oficial:', 'O quantitativo total de vagas e a bancada de cada Estado e do DF são fixados por lei complementar. A distribuição observa a proporção da população aferida pelo censo demográfico:')

with open('content/material/direito-constitucional/m08/a10-s01.md', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated a10-s01.md')
