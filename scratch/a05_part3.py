# -*- coding: utf-8 -*-
"""Part 3 for a05: s09, s10, s11 (Apropriação Indébita e Estelionato - rigorously paraphrased)."""

def get_part3_data(get_fp):
    items = []
    summaries = []

    # -------------------------------------------------------------
    # SEGMENT 09: Apropriação Indébita Geral e Previdenciária (p. 90-104)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a05/s09",
        "bizu": {
            "summary": [
                "**Apropriação Indébita Comum (art. 168)**: assenhoreamento ilícito de bem móvel cuja posse ou detenção anterior foi transferida de boa-fé pelo proprietário.",
                "**Inversão do Animus**: o crime consuma-se no momento em que o autor inverte a posse legítima anterior, passando a agir como se dono fosse (animus domini).",
                "**Majorantes da Apropriação Indébita (§ 1º)**: sanção aumentada de um terço se o bem foi confiado em depósito necessário, tutela/curatela ou ofício/profissão.",
                "**Apropriação Indébita Previdenciária (art. 168-A)**: omissão intencional do repasse tempestivo aos cofres previdenciários dos tributos descontados dos trabalhadores.",
                "**Crime Omissivo Próprio**: o art. 168-A consuma-se instantaneamente com a omissão do repasse aos cofres públicos, prescindindo de animus rem sibi habendi.",
                "**Extinção da Punibilidade por Pagamento**: o adimplemento integral do débito tributário previdenciário a qualquer tempo extingue a punibilidade estatal.",
                "**Efeitos do Parcelamento Previdenciário**: a inclusão do débito em parcelamento fiscal formal suspende a pretensão punitiva e o prazo prescricional.",
                "**Perdão Judicial Previdenciário (§ 3º)**: faculdade do julgador de não aplicar pena ao réu primário de bons antecedentes que recolher o tributo antes da denúncia ou valor irrisório.",
                "**Dificuldades Financeiras da Empresa**: a insolvência notória e risco de encerramento da atividade econômica podem configurar inexigibilidade de conduta diversa em tese."
            ],
            "teoria": [
                {
                    "statement": "No crime de apropriação indébita previdenciária, a tipificação delitiva exige a demonstração cabal de que o administrador apropriou-se pessoalmente dos valores retidos.",
                    "isTrue": False,
                    "explanation": "O STJ consolidou que o art. 168-A é crime omissivo puro de perigo abstrato, prescindindo da apropriação ou desvio pessoal das quantias descontadas."
                },
                {
                    "statement": "O pagamento integral das contribuições previdenciárias devidas aos cofres públicos realizado antes do recebimento da denúncia extingue a punibilidade.",
                    "isTrue": True,
                    "explanation": "Pela legislação extravagante tributária e jurisprudência vinculante do STF e STJ, a quitação integral do tributo a qualquer tempo extingue a punibilidade."
                },
                {
                    "statement": "Na apropriação indébita comum do art. 168, o agente emprega artifícios e fraudes antecedentes para induzir a vítima em erro e obter a posse da coisa.",
                    "isTrue": False,
                    "explanation": "A posse na apropriação indébita é transmitida de forma justa e voluntária; a fraude antecedente para conseguir o bem tipifica estelionato."
                },
                {
                    "statement": "A apropriação indébita praticada por advogado em detrimento de valores recebidos em alvará judicial atrai a causa de aumento de um terço por ofício ou profissão.",
                    "isTrue": True,
                    "explanation": "O art. 168, § 1º, III, prevê expressamente o aumento de um terço na pena corporal quando a apropriação é perpetrada em razão de ofício ou profissão."
                }
            ],
            "revisao": [
                {
                    "statement": "O acolhimento formal de pedido de parcelamento tributário dos débitos previdenciários suspende o curso da prescrição penal da pretensão punitiva.",
                    "isTrue": True,
                    "explanation": "O parcelamento previdenciário deferido acarreta a imediata suspensão da prescrição penal e da pretensão persecutória do Ministério Público."
                },
                {
                    "statement": "A apropriação indébita previdenciária admite a modalidade culposa quando o empresário esquece de enviar a guia de recolhimento bancário no vencimento.",
                    "isTrue": False,
                    "explanation": "O art. 168-A é delito estritamente doloso; o esquecimento culposo consubstancia infração administrativa fiscal sem tipicidade penal."
                },
                {
                    "statement": "A configuração da apropriação indébita comum consuma-se com o primeiro ato explícito de disposição ou negativa de restituição do bem pelo detentor.",
                    "isTrue": True,
                    "explanation": "O crime consuma-se com a exteriorização do animus domini, manifestada pela recusa formal de devolução ou alienação indevida da coisa."
                },
                {
                    "statement": "O perdão judicial previsto no artigo 168-A do Código Penal é de concessão compulsória ao réu que ostenta condenações criminais anteriores transitadas em julgado.",
                    "isTrue": False,
                    "explanation": "O benefício do § 3º é faculdade judicial e exige categoricamente que o agente seja primário e ostente bons antecedentes formais."
                }
            ],
            "pointers": [
                {"topic": "Apropriação indébita comum, animus domini e distinção do estelionato", "pageRef": 91},
                {"topic": "Causas de aumento de um terço no art. 168, § 1º", "pageRef": 94},
                {"topic": "Apropriação indébita previdenciária e natureza omissiva própria", "pageRef": 98},
                {"topic": "Extinção da punibilidade por pagamento e efeitos do parcelamento", "pageRef": 101},
                {"topic": "Perdão judicial previdenciário e inexigibilidade de conduta diversa", "pageRef": 104}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a05/s09",
        "fingerprint": get_fp("direito-penal/a05/s09"),
        "analytic": """Este segmento aprofunda a dogmática da apropriação indébita tradicional discriminada no artigo 168 do Código Penal e a figura tributária especializada da apropriação indébita previdenciária positivada no artigo 168-A.

### Apropriação indébita comum (artigo 168)
O artigo 168 criminaliza a ação de assenhorear-se indevidamente de patrimônio móvel sobre o qual já exercia prévia custódia legítima, cominando sanção de reclusão de um a quatro anos e multa. Trata-se de infração que pressupõe uma sequência cronológica tripartite:
1. *Posse ou Detenção Lícita Originária*: o agente recebe a coisa móvel legitimamente das mãos do proprietário, sem qualquer ardil, fraude ou coação física;
2. *Quebra da Fidelidade*: o autor retém o bem e opera em sua mente a inversão do título da posse (*inversio animi*);
3. *Consumação pelo Animus Domini*: o delito atinge a consumação no instante em que o infrator exterioriza a vontade definitiva de comportar-se como dono proprietário da res (alienando, locando, consumindo ou negando peremptoriamente a devolução do bem ao legítimo titular).

A diferenciação dogmática perante figuras afins é precisa: no **furto**, a coisa é arrebatada clandestinamente; no **estelionato**, a posse é entregue mediante engano antecedente; na **apropriação indébita**, a posse inicial é justa e a fraude é superveniente.

O parágrafo 1º estatui causas de aumento de **um terço** se o bem foi entregue em depósito necessário; sob o encargo de tutor, curador, testamenteiro ou inventariante judicial; ou em decorrência de profissão, ofício ou ministério funcional (ex.: advogado que se apropria de verbas rescisórias recebidas em nome do cliente).

### Apropriação indébita previdenciária (artigo 168-A)
O artigo 168-A pune a omissão do empresário que deixa de recolher aos cofres públicos previdenciários as parcelas tributárias descontadas dos pagamentos dos trabalhadores no prazo regulamentar, cominando reclusão de dois a cinco anos e multa:
- *Natureza Jurídica*: cuida-se de **crime omissivo próprio (puro) e formal**. O Superior Tribunal de Justiça firmou a tese repetitiva de que a consumação independe da demonstração do dolo específico de locupletamento (*animus rem sibi habendi*), bastando a abstenção voluntária de transferir os valores descontados do contracheque dos obreiros dentro do prazo administrativo;
- *Extinção da Punibilidade por Pagamento*: o parágrafo 2º prevê a extinção da punibilidade se o agente pagar antes do início da ação fiscal. Não obstante, por força da legislação penal tributária (Leis nº 9.249/1995, nº 10.684/2003 e nº 12.382/2011) e da orientação vinculante das Cortes Superiores, a quitação completa e integral do débito tributário a qualquer tempo, mesmo após o advento de sentença condenatória definitiva, opera a extinção irrevogável da punibilidade estatal;
- *Parcelamento Previdenciário*: o deferimento do parcelamento do débito antes ou durante o processo acarreta a **suspensão da pretensão punitiva e do curso da prescrição penal** enquanto vigorar o pagamento das cotas mensais acordadas com a Fazenda Pública;
- *Dificuldades Financeiras Corporativas*: a jurisprudência admite excepcionalmente a tese de inexigibilidade de conduta diversa caso reste fartamente documentada a absoluta insolvência patrimonial da empresa com perigo de bancarrota iminente, justificando a opção emergencial de pagamento de salários dos empregados em detrimento do recolhimento tributário.

### Para fixar
- A apropriação indébita exige posse inicial lícita seguida de inversão do ânimo para assenhoreamento.
- A apropriação é majorada de um terço quando cometida em razão de ofício, emprego ou profissão.
- A apropriação indébita previdenciária é crime omissivo puro de perigo formal e abstrato.
- Não se exige prova de apropriação pecuniária pessoal para consumação do art. 168-A.
- A quitação integral do débito tributário previdenciário extingue a punibilidade a qualquer tempo.
- O parcelamento deferido do débito previdenciário suspende a persecução penal e o prazo de prescrição.
- O perdão judicial no art. 168-A exige primariedade do infrator e quitação antes da denúncia ou valor irrisório.
- A grave crise de insolvência financeira da pessoa jurídica pode legitimar a excludente de culpabilidade.""",
        "synthetic": [
            "**Apropriação Indébita (art. 168)**: apossamento ilegítimo de bem móvel previamente recebido sob posse justa desprovida de coação inicial originária.",
            "**Consumação pelo Animus Domini**: concretiza-se no momento exato em que o detentor age com desígnio definitivo de senhorio sobre o patrimônio alheio.",
            "**Majorante Profissional**: exaspera a penalidade em um terço quando o desvio patrimonial decorrer da quebra de ofício, ministério ou dever fiduciário.",
            "**Retenção Previdenciária (art. 168-A)**: crime formal e omissivo próprio consubstanciado no não recolhimento tempestivo de tributos retidos da folha obreira.",
            "**Prescindibilidade de Desvio Pessoal**: o STJ dispensa a comprovação de apropriação pecuniária particular para a conformação típica do delito previdenciário.",
            "**Extinção por Adimplemento**: a satisfação integral das contribuições devidas aos cofres públicos extingue formalmente a pretensão punitiva penal.",
            "**Efeitos do Parcelamento**: a inclusão do débito previdenciário em programa de refinanciamento suspende a pretensão punitiva e o fluxo prescricional.",
            "**Dificuldades Financeiras Corporativas**: a crise de liquidez insuperável pode afastar a culpabilidade sob a tese de inexigibilidade de conduta diversa."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 10: Estelionato e Fraude Eletrônica (p. 105-112)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a05/s10",
        "bizu": {
            "summary": [
                "**Estelionato Comum (art. 171, caput)**: obtenção de lucro patrimonial ilegítimo em detrimento de prejuízo de outrem induzindo o ofendido em erro mediante manobras fraudulentas.",
                "**Quatro Elementos Cumulativos**: obtenção de vantagem ilícita, causação de prejuízo financeiro a outrem, emprego de meio fraudulento e induzimento/manutenção da vítima em erro.",
                "**Fraude Eletrônica Cibernética (§ 2º-A)**: reclusão de quatro a oito anos se o estelionato for cometido com informações obtidas por redes sociais, e-mails falsos ou contatos telefônicos fraudulentos.",
                "**Majorante por Servidor no Exterior (§ 2º-B)**: sanção aumentada de um terço a dois terços caso a fraude cibernética seja operada com banco de dados situado fora do território nacional.",
                "**Golpes Contra Idosos e Vulneráveis (§ 4º)**: pena aumentada de um terço ao dobro se o crime de estelionato for praticado contra pessoa idosa ou vulnerável.",
                "**Reforma do Pacote Anticrime (§ 5º)**: o estelionato passou a processar-se mediante ação penal pública condicionada à representação do ofendido.",
                "**Exceções de Ação Incondicionada no Estelionato**: a ação permanece incondicionada se a vítima for a administração pública direta/indireta, criança/adolescente, pessoa com deficiência ou maior de 70 anos.",
                "**Idade no Artigo 171, § 5º, IV**: exige que a vítima seja maior de 70 anos para a ação pública incondicionada (distinto do conceito geral de idoso de 60 anos).",
                "**Retroatividade da Representação no STF**: a exigência de representação aplica-se retroativamente aos processos em curso sem denúncia oferecida ao tempo da vigência da Lei 13.964/2019."
            ],
            "teoria": [
                {
                    "statement": "O crime de estelionato consuma-se no momento exato em que o agente exterioriza a fraude ardilosa com aptidão de enganar a vítima visada.",
                    "isTrue": False,
                    "explanation": "Por ser crime material de resultado duplo, o estelionato consuma-se quando o autor aufere a vantagem ilícita em efetivo prejuízo patrimonial alheio."
                },
                {
                    "statement": "A prática de estelionato contra pessoa com sessenta e cinco anos de idade submete a deflagração da ação penal pública à indispensável representação do ofendido.",
                    "isTrue": True,
                    "explanation": "O art. 171, § 5º, IV, excepciona a ação pública incondicionada apenas para maior de 70 anos; aos 65 anos a ação permanece condicionada."
                },
                {
                    "statement": "O estelionato praticado mediante envio de links falsos em aplicativo de mensagens e clonagem de conta subsume-se à qualificadora de fraude eletrônica.",
                    "isTrue": True,
                    "explanation": "O art. 171, § 2º-A, tipifica expressamente a fraude eletrônica perpetrada mediante redes sociais, contatos telefônicos ou meios cibernéticos análogos."
                },
                {
                    "statement": "O estelionato praticado em prejuízo de empresa pública federal processa-se mediante representação expressa do procurador da estatal.",
                    "isTrue": False,
                    "explanation": "O art. 171, § 5º, I, determina que o estelionato praticado contra a administração pública direta ou indireta é de ação pública incondicionada."
                }
            ],
            "revisao": [
                {
                    "statement": "A utilização de servidor computacional mantido fora do território brasileiro acarreta causa especial de aumento da sanção na fraude eletrônica.",
                    "isTrue": True,
                    "explanation": "O art. 171, § 2º-B, estipula majoração de um terço a dois terços se a infração for perpetrada mediante servidor fora do território nacional."
                },
                {
                    "statement": "O prejuízo patrimonial suportado exclusivamente pelo autor da fraude é idôneo a caracterizar o delito material de estelionato consumado.",
                    "isTrue": False,
                    "explanation": "A descrição típica exige prejuízo alheio em correspondência causal direta com a obtenção de vantagem ilícita pelo infrator."
                },
                {
                    "statement": "O Pacote Anticrime estabeleceu que o estelionato contra vítima criança ou adolescente processa-se por meio de ação penal pública incondicionada.",
                    "isTrue": True,
                    "explanation": "O art. 171, § 5º, II, ressalva a natureza incondicionada da persecução penal pública caso o delito vitime criança ou adolescente."
                },
                {
                    "statement": "A fraude eletrônica tipificada no § 2º-A comina sanção atenuada de detenção inferior à cominada para a figura básica do estelionato.",
                    "isTrue": False,
                    "explanation": "A fraude eletrônica comina reclusão qualificada de quatro a oito anos e multa, sensivelmente mais severa que o caput (reclusão de 1 a 5 anos)."
                }
            ],
            "pointers": [
                {"topic": "Estelionato comum, requisitos estruturais e momento consumativo", "pageRef": 106},
                {"topic": "Fraude eletrônica no art. 171, § 2º-A e novidades da Lei 14.155/2021", "pageRef": 108},
                {"topic": "Majorantes para servidores no exterior e proteção a idosos", "pageRef": 110},
                {"topic": "Reforma do Pacote Anticrime e novo regime de representação da vítima", "pageRef": 111},
                {"topic": "Exceções do § 5º e interpretação jurisprudencial do critério etário", "pageRef": 112}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a05/s10",
        "fingerprint": get_fp("direito-penal/a05/s10"),
        "analytic": """Este segmento esmiúça o crime de estelionato regulado no artigo 171 do Código Penal, analisando os elementos constitutivos da figura fundamental, a qualificadora contemporânea da fraude eletrônica e o revolucionário regime de ação penal introduzido pela Lei nº 13.964/2019.

### Elementos constitutivos do estelionato fundamental (artigo 171, caput)
O artigo 171 criminaliza a obtenção fraudulenta de vantagem pecuniária espúria mediante ardil que induza o ofendido a erro gerando dano econômico, cominando reclusão de um a cinco anos e multa:
- *Artifício e Ardil*: artifício é a fraude material externa (documentos falsos, disfarces); ardil é a astúcia verbal oratória persuasiva;
- *Erro do Ofendido*: a vítima atua com sua percepção falseada da realidade, procedendo à entrega graciosa e voluntária do patrimônio acreditando na legitimidade da transação;
- *Consumação*: trata-se de **crime material de duplo resultado**. A consumação exige a concorrência concomitante e causal da produção de prejuízo financeiro efetivo para o ofendido e o ingresso da vantagem ilícita na esfera do estelionatário.

### Fraude eletrônica cibernética (parágrafos 2º-A e 2º-B)
Inserida pela Lei nº 14.155/2021 em resposta à proliferação de golpes virtuais, a **Fraude Eletrônica** comina pena qualificada de **reclusão de quatro a oito anos e multa**:
- Incide quando a artimanha fraudulenta é concretizada mediante o uso de dados e informações fornecidas pela vítima ou por terceiro induzido a erro através de redes sociais, plataformas cibernéticas, mensagens de aplicativos, e-mails fraudulentos (*phishing*) ou ligações telefônicas ardilosas;
- *Majorante de Servidor no Exterior (§ 2º-B)*: a reprimenda aumenta-se de **um terço a dois terços** caso o golpe opere com servidores de processamento hospedados fora do Brasil;
- *Vítima Idosa ou Vulnerável (§ 4º)*: prevê aumento de **um terço ao dobro** caso o estelionato recaia sobre pessoa idosa ou em situação de vulnerabilidade mental.

### O novo regime de ação penal do estelionato (parágrafo 5º)
A Lei nº 13.964/2019 operou profunda transformação procedimental ao consagrar como regra geral que **o crime de estelionato somente se procede mediante representação do ofendido**:
- A representação atua como condição de procedibilidade que caduca no prazo decadencial estrito de seis meses a contar da descoberta da autoria delitiva;
- *Exceções Taxativas de Ação Penal Pública Incondicionada*: a representação é dispensada, agindo o Ministério Público de ofício, unicamente nas quatro hipóteses do § 5º:
  1. Quando a vítima for a Administração Pública direta ou indireta (autarquias, estatais, fundações públicas);
  2. Quando vitimar criança ou adolescente;
  3. Quando praticado em desfavor de pessoa com deficiência mental;
  4. Quando recair sobre pessoa **maior de 70 anos de idade** ou civilmente incapaz.

Cumpre registrar com rigor: para a ação penal pública incondicionada, o texto legal exige expressamente a idade de **70 anos**. A vítima idosa entre 60 e 69 anos ampara-se no Estatuto do Idoso para a causa de aumento (§ 4º), mas a ação penal em seu favor permanece condicionada à representação.

### Para fixar
- O estelionato pune a obtenção de vantagem ilícita induzindo a vítima em erro com reclusão de 1 a 5 anos.
- Trata-se de crime material consumado com a causação de prejuízo e obtenção simultânea de vantagem.
- A fraude eletrônica cibernética no art. 171, § 2º-A, comina reclusão de quatro a oito anos.
- O uso de servidores fora do país eleva a reprimenda da fraude eletrônica de um terço a dois terços.
- Com a Lei 13.964/2019 o estelionato passou a exigir representação da vítima como regra procedimental geral.
- A ação é pública incondicionada se o estelionato vitimar entes da administração pública ou incapazes.
- A exceção etária para ação incondicionada no estelionato exige pessoa maior de 70 anos e não 60 anos.
- A vítima criança ou adolescente torna a ação penal de estelionato estritamente pública incondicionada.""",
        "synthetic": [
            "**Estelionato Fundamental (art. 171)**: delito patrimonial ardiloso consumado com a causação de prejuízo concreto conjugado ao proveito indevido obtido.",
            "**Entrega Voluntária em Erro**: a vítima cede espontaneamente o bem enganada pela falsidade do ardil oratório ou simulação documental do agente.",
            "**Fraude Eletrônica (§ 2º-A)**: golpe cibernético propagado por contatos telefônicos ou plataformas virtuais apenado com quatro a oito anos de reclusão.",
            "**Servidor Estrangeiro**: exasperação fracionária de um terço a dois terços cominada quando a operação digital utiliza banco de dados internacional.",
            "**Regra Geral de Representação**: o Pacote Anticrime convolou o rito persecutório para ação penal pública subordinada à manifestação da vítima.",
            "**Exceção de 70 Anos**: a titularidade incondicionada em razão da faixa etária vigora estritamente a partir dos setenta anos de idade da vítima.",
            "**Entes Públicos e Menores**: mantém o rito incondicionado perante fraudes suportadas pelo erário governamental, crianças e adolescentes tutelados.",
            "**Aplicação Temporal**: a exigência formal de representação retroage aos feitos em andamento destituídos de denúncia criminal ofertada."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 11: Estelionato contra entidade pública e Súmulas (p. 113-122)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a05/s11",
        "bizu": {
            "summary": [
                "**Estelionato Majorado (art. 171, § 3º)**: sanção aumentada de um terço se o delito é praticado em detrimento de entidade de direito público ou assistência social.",
                "**Estelionato Previdenciário**: fraude perpetrada contra o INSS com vistas a implantar ou manter benefício previdenciário ou assistencial indevido.",
                "**Natureza Jurídica do Estelionato Previdenciário**: classificação doutrinária dual assentada na jurisprudência pacífica do STF e do STJ.",
                "**Segurado que Recebe as Prestações**: para o beneficiário que aufere os saques mensais fraudulentos, o crime é de natureza permanente, protraindo-se a consumação a cada saque.",
                "**Intermediário e Servidor Fraudadora**: para o terceiro intermediário ou servidor que concede a fraude, o crime é instantâneo de efeitos permanentes, iniciando-se a prescrição no primeiro ato.",
                "**Súmula 17 do STJ (Consunção de Falso)**: o delito de falsidade documental é absorvido pelo estelionato quando nele esgota integralmente sua potencialidade danosa.",
                "**Súmula 24 do STJ**: aplica-se a causa de aumento do art. 171, § 3º, ao estelionato em que figuram como vítimas os segurados da Previdência Social.",
                "**Súmula 73 do STJ**: a utilização de moeda grosseiramente falsificada configura crime de estelionato perante a Justiça Estadual, e não moeda falsa da competência federal."
            ],
            "teoria": [
                {
                    "statement": "Nos termos da Súmula 17 do STJ, o uso de documento público falso que exaure sua potencialidade lesiva exclusivamente no estelionato permanece punível em concurso formal.",
                    "isTrue": False,
                    "explanation": "A Súmula 17 do STJ aplica o princípio da consunção: o falso é absorvido pelo estelionato quando esgota nele sua potencialidade lesiva."
                },
                {
                    "statement": "O estelionato previdenciário praticado pelo próprio beneficiário que saca parcelas mensais ilícitas sucessivas ostenta natureza de crime permanente.",
                    "isTrue": True,
                    "explanation": "O STF e STJ firmaram que, em relação ao próprio beneficiário que recebe os pagamentos mensais, o delito é permanente, postergando o marco da prescrição."
                },
                {
                    "statement": "A falsificação grosseira de nota de cem reais incapaz de iludir o homem médio afasta a tipificação do estelionato tipificando moeda falsa federal.",
                    "isTrue": False,
                    "explanation": "A Súmula 73 do STJ dispõe que a falsificação grosseira descaracteriza a moeda falsa e amolda-se, em tese, ao estelionato perante a Justiça Estadual."
                },
                {
                    "statement": "O estelionato perpetrado em detrimento de instituto de economia popular atrai a causa de aumento de pena de um terço do parágrafo terceiro do art. 171.",
                    "isTrue": True,
                    "explanation": "O art. 171, § 3º, prevê aumento compulsório de um terço na pena cominada se o crime for cometido em detrimento de instituto de economia popular ou entidade pública."
                }
            ],
            "revisao": [
                {
                    "statement": "Para o despachante intermediário que fraudou os documentos cadastrais do INSS e recebeu pagamento único, o estelionato previdenciário é permanente.",
                    "isTrue": False,
                    "explanation": "Para o terceiro intermediário que não saca os benefícios, o crime é instantâneo de efeitos permanentes, iniciando-se a prescrição no primeiro pagamento."
                },
                {
                    "statement": "A fraude praticada contra segurado individual da Previdência Social viabiliza a incidência da majorante do parágrafo terceiro do artigo 171.",
                    "isTrue": True,
                    "explanation": "Conforme a Súmula 24 do STJ, aplica-se a majorante do § 3º ao estelionato em que figuram como vítimas os segurados da Previdência Social."
                },
                {
                    "statement": "O princípio da consunção impede a absorção do falsum pelo estelionato quando a certidão adulterada mantém potencial para o cometimento de outros delitos futuros.",
                    "isTrue": True,
                    "explanation": "A Súmula 17 do STJ exige que o falso exaura integralmente sua lesividade no estelionato; se mantiver potencial autônomo, responde em concurso."
                },
                {
                    "statement": "A competência para julgar o estelionato praticado com uso de moeda com falsificação grosseira fixa-se perante os juizados da Justiça Federal.",
                    "isTrue": False,
                    "explanation": "Pela Súmula 73 do STJ, a falsificação grosseira afasta a competência da Justiça Federal, fixando-se perante a Justiça Estadual comum."
                }
            ],
            "pointers": [
                {"topic": "Majorante do art. 171, § 3º e proteção a entidades públicas e de assistência", "pageRef": 114},
                {"topic": "Estelionato previdenciário e diferenciação de permanência entre réus", "pageRef": 117},
                {"topic": "Súmula 17 do STJ e absorção do falso pelo crime-fim de estelionato", "pageRef": 119},
                {"topic": "Súmulas 24 e 73 do STJ na jurisprudência penal patrimonial", "pageRef": 121}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a05/s11",
        "fingerprint": get_fp("direito-penal/a05/s11"),
        "analytic": """Este segmento aprofunda a qualificadora circunstanciada do estelionato contra entidades governamentais e comunitárias estipulada no artigo 171, § 3º, verticalizando o estudo dogmático do estelionato previdenciário e os enunciados sumulares consolidados pelo Superior Tribunal de Justiça.

### Estelionato contra entidade pública e assistência social (artigo 171, § 3º)
O parágrafo 3º estatui a exasperação da pena corporal em **um terço** quando o crime é perpetrado em prejuízo de:
- Entidade de direito público (União, Estados, Distrito Federal, Municípios, autarquias públicas);
- Instituto de economia popular (cooperativas habitacionais populares, consórcios comunitários);
- Entidades beneficentes de assistência social privada reconhecidas pelo poder estatal.

O fundamento da majoração reside na lesão difusa e coletiva suportada pelo patrimônio do Estado ou pela coletividade de cidadãos que dependem da assistência alimentar e social comunitária. A jurisprudência consolidada na **Súmula 24 do Superior Tribunal de Justiça** pacificou que:
*"Aplica-se ao crime de estelionato, em que figuram como vítimas os segurados da Previdência Social, a causa especial de aumento da pena prevista no art. 171, § 3º, do Código Penal"*.

### Dogmática e momento consumativo do estelionato previdenciário
O estelionato previdenciário (fraude arquitetada para deferimento de aposentadorias ou pensões fraudulentas perante o INSS) suscita marcante bifurcação na jurisprudência pacificada do STF e do STJ quanto à sua **natureza jurídica e termo inicial da prescrição da pretensão punitiva**:
1. **Em relação ao Beneficiário Titular que saca as prestações mensais**:
   - Classifica-se como **crime permanente**;
   - A consumação protrai-se continuadamente no tempo a cada saque bancário mensal indevidamente creditado;
   - O prazo de prescrição penal somente tem início no dia exato em que cessa a permanência criminosa (isto é, na data da suspensão administrativa definitiva do benefício);
2. **Em relação ao Intermediário, Despachante ou Servidor que viabilizou a fraude**:
   - Classifica-se como **crime instantâneo de efeitos permanentes**;
   - A atividade executiva do intermediário encerra-se com a inserção dos dados ou obtenção do primeiro pagamento;
   - O prazo prescricional corre imediatamente a partir da data em que o primeiro benefício fraudulento foi pago pelo ente previdenciário.

### Súmula 17 do STJ e o princípio da consunção
Uma das questões mais cobradas nos concursos policiais diz respeito ao conflito aparente entre o crime de falso (arts. 297, 298, 299 ou 304 do CP) e o estelionato. O Superior Tribunal de Justiça uniformizou a matéria na **Súmula 17**: fixando que o crime de falsificação documental resta absorvido pelo estelionato quando exaure no golpe patrimonial sua potencialidade lesiva concreta, sem remanescer perigo de outras fraudes.
Se o agente confecciona um cheque falso ou RG adulterado unicamente para aplicá-lo em uma transação comercial determinada, e após o golpe a falsidade não detém viabilidade para outros crimes, o delito de falso (crime-meio) resta absorvido pelo estelionato (crime-fim). Se o documento mantiver aptidão lesiva residual futura para outros golpes, subsiste o concurso material de crimes.

Por fim, a **Súmula 73 do STJ** preceitua que a moeda com falsificação grosseira, incapaz de ludibriar o homem comum, descaracteriza o delito federal de moeda falsa e consubstancia estelionato comum de competência da Justiça Estadual.

### Para fixar
- O art. 171, § 3º, aumenta a pena de um terço se o estelionato atingir entidade de direito público.
- A Súmula 24 do STJ estende a majorante do § 3º a fraudes praticadas contra segurados da previdência.
- O estelionato previdenciário é permanente para o beneficiário que saca prestações mensais sucessivas.
- Para o intermediário da fraude, o estelionato previdenciário é instantâneo de efeitos permanentes.
- A prescrição para o beneficiário previdenciário conta-se da data da cessação do último pagamento.
- Pela Súmula 17 do STJ o falso que exaure sua potencialidade no estelionato é por este absorvido.
- A permanência de potencial lesivo autônomo no documento falso afasta o princípio da consunção.
- A Súmula 73 do STJ enquadra a falsificação grosseira de cédulas como estelionato da Justiça Estadual.""",
        "synthetic": [
            "**Majorante Pública (§ 3º)**: eleva o sancionamento em um terço quando o ardil lesar o patrimônio do erário, autarquias ou entes beneficentes.",
            "**Súmula 24 do STJ**: aplica a majorante fracionária do § 3º perante fraudes cometidas contra os próprios segurados do sistema previdenciário.",
            "**Bifurcação Previdenciária**: o estelionato contra o INSS ostenta natureza jurídica permanente para o segurado e instantânea para o intermediário.",
            "**Marco Prescricional do Segurado**: o lapso extintivo da punibilidade só começa a correr na data do cancelamento do benefício mensal ilícito.",
            "**Marco Prescricional do Terceiro**: para o despachante a prescrição inicia-se da percepção inaugural da primeira cota fraudada obtida.",
            "**Súmula 17 do STJ**: consagra a consunção jurídica absorvendo o falso pelo estelionato quando esgotada inteiramente sua potencialidade de dano.",
            "**Potencial Lesivo Remanescente**: subsiste o concurso formal ou material caso o documento forjado preserve viabilidade lesiva para crimes futuros.",
            "**Súmula 73 do STJ**: a falsificação grosseira e perceptível afasta o crime de moeda falsa atraindo estelionato de competência da Justiça Estadual."
        ]
    })

    return items, summaries
