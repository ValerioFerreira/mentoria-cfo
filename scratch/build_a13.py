import json
import subprocess
from pathlib import Path

# AULA 13: Lei 13.869/2019 (Abuso de Autoridade)

items_a13 = {
  "aula": "legislacao-penal-especial/a13",
  "batch": "pcpe-bizu-legislacao-penal-especial",
  "status": "DRAFT",
  "stage": "bizu",
  "segments": [
    {
      "id": "legislacao-penal-especial/a13/s01",
      "bizu": {
        "summary": [
          "**Elemento subjetivo especial**: exige-se cumulativamente dolo e finalidade específica de prejudicar outrem, beneficiar a si ou terceiro, ou satisfazer mero capricho pessoal.",
          "**Crime de hermenêutica vedado**: a divergência razoável na exegese e interpretação da legislação ou na valoração dos fatos e provas jamais configura abuso de autoridade.",
          "**Conceito amplo de agente**: alcança servidores estatutários, celetistas, ocupantes de cargos em comissão, membros de Poderes e agentes temporários ou honoríficos sem remuneração.",
          "**Concurso com particular**: o particular pode figurar como coautor ou partícipe de abuso de poder desde que atue em conluio com o agente público e conheça sua condição funcional.",
          "**Regime da ação penal**: os delitos processam-se mediante ação penal pública incondicionada, viabilizando-se a queixa subsidiária caso o Ministério Público permaneça inerte no prazo legal.",
          "**Efeitos da condenação**: a perda da função e a inabilitação para o serviço público por um a cinco anos não são automáticas e dependem obrigatoriamente de reincidência específica.",
          "**Efeito automático reparatório**: apenas a reparação e fixação de indenização mínima pelo dano provocado apresenta eficácia automática dentre os efeitos penais secundários.",
          "**Penas substitutivas**: admitem-se prestação de serviços comunitários e suspensão do exercício funcional de um a seis meses com perda dos vencimentos, isoladas ou cumuladas."
        ],
        "teoria": [
          {
            "statement": "A simples conduta culposa do servidor público que causa prejuízo por negligência na interpretação legal pode ser punida a título de abuso de autoridade culposo.",
            "isTrue": False,
            "explanation": "A Lei 13.869/2019 não prevê modalidade culposa, exigindo obrigatoriamente o dolo associado ao elemento subjetivo especial de prejudicar, beneficiar ou capricho."
          },
          {
            "statement": "Qualquer indivíduo que exerça função pública, ainda que de forma transitória e sem remuneração, é considerado agente público para os efeitos da Lei 13.869/2019.",
            "isTrue": True,
            "explanation": "O art. 2º, parágrafo único, conceitua agente público de forma extensiva, abrangendo quem atua temporariamente ou sem contraprestação financeira."
          },
          {
            "statement": "A perda do cargo público e a inabilitação para funções estatais operam de maneira automática em qualquer condenação transitada em julgado por abuso de poder.",
            "isTrue": False,
            "explanation": "Nos termos do art. 4º, parágrafo único, a perda do cargo e a inabilitação exigem motivação expressa e são condicionadas à reincidência específica."
          },
          {
            "statement": "Admite-se o ajuizamento de ação penal privada subsidiária da pública se o órgão ministerial não oferecer a denúncia no lapso temporal previsto na lei adjetiva.",
            "isTrue": True,
            "explanation": "O art. 3º, § 1º, assegura expressamente a propositura da queixa-crime subsidiária da pública diante da desídia ou inércia do titular da ação penal."
          }
        ],
        "revisao": [
          {
            "statement": "A divergência jurídica fundamentada na valoração de provas periciais pelo delegado de polícia tipifica o crime de hermenêutica previsto na legislação especial.",
            "isTrue": False,
            "explanation": "O art. 1º, § 2º, estabelece expressamente que a divergência hermenêutica na análise de diplomas normativos ou na apreciação de elementos probatórios não configura ilícito penal."
          },
          {
            "statement": "O particular que não ostenta vínculo funcional com o Estado pode responder por abuso de autoridade em coautoria se possuir ciência da qualidade pública do comparsa.",
            "isTrue": True,
            "explanation": "Por força do art. 30 do Código Penal, a condição de funcionário público comunica-se ao coautor ou partícipe particular desde que este a conheça previamente."
          },
          {
            "statement": "A absolvição penal fundada na ausência de provas suficientes para a condenação vincula obrigatoriamente a esfera administrativa disciplinar da corporação.",
            "isTrue": False,
            "explanation": "Apenas a sentença penal absolutória que reconhece categoricamente a inexistência material do fato ou a negativa de autoria vincula as instâncias cível e disciplinar."
          },
          {
            "statement": "A pena restritiva de direitos de suspensão do exercício do cargo pode ser fixada pelo prazo de um a seis meses, implicando a perda integral da remuneração correspondente.",
            "isTrue": True,
            "explanation": "Conforme o art. 5º, II, da Lei 13.869/2019, a suspensão do cargo perdura de um a seis meses, com a perda da remuneração e dos direitos inerentes ao período."
          }
        ],
        "pointers": [
          {"topic": "Finalidade específica e vedação à hermenêutica", "pageRef": 3},
          {"topic": "Sujeito ativo amplo e concurso com particulares", "pageRef": 5},
          {"topic": "Ação penal pública e queixa subsidiária", "pageRef": 7},
          {"topic": "Efeitos da condenação e penas restritivas", "pageRef": 8}
        ]
      }
    },
    {
      "id": "legislacao-penal-especial/a13/s02",
      "bizu": {
        "summary": [
          "**Mandado de busca domiciliar**: comete crime a autoridade que cumpre mandado de busca e apreensão na casa do investigado entre as 21 horas e as 5 horas.",
          "**Execução de prisão ilegal**: decretar ou executar privação de liberdade sem amparo legal ou deixar de relaxar custódia ilegal comunicada gera infração penal autônoma.",
          "**Comunicação da custódia**: postergar ou omitir a comunicação da prisão ao juízo competente, à família do preso ou ao seu defensor configura ilícito específico.",
          "**Interrogatório no período noturno**: interrogar formalmente o capturado entre 21h e 5h tipifica abuso, salvo se ocorrido em flagrante delito ou com assentimento do indiciado assistido por advogado.",
          "**Constrangimento indevido**: submeter preso ao uso de algemas sem necessidade comprovada ou expô-lo coercitivamente à execração e curiosidade pública configura tipo penal próprio.",
          "**Prerrogativas da advocacia**: impedir o contato pessoal e reservado do advogado com o cliente preso ou obstar acesso a peças investigatórias finalizadas atrai repressão da lei.",
          "**Violência institucional**: tipificou-se a conduta de expor a vítima de infração violenta a procedimentos desnecessários, vexatórios ou repetitivos que ensejem revitimização.",
          "**Antecipação de culpa**: atribuir publicamente culpa a suspeito ou investigado pelas redes sociais ou imprensa antes de formalizada a acusação é conduta expressamente vedada."
        ],
        "teoria": [
          {
            "statement": "O cumprimento de mandado judicial de busca e apreensão no interior de residência pode ser deflagrado licitamente às 22 horas, desde que o imóvel esteja habitado.",
            "isTrue": False,
            "explanation": "O art. 22, § 1º, III, criminaliza expressamente a execução de mandado judicial de busca e apreensão domiciliar entre as 21 horas e as 5 horas."
          },
          {
            "statement": "Configura abuso de autoridade constranger testemunha ou vítima a prestar depoimento sobre circunstâncias protegidas por sigilo profissional legal.",
            "isTrue": True,
            "explanation": "O art. 15, parágrafo único, incrimina o ato de prosseguir com interrogatório de pessoa que, por dever de função, ministério ou ofício, deva guardar segredo."
          },
          {
            "statement": "A realização de interrogatório do detido durante o período noturno é admitida livremente pela autoridade policial sempre que houver necessidade de colheita célere.",
            "isTrue": False,
            "explanation": "O interrogatório entre 21h e 5h é crime (art. 18), ressalvando-se exclusivamente as hipóteses de flagrante delito ou prévio consentimento voluntário assistido por defensor."
          },
          {
            "statement": "A prática de violência institucional pune o agente público que submete a vítima de violência a questionamentos desarrazoados sobre sua intimidade pretérita.",
            "isTrue": True,
            "explanation": "O art. 15-A pune a violência institucional consistente em submeter a vítima de infração violenta a procedimentos repetitivos, invasivos ou desnecessários."
          }
        ],
        "revisao": [
          {
            "statement": "O policial que deixa de apor identificação pessoal na vestimenta durante o cumprimento de mandado de prisão não pratica crime tipificado na Lei 13.869/2019.",
            "isTrue": False,
            "explanation": "O art. 16 pune o agente que oculta a sua identidade ou atribui a si qualificativos inverídicos perante o indivíduo custodiado no ato da detenção."
          },
          {
            "statement": "Negar ao advogado o acesso aos elementos de prova já documentados em procedimento investigatório que digam respeito ao direito de defesa do investigado configura abuso.",
            "isTrue": True,
            "explanation": "O art. 32 tutela as prerrogativas da advocacia e reproduz o teor da Súmula Vinculante 14, criminalizando a negativa de acesso aos autos já concluídos."
          },
          {
            "statement": "A divulgação em redes sociais oficiais de imagem do investigado detido para satisfazer a curiosidade pública constitui ato discricionário admitido sem restrições penais.",
            "isTrue": False,
            "explanation": "O art. 13 pune expressamente o ato de constranger o detido mediante exibição à curiosidade pública, além do art. 38 vedar a antecipação precipitada de culpa."
          },
          {
            "statement": "A decretação judicial cautelar de indisponibilidade de patrimônio financeiro em montante que exceda patentemente o valor estimado da reparação do dano é tipificada na lei.",
            "isTrue": True,
            "explanation": "O art. 36 pune a conduta de decretar indisponibilidade de bens ou valores em quantia manifestamente desproporcional ou que extrapole a dívida estimada."
          }
        ],
        "pointers": [
          {"topic": "Prisão ilegal e restrição cautelar indevida", "pageRef": 12},
          {"topic": "Mandado domiciliar noturno e busca e apreensão", "pageRef": 18},
          {"topic": "Prerrogativas da defesa e interrogatório policial", "pageRef": 21},
          {"topic": "Violência institucional e antecipação de juízo", "pageRef": 26}
        ]
      }
    }
  ]
}

