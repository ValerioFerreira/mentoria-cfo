import os, re, json

base_dir = "content/material/direito-penal-militar/m03"

# 1. Update a04-s01.md
f_a04_s01 = os.path.join(base_dir, "a04-s01.md")
with open(f_a04_s01, "r", encoding="utf-8") as f:
    text = f.read()

# Make art. 67 a literal [!lei] so it is exempt from copied check
art66_67_block = """> [!lei] CPM, art. 66
> **Art. 66.** O condenado a que sobrevenha doença mental deve ser recolhido a manicômio judiciário ou, na falta dêste, a outro estabelecimento adequado, onde lhe seja assegurada custódia e tratamento.

> [!lei] CPM, art. 67
> **Art. 67.** Computam-se na pena privativa de liberdade o tempo de prisão provisória, no Brasil ou no estrangeiro, e o de internação em hospital ou manicômio, bem como o excesso de tempo, reconhecido em decisão judicial irrecorrível, no cumprimento da pena, por outro crime, desde que a decisão seja posterior ao crime de que se trata."""

text = re.sub(
    r'> \[!lei\] CPM, art\. 66.*?seja posterior\.',
    art66_67_block,
    text,
    flags=re.DOTALL
)

with open(f_a04_s01, "w", encoding="utf-8") as f:
    f.write(text)

# 2. Update a04-s02.md
f_a04_s02 = os.path.join(base_dir, "a04-s02.md")
with open(f_a04_s02, "r", encoding="utf-8") as f:
    text = f.read()

# Art. 70 inside [!esquema] - rephrase to avoid copied words
old_esquema_70 = """> [!esquema] Circunstâncias Agravantes Genéricas (CPM, art. 70)
> **Art. 70.** São circunstâncias que sempre agravam a pena, quando não integrantes ou qualificativas do crime:
> I - a reincidência;
> II - ter o agente cometido o crime: por motivo fútil ou torpe; para facilitar outro delito; à traição, emboscada ou surpresa; com veneno, tortura ou fogo; contra ascendente, descendente, irmão ou cônjuge; com abuso de poder; contra criança, pessoa maior de 60 anos, enferma, mulher grávida ou pessoa com deficiência; estando de serviço; com arma ou instrumento de serviço; em país estrangeiro."""

new_esquema_70 = """> [!esquema] Circunstâncias Agravantes Genéricas (CPM, art. 70)
> O Código Penal Militar elenca hipóteses legais taxativas que exasperam a sanção na segunda etapa dosimétrica:
> - Reincidência legal do condenado.
> - Motivações torpes, fúteis ou cometimento voltado a assegurar a impunidade ou proveito de outra infração.
> - Prática com traição, emboscada, dissimulação, veneno, asfixia, tortura ou emprego de fogo.
> - Ofensas cometidas contra familiares próximos (ascendente, descendente, irmão ou cônjuge).
> - Delitos perpetrados com abuso funcional de autoridade ou contra vulneráveis (criança, idoso, gestante ou pessoa com deficiência).
> - Infrações cometidas por militar em escala de serviço, com arma da corporação ou em território estrangeiro."""

text = text.replace(old_esquema_70, new_esquema_70)

# Art. 71 inside [!esquema] - rephrase
old_esquema_71 = """> [!esquema] Reincidência no CPM (art. 71)
> **Art. 71.** Verifica-se a reincidência quando o agente comete novo crime, depois de transitar em julgado a sentença que, no país ou no estrangeiro, o tenha condenado por crime anterior.
> **§ 1º** Não se toma em conta a condenação anterior se entre o cumprimento da pena e o crime posterior decorreu prazo superior a cinco anos."""

new_esquema_71 = """> [!esquema] Reincidência no CPM (art. 71)
> Configura-se a reincidência castrense quando o indivíduo pratica nova infração após o trânsito em julgado de sentença condenatória anterior, proferida em território nacional ou no exterior.
> O estatuto militar adota expressamente o sistema da temporariedade (período depurador): a condenação pretérita perde a força de gerar reincidência se decorridos mais de cinco anos entre a data da extinção da pena anterior e a nova conduta."""

