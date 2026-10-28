# -*- coding: utf-8 -*-
"""Part 2 for a08: s04, s05 (Majorantes Aduaneiras, Documentos, Sonegação Previdenciária e Licitações)."""

def get_part2_data(get_fp):
    items = []
    summaries = []

    # -------------------------------------------------------------
    # SEGMENT 04: Majorantes, Editais e Documentos Oficiais (p. 38-45)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a08/s04",
        "bizu": {
            "summary": [
                "**Majorante Aduaneira em Dobro**: aplicação da reprimenda penal duplicada quando o descaminho ou contrabando são cometidos por meio aéreo, fluvial ou marítimo.",
                "**Finalidade da Qualificadora**: reprimir a maior capacidade de evasão e o volume de mercadorias introduzidas por embarcações e aeronaves em relação a vias terrestres.",
                "**Fraude de Concorrência (revogado art. 335)**: a conduta foi reposicionada na Nova Lei de Licitações nos artigos 337-I e 337-K do Código Penal.",
                "**Inutilização de Edital ou Sinal (art. 336)**: rasgar, conspurcar ou destruir edital oficial afixado por autoridade ou romper lacre/selo público legalmente empregado.",
                "**Subtração de Livro ou Documento (art. 337)**: subtrair ou inutilizar processo judicial, documento oficial ou livro sob custódia de cartório, procurador ou advogado.",
                "**Diferença do Art. 314**: o art. 314 é crime funcional praticado pelo próprio servidor guardião; o art. 337 é cometido por particular ou advogado que acessa os autos.",
                "**Caráter Subsidiário Expressa do Art. 337**: incide apenas se o fato praticado não consubstanciar crime punido com reprimenda penal mais gravosa.",
                "**Dano Qualificado em Prédio Público**: a depredação violenta de bens e editais em sedes administrativas atrai as qualificadoras do crime de dano patrimonial."
            ],
            "teoria": [
                {
                    "statement": "O advogado que subtrai autos judiciais confiados em carga regular para impedir julgamento desfavorável comete o crime do art. 337 do CP.",
                    "isTrue": True,
                    "explanation": "O art. 337 comina pena ao particular ou procurador que subtrai ou destrói processo legalmente confiado à sua custódia processual."
                },
                {
                    "statement": "A conduta de romper lacre oficial colocado pela fiscalização sanitária em estabelecimento interditado amolda-se ao artigo 336 do CP.",
                    "isTrue": True,
                    "explanation": "O art. 336 pune expressamente quem viola, inutiliza ou rompe selo ou sinal empregado por determinação legal de autoridade pública."
                },
                {
                    "statement": "A aplicação da sanção duplicada no transporte aéreo de contrabando restringe-se aos casos em que a aeronave pertence a empresa pública estatal.",
                    "isTrue": False,
                    "explanation": "A majorante do § 3º do art. 334-A incide objetivamente sobre qualquer meio de transporte aéreo, marítimo ou fluvial, público ou privado."
                },
                {
                    "statement": "A revogação do artigo 335 do Código Penal pela Lei 14.133/2021 gerou descriminalização irrestrita das fraudes em concorrências públicas.",
                    "isTrue": False,
                    "explanation": "Houve continuidade normativo-típica, sendo as condutas licitatórias transladadas para o novo capítulo dos artigos 337-E a 337-P do CP."
                }
            ],
            "revisao": [
                {
                    "statement": "O crime de inutilização de edital ou sinal funcional comina sanção punitiva severa inafiançável de reclusão fechada superior a quatro anos.",
                    "isTrue": False,
                    "explanation": "O art. 336 constitui infração penal de menor potencial ofensivo, apenada com detenção de um mês a um ano ou simples pena de multa."
                },
                {
                    "statement": "O servidor público do cartório que destrói livro oficial de que tem a guarda funcional própria responde pelo crime do art. 314 e não pelo art. 337.",
                    "isTrue": True,
                    "explanation": "O art. 314 é crime funcional próprio praticado pelo funcionário custodiante; o art. 337 incide quando a subtração for perpetrada por particular."
                },
                {
                    "statement": "A inutilização parcial de edital que não compromete a legibilidade essencial do aviso afasta a tipicidade material por insignificância.",
                    "isTrue": False,
                    "explanation": "A jurisprudência veda a insignificância quando a integridade do ato administrativo formal de intimação pública resta diretamente desafiada."
                },
                {
                    "statement": "O transporte marítimo clandestino de mercadorias proibidas enseja a incidência da exasperação de metade sobre a pena privativa de liberdade.",
                    "isTrue": False,
                    "explanation": "O art. 334-A, § 3º, determina a aplicação da pena em dobro para o transporte marítimo, e não apenas o acréscimo fracionário de metade."
                }
            ],
            "pointers": [
                {"topic": "Majorante de modal aéreo e marítimo no descaminho e contrabando", "pageRef": 38},
                {"topic": "Transição dos crimes licitatórios para o art. 337-I e 337-K", "pageRef": 40},
                {"topic": "Inutilização de editais e sinais oficiais no art. 336", "pageRef": 42},
                {"topic": "Subtração de autos e documentos pelo particular no art. 337", "pageRef": 44}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a08/s04",
        "fingerprint": get_fp("direito-penal/a08/s04"),
        "analytic": """Este segmento aborda as causas de exasperação punitiva incidentes sobre o transporte aduaneiro qualificado, a migração topográfica dos tipos penais licitatórios sob a Nova Lei de Licitações e os crimes contra a fidelidade de editais, sinais de custódia e autos processuais.

### Majorantes aduaneiras pelo meio de transporte utilizado
O legislador penal estabeleceu um agravamento expressivo nas penas cominadas aos crimes de descaminho (artigo 334, § 3º) e contrabando (artigo 334-A, § 3º):
- *Aplicação da Pena em Dobro*: a sanção privativa de liberdade cominada na modalidade simples **aplica-se em dobro** caso a infração aduaneira seja consumada com o emprego de transporte aéreo, marítimo ou fluvial;
- *Razão de Política Criminal*: a utilização de modais aquáticos e aéreos confere maior capacidade de elisão fiscal e circulação em larga escala de cargas clandestinas, dificultando a interceptação e o controle aduaneiro rotineiro pelas autoridades de fronteira da Polícia Federal e da Receita Federal do Brasil.

### A transição dos crimes de licitação (artigo 335 revogado)
O antigo preceito do artigo 335 do Código Penal reprovava o impedimento, perturbação ou fraude de atos de concorrência pública promovidos pelo Estado:
- *Revogação pela Lei nº 14.133/2021*: com a edição da Nova Lei de Licitações e Contratos Administrativos, o artigo 335 foi formalmente revogado;
- *Continuidade Normativo-Típica*: as condutas desleais de conluio, frustração e fraude competitiva foram modernizadas e alocadas no novel Capítulo II-B do Título XI, sob as tipificações autônomas dos artigos 337-I (frustração do caráter competitivo de licitação) e 337-K (afastamento de licitante), preservando a plena punibilidade penal dos atos com respostas sancionatórias mais robustas.

### Crimes contra a custódia de editais e autos oficiais (artigos 336 e 337)
A preservação da solenidade dos atos estatais conta com proteções específicas:
- *Inutilização de Edital ou de Sinal (artigo 336)*: tutela a eficácia comunicativa e coercitiva dos avisos oficiais. Pune com detenção de um mês a um ano ou multa quem rasga, desfigura ou inutiliza editais públicos afixados por ordem legal de autoridade, bem como quem quebra ou viola selos, lacres e amarras postos pela fiscalização sanitária, fazendária ou ambiental;
- *Subtração ou Inutilização de Livro ou Documento (artigo 337)*: sanciona a conduta do particular, procurador ou advogado que subtrai, oculta ou inutiliza livro oficial, processo administrativo ou autos judiciais confiados legalmente à sua guarda;
- *Distinção Subjetiva com o Artigo 314*: caso o autor da retenção ou destruição dos autos seja o próprio servidor cartorário ou funcionário que detinha o encargo funcional de custodiá-los, a imputação desloca-se imperativamente para o artigo 314 (crime funcional), restando o artigo 337 vocacionado a particulares e causídicos em carga processual.

### Para fixar
- As sanções do contrabando e do descaminho dobram na hipótese de uso de transporte marítimo ou aéreo.
- O maior potencial de escoamento e difícil fiscalização fundamentam o gravame do modal aéreo.
- A revogação do antigo art. 335 operou migração tópica para os novos artigos 337-I e 337-K do CP.
- O art. 336 pune quem destrói editais públicos ou viola lacres e selos fixados pela fiscalização.
- O art. 337 sanciona a retenção ou subtração dolosa de processos ou documentos por advogados e civis.
- Se a subtração documental for cometida pelo servidor público guardião, comete-se o art. 314.
- A violação de edital ou sinal constitui infração penal submetida aos juizados especiais criminais.
- O dano patrimonial qualificado concorre caso haja depredação violenta de bens materiais do Estado.""",
        "synthetic": [
            "**Duplicação Aduaneira**: aplicação de penas dobradas ante o uso clandestino de vetores aéreos, fluviais ou marítimos de transporte.",
            "**Ratio da Qualificadora**: repressão proporcional à alta evasão e sofisticação de rotas que desafiam a vigilância aduaneira ordinária.",
            "**Translação de Concorrências**: acomodação dos tipos licitatórios nos artigos 337-I e 337-K do Código Penal moderno.",
            "**Proteção de Selos (art. 336)**: tutela sancionatória contra a ruptura de lacres e depredação de editais ordenados pela autoridade.",
            "**Subtração Processual (art. 337)**: reprovação penal incidente sobre particulares ou causídicos que desviam autos judiciais sob carga.",
            "**Confronto Funcional**: condutas idênticas praticadas pelo servidor público titular da custódia documental tipificam o art. 314 do estatuto.",
            "**Natureza Subsidiária**: aplicação do art. 337 condicionada à inexistência de delito formalizado com sanção de superior severidade.",
            "**Tutela da Função Judiciária**: garantia de incolumidade probatória indispensável à prestação jurisdicional e processos estatais."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 05: Sonegação Previdenciária e Crimes Residuais (p. 46-57)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a08/s05",
        "bizu": {
            "summary": [
                "**Sonegação de Tributo Social (art. 337-A)**: elisão fraudulenta ou diminuição ilícita de encargo previdenciário obrigatório e seus acréscimos por meio de manipulação contábil em livros oficiais.",
                "**Distinção do Art. 168-A (Apropriação Indébita)**: no art. 168-A desconta-se e deixa-se de repassar; no art. 337-A há fraude e sonegação omissiva na contabilidade.",
                "**Natureza de Crime Material**: o art. 337-A consubstancia crime material que exige efetivo prejuízo tributário e encerramento de lançamento administrativo fiscal.",
                "**Súmula Vinculante 24 do STF**: a tipificação material depende da conclusão do procedimento administrativo fiscal definitivo de lançamento do crédito.",
                "**Extinção da Punibilidade pelo Pagamento (§ 1º)**: se o agente confessa e quita integralmente os débitos previdenciários antes do início da ação fiscalizatória.",
                "**Perdão Judicial Facultativo (§ 2º)**: faculta-se ao juiz deixar de aplicar a pena ou aplicar só multa se o réu é primário e o débito for inferior ao mínimo fiscal.",
                "**Princípio da Insignificância Previdenciária**: aplicável segundo os tribunais superiores quando o valor sonegador não ultrapassa vinte mil reais.",
                "**Concurso de Crimes**: a falsificação contábil com o propósito único de sonegar contribuições resta absorvida pelo crime-fim do art. 337-A (princípio da consunção)."
            ],
            "teoria": [
                {
                    "statement": "O crime de sonegação de contribuição previdenciária (art. 337-A) consuma-se formalmente antes da constituição definitiva do crédito tributário.",
                    "isTrue": False,
                    "explanation": "Por se tratar de crime material tributário, a consumação reclama o prévio encerramento da esfera fiscal (Súmula Vinculante 24 do STF)."
                },
                {
                    "statement": "A quitação espontânea integral dos tributos previdenciários devidos realizada antes da ação fiscalizadora extingue a punibilidade.",
                    "isTrue": True,
                    "explanation": "O art. 337-A, § 1º, prevê expressamente a extinção da punibilidade caso o pagamento integral anteceda o início da fiscalização administrativa."
                },
                {
                    "statement": "O delito do artigo 168-A difere do artigo 337-A porque na apropriação indébita o valor foi retido da remuneração e não repassado ao INSS.",
                    "isTrue": True,
                    "explanation": "No art. 168-A há omissão de repasse do valor descontado dos trabalhadores; no art. 337-A há ocultação fraudulenta na contabilidade da empresa."
                },
                {
                    "statement": "O princípio da insignificância é inaplicável à sonegação previdenciária em virtude da indisponibilidade patrimonial absoluta do erário.",
                    "isTrue": False,
                    "explanation": "O STF e STJ consolidaram a aplicação da insignificância para débitos previdenciários não superiores a vinte mil reais, parâmetro federal."
                }
            ],
            "revisao": [
                {
                    "statement": "O parcelamento tributário formal deferido antes do recebimento da denúncia acarreta a suspensão da pretensão punitiva estatal.",
                    "isTrue": True,
                    "explanation": "O deferimento regular do parcelamento tributário previdenciário enseja a suspensão da prescrição e do curso da persecução criminal."
                },
                {
                    "statement": "No artigo 337-A do Código Penal, a simples confissão do débito perante a autoridade fiscal sem pagamento extingue a punibilidade.",
                    "isTrue": False,
                    "explanation": "A lei exige cumulativamente declarar, confessar e efetuar o pagamento integral dos valores devidos para obter a extinção punitiva."
                },
                {
                    "statement": "O juiz pode aplicar exclusivamente a sanção de multa na hipótese de o agente ser primário e o débito for inferior ao limite de execução fiscal.",
                    "isTrue": True,
                    "explanation": "O § 2º do art. 337-A faculta a concessão de perdão judicial ou aplicação isolada de multa mediante preenchimento dos requisitos legais."
                },
                {
                    "statement": "O crime de sonegação de contribuição previdenciária admite a modalidade culposa praticada por negligência do setor de contabilidade.",
                    "isTrue": False,
                    "explanation": "O art. 337-A exige dolo estrito direcionado a suprimir ou reduzir a contribuição social devida, inexistindo figura culposa típica."
                }
            ],
            "pointers": [
                {"topic": "Sonegação de contribuição previdenciária e núcleos do art. 337-A", "pageRef": 47},
                {"topic": "Distinção da apropriação indébita e aplicação da Súmula Vinculante 24", "pageRef": 50},
                {"topic": "Extinção da punibilidade pelo pagamento e parcelamento", "pageRef": 53},
                {"topic": "Perdão judicial, insignificância e absorção pelo crime-fim", "pageRef": 55}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a08/s05",
        "fingerprint": get_fp("direito-penal/a08/s05"),
        "analytic": """Este segmento finaliza a temática dos crimes de particulares contra a Administração Pública analisando a disciplina jurídica da sonegação de contribuição previdenciária positivada no artigo 337-A do Código Penal, suas causas extintivas de punibilidade, o confronto dogmático com o artigo 168-A e os parâmetros jurisprudenciais de bagatela.

### Estrutura típica da sonegação previdenciária (artigo 337-A)
Introduzido no estatuto repressivo pela Lei nº 9.983/2000, o artigo 337-A comina pena de **reclusão de dois a cinco anos e multa** para quem suprime ou reduz contribuição social previdenciária e qualquer de seus acessórios, mediante a prática de manobras fraudulentas:
1. Omissão dolosa de nomes de segurados, remunerações ou receitas em folhas de pagamento e relatórios oficiais transmitidos aos órgãos previdenciários;
2. Inserção fraudulenta de dados inverídicos ou omissão proposital de receitas e operações contábeis nos livros e demonstrativos exigidos pela legislação;
3. Omissão de fatos geradores de contribuições em guias de recolhimento oficial.

### Distinção dogmática nodal: artigo 337-A versus artigo 168-A
A doutrina e a jurisprudência fixam a separação precisa entre os ilícitos penais previdenciários:
- *Apropriação Indébita Previdenciária (artigo 168-A)*: é **crime formal e omissivo próprio**. O gestor deduz e desconta a contribuição diretamente da remuneração salarial dos empregados ou terceiros e simplesmente não repassa os valores recolhidos aos cofres da Previdência Social no prazo legal;
- *Sonegação de Contribuição Previdenciária (artigo 337-A)*: é **crime material e comissivo/omissivo fraudulento**. A empresa não desconta ou oculta a existência da relação empregatícia ou da folha de salários, sonegando e ludibriando o Fisco. Em razão de sua natureza material, incide plenamente o postulado da **Súmula Vinculante 24 do Supremo Tribunal Federal**, sendo indispensável o exaurimento do processo administrativo fiscal com a constituição definitiva do débito para viabilizar a persecução penal.

### Extinção da punibilidade, perdão judicial e insignificância
O tratamento sancionatório confere relevo destacado à recuperação do crédito fiscal:
- *Extinção da Punibilidade pelo Pagamento (§ 1º)*: extingue-se a punibilidade do infrator caso este, de maneira espontânea, declare, confesse e realize a liquidação integral dos valores e contribuições devidas antes do início de qualquer procedimento fiscalizatório promovido pela fiscalização;
- *Perdão Judicial e Multa Isolada (§ 2º)*: é facultado ao magistrado conceder perdão judicial ou cominar unicamente a pena de multa se o réu ostentar primariedade, bons antecedentes e o montante sonegador não ultrapassar o piso legalmente exigido para ajuizamento de execuções fiscais federais;
- *Princípio da Insignificância*: o Superior Tribunal de Justiça e o STF admitem o trancamento da persecução penal mediante a incidência do princípio da insignificância caso o débito previdenciário consolidado não ultrapasse vinte mil reais, consoante parâmetro vigente na execução fiscal.

### Para fixar
- O art. 337-A pune a supressão ou redução fraudulenta de contribuições previdenciárias devidas.
- Diferencia-se do art. 168-A porque na apropriação ocorre desconto real e retenção sem repasse.
- A sonegação previdenciária é crime material que exige constituição definitiva do crédito (SV 24).
- O pagamento integral espontâneo anterior ao início da ação fiscal extingue a punibilidade.
- O parcelamento deferido do débito previdenciário opera a suspensão da pretensão punitiva penal.
- O perdão judicial ou multa isolada pode incidir para débitos inferiores ao mínimo da execução.
- O princípio da insignificância material incide para valores sonegados de até vinte mil reais.
- A falsidade contábil orientada exclusivamente à sonegação é absorvida pelo crime tributário.""",
        "synthetic": [
            "**Sonegação Previdenciária (art. 337-A)**: supressão ou redução dolosa de tributos sociais cominando reclusão balizada de dois a cinco anos.",
            "**Natureza Material**: delito causal que exige dano financeiro efetivo e lançamento fiscal consumado sob o crivo da Súmula Vinculante 24.",
            "**Distinção da Apropriação**: o art. 168-A pune o não repasse de valores descontados; o art. 337-A reprime a ocultação fraudulenta contábil.",
            "**Extinção pelo Pagamento**: adimplemento integral e confissão antecedentes ao início da auditoria fiscal extinguem a punibilidade penal.",
            "**Suspensão por Parcelamento**: adesão regular a programas de parcelamento fiscal suspende a persecução penal e a contagem prescricional.",
            "**Perdão Judicial Condicionado**: faculdade judicial de dispensar pena privativa para réus primários sob débito inferior ao teto executório.",
            "**Aplicação da Bagatela**: admissão jurisprudencial da insignificância sob baliza quantitativa fixada em até vinte mil reais.",
            "**Consunção Contábil**: absorção de fraudes documentais instrumentais pelo crime-fim tributário na hipótese de contexto fático unificado."
        ]
    })

    return items, summaries
