import json
import subprocess
from pathlib import Path

# AULA 17: Lei 11.340/2006 (Lei Maria da Penha)

items_a17 = {
  "aula": "legislacao-penal-especial/a17",
  "batch": "pcpe-bizu-legislacao-penal-especial",
  "status": "DRAFT",
  "stage": "bizu",
  "segments": [
    {
      "id": "legislacao-penal-especial/a17/s01",
      "bizu": {
        "summary": [
          "**Sujeito passivo qualificado**: a tutela especial da Lei 11.340/2006 destina-se exclusivamente à mulher, englobando juridicamente a mulher transexual conforme orientação do STJ.",
          "**Âmbitos de incidência**: a violência doméstica manifesta-se na unidade doméstica, no seio da família ou em qualquer relação íntima de afeto presente ou pretérita.",
          "**Desnecessidade de coabitação**: a incidência da lei independe de o agressor conviver sob o mesmo teto que a vítima, conforme pacificado na Súmula 600 do STJ.",
          "**Formas de violência**: o art. 7º cataloga cinco modalidades: violência física, violência psicológica, violência sexual, violência patrimonial e violência moral.",
          "**Afastamento da Lei 9.099/1995**: veda-se integralmente a aplicação da Lei dos Juizados Especiais, impedindo transação penal e suspensão condicional do processo.",
          "**Ação pública incondicionada**: a ação penal nas lesões corporais dolosas cometidas em ambiente doméstico contra a mulher é sempre pública incondicionada.",
          "**Vedações penais e benesses**: proíbe-se a fixação de penas de prestação pecuniária isolada e o fornecimento de cestas básicas na condenação.",
          "**Inaplicabilidade da insignificância**: não se admite a incidência do princípio da bagatela ou insignificância perante delitos ou contravenções no contexto doméstico."
        ],
        "teoria": [
          {
            "statement": "A aplicação protetiva da Lei Maria da Penha exige a demonstração inequívoca de que o agressor e a ofendida residam no mesmo imóvel no momento da conduta.",
            "isTrue": False,
            "explanation": "A Súmula 600 do STJ estabelece expressamente que para a configuração da violência doméstica contra a mulher independe a coabitação entre autor e vítima."
          },
          {
            "statement": "A retenção, a subtração ou a destruição parcial de instrumentos de trabalho da mulher pelo companheiro caracteriza violência patrimonial típica.",
            "isTrue": True,
            "explanation": "O art. 7º, IV, da Lei 11.340/2006 define a violência patrimonial como qualquer conduta que configure retenção, subtração ou dano a bens ou instrumentos de trabalho."
          },
          {
            "statement": "Nos crimes de lesão corporal leve praticados em âmbito doméstico contra a mulher, a ação penal depende de representação da vítima no prazo decadencial de seis meses.",
            "isTrue": False,
            "explanation": "A Súmula 542 do STJ e o STF consagraram que a ação penal por lesão corporal no contexto doméstico é pública incondicionada, dispensando representação."
          },
          {
            "statement": "É terminantemente vedada a imposição de penas pecuniárias de pagamento de cestas básicas aos condenados no âmbito da Lei Maria da Penha.",
            "isTrue": True,
            "explanation": "O art. 17 veda a cominação de penas de fornecimento de cestas básicas ou outras prestações pecuniárias desprovidas de caráter sancionatório pessoal."
          }
        ],
        "revisao": [
          {
            "statement": "O princípio da insignificância pode ser acolhido judicialmente nos crimes de lesão corporal cometidos em contexto de violência familiar quando a escoriação for mínima.",
            "isTrue": False,
            "explanation": "A Súmula 589 do STJ afirma que é inaplicável o princípio da insignificância aos crimes e contravenções penais praticados contra a mulher no âmbito doméstico."
          },
          {
            "statement": "A mulher transexual goza da proteção integral dos mecanismos protetivos e sancionatórios estabelecidos pela Lei Maria da Penha.",
            "isTrue": True,
            "explanation": "O Superior Tribunal de Justiça firmou entendimento de que a Lei 11.340/2006 incide em favor de mulheres transgênero e transexuais vítimas de violência de gênero."
          },
          {
            "statement": "O instituto despenalizador da suspensão condicional do processo da Lei 9.099/1995 é plenamente compatível com os delitos tutelados na Lei 11.340/2006.",
            "isTrue": False,
            "explanation": "O art. 41 da Lei Maria da Penha e a Súmula 536 do STJ proíbem expressamente a aplicação de qualquer instituto da Lei 9.099/1995 nos crimes de violência doméstica."
          },
          {
            "statement": "A conduta de constranger a mulher mediante humilhação, isolamento e controle constante de suas ações sociais configura hipótese de violência psicológica.",
            "isTrue": True,
            "explanation": "O art. 7º, II, tipifica a violência psicológica como a ação causadora de dano emocional, humilhação, vigilância constante ou diminuição da autoestima."
          }
        ],
        "pointers": [
          {"topic": "Diretrizes e finalidades protetivas da mulher", "pageRef": 3},
          {"topic": "Relação íntima de afeto e desnecessidade de coabitação", "pageRef": 5},
          {"topic": "Formas de violência: psicológica, moral e patrimonial", "pageRef": 8},
          {"topic": "Inaplicabilidade dos juizados especiais e súmulas", "pageRef": 12}
        ]
      }
    },
    {
      "id": "legislacao-penal-especial/a17/s02",
      "bizu": {
        "summary": [
          "**Atendimento policial prioritário**: a mulher em situação de violência doméstica tem direito a atendimento policial ininterrupto, especializado e prestado preferencialmente por servidoras.",
          "**Diretrizes de inquirição humanizada**: a oitiva deve evitar a revitimização, ocorrendo em recinto acolhedor e resguardada a integridade física e moral da declarante.",
          "**Diligências policiais emergenciais**: incumbe à autoridade assegurar escolta policial, fornecer transporte seguro para abrigo e acompanhar a retirada de pertences pessoais do lar.",
          "**Remessa do pedido protetivo**: o requerimento da ofendida postulando medidas protetivas deve ser protocolizado e remetido ao juiz no prazo máximo de quarenta e oito horas.",
          "**Afastamento cautelar do agressor**: verificada situação de risco atual ou iminente, o agressor poderá ser afastado compulsoriamente do domicílio conjugal por ordem de urgência.",
          "**Competência escalonada para afastamento**: o afastamento do lar cabe ao juiz; não sendo o município sede de comarca, ao delegado; e não havendo delegado, ao policial executor.",
          "**Controle judicial do ato policial**: nas hipóteses de afastamento determinado por delegado ou policial, o juiz deve ser comunicado em até vinte e quatro horas para ratificação.",
          "**Laudos e perícias prioritárias**: as guias de requisição pericial e exames de lesões corporais gozam de prioridade absoluta nos órgãos do Instituto de Medicina Legal."
        ],
        "teoria": [
          {
            "statement": "O policial civil de plantão no município que não seja comarca pode determinar o afastamento do agressor do lar mesmo quando o delegado de polícia estiver presente na delegacia.",
            "isTrue": False,
            "explanation": "Pelo art. 12-C do diploma, o agente policial comum somente possui atribuição supletiva quando a localidade não abrigar sede judiciária de comarca e faltar delegado de plantão no momento."
          },
          {
            "statement": "A autoridade policial tem o dever legal de encaminhar ao juízo competente o expediente com o pedido de medidas protetivas da vítima em até quarenta e oito horas.",
            "isTrue": True,
            "explanation": "O art. 12, III, impõe o prazo peremptório de 48 horas para que a autoridade policial remeta ao magistrado o requerimento de medidas protetivas de urgência."
          },
          {
            "statement": "O afastamento cautelar do agressor do lar imposto por delegado de polícia em município desprovido de comarca prescinde de qualquer comunicação posterior ao Poder Judiciário.",
            "isTrue": False,
            "explanation": "Conforme o art. 12-C, § 1º, o juiz deve ser comunicado no prazo máximo de 24 horas, cabendo-lhe decidir pela manutenção ou revogação da ordem no mesmo prazo."
          },
          {
            "statement": "O atendimento prestado à mulher vítima de violência doméstica em sede policial deve ser realizado, preferencialmente, por servidores públicos do sexo feminino.",
            "isTrue": True,
            "explanation": "O art. 10-A, § 2º, assegura expressamente que a inquirição da mulher em situação de violência seja feita preferencialmente por servidoras policiais."
          }
        ],
        "revisao": [
          {
            "statement": "A realização de perguntas sucessivas sobre a vida íntima pregressa da ofendida durante a lavratura da ocorrência policial constitui procedimento ordinário lícito.",
            "isTrue": False,
            "explanation": "O art. 10-A veda expressamente a revitimização, proibindo perguntas sobre a vida pretérita que não guardem estrita pertinência com o fato delituoso apurado."
          },
          {
            "statement": "Dentre as medidas imediatas cabíveis, a autoridade policial deve assegurar acompanhamento armado à ofendida para a retirada de seus pertences do domicílio.",
            "isTrue": True,
            "explanation": "O art. 11, II, incumbe expressamente à autoridade policial acompanhar a mulher para resgatar seus objetos de uso pessoal e instrumentos de labor do lar."
          },
          {
            "statement": "O juiz de direito comunicado sobre o afastamento do lar deferido pelo delegado tem o prazo de setenta e duas horas para decidir sobre a sua homologação.",
            "isTrue": False,
            "explanation": "O prazo judicial para deliberar sobre a manutenção ou revogação da medida de afastamento emergencial é de 24 horas (art. 12-C, § 1º)."
          },
          {
            "statement": "A autoridade policial pode requerer diretamente a concessão de medidas protetivas de urgência em favor da ofendida quando registrar o boletim de ocorrência.",
            "isTrue": True,
            "explanation": "O art. 12 autoriza a remessa do requerimento da vítima acompanhado de representação policial fundamentada ao Poder Judiciário."
          }
        ],
        "pointers": [
          {"topic": "Diretrizes de atendimento e inquirição humanizada", "pageRef": 15},
          {"topic": "Diligências protetivas imediatas da autoridade policial", "pageRef": 18},
          {"topic": "Afastamento emergencial do agressor do domicílio", "pageRef": 21},
          {"topic": "Remessa judicial e prazos do art. 12-C", "pageRef": 25}
        ]
      }
    },
    {
      "id": "legislacao-penal-especial/a17/s03",
      "bizu": {
        "summary": [
          "**Prazo de deliberação judicial**: o magistrado deve apreciar e deliberar sobre as medidas protetivas de urgência no prazo improrrogável de quarenta e oito horas.",
          "**Medidas que obrigam o agressor**: incluem afastamento do lar, proibição de aproximação e de contato, suspensão de visitas e restrição ao porte ou posse de arma de fogo.",
          "**Restrição de armamento**: deferida a medida restritiva bélica, o juiz deve notificar prontamente o comando da corporação militar ou o órgão policial ao qual o agressor pertença.",
          "**Medidas de amparo à vítima**: abrangem separação de corpos, alimentos provisionais, restituição de bens subtraídos e reintegração da ofendida na posse da residência.",
          "**Tipo penal do art. 24-A**: tipifica criminalmente o descumprimento de decisão judicial que defere medidas protetivas de urgência, com pena de detenção de três meses a dois anos.",
          "**Reserva de fiança judicial**: em caso de prisão em flagrante pelo delito do art. 24-A, apenas a autoridade judicial pode arbitrar fiança, sendo vedada ao delegado de polícia.",
          "**Indiferença da esfera do juízo**: o crime do art. 24-A consuma-se independentemente de a medida descumprida ter sido fixada por juízo cível, criminal ou de família.",
          "**Irrelevância do consentimento**: a tolerância tácita ou reconciliação informal posterior da ofendida não descaracteriza a tipicidade do crime do art. 24-A."
        ],
        "teoria": [
          {
            "statement": "O delegado de polícia que efetua a prisão em flagrante de indivíduo pelo crime de descumprimento de medida protetiva do art. 24-A pode arbitrar fiança na delegacia.",
            "isTrue": False,
            "explanation": "O art. 24-A, § 2º, estabelece expressamente que na custódia em flagrante delito a concessão de fiança é atribuição reservada privativamente ao magistrado condutor do feito."
          },
          {
            "statement": "O juiz tem o prazo de quarenta e oito horas após receber o expediente de medidas protetivas de urgência para apreciar e decidir os pedidos deduzidos.",
            "isTrue": True,
            "explanation": "Conforme o art. 18, I, o magistrado dispõe do prazo de 48 horas para analisar e fixar as medidas protetivas necessárias à salvaguarda da mulher."
          },
          {
            "statement": "O descumprimento de medidas protetivas deferidas por vara cível de família não caracteriza o crime do art. 24-A, exigindo-se ordem oriunda de vara criminal.",
            "isTrue": False,
            "explanation": "O art. 24-A, § 1º, prescreve que o crime independe da competência cível ou criminal do juiz que deferiu as medidas protetivas de urgência."
          },
          {
            "statement": "A aproximação física do agressor com o consentimento momentâneo da ofendida não afasta a configuração do delito de desobediência a medidas protetivas do art. 24-A.",
            "isTrue": True,
            "explanation": "O STJ consolidou que o bem jurídico primordial do art. 24-A é a administração da justiça, sendo irrelevante a aquiescência informal da vítima sem revogação judicial."
          }
        ],
        "revisao": [
          {
            "statement": "A decretação judicial de suspensão da posse de arma de fogo do agressor dispensa comunicação ao órgão institucional de registro ou chefia de polícia.",
            "isTrue": False,
            "explanation": "O art. 22, I, impõe ao juiz o dever de notificar de imediato o órgão competente ou corporação sobre a restrição de armamento funcional ou pessoal."
          },
          {
            "statement": "O comparecimento do agressor a programas de reeducação e acompanhamento psicossocial é modalidade de medida protetiva de urgência que obriga o autor.",
            "isTrue": True,
            "explanation": "Com as recentes alterações normativas no art. 22, VI e VII, instituiu-se a obrigatoriedade de comparecimento a centros de ressocialização e reeducação do agressor."
          },
          {
            "statement": "As medidas protetivas de urgência de natureza patrimonial limitam-se à fixação de alimentos provisórios, vedando-se bloqueio judicial de contas do casal.",
            "isTrue": False,
            "explanation": "O art. 24 autoriza medidas cautelares amplas, como bloqueio de contas bancárias, indisponibilidade temporária de bens e proibição de venda de patrimônio comum."
          },
          {
            "statement": "A pena privativa de liberdade cominada ao crime de descumprimento de medidas protetivas do art. 24-A é de detenção de três meses a dois anos.",
            "isTrue": True,
            "explanation": "O preceito secundário do art. 24-A da Lei 11.340/2006 estabelece textualmente a sanção de detenção de 3 meses a 2 anos."
          }
        ],
        "pointers": [
          {"topic": "Prazos de apreciação judicial das protetivas", "pageRef": 28},
          {"topic": "Medidas de afastamento, contato e armamento", "pageRef": 32},
          {"topic": "Proteção patrimonial e alimentos provisórios", "pageRef": 37},
          {"topic": "Crime do art. 24-A e vedação à fiança policial", "pageRef": 41}
        ]
      }
    }
  ]
}

