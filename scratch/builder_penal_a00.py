# -*- coding: utf-8 -*-
"""Builder for direito-penal a00 (items and summaries)."""
import json
import os
import subprocess
import sys

ITEMS_FILE = "content/items/direito-penal/a00.json"
SUMMARIES_FILE = "content/summaries/direito-penal/a00.json"

os.makedirs(os.path.dirname(ITEMS_FILE), exist_ok=True)
os.makedirs(os.path.dirname(SUMMARIES_FILE), exist_ok=True)

# ---------------------------------------------------------
# BIZU ITEMS (a00)
# ---------------------------------------------------------
items_data = {
    "aula": "direito-penal/a00",
    "batch": "pcpe-bizu-direito-penal",
    "status": "DRAFT",
    "stage": "bizu",
    "segments": [
        {
            "id": "direito-penal/a00/s01",
            "bizu": {
                "summary": [
                    "**Princípio da Legalidade**: consagrado no artigo 5º, inciso XXXIX, da CF e no artigo 1º do CP, impõe que não há infração penal sem lei anterior que a defina, nem sanção sem prévia cominação legal.",
                    "**Reserva Legal Estrita**: exige que somente lei ordinária ou complementar em sentido formal e estrito proveniente do Parlamento possa cominar sanções privativas ou tipificar crimes.",
                    "**Anterioridade da Lei Penal**: veda a retroatividade da legislação criminal para alcançar condutas pretéritas, ressalvada unicamente a hipótese de norma benéfica ao réu.",
                    "**Vedação à Analogia In Malam Partem**: é proibido criar tipos incriminadores ou agravar sanções mediante integração analógica desfavorável ao réu.",
                    "**Analogia In Bonam Partem**: permitida de forma pacífica na dogmática nacional para favorecer a defesa em situações de lacuna involuntária da legislação.",
                    "**Taxatividade ou Determinação**: exige preceitos primários dotados de clareza conceitual e contornos nítidos, repelindo tipos incriminadores abertos ou demasiadamente ambíguos.",
                    "**Individualização da Pena**: desdobra-se nos estágios legislativo de cominação abstrata, judicial de dosimetria individual e executório de cumprimento penitenciário gradativo.",
                    "**Limitação das Penas**: veda a imposição de penas de morte fora do contexto de guerra formal, perpétuas, de trabalhos forçados, de banimento ou de perfil cruel.",
                    "**Intranscendência da Pena**: a obrigação penal jamais passará da pessoa do condenado, podendo a reparação do dano e o confisco atingir herdeiros até as forças da herança.",
                    "**Presunção de Inocência**: impede considerar o cidadão culpado antes do trânsito em julgado definitivo de sentença condenatória irrecorrível.",
                    "**Regra Probatória**: transfere com exclusividade o ônus probatório da culpabilidade ao polo acusador, vigorando a máxima in dubio pro reo em caso de dúvida fática relevante.",
                    "**Tema 1068 do STF**: soberania dos veredictos do Tribunal do Júri autoriza o cumprimento imediato da sanção privativa de liberdade imposta pelo Conselho de Sentença independentemente do quantum."
                ],
                "teoria": [
                    {
                        "statement": "O princípio da reserva legal admite a criação originária de tipos penais incriminadores por meio de medida provisória diante da relevância da matéria.",
                        "isTrue": False,
                        "explanation": "A criação de crimes e cominação de sanções submete-se à reserva de lei em sentido estrito, sendo vedada a via da medida provisória em matéria penal incriminadora."
                    },
                    {
                        "statement": "A garantia da intranscendência da sanção penal impede que a obrigação civil de reparação do dano seja estendida aos sucessores do réu falecido.",
                        "isTrue": False,
                        "explanation": "A pena corporal é estritamente pessoal, porém a reparação civil e a decretação de perda de bens podem alcançar sucessores até o limite do patrimônio transferido."
                    },
                    {
                        "statement": "O postulado da taxatividade impõe ao legislador a redação precisa das figuras típicas para conferir previsibilidade e interditar punições arbitrárias.",
                        "isTrue": True,
                        "explanation": "A taxatividade concretiza a legalidade ao exigir descrição detalhada e inequívoca das ações humanas sujeitas à repressão criminal."
                    },
                    {
                        "statement": "A presunção de não culpabilidade atua no processo penal como critério distribuidor do encargo probatório, impondo absolvição caso remanesça incerteza instrutória insuperável.",
                        "isTrue": True,
                        "explanation": "Por força do postulado do estado de inocência, o encargo probatório recai todo sobre o órgão de acusação, resolvendo-se a dúvida fática em prol da defesa."
                    }
                ],
                "revisao": [
                    {
                        "statement": "A analogia integrativa pode ser validamente manejada na esfera penal desde que atue exclusivamente em benefício da situação jurídica do imputado.",
                        "isTrue": True,
                        "explanation": "Admite-se na seara dogmática penal a integração analógica in bonam partem para afastar punibilidade ou beneficiar o acusado em caso de lacuna legal."
                    },
                    {
                        "statement": "O postulado da anterioridade veda que norma penal posterior mais branda retroaja para beneficiar agente já condenado com decisão transitada em julgado.",
                        "isTrue": False,
                        "explanation": "A novatio legis in mellius possui eficácia retroativa irrestrita, alcançando inclusive processos findos com trânsito em julgado formado."
                    },
                    {
                        "statement": "O Supremo Tribunal Federal firmou tese de repercussão geral admitindo a execução imediata da pena corporal imposta pelo corpo de jurados do Tribunal do Júri.",
                        "isTrue": True,
                        "explanation": "No julgamento do Tema 1068, o STF assentou que a soberania dos veredictos autoriza a imediata prisão do réu condenado em plenário do júri."
                    },
                    {
                        "statement": "A Constituição Federal autoriza a imposição perpétua de sanções restritivas de liberdade nas hipóteses de infrações praticadas mediante extrema violência física.",
                        "isTrue": False,
                        "explanation": "A Carta da República interdita expressamente qualquer modalidade de reprimenda de caráter perpétuo em seu artigo 5º, inciso XLVII."
                    }
                ],
                "pointers": [
                    {"topic": "Legalidade, reserva legal e anterioridade da norma penal", "pageRef": 3},
                    {"topic": "Vedação à analogia in malam partem e taxatividade dos tipos", "pageRef": 7},
                    {"topic": "Individualização da pena e limitação das espécies de sanções", "pageRef": 10},
                    {"topic": "Presunção de inocência e regra de julgamento in dubio pro reo", "pageRef": 14},
                    {"topic": "Tema 1068 do STF e execução provisória no Tribunal do Júri", "pageRef": 16}
                ]
            }
        },
        {
            "id": "direito-penal/a00/s02",
            "bizu": {
                "summary": [
                    "**Princípio da Ofensividade**: exige lesão efetiva ou perigo concreto de dano ao bem jurídico tutelado para a configuração de infração penal punível.",
                    "**Princípio da Alteridade**: veda a incriminação de comportamentos meramente internos ou de autolesão que não extravasem a esfera do próprio praticante.",
                    "**Princípio da Intervenção Mínima**: o ramo penal atua como ultima ratio do sistema protetivo social, intervindo exclusivamente na falha dos demais ramos do direito.",
                    "**Subsidiariedade Penal**: o direito repressivo opera como retaguarda sancionadora subsidiária, aplicável apenas quando sanções civis e administrativas forem insuficientes.",
                    "**Fragmentariedade Penal**: o ordenamento penal seleciona tão somente uma fração dos bens mais valiosos perante os ataques mais intoleráveis e agressivos.",
                    "**Princípio da Adequação Social**: condutas historicamente aceitas pela sociedade não devem ser punidas, ressalvado que o costume não revoga preceito penal formal.",
                    "**Súmula 502 do STJ**: a venda clandestina de mídias piratas não é acobertada pela adequação social, subsistindo a tipicidade do artigo 184 do Código Penal.",
                    "**Princípio do Ne Bis In Idem**: impede que um mesmo indivíduo suporte dupla persecução penal ou múltipla exasperação punitiva ancorada no mesmo fato histórico.",
                    "**Princípio da Proporcionalidade**: desdobra-se na proibição do excesso punitivo estatal e na proibição da proteção deficiente aos bens jurídicos fundamentais.",
                    "**Princípio da Confiança**: cada integrante da coletividade pode legitimamente esperar que os demais participantes conduzam suas atividades segundo as normas vigentes.",
                    "**Requisitos da Insignificância (STF)**: mínima ofensividade da conduta, ausência de periculosidade social, reduzidíssimo grau de reprovabilidade e inexpressividade da lesão.",
                    "**Súmula 589 do STJ**: é peremptoriamente vedada a aplicação do princípio da insignificância na violência doméstica ou familiar praticada contra a mulher."
                ],
                "teoria": [
                    {
                        "statement": "O princípio da alteridade obsta que o legislador comine sanções penais a comportamentos de autolesão que não causem prejuízo a interesses de terceiros.",
                        "isTrue": True,
                        "explanation": "A alteridade impede a persecução criminal de condutas que lesionem exclusivamente o próprio indivíduo, a exemplo da tentativa de suicídio."
                    },
                    {
                        "statement": "A tolerância costumeira e a ampla aceitação social de uma conduta típica são suficientes para promover a revogação tácita de preceito legal incriminador.",
                        "isTrue": False,
                        "explanation": "O costume atua como vetor de hermenêutica, porém somente outra lei em sentido estrito tem o condão de revogar norma penal vigente no país."
                    },
                    {
                        "statement": "O princípio da insignificância afasta a tipicidade material da conduta quando preenchidos os vetores de inexpressividade lesiva estabelecidos pela jurisprudência.",
                        "isTrue": True,
                        "explanation": "A bagatela própria opera a exclusão da tipicidade em seu aspecto material, subsistindo mera tipicidade formal desprovida de relevância penal."
                    },
                    {
                        "statement": "A jurisprudência do Superior Tribunal de Justiça autoriza o reconhecimento da insignificância em contravenções de vias de fato praticadas no ambiente familiar.",
                        "isTrue": False,
                        "explanation": "Conforme o enunciado da Súmula 589 do STJ, veda-se a insignificância em crimes e contravenções cometidos contra a mulher em âmbito doméstico."
                    }
                ],
                "revisao": [
                    {
                        "statement": "O postulado da subsidiariedade determina que a tutela penal seja mobilizada antes dos instrumentos administrativos por possuir maior poder intimidatório.",
                        "isTrue": False,
                        "explanation": "O direito penal é regido pela subsidiariedade, devendo intervir apenas de forma secundária após a constatação de ineficácia dos demais ramos."
                    },
                    {
                        "statement": "A jurisprudência sumulada do STJ afasta a incidência do princípio da adequação social sobre a comercialização não autorizada de mídias gravadas piratas.",
                        "isTrue": True,
                        "explanation": "A Súmula 502 do STJ fixou expressamente que expor à venda CDs e DVDs piratas configura fato típico pelo artigo 184, § 2º, do CP."
                    },
                    {
                        "statement": "O princípio da proporcionalidade impõe limites ao poder estatal tanto para evitar castigos excessivos quanto para coibir a desproteção estatal deficiente.",
                        "isTrue": True,
                        "explanation": "A proporcionalidade engloba dupla face constitucional: a proibição do excesso sancionatório e a proibição da tutela deficitária dos bens jurídicos."
                    },
                    {
                        "statement": "A aplicação do princípio da bagatela imprópria opera a exclusão originária da tipicidade material, impedindo a caracterização do próprio fato típico.",
                        "isTrue": False,
                        "explanation": "Na bagatela imprópria o delito nasce plenamente típico e antijurídico, mas o juiz deixa de aplicar a pena por considerá-la desnecessária diante do caso."
                    }
                ],
                "pointers": [
                    {"topic": "Ofensividade e alteridade na dogmática criminal", "pageRef": 17},
                    {"topic": "Intervenção mínima, subsidiariedade e fragmentariedade", "pageRef": 19},
                    {"topic": "Ne bis in idem e vertentes da proporcionalidade", "pageRef": 20},
                    {"topic": "Princípio da confiança e requisitos da insignificância pelo STF", "pageRef": 22},
                    {"topic": "Bagatela imprópria e vedações sumuladas (Súmula 589 STJ)", "pageRef": 28}
                ]
            }
        },
        {
            "id": "direito-penal/a00/s03",
            "bizu": {
                "summary": [
                    "**Direito Penal Substantivo**: ramo do direito público incumbido de tutelar bens jurídicos fundamentais mediante seleção de condutas ofensivas cominadas a sanções estatais.",
                    "**Fonte Material do Direito Penal**: compete privativamente à União legislar sobre direito penal, admitida autorização aos Estados por lei complementar sobre temas locais específicos.",
                    "**Fonte Formal Imediata**: no ordenamento repressivo brasileiro unicamente a lei formal ordinária ou complementar atua como fonte formal imediata de normas penais incriminadoras.",
                    "**Fontes Formais Mediatas**: compreendem os costumes, a analogia integrativa in bonam partem e os postulados fundamentais gerais do ordenamento jurídico nacional.",
                    "**Crimes Imprescritíveis**: na Constituição Federal de 1988 somente o racismo e a atuação hostil de grupos armados contra o Estado Democrático de Direito são imprescritíveis.",
                    "**Crimes Inafiançáveis**: abrangem o racismo, a ação armada hostil e o agrupamento especial composto por tortura, tráfico de entorpecentes, terrorismo e hediondos.",
                    "**Crimes Insuscetíveis de Graça ou Anistia**: restritos ao quarteto constitucional composto por tortura, tráfico ilícito de drogas, terrorismo e delitos rotulados como hediondos.",
                    "**Graça e Indulto Coletivo**: a vedação constitucional de concessão de graça aos crimes hediondos e equiparados alcança expressamente os institutos do indulto e da comutação.",
                    "**Competência do Tribunal do Júri**: assegurada para o julgamento dos delitos dolosos contra a vida e das infrações que lhes forem estritamente conexas.",
                    "**Crimes Patrimoniais com Morte**: o latrocínio previsto no artigo 157, § 3º, do CP é crime contra o patrimônio e atrai a competência do juízo singular comum (Súmula 603 do STF).",
                    "**Inimputabilidade Etária**: os indivíduos menores de 18 anos são penalmente inimputáveis, submetendo-se ao regramento pedagógico protetivo da Lei nº 8.069/1990.",
                    "**Súmula 492 do STJ**: a conduta análoga ao delito de tráfico ilícito de drogas praticada por jovem menor não conduz compulsoriamente à medida socioeducativa de internação."
                ],
                "teoria": [
                    {
                        "statement": "A prática de tortura configura delito inafiançável e insuscetível de graça ou anistia, submetendo-se, contudo, aos prazos prescricionais ordinários.",
                        "isTrue": True,
                        "explanation": "A Constituição reserva a imprescritibilidade unicamente ao racismo e à ação de grupos armados; tortura, tráfico e hediondos prescrevem normalmente."
                    },
                    {
                        "statement": "A competência originária do Tribunal do Júri engloba o processo e julgamento do crime de latrocínio por haver o resultado morte consumado.",
                        "isTrue": False,
                        "explanation": "O latrocínio é crime patrimonial complexo cuja competência recai sobre o juiz singular criminal, consoante a Súmula 603 do STF."
                    },
                    {
                        "statement": "O indulto coletivo presidencial pode ser outorgado validamente a condenados pela prática de crimes hediondos caso preencham tempo mínimo de pena.",
                        "isTrue": False,
                        "explanation": "A jurisprudência pacífica e a Carta Magna interditam a concessão de graça, indulto e comutação para delitos hediondos e equiparados."
                    },
                    {
                        "statement": "Os Estados-membros podem ser autorizados mediante lei complementar federal a legislar sobre questões específicas e de interesse regional em matéria criminal.",
                        "isTrue": True,
                        "explanation": "O parágrafo único do artigo 22 da Constituição autoriza lei complementar para delegar competência legislativa estadual sobre temas pontuais."
                    }
                ],
                "revisao": [
                    {
                        "statement": "A infração penal caracterizada como racismo ostenta pela ordem constitucional natureza jurídica inafiançável e impassível de incidência da prescrição.",
                        "isTrue": True,
                        "explanation": "O art. 5º, inciso XLII, da CF expressamente declara o racismo delito inafiançável e imprescritível sujeito a reclusão."
                    },
                    {
                        "statement": "A jurisprudência do STJ impõe a aplicação compulsória de medida de internação ao adolescente apreendido em flagrante de ato análogo ao tráfico.",
                        "isTrue": False,
                        "explanation": "Nos termos da Súmula 492 do STJ, o ato análogo ao tráfico de drogas isoladamente não autoriza a internação automática de adolescente."
                    },
                    {
                        "statement": "As fontes formais mediatas do direito penal compreendem a legislação ordinária infraconstitucional editada no âmbito do Congresso Nacional.",
                        "isTrue": False,
                        "explanation": "A lei ordinária consubstancia a fonte formal imediata por excelência; fontes secundárias ou mediatas são os costumes e princípios gerais."
                    },
                    {
                        "statement": "A conexão processual autoriza que o Tribunal do Júri processe infração penal diversa cometida em concurso com homicídio doloso consumado.",
                        "isTrue": True,
                        "explanation": "A competência constitucional do júri exerce força atrativa sobre os delitos conexos praticados no mesmo contexto fático dos crimes dolosos contra a vida."
                    }
                ],
                "pointers": [
                    {"topic": "Conceito dogmático e repartição de competência normativa penal", "pageRef": 32},
                    {"topic": "Fontes imediatas e fontes secundárias mediatas do direito penal", "pageRef": 33},
                    {"topic": "Vedações constitucionais aos crimes graves (prescritibilidade e fiança)", "pageRef": 34},
                    {"topic": "Competência do Tribunal do Júri e descarte do latrocínio", "pageRef": 35},
                    {"topic": "Menoridade penal e balizas da internação no ECA (Súmula 492 STJ)", "pageRef": 36}
                ]
            }
        }
    ]
}

