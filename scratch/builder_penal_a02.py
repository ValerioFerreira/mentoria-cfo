# -*- coding: utf-8 -*-
"""Builder for direito-penal a02 (items and summaries)."""
import json
import os

ITEMS_FILE = "content/items/direito-penal/a02.json"
SUMMARIES_FILE = "content/summaries/direito-penal/a02.json"

os.makedirs(os.path.dirname(ITEMS_FILE), exist_ok=True)
os.makedirs(os.path.dirname(SUMMARIES_FILE), exist_ok=True)

with open("content/segments/direito-penal.json", "r", encoding="utf-8") as f:
    all_segs = {s["id"]: s for s in json.load(f)["segments"]}

def get_fp(sid):
    s = all_segs[sid]
    return {"startPage": s["startPage"], "endPage": s["endPage"], "startTopic": s["startTopic"]}

# ---------------------------------------------------------
# BIZU ITEMS (a02)
# ---------------------------------------------------------
items_data = {
    "aula": "direito-penal/a02",
    "batch": "pcpe-bizu-direito-penal",
    "status": "DRAFT",
    "stage": "bizu",
    "segments": [
        {
            "id": "direito-penal/a02/s01",
            "bizu": {
                "summary": [
                    "**Conceito Analítico de Crime**: corrente majoritária tripartida define a infração penal como fato típico, antijurídico e culpável.",
                    "**Teoria Finalista da Conduta**: capitaneada por Welzel, concebe a conduta como comportamento humano voluntário e consciente dirigido a uma finalidade lícita ou ilícita.",
                    "**Dolo e Culpa no Tipo**: o finalismo deslocou o dolo e a culpa da culpabilidade para o próprio interior do fato típico.",
                    "**Exclusão Involuntária da Conduta**: atos reflexos puros, estados de inconsciência completa (sonambulismo, hipnose profunda) e coação física irresistível (*vis absoluta*) eliminam a conduta.",
                    "**Coação Moral Irresistível (*Vis Compulsiva*)**: não exclui a conduta nem a tipicidade, afastando exclusivamente a culpabilidade por inexigibilidade de conduta diversa.",
                    "**Condutas Comissivas**: consubstanciam comandos proibitivos violados mediante ação física positiva do autor.",
                    "**Crimes Omissivos Próprios ou Puros**: o tipo penal descreve uma abstenção pura de agir (como na omissão de socorro), consumando-se no exato momento da inércia desprovida de resultado material posterior.",
                    "**Crimes Omissivos Impróprios ou Comissivos por Omissão**: o agente possui o dever jurídico específico de agir para evitar a consumação do evento danoso (posição de garante do art. 13, § 2º).",
                    "**Fontes do Dever de Garante**: obrigação imposta por lei direta, assunção voluntária de responsabilidade ou comportamento anterior que criou o perigo iminente do resultado.",
                    "**Tentativa na Omissão**: os crimes omissivos próprios não admitem conatus por serem unissubsistentes; os omissivos impróprios admitem tentativa de forma pacífica.",
                    "**Capacidade Física de Agir**: a responsabilidade penal pela omissão exige a comprovação inequívoca de que o sujeito omitente podia atuar materialmente sem colocar em risco a própria segurança.",
                    "**Teorias Causalistas Superadas**: a teoria causal-naturalista e a neokantiana tratavam o dolo como normativo integrado à culpabilidade, concepção rejeitada pela reforma penal de 1984."
                ],
                "teoria": [
                    {
                        "statement": "A coação física irresistível suprime a própria voluntariedade motora do indivíduo coagido, operando a eliminação originária da conduta penal.",
                        "isTrue": True,
                        "explanation": "Na coação física absoluta (vis absoluta) não há manifestação de vontade consciente, restando afastada a própria conduta e o fato típico."
                    },
                    {
                        "statement": "Nos crimes omissivos puros, o legislador exige a efetiva verificação de modificação sensível no mundo exterior para que ocorra a consumação típica.",
                        "isTrue": False,
                        "explanation": "Os crimes omissivos próprios independem de resultado naturalístico, consumando-se pela simples abstenção desautorizada no momento oportuno."
                    },
                    {
                        "statement": "A posição de garantidor no ordenamento penal brasileiro vincula exclusivamente agentes públicos dotados de obrigação de tutela estatuída em lei formal.",
                        "isTrue": False,
                        "explanation": "O art. 13, § 2º, elenca três fontes do dever de garante: lei direta, assunção de garantia material ou comportamento precedente gerador do perigo."
                    },
                    {
                        "statement": "O sistema finalista adotado pelo Código Penal alocou o exame do dolo e da culpa como elementos anímicos situados no bojo da culpabilidade.",
                        "isTrue": False,
                        "explanation": "A teoria finalista de Welzel transferiu o dolo e a culpa para a conduta típica, integrando a tipicidade penal."
                    }
                ],
                "revisao": [
                    {
                        "statement": "O indivíduo que cria com seu comportamento prévio o perigo de um evento danoso adquire a obrigação jurídica de impedir o resultado letal superveniente.",
                        "isTrue": True,
                        "explanation": "Conforme o art. 13, § 2º, 'c', a conduta anterior criadora do risco impõe ao sujeito a posição de garante impeditiva do resultado."
                    },
                    {
                        "statement": "Movimentos corporais meramente reflexos ensejam responsabilidade penal dolosa caso o agente tenha histórico de reações corporais involuntárias.",
                        "isTrue": False,
                        "explanation": "Atos meramente reflexos consubstanciam reações puramente neuromusculares desprovidas de impulso consciente, excluindo a conduta."
                    },
                    {
                        "statement": "A coação moral irresistível afasta a culpabilidade do agente em razão da inexigibilidade de conduta diversa, conservando o fato típico e ilícito.",
                        "isTrue": True,
                        "explanation": "A coação psicológica irresistível atua sobre a autodeterminação sem retirar a capacidade física do ato, excluindo apenas a culpabilidade."
                    },
                    {
                        "statement": "A prática de crime omissivo impróprio admite a incidência da modalidade tentada quando a omissão é interrompida por fatores alheios à vontade do omitente.",
                        "isTrue": True,
                        "explanation": "Diferentemente dos crimes omissivos próprios, os comissivos por omissão são materiais e plurissubsistentes, comportando perfeitamente a tentativa."
                    }
                ],
                "pointers": [
                    {"topic": "Conceito analítico tripartido e teoria finalista da conduta", "pageRef": 3},
                    {"topic": "Hipóteses de ausência de conduta (reflexos, coação e sono)", "pageRef": 5},
                    {"topic": "Crimes omissivos próprios e natureza da abstenção", "pageRef": 7},
                    {"topic": "Dever de garante e fontes do artigo 13, parágrafo segundo", "pageRef": 9}
                ]
            }
        },
        {
            "id": "direito-penal/a02/s02",
            "bizu": {
                "summary": [
                    "**Resultado Naturalístico**: modificação sensível operada no mundo exterior provocada pelo comportamento do indivíduo (lesão corporal, morte da vítima).",
                    "**Classificação Quanto ao Resultado**: materiais (exigem resultado naturalístico para consumação), formais (resultado previsto na lei, mas dispensável) e mera conduta (não preveem resultado).",
                    "**Nexo de Causalidade**: vínculo biológico e fático que une o comportamento do indivíduo ao resultado típico gerado no mundo fenomênico.",
                    "**Teoria da Conditio Sine Qua Non**: adotada no artigo 13 do CP, reputa-se causa toda ação ou omissão sem a qual o evento não teria se verificado.",
                    "**Juízo Hipotético de Eliminação (Thyrén)**: suprime-se mentalmente a conduta; se o resultado persistir inalterado, ela não é causa; se o resultado desaparecer, ela é causa.",
                    "**Concausas Absolutamente Independentes**: atuam de modo desconectado da conduta, originando sozinhas o resultado (preexistentes, concomitantes ou supervenientes).",
                    "**Consequência das Causas Absolutas**: rompem integralmente o nexo causal, respondendo o agente exclusivamente pelos atos tentados até então praticados.",
                    "**Concausas Relativamente Independentes Preexistentes e Concomitantes**: somam-se à conduta do agente para produzir o evento (hemofilia prévia, infarto durante disparo), não rompendo o liame causal.",
                    "**Superveniência Causal Autônoma (art. 13, § 1º)**: a causa superveniente que por si só produziu o resultado exclui a imputação do evento final.",
                    "**Exemplo Clássico do Artigo 13, § 1º**: vítima alvejada sem gravidade que falece em capotamento da ambulância; o atirador responde apenas pela tentativa de homicídio.",
                    "**Causa Superveniente em Linha de Desdobramento**: a infecção hospitalar decorrente da cirurgia necessária integra a evolução natural da lesão, respondendo o agente pelo crime consumado.",
                    "**Vedação do Regresso ao Infinito**: a amplitude da causalidade física é freada no campo da tipicidade mediante a demonstração obrigatória de dolo ou culpa."
                ],
                "teoria": [
                    {
                        "statement": "Nos crimes formais, a efetiva produção do resultado naturalístico é condição indispensável para a caracterização da consumação delitiva.",
                        "isTrue": False,
                        "explanation": "Nos crimes formais ou de consumação antecipada, o delito consuma-se com a prática da conduta descrita, sendo o resultado mero exaurimento."
                    },
                    {
                        "statement": "O Código Penal acolheu no caput do artigo 13 a teoria da causalidade adequada como critério geral de imputação causal biológica.",
                        "isTrue": False,
                        "explanation": "O caput do art. 13 consagrou a teoria da equivalência dos antecedentes causais (conditio sine qua non); a causalidade adequada incide apenas na ressalva do § 1º."
                    },
                    {
                        "statement": "O surgimento superveniente de um fator causal autônomo e relativamente independente rompe a imputação do evento lesivo final em relação ao autor da conduta primária.",
                        "isTrue": True,
                        "explanation": "O art. 13, § 1º, exclui a imputação do resultado decorrente de causa superveniente que inaugurou linha causal autônoma, respondendo o autor pelos fatos anteriores."
                    },
                    {
                        "statement": "A concausa preexistente relativamente independente consistente em vulnerabilidade patológica da vítima rompe o nexo causal físico com a conduta do autor.",
                        "isTrue": False,
                        "explanation": "Concausas relativamente independentes anteriores ou concomitantes conjugam-se com a conduta sem quebrar a imputação do resultado provocado."
                    }
                ],
                "revisao": [
                    {
                        "statement": "O método hipotético de eliminação idealizado por Thyrén permite constatar se uma ação humana atua como antecedente causal necessário de um resultado empírico.",
                        "isTrue": True,
                        "explanation": "A eliminação mental da ação revela se ela é causa imprescindível do evento fenomênico no bojo da conditio sine qua non."
                    },
                    {
                        "statement": "Quando o resultado letal decorre de concausa absolutamente independente superveniente, o agente da conduta originária é absolvido de qualquer sanção.",
                        "isTrue": False,
                        "explanation": "A causa absolutamente independente afasta a imputação do resultado letal, mas o agente responde pelos atos executórios já praticados a título de tentativa."
                    },
                    {
                        "statement": "A complicação infecciosa hospitalar advinda do procedimento médico emergencial integra a linha de desdobramento natural dos ferimentos causados pelo agressor.",
                        "isTrue": True,
                        "explanation": "A intercorrência médica previsível na linha evolutiva da lesão não inaugura novo nexo autônomo, respondendo o ofensor pelo resultado morte consumado."
                    },
                    {
                        "statement": "Os crimes de mera conduta dispensam a previsão de qualquer resultado naturalístico no preceito primário do tipo penal incriminador.",
                        "isTrue": True,
                        "explanation": "Os tipos de mera conduta limitam-se a descrever uma ação pura sem qualquer vinculação a evento fático externo destacável da atividade motora."
                    }
                ],
                "pointers": [
                    {"topic": "Classificação dos crimes quanto ao resultado (materiais, formais, mera conduta)", "pageRef": 11},
                    {"topic": "Nexo causal e teoria da conditio sine qua non no artigo 13", "pageRef": 13},
                    {"topic": "Concausas absolutamente independentes e seus efeitos penais", "pageRef": 15},
                    {"topic": "Superveniência de causa relativamente independente no artigo 13, § 1º", "pageRef": 17}
                ]
            }
        },
        {
            "id": "direito-penal/a02/s03",
            "bizu": {
                "summary": [
                    "**Tipicidade Formal**: subsunção estrita e subsunção lógica entre o comportamento real do indivíduo e o modelo abstrato descrito na norma penal incriminadora.",
                    "**Tipicidade Material**: juízo de desvalor ético-social que afere se a conduta lesou concretamente e de forma intolerável o bem jurídico penalmente tutelado.",
                    "**Tipicidade Conglobante (Zaffaroni)**: soma da tipicidade material com a antinormatividade da conduta, verificando se a ordem jurídica geral como um todo não autoriza o ato.",
                    "**Elementos Objetivos Descritivos**: elementos do tipo penal apreensíveis pelos sentidos físicos humanos ordinários (coisa, mulher, arma, matar).",
                    "**Elementos Objetivos Normativos**: exigem juízo axiológico de valor jurídico ou social para sua compreensão (documento, funcionário público, indevidamente, sem justa causa).",
                    "**Elementos Subjetivos do Tipo**: ânimo especial que impulsiona o infrator, como a finalidade especial de agir ou dolo específico (fim de obter vantagem indevida).",
                    "**Funções do Tipo Penal**: função garantidora da liberdade cívica, função indiciária da antijuridicidade (*ratio cognoscendi*) e função fundamentadora do ius puniendi.",
                    "**Exclusão da Tipicidade por Coação Física**: a força física absoluta suprime o movimento volitivo, eliminando a conduta e impedindo a formação da tipicidade formal.",
                    "**Exclusão por Erro de Tipo Essencial**: o erro inevitável que recai sobre elementares constitutivas do fato extirpa originariamente o dolo e a culpa.",
                    "**Exclusão por Insignificância**: a ausência de lesividade relevante descaracteriza a tipicidade material, subsistindo mera adequação formal sem relevo penal.",
                    "**Adequação Social e Tipicidade**: comportamentos tolerados historicamente pela moralidade coletiva afastam a tipicidade material, desde que não afrontem vedação legislativa expressa.",
                    "**Tipos Penais Fechados e Abertos**: tipos fechados descrevem exaustivamente a ação punível; tipos abertos dependem de integração judicial casuística (como nos crimes culposos)."
                ],
                "teoria": [
                    {
                        "statement": "A tipicidade material aperfeiçoa-se com a verificação de perfeita correspondência formal entre o comportamento do sujeito e o preceito abstrato da lei.",
                        "isTrue": False,
                        "explanation": "A mera subsunção à letra do texto traduz tipicidade formal; a tipicidade material demanda dano concreto e substancial ao bem tutelado."
                    },
                    {
                        "statement": "Elementos normativos do tipo penal dependem de valoração jurídica ou axiológica para a elucidação precisa de seu significado na conduta.",
                        "isTrue": True,
                        "explanation": "Termos como 'indevidamente' ou 'documento' constituem elementos normativos que requerem juízo axiológico integrador."
                    },
                    {
                        "statement": "O reconhecimento do princípio da insignificância opera a exclusão da tipicidade formal, mantendo incólume a tipicidade material da infração.",
                        "isTrue": False,
                        "explanation": "A insignificância exclui a tipicidade material pela inexpressividade da lesão, preservando apenas a tipicidade formal."
                    },
                    {
                        "statement": "A tipicidade conglobante idealizada pela doutrina exige que a conduta seja materialmente lesiva e não fomentada ou autorizada por outros ramos do ordenamento.",
                        "isTrue": True,
                        "explanation": "Para Zaffaroni, a tipicidade conglobante demanda antinormatividade global, afastando a tipicidade em atos fomentados ou permitidos pela ordem jurídica."
                    }
                ],
                "revisao": [
                    {
                        "statement": "A função indiciária do tipo penal consagra que a constatação da tipicidade gera a presunção relativa de que a conduta é também ilícita.",
                        "isTrue": True,
                        "explanation": "A tipicidade atua como indício de antijuridicidade (teoria da ratio cognoscendi), ilicitude que só é afastada se presente causa de justificação."
                    },
                    {
                        "statement": "O erro de tipo essencial inevitável extirpa o dolo da conduta praticada, permitindo a punição do agente na modalidade culposa residual.",
                        "isTrue": False,
                        "explanation": "O erro de tipo inevitável (escusável) elimina tanto o dolo quanto a culpa, afastando integralmente a tipicidade penal."
                    },
                    {
                        "statement": "Os crimes culposos consubstanciam espécies paradigmáticas de tipos penais abertos diante da necessidade de integração do dever de cuidado pelo juiz.",
                        "isTrue": True,
                        "explanation": "Nos crimes culposos o magistrado deve preencher no caso concreto em que medida o agente violou o dever objetivo de cautela."
                    },
                    {
                        "statement": "Os elementos subjetivos especiais do tipo incriminador prescindem de comprovação instrutória quando a figura objetiva restar demonstrada.",
                        "isTrue": False,
                        "explanation": "A configuração do crime exige demonstração probatória tanto das elementares materiais objetivas quanto da finalidade anímica especial do autor."
                    }
                ],
                "pointers": [
                    {"topic": "Tipicidade formal, tipicidade material e tipicidade conglobante", "pageRef": 20},
                    {"topic": "Elementos descritivos, normativos e subjetivos do tipo penal", "pageRef": 22},
                    {"topic": "Funções dogmáticas do tipo penal e ratio cognoscendi", "pageRef": 25},
                    {"topic": "Causas de atipicidade (insignificância, coação e erro de tipo)", "pageRef": 27}
                ]
            }
        },
        {
            "id": "direito-penal/a02/s04",
            "bizu": {
                "summary": [
                    "**Crimes Comuns**: podem ser praticados por qualquer cidadão imputável, sem exigência de condição pessoal especial do sujeito ativo (homicídio, furto).",
                    "**Crimes Próprios**: a norma penal exige condição jurídica ou fática particular do agente, como a condição de funcionário público no peculato ou de mãe no infanticídio.",
                    "**Crimes de Mão Própria ou de Atuação Pessoal**: exigem a execução material direta e intransferível pelo próprio agente (falso testemunho), não admitindo coautoria material.",
                    "**Crimes Unissubjetivos ou Monossubjetivos**: podem ser perpetrados por um único indivíduo isoladamente, embora admitam o concurso eventual de agentes.",
                    "**Crimes Plurissubjetivos ou de Concurso Necessário**: a tipificação exige a união compulsória de uma pluralidade de pessoas (associação criminosa, rixa).",
                    "**Crimes Unissubsistentes**: a conduta é realizada em um ato corporal único indivisível (injúria verbal), não comportando a figura da tentativa.",
                    "**Crimes Plurissubsistentes**: a conduta é fragmentável em múltiplos atos executórios sequenciais, admitindo plenamente o fracionamento executório e o conatus.",
                    "**Crimes Instantâneos**: a consumação exaure-se no instante da produção do resultado lesivo, sem perdurar ao longo do tempo.",
                    "**Crimes Permanentes**: o estado de consumação delitiva prolonga-se continuamente no tempo pela deliberação consciente do infrator (sequestro, cárcere privado).",
                    "**Crimes de Dano**: exigem lesão efetiva e demonstrada ao patrimônio jurídico do ofendido para a sua consumação típica.",
                    "**Crimes de Perigo Concreto e Abstrato**: perigo concreto exige comprovação fática do risco em juízo; perigo abstrato presume o perigo de forma legal absoluta.",
                    "**Crimes Vagos**: têm como sujeito passivo a coletividade indeterminada desprovida de personalidade jurídica personificada (crimes ambientais, saúde pública)."
                ],
                "teoria": [
                    {
                        "statement": "Nos crimes de mão própria, admite-se amplamente a coautoria funcional material entre indivíduos que planejem a conduta em conjunto.",
                        "isTrue": False,
                        "explanation": "Crimes de mão própria exigem execução física indelegável pelo próprio sujeito, repelindo coautoria (admitindo apenas participação moral)."
                    },
                    {
                        "statement": "Crimes unissubsistentes caracterizam-se pela impossibilidade fática de fracionamento do iter executório em múltiplos atos autônomos.",
                        "isTrue": True,
                        "explanation": "Na unissubsistência a execução perfaz-se em ato motor único, razão pela qual esses delitos não toleram a figura da tentativa."
                    },
                    {
                        "statement": "A prisão em flagrante em crimes permanentes pode ser realizada a qualquer momento enquanto durar a consumação do ilícito no tempo.",
                        "isTrue": True,
                        "explanation": "Nos termos do art. 303 do CPP, enquanto perdurar a permanência, o agente considera-se em flagrante delito permanente."
                    },
                    {
                        "statement": "Crimes de perigo abstrato impõem ao Ministério Público o dever de demonstrar pericialmente a probabilidade de dano iminente no processo penal.",
                        "isTrue": False,
                        "explanation": "No perigo abstrato ou presumido, a nocividade da conduta é presumida de forma absoluta pela lei, dispensando prova de perigo fático real."
                    }
                ],
                "revisao": [
                    {
                        "statement": "A infração penal classificada como crime vago possui como titular da tutela jurídica entidades personificadas da administração direta.",
                        "isTrue": False,
                        "explanation": "Crime vago é aquele em que o sujeito passivo é uma coletividade despersonalizada, como a família, a sociedade ou a paz pública."
                    },
                    {
                        "statement": "Crimes plurissubjetivos exigem compulsoriamente a concorrência de múltiplos agentes para a integração típica da figura incriminadora.",
                        "isTrue": True,
                        "explanation": "Nos crimes de concurso necessário, a pluralidade de pessoas integra a própria descrição típica elementar do delito."
                    },
                    {
                        "statement": "O crime próprio admite o concurso de agentes em regime de coautoria com particular desde que este conheça a condição funcional especial do autor.",
                        "isTrue": True,
                        "explanation": "Conforme o art. 30 do CP, a condição de funcionário público comunica-se ao comparsa se ingressou na sua esfera de conhecimento prévio."
                    },
                    {
                        "statement": "A consumação do crime instantâneo de efeitos permanentes prolonga-se voluntariamente no tempo por atuação ativa e ininterrupta do agente.",
                        "isTrue": False,
                        "explanation": "No crime instantâneo de efeitos permanentes a consumação ocorre de pronto, sendo apenas os efeitos materiais que perduram independentemente da ação do autor."
                    }
                ],
                "pointers": [
                    {"topic": "Crimes comuns, próprios e de mão própria", "pageRef": 30},
                    {"topic": "Crimes unissubjetivos e plurissubjetivos de concurso necessário", "pageRef": 32},
                    {"topic": "Crimes unissubsistentes e plurissubsistentes e tentativa", "pageRef": 34},
                    {"topic": "Crimes de perigo abstrato, perigo concreto e crimes vagos", "pageRef": 36}
                ]
            }
        },
        {
            "id": "direito-penal/a02/s05",
            "bizu": {
                "summary": [
                    "**Dolo Direto de 1º Grau**: a vontade livre e consciente do autor volta-se diretamente à obtenção do resultado delituoso pretendido.",
                    "**Dolo Direto de 2º Grau ou de Consequências Necessárias**: abrange os efeitos colaterais inevitáveis e certos gerados como consequência necessária do meio empregado.",
                    "**Dolo Eventual**: o indivíduo não busca diretamente o resultado lesivo, mas prevê a sua plausibilidade e assume expressamente o risco de produzi-lo.",
                    "**Teoria do Consentimento ou Assunção**: expressamente acolhida no artigo 18, inciso I, do Código Penal para tipificar o dolo eventual ao lado do dolo direto.",
                    "**Dolo Alternativo**: o autor dirige sua conduta com intenção indiferente em relação a dois ou mais resultados lesivos possíveis ou em relação a duas vítimas.",
                    "**Crime Culposo (art. 18, II)**: ocorre quando o indivíduo dá causa ao resultado por imprudência, negligência ou imperícia na condução de sua atividade.",
                    "**Elementos Estruturantes da Culpa**: conduta humana voluntária, inobservância do dever objetivo de cuidado, resultado involuntário, nexo causal, previsibilidade objetiva e tipicidade estrita.",
                    "**Modalidades de Culpa**: imprudência (ação açodada perigosa sem cautela), negligência (omissão descuidada antes da ação) e imperícia (falta de aptidão técnica profissional).",
                    "**Culpa Consciente**: o sujeito antevê mentalmente a possibilidade do resultado danoso, mas confia sinceramente em suas habilidades para evitá-lo.",
                    "**Culpa Inconsciente**: a possibilidade do resultado lesivo era objetivamente previsível pelo homem comum, mas o agente não a vislumbra no momento do fato.",
                    "**Culpa Imprópria ou por Extensão**: o agente atua com dolo real sob falsa percepção da realidade provocada por erro inescusável sobre descriminante putativa, sendo punido a título de culpa.",
                    "**Inadmissibilidade de Compensação de Culpas**: no direito penal brasileiro é descabida a compensação de culpas recíprocas entre a vítima e o causador do ilícito."
                ],
                "teoria": [
                    {
                        "statement": "No dolo eventual, o agente realiza a conduta visando diretamente a morte da vítima como meta primária exclusiva de sua ação delituosa.",
                        "isTrue": False,
                        "explanation": "No dolo eventual o resultado primário é previsto, mas o agente não busca diretamente a sua produção, limitando-se a consentir no risco."
                    },
                    {
                        "statement": "O dolo de segundo grau alcança os efeitos lesivos acessórios que o sujeito sabe serem consequências inevitáveis do meio utilizado para atingir seu fim.",
                        "isTrue": True,
                        "explanation": "O dolo de consequências necessárias abrange danos colaterais tidos pelo autor como certos e indissociáveis do meio de execução eleito."
                    },
                    {
                        "statement": "A compensação de culpas entre o infrator e a vítima imprudente opera no direito criminal como causa de extinção da punibilidade estatal.",
                        "isTrue": False,
                        "explanation": "No direito penal vigora a incomunicabilidade e a não compensação de culpas, subsistindo a responsabilidade do autor do crime culposo."
                    },
                    {
                        "statement": "Na culpa consciente, o sujeito antevê o risco do evento, mas acredita legitimamente ser capaz de evitar a consumação do dano.",
                        "isTrue": True,
                        "explanation": "A culpa consciente distingue-se do dolo eventual porque nela o agente confia sinceramente que o perigo não se converterá em dano."
                    }
                ],
                "revisao": [
                    {
                        "statement": "A imperícia manifesta-se pela inaptidão técnica ou desrespeito a regras elementares de arte ou profissão regulamentada exercida pelo indivíduo.",
                        "isTrue": True,
                        "explanation": "A imperícia reside na ausência de conhecimentos técnicos teóricos ou práticos essenciais para o exercício de determinada profissão."
                    },
                    {
                        "statement": "A punição a título culposo prescinde de previsão normativa expressa no tipo incriminador em razão da teoria geral da equivalência.",
                        "isTrue": False,
                        "explanation": "O parágrafo único do art. 18 consagra a excepcionalidade do crime culposo, exigindo previsão tipificada explícita na lei penal."
                    },
                    {
                        "statement": "O Código Penal acolheu taxativamente no artigo 18 a teoria da representação pura para fundamentar a tipificação do dolo eventual.",
                        "isTrue": False,
                        "explanation": "O Código Penal adotou a teoria da assunção ou do assentimento para o dolo eventual, exigindo anuência interior com o resultado previsto."
                    },
                    {
                        "statement": "A culpa imprópria caracteriza-se por uma conduta originariamente dolosa decorrente de erro evitável do sujeito sobre justificativa penal.",
                        "isTrue": True,
                        "explanation": "Trata-se de hipótese em que o indivíduo atua deliberadamente desejando o resultado fático em virtude de erro inescusável de tipo permissivo."
                    }
                ],
                "pointers": [
                    {"topic": "Dolo direto de 1º e 2º grau e consequências necessárias", "pageRef": 40},
                    {"topic": "Dolo eventual versus culpa consciente e teoria da assunção", "pageRef": 42},
                    {"topic": "Elementos do crime culposo e modalidades de culpa", "pageRef": 44},
                    {"topic": "Culpa imprópria e vedação à compensação de culpas", "pageRef": 46}
                ]
            }
        },
        {
            "id": "direito-penal/a02/s06",
            "bizu": {
                "summary": [
                    "**Crime Preterdoloso**: delito complexo marcado pela coexistência de dolo na conduta antecedente e culpa restrita no resultado agravador superveniente.",
                    "**Exemplo Clássico do Preterdolo**: lesão corporal seguida de morte (artigo 129, § 3º), em que o agressor quer lesionar, mas provoca a morte culposamente.",
                    "**Iter Criminis**: itinerário temporal de desenvolvimento do delito composto por cogitação, preparação, atos executórios, consumação e eventual exaurimento.",
                    "**Cogitação e Atos Preparatórios**: a cogitação é estritamente interna e impunível; os atos de preparação externa são impuníveis, ressalvada tipificação autônoma em lei.",
                    "**Início da Execução (Critério Objetivo-Individual)**: inicia-se a execução quando o indivíduo pratica atos que, segundo seu plano concreto, são imediatamente anteriores à realização do verbo típico.",
                    "**Consumação do Delito (art. 14, I)**: ocorre quando nele se reúnem todos os elementos descritos na definição legal da figura incriminadora.",
                    "**Conceito de Tentativa (art. 14, II)**: dá-se quando, iniciada a execução, a consumação não se produz por circunstâncias inteiramente alheias à vontade do agente.",
                    "**Sanção da Tentativa**: o parágrafo único do art. 14 determina a aplicação da pena do crime consumado diminuída de um a dois terços, segundo o iter percorrido.",
                    "**Tentativa Cruenta e Branca**: cruenta (ou vermelha) quando o objeto material é atingido sofrendo lesão corporal; incruenta (ou branca) quando a vítima não é atingida.",
                    "**Tentativa Perfeita e Imperfeita**: perfeita (ou acabada/crime falho) quando o autor esgota todos os meios executórios; imperfeita quando a execução é interrompida no curso.",
                    "**Crimes que Não Admitem Tentativa**: crimes culposos reais, preterdolosos, unissubsistentes, omissivos puros, contravenções penais e crimes habituais.",
                    "**Exaurimento Delitivo**: fatos posteriores à consumação que não alteram a existência do crime, atuando apenas como circunstância judicial de dosimetria da pena."
                ],
                "teoria": [
                    {
                        "statement": "No crime preterdoloso, o indivíduo atua impulsionado por culpa estrita na conduta inicial, sobrevindo resultado danoso voluntariamente desejado a título de dolo.",
                        "isTrue": False,
                        "explanation": "A estrutura preterdolosa exige dolo na conduta antecedente e culpa estrita no resultado mais gravoso subsequente (dolo no antecedente, culpa no consequente)."
                    },
                    {
                        "statement": "A mera idealização mental do delito e os atos puramente preparatórios são impuníveis de forma absoluta no ordenamento repressivo brasileiro.",
                        "isTrue": False,
                        "explanation": "A cogitação é sempre impunível, mas os atos preparatórios podem ser excepcionalmente punidos se erigidos a crimes autônomos pelo legislador (ex.: posse de petrechos)."
                    },
                    {
                        "statement": "A diminuição de pena cominada à tentativa vincula-se ao critério da proximidade temporal e material da consumação alcançada pelo agente.",
                        "isTrue": True,
                        "explanation": "Quanto mais perto o autor chegar da consumação do delito, menor será a diminuição da reprimenda, que varia entre um e dois terços."
                    },
                    {
                        "statement": "Os crimes unissubsistentes admitem conatus quando a execução física da conduta puder ser comprovada por testemunhas oculares.",
                        "isTrue": False,
                        "explanation": "Nos crimes unissubsistentes a execução consolida-se em ato motor indivisível, inexistindo fracionamento material que viabilize a tentativa."
                    }
                ],
                "revisao": [
                    {
                        "statement": "Chama-se tentativa incruenta ou branca aquela em que o agressor dispara projéteis sem lograr ferir a integridade física da vítima visada.",
                        "isTrue": True,
                        "explanation": "A tentativa diz-se incruenta ou branca quando a vítima não sofre qualquer tipo de lesão física ou ofensa corporal concreta."
                    },
                    {
                        "statement": "O exaurimento de um delito contra a administração pública impede o reconhecimento de sua consumação jurídica formal antecedente.",
                        "isTrue": False,
                        "explanation": "O exaurimento traduz mero desdobramento posterior de delito formal já plenamente consumado, operando na dosimetria da pena."
                    },
                    {
                        "statement": "A consumação de crime material aperfeiçoa-se unicamente com a produção efetiva da modificação espacial externa prevista na norma.",
                        "isTrue": True,
                        "explanation": "Nos crimes materiais a tipicidade consumativa requer a convergência de todos os elementos típicos com a produção do resultado naturalístico."
                    },
                    {
                        "statement": "As contravenções penais admitem a punição da tentativa com redução sancionatória obrigatória de metade do teto cominado.",
                        "isTrue": False,
                        "explanation": "O art. 4º da Lei de Contravenções Penais estabelece de modo peremptório que não é punível a tentativa de contravenção."
                    }
                ],
                "pointers": [
                    {"topic": "Estrutura dogmática do crime preterdoloso", "pageRef": 48},
                    {"topic": "Fases do iter criminis e critério de início executório", "pageRef": 50},
                    {"topic": "Tentativa, critérios de punição e redução fracionária", "pageRef": 52},
                    {"topic": "Espécies de tentativa e hipóteses em que o conatus é inadmissível", "pageRef": 54}
                ]
            }
        },
        {
            "id": "direito-penal/a02/s07",
            "bizu": {
                "summary": [
                    "**Desistência Voluntária (art. 15, 1ª parte)**: o indivíduo interrompe voluntariamente a execução antes de esgotar seus meios executórios (*posso prosseguir, mas não quero*).",
                    "**Arrependimento Eficaz (art. 15, 2ª parte)**: o indivíduo esgota os atos executórios, mas adota providências concretas que impedem com sucesso a produção do resultado letal.",
                    "**Efeito do Artigo 15 (Ponte de Ouro)**: opera a exclusão da tipicidade da tentativa originária, respondendo o agente exclusivamente pelos atos lesivos já praticados.",
                    "**Fórmula de Frank**: se eu posso prosseguir, mas não quero, há desistência voluntária; se eu quero prosseguir, mas não posso por fatores externos, há tentativa.",
                    "**Arrependimento Posterior (art. 16 - Ponte de Prata)**: causa legal obrigatória de diminuição de pena aplicável a crimes cometidos sem violência ou grave ameaça à pessoa.",
                    "**Requisitos do Arrependimento Posterior**: crime sem violência/ameaça pessoal, reparação integral do dano ou restituição da coisa, voluntariedade e ato realizado até o recebimento da denúncia ou queixa.",
                    "**Fração do Arrependimento Posterior**: a redução da pena privativa de liberdade varia de um a dois terços, calibrada pela celeridade e integralidade do ressarcimento.",
                    "**Crime Impossível (art. 17 - Quase-Crime)**: verifica-se a total impunibilidade do conatus quando o instrumento escolhido revela-se desprovido de qualquer eficácia material ou o bem visado é absolutamente inadequado.",
                    "**Ineficácia e Impropriedade Absolutas**: ineficácia absoluta (revólver totalmente inapto a disparar ou veneno inócuo); impropriedade absoluta (desferir tiros em cadáver já sepultado).",
                    "**Teoria Objetiva Temperada**: acolhida pelo Código Penal, exige que a ineficácia ou impropriedade sejam absolutas; se forem relativas, haverá tentativa punível.",
                    "**Súmula 145 do STF (Flagrante Provocado)**: não há crime quando a preparação do flagrante pela polícia torna impossível a sua consumação (flagrante preparado).",
                    "**Súmula 567 do STJ (Segurança Eletrônica)**: a presença de sistema eletrônico de vigilância ou de monitoramento por seguranças não torna o furto crime impossível."
                ],
                "teoria": [
                    {
                        "statement": "Na desistência voluntária, o agente interrompe a execução delitiva por deliberação própria, respondendo penalmente unicamente pelos atos que consumou até então.",
                        "isTrue": True,
                        "explanation": "O art. 15 do CP estipula que na desistência o autor só responde pelos atos já praticados, afastando a imputação da tentativa originária."
                    },
                    {
                        "statement": "O arrependimento posterior autoriza a redução da reprimenda penal mesmo que a reparação integral do patrimônio ocorra após a prolação da sentença.",
                        "isTrue": False,
                        "explanation": "O benefício do art. 16 exige peremptoriamente que a reparação ou restituição do bem ocorra até o recebimento formal da denúncia ou queixa."
                    },
                    {
                        "statement": "A ineficácia relativa do instrumento empregado na empreitada delitiva é suficiente para configurar a excludente de crime impossível.",
                        "isTrue": False,
                        "explanation": "O ordenamento penal acolheu a teoria objetiva temperada, exigindo que a ineficácia do meio ou impropriedade do objeto sejam absolutas para afastar o crime."
                    },
                    {
                        "statement": "A Súmula 567 do STJ pacificou que a instalação de circuitos internos de câmeras em estabelecimentos comerciais descaracteriza a tentativa de furto.",
                        "isTrue": False,
                        "explanation": "Conforme a Súmula 567 do STJ, sistema de vigilância eletrônica ou monitoramento por seguranças em lojas não inviabiliza o furto nem gera crime impossível."
                    }
                ],
                "revisao": [
                    {
                        "statement": "A fórmula clássica formulada por Frank estabelece que se o infrator pode prosseguir na execução, mas voluntariamente não quer, configura-se desistência voluntária.",
                        "isTrue": True,
                        "explanation": "A máxima de Frank diferencia com exatidão a desistência voluntária ('posso prosseguir, mas não quero') da tentativa ('quero prosseguir, mas não posso')."
                    },
                    {
                        "statement": "No arrependimento posterior, a espontaneidade do infrator é exigência indeclinável para a concessão da causa de diminuição de pena.",
                        "isTrue": False,
                        "explanation": "O art. 16 exige voluntariedade, não exigindo espontaneidade; o ato pode decorrer de conselho ou sugestão de terceiros, desde que sem coação."
                    },
                    {
                        "statement": "O flagrante preparado pela autoridade policial induzindo à prática do fato sem risco concreto de consumação enseja hipótese de crime impossível.",
                        "isTrue": True,
                        "explanation": "A Súmula 145 do STF estabelece que não há crime quando a armação policial torna de antemão impossível a consumação delitiva."
                    },
                    {
                        "statement": "O arrependimento eficaz exige que a intervenção do autor logre evitar com sucesso a produção do resultado naturalístico lesivo final.",
                        "isTrue": True,
                        "explanation": "Para beneficiar-se da ponte de ouro, a atuação do infrator deve ser efetiva, impedindo com eficácia a ocorrência da consumação do delito."
                    }
                ],
                "pointers": [
                    {"topic": "Desistência voluntária, arrependimento eficaz e fórmula de Frank", "pageRef": 57},
                    {"topic": "Arrependimento posterior e requisitos do artigo 16", "pageRef": 59},
                    {"topic": "Crime impossível e teoria objetiva temperada no artigo 17", "pageRef": 61},
                    {"topic": "Jurisprudência sumulada: Súmula 145 do STF e Súmula 567 do STJ", "pageRef": 63}
                ]
            }
        },
        {
            "id": "direito-penal/a02/s08",
            "bizu": {
                "summary": [
                    "**Ilicitude ou Antijuridicidade**: contradição entre a conduta típica e o conjunto normativo protetivo da ordem jurídica, presumida relativamente pelo fato típico.",
                    "**Excludentes Legais Gerais (art. 23 do CP)**: estado de necessidade, legítima defesa, estrito cumprimento de dever legal e exercício regular de direito.",
                    "**Estado de Necessidade (art. 24)**: praticado para salvar de perigo atual bem jurídico próprio ou alheio, que o agente não provocou voluntariamente nem tinha o dever legal de enfrentar.",
                    "**Requisitos do Estado de Necessidade**: perigo atual, não causação voluntária do perigo, ameaça a direito próprio ou alheio, inexistência de dever legal de enfrentar o risco e proporcionalidade.",
                    "**Dever Legal de Enfrentar o Perigo**: não pode alegar estado de necessidade quem detém obrigação normativa legal de enfrentar o perigo (bombeiros, policiais no exercício das funções).",
                    "**Legítima Defesa (art. 25)**: uso moderado dos meios necessários para repelir injusta agressão, atual ou iminente, a direito próprio ou de outrem.",
                    "**Requisitos da Legítima Defesa**: agressão humana injusta, agressão atual ou iminente, tutela de direito próprio ou de terceiro, utilização comedida dos meios e animus defendendi.",
                    "**Legítima Defesa Real e Putativa**: legítima defesa real contra legítima defesa real é inadmissível; admite-se legítima defesa real contra agressão decorrente de legítima defesa putativa.",
                    "**Inadmissibilidade da Defesa da Honra (ADPF 779 do STF)**: a tese de legítima defesa da honra foi declarada inconstitucional pelo STF em crimes de feminicídio.",
                    "**Estrito Cumprimento de Dever Legal**: praticado por funcionário público ou particular no desempenho de determinação imposta cogentemente por lei ou norma legal.",
                    "**Exercício Regular de Direito**: atuação amparada pelo ordenamento que autoriza o exercício de prerrogativa (intervenções médico-cirúrgicas autorizadas, desportos com violência consentida).",
                    "**Excesso Punível (art. 23, parágrafo único)**: o agente responderá pelo excesso doloso ou culposo cometido em qualquer das excludentes de ilicitude."
                ],
                "teoria": [
                    {
                        "statement": "O estado de necessidade autoriza que o agente sacrifique bem alheio diante de perigo iminente cuja concretização seja incerta no momento fático.",
                        "isTrue": False,
                        "explanation": "O art. 24 do Código Penal exige expressamente perigo atual; perigo iminente é elemento privativo da legítima defesa."
                    },
                    {
                        "statement": "O Supremo Tribunal Federal julgou inconstitucional a invocação da legítima defesa da honra para justificar delitos praticados contra a vida de mulheres.",
                        "isTrue": True,
                        "explanation": "Na ADPF 779, o STF declarou inconstitucional a tese da legítima defesa da honra por contrariar a dignidade da pessoa humana e a igualdade."
                    },
                    {
                        "statement": "O bombeiro militar investido na função de salvamento pode invocar estado de necessidade para recusar atendimento a sinistros com risco corporal elevado.",
                        "isTrue": False,
                        "explanation": "O art. 24, § 1º, do Código Penal afasta o estado de necessidade em favor daqueles sobre os quais recai imposição jurídica expressa de enfrentar a situação de risco."
                    },
                    {
                        "statement": "O excesso doloso na repulsa a uma agressão inicial afasta o caráter justificante do ato defensivo, respondendo o agente pelo dano excedente causado.",
                        "isTrue": True,
                        "explanation": "O parágrafo único do art. 23 comina responsabilidade penal pelo excesso doloso ou culposo verificado em qualquer causa excludente de ilicitude."
                    }
                ],
                "revisao": [
                    {
                        "statement": "É dogmaticamente admissível a existência de legítima defesa real recíproca entre dois indivíduos que se agridam simultaneamente com base na lei.",
                        "isTrue": False,
                        "explanation": "A legítima defesa pressupõe agressão injusta; logo, é impossível haver legítima defesa real simultânea contra quem também atua em legítima defesa legítima."
                    },
                    {
                        "statement": "A prática de intervenções cirúrgicas necessárias respaldadas pelo consentimento esclarecido do paciente configura exercício regular de direito.",
                        "isTrue": True,
                        "explanation": "Atos médicos curativos respaldados por consentimento enquadram-se na excludente de exercício regular de direito ou atipicidade conglobante."
                    },
                    {
                        "statement": "A legítima defesa putativa decorre de uma percepção equivocada da realidade em que o autor supõe falsamente estar sofrendo injusta agressão.",
                        "isTrue": True,
                        "explanation": "Na legítima defesa putativa o perigo só existe na mente do sujeito em razão de erro, aplicando-se as regras do erro sobre discriminante."
                    },
                    {
                        "statement": "No estado de necessidade justificante, admite-se o sacrifício de bem jurídico de valor sensivelmente superior ao bem que se pretendia salvar.",
                        "isTrue": False,
                        "explanation": "O estado de necessidade submete-se ao juízo de proporcionalidade e razoabilidade, não se justificando a destruição de bem manifestamente mais valioso."
                    }
                ],
                "pointers": [
                    {"topic": "Ilicitude, conceito e causas de justificação no artigo 23", "pageRef": 67},
                    {"topic": "Requisitos do estado de necessidade e dever legal de agir", "pageRef": 70},
                    {"topic": "Legítima defesa, moderação dos meios e ADPF 779 do STF", "pageRef": 73},
                    {"topic": "Estrito cumprimento de dever legal, exercício regular e excesso punível", "pageRef": 77}
                ]
            }
        }
    ]
}