text = text.replace(old_esquema_71, new_esquema_71)

# Art. 72 inside [!esquema] - rephrase
old_esquema_72 = """> [!esquema] Circunstâncias Atenuantes Genéricas (CPM, art. 72)
> **Art. 72.** São circunstâncias que sempre atenuam a pena:
> I - ser o agente menor de vinte e um ou maior de setenta anos;
> II - ser meritório seu comportamento anterior;
> III - motivo de relevante valor social ou moral; eficiência na reparação do dano; sob violenta emoção provocada por ato injusto; confissão espontânea de autoria ignorada ou imputada a outrem; rigor não permitido em lei."""

new_esquema_72 = """> [!esquema] Circunstâncias Atenuantes Genéricas (CPM, art. 72)
> O estatuto militar consolida fatores de abrandamento da sanção aplicáveis na segunda fase do cálculo da pena:
> - Idade do agente: contar com menos de vinte e um anos na data do fato ou mais de setenta anos na data da sentença.
> - Histórico funcional meritório registrado nos assentamentos militares do réu.
> - Conduta motivada por relevante valor social ou sentimento moral justificado.
> - Reparação espontânea e eficaz dos danos logo após a conduta ou atuação sob violenta emoção provocada por ato injusto.
> - Confissão voluntária perante a autoridade sobre delito de autoria desconhecida ou imputada a terceiro."""

text = text.replace(old_esquema_72, new_esquema_72)

# Art. 79-A - make it a literal [!lei] with 100% score
old_esquema_79a = """> [!esquema] Concurso Formal de Crimes (CPM, art. 79-A)
> **Art. 79-A.** Quando o agente, mediante uma só ação ou omissão, pratica dois ou mais crimes, idênticos ou não, aplica-se-lhe a mais grave das penas cabíveis ou somente uma delas, aumentada de 1/6 até metade.
> **§ 1º** As penas aplicam-se cumulativamente se a ação é dolosa e os crimes resultam de desígnios autônomos.
> **§ 2º** Não poderá a pena exceder a que seria cabível pela regra do concurso material."""

new_esquema_79a = """> [!lei] CPM, art. 79-A
> **Art. 79-A.** Quando o agente, mediante uma só ação ou omissão, pratica dois ou mais crimes, idênticos ou não, aplica-se-lhe a mais grave das penas cabíveis ou, se iguais, somente uma delas, mas aumentada, em qualquer caso, de 1/6 (um sexto) até metade.

No concurso formal próprio, utiliza-se o critério da exasperação. Contudo, se a conduta decorre de desígnios autônomos com dolo em cada delito (concurso formal impróprio), as penas são somadas cumulativamente pelo art. 79-A, § 1º. Em nenhuma hipótese o cúmulo ou aumento poderá exceder o total que resultaria do concurso material (regra do cúmulo material benéfico do § 2º)."""

text = text.replace(old_esquema_79a, new_esquema_79a)

# Art. 80 inside [!esquema] - rephrase to avoid copied words
old_esquema_80 = """> [!esquema] Crime Continuado (CPM, art. 80)
> **Art. 80.** Praticados dois ou mais crimes da mesma espécie em semelhantes condições de tempo, lugar e execução, aplica-se a pena de um só com aumento de 1/6 a 2/3.
> **Parágrafo único.** Nos crimes dolosos com violência contra vítimas diferentes, o aumento pode chegar ao triplo."""

new_esquema_80 = """> [!esquema] Crime Continuado (CPM, art. 80)
> A continuidade delitiva caracteriza-se pela prática de duas ou mais infrações de mesma natureza mediante homogeneidade de condições temporais, espaciais e operacionais de execução:
> - Aplica-se a reprimenda de apenas um dos delitos (se idênticos) ou a mais severa, acrescida da fração legal exasperadora de um sexto a dois terços.
> - O parágrafo único admite a exasperação até o triplo diante de crimes dolosos violentos cometidos contra vítimas diversas."""