# RESUMOS A17
summaries_a17 = {
  "aula": "legislacao-penal-especial/a17",
  "batch": "pcpe-summary-legislacao-penal-especial",
  "status": "DRAFT",
  "segments": [
    {
      "id": "legislacao-penal-especial/a17/s01",
      "fingerprint": {
        "startPage": 3,
        "endPage": 14,
        "startTopic": "Lei nº 11.340/2006 — Disposições Preliminares e Formas de Violência"
      },
      "analytic": """A Lei 11.340/2006 (Lei Maria da Penha) edificou um microssistema multidisciplinar de prevenção, proteção e repressão às agressões perpetradas contra a mulher no espaço privado, concretizando compromissos internacionais como a Convenção de Belém do Pará e sanções históricas da Comissão Interamericana de Direitos Humanos no caso emblemático envolvendo Maria da Penha Maia Fernandes e Marco Antônio Heredia Viveiros. A normatização visa a coibir a violência de gênero estrutural e criar mecanismos nas varas especializadas de violência doméstica e familiar.

### Sujeitos e Âmbitos de Incidência
A incidência do estatuto protetivo pressupõe critérios dogmáticos específicos:
- **Sujeito Passivo**: mulher, compreendida na perspectiva de gênero e vulnerabilidade presumida pelo ordenamento jurídico. O Superior Tribunal de Justiça consagrou em julgados paradigmáticos a subsunção da mulher transexual sob o manto protetivo da lei especial;
- **Sujeito Ativo**: qualquer pessoa, homem ou mulher (admitindo-se agressão entre cônjuges femininas em relacionamentos homoafetivos, ou de mãe contra filha, nora e sogra);
- **Três Ambientes de Incidência (art. 5º)**:
  1. *Espaço Doméstico*: ambiente de convívio físico e contínuo, independentemente de laços de sangue, alcançando pessoas agregadas e empregadas domésticas residentes;
  2. *Vínculo Familiar*: agrupamento de pessoas que se reconhecem aparentadas por consanguinidade, por laços de afinidade civil ou por ato de vontade e adoção;
  3. *Vínculo Íntimo Afetivo*: relação afetiva pretérita ou atual na qual o agressor tenha mantido intimidade com a mulher, sendo prescindível qualquer coabitação (Súmula 600 do STJ). Namorados ou ex-namorados atraem a incidência da norma.

### Classificação das Formas de Violência
O art. 7º positivou cinco formas autônomas de agressão:
- **Violência Física**: ofensa à integridade corporal ou saúde física da mulher;
- **Violência Psicológica**: dano emocional, rebaixamento da autoestima, manipulação, perseguição, vigilância constante ou humilhação que prejudique o pleno desenvolvimento pessoal;
- **Violência Sexual**: compelir a vítima a presenciar, manter ou participar de ato libidinoso não consentido mediante coerção, ameaça ou uso da força, bem como impedir o uso de métodos contraceptivos;
- **Violência Patrimonial**: retenção, extravio, destruição parcial ou integral de seus objetos de uso, instrumentos de trabalho, bens móveis, valores ou documentos pessoais;
- **Violência Moral**: qualquer conduta que configure calúnia, difamação ou injúria.

### Vedações Processuais e Súmulas dos Tribunais Superiores
A resposta punitiva do legislador afastou institutos de abrandamento penal:
- **Inaplicabilidade da Lei 9.099/1995 (art. 41 e Súmula 536/STJ)**: os delitos praticados com violência doméstica não tramitam nos Juizados Especiais, repelindo transação penal e suspensão condicional do processo;
- **Vedação de Penas Pecuniárias (art. 17)**: veda-se a fixação de cestas básicas ou prestações financeiras de feição meramente indenizatória;
- **Ação Pública Incondicionada (Súmula 542/STJ)**: a ação penal nas lesões corporais dolosas leves ou qualificadas é sempre incondicionada;
- **Inadmissibilidade da Insignificância (Súmula 589/STJ)**: não se acolhe o princípio da bagatela nas agressões domésticas;
- **Veto à Substituição por Penas Alternativas (Súmula 588/STJ)**: crimes cometidos com violência ou grave ameaça obstam a substituição da pena privativa de liberdade por restritivas de direitos.

### Para fixar
- A Lei Maria da Penha tutela a mulher, incluindo expressamente mulheres transexuais.
- A coabitação entre autor e vítima é desnecessária para a configuração da violência doméstica.
- O art. 7º define cinco modalidades de agressão: física, psicológica, sexual, patrimonial e moral.
- A Lei 9.099/1995 é integralmente inaplicável aos crimes da Lei Maria da Penha.
- A ação penal por lesão corporal doméstica é invariavelmente pública incondicionada.
- O princípio da insignificância não incide sobre infrações cometidas no âmbito doméstico.""",
      "synthetic": [
        "**Titularidade feminina**: a proteção especial volta-se à mulher em razão de gênero, abrangendo mulheres transexuais.",
        "**Dispensa de coabitação**: a Súmula 600 do STJ assegura a incidência da lei sem necessidade de moradia sob o mesmo teto.",
        "**Espécies de violência**: a norma consagra as violências física, psicológica, sexual, patrimonial e moral contra a mulher.",
        "**Juizados Especiais vedados**: o art. 41 afasta integralmente a disciplina despenalizadora da Lei 9.099/1995.",
        "**Ação incondicionada na lesão**: a persecução por lesão corporal dolosa doméstica prescinde de representação da vítima.",
        "**Veto à insignificância**: a Súmula 589 do STJ proíbe a incidência do princípio da bagatela na violência familiar.",
        "**Proibição de cesta básica**: é terminantemente vedada a imposição de penas restritivas de fornecimento de cestas básicas."
      ]
    },
    {
      "id": "legislacao-penal-especial/a17/s02",
      "fingerprint": {
        "startPage": 15,
        "endPage": 27,
        "startTopic": "Atendimento Policial e Assistência à Mulher"
      },
      "analytic": """O atendimento à mulher em situação de violência doméstica demanda respostas policiais estruturadas e especializadas para interromper o ciclo da agressão e salvaguardar a dignidade da vítima em delegacias especializadas (DEAMs) e varas de violência doméstica, afastando institutos despenalizadores da justiça comum estadual.

### Diretrizes de Acolhimento e Inquirição Humanizada
O art. 10-A da Lei 11.340/2006 estabelece diretrizes cogentes para o atendimento policial à vítima:
- **Atendimento Especializado nas DEAMs**: a mulher deve ser atendida em ambiente adequado e preferencialmente por servidoras policiais femininas capacitadas;
- **Não Revitimização**: veda-se expressamente o questionamento impertinente sobre a vida íntima pregressa da ofendida ou a repetição desnecessária de oitivas que a exponham a sofrimento psíquico ou vitimização secundária;
- **Apoio Psicológico e Social**: articulação com centros de referência, defensoria pública e redes socioassistenciais municipais para informar a depoente sobre seus direitos conferidos por lei;
- **Transferência Escolar de Dependentes**: a matrícula escolar dos filhos dependentes deve ser matriculado ou transferido com prioridade na instituição de ensino mais próxima do novo domicílio da ofendida.

### Medidas Policiais Protetivas Imediatas
Ao tomar conhecimento da ocorrência, o art. 11 impõe à autoridade policial a tomada de medidas urgentes:
- **Proteção Policial**: garantir custódia e escolta policial para a integridade da vítima e de seus filhos;
- **Transporte Seguro**: providenciar condução imediata da ofendida para entidade de acolhimento (casa-abrigo) ou residência de familiares;
- **Acompanhamento no Domicílio**: escoltar a mulher para resgate pacífico de seus bens de uso pessoal e instrumentos de labor;
- **Encaminhamento Médico-Hospitalar**: levar a ofendida ao hospital ou unidade de saúde e ao Instituto de Medicina Legal (IML) para perícias corporais, juntar aos autos investigativos os prontuários e assegurar prioridade na elaboração do laudo pericial;
- **Retratação da Representação (art. 16)**: nos delitos de ação penal pública condicionada (como a ameaça), a renúncia à representação só será admitida exclusivamente perante o magistrado condutor do feito em ato solene específico previamente designado antes de o juiz acolher a denúncia ministerial, com a presença do Ministério Público.

### Procedimento em Delegacia e Afastamento Cautelar do Lar
- **Remessa do Expediente Protetivo (art. 12)**: instaurado o inquérito policial ou termo circunstanciado, incumbe ao delegado remeter em **até 48 horas** o requerimento da ofendida contendo o pedido de medidas protetivas ao juiz de direito;
- **Afastamento Compulsório do Agressor do Domicílio (art. 12-C)**: verificada a iminência de risco à vida ou à higidez física da mulher, deflagra-se a sistemática de afastamento imediato do lar conjugal:
  1. *Pelo Juiz de Direito*: em qualquer circunstância e localidade;
  2. *Pelo Delegado de Polícia*: se o município não for sede de comarca;
  3. *Pelo Policial (qualquer agente estatal de segurança)*: quando a localidade municipal não possuir fórum judicial próprio e faltar autoridade de polícia judiciária no expediente plantonista.
- **Controle Judicial Posterior**: nas hipóteses executadas por delegado ou policial, o juiz competente deve ser comunicado no prazo peremptório de **24 horas**, cabendo-lhe igual prazo de **24 horas** para decidir fundamentadamente sobre a manutenção ou cancelamento da medida.

### Para fixar
- A inquirição policial deve priorizar servidoras mulheres e vedar questionamentos sobre vida pretérita.
- A polícia tem o dever de conduzir a mulher a local seguro e escoltá-la para retirar seus pertences.
- O pedido de medidas protetivas colhido na delegacia deve ser remetido ao juiz em até 48 horas.
- O afastamento do agressor cabe ao delegado quando a comarca não estiver sediada no município.
- O policial comum só afasta o agressor se o município não for comarca e faltar delegado no plantão.
- As decisões de afastamento tomadas por autoridades policiais devem ser comunicadas ao juiz em 24 horas.""",
      "synthetic": [
        "**Inquirição humanizada**: veda-se indagar a mulher sobre vida pregressa, devendo ser inquirida preferencialmente por policiais femininas.",
        "**Diligências protetivas urgentes**: a autoridade policial deve assegurar escolta, transporte para abrigo e assistência médica imediata.",
        "**Resgate de bens do lar**: garante-se à ofendida o acompanhamento policial para a retirada pacífica de documentos e pertences pessoais.",
        "**Remessa do pleito em 48h**: a autoridade policial tem o prazo improrrogável de quarenta e oito horas para enviar os pedidos ao juiz.",
        "**Afastamento escalonado do lar**: a ordem de saída do agressor pode emanar do juiz, do delegado ou, excepcionalmente, do policial.",
        "**Subsidiaridade no afastamento**: o agente policial comum somente atua quando o município não for comarca e faltar delegado presente.",
        "**Comunicação judicial em 24h**: deferido o afastamento por delegado ou policial, o magistrado deve ser cientificado em vinte e quatro horas."
      ]
    },
    {
      "id": "legislacao-penal-especial/a17/s03",
      "fingerprint": {
        "startPage": 28,
        "endPage": 43,
        "startTopic": "Medidas Protetivas de Urgência, Descumprimento e Procedimentos"
      },
      "analytic": """As medidas protetivas de urgência consubstanciam provimentos jurisdicionais cautelares destinados a debelar o perigo imediato de dano à mulher em situação de violência, dividindo-se entre ordens que impõem restrições ao agressor e providências de salvaguarda à ofendida, com apoio de monitoração eletrônica e medidas patrimoniais estabelecidas nas disposições finais da lei para evitar conflito de normas e que a agressão cause morte.

### Prazos e Medidas que Obrigam o Agressor
Recebido o expediente encaminhado pela autoridade policial, o juiz deve deliberar no prazo improrrogável de **48 horas** (art. 18):
- **Rol do Art. 22 (Obrigações do Agressor)**:
  - Suspensão da posse ou restrição do porte de armas, notificando-se o comando da respectiva instituição armada ou órgão de controle funcional;
  - Desocupação compulsória e afastamento do teto conjugal ou local em que a mulher resida;
  - Proibição de aproximação da vítima, seus familiares e testemunhas, fixando limite mínimo de distância métrica;
  - Proibição de contato com a vítima por qualquer meio de comunicação (telefônico, mensagem, correio eletrônico ou redes sociais);
  - Proibição de frequência a determinados lugares (academia, trabalho ou domicílio de parentes);
  - Restrição ou suspensão temporária de visitas aos dependentes menores;
  - Prestação de alimentos provisionais ou provisórios;
  - Comparecimento cogente a programas de recuperação, reeducação e acompanhamento psicossocial;
  - Monitoração eletrônica do agressor por tornozeleira eletrônica como providência assecuratória da distância fixada judicialmente.

### Medidas de Tutela e Proteção da Ofendida
Os arts. 23 e 24 outorgam ampla proteção pessoal e econômica à mulher:
- **Proteção Pessoal**: encaminhamento a programa de proteção ou casa-abrigo, recondução segura ao domicílio familiar após a remoção do agressor e separação de corpos;
- **Proteção Patrimonial**: restituição de bens indevidamente retidos ou subtraídos pelo agressor, proibição temporária de celebração de atos de alienação patrimonial e bloqueio liminar de contas correntes bancárias do casal.

### O Crime de Descumprimento de Medidas Protetivas (Art. 24-A)
A Lei 13.641/2018 introduziu o tipo penal do art. 24-A para coibir a desobediência a ordens protetivas de urgência:
- **Tipo Penal e Sanção**: transgredir ou desobedecer ordem jurisdicional cautelar que deferiu providências de tutela na Lei Maria da Penha. A sanção corporal privativa de liberdade é de detenção de 3 meses a 2 anos, sem prejuízo da imposição cumulativa de prisão preventiva para salvaguarda da ordem pública;
- **Competência do Juízo Prolator (§ 1º)**: a configuração do delito independe de a medida ter emanado de vara de família, cível ou juízo criminal especializado da comarca;
- **Reserva de Fiança Judicial (§ 2º)**: havendo prisão em flagrante pelo art. 24-A, **apenas a autoridade judicial pode conceder fiança**. O delegado de polícia está categoricamente proibido de arbitrar fiança em sede policial, devendo lavrar o auto e apresentar o preso à audiência de custódia;
- **Irrelevância do Consentimento da Vítima**: a jurisprudência pacífica consolidada em Súmula do STJ e tribunais pátrios estabelece que o consentimento, a reaproximação temporária da namorada com quem mantinha afeto ou a conciliação informal com a vítima não afasta a tipicidade do crime, pois a ordem judicial tutela primordialmente a administração da justiça e a eficácia das decisões estatais contra conflitos e reiterações criminosas;
- **Proteção Integral e Não Ingerência**: as medidas protetivas que protegem a ofendida e sua integridade possuem vigência enquanto subsistir a situação de risco concreto, devendo o juízo reavaliá-las fundamentadamente quando provocado pelas partes.

### Para fixar
- O juiz tem o prazo improrrogável de 48 horas para deliberar sobre medidas protetivas requeridas.
- O comparecimento a programas de reeducação é medida protetiva obrigatória cabível contra o agressor.
- A decisão que suspende o porte de arma do agressor deve ser comunicada de imediato à sua corporação.
- O descumprimento de medidas protetivas (art. 24-A) pune o autor com detenção de três meses a dois anos.
- A concessão de fiança na prisão em flagrante do art. 24-A é prerrogativa privativa do juiz.
- A reconciliação informal com a vítima não elide o crime de desobediência a medidas protetivas.""",
      "synthetic": [
        "**Deliberação judicial célere**: o magistrado tem o dever de decidir sobre o pleito de medidas protetivas em quarenta e oito horas.",
        "**Afastamento e proibição de contato**: impõem-se o banimento do domicílio e veto absoluto à aproximação física ou telemática.",
        "**Restrição de armamento bélico**: a suspensão do porte funcional ou particular do agressor é comunicada prontamente à corporação.",
        "**Inclusão em reeducação**: o agressor pode ser compelido a frequentar programas psicossociais de reabilitação e reeducação.",
        "**Delito do art. 24-A**: descumprir ordem protetiva configura crime autônomo com pena de detenção de três meses a dois anos.",
        "**Vedação à fiança policial**: a autoridade policial não pode arbitrar fiança no flagrante do art. 24-A, competindo exclusivamente ao juiz.",
        "**Consentimento irrelevante**: a tolerância amigável da mulher não revoga a ordem judicial nem elide o crime do art. 24-A."
      ]
    }
  ]
}

Path("content/items/legislacao-penal-especial/a17.json").write_text(json.dumps(items_a17, ensure_ascii=False, indent=2), encoding="utf-8")
Path("content/summaries/legislacao-penal-especial/a17.json").write_text(json.dumps(summaries_a17, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved a17 files successfully.")