# ---------------------------------------------------------
# SUMMARIES (a00)
# ---------------------------------------------------------
summaries_data = {
    "aula": "direito-penal/a00",
    "batch": "pcpe-summary-direito-penal",
    "status": "DRAFT",
    "segments": [
        {
            "id": "direito-penal/a00/s01",
            "fingerprint": {
                "startPage": 2,
                "endPage": 16,
                "startTopic": "Princípios Fundamentais do Direito Penal"
            },
            "analytic": """Este segmento inicial examina os postulados constitucionais e dogmáticos basilares do Direito Penal, contemplando o princípio da legalidade em suas ramificações, a irretroatividade gravosa, a taxatividade, a individualização sancionatória, os limites humanitários da pena e o estado de inocência com suas repercussões executórias.

### Princípio da legalidade e suas vertentes garantistas
O postulado da legalidade representa a principal garantia do cidadão contra o arbítrio punitivo estatal, estando positivado no artigo 5º, inciso XXXIX, da Constituição Federal e no artigo 1º do Código Penal. Traduz-se no brocardo clássico latino *nullum crimen, nulla poena sine praevia lege*.

Essa garantia desdobra-se em duas vertentes complementares indispensáveis:
- **Reserva Legal Estrita**: determina que somente lei em sentido estrito (diploma ordinário ou complementar aprovado pelo Congresso Nacional) possui legitimidade para descrever condutas criminosas e cominar reprimendas privativas de liberdade. Medidas provisórias, decretos executivos ou resoluções administrativas não podem tipificar delitos ou exasperar reprimendas na seara criminal.
- **Anterioridade da Lei Penal**: veda que a novel norma repressiva incida sobre comportamentos praticados antes de sua entrada formal em vigor. A lei penal opera primordialmente para o futuro, vedando-se a criação retroativa de delitos (*lex gravior*), admitindo-se a eficácia retroativa apenas quando a alteração legislativa beneficiar materialmente o agente (*novatio legis in mellius* ou *abolitio criminis*).

### Desdobramentos da legalidade: taxatividade e analogia
Para assegurar a segurança jurídica dos administrados, o princípio da legalidade impõe limites severos à técnica legislativa e à hermenêutica judicial:
- **Mandato de Taxatividade ou Determinação**: impõe ao legislador a redação de tipos incriminadores dotados de absoluta clareza, concisão e densidade conceitual. São proscritos tipos penais excessivamente abertos ou indeterminados que confiram margem discricionária ilimitada ao juiz.
- **Vedação à Analogia In Malam Partem**: é peremptoriamente vedado colmatar lacunas legislativas mediante o emprego de analogia que resulte na criação de tipo penal incriminador ou no agravamento de sanções para hipótese não descrita em lei.
- **Admissibilidade da Analogia In Bonam Partem**: na ocorrência de omissão legislativa involuntária, a dogmática nacional admite amplamente o emprego da integração analógica favorável ao réu para assegurar prerrogativas de liberdade ou afastar a punibilidade.

### Individualização, humanidade e intranscendência das penas
A Carta Magna consagra diretrizes estruturantes para a cominação, dosimetria e aplicação prática das reprimendas corporais:
1. **Individualização da Pena**: concretiza-se em três planos consecutivos: na etapa legislativa (cominação de balizas penais abstratas adequadas à gravidade do fato), na fase judicial (fixação da sanção concreta na sentença com análise de circunstâncias judiciais e legais) e na execução penal (progressão gradativa de regimes e concessão de benefícios prisionais).
2. **Princípio da Humanidade ou Limitação das Penas**: o artigo 5º, inciso XLVII, da CF interdita categoricamente as reprimendas de morte (salvo em guerra formal declarada), de caráter perpétuo, de trabalhos forçados, de banimento territorial e quaisquer modalidades de punições cruéis ou degradantes.
3. **Princípio da Intranscendência**: a sanção penal possui caráter estritamente pessoal, não passando jamais da figura do sentenciado. Entretanto, a obrigação civil de reparação dos prejuízos causados pelo delito e a perda de bens decretada em favor da coletividade podem ser transferidas aos herdeiros até o limite absoluto das forças do patrimônio transferido na herança.

### Presunção de inocência e repercussões executórias
O postulado da não culpabilidade, erigido no artigo 5º, inciso LVII, da Constituição da República, assegura que nenhum cidadão será tido por culpado até a ocorrência do trânsito em julgado de sentença penal condenatória. Funciona como norma de tratamento processual (vedando discriminações antecipadas decorrentes do simples processo) e como norma probatória imperativa.

No âmbito probatório, incumbe com exclusividade ao Ministério Público ou ao querelante o ônus irrefutável de demonstrar autoria e materialidade delitivas. Na pendência de incerteza fática insuperável ao final da instrução criminal, impõe-se a aplicação da regra de julgamento do *in dubio pro reo*, com a absolvição do denunciado.

O Supremo Tribunal Federal, ao julgar as ADCs 43, 44 e 54, reafirmou a inconstitucionalidade da execução provisória da pena antes do trânsito em julgado para os crimes em geral. Contudo, ao apreciar o Tema 1068 de Repercussão Geral, a Suprema Corte fixou a soberania dos veredictos do Tribunal do Júri para autorizar o cumprimento imediato da sanção privativa de liberdade imposta pelo Conselho de Sentença, independentemente da quantidade de pena dosada na sentença do magistrado presidente.

### Para fixar
- A legalidade desdobra-se em reserva de lei formal estrita e anterioridade irrestrita da norma criminal.
- A irretroatividade penal atinge leis desfavoráveis, aplicando-se a retroatividade ampla à norma mais benéfica.
- A taxatividade exige precisão redacional e veda a formulação de normas incriminadoras abertas ou vagas.
- A analogia in malam partem é proibida, sendo plenamente aceita a integração analógica in bonam partem.
- A individualização da reprimenda opera nos planos legislativo abstrato, judicial dosimétrico e executório prisional.
- A intranscendência impede a passagem da pena corporal a terceiros, autorizando reparação civil aos herdeiros até as forças da herança.
- O estado de inocência veda a execução antecipada de pena sem trânsito em julgado segundo o STF (ADCs 43, 44 e 54).
- O Tema 1068 do STF autoriza a prisão imediata do réu condenado em plenário pelos jurados do Tribunal do Júri.""",
            "synthetic": [
                "**Princípio da Legalidade**: não há infração penal sem lei anterior cominadora nem sanção privativa sem prévia descrição legislativa estrita formal.",
                "**Reserva de Lei Formal**: diplomas secundários como medidas provisórias e resoluções não possuem aptidão constitucional para definir crimes ou cominar penas corporais.",
                "**Anterioridade e Irretroatividade**: a norma criminal não alcança fatos pretéritos desfavoráveis, retroagindo sem embaraços unicamente quando beneficiar materialmente o réu.",
                "**Mandato de Taxatividade**: veda normas incriminadoras indeterminadas, impondo ao Parlamento a formulação clara e delimitada dos preceitos primários incriminadores.",
                "**Integração por Analogia**: veda-se a analogia prejudicial ao acusado, admitindo-se a integração analógica benéfica na presença de omissões involuntárias da lei.",
                "**Individualização das Penas**: processa-se sequencialmente nas etapas de definição abstrata legislativa, dosimetria sentencial judicial e cumprimento penitenciário.",
                "**Limitação das Penas**: a Carta Magna proíbe terminantemente sanções perpétuas, de trabalhos forçados, de banimento, cruéis e de morte fora de guerra externa.",
                "**Intranscendência Pessoal**: a reprimenda criminal não ultrapassa a pessoa do infrator, atingindo sucessores unicamente as obrigações civis reparatórias nos limites da herança.",
                "**Presunção de Não Culpabilidade**: atua como baliza probatória com aplicação do in dubio pro reo e interdita o cumprimento prematuro de pena antes do trânsito em julgado.",
                "**Tema 1068 do STF**: a soberania constitucional do corpo de jurados autoriza a execução imediata da reprimenda corporal fixada pelo Tribunal do Júri."
            ]
        },
        {
            "id": "direito-penal/a00/s02",
            "fingerprint": {
                "startPage": 17,
                "endPage": 29,
                "startTopic": "Princípios da Ofensividade e Insignificância"
            },
            "analytic": """Este segmento aborda postulados fundamentais de contenção do poder repressivo estatal, detalhando a ofensividade, alteridade, intervenção mínima em suas duas facetas, a adequação social e as diretrizes consolidadas do princípio da insignificância material e da bagatela imprópria.

### Princípios da ofensividade, alteridade e intervenção mínima
A doutrina penal contemporânea impõe critérios materiais para a legitimação da tipificação de crimes e aplicação concreta de sanções:
- **Princípio da Ofensividade (ou Lesividade)**: preconiza que nenhuma conduta pode ser tipificada como ilícito penal sem que promova dano efetivo ou perigo concreto de lesão a um bem jurídico penalmente tutelado. Atos meramente imorais, pensamentos ou preferências individuais sem reflexo lesivo externo estão imunes ao controle penal.
- **Princípio da Alteridade**: decorre do postulado de que o direito criminal tutela exclusivamente as relações intersubjetivas. Veda-se a punição de atos meramente preparatórios internos e de comportamentos de autolesão que não transbordem os limites da esfera pessoal do próprio agente (como na autolesão corporal ou tentativa de suicídio).
- **Intervenção Mínima (*Ultima Ratio*)**: o direito penal deve intervir apenas quando todos os demais ramos jurídicos (civil, tributário, administrativo) se mostrarem ineficazes para restabelecer a paz social.

O princípio da intervenção mínima desdobra-se em duas características correlatas:
- **Subsidiariedade**: o aparato sancionador criminal funciona como último recurso da política estatal, devendo permanecer inerte sempre que a tutela administrativa ou reparação civil suprir satisfatoriamente a proteção do interesse social.
- **Fragmentariedade**: o direito repressivo não protege todos os bens da vida, mas apenas uma parcela restrita e valiosa desses bens diante de agressões graves e intoleráveis.

### Adequação social e vedação ao bis in idem
O postulado da adequação social, sistematizado por Hans Welzel, enuncia que ações materialmente toleradas pela sociedade e integradas aos costumes comunitários não devem ser censuradas criminalmente. Todavia, a jurisprudência brasileira pacificou que o mero costume reiterado não tem força jurídica para revogar preceito formal de lei penal incriminadora.

Nesse prisma, o Superior Tribunal de Justiça editou a Súmula 502, assentando que a comercialização clandestina de mídias piratas continua ostentando tipicidade penal formal e material nos moldes do artigo 184, § 2º, do CP, repelindo a alegação de adequação social fundada no consumo disseminado.

Paralelamente, o princípio do *ne bis in idem* impede a sobreposição de persecuções penais ou a múltipla valoração do mesmo fato empírico para agravar a punição de um indivíduo, consagrando a segurança jurídica e a lealdade processual contra sanções estatais desmedidas.

### Princípio da insignificância e balizas dos tribunais superiores
O princípio da insignificância (ou bagatela própria), idealizado por Claus Roxin, atua como instrumento hermenêutico de exclusão da tipicidade material. O comportamento do infrator subsume-se perfeitamente à letra da norma incriminadora (tipicidade formal), mas carece de relevância no plano lesivo concreto, desnaturando a tipicidade penal.

O Supremo Tribunal Federal consolidou quatro requisitos cumulativos indispensáveis para o reconhecimento da insignificância:
1. Mínima ofensividade da conduta empreendida pelo infrator;
2. Nenhuma periculosidade social da ação desempenhada;
3. Reduzidíssimo grau de reprovabilidade do comportamento adotado;
4. Inexpressividade da lesão jurídica provocada no patrimônio tutelado.

| Instituto | Efeito na Estrutura do Delito | Momento de Constatação |
| --- | --- | --- |
| Bagatela Própria (Insignificância) | Exclui a tipicidade material do fato | Prática do ato delituoso |
| Bagatela Imprópria | Mantém o crime e afasta a pena desnecessária | Aplicação judicial da sentença |

Na bagatela imprópria, o delito é formal e materialmente típico, restando configurada a ilicitude e a culpabilidade. Não obstante, o magistrado reconhece que a sanção penal tornou-se socialmente desnecessária diante de acontecimentos posteriores, como a reparação espontânea voluntária e a ausência de repercussão comunitária.

Por fim, cumpre destacar vedações de suma relevância para a atividade policial:
- **Súmula 589 do STJ**: é manifestamente inaplicável o princípio da insignificância em crimes e contravenções penais perpetrados contra a mulher no âmbito das relações domésticas ou familiares.
- **Súmula 599 do STJ**: a insignificância não incide sobre crimes praticados contra a administração pública, haja vista a violação da moralidade administrativa, ressalvada a hipótese excepcional de descaminho tributário abaixo do limite legal.

### Para fixar
- A ofensividade exige efetiva lesão ou perigo concreto de dano ao bem jurídico protegido pela lei penal.
- O princípio da alteridade veda a criminalização de condutas meramente íntimas e de autolesões voluntárias.
- A intervenção mínima projeta-se na subsidiariedade (último recurso) e na fragmentariedade (recorte de bens).
- A adequação social não autoriza a revogação de leis criminais por costumes comunitários reiterados.
- A Súmula 502 do STJ repele a adequação social para a comercialização habitual de mídias de CDs e DVDs piratas.
- A insignificância própria exclui a tipicidade material quando preenchidos os quatro vetores fixados pelo STF.
- Na bagatela imprópria o crime subsiste hígido, deixando o magistrado de cominar a pena por considerá-la inútil.
- A Súmula 589 do STJ veda a aplicação da insignificância nos crimes e contravenções no ambiente doméstico feminino.""",
            "synthetic": [
                "**Princípio da Ofensividade**: exige comprovação de lesão efetiva ou risco concreto de dano ao bem jurídico tutelado para a constituição válida do ilícito penal.",
                "**Princípio da Alteridade**: veda a perseguição penal de condutas de autolesão que não causem prejuízo a interesses de terceiros na convivência social.",
                "**Intervenção Mínima**: o direito penal opera como última cartada coercitiva do Estado diante da evidente fragilidade das demais esferas de controle jurídico.",
                "**Subsidiariedade e Fragmentariedade**: atua em segundo plano após falha dos demais ramos jurídicos, limitando-se a selecionar condutas flagrantemente intoleráveis.",
                "**Adequação Social**: condutas integradas aos costumes comunitários não devem ser criminalizadas, sem que o costume tenha força para revogar lei formal.",
                "**Súmula 502 do STJ**: a exposição de mídias piratas à venda constitui fato típico inafastável pela adequação social por violar preceito formal.",
                "**Princípio do Ne Bis In Idem**: veda a duplicidade de persecuções ou a múltipla sanção estatal apoiada no mesmo suporte fático histórico delitivo.",
                "**Vetor da Insignificância Material**: exclui a tipicidade material mediante mínima ofensividade, desprovimento de periculosidade, baixa reprovação e dano inexpressivo.",
                "**Bagatela Imprópria**: conserva a tipicidade e ilicitude do fato, autorizando o magistrado a deixar de impor a pena quando desnecessária no caso.",
                "**Súmula 589 do STJ**: é inadmissível a incidência da bagatela em infrações cometidas com violência doméstica ou familiar contra o gênero feminino."
            ]
        },
        {
            "id": "direito-penal/a00/s03",
            "fingerprint": {
                "startPage": 30,
                "endPage": 36,
                "startTopic": "Fontes, Tribunal do Júri e Menoridade"
            },
            "analytic": """Este segmento examina a conceituação dogmática do Direito Penal, suas matrizes formais e materiais de produção normativa, as vedações constitucionais cominadas a infrações de gravidade extrema, a competência soberana do Tribunal do Júri e o regramento protetivo da menoridade.

### Conceito dogmático e repartição de fontes penais
O Direito Penal pode ser compreendido como o segmento do direito público orientado a selecionar os valores mais caros à convivência coletiva, associando a sua transgressão culposa ou dolosa a imposição coativa de penas e medidas de segurança.

Quanto à produção e revelação das normas penais, distinguem-se duas dimensões:
- **Fontes Materiais ou Substanciais**: referem-se aos órgãos constitucionalmente investidos da atribuição originária de legislar. Conforme o artigo 22, inciso I, da Carta Magna, a competência para legislar sobre matéria penal pertence privativamente à União. O parágrafo único desse dispositivo faculta autorização aos Estados-membros, via lei complementar federal, para criar normas sobre questões regionais específicas.
- **Fontes Formais Imediatas**: correspondem aos atos jurídicos aptos a inovar na ordem jurídica criminal tipificando infrações de forma direta. No modelo jurídico brasileiro, unicamente a lei em sentido estrito (lei ordinária ou complementar emanada do Parlamento) ostenta natureza de fonte formal imediata.
- **Fontes Formais Mediatas ou Secundárias**: compreendem os costumes integrativos, a analogia *in bonam partem* e os princípios gerais do direito, operando de modo subsidiário para integrar eventuais omissões legislativas sem criar novos tipos incriminadores.

### Vedações constitucionais e crimes de extrema gravidade
A Constituição Federal de 1988 estabeleceu tratamentos rigorosos diferenciados para delitos cuja gravidade compromete a estabilidade comunitária ou a ordem democrática republicana:

| Espécie de Vedação | Crimes Abrangidos pelo Mandamento Constitucional | Dispositivo da CF/88 |
| --- | --- | --- |
| Inafiançabilidade | Todos: Racismo, Ação Armada, Tortura, Tráfico, Terrorismo e Hediondos | Art. 5º, XLII, XLIII e XLIV |
| Imprescritibilidade | Apenas dois: Racismo e Ação de Grupos Armados contra a Ordem Democrática | Art. 5º, XLII e XLIV |
| Vedação de Graça e Anistia | Quarteto TTHH: Tortura, Tráfico Ilícito de Drogas, Terrorismo e Crimes Hediondos | Art. 5º, XLIII |

Cumpre assinalar que os delitos de tortura, tráfico de entorpecentes, terrorismo e os crimes hediondos são passíveis de prescrição conforme as tabelas ordinárias do artigo 109 do Código Penal. Ademais, a vedação à graça concedida pelo Presidente da República atinge expressamente os benefícios do indulto coletivo natalino e da comutação de penas, conforme remansosa jurisprudência fixada pelo STJ.

### Competência do Tribunal do Júri e limites dogmáticos
O Tribunal do Júri consubstancia instituição de matriz constitucional garantidora das liberdades cívicas (artigo 5º, inciso XXXVIII, da CF), regendo-se pelos postulados da plenitude de defesa, sigilo irrestrito das votações, soberania incontestável dos veredictos do Conselho de Sentença e competência privativa para o julgamento dos crimes dolosos contra a vida (homicídio, infanticídio, induzimento ao suicídio e aborto), consumados ou tentados.

A competência do colegiado popular atrai, por continência ou conexão processual, os delitos conexos praticados no mesmo cenário fático. Não obstante, duas infrações graves com resultado letal não se inserem na alçada do Júri:
- **Latrocínio (artigo 157, § 3º, inciso II, do CP)**: configura crime complexo contra o patrimônio cuja intenção preponderante do agente recai sobre a subtração pecuniária, sendo julgado pelo juízo monocrático criminal singular (Súmula 603 do STF).
- **Lesão Corporal Seguida de Morte (artigo 129, § 3º, do CP)**: delito preterdoloso com dolo antecedente na ofensa corporal e culpa estrita no resultado letal superveniente.

### Menoridade penal e balizas da intervenção socioeducativa
O artigo 228 da Carta Magna e o artigo 27 do Código Penal consagram a inimputabilidade penal absoluta dos indivíduos que não atingiram a idade de dezoito anos na data do fato criminoso.

Os menores de idade sujeitam-se aos preceitos protetivos e pedagógicos do Estatuto da Criança e do Adolescente (Lei nº 8.069/1990). O adolescente que pratica fato análogo a crime comete ato infracional, sujeitando-se a medidas de natureza socioeducativa. O Superior Tribunal de Justiça, na Súmula 492, pacificou que a prática de ato infracional análogo ao tráfico ilícito de entorpecentes, por si só, não autoriza a imposição automática da medida socioeducativa de internação.

### Para fixar
- A União detém competência legislativa privativa penal, permitida delegação estadual específica via lei complementar.
- A lei formal ordinária ou complementar consubstancia a única fonte formal imediata do direito penal pátrio.
- São imprescritíveis pela ordem constitucional unicamente o racismo e a ação armada contra a ordem democrática.
- A inafiançabilidade alcança o racismo, grupos armados hostis, tortura, tráfico de drogas, terrorismo e hediondos.
- Tortura, tráfico, terrorismo e hediondos não recebem graça, anistia, indulto e comutação, mas prescrevem.
- O Tribunal do Júri julga com soberania os crimes dolosos contra a vida e as infrações que lhe forem estritamente conexas.
- O crime de latrocínio possui índole patrimonial e é julgado pelo juiz singular, conforme Súmula 603 do STF.
- Os menores de dezoito anos são penalmente inimputáveis, aplicando-se as diretrizes pedagógicas da Lei nº 8.069/1990.""",
            "synthetic": [
                "**Competência Legislativa Privativa**: compete unicamente à União legislar sobre matérias penais, cabendo delegação aos Estados por lei complementar restrita a temas locais.",
                "**Fontes Imediatas e Mediatas**: a lei ordinária atua como fonte formal primária imediata, operando costumes e princípios como fontes secundárias de integração supletiva.",
                "**Crimes Imprescritíveis**: na ordem constitucional brasileira apenas o crime de racismo e o confronto de grupos armados hostis contra o Estado Democrático de Direito são imprescritíveis.",
                "**Vedações a Graça e Anistia**: o quarteto constitucional formado por tortura, tráfico de drogas, terrorismo e crimes hediondos veda expressamente anistia, graça, indulto e comutação.",
                "**Prescritibilidade do Quarteto**: tortura, tráfico, terrorismo e hediondos são inafiançáveis e insuscetíveis de graça, submetendo-se contudo aos prazos de prescrição regulares.",
                "**Competência do Júri**: possui atribuição garantida para julgar delitos dolosos contra a vida consumados ou tentados, atraindo causas criminais conexas decorrentes do mesmo contexto.",
                "**Súmula 603 do STF**: o delito de latrocínio não integra a competência do Tribunal do Júri por ostentar natureza jurídica de crime patrimonial complexo.",
                "**Inimputabilidade Etária**: os cidadãos que possuem idade inferior a dezoito anos na conduta respondem nos moldes tutelares pedagógicos da Lei nº 8.069/1990.",
                "**Súmula 492 do STJ**: o ato infracional análogo ao comércio de entorpecentes isoladamente não legitima a imposição compulsória de medida privativa de internação."
            ]
        }
    ]
}

# Write items file
with open(ITEMS_FILE, "w", encoding="utf-8") as f:
    json.dump(items_data, f, ensure_ascii=False, indent=2)
print(f"Wrote {ITEMS_FILE}")

# Write summaries file
with open(SUMMARIES_FILE, "w", encoding="utf-8") as f:
    json.dump(summaries_data, f, ensure_ascii=False, indent=2)
print(f"Wrote {SUMMARIES_FILE}")
