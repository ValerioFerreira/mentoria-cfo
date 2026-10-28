# -*- coding: utf-8 -*-
"""Part 2 for a05: s05, s06, s07, s08 (Roubo, Latrocínio, Extorsão e Dano - rigorously paraphrased)."""

def get_part2_data(get_fp):
    items = []
    summaries = []

    # -------------------------------------------------------------
    # SEGMENT 05: Crimes de Roubo: Próprio, Impróprio e Majorado (p. 39-53)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a05/s05",
        "bizu": {
            "summary": [
                "**Roubo Próprio (art. 157, caput)**: subtração violenta mediante agressão física, grave ameaça ou recurso que reduza a capacidade de resistência da vítima.",
                "**Redução da Capacidade de Resistência**: abrange substâncias químicas anestésicas, narcóticos ou soníferos aplicados sem consentimento (boa-noite Cinderela).",
                "**Roubo Impróprio (art. 157, § 1º)**: a violência ou ameaça é perpetrada logo após a subtração para garantir a impunidade do crime ou a detenção definitiva da coisa.",
                "**Inadmissibilidade de Tentativa no Roubo Impróprio**: a doutrina clássica repele o conatus; ou o autor emprega a violência consumando o roubo, ou responde por furto.",
                "**Majorantes de Um Terço até Metade (§ 2º)**: concurso de duas ou mais pessoas, transporte de valores, veículo para outro Estado, retenção da vítima e arma branca.",
                "**Majorante por Arma de Fogo (§ 2º-A, I)**: aumento de dois terços se a violência ou grave ameaça for exercida com emprego de arma de fogo comum.",
                "**Rompimento de Obstáculo com Explosivo (§ 2º-A, II)**: aumento de dois terços na hipótese de arrombamento de obstáculo executado com substância explosiva.",
                "**Armamento de Uso Restrito ou Proibido (§ 2º-B)**: aplicação da pena em dobro caso o roubo seja perpetrado com emprego de armas restritas ou proibidas.",
                "**Arma Branca (Lei 13.964/2019)**: o Pacote Anticrime reintroduziu o emprego de arma branca (facas, punhais) como majorante de um terço até a metade no inciso VII do § 2º."
            ],
            "teoria": [
                {
                    "statement": "O roubo impróprio aperfeiçoa-se quando a violência física é desferida pelo agente momentos antes de iniciar a execução da subtração material.",
                    "isTrue": False,
                    "explanation": "No roubo impróprio (§ 1º), a violência ou ameaça é empregada logo após a subtração clandestina, visando assegurar a posse ou impunidade."
                },
                {
                    "statement": "A utilização de arma de fogo de uso restrito na prática do crime de roubo acarreta a aplicação da sanção reclusiva calculada em dobro.",
                    "isTrue": True,
                    "explanation": "O art. 157, § 2º-B, introduzido pelo Pacote Anticrime, impõe a aplicação da pena em dobro para o roubo com arma de fogo restrita ou proibida."
                },
                {
                    "statement": "A administração fraudulenta de substância entorpecente em bebida para adormecer a vítima e despojá-la de bens tipifica furto qualificado por fraude.",
                    "isTrue": False,
                    "explanation": "A dopagem com sonífero anula a capacidade reativa da vítima, amoldando-se ao roubo próprio pelo recurso que reduz a resistência (art. 157, caput)."
                },
                {
                    "statement": "O emprego de arma branca como facas de cozinha configura causa especial de aumento de um terço até metade no crime de roubo.",
                    "isTrue": True,
                    "explanation": "O art. 157, § 2º, VII, reinserido pela Lei 13.964/2019, estabelece majoração de um terço até a metade pelo emprego de arma branca."
                }
            ],
            "revisao": [
                {
                    "statement": "A restrição momentânea da liberdade da vítima mantida sob o poder dos infratores atrai majorante no crime de roubo circunstanciado.",
                    "isTrue": True,
                    "explanation": "O art. 157, § 2º, V, prevê causa de aumento fracionária quando os infratores privam momentaneamente a vítima de sua livre locomoção."
                },
                {
                    "statement": "A apreensão da arma de fogo e a elaboração de laudo de eficiência pericial são pressupostos obrigatórios para a incidência da majorante do roubo.",
                    "isTrue": False,
                    "explanation": "O STF e STJ dispensam a apreensão e perícia da arma de fogo se sua utilização for cabalmente atestada por prova testemunhal segura."
                },
                {
                    "statement": "O roubo praticado mediante concurso de agentes permite a cumulação simultânea da majorante com o apenamento em dobro por arma restrita.",
                    "isTrue": True,
                    "explanation": "As majorantes de incisos distintos e frações autônomas do art. 157 podem ser cumuladas pelo magistrado na dosimetria penal devidamente motivada."
                },
                {
                    "statement": "O uso de arma de brinquedo ou simulacro desprovido de potencial lesivo autoriza a aplicação da majorante de arma de fogo no roubo.",
                    "isTrue": False,
                    "explanation": "A Súmula 174 do STJ foi cancelada; o simulacro serve apenas para caracterizar a grave ameaça típica do caput, vedada qualquer majoração."
                }
            ],
            "pointers": [
                {"topic": "Roubo próprio, núcleos de coerção e redução da resistência", "pageRef": 40},
                {"topic": "Roubo impróprio e discussão sobre consumação e conatus", "pageRef": 43},
                {"topic": "Causas de aumento do parágrafo 2º e regime das armas brancas", "pageRef": 47},
                {"topic": "Majorantes de armas de fogo e aplicação da sanção em dobro", "pageRef": 50},
                {"topic": "Dispensa de apreensão de arma e jurisprudência vinculante", "pageRef": 52}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a05/s05",
        "fingerprint": get_fp("direito-penal/a05/s05"),
        "analytic": """Este segmento esmiúça o crime de roubo nas modalidades própria e imprópria e examina a gradação das causas de aumento de pena reformuladas pelas Leis nº 13.654/2018 e nº 13.964/2019.

### Roubo próprio e meios executórios (artigo 157, caput)
O artigo 157, caput, do Código Penal comina pena básica de reclusão de quatro a dez anos e multa à conduta de arrebatar patrimônio móvel pertencente a terceiro utilizando-se de:
1. *Violência Física (vis corporalis)*: agressão material direcionada contra a higidez biológica da vítima (socos, empurrões, imobilização traumática);
2. *Grave Ameaça (vis compulsiva)*: promessa intimidatória idônea de mal futuro, plausível e iminente apta a paralisar o ânimo defensivo do ofendido;
3. *Recurso que Reduz a Resistência*: qualquer ardil que anule a capacidade mecânica de reação ou defesa física, destacando-se a dopagem alcoólica involuntária ou ministração de fármacos sedativos (clássico golpe do "boa-noite Cinderela").

### Roubo impróprio e momento da violência (parágrafo 1º)
O parágrafo 1º tipifica o **Roubo Impróprio**, apenado com a idêntica reprimenda da forma simples. Difere do roubo próprio quanto à cronologia e finalidade dos atos coativos:
- O agente inicia a conduta mediante subtração pacífica e clandestina da coisa (como se furto fosse);
- **Logo após apoderar-se do bem**, emprega violência física ou grave ameaça contra a vítima ou terceiros perseguidores;
- *Finalidade Específica*: a coerção posterior visa assegurar a posse pacífica da res furtiva ou assegurar a impunidade do crime. A doutrina majoritária assenta que o roubo impróprio não admite a figura da tentativa: ou o agente emprega a violência consumando o delito complexo, ou, caso não consiga agredir, responde unicamente por furto tentado em concurso com eventual ameaça.

### Sistema trifásico de causas de aumento de pena
A legislação penal estabelece três patamares escalonados de majoração:
- **Majorantes de Um Terço até a Metade (§ 2º)**:
  - *Inciso II*: concurso de duas ou mais pessoas;
  - *Inciso III*: vítima em serviço de transporte de valores e o agente conhece essa condição;
  - *Inciso IV*: subtração de veículo automotor transportado para outro Estado ou exterior;
  - *Inciso V*: privação momentânea da liberdade da vítima mantida sob o jugo dos infratores;
  - *Inciso VII*: emprego ostensivo de **arma branca** (faca, canivete, punhal), reinserido pela Lei nº 13.964/2019.
- **Majorantes de Dois Terços (§ 2º-A)**:
  - *Inciso I*: emprego de **arma de fogo comum** de uso permitido;
  - *Inciso II*: destruição ou rompimento de obstáculo mediante uso de substâncias explosivas;
- **Aplicação da Pena em Dobro (§ 2º-B)**:
  - Quando a violência ou grave ameaça for exercida mediante o emprego de **arma de fogo de uso restrito ou proibido** (fuzis, metralhadoras, pistolas com numeração raspada).

Por derradeiro, o STF e o STJ pacificaram o entendimento de que a **apreensão e perícia da arma de fogo são dispensáveis** para a incidência da majorante, desde que o manejo do armamento reste comprovado por depoimentos testemunhais idôneos ou imagens de câmeras de segurança.

### Para fixar
- O roubo próprio exige violência, grave ameaça ou recurso que impossibilite a defesa da vítima.
- A dopagem involuntária com sonífero para subtrair bens amolda-se ao roubo próprio no art. 157.
- O roubo impróprio ocorre quando a violência é empregada logo após a subtração patrimonial.
- O roubo impróprio não admite tentativa perante a doutrina tradicional majoritária.
- O concurso de pessoas e a restrição de liberdade da vítima elevam a pena de um terço até metade.
- O emprego de arma de fogo comum acarreta causa de aumento autônoma de dois terços no § 2º-A.
- A arma de fogo de uso restrito ou proibido enseja a aplicação da reprimenda penal em dobro.
- É dispensável a apreensão e perícia da arma quando seu uso for comprovado por testemunhas.""",
        "synthetic": [
            "**Roubo Próprio (art. 157)**: subtração patrimonial coativa perpetrada com intimidação moral grave, agressão corporal ou anulação química da resistência.",
            "**Roubo Impróprio (§ 1º)**: emprego superveniente de violência após a subtração visando garantir a impunidade do autor ou a posse da coisa subtraída.",
            "**Inadmissibilidade de Tentativa**: no roubo impróprio a violência posterior consuma o crime ou o fato desclassifica-se para delito de furto.",
            "**Majorantes de 1/3 a 1/2**: incidem perante comparsaria, retenção da vítima no cativeiro, transporte de valores e porte ostensivo de arma branca.",
            "**Arma de Fogo Comum**: exaspera a sanção em dois terços demandando potencialidade lesiva objetiva demonstrável na instrução probatória.",
            "**Pena em Dobro (§ 2º-B)**: sanciona gravemente o emprego de armamentos privativos, restritos ou com identificação adulterada na ação delituosa.",
            "**Explosivo no Roubo**: eleva a reprimenda em dois terços quando utilizado para estilhaçar barreiras mecânicas protetivas da res.",
            "**Prescindibilidade Pericial**: a prova testemunhal convergente supre a não localização da arma para fins de aplicação da causa de aumento."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 06: Roubo Qualificado pelo Resultado e Latrocínio (p. 54-67)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a05/s06",
        "bizu": {
            "summary": [
                "**Roubo Qualificado por Lesão Grave (art. 157, § 3º, I)**: reclusão de sete a dezoito anos e multa se da violência empregada resulta lesão de natureza grave ou gravíssima.",
                "**Latrocínio (art. 157, § 3º, II)**: roubo qualificado pela morte da vítima cominada com pena severa de reclusão de vinte a trinta anos e multa.",
                "**Crime Complexo Patrimonial**: o latrocínio tutela primariamente o patrimônio e secundariamente a vida; trata-se de delito contra o patrimônio e não crime doloso contra a vida.",
                "**Competência de Julgamento (Súmula 603 STF)**: a competência para julgar o latrocínio é do juiz criminal singular togado e não do Tribunal do Júri.",
                "**Súmula 610 do STF**: confirma a consumação do latrocínio no caso de óbito verificado, ainda que a espoliação patrimonial permaneça na esfera tentada.",
                "**Tentativa de Latrocínio**: configura-se quando o agente atua com dolo de matar mas o evento letal não se consuma por circunstâncias alheias à sua vontade.",
                "**Hediondez Legal**: o latrocínio e o roubo com restrição de liberdade qualificam-se como crimes hediondos na sistemática da Lei nº 8.072/1990.",
                "**Pluralidade de Vítimas com Uma Morte**: a morte de uma única pessoa em contexto de espoliação de patrimônios múltiplos configura crime único de latrocínio na jurisprudência.",
                "**Súmula 582 do STJ**: o roubo atinge a consumação no instante da inversão detentiva, dispensando posse pacífica mesmo diante de imediata perseguição policial."
            ],
            "teoria": [
                {
                    "statement": "O julgamento do crime de latrocínio consumado submete-se à competência constitucional soberana do Tribunal do Júri Popular.",
                    "isTrue": False,
                    "explanation": "A Súmula 603 do STF estabelece que a competência para o processo e julgamento por latrocínio é do juiz singular, visto tratar-se de crime patrimonial."
                },
                {
                    "statement": "Nos moldes da Súmula 610 do STF, o crime de latrocínio resta consumado quando o evento morte ocorre, ainda que a subtração patrimonial reste frustrada.",
                    "isTrue": True,
                    "explanation": "A Súmula 610 do STF consagra que há crime de latrocínio consumado quando o homicídio se consuma, ainda que o agente não logre subtrair os bens."
                },
                {
                    "statement": "A produção culposa de lesão corporal de feição leve decorrente da violência no roubo qualifica a infração nas balizas do parágrafo terceiro.",
                    "isTrue": False,
                    "explanation": "O art. 157, § 3º, I, restringe a qualificação exclusivamente a lesões de natureza grave ou gravíssima; a lesão leve integra a violência elementar."
                },
                {
                    "statement": "A inversão momentânea da posse da res furtiva seguida de imediata perseguição policial basta para a consumação material do delito de roubo.",
                    "isTrue": True,
                    "explanation": "A Súmula 582 do STJ assenta que o roubo consuma-se com a inversão da posse, sendo prescindível a posse mansa, pacífica ou desvigiada."
                }
            ],
            "revisao": [
                {
                    "statement": "Se o infrator pretendia subtrair bens de três passageiros no coletivo e mata um deles na ação, responde por três crimes de latrocínio consumados em concurso formal.",
                    "isTrue": False,
                    "explanation": "O STF e STJ entendem que a causação de uma só morte na ação patrimonial enseja latrocínio único, exasperando-se a pena pelo concurso patrimonial."
                },
                {
                    "statement": "O delito de latrocínio ostenta natureza de crime hediondo segundo expressa previsão contida na Lei dos Crimes Hediondos.",
                    "isTrue": True,
                    "explanation": "O latrocínio figura expressamente no rol dos crimes hediondos da Lei nº 8.072/1990 em suas formas tentada e consumada."
                },
                {
                    "statement": "A ocorrência de morte resultante de caso fortuito durante a execução de roubo afasta a tipificação do delito preterdoloso de latrocínio.",
                    "isTrue": True,
                    "explanation": "O direito penal repele a responsabilidade objetiva; exige-se dolo ou no mínimo culpa na causação do evento fatal para configurar latrocínio."
                },
                {
                    "statement": "O roubo consuma-se unicamente quando o agente consegue transportar os bens até local seguro fora do alcance visual da vítima despojada.",
                    "isTrue": False,
                    "explanation": "A Súmula 582 do STJ adota a teoria da amotio: a saída do campo visual ou posse desvigiada é inteiramente prescindível para a consumação."
                }
            ],
            "pointers": [
                {"topic": "Roubo qualificado por lesão corporal grave no art. 157, § 3º, I", "pageRef": 55},
                {"topic": "Latrocínio, natureza patrimonial e competência do juízo singular", "pageRef": 58},
                {"topic": "Súmula 610 do STF e combinações de tentativa e consumação", "pageRef": 62},
                {"topic": "Súmula 582 do STJ e teoria da amotio no crime de roubo", "pageRef": 65},
                {"topic": "Hediondez do latrocínio e regras de concurso formal", "pageRef": 67}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a05/s06",
        "fingerprint": get_fp("direito-penal/a05/s06"),
        "analytic": """Este segmento aprofunda as modalidades qualificadas pelo resultado do crime de roubo previstas no artigo 157, § 3º, do Código Penal, analisando os contornos da lesão corporal grave, a dogmática do latrocínio, a competência jurisdicional togado e as diretrizes das Súmulas 582 do STJ e 610 do STF.

### Roubo qualificado por lesão grave e latrocínio
O parágrafo 3º do artigo 157 disciplina o roubo qualificado pelo resultado decorrente da violência física:
- **Lesão Corporal Grave ou Gravíssima (inciso I)**: sanção reclusiva severa de **sete a dezoito anos e multa**. Abrange qualquer lesão enquadrável nos parágrafos 1º e 2º do artigo 129. Se da violência derivarem lesões leves, estas restam absorvidas pela própria tipicidade da forma simples ou majorada;
- **Latrocínio (inciso II)**: comina sanção punitiva gravíssima de **reclusão de vinte a trinta anos e multa** se da violência derivar a morte da vítima ou de terceiro interveniente. Trata-se de autêntico crime complexo patrimonial (fusão de roubo com homicídio), em que a morte pode derivar de dolo direto, dolo eventual ou culpa estrita (*crime preterdoloso*).

### Competência e a Súmula 603 do STF
Em face de sua topografia dogmática de crime contra o patrimônio tutelado, o legislador constituinte não incluiu o latrocínio no rol dos crimes dolosos contra a vida. Consectariamente, a **Súmula 603 do Supremo Tribunal Federal** cristalizou a diretriz de que a competência para o processo e julgamento por latrocínio pertence ao juiz togado singular da vara criminal comum e não ao corpo de jurados do tribunal popular.

### A Súmula 610 do STF e a combinatória de conatus
A jurisprudência sumulada do pretório excelso fixou baliza lapidar na **Súmula 610 do STF**: consuma-se a infração complexa no exato instante em que a morte da vítima sobrevém, revelando-se irrelevante a frustração do desapossamento dos pertences materiais pretendidos.
As combinações práticas desdobram-se nos seguintes cenários:
1. *Morte Consumada e Subtração Consumada*: latrocínio plenamente consumado;
2. *Morte Consumada e Subtração Tentada*: **latrocínio consumado** (aplicação vinculante da Súmula 610 do STF, visto que o bem jurídico vida, mais relevante, pereceu);
3. *Morte Tentada e Subtração Tentada*: latrocínio na modalidade tentada;
4. *Morte Tentada e Subtração Consumada*: a orientação majoritária dos tribunais superiores reconhece **tentativa de latrocínio**, aplicando a causa de diminuição do conatus sobre as penas do § 3º, II.

### Momento consumativo e a Súmula 582 do STJ
A consolidação definitiva do marco consumativo do roubo foi proclamada na **Súmula 582 do STJ**: assenta que o delito patrimonial complexo aperfeiçoa-se no instante da inversão detentiva da coisa móvel subtraída com emprego de coação, reputando-se dispensável posse mansa, tranquila ou desvigiada e mesmo que sobrevenha imediata perseguição pelas forças de segurança.
A teoria da apreensão (*amotio*) orienta que o delito atinge a perfeição formal no segundo exato em que a res passa ao poder do agressor após a coação, rechaçando a tese desclassificatória de tentativa.

### Para fixar
- A lesão grave qualifica o roubo com pena de sete a dezoito anos no art. 157, § 3º, I.
- O latrocínio ocorre quando a violência resulta morte, apenado com reclusão de vinte a trinta anos.
- O latrocínio tutela primariamente o patrimônio, sendo processado pelo juiz singular e não pelo Júri.
- Pela Súmula 610 do STF, se o homicídio se consuma, há latrocínio consumado mesmo sem subtração.
- A morte tentada combinada com subtração patrimonial consumada tipifica tentativa de latrocínio.
- O latrocínio ostenta natureza hedionda integral nos moldes da Lei nº 8.072/1990.
- A causação de um só óbito com despojo de patrimônios plurais configura latrocínio único na jurisprudência.
- A Súmula 582 do STJ exige apenas a inversão da posse para a consumação do roubo.""",
        "synthetic": [
            "**Lesão Grave no Roubo (§ 3º, I)**: exasperação cominada com reclusão de sete a dezoito anos quando a violência física infligir dano anatômico qualificado.",
            "**Latrocínio (§ 3º, II)**: roubo qualificado pelo resultado letal doloso ou culposo apenado com a reprimenda severa de vinte a trinta anos de reclusão.",
            "**Competência do Juiz Singular**: a Súmula 603 do STF afasta o julgamento popular do Júri ante a prevalência da índole patrimonial da infração.",
            "**Súmula 610 do STF**: consolida a consumação típica do latrocínio no evento morte ainda que o objetivo patrimonial não seja concretizado.",
            "**Tentativa de Latrocínio**: perfaz-se juridicamente quando a intenção homicida falha por fatores externos, independentemente do sucesso na subtração.",
            "**Hediondez Legal**: o latrocínio e o roubo com privação de liberdade compõem o catálogo de crimes hediondos inafiançáveis e insuscetíveis de graça.",
            "**Pluralidade Patrimonial com Morte**: óbito único na cena criminosa tipifica latrocínio singular com exasperação da pena pelo concurso de espoliações.",
            "**Súmula 582 do STJ**: inversão da detenção da coisa basta à consumação, prescindindo de intervalo temporal de sossego ou posse desvigiada."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 07: Extorsão e Extorsão mediante Sequestro (p. 68-78)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a05/s07",
        "bizu": {
            "summary": [
                "**Extorsão Comum (art. 158)**: intimidação coativa violenta forçando a vítima a emitir declaração ou adotar comportamento ativo patrimonialmente desvantajoso.",
                "**Súmula 96 do STJ**: a consumação típica do delito de extorsão prescinde do alcance efetivo do locupletamento patrimonial almejado pelo agente.",
                "**Diferenciação Roubo versus Extorsão**: no roubo a atuação da vítima é prescindível (o agente subtrai a coisa); na extorsão a colaboração da vítima é indispensável (ela entrega ou digita).",
                "**Extorsão Qualificada por Restrição de Liberdade (art. 158, § 3º)**: vulgarmente denominada sequestro-relâmpago, comina reclusão de seis a doze anos e multa.",
                "**Finalidade do Sequestro-Relâmpago**: restrição temporária da vítima exigida como condição necessária para obtenção da vantagem (saques bancários em caixas).",
                "**Extorsão Mediante Sequestro (art. 159)**: enclausuramento da vítima com imposição de contrapartida financeira ou preço para a devolução de sua liberdade.",
                "**Consumação do Art. 159**: crime formal e permanente que se consuma no exato instante da privação da liberdade, sendo prescindível o recebimento do resgate financeiro.",
                "**Qualificadoras da Extorsão Mediante Sequestro**: reclusão de doze a vinte anos se durar mais de 24 horas, se o sequestrado for menor de 18 ou maior de 60, ou bando/quadrilha.",
                "**Delação Premiada (art. 159, § 4º)**: se o crime for cometido em concurso, o concorrente que denunciar o fato facilitando a libertação terá a pena reduzida de um a dois terços.",
                "**Hediondez da Extorsão**: a extorsão qualificada pela morte e a extorsão mediante sequestro integram o rol dos crimes hediondos da Lei nº 8.072/1990."
            ],
            "teoria": [
                {
                    "statement": "O crime de extorsão comum subordina sua consumação ao efetivo locupletamento e recebimento da vantagem econômica indevida pelo agente.",
                    "isTrue": False,
                    "explanation": "A Súmula 96 do STJ estabelece que a extorsão consuma-se com o constrangimento coativo, sendo a vantagem mero exaurimento do delito formal."
                },
                {
                    "statement": "A conduta consistente em obrigar a vítima sob mira de revólver a fornecer senhas de aplicativos bancários amolda-se à figura da extorsão.",
                    "isTrue": True,
                    "explanation": "A exigência de comportamento ativo da vítima (digitar ou fornecer dados sigilosos essenciais) consubstancia crime de extorsão."
                },
                {
                    "statement": "O crime de extorsão mediante sequestro admite redução de pena em favor do coautor que denunciar o bando viabilizando a libertação do refém.",
                    "isTrue": True,
                    "explanation": "O art. 159, § 4º, contempla expressa delação premiada legal com atenuação sancionatória de um a dois terços em favor do delator eficaz."
                },
                {
                    "statement": "O sequestro relâmpago qualificado pela morte acarreta a pronúncia e o julgamento popular perante o plenário do Tribunal do Júri.",
                    "isTrue": False,
                    "explanation": "A extorsão qualificada pela morte (art. 158, § 3º) é crime patrimonial de julgamento privativo do juiz togado singular."
                }
            ],
            "revisao": [
                {
                    "statement": "A retenção física da vítima em cativeiro por mais de 24 horas constitui qualificadora do crime de extorsão mediante sequestro.",
                    "isTrue": True,
                    "explanation": "O art. 159, § 1º, prevê reclusão de doze a vinte anos se o sequestro da vítima ultrapassar o intervalo temporal de 24 horas."
                },
                {
                    "statement": "Diferentemente do roubo, a conduta no crime de extorsão caracteriza-se pela dispensabilidade absoluta da cooperação física do ofendido.",
                    "isTrue": False,
                    "explanation": "É exatamente o oposto: na extorsão a cooperação da vítima é indispensável; no roubo o bem pode ser simplesmente arrebatado sem qualquer cooperação."
                },
                {
                    "statement": "O delito de extorsão mediante sequestro consuma-se unicamente quando os familiares da vítima pagam o montante exigido a título de resgate.",
                    "isTrue": False,
                    "explanation": "Trata-se de crime formal e permanente que atinge a consumação no exato instante da privação da liberdade ambulatorial do sequestrado."
                },
                {
                    "statement": "A extorsão mediante sequestro qualificada por lesão corporal grave ou morte ostenta feição hedionda legalmente inafiançável.",
                    "isTrue": True,
                    "explanation": "O art. 159 em todas as suas modalidades figura expressamente no artigo 1º da Lei nº 8.072/1990 como delito hediondo."
                }
            ],
            "pointers": [
                {"topic": "Extorsão comum, elementos constitutivos e Súmula 96 do STJ", "pageRef": 69},
                {"topic": "Critérios de diferenciação dogmática entre roubo e extorsão", "pageRef": 71},
                {"topic": "Extorsão qualificada pela restrição da liberdade e sequestro-relâmpago", "pageRef": 73},
                {"topic": "Extorsão mediante sequestro, natureza formal e permanência delitiva", "pageRef": 75},
                {"topic": "Qualificadoras temporais e delação premiada no art. 159, § 4º", "pageRef": 77}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a05/s07",
        "fingerprint": get_fp("direito-penal/a05/s07"),
        "analytic": """Este segmento disseca os tipos incriminadores de extorsão contemplados no Código Penal: a extorsão comum disciplinada no artigo 158, o sequestro-relâmpago e a extorsão mediante sequestro estatuída no artigo 159.

### Extorsão comum e momento consumativo (artigo 158)
O artigo 158 comina reclusão de quatro a dez anos e multa a quem constrange outrem com emprego de violência corporal ou intimidação grave almejando ganho patrimonial indevido mediante conduta imposta à própria vítima.

A dinâmica dogmática da extorsão corporifica-se em um **crime formal (ou de consumação antecipada)**. Consoante o teor da **Súmula 96 do Superior Tribunal de Justiça**: a extorsão consuma-se no instante da coação, prescindindo do auferimento material do lucro almejado.
A infração atinge a consumação perfeita no instante em que a coação é exercida e a vítima é forçada a agir ou tolerar a conduta, situando-se o recebimento posterior do proveito econômico como mero exaurimento punível.

### A distinção nodal entre roubo e extorsão
O divisor de águas entre o roubo e a extorsão reside na **essencialidade da cooperação da vítima**:
- *No Roubo*: a conduta cooperativa da vítima é prescindível e desnecessária. O autor apodera-se e subtrai a coisa móvel por suas próprias forças, com ou sem a concordância do ofendido (o assaltante arranca a carteira do bolso ou bolsa à força);
- *Na Extorsão*: a colaboração da vítima é faticamente indispensável. Sem o comportamento ativo voluntário-coagido da pessoa espoliada, o autor não atinge a vantagem patrimonial visada (a vítima é coagida a ditar a senha do cartão, assinar uma cártula de cheque ou realizar transferência biométrica).

### Sequestro-relâmpago (artigo 158, § 3º)
O parágrafo 3º disciplina a **extorsão qualificada pela restrição da liberdade da vítima**, vulgarmente conhecida como sequestro-relâmpago, punida com **reclusão de seis a doze anos e multa**:
- Caracteriza-se quando a privação temporária e efêmera da liberdade do ofendido consubstancia a condição indispensável para a obtenção da vantagem econômica visada pelos comparsas (ex.: obrigar a vítima a circular pela cidade dentro do automóvel para realizar sucessivos saques em terminais de autoatendimento);
- Se da violência resultar lesão corporal grave ou morte, aplicam-se as penas qualificadas do artigo 158, § 3º, parte final, submetidas ao crivo privativo do juiz togado singular.

### Extorsão mediante sequestro (artigo 159)
O artigo 159 incrimina a privação de liberdade individual executada sob a exigência condicionante de pagamento pecuniário para liberação do cativeiro, cominando severa pena básica de **reclusão de oito a quinze anos**. Cuida-se de crime formal e complexo que conjuga a privação de liberdade pessoal à espoliação patrimonial:
- Consuma-se no instante exato da privação da liberdade ambulatorial do sequestrado, ostentando caráter permanente enquanto perdurar o confinamento no cativeiro;
- *Qualificadoras*: a sanção eleva-se para doze a vinte anos se a privação durar mais de 24 horas, se o sequestrado for menor de 18 ou maior de 60 anos, ou se perpetrado por quadrilha/bando; salta para dezesseis a vinte e quatro anos por lesão grave e vinte e quatro a trinta anos em caso de morte preterdolosa;
- *Delação Premiada (§ 4º)*: prevê decote fracionário de um a dois terços em favor do comparsa que denunciar o crime à autoridade policial viabilizando a libertação eficaz do refém sadio e salvo.

### Para fixar
- A extorsão é crime formal consumado com a coação sem exigir o recebimento da vantagem indevida.
- A Súmula 96 do STJ pacifica que a obtenção da vantagem constitui mero exaurimento da extorsão.
- No roubo o auxílio da vítima é prescindível; na extorsão seu ato de cooperação é indispensável.
- O sequestro-relâmpago qualifica a extorsão no art. 158, § 3º, com reclusão de seis a doze anos.
- A extorsão mediante sequestro exige resgate e consuma-se com a simples privação de liberdade.
- O sequestro com cativeiro superior a 24 horas qualifica a infração com pena de doze a vinte anos.
- A delação premiada no art. 159, § 4º, atenua a sanção de um a dois terços pela libertação do refém.
- O art. 159 consubstancia crime hediondo em todas as suas figuras típicas na Lei 8.072/1990.""",
        "synthetic": [
            "**Extorsão Comum (art. 158)**: coação moral ou violenta cominando reclusão para obrigar o ofendido a comportamento ativo patrimonial desfavorável.",
            "**Súmula 96 do STJ**: consagra a extorsão como crime formal aperfeiçoado no constrangimento, independentemente da efetiva percepção financeira.",
            "**Diferenciação Prática**: no roubo a coisa é arrebatada unilateralmente; na extorsão a entrega patrimonial subordina-se à atuação forçada do lesado.",
            "**Sequestro-Relâmpago (§ 3º)**: restrição momentânea da liberdade individual utilizada como mecanismo instrumental direto para viabilizar saques bancários.",
            "**Extorsão Mediante Sequestro (art. 159)**: encarceramento com exigência financeira de resgate consumando-se de plano com a privação da locomoção.",
            "**Qualificadora Temporal**: exaspera o sancionamento para doze a vinte anos quando a manutenção da clausura sobrepujar vinte e quatro horas.",
            "**Delação Premiada Legal (§ 4º)**: autoriza diminuição punitiva na fração de um a dois terços ao corréu que propiciar a libertação do sequestrado.",
            "**Hediondez Rígida**: a extorsão mediante sequestro integra o rol de infrações inafiançáveis desprovidas de indulto previstas na Lei nº 8.072/1990."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 08: Da usurpação e dano (p. 79-89)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a05/s08",
        "bizu": {
            "summary": [
                "**Usurpação de Limites (art. 161, caput)**: alterar ou suprimir marcos divisórios para apropriar-se de imóvel alheio no todo ou em parte.",
                "**Esbulho Possessório (art. 161, § 1º, II)**: invasão violenta ou coletiva por três ou mais comparsas para apossar-se de propriedade fundiária alheia.",
                "**Crime de Dano Simples (art. 163, caput)**: destruir, inutilizar ou deteriorar coisa alheia, cominada com detenção de um a seis meses ou multa.",
                "**Dolo Específico no Dano**: exige o animus nocendi (vontade livre e consciente de causar prejuízo patrimonial ao dono); a forma culposa é penalmente atípica.",
                "**Dano Qualificado por Violência (parágrafo único, I)**: detenção de seis meses a três anos quando executado com agressão física ou grave ameaça à pessoa.",
                "**Dano com Explosivo ou Inflamável (inciso II)**: qualifica-se pelo emprego de fogo ou explosivos, se o fato não constituir crime mais grave.",
                "**Dano ao Patrimônio Público (inciso III)**: praticado contra bens da União, Estado, DF, Municípios, autarquias, fundações ou concessionárias de serviços públicos.",
                "**Fuga de Preso e Dano à Cela (Jurisprudência STJ)**: a danificação de grade de cela pelo detento com escopo exclusivo de fuga não tipifica dano qualificado por falta de animus nocendi.",
                "**Dano por Motivo Egoístico (inciso IV)**: qualificado se praticado por motivo egoístico ou com prejuízo financeiro considerável para o ofendido."
            ],
            "teoria": [
                {
                    "statement": "O crime de dano praticado na modalidade culposa acarreta a incidência de reprimenda mitigada de detenção na legislação penal pátria.",
                    "isTrue": False,
                    "explanation": "O Código Penal não contempla a figura culposa para o crime de dano; a deterioração negligente de bem alheio resolve-se na esfera civil."
                },
                {
                    "statement": "O dano praticado contra instalações de empresa pública federal atrai a incidência de qualificadora específica com sanção de detenção e multa.",
                    "isTrue": True,
                    "explanation": "O art. 163, parágrafo único, III, comina forma qualificada pelo cometimento de dano contra o patrimônio da União, autarquia ou empresa pública."
                },
                {
                    "statement": "A jurisprudência do STJ assenta que o preso que quebra as grades da cela exclusivamente para empreender fuga consuma dano qualificado estatal.",
                    "isTrue": False,
                    "explanation": "O STJ firmou que a fuga do preso sem intuito específico de lesar o erário afasta o animus nocendi, restando atípica a conduta perante o art. 163."
                },
                {
                    "statement": "O esbulho possessório praticado mediante a invasão pacífica e desarmada por apenas duas pessoas consubstancia crime de ação penal privada.",
                    "isTrue": False,
                    "explanation": "O art. 161, § 1º, II, exige violência, ameaça ou concurso de mais de duas pessoas (no mínimo três); invasão pacífica por dois agentes é atípica penalmente."
                }
            ],
            "revisao": [
                {
                    "statement": "A prática de crime de dano executado com o emprego de substância explosiva consubstancia circunstância qualificadora expressa do tipo penal.",
                    "isTrue": True,
                    "explanation": "O art. 163, parágrafo único, II, qualifica expressamente o dano cometido com emprego de substância inflamável ou explosiva."
                },
                {
                    "statement": "A ação penal no crime de dano simples praticado contra particular processa-se ordinariamente mediante ação pública incondicionada.",
                    "isTrue": False,
                    "explanation": "Pelo art. 167 do Código Penal, o dano simples (art. 163, caput) e o dano por motivo egoístico processam-se exclusivamente mediante queixa (ação privada)."
                },
                {
                    "statement": "A danificação deliberada de bem móvel público motivada por ato de puro vandalismo e depredação carcerária configura dano qualificado ao erário.",
                    "isTrue": True,
                    "explanation": "Havendo dolo deliberado de destruir bens públicos (vandalismo desvinculado de fuga), incide o dano qualificado do art. 163, parágrafo único, III."
                },
                {
                    "statement": "O esbulho possessório sem emprego de violência física à pessoa processa-se mediante queixa privativa do titular esbulhado.",
                    "isTrue": True,
                    "explanation": "O art. 161, § 3º, determina que se o crime de esbulho for praticado sem violência à pessoa, a ação penal somente se procede mediante queixa."
                }
            ],
            "pointers": [
                {"topic": "Alteração de limites e esbulho possessório no art. 161", "pageRef": 80},
                {"topic": "Crime de dano, núcleos de ação e exigência de animus nocendi", "pageRef": 83},
                {"topic": "Qualificadoras do crime de dano e patrimônio estatal público", "pageRef": 86},
                {"topic": "Entendimento do STJ sobre fuga de presídios e dano a celas", "pageRef": 88},
                {"topic": "Regimes de ação penal no crime de dano e usurpação", "pageRef": 89}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a05/s08",
        "fingerprint": get_fp("direito-penal/a05/s08"),
        "analytic": """Este segmento examina os crimes contra o patrimônio imobiliário e a integridade material das coisas: os delitos de usurpação de limites e esbulho possessório disciplinados no artigo 161, e as modalidades simples e qualificadas do crime de dano reguladas no artigo 163.

### Usurpação de limites e esbulho possessório
O artigo 161 tutela a posse e propriedade imobiliária:
- *Alteração de Limites (caput)*: suprimir ou deslocar tapume, marco ou qualquer sinal indicativo da linha divisória para assenhorear-se de imóvel vizinho;
- *Usurpação de Águas (§ 1º, I)*: desviar ou represar águas alheias em benefício próprio ou de outrem;
- *Esbulho Possessório (§ 1º, II)*: invadir, com emprego de violência física, grave ameaça ou mediante o concurso de **mais de duas pessoas** (no mínimo três invasores simultâneos), terreno ou edifício alheio para fins de esbulho da posse. Se a invasão decorrer de disputa cível sem violência e praticada por apenas dois agentes, o fato desborda da esfera penal punitiva.

A ação penal no esbulho sem violência física à pessoa rege-se de forma estritamente privada mediante **queixa-crime** (§ 3º).

### Crime de dano e o elemento subjetivo do tipo (artigo 163)
O artigo 163, caput, criminaliza a conduta de **destruir, inutilizar ou deteriorar coisa alheia móvel ou imóvel**, cominando pena mitigada de detenção de um a seis meses ou multa:
- *Destruir*: fazer desaparecer ou demolir materialmente o objeto;
- *Inutilizar*: retirar a aptidão funcional e utilidade prática da coisa sem destruí-la fisicamente;
- *Deteriorar*: provocar estrago, desvalorização ou comprometimento anatômico parcial do bem;
- *Animus Nocendi*: a configuração típica do crime de dano exige imperativamente o dolo específico de infligir prejuízo patrimonial direto ao titular da coisa. **O ordenamento penal brasileiro não contempla a modalidade culposa no crime de dano**, solvendo-se a avaria negligente na esfera civil da reparação de danos materiais.

### Dano qualificado e depredação de patrimônio estatal
O parágrafo único eleva a pena para detenção de seis meses a três anos e multa quando o delito é perpetrado:
1. Com emprego de violência à pessoa ou mediante grave ameaça (inciso I);
2. Com utilização de substância explosiva ou inflamável (inciso II);
3. Contra o **patrimônio público** da União, Estado, Município, Distrito Federal, empresa pública, autarquia, fundação ou sociedade concessionária prestadora de serviços públicos (inciso III);
4. Por motivo egoístico ou com prejuízo econômico considerável para a vítima (inciso IV).

### Fuga de presídios e orientação do Superior Tribunal de Justiça
A jurisprudência assentada da Sexta e Quinta Turmas do Superior Tribunal de Justiça firmou a diretriz de que **o preso que serra grades, esburaca paredes ou destrói o teto da cela de estabelecimento prisional exclusivamente com o propósito de empreender fuga não comete o crime de dano qualificado ao patrimônio público**:
- Ausente o animus nocendi (a intenção exclusiva e premeditada de lesar financeiramente o Estado), o ato material integra o instinto natural de restauração da liberdade ambulatória individual, operando-se a atipicidade penal do art. 163, parágrafo único, III;
- Todavia, caso os presidiários promovam rebelião carcerária com incêndio ou depredação gratuita de colchões, bebedouros e câmeras de segurança sem vínculo com evasão direta, resta configurado o dano qualificado doloso ao patrimônio público.

### Para fixar
- O esbulho possessório exige violência, grave ameaça ou concurso de mais de duas pessoas no art. 161.
- O crime de dano tutela a substância material da coisa exigindo animus nocendi comprovado nos autos.
- A modalidade culposa do crime de dano é fato atípico no direito penal positivo brasileiro.
- O dano qualificado contra o patrimônio público alcança bens de estatais e concessionárias de serviço.
- O preso que danifica a grade da cela exclusivamente para fugir não responde por dano qualificado.
- Atos de depredação gratuita e vandalismo de bens públicos na penitenciária tipificam o art. 163, III.
- O dano com emprego de inflamável ou explosivo qualifica a conduta com detenção de 6 meses a 3 anos.
- A ação penal do dano simples é privada, processando-se privativamente mediante queixa-crime.""",
        "synthetic": [
            "**Usurpação de Limites (art. 161)**: deslocamento fraudulento de marcos divisórios territoriais para expansão indevida de confrontações imobiliárias.",
            "**Esbulho Possessório**: apossamento forçado de imóveis mediante coação violenta ou concurso mínimo qualificado de três participantes simultâneos.",
            "**Dano Material (art. 163)**: ação dolosa de deteriorar ou inutilizar bens alheios cominando detenção na modalidade comissiva simples.",
            "**Animus Nocendi Indispensável**: reclama comprovação cabal do intuito específico de depreciar o patrimônio da vítima, sendo a culpa atípica.",
            "**Dano Qualificado Público**: exaspera o sancionamento contra atos de vandalismo infligidos contra bens de autarquias, estatais e concessionárias estatais.",
            "**Dano e Fuga de Presos**: o STJ reconhece a atipicidade da destruição mecânica da cela se direcionada exclusivamente ao resgate da liberdade física.",
            "**Vandalismo no Cárcere**: a quebra imotivada de bens estatais em motins prisionais sem finalidade de fuga imediata caracteriza dano qualificado doloso.",
            "**Regime Processual de Queixa**: o dano simples sujeita-se à iniciativa privativa da vítima mediante propositura tempestiva de queixa-crime."
        ]
    })

    return items, summaries