# ---------------------------------------------------------
# SUMMARIES (a02)
# ---------------------------------------------------------
summaries_data = {
    "aula": "direito-penal/a02",
    "batch": "pcpe-summary-direito-penal",
    "status": "DRAFT",
    "segments": [
        {
            "id": "direito-penal/a02/s01",
            "fingerprint": get_fp("direito-penal/a02/s01"),
            "analytic": """Este segmento inaugura o estudo da Teoria Geral do Crime, examinando a estrutura tripartite do conceito analítico de infração penal, a evolução da conduta sob o prisma do finalismo welzeliano, as hipóteses excludentes de voluntariedade motora e a distinção dogmática entre crimes comissivos e omissivos.

### Conceito analítico de crime e o postulado finalista
A dogmática penal brasileira adota preponderantemente a teoria tripartida (ou tripartite) de crime, compreendendo-o analiticamente como **fato típico, ilícito (ou antijurídico) e culpável**. A culpabilidade consubstancia o juízo de reprovação pessoal que recai sobre o autor do fato ilícito, atuando como verdadeiro pressuposto de aplicação da pena.

A conceituação de conduta sofreu profunda transformação evolutiva:
- **Teoria Causal-Naturalista (Liszt-Beling)**: definia a conduta como mero movimento mecânico corporal que causava alteração sensorial no mundo exterior, desprovida de qualquer finalidade. O dolo e a culpa localizavam-se exclusivamente na culpabilidade.
- **Teoria Finalista (Hans Welzel)**: compreende a conduta como o comportamento humano, voluntário e consciente, dirigido a uma finalidade lícita ou ilícita. A intenção subjetiva integra a própria estrutura da conduta, razão pela qual o dolo e a culpa foram deslocados da culpabilidade para integrar o tipo penal incriminador.

### Causas de ausência de conduta
Por ser a voluntariedade consciente elemento indeclinável da ação humana, sua inexistência suprime a própria conduta, impedindo o nascimento do fato típico:
- **Coação Física Irresistível (*Vis Absoluta*)**: ocorre quando o indivíduo é transformado em mero instrumento material de força exercida por terceiro, inexistindo qualquer manifestação volitiva (ex.: agressor que segura forçadamente a mão de alguém contra o gatilho). Exclui a conduta e a tipicidade. Distingue-se da coação moral irresistível (*vis compulsiva*), que atua na psique da pessoa, preservando a conduta típica e afastando unicamente a culpabilidade.
- **Movimentos Reflexos Puros**: consubstanciam reações orgânicas meramente sensório-motoras provocadas por estímulos biológicos imediatos desprovidos de intervenção cortical consciente (espasmos musculares ou reflexos de dor).
- **Estados de Inconsciência Completa**: episódios neurológicos de supressão absoluta da atividade psíquica voluntária, tais como sonambulismo, crises epilépticas em crise de ausência e estados de hipnose profunda.

### Crimes comissivos e omissivos: a posição de garante
Quanto à forma de manifestação exterior da conduta, os tipos penais dividem-se em ações ativas e omissivas:
- **Crimes Comissivos**: perfazem-se mediante uma ação positiva contrária a preceito normativo de natureza proibitiva (*não matarás*, *não subtrairás*).
- **Crimes Omissivos Próprios ou Puros**: o tipo penal comina diretamente um mandamento de agir solidário (*artigo 135 do CP - omissão de socorro*). Consumam-se no instante exato da inércia do indivíduo perante a situação típica, sendo desnecessária a ocorrência de resultado naturalístico. Por serem de ato único e indivisível, não toleram conatus.
- **Crimes Omissivos Impróprios ou Comissivos por Omissão**: o tipo descreve formalmente um delito comissivo (ex.: homicídio), porém a lei impõe a determinadas pessoas a obrigação de agir para impedir o resultado lesivo.

Nos termos do artigo 13, § 2º, do Código Penal, a omissão é penalmente relevante quando o omitente detém o dever jurídico de impedir a consumação do evento danoso, decorrente de três fontes:
1. Tenha por determinação normativa explícita a incumbência de vigilância ou custódia (agentes de segurança em serviço, genitores quanto aos filhos incapazes);
2. Haja assumido por relação voluntária prévia o encargo material de salvaguardar o bem tutelado (socorrista particular, monitor contratado de recreação);
3. Haja originado com ato antecedente pessoal a situação fática de risco iminente de dano (quem arremessa inadvertidamente outrem em águas profundas).

### Para fixar
- O conceito analítico de crime estrutura-se no trinômio fato típico, antijurídico e culpável.
- A teoria finalista concebe a conduta como ação voluntária orientada a uma finalidade específica.
- O dolo e a culpa integram a conduta no fato típico, deixando a culpabilidade como juízo de reprovação.
- A coação física irresistível (*vis absoluta*) exclui a conduta, enquanto a coação moral afasta a culpabilidade.
- Atos reflexos genuínos e sonambulismo suprimem a voluntariedade e descaracterizam a conduta.
- Os crimes omissivos próprios independem de resultado fático e não admitem tentativa.
- Os crimes omissivos impróprios exigem a presença de um garantidor com dever legal ou assumido de proteção.
- O garantidor responde pelo resultado consumado caso possua capacidade física real de intervir.""",
            "synthetic": [
                "**Conceito Tripartido**: a doutrina clássica sedimentou que o crime é composto por fato típico, antijurídico e culpável, sendo esta pressuposto de pena.",
                "**Teoria Finalista**: define conduta como atividade humana deliberada e voluntária guiada a um fim, situando o dolo e a culpa no tipo penal.",
                "**Exclusão da Conduta**: a coação física irresistível, o sono fisiológico e os atos reflexos puros suprimem a vontade, afastando a tipicidade.",
                "**Vis Compulsiva**: a coação moral irresistível não extirpa a conduta nem o fato típico, operando a isenção de pena no campo da culpabilidade.",
                "**Omissivos Próprios**: caracterizam-se pela violação de mandamento de agir prescindindo de resultado sensorial posterior, não comportando a tentativa.",
                "**Garantidor do Artigo 13, § 2º**: responde pelo resultado comissivo aquele que por lei, contrato ou conduta precedente perigosa detinha o dever de custódia.",
                "**Omissivos Impróprios**: admitem o conatus por serem plurissubsistentes e exigem aptidão física real para atuar sem colocar em perigo o omitente."
            ]
        },
        {
            "id": "direito-penal/a02/s02",
            "fingerprint": get_fp("direito-penal/a02/s02"),
            "analytic": """Este segmento aborda a disciplina do resultado naturalístico nas espécies delitivas e o regime jurídico do nexo de causalidade, detalhando a teoria da equivalência das condições, o método de eliminação de Thyrén e a superveniência de concausas autônomas.

### Resultado naturalístico e classificação dos crimes
O resultado jurídico (lesão ou ameaça ao interesse normativamente protegido) encontra-se presente em qualquer espécie delitiva. Todavia, o resultado naturalístico consubstancia a alteração sensorial, biológica ou física desencadeada no mundo concreto.

Sob a perspectiva da exigência de resultado naturalístico, os tipos penais subdividem-se em três categorias estruturais:
- **Crimes Materiais ou de Resultado**: a redação legal prevê a conduta e descreve expressamente o resultado exterior, exigindo sua efetiva produção física para que ocorra a consumação típica (*artigo 121 - matar alguém; artigo 155 - subtrair coisa*).
- **Crimes Formais ou de Consumação Antecipada**: a norma comina conduta e descreve um resultado naturalístico futuro, porém a consumação ocorre de pronto com a execução da conduta, sendo a obtenção do evento mero exaurimento (*artigo 159 - extorsão mediante sequestro; artigo 317 - corrupção passiva*).
- **Crimes de Mera Conduta ou de Simples Atividade**: a lei incrimina estritamente um comportamento humano positivo ou omissivo sem sequer descrever qualquer alteração espacial empírica posterior (*artigo 150 - violação de domicílio; porte ilegal de arma de fogo*).

### Nexo de causalidade e Teoria da Equivalência (*Conditio Sine Qua Non*)
O nexo causal constitui o liame físico que interliga a conduta exteriorizada pelo agente ao resultado proibido superveniente. O caput do artigo 13 do Código Penal consagrou a **Teoria da Equivalência dos Antecedentes Causais** (*conditio sine qua non*): a imputação objetiva do evento lesivo vincula-se a quem tenha concorrido para a sua deflagração física, reputando-se causa qualquer comportamento comissivo ou abstentivo sem o qual a mutação fática não se teria consumado.

Para aferir a pertinência causal de uma ação, a dogmática socorre-se do **Método Hipotético de Eliminação de Thyrén**: realiza-se a supressão mental e abstrata do comportamento praticado; se o resultado lesivo final deixar de produzir-se na forma e no tempo em que ocorreu, tal conduta consubstancia causa; se o evento permaneceria inalterado, a ação não atua como elo causal.

Para evitar o regressus ad infinitum da causalidade meramente naturalística, o ordenamento jurídico utiliza o dolo e a culpa no plano da tipicidade como freio ordenador da responsabilidade penal.

### Regime das concausas e a causalidade autônoma (art. 13, § 1º)
Concausa é a concorrência de múltiplos fatores causais paralelos que contribuem para o desfecho do evento danoso:
1. **Concausas Absolutamente Independentes**: possuem origem desconectada da conduta do agente e operam sozinhas o evento lesivo (sejam preexistentes, concomitantes ou supervenientes). O nexo causal originário resta rompido: o agente responde apenas pela tentativa de homicídio se a vítima falece por veneno ingerido antes ou por desabamento concomitante do teto.
2. **Concausas Relativamente Independentes**: derivam ou conjugam-se com a ação desencadeada pelo autor:
   - *Preexistentes ou Concomitantes*: não rompem o liame de imputação causal. Se a vítima for portadora de hemofilia preexistente ou sofrer infarto no curso da agressão física, o agressor responde pelo resultado morte consumado, desde que previsível a título doloso ou culposo.
   - *Supervenientes*: submetem-se ao comando mitigador do artigo 13, § 1º, do Código Penal.

O artigo 13, § 1º, preceitua que a superveniência de concausa relativamente independente desautoriza a imputação do desfecho final caso inaugure desdobramento causal autônomo, atribuindo-se ao agente originário unicamente os episódios executivos que antecederam o evento superveniente. Acolheu-se nessa hipótese excepcional a teoria da causalidade adequada.

Assim, se o ferido transportado em viatura de resgate hospitalar falece decorrente do tombamento do veículo na estrada, essa causa externa inaugura uma linha causal autônoma desvinculada do perigo direto do tiro, respondendo o atirador apenas pela tentativa de homicídio. Todavia, complicações médicas previsíveis advindas da cirurgia necessária mantêm íntegra a responsabilidade do autor pelo delito consumado.

### Para fixar
- Os crimes materiais condicionam a consumação à produção fática do resultado naturalístico.
- Nos crimes formais o resultado naturalístico é dispensável para a ocorrência da consumação típica.
- Os crimes de mera conduta limitam-se a reprimir uma atividade fática pura sem resultado destacável.
- O nexo causal apoia-se no critério da conditio sine qua non amparado pelo juízo de eliminação hipotética.
- O dolo e a culpa operam como freio dogmático contra o regresso ao infinito causal.
- Causas absolutamente independentes desvinculam o resultado e restringem a punição aos atos tentados.
- Concausas relativamente independentes prévias ou concomitantes não afastam a imputação do resultado.
- A causa superveniente autônoma exclui o evento final, remanescendo punição por atos antecedentes (art. 13, § 1º).""",
            "synthetic": [
                "**Classificação Tripartida**: crimes materiais exigem resultado físico, formais consumam-se com a conduta sendo o evento exaurimento, e mera conduta inexiste evento externo.",
                "**Teoria da Conditio Sine Qua Non**: reputa-se causa necessária toda ação sem a qual o evento concreto lesivo não teria se verificado na realidade fenomênica.",
                "**Juízo Hipotético de Thyrén**: método analítico mental que suprime a conduta para verificar se o evento persistiria inalterado na linha do tempo.",
                "**Concausas Absolutas**: atuam com total independência causal, afastando a imputação do resultado letal e ensejando condenação unicamente por tentativa.",
                "**Concausas Relativas Anteriores**: unem-se à conduta do agressor sem quebrar o nexo causal físico, respondendo o infrator pelo resultado lesivo consumado.",
                "**Superveniência Autônoma (art. 13, § 1º)**: a concausa que inaugura linha de causalidade própria afasta o resultado final, sancionando apenas os fatos anteriores.",
                "**Desdobramento da Lesão**: intercorrências médicas hospitalares decorrentes diretamente do atendimento curativo não rompem o nexo de imputação penal."
            ]
        },
        {
            "id": "direito-penal/a02/s03",
            "fingerprint": get_fp("direito-penal/a02/s03"),
            "analytic": """Este segmento aprofunda a dogmática da tipicidade penal, abordando a distinção indispensável entre tipicidade formal e material, o postulado da tipicidade conglobante, a classificação dos elementos estruturantes do tipo penal e as hipóteses de atipicidade.

### Tipicidade formal, tipicidade material e tipicidade conglobante
A evolução do pensamento penal superou a concepção de que o tipo penal constituía mera descrição estéril de palavras. A tipicidade penal contemporânea consubstancia um juízo complexo bipartido:
- **Tipicidade Formal**: reside na perfeita subsunção lógica e mecânica entre o comportamento empírico verificado na realidade e a hipótese abstrata positivada no preceito primário da lei incriminadora.
- **Tipicidade Material**: exige que a conduta externa cause dano efetivo, grave e socialmente intolerável ao bem jurídico tutelado. Ações que geram lesão absolutamente inexpressiva revelam-se materialmente atípicas, ainda que formalmente se amoldem ao texto legal.

A doutrina moderna, notadamente com a formulação da **Tipicidade Conglobante** de Eugenio Raúl Zaffaroni, aperfeiçoou esse modelo. Para essa vertente, a tipicidade conglobante compõe-se da conjugação da tipicidade material com a **antinormatividade**.

A conduta não pode ser considerada típica se o ordenamento jurídico considerado em sua globalidade (direito processual, civil, administrativo) fomenta, impõe ou autoriza expressamente a conduta (como a intervenção cirúrgica curativa consentida ou o estrito cumprimento de mandado de prisão por oficial de justiça).

### Elementos estruturais e funções do tipo penal
O preceito primário do tipo incriminador é construído a partir de diferentes categorias elementares:
- **Elementos Objetivos Descritivos**: termos de fácil apreensão empírica sensorial pelo homem comum, sem necessidade de apreciação axiológica prévia (*matar, coisa alheia móvel, mulher, arma*).
- **Elementos Objetivos Normativos**: exigem um juízo analítico de valor emitido pelo aplicador da lei, desdobrando-se em normativos jurídicos (*documento, funcionário público, duplicata simulada*) ou normativos culturais (*ato obsceno, decoro, reputação*).
- **Elementos Subjetivos do Tipo**: intenções anímicas especiais que qualificam a vontade delitiva, outrora denominadas dolo específico (*com o fim de obter vantagem patrimonial; para satisfazer interesse próprio*).

No sistema criminal, o tipo penal cumpre três funções axiais:
1. *Função de Garantia*: salvaguarda a esfera de liberdade dos indivíduos contra arbítrios judiciais (reserva legal);
2. *Função Indiciária da Ilicitude (*Ratio Cognoscendi*)*: a presença da tipicidade faz presumir que o fato é antijurídico, presunção relativa que subsiste até a demonstração de uma causa de justificação;
3. *Função Fundamentadora*: alicerça a legitimidade de intervenção repressiva do poder estatal.

### Causas de exclusão da tipicidade penal
A integridade da tipicidade pode ser afastada na constatação das seguintes hipóteses jurídicas:
- **Coação Física Irresistível**: aniquila a própria voluntariedade corporal da conduta, excluindo o primeiro substrato do fato típico;
- **Erro de Tipo Essencial Inevitável (artigo 20, caput)**: a falsa percepção da realidade sobre dado elementar do tipo fático afasta inexoravelmente o dolo e a culpa;
- **Princípio da Insignificância**: descaracteriza a tipicidade material em virtude da irrisoriedade do prejuízo patrimonial gerado pela conduta;
- **Adequação Social**: condutas integradas aos padrões consuetudinários pacíficos da comunidade não possuem densidade ofensiva material, ressalvada a vedação da Súmula 502 do STJ para mídias clandestinas piratas.

### Para fixar
- A tipicidade divide-se em formal (subsunção à lei) e material (lesão intolerável ao bem jurídico).
- A tipicidade conglobante exige simultaneamente lesividade substancial e antinormatividade jurídica global.
- Elementos normativos do tipo demandam valoração jurídica ou axiológica para a elucidação do comando.
- Elementos subjetivos especiais traduzem a finalidade anímica específica requerida pela figura típica.
- A função indiciária do tipo penal estabelece presunção relativa de ilicitude do comportamento examinado.
- A coação física absoluta elimina a conduta voluntária e descaracteriza a tipicidade formal.
- O erro de tipo inevitável exclui o dolo e a culpa do agente na execução da conduta.
- O princípio da bagatela opera o descarte da tipicidade material sem comprometer a tipicidade formal.""",
            "synthetic": [
                "**Tipicidade Bipartida**: compõe-se da conformação formal à letra do preceito legal e da lesão substancial intolerável exigida pela tipicidade material.",
                "**Tipicidade Conglobante**: pressupõe a união da tipicidade material com a antinormatividade de conduta não tolerada pelo ordenamento jurídico em bloco.",
                "**Elementos Normativos**: são núcleos conceituais que demandam valoração jurídica axiológica integradora prévia por parte do intérprete criminal.",
                "**Elementos Subjetivos Especiais**: expressam propósitos anímicos específicos indispensáveis para a configuração estrita do ilícito delineado em lei.",
                "**Função Indiciária**: consagra que todo fato formalmente típico atua como indício presumido de antijuridicidade na ausência de causas justificantes.",
                "**Exclusão por Erro de Tipo**: o engano invencível sobre elementares do tipo fático extirpa o dolo e impede a caracterização da modalidade culposa.",
                "**Exclusão da Tipicidade Material**: a incidência da bagatela própria afasta a relevância punitiva preservando apenas o enquadramento formal."
            ]
        },
        {
            "id": "direito-penal/a02/s04",
            "fingerprint": get_fp("direito-penal/a02/s04"),
            "analytic": """Este segmento aborda a classificação dogmática dos crimes no direito penal brasileiro, analisando as distinções relativas à qualidade dos sujeitos, à estrutura do iter executório, à permanência temporal e aos graus de ofensividade.

### Classificação quanto aos sujeitos do delito
A exigência de qualificações especiais do autor orienta uma das principais divisões dos tipos penais:
- **Crimes Comuns**: podem ser perpetrados por qualquer pessoa imputável, pois a figura incriminadora não exige predicamento fático ou jurídico particular do sujeito ativo (*artigo 121 - homicídio; artigo 155 - furto*).
- **Crimes Próprios ou Especiais**: a tipificação exige qualidade jurídica funcional ou condição pessoal específica do autor (*peculato exige funcionário público; infanticídio exige o estado puerperal da genitora*). Admitem a coautoria ou participação com terceiro particular, desde que este conheça a condição elementar especial do comparsa (artigo 30 do CP).
- **Crimes de Mão Própria ou de Atuação Pessoal**: a conduta só pode ser executada física e pessoalmente pelo indivíduo indicado no tipo (*falso testemunho, autoaborto*). Por serem de execução personalíssima e indelegável, não admitem coautoria material, sendo admissível apenas a participação moral por induzimento ou instigação.

Quanto à quantidade de participantes:
- **Crimes Unissubjetivos (Monossubjetivos)**: podem ser praticados por um único sujeito, admitindo o concurso eventual de comparsas.
- **Crimes Plurissubjetivos (Concurso Necessário)**: a norma penal exige compulsoriamente a conduta convergente de múltiplas pessoas (*artigo 288 - associação criminosa; artigo 137 - rixa*).

### Classificação quanto à execução e à temporalidade
A fragmentação da conduta no tempo e no espaço gera repercussões diretas sobre o cabimento da tentativa e do flagrante:
- **Crimes Unissubsistentes**: a fase de execução esgota-se em um ato corporal único e indivisível (*injúria verbal instantânea*). Em razão dessa unicidade física de execução, não admitem tentativa.
- **Crimes Plurissubsistentes**: a conduta executória é cindível em múltiplos atos materiais sucessivos (*escrever e enviar carta extorsiva*). Admitem perfeitamente o fracionamento executório e o reconhecimento da tentativa.

Quanto ao momento da consumação:
- **Crimes Instantâneos**: a consumação perfaz-se e encerra-se em momento temporal preciso (*homicídio, furto*).
- **Crimes Permanentes**: a consumação protrai-se voluntariamente no tempo enquanto o agente mantiver o bem jurídico sob seu jugo (*sequestro, cárcere privado, depósito de entorpecentes*). A prisão em flagrante é cabível a qualquer instante durante a permanência (artigo 303 do CPP).
- **Crimes Instantâneos de Efeitos Permanentes**: a consumação exaure-se de imediato, mas os efeitos lesivos subsistem no tempo independentemente da vontade do autor (*bigamia, homicídio*).

### Classificação quanto à ofensividade e sujeitos passivos
Quanto à exigência de dano ou exposição a risco:
- **Crimes de Dano**: demandam efetiva e comprovada lesão prejudicial ao bem jurídico tutelado para sua configuração.
- **Crimes de Perigo**: consumam-se com a simples exposição do interesse tutelado a risco de lesão. Subdividem-se em:
  - *Perigo Concreto*: a caracterização do delito exige prova judicial de que uma pessoa ou grupo determinado foi colocado em risco real;
  - *Perigo Abstrato ou Presumido*: a lei presume *juris et de jure* a periculosidade social do ato, dispensando prova pericial da iminência de dano (*porte de arma de fogo desmuniciada, tráfico de drogas*).

Por derradeiro, os **Crimes Vagos** têm como sujeito passivo a coletividade destituída de personalidade jurídica formal, como nos delitos contra a saúde pública, o meio ambiente ou a fé pública.

### Para fixar
- Crimes comuns podem ser praticados por qualquer pessoa, sem qualificação especial requerida.
- Crimes próprios exigem condição particular do agente e admitem concurso de agentes com particulares.
- Crimes de mão própria exigem execução física indelegável e não toleram a coautoria material.
- Crimes unissubsistentes realizam-se em ato motor único, sendo incompatíveis com o conatus.
- Nos crimes permanentes a consumação delitiva prolonga-se continuamente por desígnio do agente.
- A prisão em flagrante é admitida a qualquer tempo durante a permanência de delito continuado ou permanente.
- O perigo abstrato presume a nocividade social da conduta independentemente de comprovação de dano iminente.
- Crimes vagos atingem coletividades despersonalizadas como a ordem sanitária e a segurança pública.""",
            "synthetic": [
                "**Crimes Comuns e Próprios**: comuns são executados por qualquer pessoa; próprios exigem qualidade funcional ou física especial especificada no preceito primário.",
                "**Crimes de Mão Própria**: exigem atuação pessoal intransferível do autor, inviabilizando a coautoria e aceitando somente a participação por instigação.",
                "**Plurissubjetivos**: delitos de concurso necessário em que a multiplicidade de autores é pressuposto típico do tipo penal incriminador.",
                "**Unissubsistência e Tentativa**: a unissubsistência veda o conatus por esgotar-se em ato motor indivisível sem fracionamento executório viável.",
                "**Crimes Permanentes**: o estado consumativo prolonga-se no tempo por arbítrio do infrator, autorizando a custódia em flagrante a todo tempo.",
                "**Perigo Concreto e Abstrato**: perigo concreto requer demonstração de dano iminente; perigo abstrato assenta presunção absoluta legal da periculosidade.",
                "**Crimes Vagos**: caracterizam-se por terem no polo passivo entidades sociais destituídas de personalidade jurídica formalizada no direito."
            ]
        },
        {
            "id": "direito-penal/a02/s05",
            "fingerprint": get_fp("direito-penal/a02/s05"),
            "analytic": """Este segmento estuda os elementos anímicos subjetivos do fato típico, examinando as modalidades de dolo, as teorias explicativas do dolo eventual, a estrutura dogmática do crime culposo, a culpa consciente e a culpa imprópria.

### Estrutura e espécies de dolo
O dolo consubstancia a vontade livre e consciente de realizar os elementos objetivos descritos no preceito primário do tipo incriminador. Desdobra-se em elemento cognitivo (consciência do fato e de suas circunstâncias) e elemento volitivo (vontade de praticar o comportamento).

A doutrina classifica o dolo nas seguintes vertentes:
- **Dolo Direto de 1º Grau**: o objetivo primário e a meta imediata do agente residem na concretização do resultado típico incriminado (*o autor quer provocar a morte do desafeto*).
- **Dolo Direto de 2º Grau (ou de Consequências Necessárias)**: abrange os resultados colaterais acessórios que o indivíduo não deseja como fim primordial, mas tem como certos e indissociáveis do meio de execução escolhido (*colocar bomba no avião para matar um passageiro específico, assumindo como certa a morte de toda a tripulação*).
- **Dolo Eventual**: o agente antevê a possibilidade da produção do resultado lesivo e, embora não o deseje diretamente, assume o risco de sua ocorrência, agindo com indiferença (*artigo 18, I, 2ª parte*). Acolheu-se a teoria da assunção ou do assentimento.
- **Dolo Alternativo**: o autor orienta sua conduta com volição indeterminada entre dois resultados lesivos possíveis (*ferir ou matar*) ou entre vítimas distintas.

### Crime culposo e modalidades de violação de cautela
O artigo 18, parágrafo único, do CP positiva o princípio da excepcionalidade do delito culposo: a responsabilidade criminal decorre ordinariamente da atuação dolosa do agente, subordinando-se o modelo culposo à previsão expressa e excepcional no texto da norma.

A configuração do crime culposo exige a presença cumulativa de seis elementos fundamentais:
1. Conduta humana voluntária inicial;
2. Inobservância de um dever objetivo de cuidado;
3. Resultado naturalístico involuntário;
4. Nexo de causalidade biológico entre a conduta e o evento;
5. Previsibilidade objetiva da ocorrência do dano pelo homem médio;
6. Tipicidade estrita expressa em dispositivo de lei penal.

A quebra do dever de cuidado manifesta-se através de três modalidades clássicas:
- **Imprudência**: conduta positiva intempestiva e arriscada desprovida da prudência cabível (*dirigir automóvel em alta velocidade sob chuva densa*);
- **Negligência**: inação ou abstenção desatenta em momento prévio ao agir em que cabia adotar cautelas operacionais (*trafegar com veículo sem verificar o sistema de freios gastos*);
- **Imperícia**: incapacidade técnica ou despreparo prático no exercício de arte, ofício ou profissão regulamentada (*médico que maneja equipamento cirúrgico sem conhecer o protocolo técnico*).

### Culpa consciente, culpa inconsciente e culpa imprópria
A gradação da previsibilidade subjetiva permite diferenciar modalidades relevantes:
- **Culpa Inconsciente**: o resultado danoso era previsível objetivamente para qualquer cidadão prudente, mas o autor não anteviu a ocorrência do evento no momento fático da conduta.
- **Culpa Consciente**: o agente antevê mentalmente a hipótese de o resultado perigoso acontecer, porém confia sinceramente em suas aptidões pessoais para evitar a ocorrência do dano. Distingue-se do dolo eventual porque neste o agente assume com indiferença o risco do evento (*tanto faz*), ao passo que na culpa consciente o sujeito rejeita o dano acreditando na sua inviabilidade prática.
- **Culpa Imprópria (por Extensão ou Assimilação)**: verifica-se quando o indivíduo projeta dolosamente um resultado lesivo sob a influência de erro inescusável sobre causas de justificação (*descriminante putativa por erro evitável*). Por expressa determinação legal (artigo 20, § 1º), a conduta intencional é sancionada a título culposo.

No direito criminal pátrio é vedada a compensação de culpas. A culpa concomitante da vítima não apaga a responsabilidade penal do infrator, operando exclusivamente na dosimetria sentencial como circunstância judicial atenuadora da pena-base.

### Para fixar
- O dolo direto abrange a meta principal (1º grau) e os efeitos certos colaterais indissociáveis (2º grau).
- O dolo eventual apoia-se na teoria do assentimento, configurando-se pela aceitação indiferente do risco previsto.
- O crime culposo é excepcional e depende de previsão expressa no diploma incriminador.
- A inobservância do dever objetivo de cuidado desdobra-se em imprudência, negligência e imperícia.
- A imperícia vincula-se ao despreparo técnico no exercício de profissão regulamentada.
- Na culpa consciente o autor antevê o risco mas confia seriamente que ele não ocorrerá.
- A culpa imprópria decorre de erro inescusável sobre excludente e é punida como culposa por política penal.
- No direito penal não há compensação recíproca de culpas entre o infrator e a vítima.""",
            "synthetic": [
                "**Dolo de Consequências Necessárias**: compreende os resultados laterais certos decorrentes de modo inevitável do método de extermínio escolhido pelo agente.",
                "**Dolo Eventual e Teoria da Assunção**: configura-se quando o autor antevê o risco proibido e atua com indiferença, consentindo no desfecho lesivo.",
                "**Excepcionalidade da Culpa**: a punição culposa requer previsão expressa em tipo incriminador, sob pena de atipicidade penal da conduta humana.",
                "**Modalidades de Culpa**: a imprudência constitui agir afoito perigoso, a negligência traduz desídia omissiva, e a imperícia é inaptidão profissional.",
                "**Culpa Consciente versus Dolo Eventual**: na culpa consciente o indivíduo rejeita o evento confiando na sua perícia; no dolo eventual ele anui ao risco.",
                "**Culpa Imprópria**: sanciona a título culposo a conduta executada com intenção dolosa alicerçada em erro inescusável sobre descriminante.",
                "**Inadmissibilidade de Compensação**: a concorrência culposa da vítima não extingue a punibilidade nem elide a imputação ao causador originário."
            ]
        },
        {
            "id": "direito-penal/a02/s06",
            "fingerprint": get_fp("direito-penal/a02/s06"),
            "analytic": """Este segmento aborda a estrutura dos crimes preterdolosos, o desenvolvimento do iter criminis através de suas etapas sucessivas, a distinção entre preparação e execução, a consumação típica e o regime penal da tentativa.

### Estrutura do crime preterdoloso
O crime preterdoloso consubstancia figura complexa qualificada pelo resultado em que se verifica **dolo na conduta antecedente e culpa no resultado superveniente gravoso**. O indivíduo deseja perpetrar um ilícito penal básico, porém, por negligência ou imprudência na execução, acaba provocando um resultado agravador mais severo do que o pretendido.

O exemplo paradigmático reside na lesão corporal seguida de morte (*artigo 129, § 3º, do Código Penal*): o ofensor agride fisicamente o desafeto com ânimo de ferir (*animus laedendi*), mas os golpes desencadeiam traumatismo letal não desejado nem assumido a título de dolo.

Por força do artigo 19 do CP, o resultado que agrava especialmente a pena só é imputável a quem o houver causado ao menos culposamente. Por envolver culpa estrita no evento final, o delito preterdoloso **não admite tentativa**.

### Fases do Iter Criminis e o limiar executório
O iter criminis compreende o itinerário percorrido pela vontade criminosa até a realização total da conduta:
1. **Cogitação**: momento interno da ideação na mente do sujeito. Pelo princípio da alteridade, a cogitação é rigorosamente impunível pelo direito penal;
2. **Preparação**: o agente adota medidas externas de arranjo e aquisição de meios (*compra de corda para amarrar vítima*). Em regra, os atos preparatórios são impuníveis, ressalvada a previsão autônoma como crime independente pelo legislador (*posse de explosivos, associação criminosa*);
3. **Execução**: o sujeito inicia a realização dos núcleos verbais descritos no tipo incriminador;
4. **Consumação**: produz-se a integral realização dos elementos constitutivos da figura delitiva;
5. **Exaurimento**: fatos que sucedem a consumação e revelam o aproveitamento do produto criminoso, atuando como parâmetro de aumento na dosimetria judicial.

Para distinguir o ato preparatório impunível do início da execução punível, o direito pátrio adota o **Critério Objetivo-Individual** (ou Teoria Formal-Objetiva Individual): haverá início de execução quando o autor praticar ato que, segundo seu plano concreto de ação, apresentar-se como imediatamente anterior e umbilicalmente ligado ao início do verbo típico incriminado.

### Tentativa: conceito, cálculo punitivo e classificações
A tentativa (*conatus*) ocorre quando, iniciada a execução do plano criminoso, o resultado consumativo não se verifica por contingências alheias à volição do autor (*artigo 14, inciso II, do CP*).

O parágrafo único do artigo 14 adota a teoria objetiva para cominação da reprimenda: comina-se ao conatus a sanção abstrata reservada à consumação, com decote obrigatório fracionário que oscila entre **um e dois terços**. A dosimetria do abatimento orienta-se pela distância que separou o agente da consumação: quanto mais próximo o autor chegou da consumação, menor será o percentual redutor.

A doutrina classifica a tentativa sob variadas perspectivas:
- **Tentativa Cruenta (ou Vermelha)**: a vítima é atingida fisicamente e sofre lesão corporal;
- **Tentativa Incruenta (ou Branca)**: os meios mecânicos não atingem a integridade física do ofendido;
- **Tentativa Perfeita (ou Acabada / Crime Falho)**: o agente esgota integralmente todo o arsenal executório à sua disposição;
- **Tentativa Imperfeita (ou Inacabada)**: o agente tem a execução interrompida involuntariamente antes de desferir todos os atos executivos projetados.

Não admitem tentativa: crimes culposos próprios, crimes preterdolosos, crimes unissubsistentes, crimes omissivos puros, contravenções penais e crimes habituais.

### Para fixar
- O crime preterdoloso exige dolo na conduta antecedente e culpa estrita no resultado mais gravoso.
- Pelo artigo 19 do CP, a qualificadora pelo resultado demanda demonstração de dolo ou culpa.
- O iter criminis é composto por cogitação, preparação, atos executórios, consumação e exaurimento.
- A cogitação é impunível, e atos preparatórios só se punem se tipificados autonomamente em lei.
- O início executório afere-se pelo critério objetivo-individual de proximidade ao núcleo do tipo.
- A tentativa acarreta redução obrigatória de um a dois terços calibrada pela proximidade consumativa.
- A tentativa cruenta fere a integridade do ofendido; a incruenta não atinge o corpo da vítima.
- Crimes culposos, preterdolosos, omissivos próprios e contravenções penais não admitem tentativa.""",
            "synthetic": [
                "**Conceito do Preterdolo**: caracteriza-se pela coexistência de dolo na conduta preliminar e culpa no desfecho letal final, repelindo a figura da tentativa.",
                "**Artigo 19 do Código Penal**: determina que qualificadoras decorrentes de resultados gravosos exigem obrigatoriamente comprovação de ao menos culpa do agente.",
                "**Iter Criminis**: percorre cogitação impunível, preparação atípica salvo crime autônomo, execução punível, consumação e eventual exaurimento dosimétrico.",
                "**Critério de Execução**: inicia-se a execução formal quando os atos praticados guardam relação imediata e causal com o núcleo do verbo típico incriminado.",
                "**Sanção da Tentativa**: o conatus impõe abatimento fracionário de um a dois terços conforme a maior proximidade alcançada da consumação típica.",
                "**Espécies de Tentativa**: diz-se cruenta quando há lesão na vítima, incruenta quando desprovida de ofensa corpórea, e perfeita quando se esgota o arsenal.",
                "**Incompatibilidade com Conatus**: exclui-se a tentativa em crimes culposos genuínos, preterdolosos, unissubsistentes, omissivos próprios e contravenções."
            ]
        },
        {
            "id": "direito-penal/a02/s07",
            "fingerprint": get_fp("direito-penal/a02/s07"),
            "analytic": """Este segmento aborda institutos de desarmamento da tipicidade e abrandamento punitivo no iter criminis, analisando a desistência voluntária, o arrependimento eficaz, o arrependimento posterior e o crime impossível sob a luz da jurisprudência sumulada.

### Desistência voluntária e arrependimento eficaz (*A Ponte de Ouro*)
O artigo 15 do Código Penal consagra que quem cessa espontaneamente o iter executivo ou atua com eficácia para obstar o desfecho danoso final responde tão somente pelas condutas lesivas já concretizadas:
- **Desistência Voluntária (1ª parte)**: o autor inicia os atos executórios e, dispondo de meios operacionais para prosseguir na empreitada, decide livremente estancar a atividade agressiva (*posso prosseguir, mas não quero*).
- **Arrependimento Eficaz (2ª parte)**: o autor esgota todos os atos executórios à sua disposição, mas, em momento contíguo, enceta providências ativas imediatas que conseguem evitar com sucesso a verificação do resultado lesivo (*socorre a vítima baleada levando-a a tempo ao hospital*).

A distinção teórica entre a desistência voluntária e a tentativa falhada apoia-se na célebre **Fórmula de Frank**:
- Se o sujeito *pode prosseguir, mas não quer*, configura-se a desistência voluntária;
- Se o sujeito *quer prosseguir, mas não pode* em razão da intervenção de terceiros ou alerta policial, haverá tentativa punível.

A consequência jurídica de ambos os institutos (denominados pela doutrina como a *ponte de ouro* de Von Liszt) consiste na **exclusão da tipicidade da tentativa do delito originariamente almejado**, respondendo o agente exclusivamente pelo dolo residual dos atos já consumados (ex.: responde por lesão corporal leve se desistiu de prosseguir no homicídio).

### Arrependimento posterior (*A Ponte de Prata*)
O artigo 16 do Código Penal disciplina o arrependimento posterior, causa legal obrigatória de diminuição de pena privativa de liberdade: nas infrações executadas sem emprego de agressão física ou coação moral pessoal, restituído o bem ou indenizado o desfalque patrimonial até o recebimento formal da acusação ministerial ou privada, a sanção corporal suportará decote de **um a dois terços**.

A aplicação da benesse exige a confluência cumulativa de quatro requisitos rigorosos:
1. Delito cometido sem o emprego de violência física ou grave ameaça à pessoa humana;
2. Reparação integral e efetiva do dano patrimonial ou restituição da coisa subtraída;
3. Voluntariedade da reparação (não se exige espontaneidade, admitindo-se provocação de parentes ou do advogado);
4. Cumprimento da reparação em momento cronológico anterior ao despacho de recebimento formal da peça acusatória.

A modulação fracionária de redução da reprimenda (de um a dois terços) é aferida judicialmente em função da presteza, preterição e celeridade com que o acusado ressarciu a vítima.

### Crime impossível e as Súmulas 145 do STF e 567 do STJ
O artigo 17 do Código Penal consagra a figura do crime impossível (também rotulado como tentativa inidônea ou quase-crime): afasta-se a própria punibilidade do conatus na hipótese em que o meio mecânico eleito é integralmente estéril ou o objeto material sobre o qual recai o ataque é totalmente inidôneo à consumação.

O ordenamento penal adotou a **Teoria Objetiva Temperada (ou Mitigada)**:
- **Ineficácia Absoluta do Meio**: o instrumento mecânico ou químico utilizado é desprovido de qualquer aptidão lesiva para atingir o resultado almejado (*tentar envenenar alguém com ministração de açúcar refinado ou atirar com arma de fogo com mecanismo de percussão desmontado*);
- **Impropriedade Absoluta do Objeto**: o sujeito passivo ou o objeto material sobre o qual recai o ato executório é destituído da qualidade essencial para que o crime se consume (*desferir disparos contra indivíduo que já faleceu horas antes de morte natural*).

Caso a ineficácia ou impropriedade sejam meramente relativas (ex.: arma que falha em um tiro mas tem potencial de disparar o seguinte, ou vítima que guarda pouco dinheiro no bolso), haverá tentativa punível.

Na jurisprudência dos tribunais superiores, cumpre fixar duas súmulas basilares:
- **Súmula 145 do STF (Flagrante Preparado)**: não há crime quando a preparação do flagrante pela autoridade policial torna impossível a sua consumação (configura autêntico crime impossível);
- **Súmula 567 do STJ (Monitoramento Eletrônico)**: sistema de vigilância eletrônica instalado em estabelecimento comercial, a presença de câmeras ou a atuação de seguranças privados não torna o furto crime impossível, subsistindo a tipicidade tentada ou consumada.

### Para fixar
- A desistência voluntária ocorre quando o autor pode prosseguir na execução mas decide livremente interrompê-la.
- O arrependimento eficaz exige que a intervenção do autor impeça com sucesso a produção do resultado.
- Ambos os institutos da ponte de ouro afastam a tentativa, respondendo o agente só pelos atos já consumados.
- A fórmula de Frank diferencia a desistência (*posso prosseguir, mas não quero*) da tentativa (*não posso*).
- O arrependimento posterior aplica-se a crimes sem violência/grave ameaça com reparação até o recebimento da inicial.
- O crime impossível exige ineficácia do meio ou impropriedade do objeto de caráter estritamente absoluto.
- A Súmula 145 do STF declara atípico o flagrante provocado quando a armação policial inviabiliza a consumação.
- A Súmula 567 do STJ estabelece que sistemas de câmeras e vigilância em lojas não configuram crime impossível.""",
            "synthetic": [
                "**Ponte de Ouro (art. 15)**: a desistência voluntária e o arrependimento eficaz afastam a imputação da tentativa, punindo o autor apenas pelos atos pretéritos realizados.",
                "**Fórmula de Frank**: sintetiza a desistência quando o sujeito pode prosseguir mas não quer, em oposição à tentativa quando ele deseja prosseguir mas é obstado.",
                "**Arrependimento Posterior (art. 16)**: causa de diminuição de um a dois terços em crimes patrimoniais sem violência reparados até o recebimento da peça acusatória.",
                "**Crime Impossível (art. 17)**: acolheu a teoria objetiva temperada, exigindo ineficácia absoluta dos meios ou absoluta impropriedade do objeto para afastar a punição.",
                "**Meios Relativos**: a ineficácia relativa ou impropriedade parcial não descaracteriza o delito, respondendo o agente pelas sanções ordinárias da tentativa típica.",
                "**Súmula 145 do STF**: consolida a atipicidade penal no flagrante preparado pela autoridade quando o aparato impede de forma cabal a consumação do ilícito.",
                "**Súmula 567 do STJ**: a instalação de circuitos de segurança eletrônica ou monitores privados em lojas não transforma o delito de furto em crime impossível."
            ]
        },
        {
            "id": "direito-penal/a02/s08",
            "fingerprint": get_fp("direito-penal/a02/s08"),
            "analytic": """Este segmento finaliza a teoria do crime analisando a antijuridicidade, examinando o estado de necessidade, a legítima defesa e suas restrições jurisprudenciais, o estrito cumprimento do dever legal, o exercício regular de direito e o excesso punível.

### Antijuridicidade e causas de justificação (art. 23 do CP)
A ilicitude (ou antijuridicidade) consubstancia a contradição formal e axiológica entre o comportamento formalmente típico e o ordenamento jurídico tutelar. Uma vez demonstrada a tipicidade da conduta, presume-se relativamente a sua ilicitude (*ratio cognoscendi*), cabendo à defesa demonstrar a ocorrência de causa excludente.

O artigo 23 do Código Penal elenca as causas legais gerais de exclusão da ilicitude:
1. Estado de necessidade;
2. Legítima defesa;
3. Estrito cumprimento de dever legal;
4. Exercício regular de direito.

Ao lado dessas excludentes formais da Parte Geral, a doutrina reconhece causas supralegais de exclusão da antijuridicidade, como o **consentimento válido do ofendido**, desde que recaia sobre bens jurídicos eminentemente disponíveis (*patrimônio material próprio*) manifestado por titular capaz e imputável antes ou durante a conduta.

### Estado de necessidade (art. 24 do CP)
O artigo 24 do Código Penal define que atua amparado por estado de necessidade quem comete o fato típico com a finalidade exclusiva de tutelar contra risco presente bem jurídico particular ou de terceiro, perigo este que não deflagrou conscientemente e cuja repulsa não admitia outro recurso fático menos gravoso.

A caracterização do instituto pressupõe os seguintes requisitos objetivos e subjetivos:
- Existência de um **perigo atual** que ameace direito próprio ou de outrem (o CP não previu perigo iminente no estado de necessidade, apenas o perigo presente);
- Involuntariedade na produção do perigo (o causador voluntário doloso não pode alegar a justificativa);
- Inevitabilidade da conduta lesiva por outro meio menos danoso (*inexistência de via de fuga viável*);
- Proporcionalidade ou razoabilidade do sacrifício (teoria unitária: o bem salvo deve ostentar valor equivalente ou superior ao bem lesado);
- Inexistência do dever legal de enfrentar o risco (§ 1º do art. 24: bombeiros, policiais e salva-vidas não podem recusar socorro alegando estado de necessidade pessoal);
- Consciência subjetiva da situação justificante (*animus necessitatis*).

### Legítima defesa (art. 25 do CP) e vedações jurisprudenciais
O artigo 25 do Código Penal estabelece que age em legítima defesa aquele que, utilizando com moderação os instrumentos de contenção postos ao seu alcance imediato, obsta agressão ilícita humana presente ou iminente dirigida contra prerrogativa individual própria ou alheia.

Seus elementos basilares são:
- **Agressão humana injusta**: ataque ilícito desencadeado por pessoa física (ataque de animal doméstico sem instigação de dono configura estado de necessidade, e não legítima defesa);
- **Agressão atual ou iminente**: a agressão está em curso de execução ou prestes a deflagrar-se (não se admite defesa contra agressão passada já cessada nem contra receio hipotético futuro);
- **Defesa de direito próprio ou de terceiro**: qualquer interesse jurídico reconhecido pelo direito pode ser defendido;
- **Uso moderado dos meios necessários**: emprego do meio menos lesivo colocado à disposição imediata do defendente, manejado com estrita moderação para fazer cessar a agressão;
- **Elemento anímico subjetivo**: inequívoca intenção de defender-se (*animus defendendi*).

Na jurisprudência, sobressai a histórica decisão do Supremo Tribunal Federal na **ADPF 779**, que fixou a **completa inconstitucionalidade da tese da legítima defesa da honra**. O STF declarou nulos veredictos absolutórios de jurados no Tribunal do Júri apoiados na justificativa da honra em feminicídios, por manifesta violação aos direitos fundamentais à vida, à dignidade e à igualdade de gênero.

### Estrito cumprimento do dever legal, exercício regular de direito e excesso punível
- **Estrito Cumprimento do Dever Legal**: ampara o agente público ou particular que realiza ato determinado expressamente por preceito legal imperativo (*policial que cumpre mandado judicial de busca e apreensão; carrasco que executa pena de morte em guerra declarada*). O mandamento deve emanar de lei, decreto ou regulamento legal.
- **Exercício Regular de Direito**: assegura a licitude de condutas autorizadas por qualquer segmento do ordenamento jurídico (*trotes universitários moderados, violências físicas consentidas em desportos regulamentados como o boxe, intervenções médico-cirúrgicas autorizadas*).
- **Ofendículos**: mecanismos predispostos para a salvaguarda de patrimônio (*cerca elétrica, arame farpado, cacos de vidro em muros*). A instalação regular configura exercício regular de direito; seu acionamento letal contra invasor injusto transmuta-se em legítima defesa preordenada.

O parágrafo único do artigo 23 estabelece que o agente, em qualquer das hipóteses de justificação, responderá pelo **excesso doloso ou culposo**. Se o defendente extrapola deliberadamente os limites da moderação, responde pelo resultado a título doloso; se o transbordamento decorre de erro evitável no manuseio da arma, responde por culpa se houver previsão típica culposa.

### Para fixar
- As causas de justificação legais gerais do art. 23 afastam a ilicitude do fato formalmente típico.
- O consentimento do ofendido opera como causa supralegal sobre bens estritamente disponíveis.
- O estado de necessidade pressupõe perigo atual, proporcionalidade e ausência do dever legal de enfrentar o risco.
- Bombeiros e policiais investidos no cargo não podem invocar estado de necessidade para furtar-se ao socorro.
- A legítima defesa exige agressão humana injusta atual ou iminente e uso estritamente comedido dos meios.
- O STF na ADPF 779 baniu categoricamente a tese da legítima defesa da honra no ordenamento penal.
- O estrito cumprimento do dever legal pressupõe ordem cogente derivada expressamente de diploma normativo.
- O excesso doloso ou culposo nas excludentes enseja responsabilização penal nos moldes do art. 23, parágrafo único.""",
            "synthetic": [
                "**Antijuridicidade e Excludentes (art. 23)**: afasta a ilicitude típica mediante estado de necessidade, legítima defesa, estrito cumprimento de dever legal e exercício de direito.",
                "**Requisitos do Estado de Necessidade**: impõe perigo presente involuntário, razoabilidade de sacrifício e inexistência do dever funcional estrito de enfrentar o risco.",
                "**Legítima Defesa (art. 25)**: caracteriza-se pelo emprego comedido dos meios defensivos necessários contra ataque humano injusto iminente ou em curso fático.",
                "**ADPF 779 do STF**: assentou a nulidade e inconstitucionalidade absoluta da tese da legítima defesa da honra em crimes submetidos ao julgamento popular do Júri.",
                "**Estrito Cumprimento do Dever**: justifica atos praticados por agentes no cumprimento compulsório de determinações estritas cominadas pelo texto de lei formal.",
                "**Exercício Regular e Ofendículos**: ampara condutas consentidas pelo ordenamento e instalação moderada de dispositivos materiais predispostos à guarda patrimonial.",
                "**Excesso Punível**: o parágrafo único do artigo 23 comina sanção dolosa ou culposa sempre que o agente transbordar dos limites da moderação defensiva."
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
