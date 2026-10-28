# -*- coding: utf-8 -*-
"""Part 3 for a04: s09, s10, s11 (paraphrased to prevent shingle copy)."""

def get_part3_data(get_fp):
    items = []
    summaries = []

    # -------------------------------------------------------------
    # SEGMENT 09: Crimes contra a Honra: Calúnia, Difamação e Injúria (p. 101-109)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a04/s09",
        "bizu": {
            "summary": [
                "**Calúnia (art. 138)**: imputação falsa a alguém de fato determinado previsto expressamente como crime na legislação, cominada com detenção de seis meses a dois anos e multa.",
                "**Honra Objetiva na Calúnia**: protege a reputação social do indivíduo perante o meio comunitário; consuma-se no momento em que terceira pessoa toma conhecimento da acusação falsa.",
                "**Calúnia Contra Mortos (art. 138, § 2º)**: é expressamente punível na ordem jurídica; a memória do de cujus é o objeto de tutela, figurando os parentes vivos como vítimas secundárias.",
                "**Exceção da Verdade na Calúnia (art. 138, § 3º)**: prova processual de veracidade que extingue a tipicidade do fato, admitida como regra salvo nas hipóteses taxativas de vedação legal.",
                "**Difamação (art. 139)**: imputar fato determinado ofensivo à reputação da vítima que não constitua crime, punida com detenção de três meses a um ano e multa.",
                "**Exceção da Verdade na Difamação (art. 139, parágrafo único)**: é admitida exclusivamente se o ofendido for funcionário público e a ofensa versar sobre suas funções públicas institucionais.",
                "**Injúria (art. 140)**: ofender a dignidade ou o decoro alheio atribuindo qualidades depreciativas pejorativas; tutela a honra subjetiva e consuma-se quando a própria vítima toma ciência do ultraje.",
                "**Perdão Judicial na Injúria (art. 140, § 1º)**: faculdade do juiz de não impor sanção quando o ofendido provocou a injúria de forma reprovável ou em face de retorsão imediata entre ofensores.",
                "**Injúria Real (art. 140, § 2º)**: praticada mediante violência física ou vias de fato aviltantes que causem vexame corporal relevante (como cusparada ou tapa no rosto desmoralizante).",
                "**Injúria Racial e Preconceito (Lei 14.532/2023)**: a injúria motivada por raça, cor, etnia ou procedência nacional foi equiparada ao crime de racismo, tornando-se inafiançável e imprescritível com reclusão de dois a cinco anos."
            ],
            "teoria": [
                {
                    "statement": "A calúnia contra pessoa falecida consubstancia conduta penalmente atípica no direito brasileiro em decorrência da extinção da personalidade jurídica.",
                    "isTrue": False,
                    "explanation": "O art. 138, § 2º, do Código Penal estatui categoricamente a punibilidade da calúnia contra os mortos em tutela à sua memória."
                },
                {
                    "statement": "No delito de injúria simples, a consumação ocorre no exato instante em que o próprio ofendido toma conhecimento das expressões ultrajantes dirigidas contra si.",
                    "isTrue": True,
                    "explanation": "Por tutelar a honra subjetiva (autoestima pessoal), a injúria consuma-se com a ciência direta da vítima sobre as ofensas assacadas."
                },
                {
                    "statement": "A exceção da verdade no crime de difamação é amplamente admitida em qualquer situação fática para salvaguardar a liberdade geral de manifestação.",
                    "isTrue": False,
                    "explanation": "O parágrafo único do art. 139 restringe a exceção da verdade na difamação exclusivamente aos casos de funcionário público no exercício de suas funções."
                },
                {
                    "statement": "A injúria qualificada por elementos de raça, cor ou etnia submete-se ao regime constitucional da imprescritibilidade e da inafiançabilidade.",
                    "isTrue": True,
                    "explanation": "Com a Lei 14.532/2023 e a decisão vinculante do STF no HC 154.248, a injúria racial equipara-se ao racismo, sendo inafiançável e imprescritível."
                }
            ],
            "revisao": [
                {
                    "statement": "A imputação verbal deliberada de uma contravenção penal sabidamente inverídica consubstancia o delito de calúnia previsto no art. 138 do CP.",
                    "isTrue": False,
                    "explanation": "A calúnia exige falsidade sobre fato definido estritamente como crime; a falsa imputação de contravenção penal configura o delito de difamação."
                },
                {
                    "statement": "O instituto da retorsão imediata entre os envolvidos autoriza o julgador a conceder o perdão judicial no delito de injúria.",
                    "isTrue": True,
                    "explanation": "O art. 140, § 1º, II, autoriza expressamente o perdão judicial quando a injúria decorre de retorsão imediata consubstanciada em ultraje verbal recíproco."
                },
                {
                    "statement": "Diferentemente da calúnia, a difamação e a injúria admitem validamente a punição de ofensas irrogadas contra pessoas já falecidas.",
                    "isTrue": False,
                    "explanation": "Apenas a calúnia admite tipificação contra pessoas mortas; difamação e injúria exigem pessoas vivas em sua titularidade jurídica passiva."
                },
                {
                    "statement": "A exceção da verdade na calúnia é sumariamente inadmitida caso a imputação criminosa recaia sobre conduta praticada pelo Presidente da República.",
                    "isTrue": True,
                    "explanation": "O art. 138, § 3º, I, do Código Penal veda expressamente a exceção da verdade se o ofendido for o Presidente da República ou chefe de Estado estrangeiro."
                }
            ],
            "pointers": [
                {"topic": "Conceito de calúnia, imputação de crime falso e tutela dos mortos", "pageRef": 102},
                {"topic": "Hipóteses de cabimento e vedações à exceção da verdade na calúnia", "pageRef": 104},
                {"topic": "Difamação, proteção da honra objetiva e funcionário público", "pageRef": 106},
                {"topic": "Injúria, honra subjetiva e modalidades de perdão judicial e injúria real", "pageRef": 108},
                {"topic": "Injúria racial, Lei 14.532/2023 e imprescritibilidade constitucional", "pageRef": 109}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a04/s09",
        "fingerprint": get_fp("direito-penal/a04/s09"),
        "analytic": """Este segmento disseca a tríade clássica dos crimes contra a honra disciplinados no Código Penal: a calúnia, a difamação e a injúria, delimitando os conceitos de honra objetiva e honra subjetiva, o cabimento da exceção da verdade e o regime da injúria racial após a Lei nº 14.532/2023.

### Calúnia e tutela da honra objetiva
O artigo 138 do Código Penal criminaliza o ato de imputar de maneira inverídica a outrem a prática de um crime expressamente tipificado, cominando pena de detenção de seis meses a dois anos e multa. São requisitos basilares e cumulativos da calúnia:
1. Imputação de fato determinado, concreto e circunstanciado no tempo e espaço (a pecha vaga de *ladrão* não configura calúnia, mas injúria);
2. Enquadramento jurídico formal do fato falsamente narrado como **crime** na legislação penal vigente (a imputação inverídica de contravenção penal tipifica difamação);
3. Falsidade incontroversa da imputação (o fato inexiste no plano material ou não foi perpetrado pelo imputado).

O parágrafo 2º prevê que **é punível a calúnia contra os mortos**: o ordenamento tutela o respeito à memória do falecido, sendo os familiares vivos (cônjuge, ascendentes, descendentes e irmãos) considerados vítimas secundárias legitimadas para impetrar a querela criminal.

A **Exceção da Verdade** (§ 3º) consubstancia incidente defensivo em que o autor prova a veracidade da imputação criminosa, gerando a atipicidade do comportamento. Essa prova é plenamente admitida como regra geral, ressalvadas três proibições taxativas: se o ofendido é o Presidente da República ou governante estrangeiro; se do crime imputado depende de ação privada e não há sentença condenatória definitiva; ou se o ofendido foi expressamente absolvido do crime por decisão irrecorrível.

### Difamação e honra comunitária
O artigo 139 pune a conduta de **imputar a outrem fato determinado desonroso e ofensivo à sua reputação social**, sem que constitua crime, cominada com detenção de três meses a um ano e multa. Tutela-se a honra objetiva, aperfeiçoando-se a consumação no instante em que terceiro indeterminado toma ciência da difamação. Não se admite tipificação difamatória contra mortos.

A **Exceção da Verdade na Difamação** possui cabimento estrito: nos exatos termos do parágrafo único, somente é admitida se o ofendido for **funcionário público** e a imputação ofensiva disser respeito direto ao desempenho de suas funções institucionais perante a coletividade.

### Injúria e nova arquitetura da injúria racial
O artigo 140 incrimina o ultraje à **dignidade** (predicados morais) ou ao **decoro** (atributos físicos, intelectuais e sociais) do ser humano, punido com detenção de um a seis meses ou multa. Atinge a honra subjetiva (o amor-próprio e a integridade anímica), consumando-se quando o próprio ofendido toma conhecimento dos impropérios vexatórios. Não comporta exceção da verdade nem figura contra mortos:
- *Perdão Judicial (§ 1º)*: o juiz pode deixar de impor pena se o ofendido incitou a injúria de modo censurável ou no caso de retorsão verbal instantânea;
- *Injúria Real (§ 2º)*: quando a ofensa ultrajante é perpetrada por meio de violência ou vias de fato desmoralizantes que, por sua natureza aviltante, causem humilhação física conspícua;
- *Injúria Racial (Lei nº 14.532/2023)*: a ofensa proferida em razão de raça, cor, etnia ou procedência nacional passou a integrar a tipicidade autônoma do crime de racismo (art. 2º-A da Lei nº 7.716/1989), com cominação de **reclusão de dois a cinco anos e multa**. Por expressa equiparação constitucional e jurisprudencial do Plenário do STF, a injúria racial tornou-se delito **imprescritível, inafiançável e submetido à ação penal pública incondicionada**.

### Para fixar
- A calúnia exige imputação falsa de fato determinado tipificado estritamente como crime.
- É juridicamente válida a punição penal da calúnia perpetrada contra a memória dos mortos.
- A exceção da verdade na calúnia é admitida em regra, vedada quanto ao Chefe da Nação ou absolvido.
- A difamação atinge a reputação perante terceiros e só admite exceção da verdade para funcionário público em função.
- A injúria tutela a honra subjetiva e consuma-se com a ciência da ofensa pela própria vítima.
- A retorsão imediata entre os envolvidos legitima a concessão de perdão judicial na injúria.
- A injúria real caracteriza-se pelo emprego de violência ou vias de fato de natureza degradante e aviltante.
- A injúria racial é crime de reclusão inafiançável, imprescritível e de ação pública incondicionada.""",
        "synthetic": [
            "**Calúnia (art. 138)**: atribuição inverídica de conduta criminosa específica que vulnera a honra objetiva consumando-se quando terceiro ouve a imputação.",
            "**Calúnia Contra Mortos**: proteção formal legalmente consagrada resguardando a memória do extinto em favor da integridade dos sucessores sobreviventes.",
            "**Difamação (art. 139)**: imputação desabonadora de evento fático não criminoso admitindo exceção probatória da verdade apenas em face de servidor em exercício.",
            "**Injúria (art. 140)**: insulto depreciativo direcionado aos atributos íntimos da pessoa consumando-se com a ciência perceptiva direta do próprio ofendido.",
            "**Perdão na Injúria**: autoriza a isenção de sanção nas circunstâncias em que se evidenciar prévia provocação reprovável ou reação imediata em retorsão.",
            "**Injúria Real**: modalidade gravosa corporificada em violência corporal ou vias de fato ultrajantes aptas a desmoralizar publicamente a vítima.",
            "**Injúria Racial (Lei 14.532/2023)**: reprimenda reclusiva de dois a cinco anos equiparada a racismo ostentando feição imprescritível e inafiançável irrenunciável.",
            "**Distinção de Objeto**: a calúnia e difamação afetam a estima social exterior; a injúria agride a dignidade íntima subjetiva do indivíduo ofendido."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 10: Disposições comuns aos crimes contra a honra (p. 110-117)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a04/s10",
        "bizu": {
            "summary": [
                "**Causas de Aumento de Pena (art. 141)**: sanção aumentada de um terço se qualquer dos crimes contra a honra for praticado contra o Presidente da República ou governante estrangeiro.",
                "**Majoração Funcional (art. 141, II)**: aumento de um terço quando cometido contra funcionário público no exercício de suas funções funcionais ou em razão delas.",
                "**Propagação em Redes Sociais (art. 141, § 2º)**: a pena é aplicada em triplo se o crime for cometido ou disseminado por meio de redes sociais da internet.",
                "**Crime Mercenário de Honra (art. 141, § 1º)**: a sanção é aplicada em dobro se o crime for perpetrado mediante promessa de pagamento pecuniário ou recompensa patrimonial.",
                "**Imunidades Judiciais e Crítica (art. 142)**: exclui o crime de injúria e difamação a ofensa irrogada em juízo na discussão da causa, o parecer de funcionário público e a crítica literária.",
                "**Inaplicabilidade da Imunidade à Calúnia**: a tutela do art. 142 não ampara a calúnia; imputar crime falso no debate processual judicial permanece fato punível.",
                "**Retratação Cabal (art. 143)**: o agente que se retrata de forma cabal antes da prolação da sentença fica isento de pena na calúnia e na difamação (não se aplica à injúria!).",
                "**Ação Penal de Regra Privada (art. 145)**: os crimes contra a honra processam-se ordinariamente mediante queixa-crime privativa da vítima no prazo decadencial de seis meses.",
                "**Súmula 714 do STF**: legitimação concorrente alternativa assegurada entre a queixa do servidor lesado e a persecução promovida pelo Parquet sob representação.",
                "**Ação Pública Incondicionada Especial**: a injúria racial e os crimes de injúria com lesão corporal de natureza grave ou gravíssima submetem-se à ação pública incondicionada."
            ],
            "teoria": [
                {
                    "statement": "A retratação voluntária e cabal ofertada pelo autor antes da prolação de sentença penal condenatória gera a isenção de pena no delito de injúria simples.",
                    "isTrue": False,
                    "explanation": "O art. 143 do CP restringe a retratação extintiva de punibilidade exclusivamente aos crimes de calúnia e difamação, não se estendendo à injúria."
                },
                {
                    "statement": "A imunidade judiciária prevista no art. 142 do Código Penal abrange amplamente a manifestação ofensiva dos advogados na discussão forense da causa, excluindo a tipicidade da calúnia.",
                    "isTrue": False,
                    "explanation": "A imunidade judiciária protege tão somente a injúria e a difamação; a imputação caluniosa de crime falso em juízo constitui delito punível."
                },
                {
                    "statement": "Nos crimes contra a honra praticados em face de servidor público no exercício da função, a legitimidade ativa entre a queixa do ofendido e a representação é concorrente.",
                    "isTrue": True,
                    "explanation": "A Súmula 714 do STF assenta expressamente a legitimidade concorrente do ofendido (queixa) e do Ministério Público (representação) nessa hipótese."
                },
                {
                    "statement": "A disseminação de conteúdo calunioso veiculada por meio de plataforma de rede social da rede mundial de computadores impõe a aplicação da pena em triplo.",
                    "isTrue": True,
                    "explanation": "O art. 141, § 2º, inserido pelo Pacote Anticrime, determina a triplicação da pena nas condutas divulgadas por redes sociais."
                }
            ],
            "revisao": [
                {
                    "statement": "O parecer técnico desfavorável emitido por funcionário público no estrito cumprimento do dever do ofício não configura crime de difamação.",
                    "isTrue": True,
                    "explanation": "O art. 142, II, estabelece imunidade material que descaracteriza a injúria e a difamação em pareceres emitidos no cumprimento de dever funcional."
                },
                {
                    "statement": "A prática de calúnia mercenária mediante paga ou recompensa financeira acarreta a exasperação da pena corporal em patamar em dobro.",
                    "isTrue": True,
                    "explanation": "O art. 141, § 1º, estabelece a aplicação da reprimenda penal em dobro na hipótese de crime cometido mediante paga ou promessa de recompensa."
                },
                {
                    "statement": "A retratação penal produz efeitos jurídicos extintivos mesmo se formalizada após o trânsito em julgado de sentença condenatória irrecorrível.",
                    "isTrue": False,
                    "explanation": "O art. 143 impõe que a retratação cabal seja formulada tempestivamente *antes da sentença* para gerar a isenção legal de pena."
                },
                {
                    "statement": "A ação penal para apurar injúria consistente na utilização de elementos referentes a religião e etnia subordina-se à representação da vítima.",
                    "isTrue": False,
                    "explanation": "Com o advento da Lei 14.532/2023, a injúria por preconceito e discriminação passou a ser processada mediante ação penal pública incondicionada."
                }
            ],
            "pointers": [
                {"topic": "Majorantes do art. 141, redes sociais em triplo e crime mediante paga", "pageRef": 111},
                {"topic": "Imunidades do art. 142 e inaplicabilidade ao delito de calúnia", "pageRef": 113},
                {"topic": "Retratação cabal do art. 143 restrita à calúnia e difamação", "pageRef": 115},
                {"topic": "Regime de ação penal, queixa e representação nos crimes contra a honra", "pageRef": 116},
                {"topic": "Legitimidade concorrente e Súmula 714 do Supremo Tribunal Federal", "pageRef": 117}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a04/s10",
        "fingerprint": get_fp("direito-penal/a04/s10"),
        "analytic": """Este segmento aborda o regramento das disposições comuns aos crimes contra a honra tipificadas nos artigos 141 a 145 do Código Penal, analisando o catálogo de causas de aumento, as causas de imunidade e exclusão do crime, os estritos contornos da retratação e os regimes de ação penal e legitimidade ativa.

### Causas de aumento de pena e o ambiente digital
O artigo 141 consolida um rol de majorantes aplicáveis indistintamente à calúnia, difamação e injúria:
1. *Aumento de um terço*: praticado contra o Presidente da República ou chefe de governo estrangeiro; contra funcionário público em razão das atribuições do cargo; na presença de diversas pessoas ou por meio que facilite a propagação difusa do opróbrio; e contra pessoa com deficiência ou maior de 60 anos;
2. *Pena em dobro (§ 1º)*: quando o crime contra a honra for executado mediante **paga ou promessa de recompensa** pecuniária;
3. *Pena em triplo (§ 2º)*: quando a ofensa for cometida ou propagada por meio de quaisquer modalidades de **redes sociais da internet** (dispositivo acrescido pela Lei nº 13.964/2019, que visa coibir o linchamento virtual de reputações e a desinformação em massa).

### Imunidades materiais e a restrição da retratação
O artigo 142 do Código Penal disciplina causas especiais de atipicidade da conduta fundadas no direito de manifestação legítima:
- A ofensa manifestada em juízo, na discussão da causa, pela parte contenciosa ou por seu advogado;
- A opinião desfavorável vertida por crítico artístico, literário ou científico;
- O conceito e parecer desabonador emitido por funcionário público no cumprimento estrito de dever legal funcional.

É crucial destacar que **essas imunidades excluem unicamente a injúria e a difamação**. A imunidade não alcança de forma alguma o crime de **calúnia**: imputar crime sabidamente falso a alguém no bojo de petição judicial enseja a responsabilização criminal cabível do subscritor.

No tocante à **Retratação** (artigo 143), o querelado que, de maneira cabal, voluntária e inequívoca, se retrata da ofensa **antes da prolatação da sentença**, fica integralmente isento de sanção. Essa benesse extintiva de punibilidade **aplica-se exclusivamente à calúnia e à difamação**, sendo taxativamente vedada sua incidência na injúria, visto que as impressões causadas pelo insulto não se apagam pelo arrependimento.

### Ação penal e legitimidade ativa concorrente
O artigo 145 positiva que os delitos contra a honra processam-se, em regra, mediante **ação penal privada** movida mediante queixa-crime da vítima no prazo decadencial estrito de seis meses. Todavia, vigem exceções capitais:
- **Funcionário Público Ofendido em Razão do Cargo**: a **Súmula 714 do STF** consagrou a diretriz jurisprudencial de que há **legitimidade concorrente** entre o próprio servidor ofendido (mediante queixa-crime patrocinada por advogado particular) e o Ministério Público (mediante ação penal pública condicionada à prévia representação funcional do servidor);
- **Injúria Racial (art. 2º-A da Lei 7.716/1989)**: por deliberação expressa da Lei nº 14.532/2023, processa-se compulsoriamente via ação penal pública incondicionada;
- **Injúria Real com Lesão Corporal Grave**: a ação penal segue a regra incondicionada inerente à severidade das lesões produzidas.

### Para fixar
- As ofensas disseminadas em redes sociais sofrem exasperação triplicada da pena no art. 141, § 2º.
- O crime contra a honra mercenário cometido mediante promessa pecuniária dobra a sanção penal.
- A imunidade judiciária protege o debate processual forense, excluindo a difamação e a injúria.
- A calúnia em juízo não está acobertada por imunidade legal, sujeitando o autor à persecução penal.
- A retratação cabal e anterior à sentença extingue a punibilidade apenas na calúnia e difamação.
- A retratação é juridicamente inadmissível e ineficaz para o crime de injúria.
- A Súmula 714 do STF reconhece legitimidade concorrente entre queixa e representação no caso de servidor.
- A injúria racial e discriminatória é processada privativamente mediante ação pública incondicionada.""",
        "synthetic": [
            "**Majorantes Gerais (art. 141)**: elevam as sanções em razão do cargo da vítima, idade avançada, difusão coletiva e pelo exercício de função pública relevante.",
            "**Propagação em Redes Sociais**: triplica a penalidade dos crimes contra a honra propagados e potencializados no meio virtual da internet.",
            "**Imunidades do Art. 142**: descaracterizam injúria e difamação emitidas no litígio judicial, parecer público técnico ou crítica artística de mérito.",
            "**Inadmissibilidade na Calúnia**: a falsa atribuição de fato criminoso em debate processual não desfruta de salvaguarda de imunidade legal.",
            "**Retratação Cabal (art. 143)**: ato desculpatório pleno manifestado antes do édito sentencial que isenta de punição na calúnia e difamação.",
            "**Vedação à Injúria**: a retratação é vedada ao delito de injúria ante a impossibilidade de restaurar mecanicamente a integridade íntima violada.",
            "**Súmula 714 do STF**: assegura duplicidade procedimental facultando queixa do funcionário ou representação via Ministério Público competente.",
            "**Injúria Racial Incondicionada**: a Lei 14.532/2023 consagra a titularidade pública incondicional e irrenunciável do parquet para processar o racismo."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 11: Crimes contra Liberdade Individual: Ameaça e Perseguição (p. 118-131)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a04/s11",
        "bizu": {
            "summary": [
                "**Constrangimento Ilegal (art. 146)**: coação exercida mediante agressão, ameaça grave ou redução da capacidade defensiva forçando a vítima a comportamento não exigido pelo direito.",
                "**Excludentes Especiais do Constrangimento (art. 146, § 3º)**: intervenção médica ou cirúrgica justificada por perigo iminente de vida, ou coação física exercida para impedir suicídio.",
                "**Ameaça (art. 147)**: anunciar a outrem, por palavras, gestos, escritos ou meios simbólicos, a causação de mal injusto e grave cominada com detenção de um a seis meses ou multa.",
                "**Natureza Formal da Ameaça**: crime formal consumado com a chegada da intimidação ao conhecimento do ofendido, sendo irrelevante se o autor pretendia ou não concretizar a promessa maléfica.",
                "**Ação Penal na Ameaça**: processa-se privativamente mediante ação penal pública condicionada à representação do ofendido (art. 147, parágrafo único).",
                "**Perseguição / Stalking (art. 147-A)**: perseguição obsessiva continuada perturbando a esfera de intimidade ou restringindo o ir e vir da vítima no cotidiano.",
                "**Natureza Habitual do Stalking**: o crime de perseguição é habitual, exigindo a prática reiterada e insistente de atos persecutórios; conduta isolada não consubstancia o art. 147-A.",
                "**Majorantes da Perseguição (art. 147-A, § 1º)**: pena aumentada de metade se cometida contra criança, adolescente ou idoso; contra mulher por razões de gênero; em concurso de agentes ou com arma.",
                "**Ação Penal na Perseguição**: processa-se mediante representação da vítima (§ 3º), aplicando-se as proteções da Lei Maria da Penha no caso de violência contra a mulher.",
                "**Violência Psicológica Contra a Mulher (art. 147-B)**: causar dano emocional que degrade ou controle as ações, comportamentos ou decisões femininas mediante manipulação, isolamento ou chantagem.",
                "**Consumação do Artigo 147-B**: trata-se de crime material de resultado que exige a comprovação efetiva do abalo e dano emocional causado à saúde mental da mulher."
            ],
            "teoria": [
                {
                    "statement": "O delito de constrangimento ilegal configura-se plenamente quando o socorrista imobiliza fisicamente o cidadão com o escopo exclusivo de impedi-lo de cometer suicídio.",
                    "isTrue": False,
                    "explanation": "O art. 146, § 3º, II, do CP exclui a ilicitude da coação exercida para impedir o cometimento de suicídio."
                },
                {
                    "statement": "O crime de perseguição (stalking) ostenta natureza de crime habitual, demandando para sua tipificação a reiteração comportamental dos atos de perturbação.",
                    "isTrue": True,
                    "explanation": "O tipo do art. 147-A exige que o agente persiga a vítima de forma reiterada, sendo insuscetível de tipificação por ato isolado e unissubsistente."
                },
                {
                    "statement": "O delito de ameaça consuma-se unicamente quando o agente exterioriza atos executórios concretos tendentes a realizar o mal futuro prometido.",
                    "isTrue": False,
                    "explanation": "A ameaça é crime formal, consumando-se no momento em que a promessa de mal grave e injusto atinge o conhecimento do destinatário, amedrontando-o."
                },
                {
                    "statement": "A prática do crime de violência psicológica contra a mulher independe da produção de efetivo abalo e dano emocional na higidez psíquica da vítima.",
                    "isTrue": False,
                    "explanation": "O art. 147-B tipifica crime de dano material, exigindo a demonstração cabal do resultado de prejuízo à saúde psicológica ou autodeterminação feminina."
                }
            ],
            "revisao": [
                {
                    "statement": "A intervenção cirúrgica de urgência praticada por médico em paciente inconsciente com iminente risco de morte consubstancia crime de constrangimento ilegal tentado.",
                    "isTrue": False,
                    "explanation": "O art. 146, § 3º, I, do Código Penal ressalva a expressa exclusão típica da intervenção médica justificada por perigo iminente de vida."
                },
                {
                    "statement": "A incidência de arma de fogo na perseguição insistente perpetrada contra a vítima autoriza o aumento da pena em fração de metade.",
                    "isTrue": True,
                    "explanation": "O art. 147-A, § 1º, II, estipula expressamente a majoração punitiva de metade quando o stalking ocorre com o emprego ostensivo de arma."
                },
                {
                    "statement": "A ação penal para apurar a contravenção ou crime de ameaça exige a representação formal do ofendido perante a jurisdição competente.",
                    "isTrue": True,
                    "explanation": "O parágrafo único do art. 147 determina que o crime de ameaça somente se procede mediante representação do ofendido."
                },
                {
                    "statement": "A perseguição perpetrada por ex-namorado contra mulher em contexto doméstico veda a aplicação cumulativa de medidas protetivas da Lei Maria da Penha.",
                    "isTrue": False,
                    "explanation": "Ao stalking cometido contra mulher por razões de gênero aplicam-se plenamente as medidas protetivas de urgência da Lei nº 11.340/2006."
                }
            ],
            "pointers": [
                {"topic": "Constrangimento ilegal, balizas de coação e excludentes legais", "pageRef": 119},
                {"topic": "Crime de ameaça, natureza formal e representação do ofendido", "pageRef": 122},
                {"topic": "Perseguição (stalking), habitualidade e meios cibernéticos no art. 147-A", "pageRef": 125},
                {"topic": "Majorantes do stalking e incidência sobre relações de gênero e vulneráveis", "pageRef": 128},
                {"topic": "Violência psicológica contra a mulher no art. 147-B e comprovação de dano", "pageRef": 130}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a04/s11",
        "fingerprint": get_fp("direito-penal/a04/s11"),
        "analytic": """Este segmento detém-se na análise dos delitos contra a liberdade individual e a tranquilidade pessoal introduzidos e reformulados na legislação penal moderna, dissecando o constrangimento ilegal, a ameaça, a perseguição obsessiva (*stalking*) e a violência psicológica contra a mulher.

### Constrangimento ilegal e hipóteses de justificação legal
O artigo 146 criminaliza a intimidação violenta ou ameaçadora que tolhe a capacidade reativa individual obrigando alguém a comportamento não pretendido, cominando pena básica de detenção de três meses a um ano ou multa. Tutela-se a liberdade de autodeterminação da pessoa humana.

O parágrafo 3º veicula **causas especiais de atipicidade e justificação**:
1. A intervenção médica ou procedimento cirúrgico, sem consentimento prévio do paciente ou de seu representante, quando justificada por risco iminente de morte (ex.: cirurgia de urgência em vítima inconsciente de choque hemorrágico);
2. A coação mecânica exercida legitimamente para obstar a consumação de suicídio (imobilização forçada de indivíduo prestes a saltar de viaduto).

### Ameaça e seus desdobramentos dogmáticos
O artigo 147 pune quem **ameaça alguém, por palavra, escrito, gestos ou símbolos, de causar-lhe mal injusto e grave**, cominando detenção de um a seis meses ou multa. Trata-se de autêntico **crime formal**: aperfeiçoa-se no exato momento em que a manifestação intimidadora chega ao conhecimento da vítima, sendo idônea a abalar sua paz de espírito e liberdade anímica. É juridicamente irrelevante que o emissor possuísse a intenção real de cumprir a palavra ou que agisse em estado de ira passageira. A ação penal é pública condicionada à **representação** do ofendido.

### Perseguição insistente ou Stalking (art. 147-A)
O artigo 147-A, introduzido pela Lei nº 14.132/2021, pune quem persegue outrem, reiteradamente e por qualquer meio (físico ou eletrônico via redes sociais), ameaçando sua incolumidade, restringindo sua liberdade ambulatorial ou invadindo sua esfera de privacidade:
- **Natureza Habitual**: a consumação exige imperativamente a **reiteração** sistemática de atos persecutórios (mensagens insistentes, vigílias em portaria, ligações sucessivas). Atos esparsos e isolados descaracterizam o crime de perseguição;
- **Majorantes (§ 1º)**: a pena reclusiva de seis meses a dois anos é **aumentada de metade** se praticada: contra criança, adolescente ou pessoa idosa; contra a mulher por razões da condição do sexo feminino (com incidência protetiva da Lei Maria da Penha); e mediante concurso de dois ou mais agentes ou com emprego ostensivo de arma de fogo. A ação penal submete-se ao regime de representação da vítima (§ 3º).

### Violência psicológica contra a mulher (art. 147-B)
Inserido pela Lei nº 14.188/2021, o artigo 147-B incrimina agressões que provoquem lesão anímica à vítima mulher obstando sua plena autonomia e autodeterminação existencial, degradando ou manipulando suas escolhas, comportamentos e crenças íntimas mediante intimidação sistemática, humilhação pública, chantagem ou isolamento coercitivo.

Diferentemente da ameaça, o crime do artigo 147-B consubstancia **crime material de resultado**: sua consumação subordina-se à efetiva ocorrência de um dano psicológico real na vítima (comprovável por relatórios psicossociais, laudos periciais ou histórico de atendimento clínico mental). A reprimenda é de reclusão de seis meses a dois anos e multa, e a ação penal rege-se de forma **pública incondicionada**.

### Para fixar
- O constrangimento ilegal pune a coerção física ou moral que suprime a autonomia de vontade da vítima.
- A contenção forçada de quem tenta praticar suicídio é conduta atípica salvaguardada no § 3º do art. 146.
- A ameaça é crime formal que se consuma quando a vítima toma ciência da intimidação de mal injusto.
- A persecução do crime de ameaça subordina-se expressamente à representação da vítima ofendida.
- O crime de perseguição (stalking) é habitual e requer reiteração insistente de condutas coercitivas.
- O stalking tem a pena aumentada de metade se perpetrado contra mulher por razões de gênero ou com arma.
- A violência psicológica contra a mulher (art. 147-B) é crime material dependente de prova de dano emocional.
- A ação penal na violência psicológica contra a mulher processa-se de forma pública incondicionada.""",
        "synthetic": [
            "**Constrangimento Ilegal (art. 146)**: coerção violenta ou ameaçadora sobre a vítima para coagir conduta com previsão legal de exclusão para evitar suicídio.",
            "**Ameaça (art. 147)**: anúncio intimidador de mal injusto e severo consumado como crime formal assim que o recado lesivo alcança o conhecimento do ofendido.",
            "**Ação na Ameaça**: submete-se à condição de procedibilidade da representação oportuna sem a qual decai a persecução estatal.",
            "**Perseguição / Stalking (art. 147-A)**: cerceamento obsessivo reiterado exigindo habitualidade comportamental que perturbe a intimidade ou locomoção alheia.",
            "**Majorantes da Perseguição**: exaspera a sanção em metade quando vitimar mulher vulnerável, menor, ancião ou quando perpetrado com emprego armado.",
            "**Violência Psicológica (art. 147-B)**: prática degradante consubstanciada na causação de efetivo prejuízo emocional comprovado à autodeterminação feminina.",
            "**Natureza Material do Art. 147-B**: subordina a adequação típica à constatação real de perturbação e trauma na higidez mental da mulher tutelada.",
            "**Tutela de Gênero**: ampara a integridade psíquica feminina articulando tipificações repressivas com o aparato protetivo da Lei Maria da Penha."
        ]
    })

    return items, summaries
