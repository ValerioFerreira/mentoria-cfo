# -*- coding: utf-8 -*-
"""Part 1 for a08: s01, s02, s03 (Crimes de Particular, Desacato, Corrupção Ativa e Contrabando)."""

def get_part1_data(get_fp):
    items = []
    summaries = []

    # -------------------------------------------------------------
    # SEGMENT 01: Resistência, Desobediência, Desacato e Tráfico de Influência (p. 2-16)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a08/s01",
        "bizu": {
            "summary": [
                "**Usurpação de Função Pública (art. 328)**: apossamento ilegítimo de ofício governamental por civil que pratica atos oficiais simulando autoridade estatal.",
                "**Resistência Simples (art. 329, caput)**: oposição agressiva à execução de ato legal emanado de agente público mediante emprego de violência corporal ou ameaça.",
                "**Resistência Qualificada (§ 1º)**: elevação penal se, em virtude da agressão oposta, o servidor restar obstado de consumar o ato funcional de ofício.",
                "**Cúmulo Material Obrigatório (§ 2º)**: as penas cominadas à resistência aplicam-se cumulativamente com as reprimendas relativas à violência física efetivamente praticada.",
                "**Desobediência (art. 330)**: recusa passiva e desprovida de violência em acatar ordem legítima transmitida por autoridade competente no exercício funcional.",
                "**Princípio da Subsidiariedade na Desobediência**: descabe a persecução penal quando a legislação extrapenal comina sanção administrativa sem prever cumulação penal.",
                "**Desacato (art. 331)**: ultrajar, desprestigiar ou menoscabar agente público no exercício funcional ou em decorrência direta de suas atribuições estatais.",
                "**Compatibilidade Constitucional do Desacato**: o Superior Tribunal de Justiça e o STF pacificaram que o desacato é plenamente compatível com o Pacto de São José da Costa Rica.",
                "**Tráfico de Influência (art. 332)**: solicitar ou amealhar benesse particular ostentando pretensa ascendência moral ou influência sobre servidor público (venda de fumaça)."
            ],
            "teoria": [
                {
                    "statement": "O indivíduo que apenas fecha os portões e corre para não receber intimação de oficial de justiça pratica o crime de resistência simples.",
                    "isTrue": False,
                    "explanation": "A resistência exige obrigatoriamente o emprego de violência corporal ou ameaça contra o funcionário; a fuga passiva amolda-se no máximo à desobediência."
                },
                {
                    "statement": "As sanções penais do crime de resistência aplicam-se em concurso material autônomo com as reprimendas relativas à violência física infligida.",
                    "isTrue": True,
                    "explanation": "O art. 329, § 2º, estabelece expressamente a regra do cúmulo material obrigatório entre a resistência e o delito de lesão corporal ou morte."
                },
                {
                    "statement": "O crime de desacato foi revogado e descriminalizado no ordenamento nacional em virtude da Convenção Americana sobre Direitos Humanos.",
                    "isTrue": False,
                    "explanation": "O STJ, em sede de recurso repetitivo, consolidou a vigência e plena constitucionalidade do tipo penal do desacato (art. 331)."
                },
                {
                    "statement": "No tráfico de influência, a sanção sofre exasperação de metade se o infrator insinua que a propina cobrada também beneficia o servidor estatal.",
                    "isTrue": True,
                    "explanation": "O parágrafo único do art. 332 comina majorante de cinquenta por cento caso o agente afirme ou insinue que o dinheiro destina-se ao funcionário."
                }
            ],
            "revisao": [
                {
                    "statement": "O motorista que desatende ordem de parada de agente de trânsito responde criminalmente por desobediência, cumulada com multa de trânsito.",
                    "isTrue": False,
                    "explanation": "O CTB prevê infração administrativa específica sem ressalva de processo penal, restando atípica a conduta sob o prisma do artigo 330 do CP."
                },
                {
                    "statement": "A prática de desacato independe da presença física do servidor público, aperfeiçoando-se por meio de mensagem remetida a terceiro ausente.",
                    "isTrue": False,
                    "explanation": "O desacato pressupõe a presença da autoridade ou a ciência direta e imediata das injúrias proferidas no contexto da atuação funcional."
                },
                {
                    "statement": "O crime de usurpação de função pública qualifica-se com reclusão de dois a cinco anos caso o particular aufira proveito pecuniário com o engodo.",
                    "isTrue": True,
                    "explanation": "O art. 328, parágrafo único, exaspera o apenamento caso o agente logre obter vantagem indevida com o exercício usurpado da função pública."
                },
                {
                    "statement": "A consumação do tráfico de influência subordina-se à efetiva intervenção e acolhimento do pleito perante o funcionário público almejado.",
                    "isTrue": False,
                    "explanation": "Trata-se de delito formal que atinge consumação no momento em que o explorador solicita ou exige o proveito com o pretexto de intercessão."
                }
            ],
            "pointers": [
                {"topic": "Usurpação de função pública e forma qualificada", "pageRef": 4},
                {"topic": "Resistência ativa e cúmulo de penas materiais no art. 329", "pageRef": 7},
                {"topic": "Desobediência e precedentes de sanção administrativa exclusiva", "pageRef": 11},
                {"topic": "Desacato, recepção constitucional e tráfico de influência no art. 332", "pageRef": 14}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a08/s01",
        "fingerprint": get_fp("direito-penal/a08/s01"),
        "analytic": """Este segmento inaugura a repressão aos crimes cometidos por cidadãos particulares em detrimento do prestígio, autoridade e regularidade das funções governamentais, esmiuçando os tipos de usurpação de atribuições, resistência, desobediência, desacato e tráfico de influência.

### Usurpação e resistência (artigos 328 e 329)
A autoridade do comando estatal repousa no cumprimento legal de suas determinações:
- *Usurpação de Função Pública (artigo 328)*: consuma-se quando o particular arroga para si o exercício fático de atribuições inerentes a cargo estatal que não titulariza, executando atos administrativos materiais simulados. Se da impostura derivar vantagem patrimonial indevida, a sanção salta de detenção branda para reclusão de dois a cinco anos (parágrafo único);
- *Resistência (artigo 329)*: configura-se pela oposição física ou intimidadora à execução de ato de ofício legal conduzido por agente público competente ou seu auxiliar. **Exige violência contra a pessoa ou grave ameaça**. A desobediência passiva, a recusa verbal ou a simples tentativa de fuga desarmada descaracterizam a resistência;
- *Modalidade Qualificada (§ 1º)*: caso a conduta violenta impeça materialmente o agente público de ultimar o ato legal, comina-se reclusão de um a três anos;
- *Cúmulo Material Mandatório (§ 2º)*: a lei impõe expressamente a aplicação cumulativa das penas da resistência conjuntamente com as sanções cabíveis pelas agressões físicas infligidas ao funcionário agredido.

### Desobediência e desacato (artigos 330 e 331)
A distinção dogmática dos comportamentos contra a autoridade assenta-se em balizas firmes:
- *Desobediência (artigo 330)*: pune a conduta omissiva ou comissiva de desatender ordem expressa, direta e legítima emanada de servidor público. Consoante entendimento pacificado pelo STJ, **inexiste crime de desobediência quando a legislação especial extrapenal prevê sanção administrativa ou civil específica para o descumprimento sem ressalvar expressamente a responsabilidade penal cumulativa** (exemplo do descumprimento de ordem de trânsito punido apenas pelo CTB);
- *Desacato (artigo 331)*: sanciona a conduta de proferir ultraje, ofensa verbal, achincalhe ou gestos desrespeitosos contra servidor no exercício da função ou em razão dela. O Superior Tribunal de Justiça, em sede de julgamento de recursos representativos da controvérsia, fixou que a tipificação do desacato coaduna-se perfeitamente com a Constituição da República de 1988 e com o Pacto de São José da Costa Rica, inexistindo revogação da norma penal.

### Tráfico de influência (artigo 332)
O delito de tráfico de influência criminaliza o vendedor de prestígio ilusório (*venditio fumi*). Pune o agente que solicita, exige, cobra ou aufere proveito econômico a pretexto de interceder ou influenciar deliberações de servidor estatal no exercício funcional. Trata-se de crime formal que atinge consumação instantânea com a pactuação ou recebimento da remuneração, operando causa de aumento de pena de metade caso o autor insinue que a vantagem financeira destina-se também à autoridade pública influenciada.

### Para fixar
- A usurpação de função qualifica-se com reclusão quando o particular obtém vantagem econômica.
- O crime de resistência exige o emprego efetivo de violência física ou grave ameaça contra o funcionário.
- A recusa passiva em cumprir ordem sem agressão corporal afasta a tipificação do art. 329 do CP.
- As penas da resistência cumulam-se compulsoriamente com as da lesão corporal provocada.
- A desobediência é atípica se houver sanção administrativa sem cláusula expressa de cumulação penal.
- O STJ pacificou a legitimidade constitucional e convencional do crime de desacato no ordenamento.
- O desacato reclama nexo causal funcional direto entre o ultraje proferido e o ofício público do ofendido.
- O tráfico de influência tutela o prestígio da administração e consuma-se com a solicitação da vantagem.""",
        "synthetic": [
            "**Usurpação Funcional (art. 328)**: apossamento fraudulento de múnus público qualificado severamente caso resulte em proveito patrimonial ilícito.",
            "**Resistência Ativa (art. 329)**: embaraço agressivo executado por violência corporal ou intimidação grave contra ato legal de autoridade.",
            "**Cúmulo Material Obrigatório**: aplicação autônoma e cumulativa das sanções da resistência com as penas das agressões físicas perpetradas.",
            "**Desobediência Residual (art. 330)**: recusa passiva em acatar determinação regular afastada caso a lei preveja unicamente sanção administrativa.",
            "**Validade do Desacato (art. 331)**: pacificação sumulada reconhecendo a conformidade do crime perante as salvaguardas de direitos humanos.",
            "**Nexo no Desacato**: exige-se relacionamento contextual entre o menoscabo desferido e o mister funcional desempenhado pela vítima estatal.",
            "**Tráfico de Influência (art. 332)**: mercancia de falso prestígio funcional que explora a credulidade de terceiros perante a administração.",
            "**Majorante da Venda de Fumaça**: agravamento de metade na pena ao sugerir dolosamente conluio financeiro com a autoridade decisória."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 02: Corrupção Ativa e Descaminho (p. 17-27)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a08/s02",
        "bizu": {
            "summary": [
                "**Corrupção Ativa (art. 333)**: propositura ou compromisso de repasse de proveito espúrio destinado a agente público com a finalidade de cooptá-lo a praticar ou omitir ato funcional.",
                "**Núcleos Típicos na Corrupção Ativa**: estrutura-se unicamente nos verbos oferecer ou prometer; o ato de entregar dinheiro exigido pelo policial caracteriza concussão sofrida.",
                "**Bilateralidade Relativa**: a corrupção ativa prescinde da aceitação do funcionário; havendo recusa íntegra pelo servidor, subsiste o crime do art. 333 consumado.",
                "**Majorante Especial (§ único do art. 333)**: exasperação de um terço na sanção se o servidor efetivamente retarda, omite ou pratica o ato com infração funcional.",
                "**Descaminho (art. 334, caput)**: iludir o recolhimento tributário aduaneiro devido em face da entrada, saída ou consumo de mercadoria permitida pela lei.",
                "**Objeto Material do Descaminho**: recai exclusivamente sobre mercadorias lícitas desprovidas de desembaraço aduaneiro ou de pagamento de tributos.",
                "**Formas Equiparadas (§ 1º do art. 334)**: incorre nas mesmas penas quem adquire, recebe, oculta, transporta ou comercializa mercadoria iludida em proveito mercantil.",
                "**Majorante pelo Meio de Transporte (§ 3º)**: aplicação da reprimenda em dobro se o crime de descaminho for cometido em transporte aéreo, marítimo ou fluvial.",
                "**Princípio da Insignificância no Descaminho**: admitido pelos tribunais superiores caso o valor dos tributos elididos não ultrapasse o patamar legal de vinte mil reais."
            ],
            "teoria": [
                {
                    "statement": "O particular que cede à exigência intimidatória de fiscal e lhe entrega quantia em dinheiro comete crime de corrupção ativa consumado.",
                    "isTrue": False,
                    "explanation": "Quem cede à exigência é sujeito passivo do crime de concussão praticado pelo servidor, sendo atípica a sua conduta quanto à corrupção ativa."
                },
                {
                    "statement": "O crime de corrupção ativa consuma-se no instante em que a proposta de propina chega ao conhecimento do funcionário público visado.",
                    "isTrue": True,
                    "explanation": "Trata-se de delito formal que atinge consumação instantânea com a oferta ou promessa, prescindindo da aceitação ou entrega material."
                },
                {
                    "statement": "O crime de descaminho caracteriza-se pelo ingresso clandestino de substâncias e produtos que possuem proibição absoluta de comércio nacional.",
                    "isTrue": False,
                    "explanation": "A internalização de mercadoria de importação proibida configura contrabando (art. 334-A); o descaminho recai sobre produtos lícitos com sonegação tributária."
                },
                {
                    "statement": "A pena cominada ao crime de descaminho aplica-se em dobro caso a mercadoria seja introduzida em embarcação marítima clandestina.",
                    "isTrue": True,
                    "explanation": "O art. 334, § 3º, duplica a sanção na hipótese de a importação irregular consumar-se mediante transporte aéreo, marítimo ou fluvial."
                }
            ],
            "revisao": [
                {
                    "statement": "A oferta de recompensa patrimonial efetuada para que o guarda municipal execute ato lícito de seu dever não configura crime de corrupção ativa.",
                    "isTrue": False,
                    "explanation": "O art. 333 pune a vantagem ofertada para 'praticar' ato funcional, abrangendo tanto condutas lícitas funcionais quanto atos ilícitos."
                },
                {
                    "statement": "O delito de descaminho tutela precipuamente a arrecadação aduaneira e o controle fiscal da entrada e saída de bens no território pátrio.",
                    "isTrue": True,
                    "explanation": "O bem jurídico tutelado no descaminho é a ordem tributária e a administração fazendária da União no comércio exterior."
                },
                {
                    "statement": "A apreensão de produtos eletrônicos sem tributação em depósito comercial comina pena autônoma privativa do crime de receptação culposa.",
                    "isTrue": False,
                    "explanation": "A conduta de estocar e vender mercadoria descaminhada em atividade comercial subsume-se à figura equiparada do próprio descaminho (art. 334, § 1º)."
                },
                {
                    "statement": "A comprovação de reiteração habitual profissional na atividade de descaminho autoriza o afastamento do princípio da bagatela pelos tribunais.",
                    "isTrue": True,
                    "explanation": "O STF e STJ consolidaram que a habitualidade criminosa e a contumácia fiscal afastam a aplicação da insignificância material no descaminho."
                }
            ],
            "pointers": [
                {"topic": "Corrupção ativa, núcleos típicos e bilateralidade relativa", "pageRef": 18},
                {"topic": "Majorante por ato funcional infringido no art. 333", "pageRef": 21},
                {"topic": "Descaminho material e ilusão tributária no art. 334", "pageRef": 23},
                {"topic": "Formas equiparadas comerciais e transporte qualificado", "pageRef": 26}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a08/s02",
        "fingerprint": get_fp("direito-penal/a08/s02"),
        "analytic": """Este segmento esmiúça o crime de corrupção ativa promovido por terceiros perante a máquina administrativa, confrontando-o dogmaticamente com a concussão, e analisa a tipicidade autônoma do delito aduaneiro de descaminho no artigo 334 do Código Penal.

### Corrupção ativa e a quebra da probidade (artigo 333)
O artigo 333 reprova a iniciativa do particular que pretende mercadejar a imparcialidade estatal:
- *Verbos Nucleares*: consubstancia-se nas ações de **oferecer** (apresentar diretamente a vantagem ao servidor) ou **prometer** (comprometer-se a entregar retribuição futura) proveito indevido para induzir o funcionário a praticar, retardar ou omitir ato inerente às suas atribuições funcionais;
- *Natureza Jurídica e Consumação*: cuida-se de crime formal e de consumação antecipada que se aperfeiçoa no exato instante em que a proposta venal é externada e captada pelo servidor público, mostrando-se despicienda a concordância deste. Caso o servidor recuse de pronto a propina e dê voz de prisão ao ofertante, o delito do artigo 333 resta plenamente consumado;
- *Inocorrência de Bilateralidade Necessária*: a corrupção ativa pode subsistir de forma autônoma sem correspondente corrupção passiva. De modo inverso, se o servidor público impõe e exige o pagamento da quantia (concussão), o particular que simplesmente satisfaz a exigência sob constrangimento figura na condição de sujeito passivo e não de criminoso ativo;
- *Causa de Aumento de Pena (parágrafo único)*: a sanção é majorada em **um terço** se o servidor público, seduzido pela promessa pecuniária, efetivamente corrompe seus deveres, retardando ou violando ato legal de seu ofício.

### Descaminho aduaneiro (artigo 334)
O preceito do artigo 334 tutela a integridade tributária da União e o controle aduaneiro das fronteiras:
- *Conduta Típica*: pune a ação de **iludir** (burlar, fraudar ou omitir dolosamente), no todo ou em fração, o pagamento de direitos aduaneiros ou impostos incidentes sobre a introdução, exportação ou consumo de produtos;
- *Natureza da Mercadoria*: o descaminho recai imperativamente sobre **mercadorias de importação permitida e lícita** (eletrônicos, bebidas comerciais ou tecidos autorizados). A conduta criminosa reside exclusivamente na sonegação dos tributos aduaneiros devidos na alfândega;
- *Figuras Equiparadas e Mercancia (§ 1º)*: incorre na mesma cominação de reclusão de um a quatro anos aquele que comercializa, expõe à venda, mantém em depósito em proveito próprio ou transporta mercadoria que sabe ter sido internalizada sem os devidos desembaraços alfandegários;
- *Majorante pelo Meio de Transporte (§ 3º)*: a reprimenda **aplica-se em dobro** se a evasão fiscal aduaneira for perpetrada por intermédio de transporte aéreo, marítimo ou fluvial clandestino.

### Para fixar
- A corrupção ativa atinge a consumação instantânea com a oferta da vantagem indevida ao servidor.
- O crime formal de corrupção independe da aquiescência do agente público ou do pagamento efetivo.
- O particular coagido pela exigência do policial atua como vítima de concussão e não como corruptor.
- A violação do dever de ofício pelo servidor atua como causa de aumento de um terço no art. 333.
- O descaminho recai sobre mercadorias permitidas mediante evasão do pagamento de tributos aduaneiros.
- A comercialização habitual de bens importados sem tributos amolda-se à figura equiparada do § 1º.
- O transporte aéreo ou aquático duplica a sanção punitiva imposta aos autores de descaminho.
- O princípio da insignificância incide no descaminho sob teto aduaneiro de até vinte mil reais.""",
        "synthetic": [
            "**Corrupção Ativa (art. 333)**: oferta ou promessa de remuneração ilícita para aliciar funcionário público consumada com a exteriorização da proposta.",
            "**Crime Formal Autônomo**: aperfeiçoa-se sem depender da aceitação ministerial ou da efetiva liberação de benefícios materiais pretendidos.",
            "**Distinção da Concussão**: quem entrega dinheiro compulsoriamente perante exigência estatal atua na qualidade de vítima constrangida.",
            "**Majorante da Fração Terça**: acréscimo de um terço na dosimetria caso o servidor viole formalmente seus deveres estatutários.",
            "**Descaminho Fiscal (art. 334)**: burla deliberada ao recolhimento de impostos na importação de mercadorias cuja circulação é lícita.",
            "**Figuras Equiparadas**: extensão punitiva sobre o transporte, estoque e comercialização clandestina de mercadorias sonegadoras.",
            "**Agravamento pelo Transporte**: aplicação da reprimenda penal em dobro se o descaminho valer-se de modalidade aérea ou marítima.",
            "**Teto da Insignificância**: jurisprudência assente fixando parâmetro de vinte mil reais como limite financeiro da atipicidade material."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 03: Contrabando e Tópicos Jurisprudenciais (p. 28-37)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a08/s03",
        "bizu": {
            "summary": [
                "**Contrabando (art. 334-A, caput)**: importar ou exportar mercadoria que possui proibição legal de circulação ou entrada no país (reclusão de 2 a 5 anos).",
                "**Distinção Nodal de Objeto**: no descaminho a mercadoria é permitida e sonega-se imposto; no contrabando a mercadoria é proibida em absoluto ou relativamente.",
                "**Exemplos Clássicos de Contrabando**: cigarros estrangeiros clandestinos, cigarros eletrônicos (vapes), pneus usados ou agrotóxicos desprovidos de registro.",
                "**Formas Equiparadas do Contrabando (§ 1º)**: importar clandestinamente produtos que dependem de registro sanitário ou desrespeitar normas de segurança pública.",
                "**Inaplicabilidade da Insignificância no Contrabando**: o STJ e STF vedam a bagatela no contrabando, pois o bem jurídico tutelado é a saúde e segurança pública.",
                "**Exceção Restritíssima da Bagatela**: admissão excepcionalíssima pelos tribunais em quantidades ínfimas de medicamentos para tratamento médico pessoal comprovado.",
                "**Cigarros Clandestinos e Jurisprudência**: a importação não autorizada de cigarros configura contrabando em razão da violação às normas sanitárias e de controle.",
                "**Majorante de Transporte no Contrabando (§ 3º)**: dobra-se a sanção prisional caso o contrabando seja executado em transporte aéreo, marítimo ou fluvial.",
                "**Concurso de Crimes**: a falsificação de selos de controle na entrada de produtos ilícitos pode concorrer materialmente com o contrabando."
            ],
            "teoria": [
                {
                    "statement": "O princípio da insignificância é amplamente admitido pelos tribunais superiores em relação ao crime de contrabando comum de cigarros.",
                    "isTrue": False,
                    "explanation": "A jurisprudência do STF e STJ é pacífica em afastar o princípio da insignificância no contrabando de cigarros e mercadorias proibidas."
                },
                {
                    "statement": "A internação de medicamentos de uso terapêutico desprovidos de registro prévio na Anvisa subsume-se ao tipo penal do contrabando.",
                    "isTrue": True,
                    "explanation": "A conduta enquadra-se no art. 334-A, § 1º, inciso II, por importar mercadoria que depende de registro sanitário sem autorização legal."
                },
                {
                    "statement": "O descaminho e o contrabando possuem idêntica cominação abstrata de pena, com balizas estabelecidas entre um e quatro anos de reclusão.",
                    "isTrue": False,
                    "explanation": "A Lei 13.008/2014 autonomizou os tipos: o descaminho prevê reclusão de 1 a 4 anos; o contrabando comina pena de 2 a 5 anos de reclusão."
                },
                {
                    "statement": "A exasperação da sanção penal em dobro aplica-se tanto ao descaminho quanto ao contrabando executados por transporte fluvial clandestino.",
                    "isTrue": True,
                    "explanation": "Tanto o § 3º do art. 334 quanto o § 3º do art. 334-A estabelecem o dobro da reprimenda para o transporte aéreo, marítimo ou fluvial."
                }
            ],
            "revisao": [
                {
                    "statement": "A entrada no país de produtos alimentícios com imposto de importação não recolhido configura o delito de contrabando qualificado.",
                    "isTrue": False,
                    "explanation": "Sendo mercadoria de importação permitida cuja lesão consiste na falta de recolhimento tributário, configura-se o crime de descaminho."
                },
                {
                    "statement": "O crime de contrabando tutela precipuamente a saúde pública, a segurança interna e a ordem econômica nacional.",
                    "isTrue": True,
                    "explanation": "Diferente do descaminho que visa a arrecadação, o contrabando visa a proteção de bens indisponíveis da coletividade."
                },
                {
                    "statement": "A importação desautorizada de armas de fogo e munições de uso restrito subsume-se formalmente ao artigo 334-A do Código Penal.",
                    "isTrue": False,
                    "explanation": "Armas, munições e explosivos submetem-se à tipificação especial e prevalecente do Estatuto do Desarmamento (art. 18 da Lei 10.826/2003)."
                },
                {
                    "statement": "O comerciante que expõe à venda cigarros eletrônicos sabidamente proibidos no Brasil responde pelas formas equiparadas do contrabando.",
                    "isTrue": True,
                    "explanation": "O art. 334-A, § 1º, V, equipara a conduta de quem comercializa ou expõe à venda mercadoria de importação proibida em território nacional."
                }
            ],
            "pointers": [
                {"topic": "Contrabando e autonomia típica pela Lei 13.008/2014", "pageRef": 29},
                {"topic": "Formas equiparadas sanitárias e cigarros no art. 334-A", "pageRef": 31},
                {"topic": "Inaplicabilidade da insignificância perante bens supraindividuais", "pageRef": 33},
                {"topic": "Majorante de modal aquático e aéreo e conflito com leis especiais", "pageRef": 36}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a08/s03",
        "fingerprint": get_fp("direito-penal/a08/s03"),
        "analytic": """Este segmento aprofunda a dogmática aduaneira criminalizada, focando na figura autônoma do delito de contrabando positivado no artigo 334-A do Código Penal, suas diferenças em face do descaminho e as diretrizes consolidadas nas Cortes Superiores.

### Autonomia típica do contrabando (artigo 334-A)
Historicamente reunidos em um preceito comum, o contrabando e o descaminho foram definitivamente apartados pela Lei nº 13.008/2014:
- *Elemento Nuclear*: o artigo 334-A tipifica a ação de **importar ou exportar mercadoria proibida**, cominando sanção punitiva mais gravosa de **reclusão de dois a cinco anos**;
- *Objeto Material*: diferentemente do descaminho (que visa tributos sonegados sobre bens lícitos), o contrabando incide sobre coisas cuja circulação interna ou internacional seja **absoluta ou relativamente vedada pelo ordenamento jurídico** (cigarros sem fiscalização da Anvisa, dispositivos eletrônicos de fumo, agrotóxicos proibidos, peles de animais silvestres, peças automotivas usadas);
- *Distinção com Leis Especiais*: se a mercadoria proibida consistir em substâncias entorpecentes ou drogas ilícitas, incide a Lei nº 11.343/2006 (tráfico transnacional de drogas); caso envolva armamentos, artefatos explosivos ou munições, aplica-se o Estatuto do Desarmamento (Lei nº 10.826/2003), afastando o artigo 334-A pelo princípio da especialidade.

### Modalidades equiparadas e mercancia (§ 1º)
O legislador estendeu as sanções punitivas do contrabando a etapas sucessivas do ciclo de dispersão clandestina:
- Praticar fato que a lei assimila a contrabando em legislação extravagante aduaneira;
- Importar ou exportar produtos desprovidos de registro, chancela ou inspeção de órgãos oficiais competentes de fiscalização sanitária ou ambiental;
- Comercializar, manter armazenado em ponto de venda, repassar ou expor ao público consumidor produto de importação expressamente vedada por regramento legal.

### Tópicos jurisprudenciais e insignificância material
O tratamento dispensado pelos tribunais superiores expressa o elevado desvalor do contrabando:
- *Inaplicabilidade da Bagatela*: o Superior Tribunal de Justiça e o Supremo Tribunal Federal firmaram entendimento dominante no sentido de que **é inaplicável o princípio da insignificância ao delito de contrabando**. Essa orientação justifica-se pelo fato de que o bem jurídico primário tutelado não ostenta índole contábil ou fiscal, mas abarca a **saúde pública, a segurança sanitária da coletividade, o meio ambiente e a ordem industrial nacional**;
- *Cigarros e Produtos Médicos*: o contrabando de cigarros não admite a tese bagatelar em virtude do risco sanitário evidente e fomento ao crime transnacional. Excepciona-se pontualmente a jurisprudência apenas em hipóteses estritas e humanitárias de importação de ínfima quantidade de medicamentos voltados ao consumo pessoal e tratamento de moléstia grave atestada;
- *Majorante pelo Transporte (§ 3º)*: incide a **duplicação obrigatória da reprimenda penal** cominada caso a prática de contrabando envolva o transporte por meio de aeronaves, navios ou embarcações em bacias fluviais.

### Para fixar
- A Lei 13.008/2014 individualizou o contrabando cominando reprimenda severa de 2 a 5 anos de reclusão.
- O contrabando recai sobre produtos com proibição de entrada absoluta ou condicionada à inspeção.
- A importação não autorizada de armas de fogo e drogas configura crimes previstos em leis especiais.
- Vender produtos de circulação vedada no comércio urbano subsume-se à forma equiparada do contrabando.
- O princípio da insignificância é manifestamente inaplicável ao crime de contrabando nos tribunais.
- A proteção à saúde pública e segurança sanitária afasta a invocação do valor pecuniário diminuto.
- A importação clandestina de cigarros caracteriza contrabando em face do descumprimento de normas sanitárias.
- A sanção do contrabando dobra de patamar na utilização de transporte aéreo, marítimo ou fluvial.""",
        "synthetic": [
            "**Contrabando Autônomo (art. 334-A)**: ingresso clandestino de produtos submetidos a veto normativo sancionado com reclusão de dois a cinco anos.",
            "**Bens Tutelados Supraindividuais**: o tipo salvaguarda a higidez da saúde coletiva, segurança sanitária e preservação ambiental nacional.",
            "**Especialidade Punitiva**: trânsito de entorpecentes ou armamentos afasta o Código Penal em favor de diplomas regulamentares específicos.",
            "**Formas Equiparadas no Comércio**: extensão das sanções aos que expõem à venda mercadoria desprovida de validação dos órgãos federais.",
            "**Vedação à Insignificância**: jurisprudência reiterada recusando o princípio bagatelar ante a lesividade ínsita aos vetos aduaneiros.",
            "**Rigor sobre Cigarros Ilícitos**: rechaço contundente da tese da bagatela na importação desautorizada de tabaco desprovido de registro sanitário.",
            "**Exceção Médica Humanitária**: flexibilização extraordinária autorizada apenas para remédios vitais em quantitativo puramente pessoal.",
            "**Majorante pelo Transporte**: duplicação automática da resposta penal caso a mercadoria adentre o país por via aérea ou fluvial."
        ]
    })

    return items, summaries
