# -*- coding: utf-8 -*-
"""Part 2 for a07: s03, s04 (Prevaricação, Sigilo Funcional, Súmulas e Jurisprudência)."""

def get_part2_data(get_fp):
    items = []
    summaries = []

    # -------------------------------------------------------------
    # SEGMENT 03: Prevaricação, Advocacia e Sigilo (p. 21-33)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a07/s03",
        "bizu": {
            "summary": [
                "**Prevaricação Clássica (art. 319)**: retardar ou omitir ato de ofício ou praticá-lo contra lei para satisfazer sentimento ou interesse pessoal egoístico.",
                "**Elemento Subjetivo Especial na Prevaricação**: o dolo exige o propósito de atender a capricho, afeto, ódio, inimizade ou proveito moral pessoal do servidor.",
                "**Prevaricação Imprópria (art. 319-A)**: inércia dolosa do agente carcerário em obstar o ingresso ou permanência de celulares no estabelecimento prisional.",
                "**Condescendência Criminosa (art. 320)**: deixar o funcionário, movido por indulgência e clemência, de punir subordinado que cometeu infração funcional.",
                "**Distinção Subjetiva Essencial**: na prevaricação o servidor busca satisfazer interesse pessoal; na condescendência atua movido por complacência e pena alheia.",
                "**Advocacia Administrativa (art. 321)**: interceder ou defender pretensão particular perante órgãos governamentais desfrutando do prestígio ou canais funcionais inerentes ao cargo.",
                "**Advocacia Qualificada (parágrafo único)**: a sanção é agravada se o interesse particular patrocinado perante a repartição for ilegítimo ou ilegal.",
                "**Abandono de Função (art. 323)**: afastar-se do posto fora das hipóteses legais (qualificado se gera prejuízo público ou se cometido em faixa de fronteira).",
                "**Violação de Sigilo Funcional (art. 325)**: revelar segredo oficial conhecido em virtude do cargo ou franquear senha de acesso a pessoas desautorizadas."
            ],
            "teoria": [
                {
                    "statement": "O delegado de polícia que deixa de lavrar flagrante contra desafeto com a intenção exclusiva de prejudicá-lo comete prevaricação.",
                    "isTrue": True,
                    "explanation": "A conduta de omitir ou desviar o dever funcional impulsionada por sentimento pessoal de inimizade consubstancia prevaricação típica (art. 319)."
                },
                {
                    "statement": "A condescendência criminosa aperfeiçoa-se quando o chefe superior deixa de aplicar advertência ao servidor subordinado por ter recebido propina deste.",
                    "isTrue": False,
                    "explanation": "Se a omissão punitiva decorre de vantagem financeira recebida, o delito é de corrupção passiva; a condescendência exige móvel de pura indulgência."
                },
                {
                    "statement": "O crime de abandono de função comina sanção punitiva exasperada caso a deserção do posto ocorra em território situado em faixa de fronteira.",
                    "isTrue": True,
                    "explanation": "O art. 323, § 2º, qualifica o abandono funcional praticado em faixa de fronteira, fixando reclusão de um a três anos em face do perigo estatal."
                },
                {
                    "statement": "O patrocínio legítimo de pleito privado perante autarquia realizado por servidor sem usar as prerrogativas do cargo consubstancia advocacia administrativa.",
                    "isTrue": False,
                    "explanation": "O tipo do art. 321 exige expressamente que o agente se valha de sua facilidade e qualidade de funcionário público para impulsionar o pleito."
                }
            ],
            "revisao": [
                {
                    "statement": "O policial penal que dolosamente tolera a utilização de telefone celular no pavilhão carcerário responde por prevaricação imprópria.",
                    "isTrue": True,
                    "explanation": "O art. 319-A pune a omissão do agente estatal em obstar a posse ou entrada de instrumentos celulares ou terminais de rádio na carceragem."
                },
                {
                    "statement": "A violação de sigilo funcional perpetrada mediante o empréstimo voluntário de senha funcional privativa configura mera infração disciplinar atípica.",
                    "isTrue": False,
                    "explanation": "O § 1º do art. 325 equipara formalmente ao crime a cessão indevida ou empréstimo culposo ou doloso de senha a terceiro não credenciado."
                },
                {
                    "statement": "Na advocacia administrativa, se o interesse defendido for inteiramente lícito perante a administração, o fato é penalmente impunível.",
                    "isTrue": False,
                    "explanation": "Mesmo quando o interesse privado for legítimo há crime na modalidade simples (caput do art. 321); se for ilegítimo, responde na forma qualificada."
                },
                {
                    "statement": "A prevaricação exige a obtenção efetiva de benefício patrimonial ilícito pelo servidor público para que atinja sua consumação.",
                    "isTrue": False,
                    "explanation": "O preceito tutela a moralidade e satisfaz-se com sentimento ou capricho íntimo pessoal, dispensando qualquer incremento econômico."
                }
            ],
            "pointers": [
                {"topic": "Prevaricação e dolo de sentimento pessoal no art. 319", "pageRef": 22},
                {"topic": "Prevaricação imprópria em presídios no art. 319-A", "pageRef": 25},
                {"topic": "Condescendência criminosa e advocacia administrativa", "pageRef": 28},
                {"topic": "Abandono funcional e violação de sigilo por senha no art. 325", "pageRef": 31}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a07/s03",
        "fingerprint": get_fp("direito-penal/a07/s03"),
        "analytic": """Este segmento aprofunda a análise dos delitos funcionais fundados na quebra da moralidade, fidelidade disciplinar e dever de sigilo, dissecando os institutos da prevaricação, da condescendência criminosa, da advocacia administrativa e do vazamento de informações estatais.

### Prevaricação clássica e prevaricação imprópria (artigos 319 e 319-A)
O artigo 319 resguarda o princípio republicano da impessoalidade e a legalidade estrita dos atos estatais:
- *Prevaricação Genérica*: comina detenção de três meses a um ano e multa para o funcionário que retarda ou deixa de praticar, indevidamente, ato de ofício, ou o pratica contra disposição expressa de lei;
- *Elemento Subjetivo Especial*: a conduta deve ser obrigatoriamente animada pelo desígnio de **satisfazer interesse ou sentimento pessoal**. O interesse pessoal compreende ambições corporativas, vaidade, pretensões materiais ou favores morais; o sentimento pessoal traduz emoções de afeto, compadrio, ódio, rancor ou antipatia contra o administrado;
- *Prevaricação Imprópria (artigo 319-A)*: acrescida pela Lei nº 11.466/2007 para combater o crime organizado intramuros prisionais, pune o diretor de estabelecimento penitenciário ou agente público que dolosamente se abstém de impedir que os detentos recebam ou mantenham instrumentos de comunicação móvel ou radiotransmissores no estabelecimento penal. Trata-se de crime formal omissivo puro que dispensa qualquer dano efetivo para atingir a consumação punitiva.

### Condescendência criminosa e advocacia administrativa (artigos 320 e 321)
A tolerância indevida e a exploração de influência privada recebem tratamento punitivo específico:
- *Condescendência Criminosa (artigo 320)*: tipifica o ato do superior hierárquico que, **por indulgência** (sentimento de piedade, clemência ou complacência frouxa), deixa de responsabilizar subordinado infrator ou omite-se de comunicar a falta à autoridade que detenha competência para instaurar sindicância ou processo administrativo disciplinar;
- *Advocacia Administrativa (artigo 321)*: consiste em patrocinar, direta ou dissimuladamente por terceiro, interesse de ordem privada perante a Administração Pública, valendo-se das facilidades, prestígio ou canais de sua investidura funcional;
- *Qualificadora do Artigo 321*: caso o pleito particular patrocinado ostente índole manifestamente **ilegítima ou antijurídica**, a pena eleva-se para detenção de três meses a um ano e multa.

### Abandono de cargo e violação de sigilo (artigos 323 a 325)
A continuidade das funções públicas e a preservação de dados estratégicos são asseguradas por preceitos cogentes:
- *Abandono de Função (artigo 323)*: incrimina a deserção desautorizada do exercício funcional, ostentando qualificadoras rigorosas se do fato decorre prejuízo patrimonial ou operacional concreto para o serviço público (§ 1º) ou se praticado em regiões limítrofes de fronteira internacional (§ 2º);
- *Violação de Sigilo Funcional (artigo 325)*: pune o servidor que revela fato que deva permanecer em segredo de que tomou conhecimento no exercício do cargo, ou que franqueia acesso desautorizado a bancos de dados sigilosos mediante o fornecimento fraudulento de sua senha funcional (§ 1º), cominando pena qualificada na ocorrência de dano concreto à administração ou a terceiros (§ 2º).

### Para fixar
- A prevaricação (art. 319) exige a busca de satisfação de interesse ou sentimento pessoal do funcionário.
- A omissão funcional impulsionada por recebimento de vantagem pecuniária configura corrupção passiva.
- A prevaricação imprópria (art. 319-A) pune a inércia do agente em reprimir celulares nos presídios.
- A condescendência criminosa exige motivação subjetiva de indulgência e pena do servidor infrator.
- A advocacia administrativa pune o patrocínio de interesse particular perante o órgão público em que atua.
- O patrocínio de interesse ilegítimo qualifica o delito de advocacia administrativa no parágrafo único.
- O abandono de função em faixa de fronteira consubstancia modalidade qualificada punida com reclusão.
- Franquear ou ceder senha funcional para acesso desautorizado aos dados equipara-se à violação de sigilo.""",
        "synthetic": [
            "**Prevaricação Material (art. 319)**: descumprimento ou retardamento do dever legal visando atender a sentimento egoístico ou capricho subjetivo.",
            "**Prevaricação em Presídios (art. 319-A)**: inércia funcional do carcereiro em confiscar terminais móveis que comunicam a massa carcerária com o exterior.",
            "**Condescendência Criminosa (art. 320)**: perdão indevido fundado em pura complacência complacente omitindo sanções contra subordinado relapso.",
            "**Advocacia Administrativa (art. 321)**: patrocínio de pleitos privados perante repartições estatais valendo-se das regalias do cargo público.",
            "**Qualificadora por Ilegitimidade**: o patrocínio de demanda manifestamente ilícita quadruplica o rigor sancionatório da advocacia funcional.",
            "**Abandono Funcional (art. 323)**: afastamento injustificado do serviço público cominando sanção exasperada em áreas fronteiriças nacionais.",
            "**Violação de Sigilo (art. 325)**: quebra de dever fiduciário de confidencialidade funcional que expõe relatórios reservados da administração.",
            "**Fraude de Senha Eletrônica**: disponibilização de credenciais individuais a pessoas desautorizadas consubstancia crime autônomo qualificado."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 04: Concorrência e Jurisprudência dos Tribunais (p. 34-44)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a07/s04",
        "bizu": {
            "summary": [
                "**Sigilo de Concorrência (revogado art. 326)**: a conduta de violar o sigilo de proposta licitatória foi transladada para o art. 337-J do CP pela Lei 14.133/2021.",
                "**Súmula 599 do STJ**: a jurisprudência sumulada veda a tese da bagatela aos ilícitos praticados em desfavor do poder público em homenagem à probidade administrativa.",
                "**Ressalva do Descaminho Tributário**: a inaplicabilidade sumulada da insignificância comporta exceção jurisprudencial consolidada no delito de descaminho.",
                "**Súmula 330 do STJ**: é desnecessária a resposta preliminar do art. 514 do CPP quando a denúncia em crime funcional estiver lastreada em inquérito policial.",
                "**Perda do Cargo Público (art. 92, I, do CP)**: efeito extrapenal secundário da condenação funcional que exige fundamentação expressa na sentença.",
                "**Requisitos da Perda do Cargo**: pena privativa igual ou superior a 1 ano nos crimes funcionais, ou superior a 4 anos em qualquer delito comum.",
                "**Inexistência de Perda Automática**: no Código Penal a perda do cargo jamais opera de pleno direito, devendo ser expressamente motivada pelo juiz.",
                "**Súmula Vinculante 24 do STF**: a tipificação material de crimes contra a ordem tributária depende do encerramento definitivo do processo administrativo fiscal."
            ],
            "teoria": [
                {
                    "statement": "Segundo entendimento sumulado do Superior Tribunal de Justiça, é cabível aplicar o princípio da insignificância ao crime de peculato comum.",
                    "isTrue": False,
                    "explanation": "A Súmula 599 do STJ veda categoricamente a aplicação do princípio da insignificância a crimes perpetrados contra a administração pública."
                },
                {
                    "statement": "A notificação prévia prevista no artigo 514 do Código de Processo Penal torna-se dispensável se a denúncia for precedida de inquérito policial formal.",
                    "isTrue": True,
                    "explanation": "A Súmula 330 do STJ consagrou a desnecessidade de defesa preliminar funcional quando a acusação vem instruída por inquérito policial."
                },
                {
                    "statement": "A perda do cargo público decorrente de condenação por corrupção passiva opera de forma automática e imediata no trânsito em julgado.",
                    "isTrue": False,
                    "explanation": "O art. 92, parágrafo único, do CP exige motivação formal expressa na sentença para a perda do cargo, não ocorrendo de forma automática."
                },
                {
                    "statement": "A prática de descaminho com tributos sonegados inferiores a vinte mil reais admite a aplicação do princípio da insignificância material.",
                    "isTrue": True,
                    "explanation": "A jurisprudência do STF e STJ excepciona expressamente o descaminho (art. 334) da Súmula 599, fixando parâmetro de vinte mil reais."
                }
            ],
            "revisao": [
                {
                    "statement": "A revogação do artigo 326 do Código Penal pela Nova Lei de Licitações operou abolitio criminis quanto à violação de propostas licitatórias.",
                    "isTrue": False,
                    "explanation": "Houve continuidade normativo-típica, sendo a conduta inserida no art. 337-J do Código Penal pela Lei nº 14.133/2021."
                },
                {
                    "statement": "Para que incida a perda da função pública nos crimes funcionais com abuso de poder, a sanção privativa de liberdade deve ser superior a um ano.",
                    "isTrue": True,
                    "explanation": "O art. 92, I, 'a', do Código Penal estabelece o patamar de pena privativa de liberdade aplicada por tempo igual ou superior a um ano."
                },
                {
                    "statement": "O ex-servidor que já se encontrava aposentado na data do oferecimento da ação penal faz jus à notificação prévia do artigo 514 do CPP.",
                    "isTrue": False,
                    "explanation": "O STF e STJ consolidaram que a prerrogativa procedimental da defesa preliminar não se estende a agentes que já deixaram a função pública."
                },
                {
                    "statement": "A consumação de crime material contra a ordem tributária tributária reclama o prévio encerramento de lançamento administrativo.",
                    "isTrue": True,
                    "explanation": "A Súmula Vinculante 24 do STF exige o lançamento fiscal definitivo do tributo para a persecução de crime material tributário."
                }
            ],
            "pointers": [
                {"topic": "Nova tipificação de violação licitatória no art. 337-J", "pageRef": 35},
                {"topic": "Inaplicabilidade da insignificância e Súmula 599 do STJ", "pageRef": 38},
                {"topic": "Defesa prévia funcional e abrangência da Súmula 330 do STJ", "pageRef": 41},
                {"topic": "Efeitos da condenação e perda de cargo público no art. 92", "pageRef": 43}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a07/s04",
        "fingerprint": get_fp("direito-penal/a07/s04"),
        "analytic": """Este segmento consolida o estudo dos crimes funcionais examinando as transformações normativas introduzidas pela Nova Lei de Licitações (Lei nº 14.133/2021), a aplicabilidade do princípio da insignificância, os efeitos secundários da condenação e as diretrizes sumulares do STF e STJ.

### Da proposta de concorrência e transição para o artigo 337-J
Historicamente, o Código Penal criminalizava a devassa de envelopes em certames licitatórios no seu artigo 326 (violação do sigilo de proposta de concorrência). Com o advento da Lei nº 14.133/2021 (Nova Lei de Licitações), esse preceito foi formalmente revogado, ocorrendo fenômeno inequívoco de continuidade normativo-típica com a inserção do artigo 337-J no estatuto penal:
- *Elemento Material*: pune quem devassa ou facilita a divulgação indevida do teor de propostas em qualquer procedimento concorrencial ou licitatório promovido pela Administração Pública;
- *Apenamento Atualizado*: a nova ordem conferiu resposta sancionatória mais proporcional e rigorosa, cominando pena de detenção de dois a três anos e multa.

### O princípio da insignificância nos crimes contra a administração pública
A aplicação do princípio da bagatela ou insignificância perante a criminalidade funcional é tema de constante enfrentamento judicial:
- *Enunciado da Súmula 599 do Superior Tribunal de Justiça*: firmou-se que a tese da insignificância material não possui cabimento nas infrações que vulneram o aparato estatal e sua integridade moral;
- *Razão Dogmática da Vedação*: nos delitos funcionais (peculato, concussão, corrupção), o bem jurídico primário tutelado não é o valor contábil do prejuízo patrimonial, mas sim a **moralidade administrativa, a dignidade do cargo e a probidade funcional**, valores que ostentam caráter imaterial e insuscetível de quantificação financeira mínima;
- *Exceção Jurisprudencial Consolidada*: a jurisprudência pacífica do STF e do STJ excepciona exclusivamente o crime de **descaminho** (artigo 334), permitindo a incidência do princípio bagatelar desde que o montante dos tributos sonegados não ultrapasse o teto fiscal legalmente fixado para a execução fiscal federal (vinte mil reais).

### Procedimento preliminar e efeitos extrapenais da condenação
Aspectos processuais e sancionatórios de alta relevância incidem sobre a persecução funcional:
- *Defesa Preliminar e a Súmula 330 do STJ*: o artigo 514 do Código de Processo Penal prescreve a notificação do funcionário público para apresentar defesa preliminar antes do recebimento da denúncia em crimes afiançáveis. O Superior Tribunal de Justiça editou a **Súmula 330**, fixando que tal formalidade prévia é **desnecessária quando a ação penal for instruída com base em inquérito policial**, visto que a fase investigativa inquisitorial já assegurou base empírica suficiente;
- *Efeitos Específicos da Condenação (artigo 92, inciso I)*: a perda do cargo, emprego ou mandato eletivo comina-se na hipótese de condenação a reprimenda corporal fixada em patamar equivalente ou superior a doze meses quando a conduta envolver desvio funcional, ou quando a pena exceder a quatro anos em qualquer outra hipótese;
- *Exigência de Motivação Expressa*: o Código Penal brasileiro não admite a perda automática do cargo público, exigindo que o magistrado fundamente e declare expressamente o decreto de perda na fundamentação da sentença condenatória.

### Para fixar
- A Lei 14.133/2021 revogou o art. 326 e inseriu a violação de proposta de concorrência no art. 337-J do CP.
- A Súmula 599 do STJ declara que a insignificância não se aplica aos crimes contra o poder público.
- A proteção à moralidade e integridade do cargo afasta o reconhecimento do valor pecuniário ínfimo.
- O crime de descaminho é a única exceção admitida pelos tribunais para incidência da bagatela.
- A Súmula 330 do STJ dispensa a notificação do art. 514 do CPP quando houver inquérito policial.
- A perda do cargo público exige sanção privativa de liberdade igual ou superior a um ano no crime funcional.
- A perda do cargo nunca opera de forma automática, necessitando de expressa declaração motivada na sentença.
- A Súmula Vinculante 24 do STF exige o encerramento da esfera fiscal para crimes materiais tributários.""",
        "synthetic": [
            "**Translação Típica (art. 337-J)**: transferência do sigilo licitatório para o novo capítulo preservando a continuidade punitiva formal.",
            "**Súmula 599 do STJ**: veto peremptório à tese da insignificância em virtude da intangibilidade do princípio moral da probidade pública.",
            "**Exceção no Descaminho**: permissão excepcional da bagatela fazendária caso os tributos elididos não superem vinte mil reais.",
            "**Súmula 330 do STJ**: dispensa da resposta preliminar defensiva funcional quando a persecução vier precedida de inquérito policial.",
            "**Perda de Cargo Público (art. 92)**: efeito secundário não automático subordinado a prazo penal mínimo e imperativa motivação jurisdicional.",
            "**Regra do Trânsito em Julgado**: cassação do vínculo estatutário funcional somente adquire eficácia executiva após preclusão definitiva.",
            "**Proteção de Fontes Tributárias**: Súmula Vinculante 24 impede a persecução criminal de crime material antes do lançamento fiscal.",
            "**Inaplicabilidade ao Ex-Servidor**: os ritos protetivos do art. 514 do CPP cessam caso o agente já tenha se desincompatibilizado do cargo."
        ]
    })

    return items, summaries
