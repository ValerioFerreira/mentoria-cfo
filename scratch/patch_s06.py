with open('content/material/direito-penal-militar/m05/a09-s06.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update edital
text = text.replace('edital: ["geral:9.4"]', 'edital: ["geral:9.5"]')

# 2. Fix jurisprudence title
text = text.replace(
    '> [!jurisprudencia] Jurisprudência consolidada sobre Latrocínio nos Tribunais Superiores',
    '> [!jurisprudencia] STF, Súmula 610: Latrocínio Consumado e Jurisprudência dos Tribunais Superiores'
)

# 3. Fix copied phrase in 6º-A
old_6a = 'estabelece reclusão de três a dez anos para quem subtrai arma, munição, explosivo ou outro material de uso restrito militar ou que contenha sinal indicativo de pertencer a instituição militar. Trata-se de qualificadora especialíssima que visa a coibir a transferência de material bélico oficial para organizações criminosas.'
new_6a = 'comina pena de três a dez anos de reclusão quando o objeto material da subtração envolver armamento bélico, munições, artefatos explosivos ou equipamentos de destinação privativa das instituições armadas ou ostentando brasão oficial. Trata-se de qualificadora especialíssima que visa a coibir a transferência de armamentos e munições das Forças Armadas para organizações criminosas.'
text = text.replace(old_6a, new_6a)

# 4. Remove jargon consubstanci
text = text.replace('consubstancia o roubo qualificado', 'configura o roubo qualificado')
text = text.replace('consubstancia mero exaurimento', 'constitui mero exaurimento')

# 5. Develop Extorsao section
old_extorsao = '''## Extorsão militar (art. 243)

O art. 243 do CPM tipifica o crime de extorsão: constranger alguém, mediante violência ou grave ameaça, com o intuito de obter para si ou para outrem indevida vantagem econômica, a fazer, tolerar que se faça ou deixar de fazer algo. A pena básica é de reclusão de quatro a dez anos. A extorsão é crime formal (Súmula 96 do STJ), consumando-se no momento da prática da coação moral ou física, independentemente da efetiva obtenção da vantagem pecuniária pretendida.

O § 1º determina a aplicação subsidiária das causas de aumento de pena do roubo (art. 242, § 2º), exasperando a reprimenda quando a extorsão for praticada com emprego de arma, concurso de agentes ou restrição temporária de liberdade.'''

new_extorsao = '''## Extorsão militar (art. 243)

O art. 243 do Código Penal Militar tipifica o delito de extorsão nos seguintes termos: constranger alguém, mediante o emprego de violência real física ou grave ameaça moral, com o intuito deliberado de obter para si ou para terceiro indevida vantagem econômica, a fazer, tolerar que se faça ou abster-se de fazer algo juridicamente não imposto. A pena cominada no preceito fundamental é de reclusão de quatro a dez anos.

A extorsão militar ostenta natureza de crime formal e de consumação antecipada. Em consonância com a Súmula 96 do Superior Tribunal de Justiça, o delito perfaz-se de forma completa no momento exato em que a vítima suporta a coação psicológica ou física idônea, sendo desnecessária para a consumação a efetiva obtenção do proveito patrimonial ilícito visado pelo agente (que representa mero exaurimento da conduta).

O § 1º do art. 243 determina a incidência das causas especiais de aumento previstas para o roubo (art. 242, § 2º). Dessa maneira, a resposta penal sofre majoração compulsória de um terço até a metade quando o delito é perpetrado com emprego de armas brancas ou de fogo, mediante concurso de duas ou mais pessoas, contra vítima em escala de serviço militar, ou com restrição da liberdade pessoal da vítima para compelir a entrega de recursos financeiros.'''

text = text.replace(old_extorsao, new_extorsao)

# 6. Develop Hediondez section
old_hediondez = '''## Hediondez militar nos crimes contra o patrimônio

Com a inclusão do inciso VI no parágrafo único do art. 1º da Lei nº 8.072/1990 pela Lei nº 14.688/2023, o rol dos crimes hediondos militares é regido pelo princípio da identidade material. São hediondos no âmbito militar:
1. O latrocínio militar tipificado no art. 242, § 3º, do CPM;
2. O roubo circunstanciado pelo resultado morte culposa (art. 242, § 2º, VI);
3. A extorsão qualificada pela morte (art. 243 c/c art. 242, § 3º);
4. A extorsão mediante sequestro militar (art. 244 do CPM).'''

new_hediondez = '''## Hediondez militar nos crimes contra o patrimônio

A Lei nº 14.688/2023 pacificou controvérsia histórica a respeito da aplicabilidade da Lei nº 8.072/1990 (Lei dos Crimes Hediondos) no âmbito da Justiça Militar. A reforma inseriu o inciso VI no parágrafo único do art. 1º daquele diploma, estabelecendo que ostentam natureza de crime hediondo militar todas as figuras delituosas previstas no Código Penal Militar que apresentem correspondência material e identidade descritiva com os delitos hediondos da legislação comum.

Sob esse postulado da identidade normativa estrita, revestem-se de hediondez patrimonial militar:
1. **Latrocínio militar (art. 242, § 3º):** roubo com resultado morte dolosa, independentemente de haver a consumação do desfalque patrimonial;
2. **Roubo qualificado pelo resultado morte culposa (art. 242, § 2º, VI):** figura preterdolosa com evento letal;
3. **Extorsão qualificada pela morte (art. 243 c/c art. 242, § 3º):** coação econômica com desfecho letal consumado;
4. **Extorsão mediante sequestro no ambiente militar (art. 244 do CPM):** privação da liberdade com exigência de resgate financeiro.

A categorização hedionda acarreta reflexos gravosos na execução penal militar, tais como vedação de anistia, graça e indulto, além de exigir prazos mais rigorosos e cumprimento de frações diferenciadas para a concessão de livramento condicional e progressão de regime prisional.'''

text = text.replace(old_hediondez, new_hediondez)

with open('content/material/direito-penal-militar/m05/a09-s06.md', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated a09-s06.md successfully')
