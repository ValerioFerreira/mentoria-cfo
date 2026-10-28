# -*- coding: utf-8 -*-
"""Part 2 for a06: s05, s06, s07, s08 (Lenocínio, Rufianismo, Migração, Ação Penal e Vulneráveis)."""

def get_part2_data(get_fp):
    items = []
    summaries = []

    # -------------------------------------------------------------
    # SEGMENT 05: Lenocínio, Rufianismo e Exploração Sexual (p. 50-58)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a06/s05",
        "bizu": {
            "summary": [
                "**Lenocínio Genérico**: condutas delituosas que intermedeiam, facilitam ou auferem lucro econômico sobre o comércio sexual exercido por outrem.",
                "**Mediação Carnal (art. 227)**: aliciar pessoa para saciar o apetite lúbrico de terceiro (reclusão de 1 a 3 anos), punindo a corretagem de encontros íntimos.",
                "**Favorecimento da Prostituição (art. 228)**: atrair outrem à mercancia do corpo ou dificultar que abandone o meretrício (reclusão de 2 a 5 anos e multa).",
                "**Casa de Prostituição (art. 229)**: manter estabelecimento voltado à exploração sexual comercial alheia (reclusão de 2 a 5 anos e multa).",
                "**Inaplicabilidade da Adequação Social**: o Superior Tribunal de Justiça firmou que a tolerância social não descriminaliza a conduta de gerenciar casa de prostituição.",
                "**Rufianismo (art. 230)**: tirar proveito econômico da prostituição alheia, participando dos ganhos ou fazendo-se sustentar por quem a exerça (reclusão de 1 a 4 anos).",
                "**Diferenciação Prática**: no rufianismo o criminoso parasita os proventos auferidos pela meretriz, enquanto na casa de prostituição explora o recinto físico de comércio.",
                "**Atipicidade da Prostituição Individual**: a comercialização do próprio corpo por pessoa adulta e plenamente capaz consubstancia conduta juridicamente atípica no Brasil.",
                "**Revogação dos Antigos Arts. 231 e 231-A**: o tráfico de pessoas para exploração sexual foi deslocado para o art. 149-A do Código Penal pela Lei 13.344/2016."
            ],
            "teoria": [
                {
                    "statement": "A conduta da pessoa adulta que comercializa voluntariamente serviços sexuais próprios configura contravenção penal de vadiagem.",
                    "isTrue": False,
                    "explanation": "No ordenamento penal pátrio, a prostituição exercida individualmente por adulto capaz não constitui crime nem contravenção penal."
                },
                {
                    "statement": "A suposta tolerância social em relação a prostíbulos não conduz à descriminalização do delito de manter casa de prostituição.",
                    "isTrue": True,
                    "explanation": "A jurisprudência sumulada e pacífica do STJ rechaça o princípio da adequação social para afastar a tipicidade do artigo 229 do CP."
                },
                {
                    "statement": "O crime de rufianismo aperfeiçoa-se unicamente quando o agente emprega violência física ou coação moral contra a vítima prostituída.",
                    "isTrue": False,
                    "explanation": "O rufianismo simples (art. 230, caput) caracteriza-se pelo mero parasitismo financeiro sobre os ganhos da vítima, sem exigir violência física."
                },
                {
                    "statement": "O delito de mediação para satisfazer a lascívia de outrem pune a intermediação carnal ainda que sem intuito de lucro comercial.",
                    "isTrue": True,
                    "explanation": "O tipo do artigo 227 do Código Penal prescinde do propósito de lucro econômico, bastando o induzimento com finalidade libidinosa."
                }
            ],
            "revisao": [
                {
                    "statement": "O gerente de estabelecimento que apenas loca quartos a profissionais do sexo sem auferir percentual dos atos não pratica crime.",
                    "isTrue": False,
                    "explanation": "O art. 229 pune expressamente a manutenção de local destinado a encontros para exploração sexual, com ou sem participação direta no cachê."
                },
                {
                    "statement": "O tipo penal do rufianismo tutela primariamente a moralidade pública e a integridade de quem exerce a atividade de prostituição.",
                    "isTrue": True,
                    "explanation": "A norma visa proteger a liberdade sexual e impedir a exploração parasitária de recursos obtidos no meretrício alheio."
                },
                {
                    "statement": "O crime de tráfico interno de pessoas com finalidade de exploração sexual permanece tipificado no artigo 231-A do estatuto repressivo.",
                    "isTrue": False,
                    "explanation": "O art. 231-A foi revogado pela Lei 13.344/2016, passando o tráfico humano a ser disciplinado de forma unificada no artigo 149-A do Código Penal."
                },
                {
                    "statement": "Configura causa de aumento de pena no rufianismo a circunstância de ser a vítima explorada menor de dezoito anos ou vulnerável.",
                    "isTrue": True,
                    "explanation": "O parágrafo primeiro do artigo 230 comina sanção exasperada se a vítima for adolescente ou incapaz de resistir ao parasitismo."
                }
            ],
            "pointers": [
                {"topic": "Lenocínio e Mediação Carnal", "pageRef": 50},
                {"topic": "Favorecimento da Prostituição", "pageRef": 52},
                {"topic": "Casa de Prostituição e Adequação Social", "pageRef": 55},
                {"topic": "Rufianismo e Parasitismo Econômico", "pageRef": 57}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a06/s05",
        "fingerprint": get_fp("direito-penal/a06/s05"),
        "analytic": """### Princípios reitores do lenocínio e exploração sexual
O ordenamento penal brasileiro adota o sistema abolicionista moderado quanto à prostituição. Isso significa que o exercício pessoal do meretrício por indivíduo adulto e plenamente capaz não constitui conduta proibida pela lei penal. Não obstante, o Estado reprime com firmeza qualquer interferência de terceiros que incentivem, intermedeiem, organizem ou explorem economicamente o comércio carnal alheio. O complexo de normas insculpidas nos artigos 227 a 230 do estatuto penal abriga as figuras tradicionais do lenocínio, visando proteger a dignidade humana contra a mercantilização degradante do ser.

### Figuras típicas: mediação, favorecimento e casa de prostituição
A repressão estatal estrutura-se em tipos específicos conforme a modalidade de intervenção:
- **Mediação para Satisfazer Lascívia de Outrem (artigo 227)**: tipifica a conduta de aliciar ou aproximar pessoa com a finalidade de saciar a volúpia de terceiro. Pune-se a conduta do intermediador, que atua como corretor de encontros íntimos, prescindindo da obtenção de proveito pecuniário;
- **Favorecimento da Prostituição ou Outra Forma de Exploração (artigo 228)**: reprova as ações de atrair outrem à mercancia do corpo, facilitar-lhe o exercício mercantil, ou impedir e embaraçar que a pessoa abandone as atividades de meretrício. Se o fato é cometido com emprego de violência, grave ameaça ou mediante prevalecimento de autoridade parental, operam-se qualificadoras expressivas;
- **Casa de Prostituição (artigo 229)**: proíbe manter, por conta própria ou de terceiros, estabelecimento no qual se pratique exploração sexual comercial habitual. A consumação dispensa a mediação física direta do titular sobre os atos íntimos, aperfeiçoando-se com a disponibilização contínua do espaço para tal finalidade. Prevalece o entendimento jurisprudencial de que a alegada adequação social ou a tolerância das autoridades administrativas não descriminalizam a gerência desses estabelecimentos.

### Rufianismo e o parasitismo econômico
O artigo 230 do Código Penal tipifica o rufianismo, conceituado doutrinariamente como a conduta parasitária de tirar proveito da prostituição alheia. O infrator, comumente denominado cáften ou gigolô, participa direta ou indiretamente dos lucros obtidos pela vítima, ou se faz sustentar, no todo ou em fração considerável, pelos rendimentos auferidos pelo trabalho carnal desta:
- *Consumação e Habitualidade*: por consubstanciar crime habitual, exige reiteração de recolhimento financeiro, não se aperfeiçoando mediante um ato isolado de recebimento de dádiva;
- *Majorantes*: a reprimenda é agravada de forma substancial quando a vítima explorada conta com menos de 18 anos, ou quando o rufião atua como seu cônjuge, companheiro, pai ou tutor.

### Para fixar
- A prostituição individual voluntária praticada por pessoa adulta é fato atípico no ordenamento brasileiro.
- O lenocínio abrange os tipos que punem quem intermedeia, facilita ou aufere ganhos com a lascívia alheia.
- O art. 227 pune o induzimento à satisfação de lascívia alheia independentemente da busca de proveito econômico.
- O favorecimento da prostituição (art. 228) pune quem atrai a vítima ao meretrício ou obsta que ela o abandone.
- Manter casa de prostituição (art. 229) continua sendo crime formalmente reprimido pelas instâncias judiciais.
- O princípio da adequação social não afasta a tipicidade da conduta de gerenciar casa de prostituição.
- O rufianismo (art. 230) exige parasitismo reiterado sobre os proventos auferidos por pessoa prostituída.
- O tráfico humano para exploração sexual migrou dos artigos 231 e 231-A para o artigo 149-A do Código Penal.""",
        "synthetic": [
            "**Atipicidade da Prostituição**: comerciar o próprio corpo de maneira voluntária por pessoa lúcida e maior constitui conduta lícita.",
            "**Lenocínio e Mediação (art. 227)**: penaliza quem aproxima pessoas com fins luxuriosos dispensando a intenção de amealhar vantagens patrimoniais.",
            "**Favorecimento Sexual (art. 228)**: repreende ações orientadas a seduzir ou aprisionar outrem nas malhas da prostituição mercantil.",
            "**Casa de Prostituição (art. 229)**: manter instalação vocacionada à facilitação da devassidão lucrativa permanece com plena vigência punitiva.",
            "**Rejeição da Adequação Social**: a leniência dos costumes contemporâneos não extirpa a criminalidade de gerir recintos voltados ao lenocínio.",
            "**Rufianismo Habitual (art. 230)**: exploração parasitária continuada sobre as rendas colhidas por terceiro no exercício da prostituição.",
            "**Majorantes do Rufianismo**: a pena eleva-se quando a exploração recai sobre menores desamparados ou exercida com ascendência familiar.",
            "**Unificação no Art. 149-A**: o tráfico transnacional de indivíduos passou a integrar o estatuto penal sob o prisma da liberdade individual."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 06: Promoção de Migração Ilegal e Atos Obscenos (p. 59-70)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a06/s06",
        "bizu": {
            "summary": [
                "**Promoção de Migração Ilegal (art. 232-A)**: promover, intermediar ou facilitar a entrada ilegal de estrangeiro no país ou de brasileiro no exterior visando lucro.",
                "**Introdução pela Lei 13.445/2017**: a Lei de Migração positivou a figura típica dos agentes agenciadores conhecidos popularmente como 'coiotes'.",
                "**Crime Formal e Especial Fim de Agir**: aperfeiçoa-se com a atividade de fomento, exigindo expressamente o dolo específico de obter vantagem econômica.",
                "**Causas de Aumento na Migração (§ 1º)**: exaspera-se a pena se cometida com violência física, grave ameaça ou em condições degradantes de transporte.",
                "**Ato Obsceno (art. 233)**: praticar ato de conotação sexual obscena em logradouro público ou aberto e exposto ao público (detenção de 3 meses a 1 ano).",
                "**Tutela do Pudor Social**: o crime de ato obsceno tutela a moralidade pública genérica, inexistindo destinatário determinado para o gesto libinoso.",
                "**Distinção com a Importunação (art. 215-A)**: se o ato libidinoso for endereçado a passageiro específico sem anuência, há importunação e não mero ato obsceno.",
                "**Escrito ou Objeto Obsceno (art. 234)**: fabricar, comercializar, importar ou distribuir material pornográfico ofensivo em ambiente de exposição pública.",
                "**Exceções Culturais e Científicas**: publicações de cunho comprovadamente artístico, literário ou médico-científico não se amoldam ao tipo proibitivo."
            ],
            "teoria": [
                {
                    "statement": "O crime de promoção de migração ilegal prescinde da efetiva travessia das fronteiras territoriais para que se dê a consumação delitiva.",
                    "isTrue": True,
                    "explanation": "Trata-se de crime formal que se aperfeiçoa com a prática das ações de intermediar ou facilitar a viagem com escopo de ganho econômico."
                },
                {
                    "statement": "A prática de nudez total em via pública diante de transeuntes indeterminados subsume-se ao delito de importunação sexual.",
                    "isTrue": False,
                    "explanation": "A nudez genérica em via pública ofende o pudor público difuso, tipificando ato obsceno (art. 233), pois inexiste vítima singular visada."
                },
                {
                    "statement": "A produção de gravuras eróticas estritamente voltadas a simpósio de arte contemporânea amolda-se formalmente ao artigo 234 do Código Penal.",
                    "isTrue": False,
                    "explanation": "A destinação estritamente artística, literária ou científica exclui a subsunção material ao delito de objeto obsceno."
                },
                {
                    "statement": "A promoção de migração ilegal possui a reprimenda exasperada se os migrantes forem submetidos a condições degradantes de acomodação.",
                    "isTrue": True,
                    "explanation": "O parágrafo primeiro do art. 232-A prevê causa especial de aumento quando o transporte ocorre sob condições degradantes ou desumanas."
                }
            ],
            "revisao": [
                {
                    "statement": "O cidadão estrangeiro transportado clandestinamente no bojo do crime de migração ilegal figura na condição de coautor do delito.",
                    "isTrue": False,
                    "explanation": "O migrante clandestino é considerado sujeito passivo e vítima do agenciador ilícito, não respondendo pelo artigo 232-A."
                },
                {
                    "statement": "O delito de ato obsceno consubstancia infração penal de menor potencial ofensivo sujeita aos institutos da Lei dos Juizados Especiais.",
                    "isTrue": True,
                    "explanation": "A pena máxima de 1 ano de detenção cominada ao art. 233 atrai a incidência da Lei 9.099/1995 com transação e suspensão do processo."
                },
                {
                    "statement": "O crime de escrito obsceno resta caracterizado mesmo quando a exibição e guarda da imagem pornográfica se destinam ao uso estritamente privado.",
                    "isTrue": False,
                    "explanation": "O art. 234 exige finalidade mercantil, difusão pública ou distribuição, não punindo a mera posse para visualização íntima e pessoal."
                },
                {
                    "statement": "A facilitação de entrada ilegal de indivíduo sem escopo de lucro pecuniário afasta a tipificação prevista no artigo 232-A do Código Penal.",
                    "isTrue": True,
                    "explanation": "A obtenção de proveito econômico consubstancia elemento subjetivo especial essencial à caracterização do crime de migração ilegal."
                }
            ],
            "pointers": [
                {"topic": "Promoção de Migração Clandestina", "pageRef": 59},
                {"topic": "Majorantes na Ação dos Coiotes", "pageRef": 62},
                {"topic": "Ato Obsceno e Pudor Coletivo", "pageRef": 65},
                {"topic": "Escrito Obsceno e Salvaguardas Artísticas", "pageRef": 68}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a06/s06",
        "fingerprint": get_fp("direito-penal/a06/s06"),
        "analytic": """### Tutela jurídica na promoção de migração ilegal (artigo 232-A)
Inserido no Código Penal por força da Lei nº 13.445/2017 (Lei de Migração), o delito de promoção de migração ilegal pune quem promove, intermedeia ou facilita a entrada irregular de estrangeiro em solo brasileiro ou a partida de nacional com destino a país forâneo de modo clandestino. A criação do tipo preencheu lacuna histórica para incriminar as redes transnacionais de agenciamento migratório informal (os denominados 'coiotes'):
- *Elemento Subjetivo Específico*: a lei condiciona expressamente a ilicitude ao desiderato de 'obter vantagem econômica'. Sem o móvel pecuniário ou patrimonial, a conduta de mero auxílio solidário resta manifestamente atípica;
- *Natureza Jurídica e Consumação*: cuida-se de crime formal e de perigo comum. A infração atinge seu desfecho consumativo com os atos de preparação de trânsito, fornecimento de passaportes adulterados ou transporte, sendo irrelevante para fins de consumação se os migrantes conseguiram efetivamente transpor os postos de fiscalização da aduana;
- *Status do Migrante*: a pessoa que contrata os serviços de travessia ostenta a condição jurídica de vítima do esquema mercantil ilícito, não respondendo como coautora ou partícipe do delito;
- *Majorantes Relevantes (§ 1º)*: a pena de reclusão de dois a cinco anos sofre aumento de um sexto a um terço se o ato envolve violência física, grave ameaça ou quando os migrantes são transportados em condições desumanas ou degradantes.

### Crimes contra o pudor público: ato obsceno (artigo 233)
O crime de ato obsceno consubstancia a ofensa direta ao sentimento coletivo de recato moral da sociedade:
- *Local de Execução*: a realização do comportamento obsceno deve ocorrer em praça pública, logradouro de uso comum ou local aberto ou exposto ao descortino de terceiros;
- *Indeterminação dos Espectadores*: o aspecto nuclear da conduta reside na ausência de uma vítima individualizada. Trata-se de ofensa difusa ao sentimento moral geral (exemplo de indivíduo despido correndo em via pública);
- *Confronto Tipológico com a Importunação*: quando o autor direciona seu comportamento lascivo a uma pessoa específica desprovida de prévia autorização (exemplo do sujeito que se esfrega ou ejacula contra passageira em condução coletiva), afasta-se o artigo 233 para incidir o artigo 215-A (importunação sexual), infração mais grave.

### Escritos e objetos obscenos (artigo 234)
A lei pune quem fabrica, importa, exporta, distribui ou expõe ao público livros, desenhos, pinturas ou objetos com teor ostensivamente obsceno com intuito mercantil ou exibição difusa. Ficam formalmente ressalvadas do campo de incidência proibitiva as criações e exposições de natureza estritamente científica, médica, educativa ou que integrem genuína manifestação artística e cultural protegida constitucionalmente.

### Para fixar
- O art. 232-A reprime a atuação dos coiotes na condução clandestina de fluxos migratórios.
- A finalidade lucrativa consubstancia elemento subjetivo especial indispensável ao tipo de migração.
- O migrante transportado em travessia clandestina é vítima e não coautor da promoção migratória.
- Submeter viajantes a condições degradantes acarreta elevação na dosimetria penal da migração ilegal.
- O ato obsceno (art. 233) atinge a coletividade indeterminada em locais abertos ou visíveis ao público.
- A presença de vítima individualizada no ato lascivo desloca a subsunção para importunação sexual.
- O art. 234 veda o comércio e difusão pública de peças pornográficas ofensivas ao pudor social.
- Expressões e publicações de teor artístico, educativo ou científico não se amoldam a escrito obsceno.""",
        "synthetic": [
            "**Combate aos Coiotes (art. 232-A)**: repreende a intermediação lucrativa voltada a ingressos migratórios ilegais em território pátrio ou estrangeiro.",
            "**Elemento de Lucro Econômico**: a tipificação exige desígnio de amealhar vantagens materiais, afastando atos desprovidos de cupidez pecuniária.",
            "**Vítima Clandestina**: o indivíduo transportado nas rotas ilegais atua como vítima perante a ordem jurídica penal.",
            "**Causas de Aumento na Migração**: aplicação de gravame sancionatório ante o emprego de brutalidade ou sujeição a ambiente desumano de viagem.",
            "**Ato Obsceno (art. 233)**: atentado contra a moralidade difusa praticado em espaço público sem escolher espectador determinado.",
            "**Fronteira com Importunação**: o direcionamento libidinoso individualizado converte a infração leve de ato obsceno no tipo autônomo do art. 215-A.",
            "**Escrito Obsceno (art. 234)**: criminalização da mercancia e propagação pública desregrada de gravuras ou materiais pornográficos escandalosos.",
            "**Ressalva Artística e Científica**: acervos culturais, trabalhos de saúde e investigações biomédicas acham-se excluídos da incidência repressiva."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 07: Ação Penal e Disposições Gerais (p. 71-84)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a06/s07",
        "bizu": {
            "summary": [
                "**Regra Atual da Ação Penal (art. 225)**: desde a reforma da Lei 13.718/2018, as infrações sexuais do Código Penal submetem-se estritamente à iniciativa persecutória incondicionada do Ministério Público.",
                "**Superação do Cenário Anterior**: encerrou-se a exigência de representação da vítima adulta capaz, tornando a intervenção ministerial irrenunciável.",
                "**Superação da Súmula 608 do STF**: a súmula que mandava aplicar ação incondicionada com violência real perdeu objeto prático face à generalização legal.",
                "**Causa de Aumento por Concurso (art. 226, I)**: exasperação de um quarto da sanção quando o crime for cometido por duas ou mais pessoas reunidas.",
                "**Majorante por Autoridade ou Vínculo (art. 226, II)**: majora-se em metade a sanção se o autor é ascendente, padrasto, tio, tutor ou chefe da vítima.",
                "**Majorante da Gravidez (art. 226, III)**: acréscimo de metade da pena se da conduta criminosa infligida sobrevier gestação indesejada.",
                "**Transmissão de DST e Deficiência (art. 226, IV)**: exasperação de um terço a dois terços se transmite moléstia venérea ou contra deficiente mental.",
                "**Estupro Coletivo e Corretivo (§§ 1º e 2º)**: acréscimo de um terço a dois terços no estupro coletivo ou para 'corrigir' orientação comportamental da vítima.",
                "**Concurso Formal vs Crime Continuado**: a prática reiterada de atos libidinosos em continuidade fática contra mesma vítima enseja regras de concurso formal ou crime único."
            ],
            "teoria": [
                {
                    "statement": "Nos crimes contra a dignidade sexual perpetrados contra vítimas maiores e capazes vigora a ação penal pública condicionada à representação.",
                    "isTrue": False,
                    "explanation": "A Lei 13.718/2018 conferiu natureza de ação penal pública incondicionada a todos os delitos tipificados no Título VI do Código Penal."
                },
                {
                    "statement": "A prática de estupro por agente que sabe ser portador de enfermidade sexual transmissível e a repassa à vítima atrai causa de aumento.",
                    "isTrue": True,
                    "explanation": "O art. 226, IV, alínea 'a', exaspera a reprimenda em fração de 1/3 a 2/3 quando o autor transmite conscientemente moléstia venérea."
                },
                {
                    "statement": "A incidência da majorante do estupro coletivo requer a atuação física de pelo menos quatro agentes na prática dos atos executórios.",
                    "isTrue": False,
                    "explanation": "O estupro coletivo (art. 226, IV, 'a') tipifica-se com o concurso de dois ou mais agentes, bastando a participação plural."
                },
                {
                    "statement": "A gestação decorrente da violência carnal perpetrada no crime de estupro autoriza a elevação da pena cominada na fração de metade.",
                    "isTrue": True,
                    "explanation": "O art. 226, inciso III, prevê aumento de metade da sanção se do crime resulta gravidez indesejada para a ofendida."
                }
            ],
            "revisao": [
                {
                    "statement": "O perdão concedido pela vítima ao estuprador após o oferecimento da denúncia acarreta a imediata extinção de sua punibilidade.",
                    "isTrue": False,
                    "explanation": "Sendo a ação pública incondicionada, o titular exclusivo é o Ministério Público, inexistindo eficácia extintiva no perdão da vítima."
                },
                {
                    "statement": "A condição de padrasto da vítima atrai causa de aumento de pena de metade nos delitos contra os costumes e dignidade sexual.",
                    "isTrue": True,
                    "explanation": "O artigo 226, inciso II, estabelece expressamente a majorante de metade caso o ofensor seja padrasto, ascendente ou tutor."
                },
                {
                    "statement": "A qualificadora do estupro corretivo restringe-se a agressões perpetradas com objetivo puramente religioso em ambiente eclesiástico.",
                    "isTrue": False,
                    "explanation": "O estupro corretivo alcança condutas que pretendem disciplinar, punir ou alterar a identidade e o comportamento social/sexual da vítima."
                },
                {
                    "statement": "A Súmula 608 do STF continua sendo o fundamento jurídico basilar para sustentar a legitimidade do Ministério Público no estupro com violência real.",
                    "isTrue": False,
                    "explanation": "A Súmula 608 do STF tornou-se formalmente inócua após a Lei 13.718/2018 ter generalizado a ação penal incondicionada para todas as hipóteses."
                }
            ],
            "pointers": [
                {"topic": "Ação Penal Pública Incondicionada", "pageRef": 72},
                {"topic": "Evolução Legislativa e Súmula 608", "pageRef": 75},
                {"topic": "Causas de Aumento e Parentalidade", "pageRef": 78},
                {"topic": "Estupro Coletivo e Corretivo", "pageRef": 82}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a06/s07",
        "fingerprint": get_fp("direito-penal/a06/s07"),
        "analytic": """### Regime jurídico da ação penal pós-Lei 13.718/2018 (artigo 225)
Historicamente, os delitos contra a liberdade sexual subordinavam-se a um modelo restritivo de ação penal privada, fundamentado no receio de exposição vexatória da vítima (*strepitus judicii*). Essa modelagem sofreu paulatina derrogação: primeiro pela Lei nº 12.015/2009 (que fixou a regra da representação, excetuando vulneráveis) e, finalmente, pela promulgação da **Lei nº 13.718/2018**, que revolucionou o artigo 225 do Código Penal:
- *Regra Geral Universal*: atualmente, todas as infrações penais catalogadas contra a dignidade sexual processam-se compulsoriamente mediante **ação penal pública incondicionada**;
- *Ineficácia de Desistências*: o órgão ministerial atua com exclusividade. A posterior retratação, renúncia ou perdão formal manifestado pela vítima perante o juízo não ostentam força para extinguir a persecução criminal instaurada;
- *Superação Jurisprudencial*: o antigo debate fundado na **Súmula 608 do Supremo Tribunal Federal** (que preconizava ação incondicionada para estupro cometido com violência real) perdeu qualquer relevância prática, porquanto hoje até mesmo condutas sem violência real (como a violação fraudulenta ou a importunação) seguem sob o rito incondicionado pleno.

### Causas especiais de aumento de pena (artigo 226)
O Código Penal agrega causas de exasperação penal para calibrar a resposta sancionatória em face de agravantes contextuais:
- *Concurso de Agentes (inciso I)*: a sanção eleva-se em **um quarto** caso a agressão seja cometida com a concorrência de duas ou mais pessoas;
- *Relação de Parentesco e Autoridade (inciso II)*: a exasperação alcança a fração de **metade** se o autor ostenta vínculo de ascendência, padrasto, madrasta, tio, irmão, tutor, curador, preceptor ou exerça chefia empregatícia ou qualquer autoridade fática sobre o sujeito passivo;
- *Superveniência de Gravidez (inciso III)*: eleva-se a pena em **metade** se da agressão sexual resultar a concepção de prole;
- *Transmissão de Moléstia Venérea ou Vítima com Deficiência (inciso IV)*: majora-se a pena de **um a dois terços** caso o agente transmita intencionalmente à vítima doença venérea transmissível, ou se esta ostentar deficiência ou patologia limitadora de defesas.

### Estupro coletivo e estupro corretivo
A legislação confere severidade particular a modalidades torpes de ataque à dignidade humana:
- *Estupro Coletivo*: incide majoração de **um a dois terços** quando a ação é empreendida mediante condutas coordenadas por dois ou mais autores de forma sucessiva ou simultânea contra o mesmo corpo;
- *Estupro Corretivo*: aplica-se a exasperação de **um a dois terços** caso a agressão sexual tenha por desígnio controlar, punir ou reprimir o comportamento moral, social ou a orientação e identidade sexual ostentada pela vítima.

### Para fixar
- A Lei 13.718/2018 generalizou a ação pública incondicionada para todos os crimes sexuais.
- O perdão extrajudicial prestado pela ofendida não possui o condão de estancar o processo penal.
- A Súmula 608 do STF perdeu a utilidade prática em face da universalização da ação incondicionada.
- O concurso de duas ou mais pessoas nos crimes sexuais eleva a sanção na fração de um quarto.
- O parentesco próximo ou autoridade empregatícia sobre a ofendida exaspera a pena na fração de metade.
- A gravidez resultante do delito atua como causa especial de aumento equivalente a metade da pena.
- Transmitir moléstia transmissível com consciência prévia enseja majoração de um a dois terços.
- O estupro corretivo destina-se a castigar a autodeterminação social ou sexual da vítima atacada.""",
        "synthetic": [
            "**Universalidade da Ação Incondicionada**: a Lei 13.718/2018 estabeleceu iniciativa persecutória incondicionada para todas as ofensas sexuais.",
            "**Irrelevância de Retratação**: eventuais manifestações de perdão da vítima adulta não interrompem o curso da demanda estatal.",
            "**Inutilidade da Súmula 608**: a jurisprudência antiga foi superada ante a total suficiência do texto legal hoje positivado.",
            "**Majoração pelo Concurso**: duas ou mais pessoas atuando conjuntas provocam elevação em um quarto da resposta punitiva.",
            "**Autoridade e Parentesco**: ascendentes, padrastos e preceptores têm reprimenda ampliada em metade pela quebra da confiança protetiva.",
            "**Gravidez Superveniente**: o advento de gestação provocada pela violência carnal motiva agravamento em cinquenta por cento da sanção.",
            "**Contaminação Venérea Dolosa**: transmissão deliberada de enfermidade sexual atrai elevação dosimétrica de até dois terços da pena.",
            "**Estupro Corretivo**: ataque repulsivo orientado a vigiar ou subjugar escolhas comportamentais ou orientações íntimas da ofendida."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 08: Estupro de Vulnerável e Súmulas Relevantes (p. 85-94)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a06/s08",
        "bizu": {
            "summary": [
                "**Estupro de Vulnerável (art. 217-A)**: imposição de penetração carnal ou atos libidinosos em desfavor de menores desprovidos de 14 anos completos (reclusão de 8 a 15 anos).",
                "**Presunção Absoluta de Violência (§ 5º)**: irrelevante o consentimento da vítima, sua compleição física ou experiência sexual pregressa.",
                "**Súmula 593 do STJ**: a existência de relacionamento afetivo ou anuência familiar não afasta a configuração do estupro de menor de 14 anos.",
                "**Vulnerabilidade Transitória ou Patológica (§ 1º)**: incorre na mesma pena quem pratica atos contra quem não tem discernimento ou capacidade de resistência.",
                "**Exemplos de Impossibilidade de Resistir**: estado de coma, sono induzido por narcóticos ('boa noite cinderela') ou embriaguez alcoólica completa.",
                "**Qualificadora de Lesão Grave (§ 3º)**: comina reclusão de dez a vinte anos se da violência da conduta decorre ofensa corporal grave.",
                "**Qualificadora de Morte Preterdolosa (§ 4º)**: comina reclusão de doze a trinta anos se da ação resulta o evento morte a título culposo.",
                "**Natureza Hedionda**: o estupro de vulnerável constitui crime hediondo em todas as formas, vedando fiança e graça constitucional.",
                "**Erro de Tipo Essencial Invencível**: se o infrator acreditava sinceramente que a parceira era maior com base em dados concretos, afasta-se o dolo."
            ],
            "teoria": [
                {
                    "statement": "A aquiescência expressa dos pais de menor de doze anos com o ato sexual afasta a antijuridicidade material do estupro de vulnerável.",
                    "isTrue": False,
                    "explanation": "A autorização familiar é juridicamente ineficaz e irrelevante, mantendo-se a configuração típica do art. 217-A."
                },
                {
                    "statement": "A figura do estupro de vulnerável admite a modalidade tentada quando a execução do ato libidinoso for fracionável e for interrompida por circunstâncias alheias.",
                    "isTrue": True,
                    "explanation": "Por ser crime plurissubsistente de forma livre, o iter criminis pode ser fracionado, viabilizando o conatus."
                },
                {
                    "statement": "A presença de discernimento sexual precoce clinicamente atestado na vítima de treze anos descaracteriza a hediondez do art. 217-A do Código Penal.",
                    "isTrue": False,
                    "explanation": "A presunção absoluta é cronológica e objetiva, não cedendo diante de laudos médicos sobre maturidade biológica precoce."
                },
                {
                    "statement": "O padrasto que pratica atos libidinosos contra enteada menor de quatorze anos responde por estupro de vulnerável com a sanção agravada pelo vínculo doméstico.",
                    "isTrue": True,
                    "explanation": "Incide cumulativamente a causa de aumento de pena de metade do art. 226, II, do CP em face da autoridade fática do padrasto."
                }
            ],
            "revisao": [
                {
                    "statement": "O estupro de vulnerável que culmina em morte preterdolosa deve ser submetido a julgamento popular perante o Tribunal do Júri.",
                    "isTrue": False,
                    "explanation": "Trata-se de crime preterdoloso complexo contra a dignidade sexual, sob jurisdição privativa do juiz togado singular."
                },
                {
                    "statement": "A superveniência de lesão corporal de natureza grave decorrente do ato de libidinagem qualifica o estupro de vulnerável com reclusão de dez a vinte anos.",
                    "isTrue": True,
                    "explanation": "O § 3º do artigo 217-A comina sanção qualificada de dez a vinte anos para o resultado lesão grave decorrente da violência."
                },
                {
                    "statement": "O desconhecimento inescusável da idade da vítima infante decorrente de negligência indesculpável do réu afasta a sua condenação a título de estupro.",
                    "isTrue": False,
                    "explanation": "O erro vencível ou inescusável não afasta o dolo quando o tipo não possui previsão culposa, respondendo o agente pelo delito doloso."
                },
                {
                    "statement": "O estupro de vulnerável prescinde da verificação de rompimento da membrana himenal para atingir a sua plena consumação jurídica.",
                    "isTrue": True,
                    "explanation": "O delito consuma-se com qualquer ato libidinoso ou conjunção carnal, sendo despicienda a constatação pericial de rotura himenal."
                }
            ],
            "pointers": [
                {"topic": "Critério Etário e Vulnerabilidade Absoluta", "pageRef": 85},
                {"topic": "Impossibilidade de Resistência e Entorpecimento", "pageRef": 88},
                {"topic": "Qualificadoras Preterdolosas de Dano", "pageRef": 91},
                {"topic": "Súmula 593 e Pacificação Jurisprudencial", "pageRef": 93}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a06/s08",
        "fingerprint": get_fp("direito-penal/a06/s08"),
        "analytic": """### Estrutura típica do estupro de vulnerável (artigo 217-A)
Introduzido pela Lei nº 12.015/2009 para reorganizar o sistema punitivo contra o abuso de incapazes, o artigo 217-A do Código Penal tipifica o ato de manter conjunção carnal ou executar qualquer ato libidinoso heterogêneo com pessoa que conte com idade menor de 14 anos. O bem jurídico resguardado é a intangibilidade e o livre desenvolvimento psicossexual do indivíduo infanto-juvenil:
- *Sanção Fundamental*: comina pena severa de reclusão de **oito a quinze anos**;
- *Natureza Jurídica e Bem Jurídico*: cuida-se de crime comum (que pode ser perpetrado por homem ou mulher) e material ou de forma livre no que toca à execução libidinosa.

### Presunção absoluta de vulnerabilidade e a Súmula 593 do STJ
A dogmática penal contemporânea superou controvérsias históricas sobre o consentimento:
- *Critério Puramente Cronológico*: até as vésperas do 14º aniversário da vítima, vigora presunção absoluta de vulnerabilidade (*juris et de jure*);
- *Positivação pelo § 5º da Lei nº 13.718/2018*: a legislação acolheu expressamente a consolidada **Súmula 593 do STJ**, estatuindo que a consumação independe da anuência da ofendida, inexistindo relevo jurídico em sua prévia vivência erótica ou na existência de laço amoroso estabelecido com o agente;
- *Casamento e Coabitação*: a convivência conjugal precoce, a aquiescência manifestada pelos pais ou genitores ou a união estável não elidem a materialidade delitiva do crime;
- *Erro de Tipo Escusável*: a única hipótese de desoneração subjetiva é a comprovação cabal de erro de tipo essencial invencível (artigo 20 do Código Penal), quando as circunstâncias exteriores concretas (como exibição fraudulenta de documentos verossímeis) retiraram do infrator a consciência sobre a menoridade da vítima.

### Hipóteses equiparadas de vulnerabilidade (§ 1º)
Incorre exatamente na mesma reprimenda quem mantém relações sexuais com indivíduo que:
- *Por Enfermidade ou Deficiência Mental*: não possui o discernimento necessário e indispensável para a prática e valoração ética do ato carnal;
- *Por Qualquer Outra Causa, não Pode Oferecer Resistência*: contempla estados transitórios de incapacidade motora ou psíquica, tais como perda profunda de consciência por intoxicação alcoólica ou ingestão de soníferos administrados por outrem ou pela própria vítima, pacientes sob efeito de anestesia cirúrgica, ou indivíduos comatosos.

### Qualificadoras e regime hediondo (§§ 3º e 4º)
As formas qualificadas aplicam-se quando a conduta é cometida com violência física da qual advenha:
- *Lesão Corporal Grave (§ 3º)*: eleva a sanção básica para **reclusão de dez a vinte anos**;
- *Morte (§ 4º)*: configura hipótese preterdolosa com pena cominada de **reclusão de doze a trinta anos**;
- *Regime dos Crimes Hediondos*: tanto na figura nuclear quanto nas configurações qualificadas, o estupro de vulnerável é classificado formalmente como crime hediondo (artigo 1º, VI, Lei 8.072/1990).

### Para fixar
- O art. 217-A pune atos libidinosos praticados contra menor de 14 anos com 8 a 15 anos de reclusão.
- A vulnerabilidade do menor de 14 anos ostenta presunção jurídica absoluta de incapacidade.
- A Súmula 593 do STJ atesta que relacionamento afetivo anterior não descriminaliza o estupro.
- O consentimento do vulnerável ou prévia experiência carnal são plenamente desprovidos de valor jurídico.
- Pessoas desmaiadas ou embriagadas ao ponto de dormência enquadram-se no art. 217-A, § 1º.
- O erro de tipo essencial e escusável sobre a idade da menor é a única causa que elide o dolo.
- Lesão corporal grave decorrente da violência qualifica o delito com reprimenda de 10 a 20 anos.
- O evento morte preterdoloso acarreta incidência de qualificadora com sanção de 12 a 30 anos.""",
        "synthetic": [
            "**Estupro de Menor (art. 217-A)**: tipifica a consumação libidinosa contra menores de 14 anos reprimida com reclusão severa.",
            "**Vulnerabilidade Inatacável**: a imaturidade biopsicossocial goza de presunção jurídica absoluta tornando impossível qualquer consentimento.",
            "**Súmula 593 do STJ**: a existência de namoro, atração mútua ou prévia iniciação carnal jamais descaracterizam a materialidade típica.",
            "**Incapacidade Transitória (§ 1º)**: conduta punida identicamente quando o ato vitima sujeito paralisado por torpor, fármacos ou coma.",
            "**Embriaguez Incapacitante**: a perda involuntária de autocontrole motor atrai a salvaguarda legal da incapacidade temporária de resistência.",
            "**Erro de Tipo Escusável**: engano incontornável quanto aos anos cronológicos da vítima representa a única via excludente de culpabilidade.",
            "**Qualificadora por Lesão**: ocorrência preterdolosa de ferimento gravíssimo eleva a baliza punitiva para dez a vinte anos.",
            "**Qualificadora pela Morte**: desfecho letal não deliberado acarreta punição extrema comutando reclusão balizada de doze a trinta anos."
        ]
    })

    return items, summaries
