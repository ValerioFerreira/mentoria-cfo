# -*- coding: utf-8 -*-
"""Part 1 for a07: s01, s02 (Crimes Funcionais, Peculato, Concussão e Corrupção Passiva)."""

def get_part1_data(get_fp):
    items = []
    summaries = []

    # -------------------------------------------------------------
    # SEGMENT 01: Funcionário Público e Peculato (p. 2-10)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a07/s01",
        "bizu": {
            "summary": [
                "**Conceito Penal de Funcionário Público (art. 327)**: indivíduo que desempenha encargo, posto ou mister estatal em caráter provisório ou gratuito perante a administração direta ou indireta.",
                "**Funcionário Público por Equiparação (§ 1º)**: quem exerce cargo ou função em entidade paraestatal ou empresa prestadora de serviços contratada pelo poder público.",
                "**Causa de Aumento Funcional (§ 2º)**: acréscimo de um terço na pena se o autor ocupa cargo em comissão ou função de direção/assessoramento na administração pública.",
                "**Peculato-Apropriação (art. 312, caput)**: assenhoramento doloso de numerário, título representativo ou coisa móvel pública ou privada sob custódia material em decorrência do encargo público.",
                "**Peculato-Desvio (art. 312, caput, 2ª parte)**: direcionar dolosamente recursos estatais para destinação alheia ao interesse público, favorecendo a si ou a terceiro.",
                "**Peculato-Furto ou Impróprio (§ 1º)**: subtrair ou concorrer para a subtração valendo-se da facilidade proporcionada pela qualidade de funcionário quando não tem a posse direta.",
                "**Peculato Culposo (§ 2º)**: concorrência involuntária por negligência ou imprudência funcional para que outrem cometa peculato doloso ou furte bem sob custódia.",
                "**Reparação do Dano no Peculato Culposo (§ 3º)**: extingue a punibilidade se efetuada antes da sentença penal irrecorrível; reduz a sanção pela metade se posterior.",
                "**Peculato Mediante Erro de Outrem (art. 313)**: retenção indébita de quantia ou objeto entregue por equívoco espontâneo do usuário durante o atendimento estatal (peculato-estelionato)."
            ],
            "teoria": [
                {
                    "statement": "O estagiário de órgão público que atua temporariamente sem remuneração não pode figurar como sujeito ativo do crime de peculato.",
                    "isTrue": False,
                    "explanation": "O conceito do art. 327 do Código Penal abrange expressamente o exercício funcional transitório e até desprovido de remuneração pecuniária."
                },
                {
                    "statement": "A reparação voluntária do prejuízo efetuada antes do trânsito em julgado extingue a punibilidade no peculato praticado a título de culpa.",
                    "isTrue": True,
                    "explanation": "O art. 312, § 3º, prevê de modo expresso que a reparação integral precedente à sentença irrecorrível opera extinção da punibilidade no peculato culposo."
                },
                {
                    "statement": "No peculato-desvio, a consumação depende do efetivo enriquecimento ilícito do funcionário infrator com a vantagem patrimonial auferida.",
                    "isTrue": False,
                    "explanation": "O peculato-desvio consuma-se com a destinação indevida do recurso em proveito próprio ou alheio, sendo irrelevante a obtenção de lucro real."
                },
                {
                    "statement": "O peculato-furto diferencia-se do peculato próprio pelo fato de o servidor público não deter a posse prévia da coisa móvel subtraída.",
                    "isTrue": True,
                    "explanation": "No peculato-furto (art. 312, § 1º), o funcionário não tem a posse jurídica ou material do bem, valendo-se apenas de sua facilidade de acesso."
                }
            ],
            "revisao": [
                {
                    "statement": "A restituição da quantia apropriada antes do recebimento da denúncia no peculato doloso extingue a punibilidade do agente infrator.",
                    "isTrue": False,
                    "explanation": "No peculato doloso, a reparação do dano atua apenas como arrependimento posterior (art. 16) ou atenuante genérica (art. 65, III, b), sem extinguir a punibilidade."
                },
                {
                    "statement": "A ocupação de cargo comissionado de chefia na administração municipal atrai causa de aumento de pena de um terço nos crimes funcionais.",
                    "isTrue": True,
                    "explanation": "O art. 327, § 2º, estabelece a elevação de um terço da reprimenda para quem exerce cargo em comissão ou função de direção pública."
                },
                {
                    "statement": "O particular que auxilia funcionário público na subtração de bem público jamais responde por peculato em face de sua condição extraneus.",
                    "isTrue": False,
                    "explanation": "Pelo princípio da comunicabilidade das circunstâncias de caráter pessoal (art. 30 do CP), a elementar funcional comunica-se ao particular ciente dela."
                },
                {
                    "statement": "No peculato mediante erro de outrem, a conduta ardilosa de induzir a vítima em engano descaracteriza o artigo 313, tipificando estelionato.",
                    "isTrue": True,
                    "explanation": "Se o servidor cria a fraude dolosamente, pratica estelionato ou concussão; no art. 313 o erro da vítima surge espontaneamente sem provocação."
                }
            ],
            "pointers": [
                {"topic": "Conceito ampliado de funcionário público e causas de aumento", "pageRef": 3},
                {"topic": "Peculato-apropriação e peculato-desvio no art. 312 caput", "pageRef": 5},
                {"topic": "Peculato-furto e facilidade funcional no § 1º", "pageRef": 7},
                {"topic": "Peculato culposo e efeitos penais da reparação do dano", "pageRef": 9}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a07/s01",
        "fingerprint": get_fp("direito-penal/a07/s01"),
        "analytic": """Este segmento inaugural do Título XI da Parte Especial estuda a estrutura dogmática dos crimes funcionais próprios e impróprios, o conceito extensivo de servidor público para fins repressivos e as diversas modalidades de peculato positivadas nos artigos 312 e 313 do estatuto punitivo.

### O conceito extensivo de funcionário público (artigo 327)
O Código Penal adotou formulação eminentemente funcional e publicista para delimitar o círculo de sujeitos ativos dos crimes funcionais:
- *Regra Geral*: considera-se funcionário público quem, ainda que de forma transitória, eventual ou sem qualquer contraprestação financeira, desempenha cargo, emprego ou função em órgãos estatais;
- *Equiparação Funcional (§ 1º)*: estende-se tal condição aos empregados de paraestatais, concessionárias e prestadores terceirizados que executam atividade delegada típica da Administração Pública;
- *Majorante Especial (§ 2º)*: a reprimenda cominada sofre exasperação de **um terço** se o delito funcional for perpetrado por titulares de cargos em comissão ou por detentores de funções de assessoramento, direção ou chefia em órgãos da administração direta, autárquica ou fundacional;
- *Comunicabilidade ao Particular*: consoante o artigo 30 do estatuto penal, a condição elementar de funcionário público comunica-se ao comparsa civil (*extraneus*), desde que este tenha pleno e inequívoco conhecimento de tal qualidade pessoal do coautor.

### Peculato próprio e impróprio (artigo 312)
O delito de peculato tutela a integridade do patrimônio público e a probidade funcional do agente estatal:
- *Peculato-Apropriação (caput, primeira figura)*: caracteriza-se quando o agente se assenhoreia, como se proprietário fosse, de dinheiro, título ou bem móvel (seja pertencente ao Erário ou sob custódia de particular) de que detém a posse direta ou disponibilidade em virtude do cargo exercido;
- *Peculato-Desvio (caput, segunda figura)*: ocorre quando o servidor altera o destino legal de recursos públicos que tem à disposição, empregando-os em finalidade alheia ao interesse público (em proveito próprio ou para beneficiar terceiros), prescindindo de enriquecimento material consolidado;
- *Peculato-Furto ou Impróprio (§ 1º)*: incide quando o funcionário não detém a posse ou custódia da coisa, mas a subtrai ou facilita a subtração dolosa alheia valendo-se da facilidade de acesso que a sua investidura pública viabiliza.

### Peculato culposo e reparação do dano patrimonial (§§ 2º e 3º)
A legislação admite de modo excepcional a punição culposa do servidor desidioso:
- *Estrutura Culposa*: perfaz-se quando a quebra do dever objetivo de cuidado (negligência na guarda de cofres ou desleixo com chaves de depósitos) propicia materialmente o furto ou desvio empreendido por outrem;
- *Efeitos Especiais da Reparação*: nos termos do § 3º, a reparação civil integral do prejuízo consumada **antes da sentença irrecorrível opera a extinção da punibilidade do réu**; caso a reparação ocorra em momento posterior ao trânsito em julgado condenatório, gera a redução obrigatória da pena imposta na fração de metade;
- *Peculato Mediante Erro de Outrem (artigo 313)*: pune o servidor que retém e se apropria de bens ou valores recebidos no exercício do dever de ofício por erro espontâneo e desavisado da vítima, inexistindo qualquer provocação ardilosa prévia do agente.

### Para fixar
- O conceito penal de funcionário público abrange o exercício transitório e funções desprovidas de remuneração.
- A ocupação de chefia ou cargo em comissão eleva a sanção dos crimes funcionais em um terço.
- A elementar funcional comunica-se ao terceiro coautor particular ciente da condição do comparsa.
- O peculato-apropriação pressupõe a posse lícita anterior da coisa móvel em razão das atribuições funcionais.
- O peculato-furto ocorre quando o servidor não possui a guarda do bem, mas se vale de sua facilidade.
- A negligência funcional que viabiliza o cometimento de crime por terceiro tipifica o peculato culposo.
- A reparação do prejuízo antes do trânsito em julgado extingue a punibilidade no peculato culposo.
- No peculato mediante erro de outrem (art. 313), o equívoco da vítima deve ocorrer de forma espontânea.""",
        "synthetic": [
            "**Conceito Penal Ampliado (art. 327)**: abarca agentes transitórios ou gratuitos garantindo ampla salvaguarda à probidade administrativa.",
            "**Majorante Comissionada**: titulares de encargos diretivos ou postos de confiança suportam majoração em um terço na resposta penal.",
            "**Peculato-Apropriação (art. 312)**: inversão do ânimo de posse sobre bem móvel ou pecúnia confiada legitimamente ao ofício do servidor.",
            "**Peculato-Desvio**: direcionamento doloso indevido de verbas públicas para finalidades privadas ou alheias ao desígnio legal.",
            "**Peculato-Furto (§ 1º)**: subtração clandestina praticada por funcionário que não ostenta a custódia aproveitando-se das facilidades do cargo.",
            "**Peculato Culposo (§ 2º)**: desídia ou negligência na custódia de valores que viabiliza materialmente a prática delitiva por terceiros.",
            "**Extinção no Peculato Culposo**: restauração do dano antes do trânsito em julgado extingue a punibilidade penal do servidor imprudente.",
            "**Peculato Mediante Erro (art. 313)**: retenção fraudulenta de quantias entregues por equívoco espontâneo do usuário sem provocação do funcionário."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 02: Inserção Falsa, Concussão e Corrupção (p. 11-20)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a07/s02",
        "bizu": {
            "summary": [
                "**Inserção de Dados Falsos em Sistema (art. 313-A)**: crime próprio praticado exclusivamente por funcionário formalmente autorizado visando proveito indevido ou dano.",
                "**Modificação Não Autorizada de Sistema (art. 313-B)**: alterar dados ou programa sem autorização (crime praticado por qualquer funcionário, mesmo não autorizado).",
                "**Extravio ou Inutilização de Documento (art. 314)**: extraviar, sonegar ou inutilizar livro oficial ou documento sob guarda funcional em prejuízo público.",
                "**Emprego Irregular de Verbas Públicas (art. 315)**: aplicar recursos em desacordo com as destinações legais orçamentárias (crime formal que tutela a lei de finanças).",
                "**Concussão (art. 316, caput)**: exigir, para si ou outrem, direta ou indiretamente, vantagem indevida em razão da função (reclusão de 2 a 12 anos).",
                "**Verbo Nuclear 'Exigir'**: na concussão há postura impositiva de coação moral intimidadora, ao passo que na corrupção passiva há mero pedido ou solicitação.",
                "**Excesso de Exação (§ 1º do art. 316)**: exigir tributo sabidamente indevido ou empregar meio vexatório ou gravoso na cobrança funcional que a lei veda.",
                "**Corrupção Passiva (art. 317)**: solicitar ou receber vantagem indevida, ou aceitar promessa de tal retribuição, para praticar ou omitir ato funcional.",
                "**Corrupção Passiva Privilegiada (§ 2º)**: praticar ou retardar ato funcional cedendo a pedido, súplica ou influência sentimental de outrem (detenção de 3 meses a 1 ano)."
            ],
            "teoria": [
                {
                    "statement": "O crime de inserção de dados falsos em sistema de informações (art. 313-A) pode ser cometido por qualquer servidor público, ainda que desautorizado.",
                    "isTrue": False,
                    "explanation": "O art. 313-A é crime de mão própria funcional restrito exclusivamente ao servidor legalmente autorizado a operar o sistema de dados."
                },
                {
                    "statement": "O delito de concussão aperfeiçoa a sua consumação no momento em que o funcionário público profere a exigência da vantagem indevida.",
                    "isTrue": True,
                    "explanation": "A concussão é crime formal de consumação antecipada, aperfeiçoando-se com a exigência, independentemente do efetivo recebimento do valor."
                },
                {
                    "statement": "A solicitação de vantagem indevida formalizada por servidor público fora de sua repartição antes de tomar posse consuma corrupção passiva.",
                    "isTrue": True,
                    "explanation": "O art. 317 alcança a ilicitude perpetrada mesmo em período de férias, afastamento legal ou antes da posse formal, desde que motivada pelas futuras atribuições."
                },
                {
                    "statement": "No excesso de exação qualificado pelo desvio (§ 2º do art. 316), o agente aplica a quantia recolhida integralmente nos cofres públicos da comarca.",
                    "isTrue": False,
                    "explanation": "No § 2º o agente desvia o tributo ou contribuição cobrada indevidamente em proveito próprio ou de terceiros, não recolhendo ao erário."
                }
            ],
            "revisao": [
                {
                    "statement": "O policial que exige dinheiro de motorista para não lavrar auto de infração de trânsito pratica o crime de corrupção passiva simples.",
                    "isTrue": False,
                    "explanation": "A postura impositiva lastreada no verbo 'exigir' amolda-se à concussão (art. 316); a corrupção passiva (art. 317) pressupõe solicitar ou receber."
                },
                {
                    "statement": "A corrupção passiva consuma-se com a mera aceitação da promessa de retribuição pecuniária futura para violação de dever de ofício.",
                    "isTrue": True,
                    "explanation": "Trata-se de crime formal que atinge consumação instantânea com a aceitação da promessa ou com a solicitação da vantagem espúria."
                },
                {
                    "statement": "O crime de emprego irregular de verbas públicas (art. 315) pressupõe o desvio dos recursos estatais para enriquecimento pessoal do administrador.",
                    "isTrue": False,
                    "explanation": "Se houver apropriação particular há peculato; o art. 315 pune a mera aplicação dos recursos em finalidade pública diversa da prescrita na lei orçamentária."
                },
                {
                    "statement": "O funcionário que cede a pedido ou influência de familiar e retarda ato de ofício sem vantagem financeira comete corrupção passiva privilegiada.",
                    "isTrue": True,
                    "explanation": "O art. 317, § 2º, comina detenção branda à conduta de ceder a pedidos ou influência alheia sem recebimento de propina patrimonial."
                }
            ],
            "pointers": [
                {"topic": "Peculato eletrônico e inserção fraudulenta no art. 313-A", "pageRef": 12},
                {"topic": "Extravio de documentos e aplicação irregular de verbas", "pageRef": 14},
                {"topic": "Concussão e excesso de exação no art. 316", "pageRef": 16},
                {"topic": "Corrupção passiva e modalidade privilegiada no art. 317", "pageRef": 19}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a07/s02",
        "fingerprint": get_fp("direito-penal/a07/s02"),
        "analytic": """Este segmento aborda os crimes praticados por funcionário público contra os sistemas informatizados da administração, a fidelidade documental e financeira, bem como os delitos de exação ilícita, concussão e corrupção passiva no estatuto repressivo.

### Crimes contra sistemas de dados e documentos (artigos 313-A e 313-B)
A modernização das rotinas estatais motivou a criação de tipos específicos de salvaguarda eletrônica:
- *Inserção de Dados Falsos em Sistema de Informações (artigo 313-A)*: vulgarmente denominado 'peculato eletrônico', comina severa pena de reclusão de dois a doze anos. É **crime próprio restrito ao funcionário autorizado**, exigindo especial fim de agir consistente em granjear proveito ilícito para si ou terceiro ou produzir gravame danoso ao Erário;
- *Modificação ou Alteração Não Autorizada (artigo 313-B)*: pune qualquer servidor (mesmo sem autorização de senha) que realiza modificações em programas ou bancos de dados públicos sem chancela formal da chefia competente, tutelando a higidez do ambiente cibernético da administração;
- *Extravio, Sonegação ou Inutilização de Livro ou Documento (artigo 314)*: protege a documentação oficial física ou digital sob a guarda funcional do servidor;
- *Emprego Irregular de Verbas ou Rendas Públicas (artigo 315)*: tutela a legalidade orçamentária estrita. Consuma-se quando o gestor canaliza recursos para obra pública distinta daquela formalmente consignada em lei. Caso o dinheiro seja apropriado para finalidade particular egoística, opera-se o crime mais grave de peculato.

### Concussão e excesso de exação (artigo 316)
O preceito do artigo 316 sanciona atos coercitivos e de abuso de autoridade fazendária:
- *Concussão (caput)*: comina pena de reclusão de **dois a doze anos e multa** para quem **exige**, direta ou indiretamente, vantagem indevida em razão do cargo exercido (mesmo durante licenças, férias ou antes da investidura formal, contanto que vinculado ao ofício). Cuida-se de crime formal e de consumação antecipada que se aperfeiçoa no exato instante em que a exigência é formulada;
- *Excesso de Exação (§ 1º)*: ocorre na atividade tributária quando o agente fiscal exige imposto sabidamente indevido ou, sendo devido, vale-se de meios vexatórios, ultrajantes ou gravosos não chancelados pela lei tributária vigente;
- *Excesso Qualificado pelo Desvio (§ 2º)*: figura gravíssima que sanciona o fiscal que, após arrecadar indevidamente os valores do contribuinte, desvia a quantia recolhida para o patrimônio particular de outrem em vez de canalizá-la aos cofres do Tesouro.

### Corrupção passiva (artigo 317)
O crime de corrupção passiva pune a venalidade funcional do servidor público:
- *Núcleos Típicos*: estrutura-se nos verbos **solicitar**, **receber** para si ou terceiro, ou **aceitar promessa** de vantagem indevida em razão de suas atribuições funcionais;
- *Natureza Jurídica*: é crime formal na solicitação e na aceitação da promessa, consumando-se antes mesmo da entrega real do dinheiro ou realização do ato pretendido;
- *Majorante Especial (§ 1º)*: exaspera-se a pena em um terço se o agente, em consequência da vantagem ou promessa, efetivamente retarda, omite ou pratica o ato com infração de dever de ofício;
- *Corrupção Passiva Privilegiada (§ 2º)*: comina detenção atenuada de três meses a um ano caso o servidor cometa, retarde ou omita ato de ofício não por propina financeira, mas cedendo compadecidamente a súplicas, pedidos ou influência de terceiros.

### Para fixar
- O art. 313-A é crime próprio aplicável somente ao funcionário formalmente autorizado a operar o sistema.
- A modificação não autorizada (art. 313-B) pune qualquer servidor que adultere sistemas da administração.
- O emprego irregular de verbas (art. 315) ocorre sem apropriação particular quando se viola a lei orçamentária.
- A concussão (art. 316) tem como núcleo o verbo exigir e consuma-se com a imposição da coação.
- O recebimento da propina na concussão constitui mero exaurimento impunível do delito consumado.
- O excesso de exação reprime a cobrança de tributo sabidamente indevido ou por expediente vexatório.
- A corrupção passiva (art. 317) consuma-se com a solicitação ou recebimento de vantagem funcional indevida.
- Ceder a pedido ou influência alheia sem receber vantagens econômicas caracteriza corrupção privilegiada.""",
        "synthetic": [
            "**Peculato Eletrônico (art. 313-A)**: inserção fraudulenta restrita a servidor credenciado operada com propósito doloso de proveito ou dano.",
            "**Alteração Não Autorizada (art. 313-B)**: punição a quem modifica sistemas estatais sem deter prerrogativa técnica formal chancelada.",
            "**Emprego Irregular (art. 315)**: violação às normas orçamentárias mediante desvio de verbas públicas para outros fins estatais legítimos.",
            "**Concussão (art. 316)**: imposição intimidadora exigindo vantagem indevida funcional consumada no exato momento da exteriorização intimidativa.",
            "**Excesso de Exação**: abuso fazendário na arrecadação indevida ou imposição de expedientes vexatórios e humilhantes contra contribuintes.",
            "**Corrupção Passiva (art. 317)**: mercancia da função mediante solicitação ou recebimento de recompensa pecuniária desprovida de lastro.",
            "**Majorante por Ato Infringido**: exasperação de um terço na dosimetria penal ante a efetiva vulneração corrupta do dever público de ofício.",
            "**Corrupção Privilegiada (§ 2º)**: descumprimento do dever administrativo movido por compaixão ante súplicas sem recebimento de propina."
        ]
    })

    return items, summaries