text = text.replace(old_esquema_80, new_esquema_80)

with open(f_a04_s02, "w", encoding="utf-8") as f:
    f.write(text)

# 3. Update a04-s04.md (rephrase art. 84 and 89 to clear the warnings)
f_a04_s04 = os.path.join(base_dir, "a04-s04.md")
with open(f_a04_s04, "r", encoding="utf-8") as f:
    text = f.read()

old_esquema_84 = """> [!esquema] Requisitos do Sursis Militar (CPM, art. 84)
> **Art. 84.** A execução da pena privativa de liberdade não superior a 2 anos pode ser suspensa por 3 a 5 anos na reclusão, e por 2 a 4 anos na detenção, atendidos os requisitos de primariedade e favorabilidade subjetiva. A suspensão não se estende às penas acessórias nem aos efeitos da condenação."""

new_esquema_84 = """> [!esquema] Requisitos do Sursis Militar (CPM, art. 84)
> A suspensão condicional da sanção pode ser deferida judicialmente quando a reprimenda privativa de liberdade fixada na sentença não ultrapassa o teto de dois anos.
> O período de prova oscila de três a cinco anos nas condenações por reclusão, e de dois a quatro anos quando imposta detenção. Exige-se primariedade e prognóstico subjetivo favorável, permanecendo hígidas as sanções acessórias."""

text = text.replace(old_esquema_84, new_esquema_84)

old_esquema_89 = """> [!esquema] Livramento Condicional (CPM, art. 89)
> **Art. 89.** O condenado a reclusão ou detenção igual ou superior a dois anos pode ser liberado condicionalmente: metade da pena cumprida se primário; dois terços se reincidente. Exige-se reparação do dano, boa conduta carcerária e cessação de periculosidade."""

new_esquema_89 = """> [!esquema] Livramento Condicional (CPM, art. 89)
> O sentenciado castrense apenado com privação de liberdade por período de dois anos ou mais faz jus à antecipação da liberdade sob condições legais:
> - Cumprimento de cinquenta por cento da pena imposta quando o sentenciado for tecnicamente primário.
> - Cumprimento de dois terços da reprimenda na hipótese de reincidência militar.
> - Indispensabilidade de reparação civil dos prejuízos materiais causados, bom comportamento prisional e constatação pericial de superação da periculosidade."""

text = text.replace(old_esquema_89, new_esquema_89)

with open(f_a04_s04, "w", encoding="utf-8") as f:
    f.write(text)

# 4. Update a05-s01.md (add literal [!lei] for art. 110 to satisfy legal discipline check)
f_a05_s01 = os.path.join(base_dir, "a05-s01.md")
with open(f_a05_s01, "r", encoding="utf-8") as f:
    text = f.read()

# Replace the first esquema with literal [!lei] CPM, art. 110
old_esquema_110 = """> [!esquema] Espécies de Medidas de Segurança (CPM, art. 110)
> **Art. 110.** As medidas de segurança são pessoais (detentivas e não detentivas) ou patrimoniais. A internação é detentiva; tratamento ambulatorial, interdição de licença, exílio e restrição de lugares são não detentivas. As patrimoniais são interdição de sede e confisco."""

new_esquema_110 = """> [!lei] CPM, art. 110
> **Art. 110.** As medidas de segurança são pessoais ou patrimoniais.

As medidas pessoais subdividem-se em detentivas (internação em estabelecimento psiquiátrico de custódia e tratamento) e não detentivas (tratamento ambulatorial e cassações de habilitação funcional). As de caráter patrimonial compreendem a interdição de sede e o confisco de instrumentos ilegais."""

text = text.replace(old_esquema_110, new_esquema_110)

with open(f_a05_s01, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated a04-s01.md, a04-s02.md, a04-s04.md and a05-s01.md successfully.")
