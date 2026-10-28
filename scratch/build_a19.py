import json
from pathlib import Path

# AULA 19: Lei 14.344/2022 (Lei Henry Borel)

items_a19 = {
  "aula": "legislacao-penal-especial/a19",
  "batch": "pcpe-bizu-legislacao-penal-especial",
  "status": "DRAFT",
  "stage": "bizu",
  "segments": [
    {
      "id": "legislacao-penal-especial/a19/s01",
      "bizu": {
        "summary": [
          "**Marco protetivo infantojuvenil**: a Lei 14.344/2022 institui mecanismos de prevenção e enfrentamento da violência doméstica e familiar contra crianças e adolescentes.",
          "**Configuração dos âmbitos**: a violência caracteriza-se na unidade doméstica, no ambiente familiar ampliado ou em qualquer vínculo interpessoal de afeto e convivência.",
          "**Modalidades de agressão**: compreende violência física, abuso psicológico, violência sexual, agressão patrimonial e a violência institucional praticada por órgãos públicos.",
          "**Medidas protetivas urgentes**: podem ser determinadas de ofício pelo magistrado ou postuladas pelo Ministério Público, polícia judiciária, Defensoria ou Conselho Tutelar.",
          "**Afastamento cautelar do lar**: constatado risco iminente à integridade física do jovem, impõe-se a desocupação imediata do domicílio comum pelo suposto agressor.",
          "**Crime de descumprimento**: descumprir decisão judicial concessiva de medida protetiva sujeita o agente a detenção de três meses a dois anos (fiança privativa do juiz).",
          "**Dever legal de comunicação**: profissionais de saúde, educação ou assistência que presenciarem ou suspeitarem de violência devem comunicar o fato imediatamente.",
          "**Qualificadora de homicídio**: a legislação inseriu no Código Penal qualificadora autônoma para o assassinato perpetrado contra menor de quatorze anos de idade."
        ],
        "teoria": [
          {
            "statement": "As medidas protetivas de urgência previstas na Lei Henry Borel restringem-se à manifestação privativa de vontade dos genitores da criança vitimada.",
            "isTrue": False,
            "explanation": "Podem ser requeridas pelo Ministério Público, autoridade policial, Conselho Tutelar, pela própria vítima acompanhada de representante, ou concedidas de ofício."
          },
          {
            "statement": "A prática de violência doméstica contra menor independe da coabitação habitual sob o mesmo teto entre a vítima e o autor da agressão.",
            "isTrue": True,
            "explanation": "A lei expressamente estipula que a violência familiar se perfaz independentemente de coabitação física contínua sob o mesmo teto."
          },
          {
            "statement": "A autoridade policial possui competência legal plena para arbitrar fiança ao agente flagrado descumprindo medida protetiva de urgência da Lei 14.344/2022.",
            "isTrue": False,
            "explanation": "No crime de descumprimento de medida protetiva (art. 25), a concessão de fiança é competência privativa e indelegável da autoridade judicial."
          },
          {
            "statement": "A Lei Henry Borel estabeleceu causa específica de aumento de pena quando o crime for praticado por pessoa que detém autoridade sobre a criança.",
            "isTrue": True,
            "explanation": "O art. 121, § 2º-B, do CP e os preceitos especiais majoram a punição caso a conduta seja cometida por ascendente, padrasto, tutor ou responsável legal."
          }
        ],
        "revisao": [
          {
            "statement": "A violência institucional contra a criança ou adolescente prescinde de vínculo estatal, consumando-se exclusivamente na esfera privada doméstica.",
            "isTrue": False,
            "explanation": "A violência institucional é praticada por agente público no âmbito de instituições estatais prestadoras de serviços de proteção, segurança ou custódia."
          },
          {
            "statement": "O Conselho Tutelar possui legitimidade jurídica para representar perante o Poder Judiciário pela concessão de medidas cautelares protetivas urgentes.",
            "isTrue": True,
            "explanation": "A Lei 14.344/2022 outorgou expressa legitimidade postulacional ao Conselho Tutelar para pleitear a fixação de providências protetivas cautelares."
          },
          {
            "statement": "A retratação da denúncia ou representação na esfera da violência contra a criança é livremente homologada sem a intervenção ministerial em audiência.",
            "isTrue": False,
            "explanation": "A ação penal por lesão corporal ou vias de fato na violência doméstica é pública incondicionada, inviabilizando qualquer desistência ou retratação."
          },
          {
            "statement": "O descumprimento injustificado de medida protetiva deferida em favor de jovem autoriza a imediata decretação da prisão preventiva do autor da ameaça.",
            "isTrue": True,
            "explanation": "Nos termos do art. 313, III, do CPP e da legislação especial, a desobediência a provimento cautelar protetivo embasa a custódia preventiva processual."
          }
        ],
        "pointers": [
          {"topic": "Diretrizes e âmbitos de aplicação da Lei Henry Borel", "pageRef": 3},
          {"topic": "Formas de violência e violência institucional", "pageRef": 6},
          {"topic": "Competência e rol das medidas protetivas de urgência", "pageRef": 9},
          {"topic": "Descumprimento de medidas e qualificadora no Código Penal", "pageRef": 13}
        ]
      }
    }
  ]
}

