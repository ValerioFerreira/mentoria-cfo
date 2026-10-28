# -*- coding: utf-8 -*-
"""Part 1 for a06: s01, s02, s03, s04 (Crimes contra a Liberdade Sexual e Vulneráveis)."""

def get_part1_data(get_fp):
    items = []
    summaries = []

    # -------------------------------------------------------------
    # SEGMENT 01: Estupro e Assédio Sexual (p. 2-10)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a06/s01",
        "bizu": {
            "summary": [
                "**Estupro (art. 213)**: constrangimento imposto a terceiro por emprego de força física ou coação moral irresistível, voltado à consumação de penetração genital ou atos lúbricos similares (reclusão de 6 a 10 anos).",
                "**Unificação dos Tipos (Lei 12.015/2009)**: a conjunção carnal e o atentado violento ao pudor foram fundidos no mesmo artigo 213 do estatuto repressivo.",
                "**Crime Comum Pleno**: a conduta típica pode ser perpetrada por homem ou mulher contra vítima masculina ou feminina (crime comum quanto ao sujeito ativo e passivo).",
                "**Atos Libidinosos Diversos**: compreendem toques íntimos despidos de consentimento, sexo oral, sexo anal ou introdução forçada de objetos na genitália alheia.",
                "**Estupro Qualificado por Lesão ou Idade (§ 1º)**: reclusão de oito a doze anos se decorre lesão grave ou se a vítima tem entre 14 e 18 anos incompletos.",
                "**Estupro Qualificado pela Morte (§ 2º)**: reclusão de doze a trinta anos se da violência infligida resulta a morte preterdolosa da pessoa ofendida.",
                "**Hediondez do Estupro**: o crime de estupro em todas as suas modalidades (simples, majorado ou qualificado) ostenta natureza de crime hediondo na Lei 8.072/1990.",
                "**Assédio Sexual (art. 216-A)**: constranger outrem visando obter favorecimento sexual valendo-se da superioridade hierárquica inerente ao trabalho (detenção de 1 a 2 anos).",
                "**Elemento Funcional do Assédio**: exige relação formal de ascendência laboral ou subordinação funcional entre o infrator e a vítima subordinada."
            ],
            "teoria": [
                {
                    "statement": "O delito de estupro constitui crime próprio quanto ao sujeito ativo, somente podendo ser praticado por pessoa do sexo masculino.",
                    "isTrue": False,
                    "explanation": "Com a Lei 12.015/2009, o estupro passou a ser crime comum, podendo ser praticado por qualquer pessoa contra qualquer vítima."
                },
                {
                    "statement": "A prática de conjunção carnal violenta e a submissão concomitante a sexo anal forçado no mesmo contexto fático caracterizam crime único de estupro.",
                    "isTrue": True,
                    "explanation": "O STJ consolidou que atos libidinosos diversos e conjunção carnal praticados no mesmo episódio consubstanciam crime único de estupro."
                },
                {
                    "statement": "O crime de assédio sexual exige para sua subsunção que a investida seja perpetrada entre colegas de trabalho que ostentam idêntico nível funcional.",
                    "isTrue": False,
                    "explanation": "O art. 216-A exige expressamente a prevalência de superioridade hierárquica ou ascendência funcional decorrente de emprego ou ofício."
                },
                {
                    "statement": "O estupro qualificado pela morte consubstancia crime hediondo segundo expressa previsão na legislação penal extravagante.",
                    "isTrue": True,
                    "explanation": "O estupro em todas as suas configurações típicas integra o rol de crimes hediondos previsto na Lei nº 8.072/1990."
                }
            ],
            "revisao": [
                {
                    "statement": "O crime de assédio sexual consuma-se unicamente quando a vítima cede às investidas do superior hierárquico praticando o ato libidinoso almejado.",
                    "isTrue": False,
                    "explanation": "O assédio sexual é crime formal que atinge a consumação com o constrangimento insistente, prescindindo da aceitação da vítima."
                },
                {
                    "statement": "A prática de estupro contra vítima com dezesseis anos de idade atrai a incidência de qualificadora específica com sanção de reclusão de oito a doze anos.",
                    "isTrue": True,
                    "explanation": "O art. 213, § 1º, prevê pena de reclusão de oito a doze anos se a vítima é menor de dezoito e maior de catorze anos."
                },
                {
                    "statement": "A prática de ato libidinoso sem violência real praticado por professor contra aluna maior de dezoito anos amolda-se formalmente ao assédio sexual.",
                    "isTrue": False,
                    "explanation": "O assédio sexual exige ascendência no trabalho ou cargo; entre professor e aluno maior incide no máximo importunação sexual ou outro tipo."
                },
                {
                    "statement": "O resultado morte decorrente da violência no crime de estupro afasta a competência de julgamento pelo plenário do Tribunal do Júri.",
                    "isTrue": True,
                    "explanation": "O estupro qualificado pela morte é crime preterdoloso contra a dignidade sexual, julgado privativamente pelo juiz togado singular."
                }
            ],
            "pointers": [
                {"topic": "Estupro, unificação típica da Lei 12.015/2009 e atos libidinosos", "pageRef": 3},
                {"topic": "Qualificadoras de lesão corporal grave e morte no art. 213", "pageRef": 5},
                {"topic": "Assédio sexual, ascendência hierárquica e natureza formal no art. 216-A", "pageRef": 7},
                {"topic": "Hediondez dos crimes contra a liberdade sexual e julgamento singular", "pageRef": 9}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a06/s01",
        "fingerprint": get_fp("direito-penal/a06/s01"),
        "analytic": """Este segmento inaugura a tutela da dignidade sexual no estatuto repressivo, examinando com minúcias dogmáticas a unificação típica operada pela Lei nº 12.015/2009, as qualificadoras pelo resultado e a figura do assédio sexual funcional.

### Estupro e a unificação típica (artigo 213)
A reforma penal promovida pela Lei nº 12.015/2009 extirpou o antigo dualismo punitivo entre o estupro e o atentado violento ao pudor, fundindo ambas as manifestações em preceito normativo unitário:
- O artigo 213 sanciona quem constrange terceira pessoa, mediante o emprego de violência física efetiva ou grave ameaça moral intimidatória, a tolerar a conjunção carnal (introdução do pênis na cavidade vaginal) ou a suportar a realização de qualquer outro ato libidinoso heterogêneo (sexo anal, sexo oral, manipulações forçadas de regiões erógenas ou introdução de objetos na genitália alheia);
- *Sujeitos Ativo e Passivo*: superou-se a limitação biológica histórica. Trata-se de **crime comum**, suscetível de ser cometido por homens ou mulheres, e que pode ter como vítima qualquer ser humano vivo independente de seu gênero;
- *Concurso de Atos no Mesmo Episódio*: o Superior Tribunal de Justiça firmou entendimento pacificado de que a imposição de conjunção carnal forçada e de atos libidinosos orais ou anais perpetrados contra a mesma ofendida no mesmo contexto fático unitário configura **crime único de estupro**, funcionando a pluralidade de condutas lascivas como circunstância judicial desfavorável na fixação da pena-base.

### Figuras qualificadas e hediondez (parágrafos 1º e 2º)
O legislador fixou patamares sancionatórios exasperados para desfechos gravosos decorrentes da coação:
- *Parágrafo 1º*: comina reprimenda de reclusão de **oito a doze anos** caso da violência infligida decorra lesão corporal grave ou gravíssima, ou se a pessoa vitimada contar com idade compreendida entre catorze e dezoito anos incompletos;
- *Parágrafo 2º*: comina reclusão de **doze a trinta anos** na hipótese de a violência corporal resultar no evento morte a título preterdoloso ou com dolo eventual;
- *Competência e Regime Hediondo*: todas as hipóteses típicas do estupro (consumado ou tentado, simples ou qualificado) compõem o catálogo taxativo dos **crimes hediondos** da Lei nº 8.072/1990. Na ocorrência do resultado morte previsto no § 2º, a persecução penal processa-se perante o **juiz togado singular**, visto tratar-se de crime preterdoloso patrimonial-sexual e não de delito doloso contra a vida submetido ao Tribunal do Júri.

### Assédio sexual funcional (artigo 216-A)
Inserido pela Lei nº 10.224/2001, o artigo 216-A pune quem constrange outrem com a finalidade exclusiva de amealhar vantagem ou concessão sexual, prevalecendo-se da condição de superior hierárquico inerente a ofício, emprego ou função:
- *Elemento Fiduciário*: pressupõe subordinação funcional e ascendência jurídica ou fática direta entre o empregador/chefe e a pessoa subordinada;
- *Natureza Formal*: atinge a consumação instantânea no instante em que o agressor emite o constrangimento chantagista, sendo desnecessário que a vítima sucumba ou execute a lascívia pretendida;
- *Causa de Aumento (§ 2º)*: a pena de detenção de um a dois anos sofre exasperação de até um terço se o fato for praticado contra menor de dezoito anos.

### Para fixar
- A Lei 12.015/2009 unificou a penetração vaginal e os atos libidinosos no art. 213 do Código Penal.
- O estupro é crime comum, admitindo homens e mulheres indistintamente como autores e vítimas.
- Conjunção carnal e ato libidinoso praticados no mesmo episódio fático configuram crime único.
- O estupro tem pena de oito a doze anos se a vítima tiver entre 14 e 18 anos ou sofrer lesão grave.
- A morte no estupro comina reclusão de doze a trinta anos sob julgamento privativo do juiz singular.
- O estupro é crime hediondo em todas as suas modalidades consumadas ou tentadas na Lei 8.072/1990.
- O assédio sexual exige superioridade hierárquica no ambiente de trabalho e consuma-se com o constrangimento.
- A concordância da vítima com as investidas sexuais é prescindível para consumação do art. 216-A.""",
        "synthetic": [
            "**Estupro Unificado (art. 213)**: fusão típica incriminando conjunção carnal ou ato libidinoso forçado por violência com sanção de seis a dez anos.",
            "**Crime Comum Pleno**: titularidade ativa e passiva aberta a pessoas de qualquer gênero suprimindo a antiga restrição masculina da cópula.",
            "**Crime Único no Mesmo Contexto**: o STJ reconhece delito único na concorrência sucessiva de penetração vaginal e atos libidinosos no mesmo ato.",
            "**Qualificadora Etária e Lesão (§ 1º)**: apenamento de oito a doze anos incidente se a ofendida contar entre 14 e 18 anos ou suportar lesão corporal severa.",
            "**Morte no Estupro (§ 2º)**: desfecho letal comina reclusão gravosa de doze a trinta anos sob jurisdição privativa do magistrado togado singular.",
            "**Hediondez Plena**: todas as figuras do estupro integram o catálogo de crimes hediondos inafiançáveis e insuscetíveis de anistia legal.",
            "**Assédio Sexual (art. 216-A)**: constrangimento libidinoso fundado no abuso de superioridade hierárquica laboral cominando detenção formal.",
            "**Consumação Antecipada do Assédio**: aperfeiçoa-se com a pressão coercitiva psicológica prescindindo da concessão de favores sexuais pelo ofendido."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 02: Violação Sexual Fraudulenta e Importunação (p. 11-21)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a06/s02",
        "bizu": {
            "summary": [
                "**Violação Sexual Mediante Fraude (art. 215)**: consumação de cópula ou atos lascivos mediante artifício ardiloso, dissimulação médica ou falsidade que induz a vítima a equívoco e nulifica seu discernimento espontâneo.",
                "**Mecanismo Fraudulento no Art. 215**: o consentimento da vítima existe faticamente, porém encontra-se viciado por induzimento a erro quanto à pessoa ou à natureza do procedimento.",
                "**Distinção Estupro versus Violação Fraudulenta**: no estupro não há anuência ante o emprego de coação violenta física; na violação há consentimento aparente viciado por engodo ardiloso.",
                "**Importunação Sexual (art. 215-A)**: perpetração de atos corporais lubríficos não consentidos (como toques voluptuosos, apalpadas ou ejaculações) em desfavor de pessoa específica sem emprego de grave ameaça expressa (reclusão de 1 a 5 anos).",
                "**Origem da Lei 13.718/2018**: tipificou condutas invasivas graves em transporte coletivo urbano que outrora eram tratadas de forma branda como mera contravenção penal de importunação ao pudor.",
                "**Subsidiariedade Expressa do Art. 215-A**: incide apenas se a conduta libidinosa perpetrada não constituir crime de maior gravidade (como estupro violento ou vulnerável).",
                "**Consumação da Importunação**: delito comum que atinge sua consumação instantânea com a realização do toque lascivo invasivo sem a concordância da pessoa visada.",
                "**Ação Penal Incondicionada**: tanto a violação sexual mediante fraude quanto a importunação sexual são processadas exclusivamente por ação penal pública incondicionada."
            ],
            "teoria": [
                {
                    "statement": "O médico que realiza toques libidinosos não terapêuticos na paciente afirmando tratar-se de procedimento ginecológico padrão responde por estupro de vulnerável.",
                    "isTrue": False,
                    "explanation": "A utilização de falsa justificativa clínica para enganar paciente consciente e orientada amolda-se à violação sexual mediante fraude (art. 215)."
                },
                {
                    "statement": "O ato consistente em ejacular sobre as vestes de passageira em vagão de transporte público sem seu consentimento tipifica o crime de importunação sexual.",
                    "isTrue": True,
                    "explanation": "A conduta consubstancia prática direta de ato libidinoso não consentido sem o emprego de violência ou ameaça grave, amoldando-se ao art. 215-A."
                },
                {
                    "statement": "O crime de importunação sexual introduzido pela Lei 13.718/2018 comina sanção punitiva exclusiva de detenção em regime aberto domiciliar.",
                    "isTrue": False,
                    "explanation": "O art. 215-A estabelece expressamente a pena de reclusão de um a cinco anos para a importunação sexual."
                },
                {
                    "statement": "O crime de violação sexual mediante fraude difere do estupro porque na violação o consentimento da vítima é obtido mediante ardil e engano.",
                    "isTrue": True,
                    "explanation": "No estupro o consentimento é suprimido por violência; na violação sexual fraudulenta a vítima consente, mas sua vontade está viciada pelo erro."
                }
            ],
            "revisao": [
                {
                    "statement": "A revogação do artigo 61 da Lei das Contravenções Penais pela Lei 13.718/2018 gerou abolitio criminis para todas as apalpadas desautorizadas.",
                    "isTrue": False,
                    "explanation": "Houve princípio da continuidade normativo-típica, passando tais comportamentos invasivos a configurar o crime autônomo do art. 215-A do CP."
                },
                {
                    "statement": "A prática de importunação sexual perpetrada contra criança menor de doze anos amolda-se tipicamente ao delito de estupro de vulnerável.",
                    "isTrue": True,
                    "explanation": "Pela subsidiariedade expressa do art. 215-A, sendo a vítima menor de 14 anos, o ato atrai a incidência do crime mais grave do art. 217-A."
                },
                {
                    "statement": "Na violação sexual mediante fraude, a ameaça de demissão empregada pelo chefe compele a vítima a manter relações sexuais.",
                    "isTrue": False,
                    "explanation": "A intimidação patronal configura grave ameaça típica de estupro ou assédio sexual; a violação do art. 215 reclama o uso de fraude e engano."
                },
                {
                    "statement": "O crime de importunação sexual prescinde de conjunção carnal, consumando-se com a prática de qualquer ato libidinoso sem consentimento.",
                    "isTrue": True,
                    "explanation": "O núcleo do art. 215-A abrange qualquer ato lúbrico ou voluptuoso realizado contra a pessoa sem a respectiva anuência fática."
                }
            ],
            "pointers": [
                {"topic": "Violação sexual mediante fraude e vício de consentimento no art. 215", "pageRef": 12},
                {"topic": "Hipóteses fáticas de engodo da vítima e distinção com estupro", "pageRef": 15},
                {"topic": "Importunação sexual da Lei 13.718/2018 e atos em transportes no art. 215-A", "pageRef": 17},
                {"topic": "Subsidiariedade expressa e absorção por crimes hediondos", "pageRef": 20}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a06/s02",
        "fingerprint": get_fp("direito-penal/a06/s02"),
        "analytic": """Este segmento esmiúça as tipificações que resguardam a higidez e a liberdade sexual em cenários nos quais não ocorre o emprego de violência corporal: o crime de violação sexual mediante fraude (artigo 215) e a figura da importunação sexual (artigo 215-A do Código Penal).

### Violação sexual mediante fraude (artigo 215)
O artigo 215 criminaliza a execução de conjunção carnal ou ato libidinoso quando viabilizada pelo emprego de manobras ardilosas ou artifícios fraudulentos que comprometam a autodeterminação volitiva da pessoa ofendida, cominando reclusão de dois a seis anos:
- *Mecanismo do Engodo*: ao revés do delito de estupro, **inexiste coação física bruta ou ameaça grave**. O sujeito passivo exterioriza aquiescência fática com a realização da intimidade corporal, contudo essa vontade acha-se irremediavelmente maculada por falsa representação da realidade construída dolosamente pelo autor;
- *Casuística Tradicional*:
  1. *Substituição de Pessoa*: o agente adentra quarto escurecido e deita-se ao lado da vítima fingindo ser o seu parceiro habitual;
  2. *Disfarce Profissional ou Espiritual*: líderes místicos ou terapeutas que persuadem a vítima a crer que toques ginecológicos desnecessários consubstanciam rito obrigatório de bênção ou procedimento profilático de saúde;
- *Causa de Aumento (§ 1º)*: eleva-se a sanção na fração de metade se o delito é impulsionado por promessa de recompensa pecuniária ou em virtude de coabitação residencial.

### Importunação sexual (artigo 215-A)
Criado no ordenamento penal pela Lei nº 13.718/2018 para suprimir intolerável impunidade fática, o preceito do artigo 215-A comina sanção punitiva de **reclusão de um a cinco anos** para a conduta de realizar toque lascivo corporal desprovido de anuência em face de terceiro visando saciar voluptuosidade própria ou de outrem:
- *Demanda Social e Histórico*: a inovação veio combater atitudes invasivas reiteradas em coletivos, metrôs e logradouros densos (passadas de mão repentinas, beijos roubados com força, fricções genitais desautorizadas e ejaculações em vestimentas femininas), as quais anteriormente eram enquadradas na quase inócua contravenção de importunação ofensiva ao pudor (artigo 61 da LCP, devidamente revogado);
- *Cláusula de Subsidiariedade*: o preceito normativo aplica-se expressamente apenas se a infração não corporificar delito de superior gravidade. Desse modo, se o autor subjuga fisicamente a vítima por força corporal para consumar o toque íntimo, opera-se o crime de estupro; caso o ato recaia sobre infante menor de 14 anos ou pessoa desacordada, a subsunção amolda-se imperativamente ao estupro de vulnerável (artigo 217-A).

### Quadro comparativo da tutela sexual
1. **Estupro (artigo 213)**: a oposição da vítima é suplantada por força muscular ou ameaça intimidadora, inexistindo consentimento;
2. **Violação Fraudulenta (artigo 215)**: a vítima externa assentimento formal, porém fundado em engodo, dissimulação ou fraude que distorce a verdade;
3. **Importunação Sexual (artigo 215-A)**: inexiste coação violenta ostensiva nem ardil ardiloso prévio, mas sim uma investida física lasciva abrupta e invasiva desprovida de prévia autorização.

### Para fixar
- A violação sexual fraudulenta pune a conjunção ou ato libidinoso com consentimento viciado por erro.
- A fraude médica ou espiritual que induz a paciente em erro sexual tipifica o art. 215 do CP.
- A importunação sexual (art. 215-A) pune atos libidinosos sem consentimento com reclusão de 1 a 5 anos.
- O art. 215-A revogou a antiga contravenção penal trazendo tutela criminal aos abusos em transporte.
- O crime de importunação sexual possui cláusula de subsidiariedade expressa em relação ao estupro.
- Se houver violência física para beijar ou tocar a vítima, o crime é estupro e não importunação.
- Se a importunação recair sobre menor de 14 anos, o fato configura estupro de vulnerável.
- Os crimes de violação fraudulenta e importunação sexual são processados mediante ação pública incondicionada.""",
        "synthetic": [
            "**Violação Fraudulenta (art. 215)**: ato sexual consentido pela vítima cujo consentimento está juridicamente viciado por fraude substancial ou engano.",
            "**Dolo de Engodo**: abrange simulações sobre a identidade do parceiro na penumbra ou falsa roupagem de rito terapêutico curativo ginecológico.",
            "**Importunação Sexual (art. 215-A)**: tipifica a prática abrupta de atos lascivos desautorizados sem uso de agressão corporal violenta consumando reclusão.",
            "**Tutela no Transporte Público**: resposta penal contundente aos episódios de ejaculação e toques corporais forçados em ônibus e estações urbanas.",
            "**Subsidiariedade Típica**: atua como preceito subsidiário cedendo passagem perante infrações mais gravosas de estupro violento ou vulnerabilidade.",
            "**Violência Transmuta o Tipo**: a contenção física da vítima para beijo forçado desborda da importunação convolando-se em estupro consumado.",
            "**Vulnerabilidade Transmuta o Tipo**: se o ato lascivo sem anuência atingir incapaz ou menor de catorze anos, opera-se o estupro de vulnerável.",
            "**Persecução Incondicionada**: a ação penal é pública irrenunciável promovida compulsoriamente pelo Ministério Público perante a Justiça."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 03: Estupro de Vulnerável e Súmulas Relevantes (p. 22-34)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a06/s03",
        "bizu": {
            "summary": [
                "**Estupro de Vulnerável (art. 217-A, caput)**: imposição de penetração carnal ou atos libidinosos em desfavor de menores desprovidos de 14 anos completos (reclusão de 8 a 15 anos).",
                "**Presunção Absoluta de Vulnerabilidade**: critério cronológico puramente biológico; a menoridade de 14 anos gera presunção jurídica iure et de iure de incapacidade sexual.",
                "**Súmula 593 do STJ**: a subsunção típica ao abuso de vulnerável independe de suposta anuência da ofendida, bagagem sexual pretérita ou vigência de namoro entre as partes.",
                "**Incapacidade de Resistência (§ 1º)**: incorre nas mesmas penas quem pratica o ato com pessoa portadora de enfermidade ou deficiência mental, ou que não pode oferecer resistência.",
                "**Vulnerabilidade Temporária**: abrange o coma alcoólico profundo, sonambulismo, efeito de drogas pesadas ou anestesia clínica cirúrgica que anule a defesa da vítima.",
                "**Qualificadoras de Lesão e Morte**: reclusão de dez a vinte anos se resulta lesão grave (§ 3º) e doze a trinta anos se resulta a morte preterdolosa (§ 4º).",
                "**Hediondez Integral**: todas as figuras do estupro de vulnerável (simples ou qualificadas) são crimes hediondos na Lei nº 8.072/1990.",
                "**Julgamento por Juiz Togado Singular**: o resultado morte decorrente do estupro de vulnerável não vai a júri popular, mantendo-se na vara criminal comum."
            ],
            "teoria": [
                {
                    "statement": "O consentimento espontâneo manifestado por vítima de doze anos descaracteriza a tipicidade formal do crime de estupro de vulnerável.",
                    "isTrue": False,
                    "explanation": "O consentimento da vítima menor de 14 anos é juridicamente nulo e irrelevante, consoante o art. 217-A, § 5º, do CP e Súmula 593 do STJ."
                },
                {
                    "statement": "A prática de atos libidinosos contra pessoa desmaiada em decorrência de embriaguez alcoólica voluntária tipifica o crime do art. 217-A, § 1º.",
                    "isTrue": True,
                    "explanation": "A impossibilidade de oferecer resistência, ainda que decorrente de embriaguez provocada pela própria vítima, amolda-se à vulnerabilidade típica."
                },
                {
                    "statement": "A prévia prostituição ou relacionamento amoroso anterior afasta a hediondez da conduta imputada a quem mantém relações com menor de 14 anos.",
                    "isTrue": False,
                    "explanation": "A Súmula 593 do STJ consolida que experiência sexual anterior ou namoro não afastam a consumação hedionda do estupro de vulnerável."
                },
                {
                    "statement": "A ocorrência do óbito decorrente culposamente de lesões físicas em estupro de vulnerável qualifica o delito com reclusão de 12 a 30 anos.",
                    "isTrue": True,
                    "explanation": "O art. 217-A, § 4º, comina pena preterdolosa de 12 a 30 anos de reclusão se da conduta resulta morte."
                }
            ],
            "revisao": [
                {
                    "statement": "O casamento civil celebrado entre autor e a menor vítima de 13 anos opera extinção da punibilidade do delito de estupro de vulnerável.",
                    "isTrue": False,
                    "explanation": "A revogação do antigo inciso VII do art. 107 do CP aboliu em definitivo a extinção da punibilidade pelo casamento."
                },
                {
                    "statement": "A presunção de vulnerabilidade no crime do artigo 217-A do Código Penal é absoluta, não admitindo dilação probatória em contrário.",
                    "isTrue": True,
                    "explanation": "A imaturidade é presumida por ficção legal absoluta (iure et de iure) em virtude da idade cronológica menor de 14 anos."
                },
                {
                    "statement": "A consumação do estupro de vulnerável exige necessariamente contato carnal com rompimento himenal mediante conjunção carnal.",
                    "isTrue": False,
                    "explanation": "O art. 217-A pune expressamente conjunção carnal ou a prática de qualquer outro ato libidinoso heterogêneo."
                },
                {
                    "statement": "O réu que prova ter agido induzido por erro de tipo inevitável em face de documento falso sobre a idade da vítima pode ser absolvido.",
                    "isTrue": True,
                    "explanation": "O erro de tipo essencial invencível (art. 20 do CP) exclui o dolo do agente, retirando a tipicidade penal subjetiva."
                }
            ],
            "pointers": [
                {"topic": "Critério cronológico etário absoluto no art. 217-A caput", "pageRef": 24},
                {"topic": "Pacificação da Súmula 593 do STJ e irrelevância de namoro ou consentimento", "pageRef": 27},
                {"topic": "Vulnerabilidade por enfermidade ou incapacidade de resistência no § 1º", "pageRef": 30},
                {"topic": "Qualificadoras de lesão grave e morte e rol hediondo", "pageRef": 33}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a06/s03",
        "fingerprint": get_fp("direito-penal/a06/s03"),
        "analytic": """Este segmento aprofunda a mais severa e protetiva das tipificações sexuais da Parte Especial: o crime de estupro de vulnerável positivado no artigo 217-A do Código Penal, analisando a presunção absoluta de vulnerabilidade e os postulados da Súmula 593 do Superior Tribunal de Justiça.

### Estupro de vulnerável e o critério biológico (artigo 217-A, caput)
O artigo 217-A comina sanção punitiva rigorosa de **reclusão de oito a quinze anos** para a consumação de cópula vaginal ou execução de atos lascivos diversos em face de indivíduos com idade inferior a quatorze anos:
- *Objeto de Tutela*: resguarda o desenvolvimento psicossomático e a intangibilidade sexual da criança e do adolescente prematuro;
- *Presunção Absoluta de Incapacidade*: o critério cronológico de idade é puramente objetivo (*iure et de iure*). O direito penal brasileiro presume, de forma peremptória e sem admitir prova em contrário, que a pessoa com menos de quatorze anos completos é desprovida de maturidade biopsíquica indispensável para dispor validamente sobre seu próprio corpo ou deliberar sobre atos eróticos.

### A jurisprudência vinculante da Súmula 593 do STJ
A consolidação jurisprudencial do Superior Tribunal de Justiça culminou na redação da **Súmula 593**, incorporada formalmente ao Código Penal no parágrafo 5º do artigo 217-A:
A norma pacificou que a subsunção típica opera-se de forma plena e objetiva, mostrando-se desprovido de qualquer valor o suposto assentimento manifestado pelo menor, eventual histórico sexual preexistente da vítima ou a ocorrência de envolvimento sentimental e afetivo entre os partícipes da relação íntima.
Essa orientação estanca em definitivo teses defensivas recorrentes:
1. É juridicamente nulo o consentimento manifestado pela criança ofendida;
2. É desprovida de qualquer eficácia atípica a prévia experiência carnal da jovem (inclusive eventual envolvimento no meretrício);
3. É inteiramente ineficaz alegar noivado formal, consentimento dos genitores ou convivência sob regime de união estável.

### Vulnerabilidade por enfermidade ou incapacidade transitória (§ 1º)
O parágrafo 1º estende a idêntica pena de reclusão de oito a quinze anos a quem pratica atos sexuais com:
- Pessoa acometida de moléstia ou deficiência mental que anula a capacidade cognitiva de compreender a natureza do ato sexual;
- Pessoa que, em razão de qualquer condição episódica externa, acha-se impedida de esboçar oposição (indivíduos anestesiados em centro médico, intoxicados por narcóticos indutores de torpor, desmaiados ou prostrados em coma alcoólico profundo).

### Qualificadoras e hediondez
- *Lesão Corporal Grave (§ 3º)*: apenada com reclusão de **dez a vinte anos**;
- *Resultado Morte (§ 4º)*: sancionada com reclusão de **doze a trinta anos**, processada perante a vara criminal comum com juiz singular;
- *Hediondez*: o estupro de vulnerável ostenta índole hedionda em todas as suas modalidades consumadas e tentadas.

### Para fixar
- O estupro de vulnerável tutela o menor de 14 anos cominando reclusão de oito a quinze anos.
- A vulnerabilidade etária inferior a 14 anos é absoluta, dispensando prova pericial de imaturidade.
- A Súmula 593 do STJ desconsidera o consentimento da vítima, sua vida pregressa ou namoro.
- O ato libidinoso diverso da conjunção praticado com menor de 14 anos consuma o art. 217-A.
- A incapacidade de oferecer resistência abrange a embriaguez em coma e anestesia médica no § 1º.
- O resultado morte qualifica o crime com reclusão de doze a trinta anos julgado pelo juiz singular.
- Todas as formas de estupro de vulnerável ostentam natureza de crime hediondo na Lei 8.072/1990.
- O casamento com a vítima não produz qualquer efeito extintivo da punibilidade penal.""",
        "synthetic": [
            "**Estupro de Vulnerável (art. 217-A)**: conjunção ou atos libidinosos com menor de quatorze anos apenados com severa reclusão de oito a quinze anos.",
            "**Presunção Absoluta**: a imaturidade sexual da criança é absoluta e inafastável por presunção biológica de incapacidade volitiva plena.",
            "**Súmula 593 do STJ**: o crime subsiste integralmente independente de prévio consentimento, vida sexual pretérita ou relacionamento amoroso comprovado.",
            "**Incapacidade de Resistência (§ 1º)**: equiparação punitiva ao ato sexual perpetrado contra quem padece de alienação mental ou entorpecimento farmacológico.",
            "**Coma Alcoólico**: manter relação com pessoa em desacordo sensorial anulado por embriaguez profunda subsume-se ao estupro de vulnerável.",
            "**Qualificadoras Severas**: comina reclusão de dez a vinte anos por lesão grave e doze a trinta anos em face da superveniência de resultado letal.",
            "**Hediondez Legal**: o art. 217-A compõe a relação de crimes hediondos inafiançáveis e insuscetíveis de anistia ou graça presidencial.",
            "**Competência Singular**: a qualificadora de morte preterdolosa é processada pelo magistrado criminal singular e não pelo Tribunal do Júri."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 04: Crimes Sexuais contra Vulneráveis e Divulgação Ilícita (p. 35-49)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a06/s04",
        "bizu": {
            "summary": [
                "**Induzimento à Lascívia de Menores (art. 218)**: instigar jovem com idade inferior a 14 anos a satisfazer a sensualidade de terceira pessoa (reclusão de 2 a 5 anos).",
                "**Satisfação de Lascívia Mediante Presença (art. 218-A)**: executar conduta lúbrica ou forçar menor de 14 anos a contemplar atos sexuais (reclusão de 2 a 4 anos).",
                "**Exploração Sexual de Criança/Adolescente (art. 218-B)**: recrutar, submeter ou agenciar jovem com menos de 18 anos para comércio carnal mercenário ou prostituição forçada (reclusão de 4 a 10 anos).",
                "**Hediondez do Art. 218-B**: a exploração sexual de criança, adolescente ou vulnerável é catalogada expressamente como crime hediondo na Lei nº 8.072/1990.",
                "**Divulgação de Cena de Estupro e Pornografia sem Anuência (art. 218-C)**: disponibilizar, propagar ou publicar gravação de estupro ou nudez desautorizada (reclusão de 1 a 5 anos).",
                "**Pornografia de Vingança (Revenge Porn)**: difusão pérfida de intimidade corporal; a pena eleva-se de um a dois terços se perpetrada por ex-companheiro impelido por vingança.",
                "**Majorante por Lucro Econômico**: a reprimenda do art. 218-C exaspera-se de um terço a dois terços quando a veiculação visa à monetização mercantil.",
                "**Excludente de Ilicitude Probatória (§ 2º)**: não tipifica crime a transmissão de arquivos corporais para formalizar notícia-crime perante autoridades de persecução criminal."
            ],
            "teoria": [
                {
                    "statement": "A conduta delitiva de explorar sexualmente ou submeter jovem menor de dezoito anos ao meretrício mercantil (art. 218-B) ostenta natureza hedionda.",
                    "isTrue": True,
                    "explanation": "O art. 218-B do CP figura expressamente no rol dos crimes hediondos da Lei nº 8.072/1990."
                },
                {
                    "statement": "A divulgação na internet de fotos íntimas sem o consentimento da vítima praticada por ex-namorado com escopo de vingança atrai majorante especial de pena.",
                    "isTrue": True,
                    "explanation": "O art. 218-C, § 1º, exaspera a sanção em até dois terços na hipótese de o agente ostentar ou ter vivenciado vínculo conjugal ou afetivo anterior com o sujeito passivo."
                },
                {
                    "statement": "O delito de satisfação de lascívia mediante presença de criança exige o contato físico direto carnal entre o autor e a criança para sua consumação.",
                    "isTrue": False,
                    "explanation": "O art. 218-A pune o ato de satisfazer a lascívia presenciando ou fazendo a criança presenciar ato libidinoso, prescindindo de contato corporal."
                },
                {
                    "statement": "A transmissão de imagens pornográficas confidenciais para autoridade judiciária com o objetivo exclusivo de instruir notícia-crime configura crime do art. 218-C.",
                    "isTrue": False,
                    "explanation": "O art. 218-C, § 2º, ressalva expressamente a atipicidade da transmissão realizada para fins de investigação criminal ou dever de denúncia."
                }
            ],
            "revisao": [
                {
                    "statement": "O crime de corrupção de menores por satisfação de lascívia (art. 218) pune a conduta de induzir menor de catorze anos com reclusão de dois a cinco anos.",
                    "isTrue": True,
                    "explanation": "O art. 218 tutela a formação moral do menor de 14 anos contra o estímulo lascivo praticado em favor de terceiro."
                },
                {
                    "statement": "A exploração sexual de adolescente com dezessete anos de idade tipifica delito punido com pena atenuada de detenção domiciliar alternativa.",
                    "isTrue": False,
                    "explanation": "O art. 218-B comina sanção punitiva severa de reclusão de quatro a dez anos em virtude da gravidade da exploração infanto-juvenil."
                },
                {
                    "statement": "A divulgação de vídeo íntimo realizada com a finalidade expressa de comercialização em sítios cibernéticos atrai causa especial de aumento da sanção.",
                    "isTrue": True,
                    "explanation": "O art. 218-C, § 1º, estabelece o aumento de um terço a dois terços quando a divulgação ilícita visa à obtenção de proveito econômico."
                },
                {
                    "statement": "A consentida captação de imagens íntimas pelo parceiro autoriza a ulterior difusão irrestrita das mídias em redes sociais sem nova anuência.",
                    "isTrue": False,
                    "explanation": "O consentimento para a gravação íntima não autoriza a divulgação pública; a exposição desautorizada tipifica o art. 218-C do CP."
                }
            ],
            "pointers": [
                {"topic": "Induzimento à lascívia de vulneráveis no art. 218 e art. 218-A", "pageRef": 36},
                {"topic": "Exploração sexual de vulneráveis e hediondez no art. 218-B", "pageRef": 40},
                {"topic": "Divulgação de cena de estupro e pornografia de vingança no art. 218-C", "pageRef": 44},
                {"topic": "Majorantes por vínculo afetivo e finalidade mercantil na pornografia não consentida", "pageRef": 48}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a06/s04",
        "fingerprint": get_fp("direito-penal/a06/s04"),
        "analytic": """Este segmento aprofunda a tutela criminal voltada a coibir a corrupção moral de menores, a exploração sexual infanto-juvenil e os delitos cibernéticos de divulgação desautorizada de cenas íntimas e estupro introduzidos pela Lei nº 13.718/2018.

### Corrupção moral e satisfação de lascívia de menores
O Código Penal tipifica condutas que degradam a formação psicossexual infanto-juvenil:
- **Induzimento à Lascívia de Menores (artigo 218)**: comina reclusão de dois a cinco anos a quem induz criança menor de 14 anos a satisfazer a lascívia de outrem (crime de intermediação corruptora);
- **Satisfação de Lascívia Mediante Presença (artigo 218-A)**: pune com reclusão de dois a quatro anos quem pratica, na presença de criança menor de 14 anos, ou a induz a presenciar, ato libidinoso ou conjunção carnal com o intuito de satisfazer lascívia própria ou alheia. Trata-se de **crime formal e de perigo**, que prescinde de qualquer contato físico direto entre o autor e a criança espectadora.

### Exploração sexual de criança e adolescente (artigo 218-B)
O artigo 218-B pune severamente quem submete, induz ou atrai à prostituição ou a qualquer forma de exploração sexual alguém menor de 18 anos ou em situação de vulnerabilidade mental:
- *Sanção Cominada*: comina **reclusão de quatro a dez anos e multa**;
- *Responsabilidade de Terceiros e Clientes*: incorrem nas mesmas penas os proprietários de estabelecimentos que franqueiam o local para a exploração sexual infanto-juvenil, bem como quem aluga quartos ou intermedeia encontros;
- *Hediondez*: o delito do artigo 218-B figura expressamente no rol dos **crimes hediondos** da Lei nº 8.072/1990.

### Divulgação de cena de estupro e pornografia de vingança (artigo 218-C)
Criado pela Lei nº 13.718/2018 para combater a violência digital de gênero (*revenge porn*), o artigo 218-C pune quem disponibiliza, transmite, publica ou divulga vídeo, áudio ou fotografia de cena de estupro ou cena de nudez/sexo sem o consentimento do retratado:
- *Pena Básica*: reclusão de **um a cinco anos e multa**;
- *Majorantes Especiais (§ 1º)*: a reprimenda sofre exasperação de **um a dois terços** se cometida por quem mantém ou manteve relação íntima de afeto com a vítima com intuito de vingança ou humilhação, ou quando a exposição for orientada pelo propósito de obter proveito comercial financeiro;
- *Excludente Específica de Ilicitude (§ 2º)*: não consubstancia crime a transmissão de arquivos íntimos ou cenas delituosas quando operada no exercício de dever funcional ou para fins de instrução de notícia-crime e investigação perante as autoridades policiais competentes.

### Para fixar
- O art. 218 pune o induzimento de menor de 14 anos à lascívia de outrem com reclusão de 2 a 5 anos.
- A satisfação de lascívia mediante presença (art. 218-A) prescinde de contato físico com a criança.
- O art. 218-B tutela a integridade sexual de menores de 18 anos contra prostituição e exploração.
- A exploração sexual infanto-juvenil é classificada como crime hediondo na Lei nº 8.072/1990.
- O art. 218-C pune a divulgação de estupro ou fotos de nudez e sexo desprovidas de autorização.
- A pornografia de vingança cometida por ex-parceiro tem pena aumentada de um a dois terços.
- A divulgação de vídeos íntimos com o propósito de lucro comercial acarreta causa de aumento.
- A entrega de imagens desautorizadas à polícia para fins de apuração criminal é conduta atípica.""",
        "synthetic": [
            "**Induzimento à Lascívia (art. 218)**: intermediação corruptora de menores de 14 anos para saciar apetite carnal de terceiros apenada com reclusão.",
            "**Presença de Crianças (art. 218-A)**: crime formal que reprime a realização de atos libidinosos assistidos por menores dispensando contato físico direto.",
            "**Exploração de Menores (art. 218-B)**: comina reclusão de quatro a dez anos reprimindo redes de prostituição e exploração sexual infanto-juvenil.",
            "**Hediondez do Art. 218-B**: figura no catálogo hediondo inafiançável protegendo adolescentes perante redes de lenocínio e comércio carnal.",
            "**Pornografia Não Consentida (art. 218-C)**: repreende a divulgação cibernética de cenas íntimas e registros de estupro sem a autorização da pessoa exposta.",
            "**Pornografia de Vingança**: exaspera a sanção em até dois terços quando a difusão for perpetrada por ex-companheiro impulsionado por revanche afetiva.",
            "**Fins Lucrativos**: causa especial de aumento incidente se a difusão virtual for monetizada em sítios ou comunidades da rede de computadores.",
            "**Exclusão Probatória**: a remessa das mídias às autoridades da persecução penal para instruir inquérito policial goza de plena atipicidade legal."
        ]
    })

    return items, summaries
