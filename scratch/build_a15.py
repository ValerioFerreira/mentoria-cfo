import json
import subprocess
from pathlib import Path

# AULA 15: Lei 12.850/2013 (Organizações Criminosas)

items_a15 = {
  "aula": "legislacao-penal-especial/a15",
  "batch": "pcpe-bizu-legislacao-penal-especial",
  "status": "DRAFT",
  "stage": "bizu",
  "segments": [
    {
      "id": "legislacao-penal-especial/a15/s01",
      "bizu": {
        "summary": [
          "**Elemento numérico e estrutura**: a organização criminosa demanda a conjugação de quatro ou mais indivíduos, ordenada estruturalmente e caracterizada por divisão de tarefas.",
          "**Gravidade das infrações-alvo**: o desígnio do grupo deve visar à prática de infrações com pena máxima superior a quatro anos ou que ostentem natureza transnacional.",
          "**Diferenciação dogmática**: distingue-se da associação criminosa comum (três pessoas e crimes indeterminados) e da associação para o narcotráfico (duas pessoas).",
          "**Tipo penal e condutas**: o art. 2º sanciona criminalmente a ação de fundar, prover recursos econômicos, encabeçar ou fazer parte da associação delituosa estruturada.",
          "**Embaraço à persecução**: comete infração penal equiparada aquele que impede ou embaraça investigação penal voltada a apurar atividades de organização criminosa.",
          "**Majorante por arma de fogo**: a sanção carcerária sofre aumento de até a metade se houver emprego de armamento bélico nas atividades societárias ilícitas.",
          "**Efeitos ao servidor condenado**: acarreta a perda automática do cargo e a interdição para novas funções públicas pelo prazo de oito anos após a extinção da pena.",
          "**Afastamento cautelar**: o juiz pode decretar o afastamento do funcionário público investigado havendo fortes indícios, preservada a sua remuneração funcional."
        ],
        "teoria": [
          {
            "statement": "Para a configuração de organização criminosa nos moldes da Lei 12.850/2013, exige-se a reunião estável de pelo menos três pessoas para a prática de crimes.",
            "isTrue": False,
            "explanation": "A Lei 12.850/2013 exige expressamente a conjugação de quatro ou mais pessoas; a reunião de três pessoas caracteriza a associação criminosa do art. 288 do Código Penal."
          },
          {
            "statement": "A prática de infrações penais com pena privativa de liberdade máxima superior a quatro anos é um dos requisitos objetivos alternativos do conceito de organização criminosa.",
            "isTrue": True,
            "explanation": "Conforme o art. 1º, § 1º, os delitos visados devem possuir penas máximas superiores a quatro anos ou ostentar caráter transnacional."
          },
          {
            "statement": "O servidor público afastado cautelarmente de suas funções por suspeita fundada de integrar organização criminosa perde de imediato os vencimentos de seu cargo.",
            "isTrue": False,
            "explanation": "O art. 2º, § 5º, prevê o afastamento cautelar do funcionário público sem prejuízo de sua remuneração até a superveniência do trânsito em julgado."
          },
          {
            "statement": "A condenação definitiva de servidor público por integrar organização criminosa gera a perda do cargo e a interdição para a função pública pelo prazo de oito anos.",
            "isTrue": True,
            "explanation": "O art. 2º, § 6º, estabelece a perda do cargo e a interdição pelo período de oito anos subsequentes ao integral cumprimento da pena carcerária."
          }
        ],
        "revisao": [
          {
            "statement": "A divisão de tarefas entre os partícipes da organização criminosa exige obrigatoriamente formalização documental e hierarquia rígida estatutária.",
            "isTrue": False,
            "explanation": "O art. 1º, § 1º, prevê que a ordenação estrutural e a repartição funcional de tarefas operam ainda que de maneira meramente informal."
          },
          {
            "statement": "A conduta de embaraçar ou criar obstáculos a investigações que apurem crimes perpetrados por organização criminosa configura delito punido com as mesmas penas do art. 2º.",
            "isTrue": True,
            "explanation": "O art. 2º, § 1º, equipara a conduta de impedir ou embaraçar investigação penal de organização criminosa, cominando as mesmas penas de 3 a 8 anos de reclusão."
          },
          {
            "statement": "A majorante pelo emprego de arma de fogo na organização criminosa impõe exasperação obrigatória da reprimenda privativa de liberdade no patamar fixo de dois terços.",
            "isTrue": False,
            "explanation": "Conforme o art. 2º, § 2º, a presença de arma de fogo acarreta causa de aumento de pena variável de até a metade (e não patamar fixo de 2/3)."
          },
          {
            "statement": "O particular que atua como mentor financeiro aportando recursos materiais para estruturar a organização criminosa incorre nas penas do crime autônomo do art. 2º.",
            "isTrue": True,
            "explanation": "O verbo 'financiar' consta expressamente do núcleo típico do art. 2º da Lei 12.850/2013 ao lado de promover, constituir e integrar."
          }
        ],
        "pointers": [
          {"topic": "Conceito legal e requisitos da organização criminosa", "pageRef": 3},
          {"topic": "Diferença entre associação e organização criminosa", "pageRef": 4},
          {"topic": "Afastamento cautelar do agente estatal investigado", "pageRef": 5},
          {"topic": "Perda do cargo público e interdição de oito anos", "pageRef": 6}
        ]
      }
    },
    {
      "id": "legislacao-penal-especial/a15/s02",
      "bizu": {
        "summary": [
          "**Natureza da delação**: a colaboração premiada é negócio jurídico processual de caráter personalíssimo, constituindo meio de obtenção de prova.",
          "**Vedação à atuação do magistrado**: é vedado ao juiz participar das tratativas e negociações da delação, limitando-se a sua competência a homologar o acordo.",
          "**Insuficiência das declarações**: nenhuma sentença penal condenatória ou medida cautelar pode ser decretada unicamente com base na palavra do colaborador.",
          "**Resultados legais da delação**: exige-se a produção de resultados úteis, como a identificação de comparsas, recuperação de bens ou localização de vítimas.",
          "**Benefícios premiais**: o acordo validado autoriza a concessão de perdão judicial, diminuição da reprimenda privativa de liberdade em até dois terços ou substituição restritiva.",
          "**Ação controlada interna**: consiste no retardamento discricionário da intervenção policial, dependendo de prévia comunicação circunstanciada ao juiz competente.",
          "**Infiltração de agentes**: exige autorização judicial prévia motivada e manifestação do MP, com prazo inicial de até seis meses prorrogável se necessário.",
          "**Infiltração telemática virtual**: autoriza a inserção de policiais disfarçados na internet por até seis meses, respeitado o teto total de setecentos e vinte dias."
        ],
        "teoria": [
          {
            "statement": "O magistrado responsável pelo processo pode participar ativamente das rodadas de negociação do acordo de colaboração premiada entre as partes.",
            "isTrue": False,
            "explanation": "O art. 4º, § 6º, veda terminantemente ao juiz intervir nas negociações, competindo-lhe exercer controle de legalidade e voluntariedade na homologação."
          },
          {
            "statement": "A palavra isolada do colaborador premiado não autoriza, por si só, a prolação de sentença condenatória ou a decretação de prisões cautelares.",
            "isTrue": True,
            "explanation": "O art. 4º, § 16, veda condenação ou medidas cautelares lastreadas unicamente nas declarações do agente colaborador sem elementos externos de corroboração."
          },
          {
            "statement": "A deflagração de ação controlada no território nacional reclama indispensável e prévia autorização judicial para que os policiais possam postergar a abordagem.",
            "isTrue": False,
            "explanation": "Na ação controlada interna (art. 8º), exige-se apenas a prévia comunicação ao juiz competente (com ciência ao MP), dispensando-se autorização judicial prévia."
          },
          {
            "statement": "A infiltração policial de agentes disfarçados depende de prévia e motivada autorização judicial, fixando-se o prazo ordinário inicial de até seis meses.",
            "isTrue": True,
            "explanation": "Conforme o art. 10 da Lei 12.850/2013, a infiltração é medida excepcional condicionada à autorização do juiz pelo prazo de até seis meses, renovável se motivada."
          }
        ],
        "revisao": [
          {
            "statement": "O acordo de colaboração premiada pode ser celebrado diretamente entre a autoridade policial e o investigado sem a presença de advogado ou defensor.",
            "isTrue": False,
            "explanation": "A assistência jurídica técnica por advogado constituído ou defensor público é condição obrigatória de validade em todas as fases do acordo de delação."
          },
          {
            "statement": "O agente policial infiltrado não responde pelos atos ilícitos proporcionais praticados no curso da missão quando inexigível conduta diversa.",
            "isTrue": True,
            "explanation": "O art. 13 da Lei 12.850/2013 estabelece excludente de ilicitude e culpabilidade especial para a conduta estritamente necessária ao êxito da infiltração."
          },
          {
            "statement": "O perdão judicial concedido em decorrência de colaboração premiada eficaz pode ser revogado unilateralmente pela autoridade policial a qualquer tempo.",
            "isTrue": False,
            "explanation": "O perdão judicial é causa extintiva de punibilidade de competência privativa do Poder Judiciário prolator da sentença, sendo irrevogável após o trânsito em julgado."
          },
          {
            "statement": "A infiltração virtual de policiais em ambientes cibernéticos e redes sociais é disciplinada pela lei com limite máximo improrrogável de setecentos e vinte dias.",
            "isTrue": True,
            "explanation": "O art. 10-A, § 2º, autoriza a infiltração virtual por até seis meses, prorrogável sucessivamente desde que não exceda o limite global de 720 dias."
          }
        ],
        "pointers": [
          {"topic": "Meios especiais de prova e colaboração premiada", "pageRef": 7},
          {"topic": "Papel do juiz e vedação a condenações isoladas", "pageRef": 9},
          {"topic": "Ação controlada interna e comunicação prévia", "pageRef": 14},
          {"topic": "Infiltração presencial e cibernética de policiais", "pageRef": 17}
        ]
      }
    }
  ]
}

