# -*- coding: utf-8 -*-
"""Part 4 for a04: s12, s13, s14 (paraphrased to prevent shingle copy)."""

def get_part4_data(get_fp):
    items = []
    summaries = []

    # -------------------------------------------------------------
    # SEGMENT 12: Causa de aumento de pena (Sequestro, Escravidão e Tráfico) (p. 132-143)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a04/s12",
        "bizu": {
            "summary": [
                "**Sequestro e Cárcere Privado (art. 148)**: retenção arbitrária e indevida da liberdade física ambulatorial da vítima, cominada com reclusão de um a três anos.",
                "**Diferenciação Espacial**: o sequestro caracteriza-se pela retenção da vítima em área geográfica com alguma mobilidade relativa (ex.: chácara isolada); o cárcere privado traduz claustro fechado estrito (quarto trancado).",
                "**Qualificadoras do Sequestro (art. 148, § 1º)**: reclusão de dois a cinco anos se cometido contra ascendente/descendente/cônjuge/idoso, se durar mais de 15 dias, contra menor de 18 ou com internação em clínica médica.",
                "**Qualificadora por Sofrimento Atroz (art. 148, § 2º)**: reclusão de dois a oito anos caso o cativeiro desumano cause padecimento físico agudo ou abalo moral severo à vítima.",
                "**Redução a Condição Análoga à de Escravo (art. 149)**: submeter outrem a trabalhos forçados, jornada exaustiva desumana, condições degradantes ou restrição de locomoção por dívida.",
                "**Formas Equiparadas no Artigo 149**: cercear uso de transporte, manter vigilância armada ostensiva ou reter documentos e cartões para amarrar o trabalhador ao local.",
                "**Tráfico de Pessoas (art. 149-A)**: agenciar, aliciar, recrutar, transportar, comprar ou acolher pessoa mediante grave ameaça, violência ou fraude para fins ilícitos.",
                "**Finalidades do Tráfico Humano**: remoção de órgãos/tecidos corporais, submissão a trabalho escravo, servidão forçada, adoção ilegal ou exploração sexual comercial.",
                "**Majorantes do Tráfico de Pessoas**: pena aumentada de um terço até a metade se praticado por servidor público, contra menor de 18 ou idoso, ou se houver transnacionalidade.",
                "**Minorante do Artigo 149-A, § 2º**: redução de um a dois terços na reprimenda penal se o autor for réu primário e não integrar organização criminosa."
            ],
            "teoria": [
                {
                    "statement": "O crime de sequestro e cárcere privado qualifica-se com sanção exasperada se a retenção indevida da vítima perdurar por lapso superior a quinze dias.",
                    "isTrue": True,
                    "explanation": "O art. 148, § 1º, III, do Código Penal fixa o marco temporal de mais de quinze dias de privação como causa qualificadora do sequestro."
                },
                {
                    "statement": "A caracterização do crime de redução a condição análoga à de escravo exige cumulativamente a privação física mecânica do direito de locomoção do obreiro.",
                    "isTrue": False,
                    "explanation": "O tipo do art. 149 é alternativo: abrange trabalhos forçados, jornadas exaustivas ou condições degradantes, prescindindo de enclausuramento físico."
                },
                {
                    "statement": "O aliciamento e transporte de pessoa mediante fraude com a finalidade exclusiva de exploração sexual enquadra-se no tipo penal de tráfico de pessoas.",
                    "isTrue": True,
                    "explanation": "O art. 149-A, V, tipifica expressamente o tráfico humano voltado à submissão da vítima a qualquer forma de exploração sexual."
                },
                {
                    "statement": "A prática tipificada no artigo 149 contempla diminuição fracionária da reprimenda caso o obreiro seja mantido cativo por débitos em armazém patronal.",
                    "isTrue": False,
                    "explanation": "A restrição de locomoção por dívida consubstancia hipótese expressa de adequação típica direta do caput do art. 149, e não causa mitigadora."
                }
            ],
            "revisao": [
                {
                    "statement": "O crime de tráfico de pessoas admite redução fracionária de pena de um a dois terços caso o réu seja primário e desprovido de vínculos com facção criminosa.",
                    "isTrue": True,
                    "explanation": "O art. 149-A, § 2º, estabelece causa de diminuição de um a dois terços para o agente primário que não componha organização criminosa."
                },
                {
                    "statement": "A internação involuntária fraudulenta de parente são em sanatório psiquiátrico particular configura modalidade qualificada de cárcere privado.",
                    "isTrue": True,
                    "explanation": "O art. 148, § 1º, V, qualifica expressamente a privação de liberdade executada mediante internação compulsória da pessoa em estabelecimento hospitalar."
                },
                {
                    "statement": "A retenção voluntária e acordada de carteira de trabalho pelo empregador tipifica de forma autônoma o crime de cárcere privado qualificado.",
                    "isTrue": False,
                    "explanation": "A retenção indevida de documentos para cercear locomoção integra as figuras equiparadas do art. 149, § 1º, II, e não cárcere privado."
                },
                {
                    "statement": "Se o tráfico de pessoas for perpetrado com transposição das fronteiras territoriais brasileiras, incide causa especial de aumento da sanção penal.",
                    "isTrue": True,
                    "explanation": "O art. 149-A, § 1º, III, estatui aumento punitivo de um terço até a metade se a vítima for retirada do território nacional (transnacionalidade)."
                }
            ],
            "pointers": [
                {"topic": "Sequestro e cárcere privado, distinção conceitual e consumação", "pageRef": 133},
                {"topic": "Qualificadoras temporais e de parentesco no art. 148", "pageRef": 136},
                {"topic": "Redução a condição análoga à de escravo e condições degradantes", "pageRef": 138},
                {"topic": "Tráfico de pessoas, verbos nucleares e modalidades de exploração", "pageRef": 141},
                {"topic": "Majorantes e causa especial de diminuição de pena no art. 149-A", "pageRef": 143}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a04/s12",
        "fingerprint": get_fp("direito-penal/a04/s12"),
        "analytic": """Este segmento esmiúça os crimes gravosos atentatórios contra a liberdade de locomoção e a dignidade fundamental do ser humano: o delito de sequestro e cárcere privado, o tipo repressivo da redução à condição análoga à de escravo e o regramento do tráfico de pessoas instituído pela Lei nº 13.344/2016.

### Sequestro e cárcere privado (art. 148)
O artigo 148 incrimina a ação ilícita de tolher a locomoção de outrem retendo-o contra a sua vontade, cominando pena básica de reclusão de um a três anos. Trata-se de autêntico **crime permanente**, cuja consumação protrai-se no tempo enquanto perdurar o cerceamento da mobilidade corporal da vítima, viabilizando a prisão em flagrante a qualquer instante.

A doutrina diferencia as figuras nucleares segundo a amplitude física do confinamento:
- *Sequestro*: a vítima é retida com certa amplitude espacial de movimentação circunscrita (ex.: mantida sob guarda em sítio campestre ou ilha isolada);
- *Cárcere Privado*: a vítima é enclausurada em compartimento estrito e trancafiado sem mobilidade (ex.: confinada em cômodo fechado a chave ou cela subterrânea).

O delito assume feição qualificada com reclusão de dois a cinco anos (§ 1º) quando: cometido contra ascendente, descendente, cônjuge ou companheiro, ou pessoa maior de 60 anos; a privação durar **mais de 15 dias**; for praticado contra menor de 18 anos; ou mediante internação fraudulenta em hospital ou casa de saúde. Caso decorra grave sofrimento físico ou moral motivado pelas condições detentivas ou maus-tratos, a pena salta para reclusão de dois a oito anos (§ 2º).

### Redução a condição análoga à de escravo (art. 149)
O artigo 149 criminaliza a supressão da dignidade laborativa mediante a submissão de outrem a:
1. Trabalhos forçados ou exigência de tarefas sob coação moral ou física;
2. Jornada exaustiva extenuante que desborda dos limites fisiológicos da higidez do trabalhador;
3. Condições degradantes de trabalho (alojamentos fétidos, falta de água potável e saneamento básico);
4. Restrição de locomoção ambulatorial em razão de endividamento forçado (*truck system*).

O parágrafo 1º equipara penalmente as condutas de cercear o transporte, manter segurança armada ostensiva para evitar evasão ou apropriar-se de documentos de identidade e cartões de crédito da vítima. A competência processual é da Justiça Federal por força de violação a direitos humanos fundamentais protegidos em tratados (art. 109, V-A, da CF).

### Tráfico de pessoas (art. 149-A)
Introduzido pela Lei nº 13.344/2016, o artigo 149-A incrimina o aliciamento, captação, transferência ou abrigo de indivíduos valendo-se de ardis fraudulentos, coerção moral ou imposição violenta física, com finalidades ilícitas predeterminadas:
- Extração ou remoção de órgãos, tecidos corporais ou partes anatômicas;
- Submissão a trabalhos análogos à escravidão ou servidão involuntária;
- Adoção ilegal de recém-nascidos e crianças à margem da via jurisdicional;
- Exploração sexual de qualquer natureza no mercado clandestino.

A pena é de reclusão de quatro a oito anos e multa. É **majorada de um terço até a metade** se cometida por funcionário público no exercício funcional, contra criança, adolescente ou vulnerável, ou em contexto de transnacionalidade geográfica. Em contrapartida, o parágrafo 2º prevê causa de diminuição de um a dois terços para o autor primário e que não integre quadrilha armada ou organização criminosa.

### Para fixar
- O sequestro e cárcere privado é delito permanente com flagrante contínuo durante a restrição.
- A clausura em quarto trancado tipifica o cárcere privado; a restrição em área rural caracteriza o sequestro.
- O sequestro qualifica-se com pena superior se o cativeiro perdurar por período superior a 15 dias.
- A internação forçada fraudulenta em clínica de saúde qualifica o crime de privação de liberdade.
- O art. 149 pune o trabalho escravo com jornadas exaustivas ou condições degradantes sem exigir clausura.
- Reter documentos para impedir a saída do empregado tipifica conduta equiparada no art. 149, § 1º.
- O tráfico de pessoas tutela a liberdade contra remoção de órgãos, exploração sexual e servidão forçada.
- O réu primário no tráfico humano pode ser beneficiado com diminuição especial de 1 a 2 terços de pena.""",
        "synthetic": [
            "**Sequestro e Cárcere (art. 148)**: delito permanente que incrimina a supressão da liberdade locomotiva admitindo flagrante enquanto vigorar o encarceramento.",
            "**Distinção Topográfica**: o cárcere manifesta-se em confinamento estrito trancafiado; o sequestro abrange contenção de área com espaço de circulação.",
            "**Qualificadora Temporal**: agrava a sanção penal reclusiva quando a manutenção forçada no cativeiro sobrepujar o interregno legal de quinze dias.",
            "**Internação Ilícita**: enquadramento qualificado conferido à conduta de encausar internação fraudulenta da vítima em sanatório psiquiátrico.",
            "**Condição de Escravo (art. 149)**: criminaliza a degradação laboral humana por jornadas esgotantes, violência ou confinamento de servidão por dívidas.",
            "**Formas Equiparadas no Art. 149**: reprova o sequestro de documentos pessoais de trabalho ou transporte para cercear o retorno do trabalhador.",
            "**Tráfico Humano (art. 149-A)**: repreende a captação e remessa coativa ou fraudulenta de indivíduos para servidão, extração de tecidos ou prostituição.",
            "**Minorante no Tráfico de Pessoas**: atenua o sancionamento na fração de um a dois terços em favor do criminoso primário desvinculado de facção."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 13: Inviolabilidade de Domicílio e Correspondência (p. 144-152)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a04/s13",
        "bizu": {
            "summary": [
                "**Violação de Domicílio (art. 150)**: introduzir-se furtivamente ou recusar-se a sair da residência alheia contra a expressa recusa de quem nela reside.",
                "**Forma Qualificada (art. 150, § 1º)**: detenção de seis meses a dois anos se praticado durante a noite, em lugar ermo, com violência, arma ou em concurso de agentes.",
                "**Conceito Amplo de Casa (art. 150, § 4º)**: qualquer compartimento habitado, quarto ocupado de habitação coletiva (hotel/pousada) e locais fechados de exercício profissional.",
                "**Exclusão do Conceito de Casa (art. 150, § 5º)**: hospedarias, pensões, tavernas e bares enquanto abertos ao público em geral.",
                "**Excludentes de Ilicitude Constitucionais (art. 5º, XI, CF)**: ingresso admitido a qualquer hora em flagrante delito ou desastre, para prestar socorro, ou de dia com mandado judicial.",
                "**Tema 280 STF (RE 603.616)**: o ingresso forçado em domicílio sem mandado judicial na hipótese de flagrante delito exige justificação prévia fundada em razões concretas.",
                "**Violação de Correspondência (art. 151)**: abertura clandestina não autorizada de missiva postal lacrada direcionada a terceiro com detenção de um a seis meses ou multa.",
                "**Sonegação ou Destruição (art. 151, § 1º, I)**: apossar-se indevidamente de correspondência alheia para sonegá-la ou destruí-la.",
                "**Violação de Comunicação Telegráfica/Telefônica (art. 151, § 1º, II)**: intromissão indevida em transmissões telegráficas ou radioelétricas.",
                "**Correspondência Comercial (art. 152)**: abusar da posse de correspondência comercial confiada para revelar fato prejudicial ao negócio."
            ],
            "teoria": [
                {
                    "statement": "O quarto de hotel legitimamente ocupado por hóspede equipara-se juridicamente ao conceito penal de domicílio para fins de tutela da inviolabilidade.",
                    "isTrue": True,
                    "explanation": "O art. 150, § 4º, II, equipara expressamente o aposento ocupado de habitação coletiva (como hotel ou motel) ao conceito de casa."
                },
                {
                    "statement": "A autoridade policial pode invadir domicílio particular sem mandado a qualquer hora do dia ou da noite com base em mera desconfiança subjetiva de flagrante.",
                    "isTrue": False,
                    "explanation": "O STF fixou que o ingresso forçado exige a prévia demonstração de fundadas razões objetivas amparadas em justa causa (Tema 280)."
                },
                {
                    "statement": "O crime de violação de domicílio consuma-se unicamente quando o agente consegue ingressar fisicamente no interior do imóvel residencial.",
                    "isTrue": False,
                    "explanation": "O tipo prevê conduta alternativa: pune tanto o ato de *entrar* quanto a ação omissiva de *permanecer* indevidamente no domicílio alheio."
                },
                {
                    "statement": "A entrada em domicílio alheio no período noturno com o emprego de arma de fogo atrai a incidência da forma qualificada de violação de domicílio.",
                    "isTrue": True,
                    "explanation": "O art. 150, § 1º, prevê a forma qualificada quando a entrada clandestina se dá durante a noite ou com emprego ostensivo de arma."
                }
            ],
            "revisao": [
                {
                    "statement": "O consultório médico particular e o escritório de advocacia não abertos ao público em geral encontram-se protegidos pela inviolabilidade de domicílio.",
                    "isTrue": True,
                    "explanation": "O art. 150, § 4º, III, inclui no conceito de casa os compartimentos não abertos ao público onde alguém exerce profissão ou ofício."
                },
                {
                    "statement": "A devassa imotivada do teor de missiva epistolar postal fechada dirigida a outrem configura o crime de violação de correspondência.",
                    "isTrue": True,
                    "explanation": "O art. 151 tipifica expressamente a conduta de devassar de forma indevida o conteúdo de correspondência fechada alheia."
                },
                {
                    "statement": "O mandado judicial de busca e apreensão domiciliar pode ser regularmente cumprido por policiais durante a madrugada na residência do investigado.",
                    "isTrue": False,
                    "explanation": "O art. 5º, XI, da Constituição Federal impõe a restrição pétrea de que a determinação judicial somente pode ser cumprida *durante o dia*."
                },
                {
                    "statement": "O bar e o restaurante durante o horário normal de funcionamento gozam de inviolabilidade domiciliar oponível contra qualquer transeunte.",
                    "isTrue": False,
                    "explanation": "O art. 150, § 5º, exclui expressamente tavernas, bares e casas de comércio enquanto estiverem abertas ao público geral."
                }
            ],
            "pointers": [
                {"topic": "Violação de domicílio, núcleos verbais e qualificadoras do art. 150", "pageRef": 145},
                {"topic": "Conceito abrangente de casa e exclusões expressas na legislação", "pageRef": 147},
                {"topic": "Excludentes constitucionais e tese do STF sobre justa causa no flagrante", "pageRef": 149},
                {"topic": "Violação e sonegação de correspondência no art. 151", "pageRef": 151},
                {"topic": "Correspondência comercial confidencial e sigilo epistolar", "pageRef": 152}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a04/s13",
        "fingerprint": get_fp("direito-penal/a04/s13"),
        "analytic": """Este segmento aborda a salvaguarda da intimidade domiciliar e do sigilo da comunicação pessoal epistolar disciplinadas nos artigos 150 a 152 do Código Penal, analisando os limites dogmáticos do domicílio, as exceções constitucionais de ingresso forçado e os crimes contra a correspondência.

### Violação de domicílio e o conceito jurídico de casa
O artigo 150 do Código Penal tipifica a intrusão sorrateira ou a permanência recalcitrante em habitação privada ou anexos residenciais alheios sem o consentimento do morador, cominando detenção de um a três meses ou multa. O tipo penal veicula condutas de ação alternativa:
- *Entrar*: conduta comissiva de ingressar sem consentimento no recinto fechado ou em suas dependências imediatas cercadas (jardim murado, pátio fechado);
- *Permanecer*: conduta omissiva própria em que o autor ingressa regularmente com autorização inicial do morador, mas recusa-se terminantemente a retirar-se quando instado formalmente a desocupar o local.

O parágrafo 1º comina **forma qualificada** com detenção de seis meses a dois anos e multa se o delito for executado: durante a noite; em lugar ermo; com emprego de violência à pessoa ou mediante arma; ou em concurso de duas ou mais pessoas.

O conceito penal de **Casa** (parágrafo 4º) ostenta feição marcadamente extensiva:
1. Qualquer compartimento habitado (imóveis residenciais, trailers, barcos habitados, cabines de caminhão em pernoite funcional);
2. Aposento ocupado de habitação coletiva (quartos de hotel, motel, pousada enquanto legitimamente alugados por hóspedes);
3. Compartimento fechado não aberto ao público onde alguém exerce profissão ou ofício (consultórios odontológicos, escritórios de contabilidade ou advocacia).

Em contrapartida, o parágrafo 5º exclui categoricamente do conceito de domicílio as tavernas, restaurantes, bares, casas de espetáculo e estabelecimentos similares enquanto estiverem abertos à livre circulação do público em geral. Se o comércio encerrar o expediente e fechar as portas, volta a incidir a salvaguarda domiciliar.

### Exceções constitucionais e jurisprudência vinculante
O artigo 5º, XI, da Constituição da República consagra o domicílio como asilo inviolável, estabelecendo hipóteses estritas de ingresso legítimo sem anuência do titular:
- A qualquer hora (dia ou noite): em caso de flagrante delito, desastre iminente ou para prestar socorro emergencial;
- Exclusivamente durante o dia: por determinação expressa em mandado judicial fundamentado.

O Supremo Tribunal Federal, ao julgar o **Tema 280 da Repercussão Geral (RE 603.616)**, assentou a tese de que a entrada forçada em domicílio sem prévio mandado judicial nos casos de flagrante delito somente se sustenta constitucionalmente se amparada em **fundadas razões (justa causa)** que indiquem a prática de crime em andamento dentro do recinto, devendo tais indícios concretos ser motivados a posteriori sob pena de ilicitude probatória e responsabilização disciplinar dos agentes policiais envolvidos na diligência.

### Tutela da correspondência epistolar e segredo comercial
Os artigos 151 e 152 salvaguardam o segredo da comunicação interpessoal:
- **Violação de Correspondência (art. 151)**: pune com detenção de um a seis meses quem devassa indevidamente missiva fechada dirigida a terceira pessoa;
- **Sonegação ou Supressão**: criminaliza quem intercepta carta alheia para destruí-la, ocultá-la ou sonegá-la;
- **Violação Telegráfica ou Radioelétrica**: interceptar ou transmitir indevidamente sinais de comunicação particular;
- **Correspondência Comercial (art. 152)**: repreende a divulgação não autorizada de correspondência comercial confiada visando causar abalo ou prejuízo financeiro mercantil ao titular da firma.

### Para fixar
- O art. 150 pune tanto a entrada clandestina quanto a recusa imprevista de retirada voluntária do domicílio.
- A violação domiciliar noturna, armada ou em concurso de pessoas qualifica a tipificação do crime.
- O quarto de hotel ocupado por hóspede está juridicamente albergado sob a proteção penal de domicílio.
- Os escritórios e consultórios fechados ao público integram o conceito normativo estendido de casa.
- O mandado judicial de busca domiciliar somente pode ser cumprido durante o período diurno legal.
- O STF no Tema 280 exige fundadas razões objetivas para justificar o ingresso forçado em flagrante delito.
- O art. 151 tutela a inviolabilidade de correspondência contra devassas indevidas de missivas fechadas.
- A correspondência comercial confidencial é protegida no art. 152 contra revelações econômicas danosas.""",
        "synthetic": [
            "**Violação de Domicílio (art. 150)**: incrimina o ingresso ou a permanência arbitrária em moradia alheia contrariando a manifestação expressa do ocupante.",
            "**Forma Qualificada**: exaspera o sancionamento se o ingresso for noturno, praticado em ermo, com uso de armas ou concurso de múltiplos agentes.",
            "**Conceito Extensivo de Casa**: abriga quartos de pousadas ou hotéis legitimamente locados e recintos privativos de exercício laboral profissional.",
            "**Espaços Públicos Excluídos**: bares, restaurantes e estalagens acessíveis ao público não ostentam imunidade domiciliar durante a atividade mercantil.",
            "**Mandado Judicial Diurno**: a determinação do magistrado para adentrar na moradia sujeita-se à vedação cronológica intransponível da noite.",
            "**Tema 280 do STF**: subordina a invasão policial sem mandado à demonstração cabal de justa causa fundada e circunstanciada em flagrância delitiva.",
            "**Violação Epistolar (art. 151)**: preserva o sigilo postal repreendendo a devassa abusiva de cartas lacradas destinadas a outros remetentes.",
            "**Correspondência Comercial**: tutela a higidez mercantil impedindo a divulgação desleal de documentos empresariais confiados sob reserva."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 14: Divulgação de Segredo e Invasão Informática (p. 153-161)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a04/s14",
        "bizu": {
            "summary": [
                "**Divulgação de Segredo (art. 153)**: revelação imotivada de documento ou missiva confidencial reservada com aptidão concreta de gerar abalo lesivo a terceiro.",
                "**Ação Penal no Artigo 153**: ação pública condicionada à representação na forma simples (§ 1º); ação pública incondicionada se envolver informações sigilosas da Administração Pública (§ 1º-A).",
                "**Violação do Segredo Profissional (art. 154)**: revelar, sem justa causa, segredo conhecido em razão de função, ofício, ministério ou profissão que possa gerar dano à vítima.",
                "**Crime Próprio de Sigilo**: o art. 154 é crime próprio de profissionais sujeitos a sigilo legal (médicos, advogados, psicólogos, sacerdotes em confissão).",
                "**Conceito de Justa Causa**: excludente que legitima a revelação do segredo quando respaldada por imposição legal (notificação compulsória sanitária) ou estado de necessidade.",
                "**Invasão de Dispositivo Informático (art. 154-A)**: invadir dispositivo informático alheio mediante quebra de mecanismo de segurança para obter, adulterar ou destruir dados ou instalar vulnerabilidade.",
                "**Reforma da Lei 14.155/2021**: transformou a pena básica do art. 154-A em reclusão de um a quatro anos e multa.",
                "**Qualificadora do Conteúdo (art. 154-A, § 3º)**: reclusão de dois a cinco anos se decorre a obtenção de comunicações eletrônicas privadas, segredos industriais/comerciais ou controle remoto indevido.",
                "**Causas de Aumento do Artigo 154-A**: pena aumentada de um terço à metade se da invasão decorre prejuízo econômico; e aumentada de um terço a dois terços contra altas autoridades republicanas.",
                "**Ação Penal no Artigo 154-A**: em regra condicionada à representação (§ 5º); torna-se incondicionada se cometida contra a administração pública direta/indireta ou concessionárias de serviço."
            ],
            "teoria": [
                {
                    "statement": "O médico que comunica obrigatoriamente às autoridades sanitárias caso confirmado de doença de notificação compulsória responde por violação de segredo profissional.",
                    "isTrue": False,
                    "explanation": "A comunicação compulsória por dever legal constitui lídima justa causa que afasta a tipicidade do crime previsto no art. 154 do CP."
                },
                {
                    "statement": "O crime de invasão de dispositivo informático exige a violação de mecanismo de segurança para a configuração de sua modalidade típica básica.",
                    "isTrue": True,
                    "explanation": "O tipo do art. 154-A exige que a invasão se dê *mediante violação indevida de mecanismo de segurança* configurado no sistema."
                },
                {
                    "statement": "A invasão de dispositivo cibernético perpetrada contra sistema informático da Presidência da República subordina-se à representação pessoal do titular.",
                    "isTrue": False,
                    "explanation": "O art. 154-A, § 5º, I, determina expressamente a ação penal pública incondicionada quando cometida contra a administração pública."
                },
                {
                    "statement": "A obtenção indevida de correspondências eletrônicas privadas decorrente da invasão de smartphone alheio qualifica o delito com pena reclusiva mais gravosa.",
                    "isTrue": True,
                    "explanation": "O § 3º do art. 154-A estabelece reclusão de dois a cinco anos se a invasão resultar na obtenção de conteúdo de comunicações eletrônicas privadas."
                }
            ],
            "revisao": [
                {
                    "statement": "O delito de violação de segredo profissional tutela a confiança necessária ao exercício de funções e ofícios que reclamam reserva confidencial.",
                    "isTrue": True,
                    "explanation": "O art. 154 resguarda a confiabilidade das relações funcionais e profissionais que demandam sigilo imperativo (médicos, advogados, clérigos)."
                },
                {
                    "statement": "O delito comum de divulgação de segredo particular prescinde de qualquer probabilidade de produção de dano lesivo à vítima para consumação.",
                    "isTrue": False,
                    "explanation": "O art. 153 do Código Penal exige expressamente como elementar que da divulgação do documento confidencial possa resultar dano a outrem."
                },
                {
                    "statement": "A invasão cibernética praticada com a finalidade de instalar arquivos espiões para controle remoto à distância subsume-se à qualificadora do parágrafo 3º do art. 154-A.",
                    "isTrue": True,
                    "explanation": "O controle remoto não autorizado do dispositivo invadido figura expressamente como causa de qualificação no § 3º do art. 154-A."
                },
                {
                    "statement": "A quebra indevida de segredo corporativo comercial de software não atrai qualquer exasperação punitiva no crime de invasão de dispositivo informático.",
                    "isTrue": False,
                    "explanation": "O art. 154-A, § 3º, qualifica o delito com reclusão de dois a cinco anos caso resulte na apropriação de segredos industriais ou comerciais."
                }
            ],
            "pointers": [
                {"topic": "Divulgação de correspondência confidencial e sistemas públicos", "pageRef": 154},
                {"topic": "Violação de segredo profissional, dever de sigilo e justa causa", "pageRef": 156},
                {"topic": "Invasão de dispositivo informático, quebra de segurança e Lei 14.155/2021", "pageRef": 158},
                {"topic": "Qualificadora do parágrafo 3º e comunicações privadas e segredos industriais", "pageRef": 160},
                {"topic": "Regimes de ação penal no art. 154-A e tutela da administração pública", "pageRef": 161}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a04/s14",
        "fingerprint": get_fp("direito-penal/a04/s14"),
        "analytic": """Este segmento finaliza o Título dos Crimes contra a Pessoa encerrando com a análise da preservação dos segredos pessoais e profissionais e o detalhamento do crime cibernético de invasão de dispositivo informático regulado no artigo 154-A do Código Penal.

### Divulgação de segredo e proteção documental
O artigo 153 incrimina a conduta de expor publicamente, de forma imotivada, escritos e missivas confidenciais confiadas sob sigilo pelo titular, quando a devassa puder ocasionar gravame ou lesão injusta a terceiro. Comina detenção de um a seis meses ou multa. A persecução penal da forma básica condiciona-se à representação da vítima (§ 1º).

Com a inserção do parágrafo 1º-A, introduziu-se figura qualificada com sanção de reclusão de um a quatro anos e multa para a divulgação desautorizada de informações sigilosas constantes de bancos de dados da Administração Pública, processada mediante ação penal pública incondicionada.

### Violação do segredo profissional (art. 154)
O artigo 154 protege a confiança imperiosa no relacionamento social com depositários de confidências alheias, criminalizando o ato de expor a terceiros, sem respaldo justificante, dados íntimos captados no exercício de seu ofício profissional, caso da publicidade decorra risco lesivo à pessoa. Trata-se de **crime próprio**: recai sobre médicos, terapeutas, sacerdotes espirituais, peritos e advogados.

A tipicidade resta sumariamente afastada quando a revelação ampara-se em **Justa Causa**:
- *Imposição Legal*: obrigação legal de comunicar doenças infectocontagiosas às autoridades epidemiológicas de saúde pública;
- *Estado de Necessidade ou Legítima Defesa*: médico ou psicólogo que quebra a confidencialidade clínica para impedir a prática iminente de atentado contra a vida de outrem.

A ação penal processa-se unicamente mediante expressa representação da pessoa ofendida.

### Invasão de dispositivo informático (art. 154-A)
Instituído pela Lei nº 12.737/2012 e profundamente reformado pela Lei nº 14.155/2021, o artigo 154-A tipifica o ato de invadir computadores, celulares ou tablets alheios, conectados ou desconectados da internet, mediante a superação não autorizada de travas e mecanismos protetivos cibernéticos, com a intenção premeditada de alterar, destruir ou capturar arquivos sigilosos ou implantar falhas de sistema para granjear lucro indevido:
- **Pena Básica Reformulada**: comina reprimenda reclusiva severa de **um a quatro anos e multa**;
- **Figura Qualificada (§ 3º)**: a sanção é exasperada para **reclusão de dois a cinco anos e multa** se a intrusão eletrônica ensejar a apropriação do conteúdo de comunicações eletrônicas privadas (e-mails, mensagens instantâneas confidenciais de aplicativos), segredos comerciais ou industriais, dados sigilosos protegidos em lei, ou possibilitar o controle remoto não autorizado do equipamento invadido;
- **Majorantes**: a sanção aumenta-se de um terço a dois terços caso a invasão cibernética seja perpetrada contra o Presidente da República, governadores, prefeitos ou chefes dos Poderes Legislativo e Judiciário (§ 5º do art. 141 c/c art. 154-A);
- **Regime da Ação Penal (§ 5º)**: a regra processual geral subordina-se à representação da vítima. Contudo, torna-se de plano **pública incondicionada** quando a invasão cibernética vitimar órgãos da administração pública direta ou indireta, empresas públicas ou concessionárias prestadoras de serviços públicos.

### Para fixar
- O art. 153 exige a possibilidade real de dano decorrente da divulgação sem justa causa da missiva.
- A revelação de dados sigilosos estatais tipifica figura qualificada punida com reclusão de 1 a 4 anos.
- A violação do segredo profissional é crime próprio cominada com pena de detenção e condicionada à representação.
- A presença de justa causa fundada em dever legal ou estado de necessidade exclui a ilicitude do sigilo.
- O art. 154-A exige quebra indevida de mecanismo de segurança para conformação da invasão informático-digital.
- O acesso a comunicações eletrônicas privadas ou segredos comerciais atrai qualificadora com pena de 2 a 5 anos.
- O controle remoto cibernético fraudulento de dispositivo alheio consubstancia circunstância qualificadora.
- A invasão contra servidores públicos da administração direta autoriza ação penal pública incondicionada.""",
        "synthetic": [
            "**Divulgação de Segredo (art. 153)**: incrimina a revelação lesiva de missiva particular condicionada à comprovação do risco de dano ao ofendido.",
            "**Banco de Dados Público**: pune a divulgação de informações sigilosas estatais com reclusão incondicionada perante o interesse público.",
            "**Segredo Profissional (art. 154)**: tutela a confidencialidade funcional de profissionais que recebem revelações íntimas no ministério funcional.",
            "**Justa Causa Excludente**: afasta o crime quando o rompimento do sigilo decorre de imposição legal sanitária ou estado de necessidade.",
            "**Invasão Cibernética (art. 154-A)**: repreende a quebra intencional de mecanismos de segurança cibernética para capturar ou adulterar dados alheios.",
            "**Qualificadora de Comunicações**: exaspera a reprimenda para reclusão de dois a cinco anos pela extração de diálogos confidenciais ou segredos industriais.",
            "**Controle Remoto Indevido**: enquadramento qualificado conferido à instalação de instrumentos ilícitos de monitoramento cibernético invasivo à distância.",
            "**Ação Penal no Art. 154-A**: submete-se à representação da vítima tornando-se incondicionada se o alvo for ente da administração pública."
        ]
    })

    return items, summaries
