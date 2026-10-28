# -*- coding: utf-8 -*-
"""Part 1 for a09: s01, s02, s03 (Administração da Justiça, Falso Testemunho e Favorecimento)."""

def get_part1_data(get_fp):
    items = []
    summaries = []

    # -------------------------------------------------------------
    # SEGMENT 01: Denunciação Caluniosa e Medidas Protetivas (p. 2-17)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a09/s01",
        "bizu": {
            "summary": [
                "**Denunciação Caluniosa (art. 339)**: provocar instauração de inquérito, processo judicial, inquérito civil ou PAD contra pessoa sabidamente inocente.",
                "**Reforma da Lei 14.110/2020**: estendeu expressamente o tipo à imputação de infração ético-disciplinar ou ato de improbidade administrativa inverídico.",
                "**Dolo Direto de Certeza de Inocência**: exige que o agente tenha ciência inequívoca da inocência da vítima; a dúvida razoável ou erro afasta a tipicidade dolosa.",
                "**Forma Atenuada (§ 2º do art. 339)**: redução penal de metade caso a imputação caluniosa verse unicamente sobre contravenção penal.",
                "**Majorante por Anonimato (§ 1º)**: elevação de um sexto na pena se o autor se vale de anonimato ou oculta a identidade sob nome fictício suposto.",
                "**Comunicação Falsa de Crime (art. 340)**: provocar a ação de autoridade comunicando delito ou contravenção que sabe não ter ocorrido, sem apontar pessoa certa.",
                "**Descumprimento de Medidas Protetivas (art. 24-A da Lei 11.340/06)**: descumprir decisão judicial protetiva deferida em favor de mulher em situação de violência.",
                "**Inafiançabilidade Policial no Art. 24-A**: a concessão de fiança provisória é prerrogativa privativa do magistrado, vedado o arbitramento pelo delegado.",
                "**Corrupção Internacional (art. 337-B)**: prometer ou conceder vantagem espúria a funcionário estrangeiro em comércio exterior."
            ],
            "teoria": [
                {
                    "statement": "O crime de denunciação caluniosa resta configurado mesmo quando o denunciante atua impelido por mera dúvida subjetiva quanto à culpa do acusado.",
                    "isTrue": False,
                    "explanation": "O art. 339 exige dolo direto consistente na certeza plena de que o indigitado é inocente ('de que o sabe inocente'), não bastando dúvida."
                },
                {
                    "statement": "A autoridade policial não possui competência legal para arbitrar fiança no crime de descumprimento de medidas protetivas de urgência.",
                    "isTrue": True,
                    "explanation": "O art. 24-A, § 2º, da Lei 11.340/2006 estabelece expressamente que apenas a autoridade judicial poderá conceder fiança ao preso em flagrante."
                },
                {
                    "statement": "A comunicação de crime imaginário a órgão policial sem individualizar qualquer pessoa determinada como autora subsume-se ao art. 339 do CP.",
                    "isTrue": False,
                    "explanation": "Se a comunicação não indica sujeito passivo determinado, tipifica-se o crime de comunicação falsa de crime ou contravenção (art. 340)."
                },
                {
                    "statement": "Com a Lei 14.110/2020, imputar falsamente ato de improbidade administrativa a rival sabendo-o inocente configura denunciação caluniosa.",
                    "isTrue": True,
                    "explanation": "A reforma introduzida pela Lei 14.110/2020 inseriu expressamente a ação de improbidade administrativa no rol nuclear do artigo 339 do CP."
                }
            ],
            "revisao": [
                {
                    "statement": "A retratação voluntária do denunciante após o recebimento formal da denúncia criminal opera a imediata extinção de sua punibilidade penal.",
                    "isTrue": False,
                    "explanation": "O Código Penal não prevê causa extintiva de punibilidade pela retratação no delito de denunciação caluniosa (art. 339)."
                },
                {
                    "statement": "A falsa imputação de contravenção penal perante a polícia acarreta a aplicação da sanção da denunciação caluniosa atenuada de metade.",
                    "isTrue": True,
                    "explanation": "O art. 339, § 2º, estabelece que a pena é diminuída de metade se a imputação inverídica for de contravenção e não de crime."
                },
                {
                    "statement": "O consentimento da mulher ofendida em receber o agressor na residência descaracteriza a tipicidade formal do crime do art. 24-A da Lei Maria da Penha.",
                    "isTrue": False,
                    "explanation": "O STJ firmou que a anuência da vítima não afasta o crime do art. 24-A, pois a decisão judicial é imperativa e tutela a administração da justiça."
                },
                {
                    "statement": "O envio de carta apócrifa anônima à ouvidoria que dá ensejo a processo administrativo disciplinar qualifica a denunciação caluniosa com majorante.",
                    "isTrue": True,
                    "explanation": "O § 1º do art. 339 prevê a majoração de um sexto na pena se o agente se vale de anonimato para deflagrar a perseguição indevida."
                }
            ],
            "pointers": [
                {"topic": "Denunciação caluniosa e alterações da Lei 14.110/2020", "pageRef": 4},
                {"topic": "Comunicação falsa e distinção com imputação nominada", "pageRef": 8},
                {"topic": "Descumprimento de medidas protetivas e fiança judicial", "pageRef": 12},
                {"topic": "Corrupção transnacional em transações internacionais no art. 337-B", "pageRef": 15}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a09/s01",
        "fingerprint": get_fp("direito-penal/a09/s01"),
        "analytic": """Este segmento inaugura a análise dos crimes perpetrados contra a Administração da Justiça, dissecando os preceitos que punem a instrumentalização fraudulenta dos órgãos investigativos do Estado e as violações à autoridade das decisões jurisdicionais protetivas.

### Denunciação caluniosa e a reforma da Lei nº 14.110/2020 (artigo 339)
O preceito do artigo 339 reprime a conduta lesiva de provocar a instauração de procedimentos estatais contra indivíduo sabidamente inocente:
- *Reformas Estruturais*: a Lei nº 14.110/2020 ampliou expressamente o objeto material da denunciação. Atualmente, o tipo abrange provocar a deflagração de **inquérito policial, procedimento investigatório criminal ministerial, processo judicial formal, inquérito civil público, ação de improbidade administrativa ou processo administrativo disciplinar (PAD)** contra quem o denunciante sabe ser inocente;
- *Elemento Subjetivo Especial*: a jurisprudência é uníssona em exigir **dolo direto e certeza subjetiva de inocência**. O agente deve agir com a convicção plena de que a imputação é desprovida de veracidade. Caso atue respaldado em meras suspeitas, animosidade culposa ou dúvida plausível sobre os fatos, afasta-se a subsunção ao artigo 339 por atipicidade da conduta;
- *Causas Modificadoras de Pena*:
  1. *Majorante (§ 1º)*: eleva-se a pena em um sexto se o autor oculta a identidade mediante missiva apócrifa ou socorre-se de nome suposto;
  2. *Forma Atenuada (§ 2º)*: a pena cominada diminui-se de metade na hipótese de a acusação forjada versar sobre mera contravenção penal.

### Comunicação falsa de crime ou de contravenção (artigo 340)
O artigo 340 pune o indivíduo que aciona indevidamente o aparato de persecução estatal, provocando a ação de autoridade pública ao comunicar-lhe a ocorrência de infração penal inexistente:
- *Distinção com a Denunciação Caluniosa*: na comunicação falsa, **não há direcionamento contra pessoa determinada**. O comunicante apenas relata fato delituoso imaginário (exemplo da pessoa que registra falso furto de automóvel na delegacia para fraudar a seguradora privada, sem acusar pessoa específica); caso venha a apontar nominalmente um desafeto, o crime transmuta-se para a figura mais grave de denunciação caluniosa.

### Descumprimento de medidas protetivas (artigo 24-A da Lei Maria da Penha)
Inserido na Lei nº 11.340/2006, o tipo penal do artigo 24-A pune quem descumpre ordem judicial concessiva de provimento de urgência protetivo em contexto de violência de gênero:
- *Tutela da Dignidade da Justiça*: o bem jurídico primordial é a efetividade dos mandamentos emanados do Poder Judiciário. Em virtude disso, o Superior Tribunal de Justiça firmou que o consentimento ou a condescendência posterior da vítima não elidem a materialidade delitiva;
- *Prerrogativa Fidejussória*: o parágrafo segundo do dispositivo veda peremptoriamente ao delegado de polícia o arbitramento de fiança, conferindo essa faculdade em caráter exclusivo ao magistrado competente.

### Para fixar
- A Lei 14.110/2020 inseriu a improbidade administrativa e o PAD no tipo da denunciação caluniosa.
- O dolo no art. 339 reclama a ciência inequívoca e induvidosa da inocência da pessoa incriminada.
- A imputação inverídica de contravenção penal enseja causa especial de diminuição de metade da pena.
- O emprego de nome falso ou anonimato exaspera a reprimenda da denunciação na fração de um sexto.
- A comunicação falsa de crime (art. 340) tutela o serviço policial quando não há vítima imputada.
- O art. 24-A da Lei Maria da Penha reprime o descumprimento de provimentos judiciais protetivos.
- Apenas a autoridade judiciária detém atribuição legal para conceder fiança no crime do art. 24-A.
- A reconciliação amigável entre as partes não revoga de pleno direito a proibição judicial de aproximação.""",
        "synthetic": [
            "**Denunciação Caluniosa (art. 339)**: acionamento ardiloso do aparato persecutório estatal em detrimento de cidadão sabidamente inocente.",
            "**Abrangência pela Lei 14.110/20**: inclusão formal de ações civis públicas, investigações de improbidade e procedimentos disciplinares corporativos.",
            "**Dolo de Inocência Certa**: elementar típica subjetiva indispensável exigindo convicção inconteste do falsário acerca da ausência de culpa alheia.",
            "**Comunicação Falsa (art. 340)**: alarme infundado perante repartição policial noticiando ilícito fictício sem eleger pessoa determinada.",
            "**Descumprimento Protetivo (art. 24-A)**: quebra voluntária de restrições fixadas pela magistratura em amparo à integridade feminina.",
            "**Reserva Judicial de Fiança**: proibição normativa de arbitramento da caução pela autoridade policial em sede de flagrante do art. 24-A.",
            "**Inadmissão de Anuência da Vítima**: a jurisprudência repele o perdão informal como causa de descriminalização do descumprimento de ordem.",
            "**Corrupção Internacional**: repressão mercantil incidente sobre manobras espúrias voltadas a cooptar servidores de potências estrangeiras."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 02: Falso Testemunho, Perícia e Coação (p. 18-32)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a09/s02",
        "bizu": {
            "summary": [
                "**Autoacusação Falsa (art. 341)**: acusar-se falsamente perante a autoridade de crime inexistente ou praticado por outra pessoa.",
                "**Falso Testemunho ou Perícia (art. 342)**: declaração intencionalmente mendaz, silenciamento ou distorção dos fatos emitidos em juízo ou inquérito por depoente sob juramento legal.",
                "**Crime Próprio de Mão Própria**: delito que exige a execução direta e pessoal do depoente qualificado, inviabilizando a coautoria de quem não depõe.",
                "**Majorante por Suborno (§ 1º do art. 342)**: aumento de um sexto a um terço se praticado mediante suborno ou para produzir prova em processo penal.",
                "**Retratação Despenalizadora (§ 2º)**: extinção da punibilidade assegurada caso o depoente volte atrás voluntariamente revelando os fatos verídicos antes da sentença de primeiro grau.",
                "**Corrupção Ativa de Testemunha (art. 343)**: dar, oferecer ou prometer vantagem indevida a testemunha para falsear a verdade (crime formal autônomo).",
                "**Coação no Curso do Processo (art. 344)**: empregar violência corporal ou grave ameaça contra partícipe ou autoridade processual para favorecer interesse.",
                "**Autotutela Arbitrária (art. 345)**: emprego de meios particulares diretos para realização forçada de direito próprio que se julga legítimo à margem do Poder Judiciário.",
                "**Fraude Processual (art. 347)**: inovar artificiosamente o estado de lugar, coisa ou pessoa visando induzir o juiz ou perito em erro decisório."
            ],
            "teoria": [
                {
                    "statement": "O crime de falso testemunho consuma-se com o encerramento formal do depoimento, independentemente de a mentira influenciar o veredito.",
                    "isTrue": True,
                    "explanation": "O falso testemunho é crime formal que se aperfeiçoa com a assinatura do termo ou encerramento da inquirição judicial ou policial."
                },
                {
                    "statement": "A retratação da testemunha que declara a verdade extingue a punibilidade se operada a qualquer momento antes do trânsito em julgado.",
                    "isTrue": False,
                    "explanation": "O art. 342, § 2º, estabelece como marco temporal preclusivo a prolação da sentença no processo em que se consumou o falso depoimento."
                },
                {
                    "statement": "O delito de exercício arbitrário das próprias razões procede-se mediante ação penal privada caso não haja o emprego de violência corporal.",
                    "isTrue": True,
                    "explanation": "O parágrafo único do art. 345 estabelece que a ação penal é exclusivamente privada se não houver emprego de violência à pessoa."
                },
                {
                    "statement": "A conduta do advogado que orienta dolosamente a testemunha a prestar declarações mendazes é sempre atípica perante o Código Penal.",
                    "isTrue": False,
                    "explanation": "O partícipe moral que instiga ou suborna a testemunha responde como partícipe do falso testemunho ou autor do art. 343."
                }
            ],
            "revisao": [
                {
                    "statement": "A vítima do crime que mente no processo em suas declarações orais comete o crime formal de falso testemunho do art. 342 do CP.",
                    "isTrue": False,
                    "explanation": "O ofendido não presta compromisso de dizer a verdade como testemunha, não figurando como sujeito ativo do artigo 342."
                },
                {
                    "statement": "A coação no curso do processo qualifica-se com pena mais grave caso envolva delito contra a dignidade sexual em apuração.",
                    "isTrue": True,
                    "explanation": "O parágrafo único do art. 344 prevê causa de aumento da pena de um sexto a um terço se o processo envolver crimes contra a dignidade sexual."
                },
                {
                    "statement": "O delito de autoacusação falsa (art. 341) resta consumado mesmo se o fato confessado pelo agente constituir mera contravenção penal.",
                    "isTrue": False,
                    "explanation": "O tipo do artigo 341 exige expressamente a autoacusação de 'crime', sendo a imputação de contravenção atípica perante este preceito."
                },
                {
                    "statement": "A inovação artificiosa em local de acidente automobilístico para enganar a perícia oficial tipifica a fraude processual do art. 347.",
                    "isTrue": True,
                    "explanation": "O art. 347 tutela a fidedignidade probatória, punindo a alteração dolosa do estado de pessoas, coisas ou lugares na pendência do feito."
                }
            ],
            "pointers": [
                {"topic": "Falso testemunho e consumação formal de mão própria", "pageRef": 20},
                {"topic": "Eficácia extintiva temporal da retratação antes da sentença", "pageRef": 23},
                {"topic": "Coação processual e exercício arbitrário das próprias razões", "pageRef": 27},
                {"topic": "Fraude processual e inovação artificiosa no art. 347", "pageRef": 30}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a09/s02",
        "fingerprint": get_fp("direito-penal/a09/s02"),
        "analytic": """Este segmento aborda os ilícitos penais que atacam a pureza probatória e a integridade da jurisdição estatal, detalhando os delitos de falso testemunho e perícia, corrupção de depoentes, coação processual, autotutela arbitrária e fraude probatória.

### Falso testemunho e falsa perícia (artigo 342)
O artigo 342 comina reclusão de dois a quatro anos e multa à testemunha, perito oficial, tradutor ou intérprete que faz afirmação falsa, nega a verdade ou cala dolosamente aquilo que sabe:
- *Natureza de Mão Própria e Formal*: cuida-se de delito de mão própria, que só pode ser fisicamente executado por quem figura no papel processual de testemunha compromissada. Não admite coautoria com terceiros não testemunhas (admitindo-se apenas a participação por instigação). A consumação perfectibiliza-se com o encerramento do ato de depoimento e assinatura da ata, independentemente de o juiz ser iludido ou não pelo testemunho;
- *Causas Especiais de Aumento (§ 1º)*: a pena cominada sofre exasperação de **um sexto a um terço** caso o falso seja cometido mediante promessa ou recebimento de suborno pecuniário, ou praticado com o propósito deliberado de produzir prova em feito criminal;
- *Retratação Extintiva de Punibilidade (§ 2º)*: o dispositivo consagra benefício despenalizador expressivo: **o fato deixa de ser punível se, antes da prolatação da sentença no processo em que ocorreu o falso, o agente se retrata formalmente e declara a verdade perante a autoridade judiciária**. Caso a retratação ocorra após a sentença originária de primeiro grau, subsiste o crime, operando-se no máximo atenuante genérica.

### Coação processual e autotutela arbitrária (artigos 344 e 345)
O império da lei interdita a imposição violenta de vontades particulares em feitos judiciais:
- *Coação no Curso do Processo (artigo 344)*: sanciona o emprego de violência corporal física ou grave ameaça contra autoridade judiciária, membros do Ministério Público, partes, peritos, advogados ou testemunhas, visando favorecer interesse próprio ou alheio em processo judicial, policial ou arbitral. O preceito conta com causa especial de aumento caso envolva litígios alusivos a crimes contra a dignidade sexual (parágrafo único);
- *Exercício Arbitrário das Próprias Razões (artigo 345)*: pune o ato de fazer justiça pelas próprias mãos para satisfazer pretensão legítima (ou que o autor sinceramente supõe legítima), usurpando o monopólio jurisdicional do Estado. **Se a execução da autotutela for perpetrada sem violência contra a pessoa (apenas mediante arrombamento ou tomada de coisa), a ação penal procede-se estritamente mediante queixa-crime privada** do ofendido.

### Fraude processual (artigo 347)
O crime de fraude processual reprova as maquinações materiais destinadas a contaminar a convicção do magistrado ou do perito oficial:
- Consuma-se pela inovação artificiosa no estado de lugares, coisas ou aspectos físicos de pessoas no curso de processo civil ou trabalhista;
- *Forma Qualificada (parágrafo único)*: a sanção é duplicada caso a inovação fraudulenta se destine a produzir efeitos no âmbito de processo penal ainda não instaurado ou já em andamento.

### Para fixar
- O falso testemunho é crime formal e de mão própria consumado com o término da audiência.
- O informante descompromissado e a vítima não cometem o crime do art. 342 do estatuto penal.
- O suborno à testemunha atrai a causa de aumento de pena de um sexto a um terço no § 1º.
- A retratação antes da prolação da sentença extingue formalmente a punibilidade do falso testemunho.
- A coação no curso do processo (art. 344) tutela a liberdade dos participantes na instrução processual.
- O exercício arbitrário das próprias razões sem violência corporal é processado por queixa privada.
- A alteração dolosa do local de crime para iludir peritos oficiais amolda-se à fraude processual.
- A pena da fraude processual aplica-se em dobro caso a adulteração ocorra em feito criminal.""",
        "synthetic": [
            "**Falso Testemunho (art. 342)**: quebra dolosa do dever de veracidade processual praticada por testemunha ou perito sob rito formal.",
            "**Inadmissão de Coautoria**: crime de mão própria personalíssimo que admite apenas participação moral por instigação ou suborno.",
            "**Eficácia da Retratação**: extinção da punibilidade assegurada caso a testemunha fale a verdade antes da prolação da sentença.",
            "**Coação no Processo (art. 344)**: intimidação violenta desferida contra sujeitos do processo visando constranger a marcha jurisdicional.",
            "**Majorante na Dignidade Sexual**: exasperação sancionatória na hipótese de a coação intimidatória ocorrer em litígios de delitos sexuais.",
            "**Exercício Arbitrário (art. 345)**: autotutela desautorizada de direitos legítimos com persecução exclusivamente privada na ausência de violência corporal.",
            "**Fraude Processual (art. 347)**: inovação ardilosa em cena de fato ou vestígios para enganar a formação de convicção dos peritos.",
            "**Duplicação em Feito Penal**: elevação da resposta punitiva em cem por cento caso a maquinação probatória atinja litígio criminal."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 03: Favorecimento, Evasão e Patrocínio Infiel (p. 33-42)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a09/s03",
        "bizu": {
            "summary": [
                "**Favorecimento Pessoal (art. 348)**: prestar auxílio a autor de crime para que este se subtraia à atuação e captura da autoridade pública.",
                "**Escusa Absolutória no Favorecimento Pessoal (§ 2º)**: isenção de pena inafastável se quem presta o auxílio de fuga for cônjuge, companheiro, ascendente, descendente ou irmão.",
                "**Favorecimento Real (art. 349)**: prestar a criminoso auxílio material voltado a tornar seguro o proveito econômico do delito praticado.",
                "**Distinção de Receptação e Coautoria**: o favorecimento real é subsidiário e pressupõe que o favorecedor não tenha participado do crime originário nem adquirido a coisa para si.",
                "**Favorecimento Real Impróprio (art. 349-A)**: ingressar ou intermediar a entrada clandestina de telefone celular ou rádio transmissor em recinto penitenciário.",
                "**Evasão Mediante Violência (art. 352)**: evadir-se ou tentar a fuga o indivíduo preso mediante o emprego de agressão violenta contra pessoas (guardas ou civis).",
                "**Atipicidade da Fuga sem Violência**: a fuga limpa sem agressão corporal contra o agente carcerário não constitui crime, ensejando mera falta disciplinar grave na LEP.",
                "**Arrebatamento de Preso (art. 353)**: arrancar pela força ou resgatar preso da custódia do poder público (crime praticado por terceiros externos).",
                "**Patrocínio Infiel (art. 355)**: trair dever profissional de procurador ou advogado prejudicando dolosamente os interesses da parte que defende em juízo."
            ],
            "teoria": [
                {
                    "statement": "O pai que esconde o próprio filho foragido da polícia em sítio isolado resta isento de pena pelo crime de favorecimento pessoal.",
                    "isTrue": True,
                    "explanation": "O art. 348, § 2º, estabelece escusa absolutória que isenta de pena o ascendente, descendente, cônjuge ou irmão que auxilia a fuga."
                },
                {
                    "statement": "A fuga de detento realizada mediante escalada e rompimento de grades sem qualquer agressão física contra guardas tipifica o art. 352 do CP.",
                    "isTrue": False,
                    "explanation": "O art. 352 exige violência física direta contra a pessoa; a fuga com força nas coisas é fato penalmente atípico, configurando falta da LEP."
                },
                {
                    "statement": "O advogado que defende sucessivamente na mesma causa partes que ostentam interesses antagônicos comete patrocínio simultâneo ou tergiversação.",
                    "isTrue": True,
                    "explanation": "O parágrafo único do art. 355 pune o patrono que defende no mesmo processo partes com pretensões jurídicas opostas."
                },
                {
                    "statement": "O agente que ingressa em estabelecimento carcerário portando chip de telefonia celular escondido responde por prevaricação imprópria.",
                    "isTrue": False,
                    "explanation": "A conduta de introduzir componentes de comunicação no presídio amolda-se formalmente ao art. 349-A (favorecimento real impróprio)."
                }
            ],
            "revisao": [
                {
                    "statement": "A escusa absolutória por laço de parentesco prevista no favorecimento pessoal aplica-se identicamente ao crime de favorecimento real patrimonial.",
                    "isTrue": False,
                    "explanation": "A isenção de pena por consanguinidade restringe-se ao favorecimento pessoal (§ 2º do art. 348), inexistindo no favorecimento real (art. 349)."
                },
                {
                    "statement": "O favorecimento real pressupõe que o agente não tenha concorrido previamente na qualidade de coautor ou partícipe no crime antecedente.",
                    "isTrue": True,
                    "explanation": "Caso tenha participado do delito anterior, responde pelo próprio crime patrimonial antecedente e não pelo delito acessório do art. 349."
                },
                {
                    "statement": "O arrebatamento de preso (art. 353) consuma-se unicamente se os detentos libertados conseguirem alcançar a fuga definitiva da comarca.",
                    "isTrue": False,
                    "explanation": "É crime formal de perigo que se consuma no exato momento da retirada violenta do indivíduo da custódia material do agente de guarda."
                },
                {
                    "statement": "A entrada desautorizada de carregador de celular na penitenciária amolda-se à figura típica autônoma do artigo 349-A do Código Penal.",
                    "isTrue": True,
                    "explanation": "O STJ pacificou que a introdução de carregadores, baterias ou aparelhos no presídio subsume-se ao favorecimento real do art. 349-A."
                }
            ],
            "pointers": [
                {"topic": "Favorecimento pessoal e escusa absolutória familiar no art. 348", "pageRef": 34},
                {"topic": "Favorecimento real patrimonial e ingresso de celular no art. 349-A", "pageRef": 36},
                {"topic": "Evasão qualificada pela violência e atipicidade da fuga sem violência", "pageRef": 39},
                {"topic": "Patrocínio infiel, tergiversação e sonegação de documentos", "pageRef": 41}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a09/s03",
        "fingerprint": get_fp("direito-penal/a09/s03"),
        "analytic": """Este segmento aborda os crimes processuais que conspiram contra a custódia de indivíduos sob custódia estatal, a fidelidade profissional no patrocínio judiciário e as distinções dogmáticas entre favorecimento pessoal e real.

### Favorecimento pessoal e favorecimento real (artigos 348 a 349-A)
A legislação penal delineia com rigor o auxílio clandestino prestado a autores de crimes:
- *Favorecimento Pessoal (artigo 348)*: consiste na conduta de prestar auxílio a quem praticou um crime para subtraí-lo à ação da autoridade encarregada de sua custódia ou captura;
- *Escusa Absolutória Familiar (§ 2º)*: por razões de piedade familiar e inexigibilidade de conduta diversa, **o cônjuge, companheiro, ascendente, descendente ou irmão que presta auxílio de fuga ao familiar foragido fica inteiramente isento de pena**;
- *Favorecimento Real (artigo 349)*: pune quem presta a criminoso auxílio destinado a assegurar o proveito econômico obtido com o delito (guardar jóias roubadas no sótão para o comparsa). **A escusa familiar do parentesco não se aplica ao favorecimento real**;
- *Favorecimento Real Impróprio (artigo 349-A)*: acrescido pela Lei nº 12.012/2009, tipifica a ação de ingressar, intermediar ou facilitar a entrada de aparelho telefônico, radiotransmissor ou seus acessórios essenciais (como baterias e chips) em estabelecimentos carcerários sem chancela da direção.

### Crimes de fuga e arrebatamento (artigos 351 a 353)
A preservação da custódia cautelar penal possui contornos dogmáticos expressivos:
- *Evasão Mediante Violência contra a Pessoa (artigo 352)*: sanciona a fuga ou tentativa de fuga empreendida pelo próprio detento **mediante o emprego exclusivo de violência física corporal contra guardas ou agentes**. Consoante a doutrina unânime, **a fuga passiva ou com rompimento de obstáculos físicos (serrar grades, escavar túneis) consubstancia fato penalmente atípico**, resolvendo-se administrativamente como falta disciplinar de natureza grave na Lei de Execução Penal;
- *Arrebatamento de Preso (artigo 353)*: pune a conduta de terceiros externos que atacam comboios ou postos de custódia para retirar violentamente a pessoa presa da custódia do Estado.

### Patrocínio infiel e tergiversação (artigo 355)
O dever fiduciário de lealdade que norteia a atuação do advogado é penalmente protegido:
- *Patrocínio Infiel*: pune com detenção de seis meses a três anos o procurador judicial que atraiçoa deliberadamente o interesse profissional do constituinte, gerando-lhe gravame patrimonial ou jurídico na lide;
- *Patrocínio Simultâneo ou Sucessivo (parágrafo único)*: pune a conduta do patrono que defende interesses antagônicos e inconciliáveis de partes opostas no mesmo processo (tergiversação).

### Para fixar
- O favorecimento pessoal protege o criminoso contra a captura policial da justiça.
- A escusa absolutória por parentesco do art. 348 beneficia cônjuges, ascendentes, descendentes e irmãos.
- O favorecimento real assegura o proveito patrimonial do crime e não admite escusa familiar.
- O art. 349-A reprime a introdução de aparelhos de comunicação móvel em estabelecimentos penais.
- A evasão de preso sem emprego de agressão física contra pessoas é conduta penalmente atípica.
- Romper grades ou escavar túneis na fuga prisional consubstancia falta grave disciplinar na LEP.
- O arrebatamento de preso (art. 353) consubstancia crime de terceiros contra a escolta de guarda.
- O patrocínio infiel tutela a lealdade da defesa processual exercida por advogados e procuradores.""",
        "synthetic": [
            "**Favorecimento Pessoal (art. 348)**: auxílio material prestado ao criminoso foragido visando frustrar a sua prisão preventiva ou definitiva.",
            "**Escusa Absolutória de Sangue**: imunidade penal legal irrenunciável que protege ascendentes, irmãos e cônjuges contra punição no art. 348.",
            "**Favorecimento Real (art. 349)**: salvaguarda clandestina do proveito financeiro do crime vedada a incidência de qualquer escusa de parentesco.",
            "**Aparelhos no Presídio (art. 349-A)**: tipificação especial repressora do contrabando interno de chips e baterias para o ambiente penitenciário.",
            "**Evasão Violenta (art. 352)**: criminalização da fuga carcerária realizada exclusivamente mediante agressão física direcionada contra o guarda.",
            "**Atipicidade da Fuga Limpa**: ausência de crime na evasão desprovida de violência pessoal resolvendo-se por falta disciplinar executória.",
            "**Arrebatamento de Preso (art. 353)**: investida violenta perpetrada por terceiros para resgatar comparsas submetidos a custódia legítima.",
            "**Tergiversação Processual**: patrocínio simultâneo espúrio de interesses contraditórios entre litigantes adversos no mesmo feito judicial."
        ]
    })

    return items, summaries
