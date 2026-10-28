# -*- coding: utf-8 -*-
"""Builder for direito-penal a01 (items and summaries)."""
import json
import os

ITEMS_FILE = "content/items/direito-penal/a01.json"
SUMMARIES_FILE = "content/summaries/direito-penal/a01.json"

os.makedirs(os.path.dirname(ITEMS_FILE), exist_ok=True)
os.makedirs(os.path.dirname(SUMMARIES_FILE), exist_ok=True)

# Load exact segment info from segments file
with open("content/segments/direito-penal.json", "r", encoding="utf-8") as f:
    all_segs = {s["id"]: s for s in json.load(f)["segments"]}

def get_fp(sid):
    s = all_segs[sid]
    return {"startPage": s["startPage"], "endPage": s["endPage"], "startTopic": s["startTopic"]}

# ---------------------------------------------------------
# BIZU ITEMS (a01)
# ---------------------------------------------------------
items_data = {
    "aula": "direito-penal/a01",
    "batch": "pcpe-bizu-direito-penal",
    "status": "DRAFT",
    "stage": "bizu",
    "segments": [
        {
            "id": "direito-penal/a01/s01",
            "bizu": {
                "summary": [
                    "**Tempo do Crime**: adotou-se no artigo 4º do Código Penal a Teoria da Atividade, considerando-se praticada a infração no instante da ação ou omissão, ainda que outro seja o instante do resultado.",
                    "**Extratividade da Lei Penal**: gênero que abrange a retroatividade benéfica e a ultratividade de normas já revogadas para alcançar acontecimentos pretéritos.",
                    "**Novatio Legis In Pejus**: lei posterior mais gravosa não retroage sob hipótese alguma, aplicando-se o princípio da irretroatividade da lei penal desfavorável.",
                    "**Novatio Legis In Mellius**: diploma superveniente mais benéfico possui eficácia retroativa irrestrita, beneficiando o acusado mesmo com trânsito em julgado formado.",
                    "**Abolitio Criminis**: extingue integralmente os efeitos penais principais e secundários da condenação, conservando intactos unicamente os efeitos extrapenais civis.",
                    "**Vedação à Lex Tertia (Súmula 501 do STJ)**: é vedado ao juiz selecionar partes benéficas de leis distintas para criar um terceiro estatuto normativo híbrido.",
                    "**Leis Temporárias e Excepcionais**: possuem autorrevogabilidade e ultratividade gravosa obrigatória, incidindo sobre fatos praticados em sua vigência mesmo após a sua cessação.",
                    "**Crimes Permanentes e Continuados (Súmula 711 do STF)**: aplica-se a lei nova mais severa se a sua entrada em vigor ocorreu antes da cessação da continuidade ou permanência.",
                    "**Vacatio Legis**: lapso temporal entre a publicação e a entrada em vigor durante o qual a nova lei não produz efeitos punitivos no ordenamento jurídico.",
                    "**Competência na Execução Penal (Súmula 611 do STF)**: após o trânsito em julgado de condenação, a aplicação da lei penal mais benigna compete ao Juízo das Execuções.",
                    "**Complementos da Norma Penal em Branco**: alteração do complemento de norma em branco retroage se importar real modificação favorável do preceito sancionatório.",
                    "**Período de Transição Normativa**: a apuração de qual legislação é mais favorável deve ser realizada no caso concreto com a análise global de cada diploma."
                ],
                "teoria": [
                    {
                        "statement": "O Código Penal acolheu expressamente a teoria do resultado para a determinação do momento exato do cometimento da conduta delituosa.",
                        "isTrue": False,
                        "explanation": "O art. 4º do Código Penal acolheu a teoria da atividade, fixando o tempo do delito no momento da ação ou omissão delitiva."
                    },
                    {
                        "statement": "A ocorrência de abolitio criminis faz cessar a execução penal e os efeitos secundários penais da sentença condenatória transitada em julgado.",
                        "isTrue": True,
                        "explanation": "A descriminalização apaga a sanção e todos os efeitos secundários penais como reincidência, preservando apenas as obrigações civis de indenização."
                    },
                    {
                        "statement": "O magistrado criminal pode mesclar dispositivos benéficos de diplomas sucessivos distintos para conceber uma terceira norma penal mais favorável ao sentenciado.",
                        "isTrue": False,
                        "explanation": "A Súmula 501 do Superior Tribunal de Justiça veda expressamente a combinação de leis penais para criar uma lex tertia judicial."
                    },
                    {
                        "statement": "As leis excepcionais e temporárias possuem ultratividade, aplicando-se aos fatos cometidos sob o seu império mesmo após expirado o seu período de duração.",
                        "isTrue": True,
                        "explanation": "Conforme o art. 3º do Código Penal, as leis intermitentes são dotadas de ultratividade legal, punindo condutas ocorridas durante sua vigência."
                    }
                ],
                "revisao": [
                    {
                        "statement": "Na hipótese de delito continuado ou permanente, incide a lei penal novel mais severa caso a sua vigência anteceda a cessação do iter delitivo.",
                        "isTrue": True,
                        "explanation": "Consoante o enunciado da Súmula 711 do STF, aplica-se a lei mais grave se a continuidade ou permanência perdurar após a sua entrada em vigor."
                    },
                    {
                        "statement": "A novatio legis in pejus pode atingir fatos consumados antes de sua publicação caso trate exclusivamente de prazo de cumprimento de pena privativa.",
                        "isTrue": False,
                        "explanation": "A irretroatividade da lei penal desfavorável é dogma constitucional pétreo que interdita qualquer aplicação retroativa gravosa."
                    },
                    {
                        "statement": "O instituto da abolitio criminis afasta a obrigação civil do condenado de reparar os prejuízos patrimoniais suportados pela vítima da conduta despenalizada.",
                        "isTrue": False,
                        "explanation": "A abolitio criminis extingue tão somente os reflexos penais do julgamento, remanescendo incólumes os efeitos extrapenais e a reparação civil do dano."
                    },
                    {
                        "statement": "Compete privativamente ao Juízo das Execuções Penais a aplicação de lei superveniente mais benéfica após a consolidação do trânsito em julgado condenatório.",
                        "isTrue": True,
                        "explanation": "A Súmula 611 do Supremo Tribunal Federal estabelece que, transitada em julgado a condenação, a aplicação da lei mais benigna cabe ao juízo da execução."
                    }
                ],
                "pointers": [
                    {"topic": "Tempo do crime e teoria da atividade no artigo 4º", "pageRef": 3},
                    {"topic": "Conflito de leis penais no tempo e abolitio criminis", "pageRef": 5},
                    {"topic": "Vedação da combinação de leis e Súmula 501 do STJ", "pageRef": 9},
                    {"topic": "Leis temporárias, excepcionais e ultratividade legal", "pageRef": 12},
                    {"topic": "Crimes permanentes e aplicação da Súmula 711 do STF", "pageRef": 15}
                ]
            }
        },
        {
            "id": "direito-penal/a01/s02",
            "bizu": {
                "summary": [
                    "**Lugar do Crime**: o artigo 6º do Código Penal consagrou a Teoria da Ubiquidade ou Mista, considerando cometido o crime tanto no local da conduta quanto no do resultado.",
                    "**Mnemônico LUTA**: sintetiza as balizas espaciais e temporais do Código Penal: Lugar do crime adota Ubiquidade e Tempo do crime adota Atividade.",
                    "**Territorialidade Temperada**: o artigo 5º do CP adota a territorialidade mitigada, aplicando a lei brasileira aos crimes cometidos no território nacional sem prejuízo de convenções e tratados.",
                    "**Território Nacional Geográfico**: abrange o espaço terrestre delimitado pelas fronteiras, as águas interiores, o mar territorial de 12 milhas náuticas e o espaço aéreo sobrejacente.",
                    "**Território por Extensão Público**: embarcações e aeronaves públicas brasileiras ou a serviço governamental são território nacional onde quer que se encontrem.",
                    "**Território por Extensão Privado**: navios e aviões mercantes privados com bandeira brasileira são território nacional quando em alto-mar ou espaço aéreo correspondente.",
                    "**Aeronaves e Embarcações Estrangeiras Privadas**: ficam sujeitas à jurisdição brasileira quando se encontrarem aportadas em porto nacional ou pousadas em solo brasileiro.",
                    "**Extraterritorialidade Incondicionada (art. 7º, I)**: a lei brasileira aplica-se obrigatoriamente sem depender de condições, mesmo que o réu seja absolvido no exterior.",
                    "**Hipóteses Incondicionadas**: crimes contra vida ou liberdade do Presidente da República, contra patrimônio de ente federativo/autarquia, contra administração pública por servidor e genocídio por nacional.",
                    "**Extraterritorialidade Condicionada (art. 7º, II)**: depende da presença cumulativa das condições do artigo 7º, § 2º (entrada no país, fato punível no exterior, crime extraditável, sem absolvição prévia).",
                    "**Hipóteses Condicionadas**: crimes que o Brasil se obrigou por tratado a reprimir, praticados por brasileiro no exterior ou a bordo de aeronaves/embarcações privadas nacionais em território estrangeiro.",
                    "**Extraterritorialidade Hipercondicionada (art. 7º, § 3º)**: crime contra brasileiro no exterior praticado por estrangeiro, exigindo requisição ministerial expressa e não extradição."
                ],
                "teoria": [
                    {
                        "statement": "O Código Penal adotou a teoria da ubiquidade para a definição do lugar do crime e a teoria do resultado para a fixação do tempo do delito.",
                        "isTrue": False,
                        "explanation": "O Código Penal adotou a ubiquidade para o lugar do crime (art. 6º) e a atividade para o tempo do delito (art. 4º), conforme o mnemônico LUTA."
                    },
                    {
                        "statement": "Embarcações particulares que ostentam bandeira brasileira são consideradas extensão do território nacional quando navegarem em águas de alto-mar.",
                        "isTrue": True,
                        "explanation": "O art. 5º, § 1º, do CP define que embarcações privadas sob pavilhão brasileiro constituem território por extensão quando em alto-mar."
                    },
                    {
                        "statement": "O crime praticado contra a liberdade de locomoção do Presidente da República submete-se à extraterritorialidade incondicionada da lei penal brasileira.",
                        "isTrue": True,
                        "explanation": "Nos termos do art. 7º, I, alínea 'a', do CP, os crimes contra a vida ou liberdade do Presidente atraem extraterritorialidade incondicionada."
                    },
                    {
                        "statement": "A punição de delito submetido à extraterritorialidade incondicionada exige como requisito essencial a entrada formal do agente infrator no território brasileiro.",
                        "isTrue": False,
                        "explanation": "Na extraterritorialidade incondicionada a lei brasileira é aplicável mesmo que o réu não ingresse no país e ainda que tenha sido absolvido no estrangeiro."
                    }
                ],
                "revisao": [
                    {
                        "statement": "O crime cometido por estrangeiro fora do Brasil contra cidadão brasileiro submete-se a condições adicionais como a ausência de pedido de extradição e requisição do Ministro da Justiça.",
                        "isTrue": True,
                        "explanation": "Trata-se da extraterritorialidade hipercondicionada do art. 7º, § 3º, que impõe cumulativamente as condições gerais e as do parágrafo terceiro."
                    },
                    {
                        "statement": "Aeronaves militares estrangeiras pousadas em aeroportos civis no solo brasileiro submetem-se imediatamente à jurisdição criminal brasileira pela soberania territorial.",
                        "isTrue": False,
                        "explanation": "Aeronaves públicas ou a serviço do governo estrangeiro ostentam imunidade territorial, mantendo a jurisdição originária de seu país de bandeira."
                    },
                    {
                        "statement": "O princípio da territorialidade adotado pelo ordenamento pátrio é absoluto, não admitindo exceções previstas em tratados internacionais de cooperação.",
                        "isTrue": False,
                        "explanation": "O Brasil adota a territorialidade temperada ou mitigada, ressalvando expressamente as convenções, regras e tratados de direito internacional."
                    },
                    {
                        "statement": "A prática de crime de genocídio cometido no exterior quando o autor for indivíduo nacional brasileiro atrai a extraterritorialidade incondicionada da legislação penal.",
                        "isTrue": True,
                        "explanation": "O art. 7º, inciso I, alínea 'd', do Código Penal inclui expressamente o delito de genocídio praticado por brasileiro no rol incondicionado."
                    }
                ],
                "pointers": [
                    {"topic": "Lugar do crime, teoria da ubiquidade e mnemônico LUTA", "pageRef": 19},
                    {"topic": "Conceito de território nacional real e ficto por extensão", "pageRef": 21},
                    {"topic": "Hipóteses de extraterritorialidade incondicionada no artigo 7º", "pageRef": 24},
                    {"topic": "Extraterritorialidade condicionada e requisitos do parágrafo segundo", "pageRef": 28},
                    {"topic": "Extraterritorialidade hipercondicionada e requisição ministerial", "pageRef": 31}
                ]
            }
        },
        {
            "id": "direito-penal/a01/s03",
            "bizu": {
                "summary": [
                    "**Pena Cumprida no Estrangeiro**: nos termos do artigo 8º do CP, a sanção executada no exterior funciona como atenuante obrigatória se diversa da sanção pátria, operando compensação temporal direta quando ambas forem de idêntica espécie.",
                    "**Cômputo e Homogeneidade**: reprimendas homogêneas (como reclusão no estrangeiro e no país) ensejam abatimento aritmético integral de dias; reprimendas heterogêneas operam como causa atenuante na dosimetria.",
                    "**Contagem de Prazo Penal (art. 10 do CP)**: inclui-se o dia do começo na contagem do prazo, computando-se os dias, meses e anos pelos períodos fixados no calendário comum.",
                    "**Fatalidade do Prazo Penal**: os prazos de direito material penal são fatais e improrrogáveis, não se postergando o seu termo final mesmo que recaia em sábado, domingo ou feriado.",
                    "**Frações Descartadas no Cálculo**: são ignoradas no cômputo executório as parcelas horárias inferiores a vinte e quatro horas nas sanções privativas, descartando-se os centavos residuais na pena de multa.",
                    "**Legislação Especial (art. 12 do CP)**: as regras gerais da Parte Geral do Código Penal aplicam-se aos fatos incriminados por leis especiais se estas não dispuserem de modo contrário.",
                    "**Sujeito Ativo do Crime**: pessoa física que pratica a conduta incriminada, admitida a responsabilização penal da pessoa jurídica exclusivamente em crimes ambientais (art. 225, § 3º, da CF).",
                    "**Sujeito Passivo Material**: titular do bem jurídico penalmente ofendido ou ameaçado de dano concreto pela ação do infrator.",
                    "**Sujeito Passivo Formal ou Constante**: o Estado é sujeito passivo formal em toda infração penal, haja vista o seu interesse originário na preservação da ordem pública.",
                    "**Imunidade Diplomática**: representantes de Estados soberanos e diplomatas credenciados gozam de imunidade absoluta de jurisdição penal perante as autoridades judiciais do Brasil.",
                    "**Imunidade Parlamentar Material**: membros do Congresso Nacional gozam de inviolabilidade jurídica plena por suas manifestações orais, pronunciamentos e votos emitidos em correlação funcional com o mandato.",
                    "**Imunidade Parlamentar Formal**: abrange a imunidade prisional (somente flagrante de crime inafiançável) e a imunidade processual de sustação de ação penal por deliberação da casa legislativa."
                ],
                "teoria": [
                    {
                        "statement": "A pena corporal restritiva de liberdade cumprida no exterior por delito também julgado no Brasil atenua a sanção brasileira caso ambas as reprimendas sejam idênticas.",
                        "isTrue": False,
                        "explanation": "Quando as penas são idênticas, opera-se o cômputo (desconto proporcional do tempo cumprido); a atenuação recai sobre penas de naturezas diversas."
                    },
                    {
                        "statement": "Na contagem do prazo de direito penal substantivo, inclui-se o primeiro dia de contagem no cômputo do lapso temporal fixado em lei.",
                        "isTrue": True,
                        "explanation": "O art. 10 do Código Penal dispõe expressamente que o dia do começo é incluído no cômputo do prazo penal de direito material."
                    },
                    {
                        "statement": "O prazo penal substantivo que vence em dia de domingo prorroga-se automaticamente até o primeiro dia útil subsequente.",
                        "isTrue": False,
                        "explanation": "Diferentemente do prazo processual, o prazo penal material é fatal e improrrogável, exaurindo-se no dia exato de calendário sem prorrogação."
                    },
                    {
                        "statement": "A ordem constitucional admite a responsabilização criminal direta da pessoa jurídica pela prática de condutas ofensivas ao meio ambiente.",
                        "isTrue": True,
                        "explanation": "O art. 225, § 3º, da Constituição consagra a responsabilidade penal da pessoa jurídica em ilícitos ambientais, regulamentada pela Lei nº 9.605/1998."
                    }
                ],
                "revisao": [
                    {
                        "statement": "No cômputo executório das sanções encarceradoras, o sistema penal manda ignorar as frações horárias residuais inferiores a um dia de custódia.",
                        "isTrue": True,
                        "explanation": "O art. 11 do Código Penal determina o descarte de frações residuais de dia nas sanções reclusivas, detentivas e alternativas."
                    },
                    {
                        "statement": "A imunidade parlamentar material impede a persecução criminal de parlamentares por opiniões e votos emitidos desde que relacionados com as funções do mandato.",
                        "isTrue": True,
                        "explanation": "O art. 53 da CF assegura a inviolabilidade penal por opiniões, palavras e votos proferidos no exercício funcional do mandato representativo."
                    },
                    {
                        "statement": "Diplomatas estrangeiros em serviço no país submetem-se integralmente à prisão em flagrante por autoridades policiais brasileiras na ocorrência de crimes inafiançáveis.",
                        "isTrue": False,
                        "explanation": "Por força da Convenção de Viena sobre Relações Diplomáticas, agentes diplomáticos detêm imunidade total à jurisdição penal do Estado receptor."
                    },
                    {
                        "statement": "O Estado figura invariavelmente como sujeito passivo formal em todas as infrações penais previstas na legislação punitiva brasileira.",
                        "isTrue": True,
                        "explanation": "O Estado é sujeito passivo formal ou genérico de qualquer ilícito penal por ser o garantidor da paz e da ordem jurídica comunitária."
                    }
                ],
                "pointers": [
                    {"topic": "Pena cumprida no estrangeiro: cômputo e atenuação no art. 8º", "pageRef": 34},
                    {"topic": "Regras de contagem de prazo material penal e fatalidade", "pageRef": 36},
                    {"topic": "Frações não computáveis de tempo e multa", "pageRef": 37},
                    {"topic": "Sujeito ativo, passivo e pessoa jurídica nos crimes ambientais", "pageRef": 39},
                    {"topic": "Imunidades diplomáticas e parlamentares na ordem jurídica", "pageRef": 41}
                ]
            }
        },
        {
            "id": "direito-penal/a01/s04",
            "bizu": {
                "summary": [
                    "**Eficácia da Sentença Estrangeira (art. 9º do CP)**: a homologação no Superior Tribunal de Justiça é indispensável para obrigar à reparação do dano ou sujeitar a medida de segurança.",
                    "**Requisitos de Homologação**: a reparação civil depende de pedido da parte interessada; a medida de segurança depende de existência de tratado de extradição ou requisição ministerial.",
                    "**Espécies de Interpretação Quanto à Origem**: autêntica (feita pela própria lei), judicial (realizada pelos magistrados nos tribunais) e doutrinária (elaborada pelos juristas).",
                    "**Espécies de Interpretação Quanto aos Meios**: gramatical ou literal, teleológica (busca a finalidade da norma), histórica (examina a gênese) e sistemática (contextualiza no ordenamento).",
                    "**Espécies de Interpretação Quanto ao Resultado**: declarativa (texto coincide com a intenção), extensiva (amplia o alcance do texto) e restritiva (restringe o alcance literal do texto).",
                    "**Interpretação Analógica**: técnica permitida em que a lei traz uma fórmula casuística seguida de fórmula genérica de encerramento (ex.: ou outro meio insidioso ou cruel).",
                    "**Analogia e Tipicidade**: analogia é forma de integração de lacuna legal, vedada in malam partem e admitida in bonam partem; interpretação analógica é método interpretativo hígido.",
                    "**Conflito Aparente de Normas**: ocorre quando uma única conduta parece enquadrar-se formalmente em dois ou mais dispositivos penais vigentes ao mesmo tempo.",
                    "**Requisitos do Conflito**: unidade de fato histórico delitivo, aparente pluralidade de normas incidentes, vigência simultânea dos preceitos e efetiva aplicabilidade de apenas uma norma.",
                    "**Princípio da Especialidade**: a norma especial contém todos os elementos da norma geral e adiciona elemento especializante, prevalecendo sobre a regra geral (*lex specialis derogat generali*).",
                    "**Princípio da Subsidiariedade**: a norma subsidiária atua como soldado de reserva, aplicando-se somente quando a infração primária de maior gravidade não se configurar.",
                    "**Princípio da Consunção ou Absorção**: o fato de maior intensidade lesiva absorve os atos preparatórios, crimes-meio, antefatos impuníveis e pós-fatos impuníveis da conduta.",
                    "**Princípio da Alternatividade**: aplica-se aos crimes de ação múltipla ou conteúdo variado em que o agente pratica vários verbos nucleares no mesmo contexto fático contra a mesma vítima."
                ],
                "teoria": [
                    {
                        "statement": "A produção de efeitos da sentença penal estrangeira no Brasil para fins de decretação de medida de segurança depende de homologação prévia pelo STJ.",
                        "isTrue": True,
                        "explanation": "O art. 9º, alínea 'b', do Código Penal estabelece que a imposição de medidas de segurança por decisão estrangeira requer homologação do Superior Tribunal de Justiça."
                    },
                    {
                        "statement": "O princípio da consunção determina a aplicação da regra subsidiária quando a conduta principal não preencher todos os requisitos da figura típica primária.",
                        "isTrue": False,
                        "explanation": "A aplicação subsidiária de reserva decorre do princípio da subsidiariedade; a consunção cuida da absorção do crime-meio pelo crime-fim."
                    },
                    {
                        "statement": "A interpretação analógica veda o emprego de cláusulas genéricas abertas, exigindo enumeração exaustiva de todas as hipóteses fáticas pelo legislador.",
                        "isTrue": False,
                        "explanation": "A interpretação analógica opera exatamente mediante emprego deliberado de uma fórmula casuística exemplificativa seguida de uma cláusula genérica de encerramento."
                    },
                    {
                        "statement": "O princípio da especialidade prescinde de ponderação sobre a gravidade das sanções, prevalecendo o preceito especial mesmo que comine sanção mais suave.",
                        "isTrue": True,
                        "explanation": "A especialidade decorre do confronto lógico-estrutural dos preceitos típicos, prevalecendo a norma especial independentemente de sua gravidade sancionatória."
                    }
                ],
                "revisao": [
                    {
                        "statement": "A homologação judicial de sentença estrangeira para a produção de efeitos reparatórios cíveis no Brasil pode ser decretada de ofício pelo magistrado instrutor.",
                        "isTrue": False,
                        "explanation": "Conforme o art. 9º, parágrafo único, 'a', do Código Penal, a homologação para reparação do dano depende exclusivamente de requerimento da parte interessada."
                    },
                    {
                        "statement": "Nos crimes plurinucleares de conteúdo variado, a execução reiterada de múltiplos verbos nucleares num único contexto contra o mesmo objeto material configura crime único.",
                        "isTrue": True,
                        "explanation": "Pelo princípio da alternatividade, a realização sucessiva de verbos do mesmo tipo penal misto alternativo caracteriza crime formal único."
                    },
                    {
                        "statement": "A analogia constitui genuína técnica de interpretação teleológica do texto normativo positivo sem inovar na ordem jurídica material.",
                        "isTrue": False,
                        "explanation": "A analogia é instrumento de integração integradora de lacunas do sistema jurídico, operando onde o texto legislado não previu disciplina expressa."
                    },
                    {
                        "statement": "O antefato impunível é absorvido pelo delito principal quando se caracterizar como meio executório necessário de passagem para a consecução da finalidade criminosa.",
                        "isTrue": True,
                        "explanation": "Pelo princípio da consunção, o fato anterior menos lesivo funcionalmente direcionado à prática do delito principal resta consumido pela conduta final."
                    }
                ],
                "pointers": [
                    {"topic": "Eficácia da sentença estrangeira e homologação pelo STJ no art. 9º", "pageRef": 42},
                    {"topic": "Métodos e espécies de interpretação da legislação penal", "pageRef": 44},
                    {"topic": "Distinção dogmática entre interpretação analógica e analogia", "pageRef": 46},
                    {"topic": "Princípios da especialidade e subsidiariedade no conflito de normas", "pageRef": 48},
                    {"topic": "Princípio da consunção, antefato impunível e alternatividade", "pageRef": 50}
                ]
            }
        }
    ]
}