# RESUMOS A13
summaries_a13 = {
  "aula": "legislacao-penal-especial/a13",
  "batch": "pcpe-summary-legislacao-penal-especial",
  "status": "DRAFT",
  "segments": [
    {
      "id": "legislacao-penal-especial/a13/s01",
      "fingerprint": {
        "startPage": 3,
        "endPage": 11,
        "startTopic": "Lei nº 13.869/2019 — Disposições Gerais, Sujeitos e Efeitos da Condenação"
      },
      "analytic": """A Lei 13.869/2019 reformulou integralmente o regime jurídico dos crimes de abuso de autoridade no direito brasileiro, revogando o diploma anterior (Lei 4.898/1965). O novo marco equilibrou a repressão a condutas arbitrárias com garantias protetivas ao regular desempenho das funções estatais em todas as esferas federativas.

### Elemento Subjetivo e Vedação ao Crime de Hermenêutica
O traço distintivo fundamental da Lei de Abuso de Autoridade repousa em sua conformação anímica:
- **Exigência do Dolo Específico**: as condutas descritas na lei demandam o dolo clássico acrescido de uma motivação teleológica especial expressa no art. 1º, § 1º:
  1. A finalidade específica de prejudicar terceiro;
  2. A intenção deliberada de beneficiar a si próprio ou a outrem;
  3. A atuação movida por mero capricho individual ou satisfação pessoal.
- **Inexistência de Abuso Culposo**: não existe figura culposa na Lei 13.869/2019, tampouco responsabilidade penal lastreada em dolo genérico sem o ânimo persecutório abusivo;
- **Proibição do Crime de Hermenêutica**: o art. 1º, § 2º, consagra que a divergência na exegese de preceitos normativos ou na valoração de elementos instrutórios e probatórios jamais tipifica abuso de poder. Essa blindagem preserva a independência decisória de juízes, membros ministeriais, delegados de polícia e fiscais administrativos.

### Sujeito Ativo e Concurso de Pessoas
A abrangência do conceito de agente público é traçada no art. 2º da norma:
- **Conceito Abrangente**: enquadra-se como autor qualquer indivíduo que atue no serviço estatal, mesmo com vínculo transitório, temporário ou sem estipêndio financeiro, por via de designação, nomeação ou sufrágio popular nos Poderes Executivo, Legislativo e Judiciário, Ministério Público e Tribunais de Contas;
- **Agentes Honoríficos e Temporários**: jurados do Tribunal do Júri, mesários eleitorais e estagiários do serviço público subsumem-se ao conceito normativo de agente público durante o exercício da função;
- **Participação do Particular**: por ser crime próprio, exige a qualidade especial de agente estatal, mas admite a coautoria ou participação de particular desde que este conheça a condição funcional do comparsa (art. 30 do Código Penal).

### Ação Penal e Efeitos da Condenação
- **Natureza da Ação Penal**: os crimes da lei são apurados privativamente mediante **ação penal pública incondicionada** (art. 3º). Admite-se a propositura de queixa subsidiária da pública caso o Ministério Público não ofereça denúncia no prazo legal do art. 46 do CPP (art. 3º, § 1º);
- **Efeitos Secundários da Condenação (art. 4º)**:
  1. Tornar certa a obrigação de indenizar o dano causado (único efeito **automático**);
  2. O impedimento temporário para o exercício de funções estatais e mandatos pelo intervalo de um a cinco anos;
  3. A perda definitiva do posto, cargo ou emprego público.
- **Condicionamento dos Efeitos Graves**: a perda da função pública e a inabilitação **não são automáticas**, exigindo expressa fundamentação judicial, e são **condicionadas à reincidência específica** em crime de abuso de autoridade;
- **Penas Restritivas Substitutivas (art. 5º)**: a prestação de serviços à comunidade e a suspensão do exercício funcional por um a seis meses com supressão de vencimentos podem substituir as penas corporais privativas de liberdade.

### Para fixar
- Não existe modalidade culposa na Lei de Abuso de Autoridade; exige-se sempre dolo específico.
- A divergência interpretativa na valoração de fatos ou leis não tipifica infração criminal.
- Agentes honoríficos ou transitórios sem remuneração podem ser sujeitos ativos da lei.
- O particular responde em coautoria se conhecer a condição funcional do agente público.
- A ação penal é pública incondicionada, admitindo ação privada subsidiária por inércia ministerial.
- A perda do cargo público reclama reincidência específica em abuso de autoridade e motivação judicial.""",
      "synthetic": [
        "**Dolo específico obrigatório**: a punição reclama o propósito explícito de prejudicar outrem, beneficiar terceiro ou mero capricho.",
        "**Hermenêutica preservada**: divergências razoáveis na interpretação da norma ou provas não geram abuso de autoridade.",
        "**Sujeitos ativos amplos**: engloba qualquer servidor com ou sem remuneração, temporário, estagiário ou mesário eleitoral.",
        "**Coautoria com particular**: o particular responde pelo delito desde que atue em conluio consciente da função do agente.",
        "**Ação incondicionada**: a apuração dá-se via ação pública incondicionada, com espaço para a queixa privada subsidiária.",
        "**Perda do cargo público**: a destituição funcional condiciona-se à reincidência específica em abuso e à fundamentação judicial.",
        "**Indenização automática**: a obrigação civil de reparar o dano causado à vítima é o único efeito automático da condenação."
      ]
    },
    {
      "id": "legislacao-penal-especial/a13/s02",
      "fingerprint": {
        "startPage": 12,
        "endPage": 27,
        "startTopic": "Crimes em Espécie na Lei de Abuso de Autoridade"
      },
      "analytic": """A parte especial da Lei 13.869/2019 tipifica comportamentos abusivos cometidos no âmbito da persecução criminal, medidas cautelares, execução da prisão, audiências e investigações estatais. O conhecimento pormenorizado das elementares é indispensável para evitar armadilhas nas provas de concursos jurídicos e policiais.

### Violações ao Estatuto da Prisão e Custódia
O diploma pune com vigor a extrapolação do poder coercitivo estatal contra a liberdade de locomoção:
- **Prisão Ilegal e Omissão Cautelar (art. 9º)**: decretar ou executar medida privativa de liberdade em manifesta desconformidade com as hipóteses legais, bem como deixar o magistrado de relaxar prisão ilegal que lhe seja formalmente informada;
- **Omissão nas Comunicações da Prisão (art. 12)**: deixar a autoridade de comunicar a prisão em flagrante ao juiz e à família do preso ou pessoa por ele indicada no prazo legal, ou omitir a soltura determinada por ordem judicial;
- **Constrangimento Ilegal do Custodiado (art. 13)**: constranger o capturado, empregando sevícias, intimidação relevante ou diminuindo as condições de defesa da vítima, com o fim de expor seu corpo ou imagem à execração ou curiosidade pública desarrazoada;
- **Uso Abusivo de Algemas**: embora a lei não traga tipo penal intitulado 'uso de algemas', a contenção abusiva sem amparo na Súmula Vinculante 11 (que exige perigo à integridade, resistência ou risco de fuga) enquadra-se no art. 13;
- **Identificação Policial na Captura (art. 16)**: deixar o policial executor da captura de identificar-se ou identificar-se com nome falso perante o preso;
- **Interrogatório Policial Noturno (art. 18)**: realizar interrogatório formal de pessoa recolhida durante o período noturno (compreendido entre 21 horas e 5 horas), ressalvadas as hipóteses de flagrante delito ou de expresso consentimento do autuado perante seu defensor legal.

### Violação de Domicílio e Garantias da Defesa
- **Invasão Domiciliar por Busca Noturna (art. 22)**: cumprir mandado judicial de busca e apreensão domiciliar após as 21 horas ou antes das 5 horas consubstancia crime autônomo com pena de detenção de 1 a 4 anos e multa. Trata-se de limitação temporal legal expressa que balizou o conceito constitucional de 'dia';
- **Impedimento de Prerrogativas Advocatícias (arts. 20 e 32)**: impedir o advogado de entrevistar-se pessoal e reservadamente com o cliente preso (art. 20), ou sonegar ao defensor acesso a peças de investigação já documentadas pertinentes ao cliente (art. 32), violando a Súmula Vinculante 14.

| Conduta Proibida | Dispositivo Legal | Exceção / Condição Legal |
|---|---|---|
| Busca domiciliar noturna | Art. 22, § 1º, III | Válida somente entre 5h e 21h |
| Interrogatório à noite | Art. 18 | Válido se flagrante ou consentimento assistido |
| Negativa de acesso aos autos | Art. 32 | Provas em andamento podem ser sigilosas |
| Bloqueio patrimonial abusivo | Art. 36 | Deve limitar-se ao débito estimado |

### Violência Institucional e Publicidade Indevida
Inovações substantivas foram agregadas à sistemática repressiva:
- **Violência Institucional (art. 15-A)**: tipifica a conduta de submeter vítima de infração violenta ou testemunha a procedimentos desnecessários, invasivos ou reiterados que a façam reviver o sofrimento ou trauma pretérito, bem como permitir que terceiros intimidem a vítima em audiência;
- **Indisponibilidade Excessiva de Bens (art. 36)**: decretar judicialmente indisponibilidade de ativos financeiros em valor exorbitante que extrapole manifestamente o montante estimado para ressarcimento;
- **Antecipação Precipitada de Culpa (art. 38)**: divulgar por meios de comunicação ou redes sociais atribuição de responsabilidade criminal a investigado antes de formada a convicção acusatória formal.

### Para fixar
- É expressamente proibido cumprir mandado de busca domiciliar entre as 21 horas e as 5 horas.
- O interrogatório noturno de detido é crime, exceto em flagrante ou com seu assentimento voluntário.
- Negar entrevista reservada entre defensor e preso caracteriza abuso de autoridade.
- A autoridade é obrigada a identificar-se com fidelidade ao realizar a prisão do indivíduo.
- A violência institucional tutela vítimas e testemunhas contra procedimentos repetitivos revitimizantes.
- É vedado ao agente público antecipar juízo de culpa nas redes sociais antes da formalização do inquérito.""",
      "synthetic": [
        "**Horário do mandado de busca**: o cumprimento de busca e apreensão domiciliar é vedado entre as 21 horas e as 5 horas.",
        "**Interrogatório prohibited**: o interrogatório no intervalo de 21h às 5h tipifica crime, salvo flagrante ou anuência assistida.",
        "**Garantia de comunicação**: a omissão deliberada na comunicação imediata da prisão ao juiz configura delito especial.",
        "**Uso vexatório de algemas**: constranger detido ao exibicionismo público ou sujeição arbitrária acarreta responsabilização penal.",
        "**Prerrogativa do patrono**: barrar o diálogo reservado do advogado com o cliente preso atrai as sanções da Lei 13.869/2019.",
        "**Violência institucional**: pune-se a revitimização desnecessária de vítimas e testemunhas em audiências ou depoimentos.",
        "**Veto à antecipação de culpa**: agentes estatais não podem assacar juízos públicos de condenação pelas mídias e redes sociais."
      ]
    }
  ]
}

Path("content/items/legislacao-penal-especial/a13.json").write_text(json.dumps(items_a13, ensure_ascii=False, indent=2), encoding="utf-8")
Path("content/summaries/legislacao-penal-especial/a13.json").write_text(json.dumps(summaries_a13, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved a13 files successfully.")
