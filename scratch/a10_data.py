# -*- coding: utf-8 -*-
"""Data for a10: s01, s02 (Crimes em Licitações e Contratos Administrativos - Lei 14.133/2021)."""

def get_a10_data(get_fp):
    items = []
    summaries = []

    # -------------------------------------------------------------
    # SEGMENT 01: Contratação Direta e Frustração Competitiva (p. 2-14)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a10/s01",
        "bizu": {
            "summary": [
                "**Nova Topografia Penal (Lei 14.133/2021)**: inserção do Capítulo II-B no Título XI do Código Penal (arts. 337-E a 337-P), revogando a Seção da Lei 8.666/93.",
                "**Contratação Direta Ilegal (art. 337-E)**: autorizar, viabilizar ou efetuar dispensa ou inexigibilidade de licitação fora das hipóteses normativas (reclusão de 4 a 8 anos).",
                "**Responsabilidade do Beneficiário (§ único do art. 337-E)**: sujeita-se à idêntica reprimenda penal o particular ou contratado que aufere benefício com a contratação ilícita.",
                "**Frustração do Caráter Competitivo (art. 337-F)**: fraudar o certame para obter proveito decorrente da adjudicação contratual (reclusão de 4 a 8 anos e multa).",
                "**Patrocínio de Contratação Indevida (art. 337-G)**: advogar interesse privado perante o ente público dando causa a contratação cuja anulação seja decretada.",
                "**Modificação Irregular de Contrato (art. 337-H)**: outorgar vantagem contratual, acréscimo ou prorrogação indevida em favor da empreiteira sem respaldo editalício.",
                "**Perturbação de Ato Licitatório (art. 337-I)**: tumultuar, embaraçar ou inviabilizar a realização de sessão do certame público de disputa.",
                "**Violação de Sigilo de Proposta (art. 337-J)**: devassar ou possibilitar o acesso antecipado a envelopes e lances confidenciais apresentados pelos concorrentes.",
                "**Penas Prisionais Severas**: a Nova Lei de Licitações comutou as antigas penas de detenção para severas reprimendas de reclusão com regime inicial fechado."
            ],
            "teoria": [
                {
                    "statement": "O particular que se beneficia conscientemente de contratação direta ilegal celebrada sem licitação comete o crime do artigo 337-E.",
                    "isTrue": True,
                    "explanation": "O parágrafo único do art. 337-E equipara expressamente a pena do contratado ou beneficiário à do servidor que autorizou a contratação ilícita."
                },
                {
                    "statement": "A infração de devassar propostas fechadas em certame concorrencial (art. 337-J) comina reprimenda privativa de reclusão fixada em doze anos.",
                    "isTrue": False,
                    "explanation": "O art. 337-J comina pena de detenção de dois a três anos e multa, sendo uma das poucas figuras mantidas sob detenção."
                },
                {
                    "statement": "A concessão de prorrogação contratual sem previsão editalícia que beneficia o particular contratado amolda-se formalmente ao art. 337-H.",
                    "isTrue": True,
                    "explanation": "O art. 337-H tipifica expressamente admitir, possibilitar ou dar causa a modificação ou vantagem, inclusive prorrogação, sem autorização em lei."
                },
                {
                    "statement": "A infração de macular a competitividade do certame licitatório (art. 337-F) admite punição na modalidade culposa decorrente de desatenção burocrática.",
                    "isTrue": False,
                    "explanation": "O preceito incriminador exige dolo específico de angariar proveito indevido com a adjudicação, não admitindo a modalidade culposa."
                }
            ],
            "revisao": [
                {
                    "statement": "A revogação dos crimes da Lei 8.666/1993 pela Lei 14.133/2021 acarretou abolitio criminis retroativa para todas as fraudes anteriores.",
                    "isTrue": False,
                    "explanation": "Houve inequívoca continuidade normativo-típica com a inserção dos tipos penais nos artigos 337-E a 337-P do Código Penal."
                },
                {
                    "statement": "O crime de contratação direta ilegal comina pena de reclusão de quatro a oito anos, além de pena de multa proporcional.",
                    "isTrue": True,
                    "explanation": "O art. 337-E estabelece a sanção punitiva de reclusão balizada de 4 a 8 anos e multa, ampliando o rigor repressivo anterior."
                },
                {
                    "statement": "A configuração da frustração do caráter competitivo exige o prejuízo financeiro efetivo e superfaturamento comprovado da obra.",
                    "isTrue": False,
                    "explanation": "O art. 337-F tutela a competitividade e moralidade do certame, consumando-se com a fraude concursal com fim de adjudicação."
                },
                {
                    "statement": "No crime de patrocínio de contratação indevida (art. 337-G), é dispensável a posterior invalidação judicial do certame para a tipificação.",
                    "isTrue": False,
                    "explanation": "O art. 337-G exige como elementar objetiva expressa que a invalidação da contratação venha a ser declarada pelo Poder Judiciário."
                }
            ],
            "pointers": [
                {"topic": "Nova disciplina dos crimes licitatórios da Lei 14.133/2021", "pageRef": 3},
                {"topic": "Contratação direta ilegal e responsabilidade do particular no art. 337-E", "pageRef": 6},
                {"topic": "Frustração da competitividade e modificação contratual espúria", "pageRef": 9},
                {"topic": "Perturbação de certame e violação de sigilo licitatório no art. 337-J", "pageRef": 12}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a10/s01",
        "fingerprint": get_fp("direito-penal/a10/s01"),
        "analytic": """Este segmento inaugura a abordagem dos crimes em licitações e contratos administrativos sob a égide da Lei nº 14.133/2021, que revogou a disciplina penal da antiga Lei nº 8.666/1993 e inseriu o novel Capítulo II-B no Título XI da Parte Especial do Código Penal (artigos 337-E a 337-P).

### Transição legislativa e contratação direta indevida (artigo 337-E)
A promulgação da Nova Lei de Licitações (Lei nº 14.133/2021) conferiu resposta contundente à macrocriminalidade orçamentária e aos desvios em certames públicos:
- *Continuidade Normativo-Típica*: as condutas repressivas foram migradas formalmente para o seio do estatuto penal ordinário, mantendo-se a punibilidade sob balizas apenatórias sensivelmente agravadas;
- *Contratação Direta Ilegal (artigo 337-E)*: reprova admitir, possibilitar ou dar causa à contratação direta (seja por indevida dispensa ou inadequada inexigibilidade) fora das hipóteses taxativas autorizadas em lei. O legislador comutou a antiga pena branda para **reclusão de quatro a oito anos e multa**;
- *Responsabilidade do Contratado Particular (parágrafo único)*: responde pelas mesmas penas da reclusão o particular ou empresa que, tendo comprovadamente concorrido para a consumação da ilegalidade, celebra o contrato com a Administração Pública ou aufere proveito econômico decorrente do ajuste ilícito.

### Frustração da competitividade e desvios contratuais (artigos 337-F a 337-H)
A salvaguarda da isonomia entre os licitantes e a fidelidade aos termos do edital contam com tipos específicos de proteção:
- *Frustração do Caráter Competitivo de Licitação (artigo 337-F)*: criminaliza a ação de fraudar ou frustrar, mediante conluio, cartelização, exigências direcionadas ou cláusulas restritivas, a livre concorrência do processo licitatório com o propósito de adjudicar o objeto contratual (reclusão de quatro a oito anos e multa);
- *Patrocínio de Contratação Indevida (artigo 337-G)*: reprime o funcionário ou particular que intercede perante a administração dando causa à realização de licitação ou contrato cuja ilicitude seja posteriormente declarada pelo Poder Judiciário;
- *Modificação ou Vantagem Indevida na Execução (artigo 337-H)*: pune quem autoriza ou proporciona aditivos contratuais, prorrogações graciosas ou vantagens financeiras em favor do contratado sem autorização em lei ou no instrumento convocatório original.

### Perturbação e quebra de sigilo (artigos 337-I e 337-J)
A ordem nas sessões públicas de disputa e a inviolabilidade das propostas comerciais são tuteladas expressamente:
- *Perturbação de Processo Licitatório (artigo 337-I)*: pune quem impede, perturba fisicamente ou tumultua a realização de qualquer etapa procedimental do certame cominando reclusão de seis meses a três anos;
- *Violação de Sigilo em Licitação (artigo 337-J)*: tipifica a devassa indevida do conteúdo das propostas fechadas ou lances sigilosos apresentados pelos concorrentes.

### Para fixar
- A Lei 14.133/2021 inseriu os crimes licitatórios no Código Penal nos artigos 337-E a 337-P.
- A contratação direta fora das hipóteses legais comina reclusão rigorosa de quatro a oito anos.
- O particular que celebra o contrato ou aufere proveito ilícito responde nas mesmas penas (art. 337-E).
- Frustrar o caráter concorrencial da licitação atrai reclusão de quatro a oito anos e multa.
- O patrocínio indevido (art. 337-G) exige anulação formal decretada pelo Poder Judiciário.
- Modificar contrato concedendo vantagens desautorizadas tipifica o delito do artigo 337-H.
- A perturbação de atos e sessões da licitação comina pena de reclusão de 6 meses a 3 anos.
- Violar o sigilo das propostas confidenciais do certame amolda-se formalmente ao art. 337-J.""",
        "synthetic": [
            "**Inovação da Lei 14.133/21**: alocação dos crimes licitatórios na Parte Especial com gravoso endurecimento das balizas penais de reclusão.",
            "**Contratação Direta Espúria (art. 337-E)**: dispensa ou inexigibilidade fraudulenta de certame cominando reclusão gravosa de quatro a oito anos.",
            "**Extensão ao Particular Contratado**: corresponsabilidade integral do contratado que se locupleta com o ajuste administrativo ilegal.",
            "**Frustração Competitiva (art. 337-F)**: manobras de cartel e direcionamento editalício punidas severamente para blindar a isonomia concorrencial.",
            "**Patrocínio Indevido (art. 337-G)**: intercessão espúria que culmina na decretação de nulidade judicial da contratação governamental.",
            "**Aditivos Fraudulentos (art. 337-H)**: concessão de acréscimos ou prorrogações sem lastro editalício em benefício da empreiteira prestadora.",
            "**Perturbação do Certame (art. 337-I)**: tumulto orquestrado visando embaraçar o transcurso regular das fases competitivas do pregão.",
            "**Sigilo Licitatório (art. 337-J)**: violação fiduciária do sigilo das propostas comerciais assegurando a higidez isonômica do certame."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 02: Fraude, Inidoneidade e Penas Pecuniárias (p. 15-28)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a10/s02",
        "bizu": {
            "summary": [
                "**Afastamento de Licitante (art. 337-K)**: afastar ou procurar afastar licitante por meio de violência, ameaça, fraude ou oferta de vantagem (reclusão de 3 a 5 anos).",
                "**Forma Equiparada no Art. 337-K**: incorre na mesma sanção o concorrente que se abstém de disputar o certame em troca da vantagem recebida do rival.",
                "**Fraude em Licitação ou Contrato (art. 337-L)**: fraudar a entrega de mercadoria ou serviço depreciando a qualidade ou alterando a substância (reclusão de 4 a 8 anos).",
                "**Contratação Inidônea (art. 337-M)**: admitir à licitação ou celebrar contrato com empresa declarada inidônea pelo poder público (reclusão de 1 a 3 anos).",
                "**Forma Qualificada da Inidoneidade (§ 2º)**: pena de reclusão de três a seis anos se a empresa inidônea efetivamente celebra o contrato ou aufere pagamentos.",
                "**Impedimento Indevido de Cadastro (art. 337-N)**: obstar ou dificultar injustamente a inscrição de interessado idôneo nos registros cadastrais oficiais.",
                "**Omissão Grave por Projetista (art. 337-O)**: omitir ou falsear dados em projeto ou levantamento técnico licitatório com prejuízo ao erário.",
                "**Piso Vinculante da Multa (art. 337-P)**: a reprimenda pecuniária nas infrações licitatórias possui patamar mínimo estrito estabelecido em dois centésimos da cifra contratada.",
                "**Cumulação Obrigatória da Multa**: a sanção pecuniária do art. 337-P é cominada cumulativamente com as penas privativas de liberdade dos tipos."
            ],
            "teoria": [
                {
                    "statement": "O concorrente que aceita dinheiro de concorrente rival para não formular lance na fase de disputa comete o crime do art. 337-K.",
                    "isTrue": True,
                    "explanation": "O parágrafo único do art. 337-K pune identicamente quem se abstém de licitar em razão da vantagem indevida acordada."
                },
                {
                    "statement": "A pena de multa fixada para os crimes licitatórios pode ser arbitrada pelo juiz em valor inferior a um por cento do contrato administrativo.",
                    "isTrue": False,
                    "explanation": "O art. 337-P institui piso legal obrigatório de dois por cento sobre o montante financeiro global do ajuste administrativo."
                },
                {
                    "statement": "A celebração de contrato com profissional sancionado com declaração de inidoneidade configura crime cominado no art. 337-M do CP.",
                    "isTrue": True,
                    "explanation": "O art. 337-M criminaliza expressamente a conduta de admitir à licitação ou contratar pessoa ou empresa declarada inidônea."
                },
                {
                    "statement": "O crime de fraude na execução de contrato administrativo (art. 337-L) admite a modalidade culposa decorrente de defeito involuntário da fábrica.",
                    "isTrue": False,
                    "explanation": "O tipo do artigo 337-L reclama dolo estrito de fraudar a entrega do bem ou serviço em desfavor da Administração Pública."
                }
            ],
            "revisao": [
                {
                    "statement": "A consumação do afastamento de licitante (art. 337-K) exige a desistência formal comprovada do competidor intimidado.",
                    "isTrue": False,
                    "explanation": "Trata-se de crime formal que atinge a consumação com o emprego da violência, ameaça ou oferta ('afastar ou procurar afastar')."
                },
                {
                    "statement": "O engenheiro que elabora projeto básico omitindo conscientemente dados geológicos graves da obra comete o delito do art. 337-O.",
                    "isTrue": True,
                    "explanation": "O art. 337-O sanciona a omissão grave de informações ou apresentação de dados inexatos por projetistas em licitações públicas."
                },
                {
                    "statement": "O servidor que dificulta dolosamente a inscrição de consórcio nos registros cadastrais para favorecer terceiro comete o art. 337-N do CP.",
                    "isTrue": True,
                    "explanation": "O art. 337-N pune o impedimento indevido ou a dificuldade imposta à inscrição de interessados no cadastro de fornecedores."
                },
                {
                    "statement": "No crime de contratação inidônea, o fato de a empresa inidônea chegar a celebrar o contrato atua como causa extintiva de punibilidade.",
                    "isTrue": False,
                    "explanation": "A celebração do contrato configura modalidade qualificada (§ 2º do art. 337-M), elevando a sanção para reclusão de três a seis anos."
                }
            ],
            "pointers": [
                {"topic": "Afastamento de concorrente e formas equiparadas no art. 337-K", "pageRef": 16},
                {"topic": "Fraude na execução de contratos administrativos no art. 337-L", "pageRef": 19},
                {"topic": "Contratação inidônea e figuras qualificadas no art. 337-M", "pageRef": 22},
                {"topic": "Omissão de projetista e piso mínimo da pena de multa no art. 337-P", "pageRef": 26}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a10/s02",
        "fingerprint": get_fp("direito-penal/a10/s02"),
        "analytic": """Este segmento conclui a análise dogmática dos crimes em licitações e contratos administrativos da Lei nº 14.133/2021, examinando os tipos penais de afastamento forçado de concorrentes, fraudes na execução material das obras, admissão de firmas inidôneas e o critério especial de cálculo da pena de multa.

### Afastamento de concorrentes e fraudes de execução (artigos 337-K e 337-L)
A integridade da disputa pública e o fiel cumprimento das avenças administrativas são respaldados com rigor:
- *Afastamento de Licitante (artigo 337-K)*: comina reclusão de três a cinco anos e multa a quem **afasta ou procura afastar competidor** valendo-se de violência física, grave ameaça intimidadora, fraude ou oferecimento de compensação pecuniária;
- *Bilateralidade na Corrupção Concursal (parágrafo único)*: incorre na mesmíssima pena o concorrente que se abstém dolosamente de concorrer ou desiste de formular lances após aceitar a vantagem indevida ofertada pelo rival;
- *Fraude em Licitação ou Contrato (artigo 337-L)*: pune com **reclusão de quatro a oito anos e multa** quem frauda o certame ou o contrato administrativo dele decorrente mediante a entrega de materiais de qualidade inferior, alteração dolosa da substância contratada, falsificação de medições ou torna a execução excessivamente onerosa com fito de locupletamento ilícito.

### Inidoneidade, embaraços cadastrais e dever do projetista (artigos 337-M a 337-O)
O ordenamento pune a violação de sanções administrativas prévias e a má-fé técnica:
- *Contratação Inidônea (artigo 337-M)*: pune o servidor que admite na licitação ou contrata empresa ou profissional previamente declarado inidôneo pela Administração Pública. Incorre nas mesmas penas o particular que, estando inidôneo, participa da disputa (§ 1º). Caso a contratação inidônea venha a ser consumada, incide a forma qualificada com pena de reclusão de três a seis anos (§ 2º);
- *Impedimento Indevido de Registro (artigo 337-N)*: reprime a criação de embaraços abusivos ao credenciamento cadastral de licitantes idôneos;
- *Omissão Grave de Dado por Projetista (artigo 337-O)*: responsabiliza penalmente autores de projetos básicos ou executivos que omitirem dolosamente dados geológicos, estruturais ou orçamentários vitais, acarretando aditivos lesivos e superfaturamentos futuros.

### Critério autônomo da pena de multa (artigo 337-P)
Em derrogação parcial ao regramento genérico de dias-multa do Código Penal, o novel artigo 337-P prescreve que a pena pecuniária nas infrações de licitação possui como baliza mínima legal o patamar de dois centésimos da quantia financeira global pactuada no certame ou no ajuste direto correspondente. Trata-se de calibragem sancionatória proporcional à dimensão econômica do ajuste, impedindo que infrações orçamentárias vultosas sejam punidas com sanções pecuniárias simbólicas ou ineficazes.

### Para fixar
- O art. 337-K pune quem afasta ou procura afastar concorrente por violência, fraude ou propina.
- O licitante que aceita vantagem para desistir da disputa responde pela mesma pena no art. 337-K.
- Fraudar a execução da obra entregando materiais inferiores configura o delito do art. 337-L.
- Contratar fornecedor declarado inidôneo é crime formal com forma qualificada se houver execução.
- O art. 337-N veda dificultar injustamente a participação cadastral de interessados idôneos.
- O projetista que falseia levantamentos técnicos responde penalmente pelo art. 337-O.
- A pena de multa nos crimes licitatórios nunca poderá ser inferior a dois por cento do contrato.
- A multa pecuniária do art. 337-P é de aplicação obrigatória e cumulativa com a pena privativa.""",
        "synthetic": [
            "**Afastamento Licitatório (art. 337-K)**: eliminação forçada ou comprada de concorrentes punida rigorosamente na iniciativa e na desistência acordada.",
            "**Fraude de Execução (art. 337-L)**: desvirtuamento qualitativo e faturamento fraudulento de materiais em desfavor dos cofres da administração.",
            "**Contratação Inidônea (art. 337-M)**: celebração de pactos com pessoas descredenciadas pelo poder público qualificada na contratação consumada.",
            "**Barreira Cadastral (art. 337-N)**: embaraço abusivo visando tolher a habilitação formal de concorrentes regulares no registro estatal.",
            "**Fraude do Projetista (art. 337-O)**: responsabilidade penal de engenheiros e projetistas ante a sonegação de dados estruturais na feitura do edital.",
            "**Piso Legal da Multa (art. 337-P)**: vedação vinculante de arbitramento pecuniário inferior a dois por cento da cifra global do contrato ajustado.",
            "**Cumulatividade das Penas**: imposição simultânea da sanção pecuniária financeira e da pena corporal de reclusão cominada no preceito.",
            "**Salvaguarda Orçamentária**: blindagem dos procedimentos concorrenciais estatais contra manobras patrimoniais que lesam o interesse coletivo."
        ]
    })

    return items, summaries