# RESUMOS A19
summaries_a19 = {
  "aula": "legislacao-penal-especial/a19",
  "batch": "pcpe-summary-legislacao-penal-especial",
  "status": "DRAFT",
  "segments": [
    {
      "id": "legislacao-penal-especial/a19/s01",
      "fingerprint": {
        "startPage": 3,
        "endPage": 15,
        "startTopic": "Lei nº 14.344/2022 — Violência Doméstica e Familiar contra Criança e Adolescente"
      },
      "analytic": """A Lei 14.344/2022, amplamente denominada Lei Henry Borel, inaugurou no ordenamento jurídico brasileiro um microssistema protetivo integral voltado a coibir a violência doméstica e familiar cometida contra crianças e adolescentes. Inspirada na sistemática consagrada pela Lei Maria da Penha, a nova legislação articulou providências criminais severas, instrumentos processuais cautelares rápidos e uma rede multidisciplinar de assistência pública.

### Conceituação e Âmbitos de Ocorrência da Violência
A incidência do estatuto protetivo demanda a conjugação do sujeito passivo qualificado pela faixa etária (criança de até 12 anos incompletos ou adolescente entre 12 e 18 anos) com cenários relacionais específicos:
- **Espaço da Unidade Doméstica**: compreendido como o ambiente permanente de convivência coletiva sob o mesmo teto, independentemente de existir laço de parentesco consanguíneo, abrangendo pessoas agregadas ou prestadores de serviços;
- **Âmbito da Comunidade Familiar**: comunidade formada por indivíduos que se reconhecem aparentados por vínculos naturais, civis ou por afinidade jurídica (como padrastos, madrastas e tios);
- **Relação Íntima de Convivência ou Afeto**: qualquer laço afetivo no qual o agressor conviva ou tenha convivido com a jovem vítima, sendo irrelevante a coabitação física continuada sob o mesmo teto;
- **Modalidades de Agressão Reprimidas**: o diploma tutela os jovens contra agressões físicas, violações psicológicas (humilhação, alienação parental e ameaças), violências sexuais em quaisquer modalidades, esbulhos ou prejuízos patrimoniais e a denominada violência institucional, que ocorre quando órgãos ou servidores estatais revitimizam a criança em depoimentos desnecessários ou atendimentos hostis.

### Medidas Protetivas de Urgência e Competência Cautelar
As medidas protetivas traduzem tutelas inibitórias de urgência desenhadas para estancar agressões iminentes ou reiteradas:
- **Legitimação Postulacional Ampla**: as cautelares podem ser decretadas pelo juiz criminal ou da infância, a requerimento formal do Ministério Público, por representação fundamentada da autoridade policial, a pedido formulado pelo Conselho Tutelar, ou por petição da própria vítima assistida;
- **Providências Constritivas contra o Agressor**: determinação de desocupação e afastamento imediato da residência ou domicílio comum com o menor; fixação de distância mínima com vedação de qualquer aproximação física, virtual ou telefônica com a vítima, parentes e testemunhas; suspensão cautelar da posse ou restrição ao porte funcional de armas de fogo; e fixação liminar de pensão alimentícia provisória;
- **Tutelas Assistenciais voltadas ao Menor**: inclusão prioritária da criança e de seus familiares responsáveis em programas governamentais de proteção a testemunhas e vítimas ameaçadas; determinação de matrícula em educandário escolar próximo do novo endereço; e encaminhamento a acolhimento institucional assistido em casos extremos de risco concreto.

### Tipos Penais Próprios, Descumprimento e Inovações no Código Penal
A Lei 14.344/2022 agregou respostas punitivas contundentes para coibir a impunidade:
- **Crime de Desobediência à Medida Protetiva (art. 25)**: punição autônoma com pena de detenção de três meses a dois anos para quem descumpre ordem judicial concessiva de providência cautelar protetiva. A legislação fixou reserva judicial indelegável para o arbitramento de fiança em caso de flagrante delito, competindo exclusivamente ao magistrado analisar a concessão de liberdade provisória;
- **Omissão Relevante de Notificação**: criminaliza-se a postura inerte de profissionais de saúde, assistentes sociais ou professores que deixam de comunicar às autoridades competentes a prática de maus-tratos ou violências sofridas por menores de que tenham ciência formal no exercício da função;
- **Qualificadora Específica do Homicídio (art. 121, § 2º, IX, do CP)**: tipificou-se o homicídio contra menor de 14 anos como qualificadora autônoma hedionda, majorada expressamente se o crime for executado por genitor, padrasto, tutor ou curador que exercia autoridade direta sobre a criança indefesa.

### Para fixar
- A Lei Henry Borel tutela integralmente crianças e adolescentes contra agressões domésticas e familiares.
- A configuração da violência independe de coabitação sob o mesmo teto entre agressor e ofendido.
- A violência institucional decorre de condutas abusivas ou revitimizadoras praticadas pelo próprio Estado.
- As medidas cautelares protetivas podem ser provocadas pelo Conselho Tutelar ou pelo Ministério Público.
- O afastamento obrigatório do agressor do lar comum constitui medida assecuratória da incolumidade do jovem.
- A concessão de fiança no crime de descumprimento de protetiva é privativa da autoridade judiciária.
- O homicídio contra criança menor de 14 anos é crime hediondo qualificado no Código Penal.""",
      "synthetic": [
        "**Microssistema protetivo da infância**: a Lei 14.344/2022 estabelece mecanismos de proteção integral contra violências domésticas voltadas a menores.",
        "**Independência de coabitação residencial**: a violência familiar contra menor consuma-se mesmo sem moradia contínua sob o mesmo teto comum.",
        "**Modalidades amplas de violação**: abrange violências física, psicológica, sexual, patrimonial e a violência institucional praticada por agentes estatais.",
        "**Legitimidade do Conselho Tutelar**: o colegiado tutelar possui legitimidade formal para requerer medidas protetivas urgentes ao Poder Judiciário.",
        "**Afastamento cautelar compulsório**: o juiz determina a imediata saída do agressor da residência familiar para salvaguardar a integridade do menor.",
        "**Descumprimento e fiança judicial**: o crime do art. 25 sujeita-se a detenção de três meses a dois anos com fiança restrita ao magistrado.",
        "**Dever comunicatório profissional**: servidores da educação, saúde e assistência social respondem criminalmente pela omissão de relato de agressões.",
        "**Qualificadora hedionda de homicídio**: assassinar criança menor de catorze anos tipifica homicídio qualificado gravoso no Código Penal."
      ]
    }
  ]
}

Path("content/items/legislacao-penal-especial/a19.json").write_text(json.dumps(items_a19, ensure_ascii=False, indent=2), encoding="utf-8")
Path("content/summaries/legislacao-penal-especial/a19.json").write_text(json.dumps(summaries_a19, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved a19 files successfully.")
