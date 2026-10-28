# -*- coding: utf-8 -*-
"""Part 2 for a09: s04, s05 (Exploração de Prestígio, Finanças Públicas e Crimes da LRF)."""

def get_part2_data(get_fp):
    items = []
    summaries = []

    # -------------------------------------------------------------
    # SEGMENT 04: Exploração de Prestígio e Arrematação (p. 43-53)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a09/s04",
        "bizu": {
            "summary": [
                "**Exploração de Prestígio (art. 357)**: solicitar ou amealhar proveito a pretexto de exercer influência sobre magistrado, jurado, promotor ou testemunha.",
                "**Distinção com Tráfico de Influência**: no art. 332 a influência recai sobre funcionário público genérico; no art. 357 atinge especificamente atores da Justiça.",
                "**Majorante por Alegação de Rateio (parágrafo único)**: exasperação de um terço na pena se o autor insinua que a propina destina-se também ao magistrado ou membro do MP.",
                "**Fraude em Arrematação Judicial (art. 358)**: perturbar leilão judiciário ou afastar arrematante mediante o emprego de ameaça, violência ou oferta de dádiva pecuniária.",
                "**Desobediência a Decisão sobre Direito (art. 359)**: exercer cargo, ofício, habilitação ou múnus de que se acha privado ou suspenso por provimento jurisdicional.",
                "**Crime Próprio de Decisão Judicial**: pressupõe a existência de determinação do Poder Judiciário decretando a interdição temporária ou definitiva do direito.",
                "**Inaplicabilidade à Decisão Administrativa**: o descumprimento de suspensão imposta unicamente por conselho de classe ou órgão de trânsito não tipifica o art. 359.",
                "**Súmula 18 do STJ e Competência**: a fixação de competência jurisdicional rege-se pela natureza do interesse federal ou estadual envolvido na administração da justiça."
            ],
            "teoria": [
                {
                    "statement": "O intermediador que solicita vantagem financeira afirmando possuir influência espúria sobre o juiz da causa comete exploração de prestígio.",
                    "isTrue": True,
                    "explanation": "O art. 357 tipifica expressamente a conduta de solicitar vantagem a pretexto de influenciar magistrado ou membros do Ministério Público."
                },
                {
                    "statement": "O crime de exploração de prestígio diferencia-se do tráfico de influência pelo fato de a vantagem ser destinada à autoridade do Poder Executivo.",
                    "isTrue": False,
                    "explanation": "Na exploração de prestígio a suposta influência é voltada aos atores da Justiça; perante o Poder Executivo tipifica-se o tráfico de influência (art. 332)."
                },
                {
                    "statement": "O motorista que dirige com a CNH suspensa por deliberação do Detran comete o crime do artigo 359 do Código Penal.",
                    "isTrue": False,
                    "explanation": "O art. 359 exige descumprimento de decisão judicial; a suspensão administrativa de trânsito consubstancia mera infração do CTB."
                },
                {
                    "statement": "A pena cominada à exploração de prestígio sofre acréscimo de um terço se o agente insinua que o valor será partilhado com o jurado do Tribunal do Júri.",
                    "isTrue": True,
                    "explanation": "O parágrafo único do art. 357 exaspera a sanção em 1/3 se o autor alega ou insinua que o benefício financeiro destina-se também ao jurado."
                }
            ],
            "revisao": [
                {
                    "statement": "O crime de fraude em arrematação judicial (art. 358) consubstancia infração penal que admite o concurso mediante oferta de suborno a concorrente.",
                    "isTrue": True,
                    "explanation": "O tipo reprime afastar concorrente por violência, grave ameaça, promessa ou dádiva pecuniária no pregão do leilão público."
                },
                {
                    "statement": "A exploração de prestígio exige que o magistrado ou promotor realmente receba a propina para que se dê a consumação do delito.",
                    "isTrue": False,
                    "explanation": "É crime formal de consumação antecipada que se aperfeiçoa com a solicitação ou recebimento da quantia pelo explorador, inexistindo conluio com o juiz."
                },
                {
                    "statement": "O advogado suspenso cautelarmente por provimento da OAB que segue atuando em audiências comete o crime do art. 359 do CP.",
                    "isTrue": False,
                    "explanation": "A suspensão administrativa emanada de entidade corporativa não se amolda à 'decisão judicial' exigida pelo preceito do artigo 359."
                },
                {
                    "statement": "No crime do artigo 358 do Código Penal, se o agente empregar violência corporal física, as penas da violência são aplicadas em cumulação.",
                    "isTrue": True,
                    "explanation": "Aplica-se a regra geral da repressão à violência que não resta absorvida quando cominada sem prejuízo da lesão corporal ou morte decorrente."
                }
            ],
            "pointers": [
                {"topic": "Exploração de prestígio e distinção com tráfico de influência", "pageRef": 44},
                {"topic": "Majorante de insinuação de repasse aos operadores da justiça", "pageRef": 46},
                {"topic": "Fraude em arrematação judicial no art. 358", "pageRef": 49},
                {"topic": "Desobediência a provimento jurisdicional suspensivo no art. 359", "pageRef": 52}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a09/s04",
        "fingerprint": get_fp("direito-penal/a09/s04"),
        "analytic": """Este segmento aborda as tipificações que resguardam o decoro e a probidade do Poder Judiciário, focando no crime de exploração de prestígio (artigo 357), na preservação das hastas públicas em arrematações e na eficácia coercitiva de decisões restritivas de direito.

### Exploração de prestígio perante a Justiça (artigo 357)
O artigo 357 comina reclusão de um a cinco anos e multa à conduta do farsante que mercantiliza sua proximidade com a prestação jurisdicional:
- *Núcleos e Sujeitos Tutelados*: sanciona quem solicita ou aufere vantagem patrimonial ou de qualquer outra índole, a pretexto de interceder ou influenciar deliberações de **juiz, jurado do Conselho de Sentença, órgão do Ministério Público, perito judicial, tradutor, intérprete ou testemunha**;
- *Confronto Hermenêutico com o Tráfico de Influência (artigo 332)*:
  1. No *Tráfico de Influência*, a intermediação espúria é anunciada perante servidor público ordinário da Administração Pública (como fiscais tributários, policiais civis ou diretores de autarquias);
  2. Na *Exploração de Prestígio*, a promessa corruptora atinge especificamente os operadores, magistrados e partícipes formais do Poder Judiciário e da função jurisdicional;
- *Majorante Especial (parágrafo único)*: exaspera-se a reprimenda cominada na fração de **um terço** caso o infrator insinue, sugira ou afirme perante a vítima que a remuneração cobrada é exigida pelo próprio magistrado ou rateada com o promotor de justiça da vara.

### Fraudes em leilões judiciais e descumprimento de sentenças (artigos 358 e 359)
A solenidade dos atos processuais e a coercibilidade das sanções encontram amparo sancionador:
- *Violência ou Fraude em Arrematação Judicial (artigo 358)*: tutela o patrimônio sob alienação e a igualdade dos licitantes em leilões forenses. Pune quem obsta, perturba ou frauda ato de hasta pública, ou emprega ameaças, violência física, dádivas ou promessas de compensação financeira para afastar licitantes concorrentes;
- *Desobediência a Decisão Judicial sobre Perda ou Suspensão de Direito (artigo 359)*: incrimina o comportamento do indivíduo que volta a exercer múnus público, profissão, cargo, habilitação ou mandato de que foi legalmente privado ou suspenso em virtude de provimento emanado do Poder Judiciário;
- *Exigência de Título Judicial*: o preceito do artigo 359 reclama imperativamente a existência de **decisão condenatória ou cautelar proferida por juiz togado**. Caso a interdição decorra de processo administrativo promovido por órgão de trânsito ou conselho profissional de fiscalização, a conduta é atípica perante a órbita penal.

### Para fixar
- A exploração de prestígio (art. 357) tutela o prestígio dos órgãos e atores da função jurisdicional.
- Diferencia-se do art. 332 porque este visa servidores administrativos em geral e não membros da Justiça.
- A insinuação de que o juiz ou jurado receberá fração da quantia eleva a reprimenda em um terço.
- O crime consuma-se com a solicitação ou cobrança de vantagem cominando pena privativa de liberdade.
- O art. 358 reprime a frustração desleal da igualdade de concorrentes em arrematações forenses.
- A violência praticada em arrematações cumula-se formalmente com a pena da lesão corporal provocada.
- O art. 359 exige decisão judicial para configurar a desobediência a suspensão de atividade.
- O descumprimento de restrição imposta por órgão meramente administrativo não tipifica o art. 359.""",
        "synthetic": [
            "**Exploração de Prestígio (art. 357)**: solicitação mercenária de utilidades alegando ascendência fática sobre juízes, promotores ou peritos judiciais.",
            "**Diferenciação Funcional**: distinção com o tráfico de influência restrito aos servidores ordinários do Poder Executivo em geral.",
            "**Majorante de Rateio**: aumento de um terço na reprimenda caso haja insinuação dolosa de que a propina subsidiará o magistrado.",
            "**Consumação Formal**: aperfeiçoamento da infração no instante da postulação remuneratória dispensando qualquer contato real com a autoridade judicial.",
            "**Arrematação Forense (art. 358)**: proteção contra conluios, fraudes ou violências orientadas a afastar arrematantes em hasta judiciária.",
            "**Desobediência Jurisdicional (art. 359)**: exercício espúrio de encargos ou atividades expressamente interditadas por decisão da magistratura.",
            "**Imprescritibilidade do Provimento**: exigência indeclinável de édito judicial excluindo punição de sanções unicamente administrativas de conselho.",
            "**Garantia da Autoridade Jurisdicional**: salvaguarda indeclinável da autoridade das ordens mandamentais emanadas pelo Poder Judiciário."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 05: Crimes contra as Finanças Públicas (p. 54-67)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a09/s05",
        "bizu": {
            "summary": [
                "**Crimes contra as Finanças Públicas**: preceitos dos arts. 359-A a 359-H acrescidos pela Lei 10.028/2000 em consonância com a Lei de Responsabilidade Fiscal.",
                "**Empréstimo Governamental Irregular (art. 359-A)**: celebração de financiamento ou mútuo estatal desprovido de respaldo legislativo orçamentário ou deliberação senatorial.",
                "**Inscrição Indevida em Restos a Pagar (art. 359-B)**: inscrever em restos a pagar despesa que não tenha sido previamente empenhada na forma legal.",
                "**Assunção de Obrigação no Último Ano (art. 359-C)**: ordenar despesa nos últimos dois quadrimestres do mandato que não possa ser paga integralmente no exercício.",
                "**Ordenação de Despesa Não Autorizada (art. 359-D)**: ordenar despesa que não esteja consignada formalmente nas leis orçamentárias anuais em vigor.",
                "**Prestação de Garantia Graciosa (art. 359-E)**: prestar garantia do ente público sem a exigência de contragarantia legalmente fixada pelo poder legislativo.",
                "**Não Cancelamento de Restos a Pagar (art. 359-F)**: deixar de cancelar restos a pagar cuja quantia exceda o limite legal estabelecido na legislação fiscal.",
                "**Aumento de Despesa com Pessoal (art. 359-G)**: ordenar ato que acarrete aumento de despesa de pessoal nos cento e oitenta dias que antecedem o fim do mandato.",
                "**Sujeito Ativo Qualificado**: infrações penais próprias restritas a autoridades que desempenham o múnus de ordenadores de despesas públicas governamentais."
            ],
            "teoria": [
                {
                    "statement": "A conduta proibida de contrair obrigações financeiras desprovidas de lastro em final de gestão (art. 359-C) incide sobre atos praticados nos dois últimos quadrimestres.",
                    "isTrue": True,
                    "explanation": "O art. 359-C reprime a ordenação de despesa nos dois últimos quadrimestres do mandato cuja contrapartida de caixa inexista para o exercício seguinte."
                },
                {
                    "statement": "O delito de aumento de despesa total com pessoal qualifica-se como crime comum praticado por qualquer servidor público da repartição.",
                    "isTrue": False,
                    "explanation": "Os crimes dos artigos 359-A a 359-H são crimes próprios de gestores públicos com competência funcional para ordenar gastos e despesas."
                },
                {
                    "statement": "A concessão de garantia estatal desprovida de contragarantia exigida na legislação financeira amolda-se formalmente ao art. 359-E do CP.",
                    "isTrue": True,
                    "explanation": "O art. 359-E pune expressamente a prestação de garantia graciosa ou sem contraprestação prevista nas normas financeiras."
                },
                {
                    "statement": "A realização de operação de crédito sem expressa autorização do Senado Federal consubstancia mera infração político-administrativa desprovida de sanção penal.",
                    "isTrue": False,
                    "explanation": "O art. 359-A do Código Penal tipifica expressamente a conduta como crime cominando sanção de reclusão de um a dois anos."
                }
            ],
            "revisao": [
                {
                    "statement": "O crime de ordenação de despesa não autorizada (art. 359-D) admite a modalidade culposa decorrente de negligência do corpo contábil da prefeitura.",
                    "isTrue": False,
                    "explanation": "Não há previsão culposa para os crimes contra as finanças públicas, exigindo-se dolo direto do ordenador de despesa estatal."
                },
                {
                    "statement": "A formalização contábil em restos a pagar de encargo destituído de prévio e regular empenho orçamentário amolda-se ao artigo 359-B do estatuto punitivo.",
                    "isTrue": True,
                    "explanation": "O art. 359-B sanciona a formalização de restos a pagar desprovidos de regular empenho orçamentário antecedente."
                },
                {
                    "statement": "O aumento da despesa de pessoal promovido no primeiro semestre do mandato executivo subsume-se ao tipo do artigo 359-G do Código Penal.",
                    "isTrue": False,
                    "explanation": "O art. 359-G restringe a ilicitude penal aos atos expedidos nos 180 dias anteriores ao término do mandato ou da legislatura."
                },
                {
                    "statement": "Os crimes contra as finanças públicas foram inseridos no Código Penal para operacionalizar as sanções da Lei de Responsabilidade Fiscal.",
                    "isTrue": True,
                    "explanation": "A Lei 10.028/2000 introduziu o Capítulo IV no Título XI do CP para punir penalmente o descumprimento das regras orçamentárias da LRF."
                }
            ],
            "pointers": [
                {"topic": "Crimes de finanças públicas e contexto da Lei 10.028/2000", "pageRef": 55},
                {"topic": "Operações de crédito sem autorização legal no art. 359-A", "pageRef": 58},
                {"topic": "Assunção de obrigações e aumento de pessoal no fim do mandato", "pageRef": 62},
                {"topic": "Ordenação de despesa e prestação de garantia graciosa", "pageRef": 65}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a09/s05",
        "fingerprint": get_fp("direito-penal/a09/s05"),
        "analytic": """Este segmento finaliza a temática dos crimes contra a Administração Pública analisando o Capítulo IV do Título XI, introduzido pela Lei nº 10.028/2000 para conferir tutela penal às diretrizes de probidade e equilíbrio fiscal disciplinadas pela Lei de Responsabilidade Fiscal (Lei Complementar nº 101/2000).

### Diretrizes gerais dos crimes contra as finanças públicas
A disciplina penal dos artigos 359-A a 359-H estrutura-se em salvaguardas macrofiscais do Estado:
- *Sujeito Ativo Específico*: consubstanciam crimes próprios materiais ou formais praticados exclusivamente por autoridades que ostentam a competência normativa de **ordenadores de despesa** (prefeitos, governadores, secretários de fazenda, presidentes de cortes de contas e dirigentes de casas legislativas);
- *Inadmissão de Culpa*: todas as condutas delineadas no capítulo reclamam o dolo estrito, restando penalmente atípicos equívocos orçamentários involuntários ou meras imperfeições contábeis destituídas de má-fé deliberada.

### Das operações de crédito e assunção no final de mandato (artigos 359-A a 359-D)
O estatuto repressivo pune práticas irresponsáveis de endividamento público:
- *Contratação de Operação de Crédito sem Autorização (artigo 359-A)*: sanciona com reclusão de um a dois anos a ordenação ou celebração de empréstimos e mútuos estatais sem prévia autorização da respectiva lei orçamentária ou sem o crivo indispensável do Senado Federal;
- *Inscrição em Restos a Pagar sem Empenho (artigo 359-B)*: reprime a inserção dolosa de créditos em restos a pagar desprovidos de prévio e regular empenho orçamentário formal;
- *Assunção de Obrigação no Último Ano de Gestão (artigo 359-C)*: comina reclusão de **um a quatro anos** ao governante que assume obrigação nos dois últimos quadrimestres de seu mandato executivo cuja despesa não possa ser liquidada no próprio exercício ou cujas parcelas subsequentes fiquem desprovidas de suficiente contrapartida de recursos financeiros de caixa;
- *Ordenação de Despesa Não Autorizada por Lei (artigo 359-D)*: reprova a ordem de liberação ou comprometimento de recursos que não estejam formalmente previstos na lei orçamentária em vigor.

### Garantias e aumento de gastos com folha salarial (artigos 359-E a 359-G)
Regras adicionais impedem a dilapidação do Erário às vésperas de transições republicanas:
- *Garantia Graciosa (artigo 359-E)*: pune o chefe do executivo que presta garantia fiduciária do ente federado desprovida de contragarantia equivalente exigida pelas normas de finanças públicas;
- *Aumento de Despesa com Pessoal (artigo 359-G)*: sanciona a prática demagógica de autorizar, expedir ou sancionar atos que acarretem a elevação global dos gastos com folha de pagamento do funcionalismo nos **cento e oitenta dias que antecedem o término do mandato** ou legislatura, resguardando o sucessor eleito de déficits estruturais irreversíveis.

### Para fixar
- Os crimes dos arts. 359-A a 359-H foram criados pela Lei 10.028/2000 em suporte às diretrizes da LRF.
- Todos os tipos contra as finanças públicas consubstanciam crimes próprios de ordenadores de despesas.
- Não há previsão de figura culposa para as infrações penais contra a gestão das finanças governamentais.
- O art. 359-A reprime a tomada de empréstimos estatais sem autorização legal ou do Senado Federal.
- A inscrição em restos a pagar exige empenho orçamentário formal sob pena de tipificação no art. 359-B.
- O art. 359-C pune despesas criadas nos dois últimos quadrimestres sem disponibilidade financeira de caixa.
- O art. 359-D pune a realização ou ordenação de gastos desprovidos de previsão orçamentária expressa.
- É proibido elevar gastos totais de pessoal nos 180 dias finais do mandato sob pena de reclusão.""",
        "synthetic": [
            "**Tutela Fiscal da LRF**: delitos introduzidos pela Lei 10.028/2000 para assegurar a higidez macroeconômica e a responsabilidade das contas estatais.",
            "**Crimes de Gestores Próprios**: sujeição ativa restrita a ordenadores de despesas e autoridades decisórias no topo do organograma da máquina pública.",
            "**Crédito Desautorizado (art. 359-A)**: celebração de financiamentos e mútuos estatais desprovidos de aprovação do legislativo ou do Senado Federal.",
            "**Restos a Pagar Irregulares (art. 359-B)**: inscrição orçamentária arbitrária de despesas não empenhadas previamente na forma da legislação financeira.",
            "**Despesas no Fim de Mandato (art. 359-C)**: criação de encargos nos dois últimos quadrimestres desprovidos de suficiente suporte financeiro de caixa.",
            "**Gastos Extralegais (art. 359-D)**: ordenação ou autorização de despesas públicas sem chancela prévia na lei orçamentária anual vigente.",
            "**Garantia Sem Lastro (art. 359-E)**: prestação de fiança governamental graciosa sem formalização de contragarantia exigida pelo ordenamento.",
            "**Vedação Salarial de Transição (art. 359-G)**: veto absoluto a acréscimos na despesa com pessoal nos cento e oitenta dias que antecedem o fim da gestão."
        ]
    })

    return items, summaries