# ---------------------------------------------------------
# SUMMARIES (a01)
# ---------------------------------------------------------
summaries_data = {
    "aula": "direito-penal/a01",
    "batch": "pcpe-summary-direito-penal",
    "status": "DRAFT",
    "segments": [
        {
            "id": "direito-penal/a01/s01",
            "fingerprint": get_fp("direito-penal/a01/s01"),
            "analytic": """Este segmento aborda a disciplina da aplicação da lei penal no tempo, detalhando a teoria da atividade acolhida pelo ordenamento brasileiro, o princípio da legalidade temporal, a sucessão de normas penais, o conflito intertemporal, a ultratividade das leis temporárias e excepcionais, a vedação da combinação de leis e a incidência em crimes permanentes e continuados.

### Teoria da atividade e momento do cometimento do crime
A fixação precisa do momento em que a conduta delituosa se considera consumada revela-se fundamental para definir a imputabilidade etária do agente, a legislação material aplicável e os marcos iniciais de prazos prescricionais.

A dogmática penal concebeu historicamente três vertentes sobre o tempo do crime:
- **Teoria da Atividade**: considera praticado o delito no momento exato em que o indivíduo realiza a conduta comissiva ou omissiva, independentemente de quando venha a produzir-se o resultado lesivo final.
- **Teoria do Resultado**: fixa o tempo da infração no instante da concretização do evento danoso final almejado ou culposamente ocasionado.
- **Teoria da Ubiquidade ou Mista**: considera tempo do crime tanto o instante da ação executória quanto o momento em que sobrevém o resultado naturalístico.

O Código Penal brasileiro consagrou taxativamente no artigo 4º a **Teoria da Atividade**: o ilícito penal tem-se por executado no instante exato em que o indivíduo exterioriza sua conduta volitiva comissiva ou abstentiva, sendo despiciendo o momento em que os efeitos fáticos materiais venham efetivamente a manifestar-se. Desse modo, se um indivíduo desferir disparos de arma de fogo na véspera de completar dezoito anos de idade e a vítima falecer em decorrência dos ferimentos uma semana depois, o agente responderá segundo os ditames protetivos do Estatuto da Criança e do Adolescente por ser inimputável na data da conduta.

### Conflito de leis penais no tempo e o postulado da irretroatividade
O artigo 5º, inciso XL, da Constituição Federal estabelece que a lei penal não retroagirá, salvo para beneficiar o réu. A partir dessa diretriz constitucional, a sucessão de leis criminais no tempo rege-se pelas seguintes figuras fundamentais:

| Hipótese Dogmática | Conceito Operacional | Efeito Prático na Conduta |
| --- | --- | --- |
| *Novatio Legis Incriminadora* | Norma inédita que passa a tipificar conduta antes indiferente penal | Não retroage; aplica-se apenas a fatos futuros |
| *Novatio Legis In Pejus* | Norma superveniente que agrava a situação jurídica do autor do crime | Não retroage; veda-se a aplicação a fatos passados |
| *Novatio Legis In Mellius* | Norma superveniente que suaviza o tratamento penal do delito | Retroatividade irrestrita, alcançando condenações transitadas em julgado |
| *Abolitio Criminis* | Supressão legislativa formal e material do tipo penal incriminador | Extingue a punibilidade e cessa todos os efeitos penais da sentença |

Na ocorrência de *abolitio criminis* (artigo 2º do Código Penal), cessam imediatamente a execução da sanção corporal e todos os efeitos penais secundários decorrentes da sentença condenatória, tais como o lançamento do nome no rol dos culpados e a caracterização da reincidência penal em crimes futuros. Não obstante, remanescem inalterados os efeitos de natureza civil extrapenal, subsistindo a higidez da obrigação indenizatória de reparar o prejuízo financeiro causado ao ofendido.

A aplicação da *novatio legis in mellius* a fatos acobertados por trânsito em julgado compete privativamente ao Juízo das Execuções Penais, consoante a sólida diretriz da Súmula 611 do Supremo Tribunal Federal, dispensando o ajuizamento de revisão criminal perante o tribunal originário.

### Vedação à combinação de leis penais (*Lex Tertia*)
Questão outrora tormentosa na doutrina relacionava-se à possibilidade de o órgão jurisdicional selecionar frações favoráveis de diplomas distintos para compor uma terceira norma integrada mais benéfica ao acusado.

O Superior Tribunal de Justiça pacificou essa controvérsia ao editar a **Súmula 501**, dispondo categoricamente: é cabível a aplicação retroativa da lei penal mais benigna, desde que não haja a combinação de dispositivos com a legislação revogada para a formação de uma terceira norma mista (*lex tertia*). A atividade de mesclar trechos isolados usurparia a competência legislativa privativa reservada ao Parlamento, violando o princípio da separação dos poderes.

### Leis excepcionais e leis temporárias (*Leis Intermitentes*)
O artigo 3º do Código Penal estabelece tratamento singular para normas editadas com vigência transitória delimitada:
- **Leis Temporárias**: trazem em seu próprio texto o dia de termo final de sua vigência jurídica (ex.: diploma de restrições sanitárias válido expressamente até determinada data).
- **Leis Excepcionais**: vinculam sua vigência à manutenção de um cenário extraordinário e transitório de anormalidade social (ex.: calamidades públicas, epidemias, conflitos armados).

Essas espécies normativas são caracterizadas pela autorrevogabilidade e pela **ultratividade gravosa obrigatória**. Os fatos delituosos cometidos durante o período de sua vigência temporal continuarão sendo punidos com base em suas penas severas mesmo após a sua cessação natural, impedindo que os infratores procrastinem a instrução processual na expectativa de alcançar impunidade pela extinção da vigência legal.

### Crimes permanentes, continuados e a Súmula 711 do STF
Nos crimes permanentes (cuja consumação se prolonga no tempo por vontade deliberada do agente, a exemplo do sequestro) e nos crimes continuados (série articulada de delitos da mesma espécie cometidos sob condições semelhantes de tempo, lugar e maneira de execução), a conduta renova-se dia a dia.

Diante dessa peculiar dinâmica executória, o Supremo Tribunal Federal firmou a **Súmula 711**: o preceito sancionatório novel mais gravoso incide nos ilícitos de natureza protraída ou continuada desde que o seu início formal de vigência preceda a consumação do elo de continuidade ou a cessação do estado de permanência. Se durante o cativeiro de um sequestro entrar em vigor alteração legislativa elevando a pena abstrata cominada, a novel sanção mais severa incidirá integralmente sobre o agente porque o delito permanecia em plena execução sob a vigência do novo preceito.

### Para fixar
- O Código Penal acolheu a Teoria da Atividade para a definição do tempo do crime no artigo 4º.
- A irretroatividade penal impede a retroação da lei mais grave (*novatio legis in pejus*).
- A lei mais branda (*novatio legis in mellius*) retroage irrestritamente, alcançando fatos transitados em julgado.
- A *abolitio criminis* cessa os efeitos penais principais e secundários, preservando os reflexos civis reparatórios.
- A Súmula 501 do STJ veda ao magistrado combinar leis sucessivas para criar norma híbrida (*lex tertia*).
- As leis temporárias e excepcionais gozam de ultratividade legal, punindo condutas ocorridas sob sua vigência.
- A competência para aplicar a lei mais favorável após a coisa julgada é do Juízo da Execução (Súmula 611 do STF).
- A Súmula 711 do STF determina a incidência da lei mais severa se a sua vigência anteceder a cessação da permanência.""",
            "synthetic": [
                "**Teoria da Atividade (art. 4º)**: considera praticado o crime no momento exato da conduta ativa ou omissiva, independentemente de quando venha a produzir-se o resultado danoso.",
                "**Irretroatividade da Lex Gravior**: a norma criminal superveniente mais gravosa não retroage sob hipótese alguma, disciplinando apenas condutas futuras à publicação.",
                "**Retroatividade da Lex Mitior**: o diploma mais favorável incide retroativamente sobre todos os fatos pretéritos, alcançando processos com condenação transitada em julgado.",
                "**Abolitio Criminis**: extingue a punibilidade e afasta todos os efeitos penais primários e secundários da condenação, conservando intactos unicamente os efeitos de reparação civil.",
                "**Súmula 501 do STJ**: veda peremptoriamente a combinação judicial de normas sucessivas com a finalidade de conceber um terceiro preceito híbrido inexistente no ordenamento.",
                "**Leis Intermitentes (art. 3º)**: as normas penais temporárias e excepcionais são ultrativas, sancionando os delitos praticados durante a vigência mesmo após a sua extinção.",
                "**Súmula 711 do STF**: aplica-se a legislação penal posterior mais severa ao crime permanente ou continuado se a sua vigência anteceder o término da permanência delitiva.",
                "**Competência Executória (Súmula 611 STF)**: transitada em julgado a sentença condenatória, a atribuição para aplicar preceito legal superveniente mais benigno recai sobre a Execução."
            ]
        },
        {
            "id": "direito-penal/a01/s02",
            "fingerprint": get_fp("direito-penal/a01/s02"),
            "analytic": """Este segmento analisa a disciplina jurídica da aplicação da lei penal no espaço, abrangendo o lugar do crime sob a ótica da teoria da ubiquidade, a delimitação de território nacional por extensão, as prerrogativas de embarcações e aeronaves, bem como o sistema de extraterritorialidade incondicionada, condicionada e hipercondicionada.

### Lugar do crime e a Teoria da Ubiquidade
Diferentemente do critério adotado para o momento temporal da conduta delituosa, o artigo 6º do Código Penal consagrou taxativamente a **Teoria da Ubiquidade** (ou Mista) para a definição do lugar do crime: o local da infração é determinado tanto pela localidade geográfica em que se desenvolveu qualquer fração da execução comissiva ou abstentiva quanto pelo território em que o evento lesivo se consumou ou almejava consumar-se.

Essa sistemática evita vácuos de jurisdição nos chamados crimes à distância ou de espaço máximo, que transpassam fronteiras de diferentes Estados soberanos. A distinção clássica dos postulados é memorizada pelo célebre mnemônico **LUTA**:
- **Lu**gar do crime adota a **U**biquidade (artigo 6º do CP);
- **T**empo do crime adota a **A**tividade (artigo 4º do CP).

### Princípio da territorialidade mitigada e território fictício
O artigo 5º do Código Penal estabelece que se aplica a lei brasileira, salvaguardadas as disposições pactuadas em diplomas diplomáticos e tratados internacionais ratificados pelo país, a qualquer ilícito cometido no território nacional. O Brasil adota a **territorialidade temperada ou mitigada**, reconhecendo imunidades e prerrogativas diplomáticas recepcionadas em acordos multilaterais.

O território geográfico nacional abrange a faixa terrestre continental e insular, as águas interiores delimitadas, o mar territorial de doze milhas náuticas a partir da linha de base costeira e a coluna de espaço aéreo correspondente a essa projeção vertical.

Ademais, o direito penal consagra a extensão jurídica ficta do território nacional sobre meios de transporte:
- **Aeronaves e Embarcações Públicas**: quando brasileiras ou a serviço do governo nacional, consideram-se extensão de território pátrio onde quer que se encontrem (inclusive atracadas em porto ou sobrevoando território estrangeiro).
- **Aeronaves e Embarcações Privadas Brasileiras**: configuram território nacional por extensão quando se encontrarem navegando em alto-mar ou sobrevoando o espaço aéreo internacional desprovido de jurisdição estrangeira.
- **Embarcações Privadas Estrangeiras**: que navegam em águas marítimas territoriais brasileiras ou se encontram ancoradas em nossos portos submetem-se imediatamente à jurisdição da lei penal do Brasil.

### Regime da extraterritorialidade incondicionada (art. 7º, I)
A extraterritorialidade consubstancia a aplicação coativa da legislação brasileira a infrações perpetradas inteiramente fora do território nacional.

No artigo 7º, inciso I, do Código Penal, estão elencadas as hipóteses de **extraterritorialidade incondicionada**, nas quais a lei nacional incide de forma mandatória, ainda que o agente venha a ser absolvido ou tenha cumprido pena no país estrangeiro:
1. Crimes perpetrados contra a vida ou a liberdade do Presidente da República (fundamentado no princípio da defesa real);
2. Crimes contra o patrimônio ou a fé pública da União, estados, Distrito Federal, municípios, empresas públicas, sociedades de economia mista e autarquias (princípio da defesa ou proteção);
3. Crimes contra a administração pública nacional, praticados por quem está a seu serviço oficial no exterior (princípio da proteção funcional);
4. Delito de genocídio, quando o autor for brasileiro ou pessoa domiciliada no território nacional (princípio da universalidade ou da nacionalidade ativa).

Nas hipóteses incondicionadas, o agente é processado e julgado conforme a lei penal brasileira ainda que o fato não seja considerado infração penal pela lei do país onde foi consumado.

### Extraterritorialidade condicionada e hipercondicionada
As hipóteses do artigo 7º, inciso II, configuram a **extraterritorialidade condicionada**, exigindo para sua persecução o adimplemento simultâneo de cinco condições cumulativas fixadas no § 2º:
- Crimes que, por força de tratados multilaterais, o Brasil se comprometeu a reprimir (princípio da justiça universal);
- Crimes praticados por cidadão brasileiro fora do território pátrio (princípio da nacionalidade ativa);
- Crimes cometidos a bordo de aeronaves ou embarcações mercantes brasileiras quando em país estrangeiro e aí não tenham sido processados.

As condições cumulativas obrigatórias são: ingresso físico do acusado no território brasileiro; constituir a conduta fato punível também pela lei alienígena do país de ocorrência; enquadrar-se entre as hipóteses autorizadoras de extradição segundo a ordem nacional; inexistência de veredito absolutório nas cortes forâneas ou de exaurimento integral da custódia prisional no exterior; e inocorrência de perdão ou de causa extintiva de punibilidade lá fora.

Por fim, o artigo 7º, § 3º, introduz a **extraterritorialidade hipercondicionada**: cuida do crime praticado por estrangeiro contra brasileiro fora do país. Além de satisfazer todas as condições do § 2º, impõe dois requisitos suplementares: não ter sido pedida ou ter sido negada a extradição do agente, e haver requisição formal e expressa do Ministro da Justiça.

### Para fixar
- O Código Penal acolheu a Teoria da Ubiquidade para a fixação do lugar do crime no artigo 6º.
- O mnemônico LUTA sintetiza Lugar/Ubiquidade e Tempo/Atividade na legislação repressiva nacional.
- O Brasil adota a territorialidade mitigada, ressalvando as normas e tratados de direito internacional.
- Embarcações públicas brasileiras são extensão de território nacional onde quer que estejam situadas.
- Embarcações particulares nacionais são território fictício quando em alto-mar ou espaço aéreo internacional.
- A extraterritorialidade incondicionada (art. 7º, I) incide mesmo que o agente seja absolvido no exterior.
- A extraterritorialidade condicionada (art. 7º, II) depende do preenchimento cumulativo dos requisitos do § 2º.
- O crime contra brasileiro no exterior praticado por estrangeiro exige expressa requisição do Ministro da Justiça.""",
            "synthetic": [
                "**Teoria da Ubiquidade (art. 6º)**: considera praticada a infração tanto no local da conduta comissiva ou omissiva quanto no local em que sobreveio ou deveria sobrevir o resultado.",
                "**Mnemônico LUTA**: resume com clareza as diretrizes espaciais e temporais ao fixar Lugar com Ubiquidade e Tempo com Atividade no Código Penal.",
                "**Territorialidade Mitigada (art. 5º)**: a lei pátria aplica-se a toda infração cometida no território nacional, admitindo ressalvas fixadas em convenções e regras internacionais.",
                "**Embarcações Públicas**: navios e aviões governamentais ou sob serviço público brasileiro configuram extensão do território onde quer que se encontrem ancorados.",
                "**Embarcações Privadas**: meios de transporte mercantes com pavilhão brasileiro constituem território fictício apenas quando em trânsito por alto-mar desprovido de jurisdição.",
                "**Extraterritorialidade Incondicionada**: abrange crimes contra a vida do Presidente, patrimônio público, administração no exterior e genocídio por cidadão brasileiro.",
                "**Condições do Artigo 7º, § 2º**: exigem cumulativamente ingresso em território nacional, dupla incriminação, crime extraditável e ausência de absolvição prévia no estrangeiro.",
                "**Extraterritorialidade Hipercondicionada**: incide em agressões contra brasileiros no exterior cometidas por estrangeiros, exigindo não extradição e requisição ministerial."
            ]
        },
        {
            "id": "direito-penal/a01/s03",
            "fingerprint": get_fp("direito-penal/a01/s03"),
            "analytic": """Este segmento aborda a disciplina da aplicação pessoal da lei penal, examinando os sujeitos ativo e passivo da infração, os efeitos da pena cumprida no exterior, o regramento estrito de contagem dos prazos penais de direito substantivo, o descarte das frações não computáveis e o regime jurídico das imunidades diplomáticas e parlamentares.

### Sujeitos ativo e passivo na relação jurídico-penal
O cometimento de toda conduta punível instaura uma relação trilateral entre o infrator, o titular do interesse agredido e o poder soberano estatal:
- **Sujeito Ativo**: indivíduo imputável que pratica o comportamento moldado pelo preceito primário do tipo penal incriminador. No ordenamento jurídico brasileiro, a responsabilidade penal recai ordinariamente sobre pessoas físicas. Contudo, em consagração ao comando do artigo 225, § 3º, da Carta Magna, admite-se a responsabilização criminal direta de pessoas jurídicas exclusivamente em ilícitos ambientais regulados pela Lei nº 9.605/1998, sem exigência de dupla imputação simultânea de dirigentes conforme assentado pelo STF e STJ.
- **Sujeito Passivo Material**: titular do bem jurídico penal individual tutelado que suporta o dano ou ameaça concreta provocada pelo crime (ex.: o proprietário no furto, a vítima no homicídio).
- **Sujeito Passivo Formal ou Constante**: o Estado ostenta invariavelmente a condição de sujeito passivo formal em toda e qualquer infração penal, haja vista sua atribuição de resguardar a incolumidade comunitária.

### Pena cumprida no estrangeiro (art. 8º do CP)
O artigo 8º do Código Penal regulamenta os desdobramentos sancionatórios decorrentes de julgamentos transnacionais pelo mesmo fato histórico delitivo, operando a harmonização entre a soberania nacional e a vedação ao *bis in idem*:
- **Penas Idênticas**: a reprimenda cumprida no exterior é integralmente computada (descontada) da pena imposta pela jurisdição penal do Brasil. Se o indivíduo cumpriu dois anos de prisão no país estrangeiro e for sentenciado a seis anos de reclusão no Brasil, cumprirá os quatro anos remanescentes.
- **Penas Diversas**: a reprimenda suportada no exterior atenua a sanção fixada pelo magistrado brasileiro, funcionando como causa obrigatória de diminuição na dosimetria sentencial.

### Contagem de prazo penal substantivo e frações descartáveis
O artigo 10 do Código Penal disciplina a contagem dos prazos de direito material penal (como os prazos de prescrição, decadência do direito de queixa e cumprimento de pena corporal):
- **Inclusão do Dia Inicial**: inclui-se o dia do começo no cômputo da contagem do prazo, computando-se os dias, meses e anos de acordo com o calendário civil comum.
- **Fatalidade e Improrrogabilidade**: diferentemente das normas de direito processual penal (que excluem o primeiro dia e prorrogam o termo final que coincide com fim de semana ou feriado), os prazos penais materiais são fatais e contínuos. O prazo penal extingue-se impreterivelmente na data de seu vencimento, sem prorrogação para o primeiro dia útil subsequente.

O artigo 11 do Código Penal fixa o tratamento aplicável às frações numéricas mínimas: são desconsideradas no cálculo prisional de penas reclusivas ou alternativas as porções inferiores a vinte e quatro horas inteiras; do mesmo modo, na pena pecuniária de multa, ignoram-se sumariamente os centavos residuais.

O artigo 12 do diploma penal enuncia o princípio da subsidiariedade da Parte Geral, estabelecendo que suas regras gerais incidem subsidiariamente sobre toda legislação penal extravagante sempre que a norma especial não regular expressamente a matéria em sentido oposto.

### Imunidades diplomáticas e imunidades parlamentares
A igualdade perante a lei comporta prerrogativas funcionais estabelecidas para salvaguardar a estabilidade das funções institucionais:
- **Imunidade Diplomática**: decorrente da Convenção de Viena de 1961, assegura imunidade de jurisdição penal absoluta e isenção de persecução penal interna para embaixadores, diplomatas e familiares dependentes em exercício no Brasil, respondendo apenas perante a jurisdição do seu país de origem.
- **Imunidade Parlamentar Material (ou Inviolabilidade)**: o artigo 53 da CF assegura que membros do parlamento federal gozam de imunidade substantiva que afasta responsabilização jurídica por posicionamentos discursivos e manifestações volitivas vinculadas ao exercício legislativo.
- **Imunidade Parlamentar Formal (Processual)**: parlamentares federais não podem ser presos desde a expedição do diploma, salvo em flagrante de crime inafiançável, cabendo à respectiva casa legislativa deliberar sobre a manutenção da custódia e eventual sustação do andamento da ação penal.

### Para fixar
- Pessoas jurídicas respondem penalmente no Brasil de forma exclusiva nos crimes ambientais (art. 225, § 3º, da CF).
- O Estado figura como sujeito passivo formal constante de todas as infrações penais descritas no ordenamento.
- A pena cumprida no exterior é computada quando homogênea ou atenua a pena brasileira quando diversa (art. 8º).
- O prazo penal material inclui o dia do início em sua contagem e é marcado pela fatalidade improrrogável.
- Desprezam-se as frações de dia nas penas privativas de liberdade e as frações de real na pena de multa (art. 11).
- As regras da Parte Geral do Código Penal aplicam-se subsidiariamente aos fatos previstos em leis especiais (art. 12).
- Diplomatas credenciados detêm imunidade total perante a jurisdição penal do Estado brasileiro recebedor.
- A imunidade parlamentar material acoberta votos e opiniões que guardem pertinência funcional com o mandato cívico.""",
            "synthetic": [
                "**Pessoa Jurídica Infratora**: admite-se a responsabilização criminal direta de entidades coletivas exclusivamente nas infrações contra o meio ambiente (art. 225, § 3º, da CF).",
                "**Sujeitos Passivos**: o sujeito passivo material consubstancia o titular imediato do bem agredido, enquanto o Estado figura como sujeito passivo formal em todo delito.",
                "**Pena no Exterior (art. 8º)**: a sanção cumprida fora do país opera desconto direto quando homogênea à condenação brasileira ou atenua a sanção imposta quando heterogênea.",
                "**Prazo Material Penal (art. 10)**: inclui obrigatoriamente o dia inicial no cômputo e caracteriza-se pela fatalidade inadiável sem prorrogação para dias úteis.",
                "**Frações Descartáveis (art. 11)**: descartam-se as frações de dia nas penas privativas de liberdade e restritivas de direitos, bem como as frações de real no cálculo da multa penal.",
                "**Eficácia Subsidiária (art. 12)**: as regras gerais estruturantes da Parte Geral do Código Penal irradiam sobre leis especiais que não disponham de modo contrário.",
                "**Imunidade Diplomática Absoluta**: afasta a incidência coativa da jurisdição penal do Estado receptor sobre agentes diplomáticos e membros oficiais de representações estrangeiras.",
                "**Imunidade Parlamentar**: protege opiniões, palavras e votos com vínculo funcional ao mandato, além de limitar prisões cautelares a flagrantes de crimes inafiançáveis."
            ]
        },
        {
            "id": "direito-penal/a01/s04",
            "fingerprint": get_fp("direito-penal/a01/s04"),
            "analytic": """Este segmento analisa a eficácia da sentença penal estrangeira no território brasileiro, as diretrizes hermenêuticas e metodológicas de interpretação e integração da norma penal, e os princípios balizadores do conflito aparente de normas penais.

### Eficácia da sentença estrangeira no Brasil (art. 9º do CP)
A soberania estatal veda que decisões criminais proferidas por cortes alienígenas produzam imediatos efeitos executórios diretos no território nacional. Consoante o artigo 9º do Código Penal, a sentença condenatória penal emanada de tribunal estrangeiro somente produz efeitos no Brasil em duas hipóteses expressas e condicionadas:
1. Para obrigar o condenado à reparação do dano civil, a restituições materiais e a outros efeitos secundários civis;
2. Para sujeitar o indivíduo à imposição de medida de segurança pessoal.

Para a produção desses efeitos, é indeclinável a sua **homologação formal pelo Superior Tribunal de Justiça** (artigo 105, inciso I, alínea 'i', da Constituição Federal). Quanto à legitimidade para provocar a deliberação homologatória:
- A reparação do dano e efeitos civis depende de pedido expresso formulado pela parte interessada;
- A imposição de medida de segurança depende da existência de tratado bilateral de extradição ou, na sua ausência, de requisição formal do Ministro da Justiça.

### Métodos de interpretação e integração da lei penal
A hermenêutica penal busca desvelar o conteúdo substantivo e o alcance protetivo dos tipos incriminadores:
- **Quanto à Origem**: autêntica (editada pela própria lei ou exposição de motivos oficial vinculante), judicial (construída pelos juízos na jurisprudência contenciosa) ou doutrinária (formulada pelos comentaristas e teóricos do direito).
- **Quanto aos Meios**: gramatical ou filológica (atenta à literalidade do vernáculo), teleológica (busca a finalidade teleológica e a razão de ser da norma protetiva), histórica (examina a gênese da norma) ou sistemática (harmoniza o preceito no ordenamento jurídico geral).
- **Quanto ao Resultado**: declarativa (a letra do texto coincide perfeitamente com a intenção do legislador), extensiva (amplia o alcance literal da lei para cobrir a real intenção normativa) ou restritiva (restringe a fórmula literal que extrapolou os fins pretendidos).

Cumpre não confundir a interpretação analógica com o instituto integrativo da analogia:
- **Interpretação Analógica**: método interpretativo plenamente lícito em que o preceito traz uma fórmula casuística exemplificativa seguida de uma cláusula genérica de encerramento (como no artigo 121, § 2º, I: mediante paga, promessa de recompensa ou outro motivo torpe).
- **Analogia**: autêntico mecanismo de integração de lacunas normativas involuntárias, sendo peremptoriamente vedada *in malam partem* e admitida *in bonam partem*.

### Conflito aparente de normas penais e princípios resolutivos
Ocorre o conflito aparente de normas penais quando um único fato humano praticado no mundo real subsume-se formalmente a dois ou mais dispositivos legais vigentes e aplicáveis. Para a caracterização do conflito aparente, exige-se unidade de fato histórico, aparente multiplicidade de regras vigentes e a identificação de que apenas um preceito é verdadeiramente aplicável.

A doutrina penal consagrou quatro postulados para a solução do conflito aparente:

| Princípio Hermenêutico | Brocardo Latino | Diretriz de Aplicação Prática |
| --- | --- | --- |
| **Especialidade** | *Lex specialis derogat generali* | A norma especial traz todos os dados da geral e agrega elemento especializante, prevalecendo sobre ela |
| **Subsidiariedade** | *Lex primaria derogat subsidiariae* | A norma subsidiária funciona como soldado de reserva, incidindo apenas se a primária for afastada |
| **Consunção (Absorção)** | *Lex consumens derogat consumptae* | O fato mais grave absorve o fato menos grave que atua como meio ou fase preparatória necessária |
| **Alternatividade** | - | Tipos mistos alternativos de múltiplos verbos: praticar vários verbos no mesmo contexto gera crime único |

No princípio da consunção, o delito-fim de maior gravidade lesiva consome os atos preparatórios e executórios (*antefato impunível*), os crimes-meio instrumentais e as condutas exaurientes sem novo dano autônomo (*pós-fato impunível*). A Súmula 17 do Superior Tribunal de Justiça materializa essa diretriz ao fixar que o falso se exaure no estelionato sem mais potencialidade lesiva, sendo por este absorvido.

### Para fixar
- A sentença penal estrangeira requer homologação no STJ para produzir reparação civil ou medida de segurança.
- A reparação civil decorrente de sentença estrangeira depende de provocação expressa da parte interessada.
- A medida de segurança estrangeira depende de tratado de extradição ou de requisição do Ministro da Justiça.
- A interpretação autêntica decorre do próprio legislador e vincula compulsoriamente os aplicadores da norma.
- A interpretação analógica emprega cláusula genérica após enumeração e consubstancia método interpretativo válido.
- O princípio da especialidade faz prevalecer a regra com elementos específicos sobre a norma de caráter geral.
- A subsidiariedade opera como mecanismo de reserva punitiva diante da inaplicabilidade da norma primária.
- A consunção determina a absorção do crime-meio instrumental pelo crime-fim consumado mais lesivo.""",
            "synthetic": [
                "**Sentença Estrangeira (art. 9º)**: produz efeitos no Brasil exclusivamente para obrigar à reparação do dano civil e para a imposição de medida de segurança.",
                "**Homologação no STJ**: compete privativamente ao Superior Tribunal de Justiça homologar provimentos penais estrangeiros dependendo de provocação da parte ou do Ministério da Justiça.",
                "**Espécies de Interpretação**: classificam-se quanto à fonte em autêntica, judicial e doutrinária, e quanto ao resultado em declarativa, restritiva e extensiva.",
                "**Interpretação Analógica**: técnica autorizada em que o texto normativo adota enumeração casuística seguida de cláusula de encerramento genérica flexível.",
                "**Princípio da Especialidade**: a norma especial agrega elemento especializante e afasta o preceito genérico sem perquirir sobre o patamar da reprimenda.",
                "**Princípio da Subsidiariedade**: a norma de reserva aplica-se de maneira condicionada apenas na ausência de tipificação pela regra principal preponderante.",
                "**Princípio da Consunção**: o delito principal mais danoso consome os crimes-meio antecedentes, os antefatos preparatórios e os pós-fatos impuníveis desprovidos de novo dano.",
                "**Princípio da Alternatividade**: nos crimes de ação múltipla ou conteúdo variado, a execução sucessiva de núcleos típicos no mesmo cenário enseja crime único."
            ]
        }
    ]
}

# Write files
with open(ITEMS_FILE, "w", encoding="utf-8") as f:
    json.dump(items_data, f, ensure_ascii=False, indent=2)
print(f"Wrote {ITEMS_FILE}")

with open(SUMMARIES_FILE, "w", encoding="utf-8") as f:
    json.dump(summaries_data, f, ensure_ascii=False, indent=2)
print(f"Wrote {SUMMARIES_FILE}")
