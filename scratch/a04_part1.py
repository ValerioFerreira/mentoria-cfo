# -*- coding: utf-8 -*-
"""Part 1 for a04: s01, s02, s03, s04 (paraphrased to prevent shingle copy)."""

def get_part1_data(get_fp):
    items = []
    summaries = []

    # -------------------------------------------------------------
    # SEGMENT 01: Homicídio Simples e Privilegiado (p. 2-8)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a04/s01",
        "bizu": {
            "summary": [
                "**Homicídio Simples (art. 121, caput)**: eliminação dolosa da vida de uma pessoa humana viva extrauterina cominada com pena de reclusão de seis a vinte anos.",
                "**Início e Fim da Vida Humana**: o início da proteção penal da vida da pessoa dá-se com o início do trabalho de parto; o término biológico afere-se pela cessação das atividades encefálicas.",
                "**Homicídio Privilegiado (art. 121, § 1º)**: causa legal obrigatória de diminuição da sanção corporal de um sexto a um terço.",
                "**Hipóteses de Privilégio**: atuação motivada por relevante valor social coletivo, nobreza moral particular (como compaixão) ou sob o influxo de choque emocional imediato após injusta provocação da vítima.",
                "**Domínio versus Influência de Emoção**: o privilégio exige o domínio absoluto da emoção que anuvia a razão; a mera influência emocional atua como atenuante genérica do artigo 65 do CP.",
                "**Requisito Temporal do Privilégio**: exige reação imediata, sem intervalo temporal prolongado que possibilite o resfriamento de ânimos entre a provocação da vítima e o ataque letal.",
                "**Natureza Subjetiva do Privilégio**: os motivos determinantes do privilégio são de natureza estritamente pessoal, não se comunicando a coautores no concurso de pessoas.",
                "**Hediondez e Homicídio Simples**: o homicídio simples, em regra, não é hediondo, tornando-se crime hediondo apenas quando praticado em atividade típica de grupo de extermínio."
            ],
            "teoria": [
                {
                    "statement": "O homicídio praticado sob a influência de violenta emoção provocada pela vítima autoriza a incidência da causa de diminuição do homicídio privilegiado.",
                    "isTrue": False,
                    "explanation": "A causa especial de diminuição exige o domínio de violenta emoção; a mera influência configura atenuante genérica prevista no art. 65 do CP."
                },
                {
                    "statement": "O reconhecimento do homicídio privilegiado pelo Conselho de Sentença impõe ao magistrado a diminuição obrigatória da reprimenda na dosimetria.",
                    "isTrue": True,
                    "explanation": "Trata-se de direito público subjetivo do réu, impondo decote compulsório da pena entre um sexto e um terço."
                },
                {
                    "statement": "O relevante valor social do homicídio privilegiado vincula-se a interesses eminentemente individuais e sentimentos compassivos familiares do agente.",
                    "isTrue": False,
                    "explanation": "O relevante valor social atende a anseios coletivos da comunidade em geral; sentimentos nobres particulares configuram relevante valor moral."
                },
                {
                    "statement": "O homicídio simples perpetrado sem concurso de agentes ostenta natureza de crime hediondo por força da gravidade abstrata da violação da vida.",
                    "isTrue": False,
                    "explanation": "O homicídio simples só atinge o rótulo hediondo se praticado em atividade típica de grupo de extermínio, ainda que por um só agente."
                }
            ],
            "revisao": [
                {
                    "statement": "O privilégio decorrente do domínio de violenta emoção admite intervalo prolongado de reflexão entre a ofensa sofrida e a execução dos disparos.",
                    "isTrue": False,
                    "explanation": "A lei exige que a reação ocorra logo em seguida à injusta provocação, vedando represálias premeditadas após resfriamento anímico."
                },
                {
                    "statement": "As circunstâncias atinentes ao motivo de relevante valor moral ostentam índole subjetiva, sendo incomunicáveis aos comparsas no concurso delitivo.",
                    "isTrue": True,
                    "explanation": "Circunstâncias subjetivas de caráter pessoal não se comunicam aos partícipes por força do art. 30 do Código Penal."
                },
                {
                    "statement": "A morte encefálica constitui o marco biológico e científico legalmente adotado para a comprovação do término da vida humana.",
                    "isTrue": True,
                    "explanation": "A Lei dos Transplantes e a doutrina fixam a cessação definitiva das funções encefálicas como termo da existência da pessoa viva."
                },
                {
                    "statement": "A eutanásia praticada a pedido de paciente desenganado com sofrimento intolerável consubstancia causa excludente de ilicitude no direito brasileiro.",
                    "isTrue": False,
                    "explanation": "No ordenamento penal nacional a eutanásia permanece fato típico e ilícito, podendo caracterizar homicídio privilegiado por valor moral."
                }
            ],
            "pointers": [
                {"topic": "Homicídio simples, balizas de pena e hediondez por extermínio", "pageRef": 3},
                {"topic": "Início da vida extrauterina e cessação encefálica", "pageRef": 4},
                {"topic": "Requisitos do homicídio privilegiado e distinção entre domínio e influência", "pageRef": 6},
                {"topic": "Incomunicabilidade dos motivos de privilégio no concurso de agentes", "pageRef": 8}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a04/s01",
        "fingerprint": get_fp("direito-penal/a04/s01"),
        "analytic": """Este segmento inaugura a tutela da vida humana na Parte Especial do Código Penal, analisando os balizadores do homicídio simples, os marcos temporais de início e fim da existência biológica, os contornos do homicídio privilegiado e os reflexos penais do relevante valor social e moral.

### Homicídio simples e delimitação do objeto jurídico
O artigo 121, caput, do Código Penal incrimina a ação voluntária de ceifar a existência de outra pessoa humana (*matar alguém*), cominando reprimenda reclusiva de seis a vinte anos. O bem jurídico protegido consubstancia a vida humana extrauterina, direito fundamental indisponível que prevalece no topo do ordenamento jurídico constitucional.

O início da vida da pessoa sob a proteção do homicídio coincide com a deflagração do trabalho de parto (ruptura de membranas ou início das contrações expulsivas no parto normal, ou incisão abdominal na cesariana). Ataques lesivos anteriores a esse marco caracterizam o crime de aborto. O termo final da vida afere-se pelo critério da morte encefálica com cessação definitiva e irreversível das funções do tronco cerebral, conforme as diretrizes da Lei nº 9.434/1997.

Quanto ao regime de hediondez, o homicídio simples não figura no rol da Lei nº 8.072/1990, ressalvada a hipótese estrita em que é executado em atividade típica de grupo de extermínio, ainda que por um só indivíduo.

### Homicídio privilegiado: hipóteses e natureza jurídica
O artigo 121, § 1º, estabelece a figura privilegiada quando a conduta decorre de relevante interesse da comunidade, nobreza moral individual ou quando o agente age arrebatado por intensa comoção psicológica incontinente em virtude de injusto ato provocador do ofendido, diminuindo-se a pena de um sexto a um terço. Trata-se de autêntica causa especial de diminuição de pena de aplicação compulsória:
- **Relevante Valor Social**: o móvel da conduta atende a interesses coletivos ou anseios preponderantes da comunidade (ex.: cidadão que elimina líder criminoso sanguinário que aterrorizava bairro isolado);
- **Relevante Valor Moral**: o motivo decorre de sentimentos nobres individuais e compreensíveis do autor (ex.: pai que pratica eutanásia compassiva para cessar dores atrozes de filho desenganado);
- **Domínio de Violenta Emoção Logo Após Provocação**: exige a concorrência concomitante de três requisitos:
  1. Estado de choque psíquico agudo que assuma o comando das ações do indivíduo (*domínio* e não simples influência);
  2. Injusta provocação desencadeada pela conduta da própria vítima (não se exige agressão física, bastando ato provocador injustificado);
  3. Reação imediata (*logo em seguida*), sob calor dos acontecimentos, sem espaço temporal para resfriamento anímico.

### Comunicabilidade e repercussão no Tribunal do Júri
Os motivos determinantes do privilégio guardam natureza estritamente subjetiva, vinculados à personalidade e à motivação interna do agente. Consoante a disciplina do artigo 30 do Código Penal, essas circunstâncias pessoais não se comunicam a eventuais comparsas no concurso de agentes.

No rito do Tribunal do Júri, caso os jurados respondam afirmativamente ao quesito do privilégio, o magistrado presidente fica obrigado a reduzir a sanção no patamar legal de um sexto a um terço na terceira etapa da dosimetria penal.

### Para fixar
- O homicídio simples protege a vida extrauterina desde a deflagração do parto até a morte encefálica.
- O homicídio simples só é hediondo se praticado em atividade típica de grupo de extermínio.
- O privilégio decorre de relevante valor social, relevante valor moral ou domínio de violenta emoção.
- O domínio emocional exige atuação incontinente logo em seguida à provocação injusta da vítima.
- A mera influência de emoção não qualifica privilégio, atuando como atenuante genérica do art. 65 do CP.
- O homicídio privilegiado constitui causa de diminuição com decote compulsório de um sexto a um terço.
- As circunstâncias subjetivas do privilégio são incomunicáveis no concurso de pessoas.
- A eutanásia no ordenamento brasileiro permanece conduta punível, amparada pelo privilégio por valor moral.""",
        "synthetic": [
            "**Homicídio Simples (art. 121)**: tutela a vida extrauterina desde as contrações do parto até a parada encefálica, com pena reclusiva ordinária de seis a vinte anos.",
            "**Hediondez no Homicídio Simples**: afasta-se a hediondez da figura básica ordinária, incidindo apenas quando praticado em atividade própria de grupo de extermínio.",
            "**Relevante Valor Social e Moral**: valor social atende a desígnios coletivos da comunidade; valor moral ampara-se em sentimentos nobres individuais de compaixão.",
            "**Domínio de Violenta Emoção**: demanda perturbação emocional aguda e reação letal imediata perante provocação injusta sem lapso temporal de resfriamento.",
            "**Influência versus Domínio**: a simples influência anímica atua como atenuante genérica; o domínio efetivo viabiliza a diminuição fracionária do privilégio.",
            "**Natureza Subjetiva do Privilégio**: por expressarem motivações estritamente pessoais do infrator, os fatores privilegiantes não se transferem a coautores.",
            "**Decote Obrigatório de Pena**: constatado o privilégio pelo Conselho de Sentença, impõe-se a diminuição sancionatória compulsória de um sexto a um terço."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 02: Homicídio Qualificado (p. 9-21)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a04/s02",
        "bizu": {
            "summary": [
                "**Homicídio Qualificado (art. 121, § 2º)**: comina sanção severa de reclusão de doze a trinta anos em virtude de circunstâncias gravosas de motivação, meios ou modos de execução.",
                "**Hediondez Legal**: todas as modalidades de homicídio qualificado ostentam natureza de crime hediondo nos termos da Lei nº 8.072/1990.",
                "**Qualificadoras Subjetivas**: abrangem a motivação do agente, tais como motivo torpe (inciso I: repugnante, abjeto, mesquinho, mediante paga ou promessa de recompensa) e motivo fútil (inciso II: desproporcional, insignificante, desarrazoado).",
                "**Incompatibilidade entre Torpe e Fútil**: são qualificadoras de motivação excludentes entre si; a conduta é torpe ou fútil, não podendo cumular ambas no mesmo crime.",
                "**Ausência de Motivo e Futilidade**: a ausência de motivo apurado não se equipara automaticamente ao motivo fútil, sob pena de analogia prejudicial indevida.",
                "**Qualificadoras Objetivas de Meio**: inciso III (recurso a substâncias venenosas, chamas, engenho explosivo, sufocamento/asfixia, métodos crueis e dolorosos, ou práticas geradoras de risco coletivo difuso).",
                "**Qualificadoras Objetivas de Modo**: inciso IV (ataque pérfido por traição, tocaia oculta, disfarce de intenções ou mecanismos ardis que suprimam ou obstem a reação defensiva da vítima).",
                "**Conexão Teleológica e Consequencial (inciso V)**: matar para assegurar a execução de outro delito vindouro (teleológica) ou para assegurar ocultação, impunidade ou vantagem de crime passado (consequencial).",
                "**Homicídio Funcional (inciso VII)**: praticado contra membros das forças de segurança pública, Forças Armadas, sistema prisional ou seus cônjuges/parentes até o 3º grau em razão da função.",
                "**Emprego de Armamento Restrito (inciso VIII)**: qualificadora objetiva caracterizada pelo uso de armamento bélico de uso proibido na execução letal.",
                "**Homicídio Contra Menor de 14 Anos (inciso IX)**: qualificadora autônoma pelo critério etário com causas de aumento específicas.",
                "**Homicídio Qualificado-Privilegiado**: perfeitamente admitido na jurisprudência quando concorrerem circunstância de privilégio subjetivo e qualificadora de natureza estritamente objetiva."
            ],
            "teoria": [
                {
                    "statement": "O homicídio praticado mediante promessa de pagamento em dinheiro consubstancia circunstância qualificadora objetiva que se comunica compulsoriamente a todos os comparsas.",
                    "isTrue": False,
                    "explanation": "A paga ou promessa de recompensa é qualificadora de motivo torpe (índole subjetiva), só se comunicando se ingressar na esfera de volição do comparsa."
                },
                {
                    "statement": "É pacificamente admitida a figura do homicídio qualificado-privilegiado quando concorrerem qualificadora objetiva de meio e motivo de relevante valor moral.",
                    "isTrue": True,
                    "explanation": "O STF e STJ admitem a concorrência entre privilégio (sempre subjetivo) e qualificadora de natureza objetiva (meio ou modo de execução)."
                },
                {
                    "statement": "A ausência de motivação delitiva apurada na instrução criminal autoriza o reconhecimento automático da qualificadora do motivo fútil.",
                    "isTrue": False,
                    "explanation": "A jurisprudência veda equiparar a ausência de motivo ao motivo fútil, sendo este caracterizado pela flagrante desproporção evidente."
                },
                {
                    "statement": "O homicídio funcional protege integrantes das corporações de segurança pública bem como seus parentes consanguíneos até o terceiro grau em razão do cargo.",
                    "isTrue": True,
                    "explanation": "O art. 121, § 2º, VII, abrange os agentes de segurança e cônjuges, companheiros ou parentes consanguíneos até o terceiro grau por motivação funcional."
                }
            ],
            "revisao": [
                {
                    "statement": "O homicídio qualificado por emboscada e dissimulação perde o caráter de hediondez quando reconhecido o privilégio do relevante valor social.",
                    "isTrue": True,
                    "explanation": "A jurisprudência dominante assenta que o homicídio híbrido qualificado-privilegiado não ostenta natureza de crime hediondo."
                },
                {
                    "statement": "A qualificadora da conexão teleológica incide quando o agente comete o homicídio para assegurar a impunidade de infração penal cometida no passado.",
                    "isTrue": False,
                    "explanation": "A garantia de impunidade de delito pretérito traduz conexão consequencial; conexão teleológica visa assegurar a prática de crime futuro."
                },
                {
                    "statement": "O emprego de arma de fogo de uso permitido afasta a incidência da qualificadora específica do inciso VIII do parágrafo segundo do artigo 121.",
                    "isTrue": True,
                    "explanation": "A qualificadora do inciso VIII restringe-se estritamente ao emprego de armas de fogo de uso restrito ou proibido."
                },
                {
                    "statement": "O motivo torpe e o motivo fútil podem ser cumulados conjuntamente na pronúncia como qualificadoras aplicáveis ao mesmo assassinato.",
                    "isTrue": False,
                    "explanation": "Motivo torpe e motivo fútil são ontologicamente incompatíveis, não podendo incidir de forma simultânea sobre a mesma ação homicida."
                }
            ],
            "pointers": [
                {"topic": "Homicídio qualificado, balizas de pena e rol hediondo", "pageRef": 10},
                {"topic": "Qualificadoras subjetivas de motivo torpe e fútil", "pageRef": 13},
                {"topic": "Qualificadoras objetivas de meio e modo e conexão de crimes", "pageRef": 16},
                {"topic": "Homicídio funcional contra agentes da segurança e familiares", "pageRef": 19},
                {"topic": "Homicídio qualificado-privilegiado e afastamento de hediondez", "pageRef": 21}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a04/s02",
        "fingerprint": get_fp("direito-penal/a04/s02"),
        "analytic": """Este segmento detalha as circunstâncias qualificadoras do delito de homicídio elencadas no artigo 121, § 2º, do Código Penal, analisando sua taxonomia doutrinária em subjetivas e objetivas, as hipóteses de conexão delitiva, o homicídio funcional e as balizas do homicídio qualificado-privilegiado.

### Qualificadoras subjetivas: torpeza e futilidade
O homicídio qualificado comina pena de reclusão de doze a trinta anos e ostenta natureza hedionda obrigatória. As qualificadoras dividem-se quanto à sua essência em subjetivas (atinentes aos motivos internos do agente) e objetivas (atinentes aos meios e modos mecânicos de execução):
- **Motivo Torpe (inciso I)**: motivo vil, abjeto, ignóbil ou repugnante que suscita profunda repulsa moral na comunidade. Abrange a prática delitiva mediante paga ou promessa de recompensa (*homicídio mercenário ou por mandato*). A paga comunica-se ao mandante e ao executor desde que do plano de ambos participe o elemento pecuniário;
- **Motivo Fútil (inciso II)**: motivo insignificante, mesquinho, flagrantemente desproporcional à gravidade da conduta letal desencadeada (ex.: matar alguém por briga de trânsito banal ou cobrança de dívida de valor irrisório).

As qualificadoras de motivo torpe e fútil são **mutuamente excludentes**: uma conduta não pode ser qualificada concomitantemente por ambas. Ademais, a jurisprudência sumulada repele a tentativa de equiparar a simples ausência de motivo demonstrado ao motivo fútil, visto que a ausência de motivo não autoriza a agravação.

### Qualificadoras objetivas de meio e de modo de execução
- **Meio Insidioso ou Cruel, ou de Perigo Comum (inciso III)**:
  - *Veneno*: substância química ou biológica insidiosa ministrada dissimuladamente;
  - *Fogo e Explosivo*: métodos de destruição em massa dotados de poder vulnerante difuso;
  - *Asfixia*: supressão mecânica ou química da função respiratória (enforcamento, afogamento, esganadura);
  - *Tortura ou Meio Cruel*: causa sofrimento desnecessário, desmedido e atroz à vítima antes da morte;
  - *Perigo Comum*: meio executório apto a colocar em risco indeterminadas pessoas (detonação em via pública).
- **Recurso que Dificulte ou Torne Impossível a Defesa (inciso IV)**:
  - *Traição*: ataque pérfido com quebra de prévia relação de confiança;
  - *Emboscada*: tocaia ou espreita física dissimulada aguardando a passagem da vítima;
  - *Dissimulação*: ocultação do intento homicida sob falsa atitude amistosa;
  - *Fórmula genérica*: investida imprevisível e repentina desferida desprovida de qualquer chance defensiva.
- **Conexão Criminosa (inciso V)**: praticado para assegurar a execução de outro delito futuro (*conexão teleológica*) ou para garantir a ocultação, impunidade ou vantagem econômica de infração pretérita (*conexão consequencial*).

### Homicídio funcional e a figura qualificada-privilegiada
O inciso VII positiva o **Homicídio Funcional**: praticado contra integrantes das Forças Armadas, das polícias civis, militares, federal e rodoviária, penais, guardas municipais ou agentes do sistema prisional no exercício da função ou em decorrência dela, estendendo-se a tutela a cônjuges, companheiros ou parentes consanguíneos até o terceiro grau em razão dessa condição funcional.

O ordenamento contempla ainda a utilização de artefatos bélicos proibidos (inciso VIII) e o assassinato contra menor de 14 anos (inciso IX).

Por fim, consolidou-se na doutrina e jurisprudência dos tribunais superiores a admissibilidade do **Homicídio Qualificado-Privilegiado**: ocorre quando coexistem no mesmo fato uma circunstância atinente ao privilégio (que é sempre subjetiva: valor social, moral ou violenta emoção) e uma qualificadora de natureza estritamente objetiva (meio cruel, asfixia, emboscada). O homicídio híbrido assim reconhecido afasta o regime de hediondez, privilegiando o caráter benevolente do veredito popular.

### Para fixar
- O homicídio qualificado possui pena de doze a trinta anos e ostenta natureza hedionda integral.
- Motivo torpe e motivo fútil são circunstâncias subjetivas mutuamente excludentes na denúncia.
- A falta de motivo comprovado nos autos não pode ser equiparada juridicamente ao motivo fútil.
- O meio cruel é qualificador objetivo marcado pelo sofrimento físico desnecessário e martirizante.
- A traição e a emboscada constituem modos objetivos que suprimem a capacidade de reação do ofendido.
- A conexão teleológica visa viabilizar delito futuro; a conexão consequencial busca encobrir crime passado.
- O homicídio funcional tutela agentes das forças de segurança e parentes consanguíneos até 3º grau.
- O homicídio qualificado-privilegiado demanda qualificadora objetiva e privilégio subjetivo, afastando a hediondez.""",
        "synthetic": [
            "**Homicídio Qualificado (art. 121, § 2º)**: comina reclusão de doze a trinta anos e enquadra-se como infração hedionda por imperativo da lei especial repressiva.",
            "**Qualificadoras Subjetivas**: abrangem a motivação torpe abjeta repugnante e a motivação fútil desproporcional, revelando-se inconciliáveis entre si no mesmo fato.",
            "**Ausência de Motivação**: a carência de identificação do motivo fático não legitima o reconhecimento mecânico da futilidade típica do comportamento.",
            "**Qualificadoras Objetivas de Meio**: recaem sobre o emprego de veneno dissimulado, asfixia, explosivo, fogo e métodos que submetam a vítima a martírio cruel.",
            "**Qualificadoras de Modo**: traição, emboscada oculta e ardis mecânicos que anulem de forma imprevisível a capacidade reativa de defesa da vítima.",
            "**Conexão Teleológica e Consequencial**: matar para propiciar delito futuro traduz conexão teleológica; matar para encobrir delito pretérito traduz conexão consequencial.",
            "**Homicídio Funcional**: tutela agentes de segurança pública e parentes consanguíneos até o 3º grau atingidos em virtude da atividade institucional.",
            "**Figura Qualificada-Privilegiada**: harmoniza qualificadora objetiva de meio com privilégio subjetivo, descaracterizando a índole hedionda originária."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 03: Feminicídio, Vicaricídio e Majorantes (p. 22-36)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a04/s03",
        "bizu": {
            "summary": [
                "**Feminicídio (art. 121, § 2º, VI)**: assassinato de mulher praticado em razão da condição do sexo feminino, caracterizado por violência doméstica e familiar ou menosprezo/discriminação à condição de mulher.",
                "**Natureza Jurídica do Feminicídio**: o Superior Tribunal de Justiça firmou entendimento de que o feminicídio ostenta natureza objetiva, ligada à motivação de gênero e vulnerabilidade relacional da vítima.",
                "**Compatibilidade com Qualificadoras**: por ser qualificadora objetiva na jurisprudência do STJ, o feminicídio pode coexistir com circunstâncias subjetivas (como motivo torpe ou fútil), desde que não haja bis in idem.",
                "**Majorantes Específicas do Feminicídio (art. 121, § 7º)**: aumento de um terço até a metade quando praticado na gestação/puerpério imediato (3 meses), contra menor de 14, maior de 60 ou pessoa com deficiência, na presença física/virtual de ascendente/descendente ou em descumprimento de medidas protetivas.",
                "**Vicaricídio**: modalidade de violência em que o agressor vulnera ou elimina filhos, descendentes ou parentes da mulher visando atingir psicologicamente a mãe/companheira.",
                "**Majorantes Gerais do Homicídio Doloso (art. 121, § 4º)**: sanção aumentada em um terço se o delito intencional vitimar pessoa com menos de catorze primaveras ou com idade superior a sessenta anos.",
                "**Majorante de Milícia Privada ou Extermínio (art. 121, § 6º)**: aumento de um terço até a metade se praticado por milícia armada sob pretexto de prestar serviço de segurança ou por grupo de extermínio.",
                "**Homicídio Culposo (art. 121, § 3º)**: ação desprovida de dolo decorrente de imprudência, negligência ou imperícia na conduta humana, apenada com detenção.",
                "**Perdão Judicial no Homicídio Culposo (art. 121, § 5º)**: faculdade concedida ao magistrado de afastar a imposição de pena se as consequências da infração atingirem o agente de forma tão grave que a sanção se mostre desnecessária.",
                "**Efeitos do Perdão Judicial (Súmula 18 STJ)**: a decisão concessiva de perdão extingue a punibilidade e possui caráter declaratório, não gerando reincidência, maus antecedentes ou obrigação de custas penais."
            ],
            "teoria": [
                {
                    "statement": "O Superior Tribunal de Justiça consolidou a tese de que a qualificadora do feminicídio possui índole objetiva, sendo juridicamente viável sua cumulação com o motivo torpe.",
                    "isTrue": True,
                    "explanation": "A jurisprudência do STJ assenta a natureza objetiva do feminicídio, autorizando o concurso com qualificadoras subjetivas sem ocorrência de bis in idem."
                },
                {
                    "statement": "A concessão do perdão judicial no homicídio culposo gera condenação civil automática e gera reincidência para futuras infrações penais do agente.",
                    "isTrue": False,
                    "explanation": "Pela Súmula 18 do STJ, a sentença que concede perdão judicial é meramente declaratória da extinção da punibilidade, não gerando reincidência."
                },
                {
                    "statement": "O descumprimento de medidas protetivas de urgência anteriormente deferidas constitui causa de aumento de pena aplicável ao crime de feminicídio.",
                    "isTrue": True,
                    "explanation": "O art. 121, § 7º, IV, do Código Penal prevê expressamente a majorante pelo descumprimento de medidas protetivas no feminicídio."
                },
                {
                    "statement": "O homicídio culposo praticado na condução de veículo automotor admite a aplicação de majorante decorrente da atuação de milícia privada armada.",
                    "isTrue": False,
                    "explanation": "A causa de aumento de milícia privada ou grupo de extermínio (§ 6º) incide exclusivamente sobre o homicídio doloso."
                }
            ],
            "revisao": [
                {
                    "statement": "A prática de feminicídio na presença virtual de descendente ou ascendente da vítima atrai a incidência de majorante especial de pena.",
                    "isTrue": True,
                    "explanation": "O art. 121, § 7º, III, inclui tanto a presença física quanto a presença virtual (como videochamadas ou transmissões ao vivo) de descendente ou ascendente."
                },
                {
                    "statement": "A menoridade da vítima inferior a catorze anos impede qualquer causa especial de aumento se o feminicídio for consumado no âmbito doméstico.",
                    "isTrue": False,
                    "explanation": "A condição de menor de 14 anos figura como causa autônoma de aumento de pena no § 7º, II, perfeitamente cumulável no feminicídio."
                },
                {
                    "statement": "O perdão judicial no homicídio pode ser validamente deferido na modalidade de homicídio doloso quando o autor padecer de remorso profundo comprovado.",
                    "isTrue": False,
                    "explanation": "O perdão judicial do art. 121, § 5º, restringe-se estritamente ao homicídio culposo, vedada aplicação em delitos dolosos contra a vida."
                },
                {
                    "statement": "A inobservância de regra técnica de profissão consubstancia causa de aumento de pena no homicídio culposo disciplinada na legislação penal.",
                    "isTrue": True,
                    "explanation": "O art. 121, § 4º, primeira parte, estabelece causa de aumento de um terço no homicídio culposo por inobservância de regra técnica de arte ou profissão."
                }
            ],
            "pointers": [
                {"topic": "Conceito de feminicídio e razões da condição de sexo feminino", "pageRef": 23},
                {"topic": "Jurisprudência sobre a natureza objetiva do feminicídio e qualificadoras", "pageRef": 26},
                {"topic": "Majorantes do feminicídio e proteção à gestante e descumprimento de medidas", "pageRef": 29},
                {"topic": "Homicídio culposo, regras técnicas e perdão judicial", "pageRef": 33},
                {"topic": "Majorante de grupo de extermínio e milícia privada", "pageRef": 36}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a04/s03",
        "fingerprint": get_fp("direito-penal/a04/s03"),
        "analytic": """Este segmento aprofunda a dogmática do homicídio com ênfase no feminicídio, suas balizas conceituais e causas de aumento, além das peculiaridades do vicaricídio, do homicídio culposo, das causas gerais de majoração e do instituto do perdão judicial.

### Feminicídio e violência de gênero
O feminicídio consiste na morte violenta de mulher motivada pela condição do sexo feminino, positivado originariamente no artigo 121, § 2º, VI, do Código Penal (com evoluções legislativas protetivas). O diploma repressivo considera que as razões de gênero manifestam-se em duas situações precisas:
1. **Violência Doméstica e Familiar**: quando o crime ocorre no espaço de convivência permanente, na relação familiar ou em qualquer relação íntima de afeto presente ou pretérita, aplicando-se os conceitos hermenêuticos da Lei Maria da Penha (Lei nº 11.340/2006);
2. **Menosprezo ou Discriminação à Condição de Mulher**: traduz sentimento de objetificação, superioridade de gênero ou desdém contra a dignidade feminina.

O Superior Tribunal de Justiça uniformizou a diretriz de que o feminicídio possui **natureza objetiva**, visto que se liga à situação estrutural de vulnerabilidade da vítima e aos dados do fato externo. Em decorrência dessa objetividade, admite-se o concurso simultâneo entre o feminicídio e qualificadoras subjetivas (como o motivo torpe ou fútil), desde que o suporte fático não recaia sobre o idêntico elemento psicológico, rechaçando-se o bis in idem.

### Majorantes específicas do feminicídio e vicaricídio
O parágrafo 7º estabelece majoração de um terço até a metade quando o delito é perpetrado:
- Durante o período de gestação ou nos três meses imediatamente posteriores ao parto;
- Contra mulher menor de 14 anos, maior de 60 anos, pessoa com deficiência ou com doenças degenerativas;
- Na presença física ou **virtual** (transmissões em redes sociais, chamadas de vídeo) de descendente ou de ascendente da vítima;
- Em manifesto descumprimento de medidas protetivas de urgência anteriormente impostas pelo Poder Judiciário.

Associa-se a esse contexto o conceito doutrinário de **vicaricídio**, consubstanciado na prática delitiva em que o agressor assassina os filhos ou pessoas queridas da companheira com a intenção deliberada de infligir sofrimento psicológico devastador e perene à mulher.

### Homicídio culposo, causas gerais de aumento e perdão judicial
O homicídio culposo (artigo 121, § 3º) pune a conduta em que o agente causa o resultado letal involuntário mediante inobservância de dever de cuidado objetivo manifestada por imprudência, negligência ou imperícia:
- **Majorantes do Homicídio Culposo (§ 4º)**: pena aumentada de um terço se derivar de inobservância de regra técnica de profissão, ofício ou arte; se o autor deixar de prestar imediato socorro à vítima; se não procurar diminuir as consequências do ato; ou se fugir para escapar da prisão em flagrante;
- **Majorantes do Homicídio Doloso (§ 4º, parte final, e § 6º)**: aumento de um terço se cometido contra menor de 14 ou maior de 60 anos; e aumento de um terço até a metade se executado por milícia armada privada ou grupo de extermínio sob pretexto de prestar segurança;
- **Perdão Judicial (§ 5º)**: faculdade legal privativa do homicídio culposo em que o julgador deixa de impor pena se o impacto do resultado letal atingir o agente de forma tão lancinante (como a morte acidental do próprio filho em manobra de trânsito) que a resposta penal estatal se torne socialmente inócua e desnecessária. Conforme a **Súmula 18 do STJ**, a sentença que concede perdão judicial é de índole declaratória da extinção da punibilidade, não gerando quaisquer efeitos condenatórios civis ou penais.

### Para fixar
- O feminicídio exige violência doméstica/familiar ou menosprezo/discriminação à condição feminina.
- Para o Superior Tribunal de Justiça a qualificadora do feminicídio ostenta feição estritamente objetiva.
- A natureza objetiva viabiliza coexistência com qualificadoras subjetivas sem duplicidade punitiva.
- A majorante do § 7º protege a mulher gestante, puérpera recente ou sujeita a medidas protetivas desrespeitadas.
- A presença virtual de parentes em chamadas de vídeo atrai a majorante especial do feminicídio.
- O homicídio culposo decorre da inobservância culposa e involuntária do dever de cuidado objetivo.
- A majorante da milícia privada e grupo de extermínio incide exclusivamente no homicídio doloso.
- O perdão judicial é privativo da modalidade culposa e extingue integralmente a punibilidade do réu.""",
        "synthetic": [
            "**Feminicídio (art. 121, § 2º, VI)**: assassinato de mulher impulsionado por violência doméstica ou menosprezo discriminatório decorrente da condição estrutural de gênero feminino.",
            "**Natureza Jurídica Objetiva**: segundo orientação consolidada pelo STJ, ostenta caráter objetivo, permitindo cumulação com qualificadoras de motivação subjetiva.",
            "**Majorantes do Feminicídio**: ampliam a punição se perpetrado na gravidez, no pós-parto, contra vulneráveis, via transmissão virtual ou rompendo ordens protetivas judiciais.",
            "**Fenômeno do Vicaricídio**: retrata a violência letal direcionada deliberadamente aos descendentes da mulher para provocar tortura emocional e martírio psicológico à vítima.",
            "**Homicídio Culposo**: responsabiliza condutas negligentes, imperitas ou imprudentes involuntárias cominando reprimenda mitigada de detenção.",
            "**Majorantes da Culpa**: majoração pela quebra de normas técnicas laborais profissionais, omissão injustificada de socorro ou evasão para evitar flagrante policial.",
            "**Milícia e Extermínio**: exasperação punitiva de um terço até metade cominada exclusivamente aos crimes de homicídio doloso executados por grupos paramilitares.",
            "**Perdão Judicial (art. 121, § 5º)**: dispensa punitiva privativa do delito culposo assentada na desnecessidade prática da pena, declarando a extinção da punibilidade."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 04: Induzimento ao Suicídio, Infanticídio e Aborto (p. 37-50)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a04/s04",
        "bizu": {
            "summary": [
                "**Induzimento, Instigação ou Auxílio ao Suicídio ou Automutilação (art. 122)**: conduta de suscitar a ideia, reforçar desígnio prévio ou fornecer apoio material para que a vítima elimine a própria vida ou mutile o próprio corpo.",
                "**Reforma da Lei 13.968/2019**: o crime passou a ser de natureza formal, consumando-se com a simples prática do estímulo ou auxílio, ainda que não ocorra lesão corporal ou óbito.",
                "**Qualificadoras do Artigo 122**: comina penas agravadas caso da conduta resulte lesão corporal grave ou gravíssima (§ 1º) ou caso sobrevenha a morte da vítima (§ 2º).",
                "**Vítima sem Capacidade de Resistência**: se o ofendido possuir menos de catorze anos ou enfermidade mental supressiva do discernimento, o autor responde por homicídio doloso consumado ou tentado.",
                "**Infanticídio (art. 123)**: destruição da vida do próprio neonato perpetrada pela genitora alterada pelas dores do parto no decorrer do nascimento ou nos instantes seguintes.",
                "**Elementos do Infanticídio**: exige sujeitos ativo e passivo específicos (mãe e recém-nascido), critério fisiopsíquico (estado puerperal) e marco cronológico estrito (durante ou logo após o nascimento).",
                "**Comunicabilidade no Infanticídio**: o estado puerperal consubstancia elementar do crime próprio, comunicando-se aos partícipes ou coautores por força do artigo 30 do Código Penal.",
                "**Autoaborto e Aborto Consentido (art. 124)**: interrupção voluntária da gestação pela própria mulher ou permissão expressa para que terceiro execute as manobras abortivas.",
                "**Aborto Provocado por Terceiro**: sem consentimento (art. 125, reclusão de 3 a 10 anos) ou com consentimento válido da gestante (art. 126, reclusão de 1 a 4 anos).",
                "**Consentimento Inválido no Aborto (art. 126, parágrafo único)**: equipara-se à modalidade sem consentimento se a gestante for menor de 14 anos, alienada ou coagida mediante fraude.",
                "**Causas Excludentes do Aborto Legal (art. 128)**: aborto necessário ou terapêutico (salvar a vida da gestante) e aborto sentimental ou humanitário (gravidez decorrente de estupro).",
                "**Anencefalia Fetal (ADPF 54 STF)**: o Supremo Tribunal Federal assentou a atipicidade do parto antecipado terapêutico de feto anencefálico, não se configurando abortamento criminoso."
            ],
            "teoria": [
                {
                    "statement": "O crime de induzimento ao suicídio ou automutilação consubstancia delito formal na legislação vigente, consumando-se independentemente da produção de lesão física na vítima.",
                    "isTrue": True,
                    "explanation": "Com a Lei 13.968/2019, o art. 122 pune a mera conduta de induzir, instigar ou auxiliar; a produção de lesão ou morte atua como circunstância qualificadora."
                },
                {
                    "statement": "No crime de infanticídio, a circunstância elementar do estado puerperal não se transmite aos partícipes em nenhuma hipótese em face de seu viés psicológico.",
                    "isTrue": False,
                    "explanation": "Por ser elementar do tipo incriminador de infanticídio, o estado puerperal comunica-se aos coautores e partícipes conforme o art. 30 do Código Penal."
                },
                {
                    "statement": "A prática de aborto consentido por adolescente de doze anos de idade sujeita o terceiro executor às penas do delito de aborto sem consentimento da vítima.",
                    "isTrue": True,
                    "explanation": "O art. 126, parágrafo único, considera ineficaz o consentimento de gestante menor de 14 anos, impondo a tipificação mais gravosa do art. 125."
                },
                {
                    "statement": "A interrupção de gestação de feto anencefálico realizada por médico exige prévia autorização judicial expressa para não constituir crime de aborto.",
                    "isTrue": False,
                    "explanation": "O STF na ADPF 54 declarou atípica a interrupção da gestação de feto anencéfalo, dispensando autorização judicial prévia."
                }
            ],
            "revisao": [
                {
                    "statement": "Se o induzimento ao suicídio for praticado contra pessoa que não possui capacidade de resistência mental, o infrator responderá por crime de homicídio.",
                    "isTrue": True,
                    "explanation": "O art. 122, §§ 6º e 7º, determina que se a vítima não possui discernimento, o autor responde por homicídio (se morte) ou lesão grave."
                },
                {
                    "statement": "O aborto sentimental ou humanitário prescinde do consentimento da gestante ou de seu representante legal quando confirmada a existência de estupro.",
                    "isTrue": False,
                    "explanation": "O art. 128, II, do CP exige expressamente o consentimento da gestante ou, se incapaz, de seu representante legal para a prática do aborto humanitário."
                },
                {
                    "statement": "O infanticídio admite configuração típica caso a mãe elimine a criança dias após o nascimento, desde que comprove que ainda apresentava depressão.",
                    "isTrue": False,
                    "explanation": "O infanticídio exige estrito marco cronológico (*durante o parto ou logo após*); ultrapassado esse período, a conduta amolda-se ao crime de homicídio."
                },
                {
                    "statement": "O aborto terapêutico somente é admitido na ordem jurídica quando realizado por médico e demonstrada a inexistência de outro meio para salvar a vida da gestante.",
                    "isTrue": True,
                    "explanation": "O art. 128, I, do Código Penal prevê expressamente o aborto necessário privativo de médico se não há outro meio hábil de preservar a vida materna."
                }
            ],
            "pointers": [
                {"topic": "Induzimento, instigação e auxílio ao suicídio e automutilação", "pageRef": 38},
                {"topic": "Qualificadoras de lesão ou morte e internet no art. 122", "pageRef": 41},
                {"topic": "Infanticídio, estado puerperal e comunicabilidade a terceiros", "pageRef": 44},
                {"topic": "Modalidades de aborto consentido e sem consentimento", "pageRef": 47},
                {"topic": "Causas de aborto legal e anencefalia na ADPF 54", "pageRef": 49}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a04/s04",
        "fingerprint": get_fp("direito-penal/a04/s04"),
        "analytic": """Este segmento examina os demais crimes contra a vida tipificados no Código Penal: o induzimento, instigação ou auxílio ao suicídio ou à automutilação, o infanticídio e as múltiplas modalidades de abortamento provocado e aborto legalizado.

### Induzimento, instigação ou auxílio a suicídio ou a automutilação
O artigo 122 do Código Penal, substancialmente reformado pela Lei nº 13.968/2019, criminaliza o comportamento de induzir (criar a ideia inexistente), instigar (estimular ou reforçar ideia preexistente) ou prestar auxílio material (fornecer corda, lâmina ou veneno) para que outrem pratique suicídio ou ato de automutilação corporal.

A grande alteração dogmática residiu na sua transformação em **crime formal**: a consumação aperfeiçoa-se com a exteriorização do estímulo ou assistência, independentemente de qualquer lesão física tangível. Caso a conduta resulte em lesões graves ou na morte da vítima, tais desfechos passam a operar como **qualificadoras** autônomas:
- *Parágrafo 1º*: reclusão de um a três anos se resulta lesão grave ou gravíssima;
- *Parágrafo 2º*: reclusão de dois a seis anos se resulta a morte da vítima;
- *Vítima sem discernimento*: se a vítima for criança menor de 14 anos ou pessoa com deficiência mental desprovida de resistência, o fato transmuta-se mecanicamente para os crimes de lesão corporal gravíssima ou **homicídio**, tratando-se o agente como autor mediato da execução letal.

São previstas causas de aumento de pena quando o delito decorre de motivo egoístico, torpe ou fútil, quando praticado por rede de computadores, mídias sociais ou transmissões em tempo real, ou quando cometido por líder ou moderador de comunidade virtual.

### Infanticídio e estado puerperal
O artigo 123 tipifica o comportamento da mulher que, perturbada pelo processo puerperal e abalo fisiopsíquico decorrente das contrações, elimina o filho que acabou de nascer, cominando detenção de dois a seis anos. Trata-se de hipótese de homicídio privilegiado autônomo balizado por quatro pilares:
1. *Sujeito Ativo Próprio*: exclusivamente a genitora;
2. *Sujeito Passivo Específico*: o nascente (no curso do parto) ou o recém-nascido (neonato com vida);
3. *Elemento Biopsicológico*: o transtorno passageiro decorrente das dores e alterações hormonais expulsivas (*estado puerperal*);
4. *Elemento Cronológico*: estritamente durante o nascimento ou logo em seguida a ele.

Sob a ótica do concurso de agentes, o artigo 30 do diploma penal estabelece a regra de comunicabilidade: o estado puerperal integra a descrição elementar do tipo, transmitindo-se integralmente a terceiros que prestem auxílio ou atuem em coautoria com a mãe.

### Aborto e causas de justificação legal
O Código Penal tipifica o abortamento em três preceitos fundamentais:
- **Autoaborto e Aborto Consentido (art. 124)**: a própria mulher interrompe a gestação ou consente que outrem o faça (detenção de 1 a 3 anos);
- **Aborto Provocado por Terceiro sem Consentimento (art. 125)**: executado contra a vontade real ou presumida da gestante (reclusão de 3 a 10 anos);
- **Aborto Provocado por Terceiro com Consentimento (art. 126)**: executado com a anuência voluntária da mulher (reclusão de 1 a 4 anos). Se a gestante não for maior de 14 anos, for portadora de enfermidade psíquica ou se a anuência for obtida mediante coação ou fraude, a concordância é nula, tipificando-se o artigo 125.

O artigo 128 elenca as hipóteses de **Aborto Legal** praticado privativamente por médico:
1. *Aborto Necessário/Terapêutico (inciso I)*: única alternativa clínica disponível para salvaguardar a vida da gestante em risco iminente;
2. *Aborto Humanitário/Sentimental (inciso II)*: gestação resultante de crime de estupro, precedida de consentimento expresso da vítima ou de seu responsável legal, sem necessidade de autorização judicial.

Em sede de controle concentrado de constitucionalidade, o Supremo Tribunal Federal firmou na **ADPF 54** a atipicidade do parto terapêutico antecipado de feto anencefálico. Constatada a inviabilidade extrauterina irreversível da vida fetal decorrente de má-formação congênita do encéfalo, afasta-se a incidência do direito penal protetor.

### Para fixar
- O art. 122 é crime formal e tutela a vida e a integridade perante suicídio e automutilação.
- O resultado morte ou lesão atua como circunstância qualificadora específica do art. 122.
- Induzir menor de 14 anos ou incapaz sem discernimento caracteriza homicídio por autoria mediata.
- O infanticídio exige a influência do estado puerperal durante ou logo após o trabalho de parto.
- A elementar do estado puerperal comunica-se aos partícipes e coautores por força do art. 30 do CP.
- O aborto em menor de 14 anos equipara-se à modalidade cometida sem o consentimento da gestante.
- O aborto humanitário exige gravidez decorrente de estupro e consentimento da gestante.
- O STF na ADPF 54 reconheceu a atipicidade da interrupção gestacional de feto anencéfalo.""",
        "synthetic": [
            "**Instigação ao Suicídio e Automutilação (art. 122)**: delito formal consumado com o fomento anímico ou auxílio material, prescindindo de resultado corporal prévio.",
            "**Qualificadoras no Artigo 122**: a produção efetiva de lesões corporais severas ou a causação da morte exasperam a sanção em moldes qualificadores.",
            "**Incapazes e Menores de 14 Anos**: induzir indivíduo privado de discernimento ao ato autodestrutivo transmuta a capitulação fática para o delito de homicídio doloso.",
            "**Infanticídio (art. 123)**: morte do nascente ou recém-nascido perpetrada pela mãe perturbada pelo estado puerperal durante ou imediatamente após o parto.",
            "**Comunicabilidade da Elementar**: o estado puerperal ostenta natureza de elementar típica, estendendo-se juridicamente ao coautor ou partícipe por força legal.",
            "**Autoaborto e Aborto por Terceiro**: criminaliza a gestante que extirpa o concepto e terceiros que atuam com ou sem consentimento gestacional válido.",
            "**Consentimento Inválido**: a anuência de gestante menor de 14 anos é juridicamente nula, convolando o fato no crime gravoso de aborto sem consentimento.",
            "**Aborto Permitido e ADPF 54**: autoriza a interrupção médica necessária e sentimental decorrente de estupro, bem como na anencefalia congênita chancelada pelo STF."
        ]
    })

    return items, summaries