# RESUMOS A15
summaries_a15 = {
  "aula": "legislacao-penal-especial/a15",
  "batch": "pcpe-summary-legislacao-penal-especial",
  "status": "DRAFT",
  "segments": [
    {
      "id": "legislacao-penal-especial/a15/s01",
      "fingerprint": {
        "startPage": 3,
        "endPage": 6,
        "startTopic": "Lei nº 12.850/2013 — Conceito de Organização Criminosa e Tipos Penais"
      },
      "analytic": """A Lei 12.850/2013 supriu histórica lacuna normativa ao estipular o conceito dogmático de organização criminosa e instituir mecanismos modernos de combate à criminalidade corporativa e estruturada.

### Elementos Constitutivos da Organização Criminosa
O art. 1º, § 1º, define que se considera organização criminosa a associação de:
- **Quatro ou mais pessoas**: requisito numérico cogente. Difere do concurso eventual de pessoas, da associação para o tráfico (art. 35 da Lei 11.343/2006, que exige duas ou mais pessoas) e da associação criminosa comum (art. 288 do CP, que reclama três indivíduos);
- **Ordenação Estrutural e Divisão de Tarefas**: demanda articulação hierárquica e repartição funcional de atribuições, ainda que exercidas de modo informal;
- **Finalidade Econômica ou Moral**: obtenção, direta ou indireta, de vantagem de qualquer natureza;
- **Gravidade Delitiva**: direcionamento à prática de infrações penais cujas penas privativas de liberdade máximas sejam **superiores a 4 anos**, ou que possuam caráter transnacional.

### O Delito Autônomo e Sanções Funcionais
O art. 2º da norma pune quem promove, constitui, financia ou integra, pessoalmente ou por interposta pessoa, organização criminosa, cominada pena de reclusão de 3 a 8 anos e multa:
- **Obstrução de Justiça (§ 1º)**: incorre nas mesmas penas quem embaraça ou impede investigação de infração penal que envolva organização criminosa;
- **Majorantes Gerais (§§ 2º e 4º)**: a reprimenda é majorada em até a metade se houver uso de arma de fogo, e aumentada de 1/6 a 2/3 se houver concurso de criança ou adolescente, conexão internacional ou envolvimento de funcionário público;
- **Sanções ao Servidor Público (§§ 5º e 6º)**: constatados indícios suficientes, o juiz poderá determinar o afastamento cautelar do servidor investigado de suas funções, sem prejuízo da remuneração salarial. Sobrevindo condenação irrecorrível, operam-se a perda automática do cargo e a inabilitação para funções públicas pelo lapso de **oito anos** após o cumprimento da pena carcerária.

### Para fixar
- A configuração da organização criminosa exige quatro ou mais pessoas articuladas com divisão de tarefas.
- As infrações visadas pelo grupo devem ostentar pena máxima superior a quatro anos ou transnacionalidade.
- O crime autônomo pune promover, constituir, financiar ou integrar o grupo delitivo.
- A obstrução a investigações sobre organização criminosa atrai as mesmas sanções do crime principal.
- O afastamento cautelar do funcionário público investigado não suspende sua remuneração.
- A condenação transitada em julgado acarreta perda do cargo e interdição pública pelo prazo de oito anos.""",
      "synthetic": [
        "**Pluralidade qualificada de agentes**: exige-se a reunião formal ou informal de quatro ou mais indivíduos plenamente organizados.",
        "**Gravidade objetiva das infrações**: as condutas ilícitas visadas pela sociedade criminosa devem ter penas máximas superiores a quatro anos.",
        "**Núcleo abrangente da incriminação**: tipificam-se as condutas de promover, constituir, financiar materialmente ou integrar a organização.",
        "**Obstrução e embaraço processual**: embaraçar ou criar obstáculos a inquéritos sobre organizações atrai a mesma pena do delito principal.",
        "**Preservação remuneratória no afastamento**: o afastamento cautelar provisório do agente estatal dá-se sem qualquer prejuízo dos vencimentos.",
        "**Inabilitação funcional prolongada**: a condenação irrecorrível impõe a destituição do cargo público e interdição para novas funções por oito anos."
      ]
    },
    {
      "id": "legislacao-penal-especial/a15/s02",
      "fingerprint": {
        "startPage": 7,
        "endPage": 19,
        "startTopic": "Meios de Obtenção de Prova: Colaboração Premiada e Ação Controlada"
      },
      "analytic": """A Lei 12.850/2013 dedicou disciplina minuciosa aos meios extraordinários de obtenção de prova no enfrentamento ao crime organizado, positivando procedimentos para a colaboração premiada, a ação controlada e as infiltrações policiais.

### Regime Jurídico da Colaboração Premiada
A colaboração premiada qualifica-se como meio de obtenção de prova e negócio jurídico processual personalíssimo:
- **Partes e Intervenientes**: o acordo é pactuado entre o delegado de polícia (com parecer do órgão ministerial) ou o Ministério Público e o investigado ou acusado, acompanhado obrigatoriamente de seu patrono constituído ou defensor público;
- **Proibição da Intervenção Judicial**: o magistrado não pode participar das negociações do acordo. Sua função circunscreve-se à análise da legalidade, regularidade e voluntariedade do pacto em sede de homologação;
- **Resultados Legais Exigidos**: para fruição dos prêmios, a delação deve proporcionar ao menos um resultado eficaz do art. 4º (identificação de comparsas, revelação da teia hierárquica, prevenção de crimes, resgate do proveito do delito ou resguardo da integridade de vítimas);
- **Benefícios Concedidos**: verificado o sucesso, o magistrado prolator da sentença pode aplicar o perdão judicial, minorar a pena privativa de liberdade em até 2/3 ou substituí-la por sanções restritivas de direitos;
- **Inadmissibilidade de Condenação Isolada**: a declaração do colaborador jamais autoriza, isoladamente, a decretação de medidas cautelares patrimoniais ou pessoais, o recebimento de petição inicial acusatória ou a prolação de decreto condenatório (§ 16 do art. 4º);
- **Garantia de Confidencialidade**: as tratativas preliminares submetem-se a rigoroso sigilo funcional, respondendo administrativamente e penalmente o celebrante ou autoridade que violar a reserva dos autos.

### Ação Controlada Interna e Transnacional
A técnica da ação controlada autoriza postergar a intervenção policial para momento de maior eficiência probatória:
- **Ação Controlada Nacional (art. 8º)**: não depende de prévia autorização judicial. O delegado ou autoridade competente deve realizar **prévia comunicação formal circunstanciada** ao juízo competente, com ciência imediata ao Ministério Público, estabelecendo limites ao monitoramento;
- **Ação Controlada Transnacional (art. 9º)**: quando a rota do delito transpassar fronteiras internacionais, a execução reclama prévia autorização do juiz nacional e cooperação jurídica internacional;
- **Controle de Legalidade**: caso o juiz verifique desvio de finalidade ou perigo iminente desmedido à coletividade, poderá determinar a imediata cessação do retardamento e a abordagem dos agentes monitorados.

### Infiltração de Agentes Policiais Presencial e Virtual
A infiltração policial constitui medida subsidiária extrema de inteligência criminal:
- **Infiltração Presencial (art. 10)**: autorizada pelo juiz em decisão sigilosa fundamentada, perante requerimento policial ou ministerial, quando a prova não puder ser obtida por outros meios corriqueiros. O prazo ordinário é de até seis meses, prorrogável mediante demonstração motivada da subsistência da necessidade operacional;
- **Infiltração Virtual (art. 10-A)**: inserida pelo Pacote Anticrime para apuração em ambientes digitais e telemáticos. Submete-se à autorização judicial prévia, vigorando por até seis meses, com renovações sucessivas até o teto temporal de **720 dias**;
- **Excludente Especial de Responsabilidade (art. 13)**: o policial infiltrado não responde penalmente pelas infrações perpetradas no cumprimento da ordem estrita da missão quando inexigível conduta diversa, guardada a proporcionalidade em relação à salvaguarda dos objetivos da operação.

| Mecanismo de Prova | Requisito de Deflagração | Prazo Legal |
|---|---|---|
| Colaboração Premiada | Negócio jurídico e homologação judicial | Rescisão se descumprido |
| Ação Controlada Interna | Prévia comunicação ao juiz (sem autorização prévia) | Enquanto perdurar o flagrante retardado |
| Infiltração Policial Física | Prévia autorização judicial motivada | Até 6 meses (prorrogável) |
| Infiltração Policial Virtual | Prévia autorização judicial motivada | Até 6 meses (limite global 720 dias) |

### Para fixar
- O juiz não participa das negociações da delação premiada, atuando exclusivamente na homologação.
- O depoimento do colaborador não basta para fundamentar condenações ou prisões preventivas.
- A delação premiada eficaz pode outorgar perdão judicial ou redução penal em até dois terços.
- A ação controlada em território doméstico prescinde de autorização judicial, demandando comunicação prévia.
- A infiltração de policiais em campo depende de autorização judicial prévia e dura até seis meses.
- A infiltração virtual em redes telemáticas vigora por seis meses e comporta limite global de 720 dias.""",
      "synthetic": [
        "**Delação desjudicializada**: o juiz não participa das tratativas do acordo de colaboração, cabendo-lhe apenas homologá-lo.",
        "**Veto à condenação solitária**: nenhuma sentença condenatória ou cautelar pode sustentar-se unicamente na fala do delator.",
        "**Benefícios do colaborador**: viabiliza-se o perdão judicial, diminuição de até dois terços da pena ou penas alternativas.",
        "**Ação controlada interna**: consiste no retardo do flagrante mediante comunicação prévia ao juiz, sem requerer prévia autorização.",
        "**Infiltração com crivo judicial**: a infiltração de agentes em campo reclama autorização do magistrado pelo prazo de seis meses.",
        "**Infiltração cibernética**: o monitoramento disfarçado na internet opera por até seis meses com limite máximo de 720 dias.",
        "**Excludente do infiltrado**: o agente disfarçado não responde pelos atos ilícitos proporcionais cometidos sob inexigibilidade."
      ]
    }
  ]
}

Path("content/items/legislacao-penal-especial/a15.json").write_text(json.dumps(items_a15, ensure_ascii=False, indent=2), encoding="utf-8")
Path("content/summaries/legislacao-penal-especial/a15.json").write_text(json.dumps(summaries_a15, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved a15 files successfully.")
