import re

with open('content/material/direito-constitucional/m08/a10-s01.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace line 63
old_63 = '- **União:** adota o **bicameralismo federativo** (art. 44). O Poder Legislativo é exercido pelo Congresso Nacional, composto pela Câmara dos Deputados e pelo Senado Federal;'
new_63 = '- **União:** adota o modelo bicameral federativo previsto no art. 44 da Carta Magna, atuando o parlamento federal por meio da integração harmônica entre a Câmara dos Deputados e o Senado Federal;'
text = text.replace(old_63, new_63)

# Replace line 269
old_269 = 'O art. 57, § 4º, estipula que cada Casa reúne-se em sessões preparatórias para a posse dos membros e eleição de suas Mesas "para mandato de 2 (dois) anos, vedada a recondução para o mesmo cargo na eleição imediatamente subsequente".'
new_269 = 'O texto constitucional disciplina no art. 57, § 4º, que as Casas reunir-se-ão em sessões preparatórias para empossar seus membros e escolher os integrantes dos órgãos diretivos, fixando mandato de dois anos e proibindo a reeleição contígua para a mesma função diretiva.'
text = text.replace(old_269, new_269)

# Paraphrase "vedada a recondução para o mesmo cargo na eleição imediatamente subsequente" in line 344
text = text.replace(
    'eleição imediatamente subsequente dentro da mesma legislatura.',
    'escolha sucessiva no biênio seguinte dentro da mesma legislatura.'
)

# Trim ~250 words across sections to stay well below 3934
text = text.replace(
    'O art. 2º da Carta Magna estabelece a clássica divisão tripartite entre os Poderes da União: Legislativo, Executivo e Judiciário, independentes e harmônicos entre si. O poder estatal em si é uno, indivisível e emana do povo; o que se reparte entre os órgãos constitucionais são as diferentes funções estatais especializadas.\n\nO modelo adotado rejeita a separação estanque ou absoluta: cada órgão exerce com preponderância determinada função típica, desempenhando de modo acessório ou instrumental certas funções atípicas expressamente autorizadas pelo texto constitucional:',
    'O art. 2º da Carta Magna consagra a divisão entre os Poderes da União: Legislativo, Executivo e Judiciário, independentes e harmônicos. O poder estatal é uno e emana do povo; o que se reparte são as funções especializadas. O ordenamento adota a separação flexível: cada órgão exerce predominantemente uma função típica, desempenhando de modo acessório funções atípicas autorizadas pela Constituição:'
)

text = text.replace(
    'A condução administrativa, financeira e dos trabalhos legislativos de cada Casa parlamentar compete às respectivas Mesas Diretoras:\n\n- **Mesa da Câmara dos Deputados:** presidida pelo Presidente da Câmara;\n- **Mesa do Senado Federal:** presidida pelo Presidente do Senado;\n- **Mesa do Congresso Nacional (art. 57, § 5º):** estrutura mista presidida pelo Presidente do Senado Federal, sendo os demais cargos ocupados alternadamente pelos titulares equivalentes da Câmara e do Senado.\n\nA composição das Mesas deve assegurar, tanto quanto possível, a representação proporcional dos partidos e dos blocos parlamentares atuantes na Casa legislativa (art. 58, § 1º).',
    'A direção dos trabalhos legislativos e dos serviços administrativos compete às Mesas Diretoras da Câmara dos Deputados e do Senado Federal. A Mesa do Congresso Nacional (art. 57, § 5º) possui estrutura mista presidida pelo Presidente do Senado, revezando-se os demais cargos entre as duas Casas. A composição das Mesas assegura, quanto possível, a proporcionalidade partidária (art. 58, § 1º).'
)

with open('content/material/direito-constitucional/m08/a10-s01.md', 'w', encoding='utf-8') as f:
    f.write(text)

print('Patched successfully')
