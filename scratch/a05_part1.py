# -*- coding: utf-8 -*-
"""Part 1 for a05: s01, s02, s03, s04 (Crimes de Furto - rigorously paraphrased)."""

def get_part1_data(get_fp):
    items = []
    summaries = []

    # -------------------------------------------------------------
    # SEGMENT 01: Furto Simples, Noturno e Privilegiado (p. 2-11)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a05/s01",
        "bizu": {
            "summary": [
                "**Furto Simples (art. 155, caput)**: desapossamento clandestino e pacífico de coisa móvel de outrem para assenhoreamento definitivo cominada com reclusão de um a quatro anos e multa.",
                "**Objeto Material do Furto**: apenas coisas móveis corpóreas dotadas de valor patrimonial tangível, excluindo bens imóveis e coisas comuns a todos (res communes).",
                "**Equiparação Legal de Energia (art. 155, § 3º)**: a eletricidade, energia térmica ou qualquer outra fonte com expressão econômica equiparam-se juridicamente à coisa móvel.",
                "**Momento Consumativo (Teoria da Amotio)**: adota-se a teoria da apreensão ou amotio, consumando-se o furto no instante da inversão da posse, prescindindo de posse mansa, pacífica ou desvigiada.",
                "**Repouso Noturno (art. 155, § 1º)**: causa de aumento de um terço aplicável quando a subtração ocorre durante o sossego noturno, caracterizado pelo repouso habitual da comunidade local.",
                "**Furto em Estabelecimento Comercial**: o STJ pacificou que a majorante do repouso noturno incide mesmo que o imóvel seja comercial desabitado ou esteja temporariamente vazio.",
                "**Furto Privilegiado (art. 155, § 2º)**: direito público subjetivo do réu que impõe redução de um a dois terços ou substituição por multa se o autor for primário e o bem de pequeno valor.",
                "**Critério do Pequeno Valor**: balizado na jurisprudência pela quantia equivalente a até um salário mínimo vigente na época dos fatos (distinto de valor insignificante).",
                "**Súmula 511 do STJ**: viabiliza a cumulação do furto privilegiado com qualificadoras de feição estritamente objetiva (como chave falsa ou escalada)."
            ],
            "teoria": [
                {
                    "statement": "A consumação do delito de furto subordina-se à posse mansa, pacífica e desvigiada da coisa subtraída pelo agente após a perseguição policial.",
                    "isTrue": False,
                    "explanation": "O STF e o STJ adotam a teoria da amotio: o furto consuma-se com a simples inversão da posse, ainda que por breve instante e seguida de imediata perseguição."
                },
                {
                    "statement": "A causa especial de aumento do repouso noturno incide na hipótese de furto cometido em estabelecimento comercial desabitado durante a madrugada.",
                    "isTrue": True,
                    "explanation": "O STJ firmou entendimento de que a majorante do repouso noturno decorre da maior vulnerabilidade patrimonial na madrugada, aplicando-se a lojas fechadas."
                },
                {
                    "statement": "O furto de energia elétrica mediante ligação clandestina direta que contorna o medidor subsume-se formalmente à figura do crime de estelionato.",
                    "isTrue": False,
                    "explanation": "A ligação direta sem qualquer registro no medidor configura furto por equiparação (art. 155, § 3º); a adulteração mecânica do medidor atrai estelionato."
                },
                {
                    "statement": "A primariedade penal do agente associada ao valor da res furtiva inferior a um salário mínimo autoriza o reconhecimento do furto privilegiado.",
                    "isTrue": True,
                    "explanation": "O art. 155, § 2º, impõe a aplicação dos benefícios do privilégio ao agente primário quando o objeto subtraído for de pequeno valor econômico."
                }
            ],
            "revisao": [
                {
                    "statement": "A incidência de qualificadoras de ordem subjetiva autoriza plenamente a aplicação concomitante do benefício do privilégio no delito de furto.",
                    "isTrue": False,
                    "explanation": "A Súmula 511 do STJ restringe o privilégio às qualificadoras estritamente objetivas, repelindo o privilégio em qualificadoras subjetivas como o abuso de confiança."
                },
                {
                    "statement": "O conceito penal de coisa móvel abrange juridicamente os títulos de crédito ao portador e os impulsos de sinal de televisão a cabo não autorizados.",
                    "isTrue": False,
                    "explanation": "O STF assentou que o sinal clandestino de TV a cabo não configura furto de energia, ante a vedação da analogia in malam partem na esfera penal."
                },
                {
                    "statement": "O pequeno valor monetário para concessão do furto privilegiado não pode ser confundido com a inexpressividade econômica do princípio da insignificância.",
                    "isTrue": True,
                    "explanation": "O pequeno valor (até 1 salário mínimo) atenua a sanção típica no privilégio, ao passo que a insignificância exclui a tipicidade material do fato."
                },
                {
                    "statement": "A causa de aumento de repouso noturno pode ser aplicada tanto no furto simples quanto no furto qualificado segundo o rito dominante dos tribunais superiores.",
                    "isTrue": False,
                    "explanation": "O Superior Tribunal de Justiça, no Tema Repetitivo 1087, assentou a inaplicabilidade da majorante do repouso noturno na figura do furto qualificado."
                }
            ],
            "pointers": [
                {"topic": "Furto simples, objeto material e tipicidade subjetiva do animus rem sibi habendi", "pageRef": 3},
                {"topic": "Teoria da amotio e jurisprudência vinculante sobre consumação do furto", "pageRef": 6},
                {"topic": "Majorante do repouso noturno, balizas de aplicação e Tema 1087 do STJ", "pageRef": 8},
                {"topic": "Furto privilegiado, requisitos objetivos e Súmula 511 do STJ", "pageRef": 10}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a05/s01",
        "fingerprint": get_fp("direito-penal/a05/s01"),
        "analytic": """Este segmento inaugura o Título dos Crimes contra o Patrimônio analisando a estrutura dogmática do furto simples, o marco temporal de consumação patrimonial, a majorante circunstanciada do repouso noturno e o privilégio legal.

### Furto simples e delimitação do bem jurídico tutelado
O artigo 155, caput, do Código Penal incrimina o assenhoreamento clandestino e pacífico de patrimônio alheio (*subtrair, para si ou para outrem, coisa móvel alheia*), cominando reprimenda de reclusão de um a quatro anos e sanção pecuniária. O objeto jurídico tutelado reside na propriedade, posse legítima ou simples detenção fática de bens móveis:
- *Objeto Material*: exclusivamente coisas corpóreas móveis passíveis de apreensão e transporte físico que apresentem valor econômico. Coisas abandonadas (*res derelicta*) ou nunca apropriadas (*res nullius*) não consubstanciam objeto de furto;
- *Equiparação de Energia (parágrafo 3º)*: a energia elétrica ou quaisquer outras formas energéticas com expressão comercial econômica equiparam-se juridicamente à coisa móvel. Importa ressaltar a clássica distinção jurisprudencial: a ligação clandestina direta ("gato" sem passar por relógio medidor) configura **furto de energia**; em contrapartida, a fraude mecânica ou eletrônica que altera o relógio para registrar consumo a menor tipifica o crime de **estelionato** (art. 171 do CP).

### Momento consumativo e teoria da amotio
A doutrina penal e a jurisprudência uniformizada do Supremo Tribunal Federal e do Superior Tribunal de Justiça consagraram a adoção da **Teoria da Amotio (ou Apprehensio)** para definir o instante consumativo do furto:
- A consumação opera-se no instante exato em que a coisa subtraída passa para o domínio do agente criminoso com a inversão da posse (*inversio possessionis*);
- Prescinde-se de posse mansa, pacífica, duradoura ou desvigiada pelo proprietário;
- A pronta perseguição policial imediata e a recuperação da res furtiva minutos após a abordagem não desnaturam a consumação consumada, afastando a tese de crime tentado.

### Repouso noturno e jurisprudência dos tribunais superiores
O parágrafo 1º estatui majoração de **um terço** se o delito for executado durante o período de **repouso noturno**:
- O repouso noturno é critério sociológico costumeiro: coincide com o lapso cronológico em que a localidade costumeiramente se recolhe ao descanso, fragilizando a vigilância comunitária sobre os bens;
- O STJ firmou a orientação de que a causa de aumento incide mesmo quando a subtração recai sobre casa desabitada, via pública ou estabelecimento comercial fechado;
- **Tema Repetitivo 1087 do STJ**: a Corte Especial fixou a tese de que a causa de aumento do repouso noturno (§ 1º) **não é aplicável ao furto qualificado (§ 4º)**, sendo restrita à figura básica do furto simples, face à topografia do Código e à proporcionalidade punitiva.

### Furto privilegiado (art. 155, § 2º)
O instituto do privilégio impõe obrigatoriamente a diminuição da reprimenda privativa de liberdade de um a dois terços, ou sua substituição isolada por multa, quando preenchidos dois requisitos cumulativos:
1. *Primariedade Técnica*: o réu não pode ostentar reincidência penal formal;
2. *Pequeno Valor da Coisa*: a jurisprudência adota como parâmetro econômico a importância equivalente a até um salário mínimo ao tempo da conduta.

Nos moldes da **Súmula 511 do STJ**, é plenamente viável a harmonização do furto privilegiado com a modalidade qualificada, desde que a qualificadora apresente **natureza estritamente objetiva** (como a destruição de obstáculo, chave falsa ou concurso de pessoas), repelindo-se o privilégio nas hipóteses de índole subjetiva como o abuso de confiança.

### Para fixar
- O furto pune a subtração clandestina de bem móvel com reclusão de um a quatro anos e multa.
- A energia elétrica equipara-se à coisa móvel; a ligação direta configura furto e o desvio por fraude é estelionato.
- Pela teoria da amotio, o furto consuma-se na inversão da posse, dispensando posse mansa e desvigiada.
- O repouso noturno acarreta elevação de um terço da reprimenda do furto simples.
- Conforme o Tema 1087 do STJ, a majorante de repouso noturno não incide no furto qualificado.
- O furto privilegiado exige primariedade do infrator e valor do objeto não excedente a um salário mínimo.
- A insignificância penal exclui a tipicidade material, distinguindo-se do pequeno valor do privilégio.
- A Súmula 511 do STJ autoriza cumular privilégio com qualificadoras de natureza estritamente objetiva.""",
        "synthetic": [
            "**Furto Simples (art. 155)**: subtração desprovida de violência ou ameaça de patrimônio móvel corpóreo dotado de substância econômica positiva.",
            "**Equiparação de Energia**: ligação clandestina contornando medição caracteriza furto; adulterar medidor para mascarar leitura atrai o tipo de estelionato.",
            "**Teoria da Amotio**: aperfeiçoamento consumativo imediato com a inversão da detenção da coisa, dispensando posse pacífica ou saída da esfera de vigilância.",
            "**Majorante Noturna (§ 1º)**: eleva a sanção em um terço pela exploração da quietude social na madrugada, aplicável inclusive a lojas comerciais fechadas.",
            "**Tema 1087 do STJ**: restringe a causa de aumento do repouso noturno à modalidade simples, vedando sua extensão analógica ao furto qualificado.",
            "**Furto Privilegiado (§ 2º)**: decote compulsório da pena corporificado em favor do criminoso primário quando o bem não extrapola um salário mínimo.",
            "**Súmula 511 do STJ**: autoriza a aplicação híbrida do privilégio no furto qualificado unicamente perante qualificadoras de natureza fática objetiva.",
            "**Pequeno Valor e Bagatela**: pequeno valor viabiliza atenuação de pena no privilégio; a bagatela material exclui integralmente a própria tipicidade penal."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 02: Furto Qualificado Clássico (p. 12-20)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a05/s02",
        "bizu": {
            "summary": [
                "**Furto Qualificado (art. 155, § 4º)**: comina sanção severa de reclusão de dois a oito anos e multa em face de métodos gravosos de execução patrimonial.",
                "**Rompimento de Obstáculo (inciso I)**: destruição ou arrombamento mecânico de barreira externa predisposta à proteção da res furtiva (portas, janelas, cadeados).",
                "**Violência Contra a Própria Coisa**: a destruição violenta deve recair sobre o obstáculo e não sobre o próprio objeto pretendido (arrombar o vidro do carro para furtar o toca-fitas qualifica; arrombar o vidro para levar o próprio veículo é furto simples).",
                "**Abuso de Confiança (inciso II)**: aproveitamento doloso de prévio vínculo fiduciário de lealdade e credibilidade estabelecido entre autor e proprietário.",
                "**Relação de Emprego**: o mero vínculo formal de emprego não gera automaticamente abuso de confiança, exigindo-se prova de confiança especial depositada no funcionário.",
                "**Furto Mediante Fraude**: o autor emprega ardil ou engano para iludir a vigilância da vítima e subtrair a coisa (distingue-se do estelionato em que a vítima entrega voluntariamente a posse).",
                "**Escalada e Destreza (inciso II)**: escalada exige esforço físico incomum ou uso de instrumentos (túneis, escadas); destreza traduz agilidade manual dissimulada (punga).",
                "**Emprego de Chave Falsa (inciso III)**: utilização de qualquer instrumento mecânico, gazua, chave micha ou cópia clandestina apto a acionar o segredo da fechadura.",
                "**Concurso de Pessoas (inciso IV)**: reunião de duas ou mais pessoas na empreitada delitiva, aplicando-se inclusive quando um dos comparsas for inimputável."
            ],
            "teoria": [
                {
                    "statement": "No furto com destruição de obstáculo, a quebra do vidro do automóvel para subtrair o veículo em si atrai compulsoriamente a qualificadora do inciso I.",
                    "isTrue": False,
                    "explanation": "A jurisprudência assenta que a destruição direcionada contra a própria coisa subtraída não qualifica o furto, incidindo a forma simples."
                },
                {
                    "statement": "O furto mediante fraude distingue-se do estelionato porque na fraude do furto o ardil serve para diminuir a vigilância e permitir a subtração.",
                    "isTrue": True,
                    "explanation": "No furto com fraude o agente burla a vigilância para tomar a coisa; no estelionato o engano faz a própria vítima entregar livremente o bem."
                },
                {
                    "statement": "A prática de furto qualificado pelo concurso de agentes resta descaracterizada caso o comparsa identificado nos autos seja adolescente inimputável.",
                    "isTrue": False,
                    "explanation": "O concurso de agentes qualifica o furto ainda que o parceiro seja menor inimputável ou não venha a ser identificado na instrução."
                },
                {
                    "statement": "A qualificadora da escalada exige esforço físico incomum ou superação de via anormal de acesso, sendo imprescindível comprovação pericial quando deixar vestígios.",
                    "isTrue": True,
                    "explanation": "A escalada pressupõe esforço excepcional por via anormal, dependendo de laudo pericial para sua comprovação material no processo penal."
                }
            ],
            "revisao": [
                {
                    "statement": "A destreza apta a qualificar o furto reside na habilidade manual disfarçada de batedor de carteira que passa despercebida pela vítima no ato.",
                    "isTrue": True,
                    "explanation": "A destreza traduz particular sutileza de movimentos físicos impeditiva da percepção da subtração pela vítima no momento executivo."
                },
                {
                    "statement": "A simples relação trabalhista comum entre patrão e funcionário presume de forma absoluta o abuso de confiança na subtração patrimonial.",
                    "isTrue": False,
                    "explanation": "O vínculo de emprego isolado não gera presunção; é imperiosa a demonstração fática de especial laço de lealdade e confiança traído."
                },
                {
                    "statement": "O emprego de chave verdadeira que havia sido legitimamente emprestada ao agente pelo proprietário consubstancia a qualificadora de chave falsa.",
                    "isTrue": False,
                    "explanation": "O uso de chave verdadeira obtida de forma regular não configura a qualificadora do inciso III, configurando no máximo abuso de confiança."
                },
                {
                    "statement": "O sistema antifurto de vigilância eletrônica instalado em loja de departamentos torna o furto impossível na modalidade tentada.",
                    "isTrue": False,
                    "explanation": "Conforme a Súmula 567 do STJ, a existência de vigilância eletrônica ou seguranças em loja comercial não torna o crime de furto impossível."
                }
            ],
            "pointers": [
                {"topic": "Furto qualificado por rompimento de obstáculo e vestígios periciais", "pageRef": 13},
                {"topic": "Abuso de confiança e diferenciação dogmática entre furto mediante fraude e estelionato", "pageRef": 15},
                {"topic": "Escalada e destreza, conceitos e exigências probatórias", "pageRef": 17},
                {"topic": "Emprego de chave falsa, conceito amplo e gazuas", "pageRef": 18},
                {"topic": "Concurso de duas ou mais pessoas e Súmula 567 do STJ", "pageRef": 20}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a05/s02",
        "fingerprint": get_fp("direito-penal/a05/s02"),
        "analytic": """Este segmento detém-se no estudo pormenorizado das qualificadoras clássicas do crime de furto discriminadas no artigo 155, § 4º, do Código Penal, analisando os critérios de arrombamento, o abuso de fidúcia, a distinção entre fraude e estelionato, a escalada e a mecânica das chaves falsas.

### Rompimento de obstáculo à subtração da coisa (inciso I)
A pena cominada eleva-se para o patamar de reclusão de dois a oito anos e multa quando o crime é cometido com destruição ou arrombamento de obstáculo exterior predisposto a resguardar o bem móvel:
- *Obstáculo Exterior versus Própria Coisa*: a violência física mecânica deve incidir sobre elemento que protege o bem (quebra de cadeado, porta arrombada, janela estilhaçada). A jurisprudência consolidada do Superior Tribunal de Justiça pacificou que, caso a violência física recaia sobre o próprio objeto material visado (ex.: romper o vidro do carro para furtar o próprio veículo), a conduta permanece como **furto simples**. Se o rompimento do vidro do carro visa subtrair a carteira deixada no porta-luvas, a qualificadora resta plenamente caracterizada;
- *Exigência Pericial*: por deixar vestígios materiais externos transitórios, a qualificadora subordina-se à confecção de laudo pericial formal, salvo justificada impossibilidade.

### Abuso de confiança e furto mediante fraude (inciso II)
- **Abuso de Confiança**: exige comprovação empírica de vínculo fiduciário qualificado e credibilidade especial preexistente depositada pelo ofendido no infrator. O mero vínculo empregatício formal de prestação de serviços não induz presunção automática de confiança especial;
- **Furto Mediante Fraude versus Delito de Estelionato**: divisor de águas dogmático recorrente na prática criminal:
  - *No Furto Mediante Fraude*: o engodo ardiloso é arquitetado pelo agente exclusivamente para desviar e arrefecer a vigilância da vítima sobre a coisa, permitindo-lhe a subtração clandestina e unilateral da res furtiva;
  - *No Estelionato (art. 171)*: o engano faz com que o ofendido, voluntariamente induzido em erro, proceda à entrega espontânea da posse definitiva do bem ao autor delitivo.

### Escalada, destreza, chave falsa e concurso de pessoas
- **Escalada**: ingresso no imóvel por via anormal de entrada (telhados, dutos de ventilação, muros consideráveis) demandando esforço físico fora do comum ou instrumental mecânico acessório (escadas, cordas com gancho);
- **Destreza**: habilidade corporal dissimulada singular operada pelo batedor de carteiras (*punga*), capaz de extrair o pertence sob os bolsos da vítima sem que esta se aperceba da investida no momento;
- **Chave Falsa (inciso III)**: engloba qualquer instrumento apto a acionar fechaduras sem rompê-las fisicamente, abrangendo gazuas, michas, pedaços de arame moldados e cópias clandestinas obtidas sem o consentimento do titular. O uso da chave verdadeira subtraída afasta o inciso III;
- **Concurso de Pessoas (inciso IV)**: exige adesão volitiva de dois ou mais agentes, incidindo ainda que um dos concorrentes atue sob a capa da inimputabilidade etária.

Cumpre assinalar a diretriz da **Súmula 567 do Superior Tribunal de Justiça**: a existência de câmeras eletrônicas ou agentes de segurança privada em estabelecimentos comerciais não converte o furto tentado em hipótese de crime impossível.

### Para fixar
- O furto qualificado comina pena de reclusão de dois a oito anos e multa no art. 155, § 4º.
- Romper o obstáculo externo qualifica o crime; violar a própria coisa visada mantém a figura simples.
- A qualificadora de arrombamento de obstáculo exige laudo de exame de corpo de delito direto.
- O mero contrato de trabalho não presume de pleno direito o abuso de confiança na subtração.
- No furto mediante fraude a artimanha burla a vigilância; no estelionato a vítima entrega a coisa de boa-fé.
- A escalada impõe superação de via anormal e incomum de ingresso no recinto mediante esforço relevante.
- A chave falsa engloba michas, gazuas e réplicas clandestinas capazes de abrir o mecanismo da fechadura.
- A vigilância eletrônica em estabelecimentos comerciais não caracteriza hipótese de crime impossível.""",
        "synthetic": [
            "**Furto Qualificado (art. 155, § 4º)**: comina sanção reclusiva severa de dois a oito anos diante da mecânica gravosa empregada na conduta delitiva.",
            "**Rompimento de Obstáculo**: arrombamento de trava externa que protege a res; violência sobre o próprio bem visado configura delito simples.",
            "**Abuso de Confiança**: demanda quebra deliberada de vínculo de fidelidade subjetiva real prévia travada faticamente com o detentor do patrimônio.",
            "**Fraude no Furto versus Estelionato**: a fraude no furto ilude a atenção para subtrair; no estelionato engendra a entrega voluntária do objeto pelo lesado.",
            "**Escalada e Esforço Anormal**: superação física mecânica de obstáculos verticais ou acessos anormais exigindo comprovação pericial de vestígios.",
            "**Destreza no Punga**: sutileza e agilidade manual extrema que impede a percepção sensorial da subtração patrimonial no instante executório.",
            "**Emprego de Chave Falsa**: manejo de gazuas, michas e chaves adulteradas ou copiadas fraudulentamente para vencer o mecanismo de tranca.",
            "**Súmula 567 do STJ**: a presença de câmeras ou seguranças de loja comercial não converte a tentativa patrimonial em crime impossível."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 03: Furto Qualificado e Novidades Legislativas (p. 21-28)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a05/s03",
        "bizu": {
            "summary": [
                "**Furto com Artefatos Explosivos (art. 155, § 4º-A)**: apenado com reclusão de quatro a dez anos e multa caso haja detonação explosiva causadora de perigo comum.",
                "**Furto Mediante Fraude Eletrônica (art. 155, § 4º-B)**: reclusão de quatro a oito anos e multa se praticado por meio de dispositivos eletrônicos conectados ou não à internet.",
                "**Fraude Eletrônica Cibernética**: abrange invasão de celulares e clonagens telemáticas; comina aumento de um terço a dois terços se o servidor de dados estiver fora do Brasil.",
                "**Majoração por Vulnerabilidade Etária (§ 4º-C)**: exasperação de um terço ao dobro se a fraude cibernética for perpetrada contra pessoa idosa ou vulnerável.",
                "**Subtração de Veículo Automotor (art. 155, § 5º)**: reclusão de três a oito anos se o veículo for transportado para outro Estado da Federação ou para o exterior.",
                "**Consumação do Art. 155, § 5º**: exige a efetiva transposição física da divisa interestadual ou fronteira internacional com o veículo automotor subtraído.",
                "**Furto de Semovente Domesticável / Abigeato (art. 155, § 6º)**: reclusão de dois a cinco anos para a subtração de semovente domesticável de produção, ainda que abatido no local.",
                "**Subtração de Substância Explosiva (art. 155, § 7º)**: reclusão de quatro a dez anos se a subtração recair sobre explosivos ou acessórios que possibilitem sua montagem.",
                "**Hediondez no Furto com Explosivo**: a Lei 13.964/2019 incluiu o furto qualificado pelo emprego de explosivo (art. 155, § 4º-A) no rol taxativo dos crimes hediondos da Lei 8.072/1990."
            ],
            "teoria": [
                {
                    "statement": "O delito de furto qualificado pelo emprego de explosivo consubstancia crime hediondo segundo expressa disposição da legislação penal extravagante.",
                    "isTrue": True,
                    "explanation": "A Lei Anticrime (Lei 13.964/2019) incluiu o art. 155, § 4º-A, no rol taxativo de crimes hediondos da Lei nº 8.072/1990."
                },
                {
                    "statement": "Para a configuração da qualificadora do furto de veículo automotor transportado para outro Estado, basta a comprovação da intenção subjetiva de transpor a divisa.",
                    "isTrue": False,
                    "explanation": "O art. 155, § 5º, exige a transposição física e material efetiva dos limites territoriais interestaduais ou internacionais para consumar a qualificadora."
                },
                {
                    "statement": "A fraude eletrônica cometida contra idoso por meio de rede social autoriza a exasperação da pena corporal de um terço até o dobro.",
                    "isTrue": True,
                    "explanation": "O art. 155, § 4º-C, estabelece aumento de um terço ao dobro quando a fraude eletrônica for executada contra pessoa idosa ou vulnerável."
                },
                {
                    "statement": "A desossa e abate do gado bovino no pasto da fazenda durante o ato executório não descaracteriza a qualificadora de abigeato do art. 155, § 6º.",
                    "isTrue": True,
                    "explanation": "O tipo do art. 155, § 6º, abrange o semovente de corte mesmo que venha a ser abatido ou esquartejado na própria área espoliada."
                }
            ],
            "revisao": [
                {
                    "statement": "O furto praticado mediante subtração de dinamites e detonadores atrai a pena qualificada do parágrafo 7º do artigo 155 do Código Penal.",
                    "isTrue": True,
                    "explanation": "O art. 155, § 7º, comina reclusão de quatro a dez anos quando a própria res furtiva consiste em substâncias explosivas ou acessórios correlatos."
                },
                {
                    "statement": "A prática de furto de veículo interceptado por barreira policial antes de cruzar a divisa interestadual consuma a qualificadora do parágrafo quinto.",
                    "isTrue": False,
                    "explanation": "Sem a transposição física consumada da fronteira interestadual, o autor responde por furto simples ou qualificado comum sem a qualificadora do § 5º."
                },
                {
                    "statement": "O cometimento de furto cibernético mediante utilização de servidor informático situado no exterior atrai causa especial de aumento de pena.",
                    "isTrue": True,
                    "explanation": "O art. 155, § 4º-B, § 4º-C, prevê aumento de um terço a dois terços caso a fraude eletrônica opere com servidor localizado fora do território nacional."
                },
                {
                    "statement": "A qualificadora de abigeato aplica-se a qualquer animal silvestre encontrado em cativeiro doméstico particular sem autorização ambiental.",
                    "isTrue": False,
                    "explanation": "A qualificadora restringe-se taxativamente aos semoventes domesticáveis de produção e criação agropecuária (bovinos, equinos, suínos)."
                }
            ],
            "pointers": [
                {"topic": "Furto com emprego de explosivo e inserção no rol hediondo", "pageRef": 22},
                {"topic": "Fraude eletrônica cibernética e causas de aumento no art. 155, § 4º-B", "pageRef": 24},
                {"topic": "Furto de veículos transportados interestadualmente e consumação", "pageRef": 26},
                {"topic": "Abigeato e subtração de semoventes domesticáveis de produção", "pageRef": 27},
                {"topic": "Subtração de artefatos explosivos e tutela da segurança coletiva", "pageRef": 28}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a05/s03",
        "fingerprint": get_fp("direito-penal/a05/s03"),
        "analytic": """Este segmento aprofunda as figuras contemporâneas e qualificadoras especializadas do crime de furto inseridas pelas reformas da Lei nº 13.964/2019 e da Lei nº 14.155/2021, examinando o emprego de explosivos, a fraude eletrônica cibernética, o abigeato e o transporte interestadual de veículos.

### Furto com emprego de explosivo e natureza hedionda (art. 155, § 4º-A)
O Código Penal estabelece sanção reclusiva de **quatro a dez anos e multa** se a conduta delitiva for perpetrada mediante emprego de substância explosiva ou artefato congênere dotado de poder causador de perigo comum (prática usual em arrombamentos de caixas eletrônicos bancários).

Por imperativo legal introduzido pela Lei Anticrime (Lei nº 13.964/2019), essa modalidade qualificada foi incorporada ao **rol taxativo dos crimes hediondos** (artigo 1º, inciso IX, da Lei nº 8.072/1990). Em contrapartida simétrica, o parágrafo 7º comina a idêntica pena severa de reclusão de quatro a dez anos se a própria coisa subtraída consubstanciar substância explosiva ou artefato destinado à sua fabricação mecânica.

### Fraude eletrônica e vulnerabilidade cibernética (§§ 4º-B e 4º-C)
Criada pela Lei nº 14.155/2021, a **Fraude Eletrônica** comina reclusão de **quatro a oito anos e multa** na hipótese em que a subtração patrimonial for praticada mediante artifícios enganosos veiculados em dispositivos eletrônicos (computadores, celulares, redes sociais, clonagem de contas de aplicativos de mensagens ou invasão de home banking):
- *Causas de Aumento (§ 4º-B, parte final)*: a pena eleva-se de **um terço a dois terços** se o crime for perpetrado mediante a utilização de servidor de banco de dados localizado no exterior da República;
- *Proteção a Idosos e Vulneráveis (§ 4º-C)*: a sanção aumenta-se de **um terço ao dobro** caso o golpe cibernético recaia sobre pessoa idosa ou pessoa com vulnerabilidade mental evidente.

### Transporte interestadual ou internacional de veículos (§ 5º)
O parágrafo 5º apena com reclusão de **três a oito anos** a subtração de automóveis ou motocicletas quando houver condução efetiva do meio de transporte para além dos limites estaduais ou fronteiras internacionais. A jurisprudência consolidada dos tribunais superiores assenta que a qualificadora exige a **transposição fática e material efetiva** da fronteira geográfica. Caso o veículo seja interceptado por bloqueio policial antes de cruzar a divisa interestadual, o autor responderá por furto simples ou qualificado comum, afastando-se o parágrafo 5º.

### Abigeato ou furto de semoventes de produção (§ 6º)
O parágrafo 6º pune com reclusão de **dois a cinco anos** a subtração de semovente domesticável de produção (bovinos, equinos, ovinos, suínos e caprinos voltados à exploração agropecuária). O preceito legal expressamente equipara a infração à subtração do animal abatido ou desossado no próprio local do crime, coibindo o mercado clandestino de carnes no ambiente rural.

### Para fixar
- O furto mediante emprego de explosivo tem pena de quatro a dez anos e ostenta natureza hedionda.
- Subtrair artefatos ou substâncias explosivas tipifica figura qualificada autônoma no art. 155, § 7º.
- A fraude eletrônica cibernética comina reclusão de quatro a oito anos no § 4º-B do art. 155.
- Utilizar servidores situados no exterior acarreta aumento punitivo de um terço a dois terços na fraude.
- A fraude virtual perpetrada contra pessoa idosa autoriza elevação da reprimenda de um terço ao dobro.
- A qualificadora do veículo automotor exige a efetiva transposição espacial da divisa do Estado.
- O abigeato pune a subtração de animais de produção com reclusão de dois a cinco anos.
- O abate e esquartejamento do gado dentro da fazenda não descaracteriza a qualificadora de abigeato.""",
        "synthetic": [
            "**Explosivo no Furto (§ 4º-A)**: repreende detonações de caixas eletrônicos com sanção de quatro a dez anos ostentando hediondez formal plena.",
            "**Subtração de Explosivos (§ 7º)**: qualificação penal autônoma sancionando a apropriação clandestina de artefatos de alto poder destrutivo bélico.",
            "**Fraude Eletrônica (§ 4º-B)**: criminaliza golpes digitais operados por conexões cibernéticas cominando reclusão gravosa de quatro a oito anos.",
            "**Majorante Internacional**: exaspera o apenamento eletrônico na fração de um terço a dois terços diante do uso de servidores remotos alienígenas.",
            "**Golpes Contra Idosos**: exasperação de um terço ao dobro quando a astúcia cibernética for direcionada contra o patrimônio de pessoas idosas.",
            "**Veículos e Fronteiras (§ 5º)**: requer a efetiva transposição material das divisas geográficas interestaduais para consumação da qualificadora.",
            "**Abigeato Rural (§ 6º)**: reprime o desfalque de rebanhos de semoventes de corte ou leite ainda que abatidos no pasto durante a empreitada.",
            "**Proteção Agropecuária**: tipificação que salvaguarda a cadeia de produção econômica rural perante o furto de cabeças de gado domesticáveis."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 04: Disposições Finais do Furto e Insignificância (p. 29-38)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a05/s04",
        "bizu": {
            "summary": [
                "**Furto de Coisa Comum (art. 156)**: apropriação por condômino ou coerdeiro de bem móvel indiviso retirando-o da posse legítima de quem o detém.",
                "**Excludente de Ilicitude do Furto Comum (§ 2º)**: descaracteriza a ilicitude quando a subtração de bens fungíveis limita-se à cota-parte legítima devida ao herdeiro.",
                "**Ação Penal no Art. 156**: processa-se privativamente mediante ação penal pública condicionada à representação do ofendido (§ 1º).",
                "**Princípio da Insignificância**: causa supralegal de exclusão da tipicidade material aplicável quando a lesão ao bem patrimonial for irrisória.",
                "**Requisitos do STF para a Bagatela**: mínima ofensividade da conduta, nenhuma periculosidade social da ação, reduzidíssimo grau de reprovabilidade e inexpressividade da lesão jurídica.",
                "**Reincidência e Insignificância**: o STF admite excepcionalmente a bagatela ao reincidente caso a medida se mostre socialmente recomendável e proporcional.",
                "**Furto Noturno e Qualificado com Insignificância**: a incidência de qualificadoras em regra afasta o princípio da insignificância face à maior reprovabilidade da ação.",
                "**Furto Famélico**: subtração de gêneros alimentícios perecíveis em quantidade estritamente indispensável para saciar fome inadiável de si ou de sua família.",
                "**Natureza do Furto Famélico**: consubstancia causa excludente da ilicitude amparada no estado de necessidade justificante (art. 24 do Código Penal).",
                "**Furto de Uso**: apropriação momentânea de coisa infungível com intenção de uso passageiro e pronta restituição integral no local de origem sem dano, reputada penalmente atípica."
            ],
            "teoria": [
                {
                    "statement": "No furto de coisa comum, afasta-se a punibilidade caso a retirada de bem fungível não sobrepuje o valor correspondente à fração devida ao coproprietário.",
                    "isTrue": True,
                    "explanation": "O art. 156, § 2º, ressalva a atipicidade da conduta quando o bem for fungível e seu montante respeitar a quota-parte patrimonial do autor."
                },
                {
                    "statement": "O furto de uso consubstancia conduta penalmente atípica no direito penal brasileiro em decorrência da ausência do animus rem sibi habendi.",
                    "isTrue": True,
                    "explanation": "A ausência do dolo de apossamento definitivo descaracteriza a tipicidade do furto, exigindo rápida devolução da coisa no local de origem."
                },
                {
                    "statement": "O furto famélico praticado em situação de miserabilidade extrema para conter a fome iminente consubstancia causa de exclusão da culpabilidade por inexigibilidade de conduta diversa.",
                    "isTrue": False,
                    "explanation": "O furto famélico é enquadrado pela doutrina e jurisprudência como causa de exclusão da ilicitude amparada no estado de necessidade (art. 24 do CP)."
                },
                {
                    "statement": "A ação penal para apurar o delito de furto de coisa comum submete-se à condição de procedibilidade da representação do condômino ofendido.",
                    "isTrue": True,
                    "explanation": "O art. 156, § 1º, do Código Penal estatui que a persecução penal somente se procede mediante representação."
                }
            ],
            "revisao": [
                {
                    "statement": "O princípio da insignificância no crime de furto descaracteriza a tipicidade formal do comportamento do agente delitivo.",
                    "isTrue": False,
                    "explanation": "A insignificância afasta a tipicidade material (relevância do desvalor lesivo), permanecendo intacta a tipicidade formal da conduta."
                },
                {
                    "statement": "A restituição da coisa após o uso passageiro em local diverso daquele onde foi subtraída afasta a atipicidade do furto de uso.",
                    "isTrue": True,
                    "explanation": "O furto de uso exige a restituição incontinente no local primitivo; o abandono da coisa em lugar ermo tipifica furto comum consumado."
                },
                {
                    "statement": "O Superior Tribunal de Justiça admite a incidência mecânica e automática da insignificância no furto qualificado por rompimento de obstáculo.",
                    "isTrue": False,
                    "explanation": "A presença de qualificadora (arrombamento) evidencia maior reprovabilidade da conduta, afastando a bagatela segundo o STJ."
                },
                {
                    "statement": "A mínima ofensividade e o reduzido grau de reprovabilidade do comportamento compõem os vetores fixados pelo STF para o princípio da bagatela.",
                    "isTrue": True,
                    "explanation": "O STF fixou os quatro requisitos vetoriais concomitantes para aferição da insignificância patrimonial em sede penal."
                }
            ],
            "pointers": [
                {"topic": "Furto de coisa comum, quotas ideais e representação", "pageRef": 30},
                {"topic": "Princípio da insignificância, vetores do STF e repercussões na reincidência", "pageRef": 32},
                {"topic": "Furto famélico e excludente de ilicitude por estado de necessidade", "pageRef": 35},
                {"topic": "Furto de uso, requisitos de pronta restituição e atipicidade", "pageRef": 37}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a05/s04",
        "fingerprint": get_fp("direito-penal/a05/s04"),
        "analytic": """Este segmento conclui o capítulo do furto abordando as regras do furto de coisa comum, os parâmetros do princípio da insignificância patrimonial, as balizas do furto famélico e a atipicidade do furto de uso.

### Furto de coisa comum (artigo 156)
O artigo 156 tipifica a subtração perpetrada pelo condômino, coerdeiro ou sócio que se apodera da coisa móvel comum pertencente ao condomínio, cominando pena de detenção de seis meses a dois anos ou multa. Trata-se de **crime próprio** dependente de vínculo societário ou hereditário com a titularidade fracionária do acervo.

O preceito tutela a posse legítima exercida pelo condômino vigilante e prevê relevantes peculiaridades:
- *Condição de Procedibilidade (§ 1º)*: a ação penal é pública condicionada à expressa **representação** do sócio ou herdeiro lesado;
- *Causa de Exclusão da Tipicidade/Punibilidade (§ 2º)*: afasta-se a punição criminal caso o desfalque recaia sobre coisas fungíveis sem que a quantia retirada ultrapasse a fração legítima patrimonial pertencente ao autor da partilha. Se o herdeiro retira quantia em dinheiro do cofre inventariado correspondente à sua exata fração legítima de partilha futura, a conduta resta atípica.

### Princípio da insignificância e jurisprudência vinculante
O princípio da bagatela opera como **causa supralegal de exclusão da tipicidade material**: embora o fato preencha formalmente a moldura do tipo incriminador, a lesão insignificante ao bem patrimonial afasta a intervenção do direito penal como ultima ratio. O Supremo Tribunal Federal consolidou **quatro vetores cumulativos** para sua admissibilidade:
1. Mínima ofensividade da conduta exteriorizada;
2. Ausência absoluta de periculosidade social da ação criminosa;
3. Reduzidíssimo grau de reprovabilidade do comportamento adotado;
4. Inexpressividade da lesão jurídica provocada no patrimônio tutelado.

Em regra, a presença de qualificadoras no furto (arrombamento, chave falsa, destreza) ou a reincidência do réu afastam a aplicação da bagatela face à reprovabilidade acentuada. Não obstante, o STF assentou que a reincidência não deve atuar como óbice mecânico insuperável, cabendo ao juiz valorar as circunstâncias concretas de vulnerabilidade do indivíduo.

### Furto famélico e furto de uso
- **Furto Famélico**: ocorre quando o sujeito desprovido de recursos materiais mínimos subtrai alimentos ou remédios de sobrevivência imediata em quantidade estritamente indispensável para aplacar a fome urgente de si ou de sua família. Não se trata de hipótese de bagatela nem de inexigibilidade de conduta diversa, mas sim de autêntica **causa de exclusão da ilicitude amparada no estado de necessidade** (artigo 23, inciso I, e artigo 24 do Código Penal);
- **Furto de Uso**: consiste na apropriação puramente momentânea de coisa infungível para utilização temporária e subsequente restituição voluntária integral da coisa. Ostenta natureza de **fato penalmente atípico** pela ausência do elemento subjetivo especial do tipo (*animus rem sibi habendi* ou ânimo de assenhoreamento definitivo). São requisitos cumulativos para a caracterização do furto de uso:
  1. Utilização rápida e passageira da coisa móvel infungível;
  2. Restituição integral da coisa sem avarias no estado anterior;
  3. Devolução voluntária da coisa no local exato de onde foi retirada e antes que a vítima note o desfalque;
  4. Inexistência de dolo de apossamento. Se o bem for abandonado em via pública ou danificado, opera-se o crime de furto consumado.

### Para fixar
- O furto de coisa comum pune a subtração pelo sócio ou coerdeiro com detenção de seis meses a dois anos.
- A subtração de bem fungível até o limite da quota-parte a que tem direito o herdeiro é impunível.
- A ação penal do furto de coisa comum subordina-se à representação da parte lesada.
- O princípio da insignificância afasta a tipicidade material da conduta perante lesão patrimonial inexpressiva.
- O STF exige mínima ofensividade, ausência de periculosidade, reduzida reprovabilidade e lesão inexpressiva.
- A reincidência não impede de forma automática a bagatela segundo precedentes do STF.
- O furto famélico afasta a ilicitude da conduta com amparo no estado de necessidade justificante.
- O furto de uso é penalmente atípico pela ausência de dolo de assenhoreamento definitivo da coisa.""",
        "synthetic": [
            "**Furto de Coisa Comum (art. 156)**: delito próprio do coproprietário que arrebata coisa comum com ação condicionada à representação do consorte.",
            "**Quota Imune no Art. 156**: descaracteriza o delito a subtração de bem fungível cuja expressão não sobrepuje a fração legítima devida ao herdeiro.",
            "**Princípio da Insignificância**: causa de atipicidade material assentada na inexpressividade econômica da agressão patrimonial aos bens alheios.",
            "**Critérios da Bagatela**: mínima ofensividade, reduzida reprovabilidade social, inexpressividade de danos e ausência de perigo coletivo comunitário.",
            "**Reincidência e Bagatela**: a habitualidade delitiva afasta ordinariamente a bagatela, comportando ressalva se socialmente recomendável pelo juiz.",
            "**Furto Famélico**: subtração estritamente alimentar para sobrevivência biológica imediata que exclui a ilicitude por estado de necessidade.",
            "**Atipicidade do Furto de Uso**: apropriação transitória com pronta devolução voluntária e integral do bem no local de origem desprovida de dolo definitivo.",
            "**Exigência na Restituição**: abandonar o bem utilizado em via pública descaracteriza o uso passageiro e consuma o crime de furto comum."
        ]
    })

    return items, summaries
