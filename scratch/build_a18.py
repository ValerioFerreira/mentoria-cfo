import json
import subprocess
from pathlib import Path

# AULA 18: Lei 11.343/2006 (Lei de Drogas)

items_a18 = {
  "aula": "legislacao-penal-especial/a18",
  "batch": "pcpe-bizu-legislacao-penal-especial",
  "status": "DRAFT",
  "stage": "bizu",
  "segments": [
    {
      "id": "legislacao-penal-especial/a18/s01",
      "bizu": {
        "summary": [
          "**Norma penal em branco**: os tipos da Lei 11.343/2006 dependem de complementação por ato administrativo infralegal da autoridade sanitária (Portaria 344/1998 da Anvisa).",
          "**Conceito de SISNAD**: o Sistema Nacional de Políticas Públicas sobre Drogas congrega órgãos dos entes federativos voltados à prevenção, atenção e repressão ao narcotráfico.",
          "**Princípios orientadores**: a política nacional funda-se no respeito aos direitos humanos fundamentais e na responsabilidade compartilhada entre Estado e corpo social.",
          "**Órgão colegiado diretivo**: o Conselho Nacional de Políticas sobre Drogas (CONAD) atua como instância formuladora superior de diretrizes normativas e operacionais.",
          "**Integração federativa**: o SISNAD descentraliza ações preventivas articulando União, estados, Distrito Federal e municípios na rede assistencial.",
          "**Distinção de eixos**: a política sobre drogas estrutura-se em duas vertentes autônomas: o tratamento e reinserção do usuário e a repressão ao tráfico ilícito.",
          "**Atualização do rol**: substâncias retiradas dos atos da Anvisa deixam de caracterizar droga ilícita, aplicando-se o princípio da retroatividade da norma mais benéfica.",
          "**Responsabilidade comunitária**: estimula-se a coparticipação de entidades privadas sem fins lucrativos e comunidades terapêuticas acolhedoras."
        ],
        "teoria": [
          {
            "statement": "Os crimes tipificados na Lei de Drogas são estruturados como normas penais completas, dispensando qualquer complementação por atos normativos infralegais do Poder Executivo.",
            "isTrue": False,
            "explanation": "Trata-se de normas penais em branco heterogêneas, cujo elemento normativo 'droga' depende de portaria administrativa regulamentar da Anvisa."
          },
          {
            "statement": "O Sistema Nacional de Políticas Públicas sobre Drogas (SISNAD) adota o princípio da responsabilidade compartilhada entre o poder público e a sociedade civil.",
            "isTrue": True,
            "explanation": "O art. 4º, I, da Lei 11.343/2006 consagra expressamente a responsabilidade compartilhada como diretriz basilar do SISNAD."
          },
          {
            "statement": "O Conselho Nacional de Políticas sobre Drogas (CONAD) é órgão com atribuição privativa e exclusiva para o julgamento de recursos penais em matéria de entorpecentes.",
            "isTrue": False,
            "explanation": "O CONAD é órgão colegiado consultivo e deliberativo de políticas públicas governamentais, não exercendo qualquer função jurisdicional."
          },
          {
            "statement": "A revogação de determinada substância da lista de substâncias proibidas da Anvisa opera abolitio criminis retroativa em benefício do acusado.",
            "isTrue": True,
            "explanation": "Sendo norma penal em branco, a alteração benéfica do complemento administrativo repercute na esfera penal retroativamente (art. 2º do Código Penal)."
          }
        ],
        "revisao": [
          {
            "statement": "A atuação do SISNAD é centralizada de forma unipessoal e restrita aos órgãos policiais da administração direta federal.",
            "isTrue": False,
            "explanation": "O SISNAD é descentralizado e articulado entre a União, estados e municípios, abrangendo saúde, educação e assistência social."
          },
          {
            "statement": "A prevenção do uso indevido de substâncias entorpecentes constitui objetivo fundamental autônomo expressamente traçado na Lei 11.343/2006.",
            "isTrue": True,
            "explanation": "O art. 3º do diploma elenca a prevenção ao consumo abusivo de drogas como um dos dois grandes pilares de atuação institucional do sistema."
          },
          {
            "statement": "A Lei 11.343/2006 atribui às Forças Armadas a responsabilidade primordial pelo tratamento médico e psicológico dos dependentes químicos no país.",
            "isTrue": False,
            "explanation": "A atenção à saúde e reinserção social recai sobre a rede do SUS e do SUAS, não integrando a missão constitucional primária das Forças Armadas."
          },
          {
            "statement": "A articulação com entidades da sociedade civil organizada é diretriz indispensável para a eficácia das medidas preventivas disciplinadas no SISNAD.",
            "isTrue": True,
            "explanation": "O modelo preventivo estabelecido no art. 4º estimula a participação e o engajamento comunitário permanente."
          }
        ],
        "pointers": [
          {"topic": "Definição de drogas e norma penal em branco", "pageRef": 3},
          {"topic": "Princípios e finalidades institucionais do SISNAD", "pageRef": 6},
          {"topic": "Composição e competências do CONAD", "pageRef": 9},
          {"topic": "Descentralização federativa e comunidades terapêuticas", "pageRef": 11}
        ]
      }
    },
    {
      "id": "legislacao-penal-especial/a18/s02",
      "bizu": {
        "summary": [
          "**Diretrizes de prevenção**: as ações preventivas devem focar na conscientização escolar e comunitária, evitando estigmatização de usuários e dependentes.",
          "**Atividades de atenção**: compreendem cuidados multiprofissionais de saúde visando à redução de danos, desintoxicação e reinserção ocupacional e familiar.",
          "**Modalidades de internação**: o tratamento da dependência comporta a internação voluntária e a internação involuntária sob expressa indicação médica.",
          "**Internação involuntária**: formalizada a pedido de familiar ou responsável legal, depende de laudo médico circunstanciado e comunicação ao MP em 72 horas.",
          "**Comunicação ao Ministério Público**: o início e o término da internação involuntária devem ser cientificados ao Ministério Público e à Defensoria em três dias.",
          "**Duração da involuntária**: a internação involuntária perdura pelo tempo necessário à desintoxicação, fixado o prazo máximo legal de noventa dias.",
          "**Vedações em comunidades**: é expressamente vedada a internação involuntária de usuários no âmbito de comunidades terapêuticas acolhedoras.",
          "**Vínculo com o SUS**: as unidades assistenciais do SISNAD integram funcionalmente a Rede de Atenção Psicossocial (RAPS) do Sistema Único de Saúde."
        ],
        "teoria": [
          {
            "statement": "A internação involuntária do usuário de substâncias entorpecentes pode ser realizada em comunidade terapêutica por decisão do dirigente da entidade.",
            "isTrue": False,
            "explanation": "A Lei 11.343/2006 (art. 23-A, § 9º) proíbe taxativamente a realização de qualquer modalidade de internação involuntária em comunidades terapêuticas acolhedoras."
          },
          {
            "statement": "A internação involuntária depende de expressa recomendação de profissional médico e deve ser comunicada ao Ministério Público no prazo de setenta e duas horas.",
            "isTrue": True,
            "explanation": "Conforme o art. 23-A, § 7º, a internação involuntária exige laudo médico e prévia comunicação ao Ministério Público estadual no prazo de 72 horas."
          },
          {
            "statement": "O prazo máximo admitido por lei para a permanência do paciente em regime de internação involuntária de desintoxicação é de cento e oitenta dias.",
            "isTrue": False,
            "explanation": "O art. 23-A, § 8º, estipula que a internação involuntária durará o tempo necessário à desintoxicação no prazo máximo improrrogável de 90 dias."
          },
          {
            "statement": "As atividades de atenção e reinserção social do dependente de drogas devem observar a abordagem de redução de vulnerabilidades e danos individuais.",
            "isTrue": True,
            "explanation": "O art. 20 consagra a reinserção social pautada em critérios técnicos humanizados de acolhimento psicossocial e reabilitação cidadã."
          }
        ],
        "revisao": [
          {
            "statement": "A internação voluntária do dependente de drogas independe de sua expressa declaração de consentimento no momento da admissão hospitalar.",
            "isTrue": False,
            "explanation": "A internação voluntária caracteriza-se obrigatoriamente pela concordância manifestada expressamente pelo paciente no ato do acolhimento."
          },
          {
            "statement": "A interrupção da internação involuntária pode ser determinada a qualquer tempo pelo médico responsável pelo tratamento clínico do dependente.",
            "isTrue": True,
            "explanation": "O art. 23-A, § 6º, confere ao médico assistente ou à família a prerrogativa de determinar a alta da internação involuntária."
          },
          {
            "statement": "A internação involuntária pode ser formalizada por requisição verbal de qualquer pessoa estranha ao núcleo familiar do indivíduo sem laudo clínico.",
            "isTrue": False,
            "explanation": "A internação involuntária reclama pedido de familiar ou responsável legal e imprescindível autorização formal de médico registrado no CRM."
          },
          {
            "statement": "A rede pública de saúde deve garantir acesso universal e gratuito a leitos especializados e ambulatórios de atenção aos usuários de entorpecentes.",
            "isTrue": True,
            "explanation": "Trata-se de garantia expressa nas diretrizes do SISNAD articuladas com os princípios do Sistema Único de Saúde."
          }
        ],
        "pointers": [
          {"topic": "Diretrizes de prevenção nas escolas e comunidades", "pageRef": 13},
          {"topic": "Atividades de atenção e redução de danos", "pageRef": 15},
          {"topic": "Regime da internação involuntária e laudo médico", "pageRef": 18},
          {"topic": "Prazos de desintoxicação e fiscalização pelo MP", "pageRef": 20}
        ]
      }
    },
    {
      "id": "legislacao-penal-especial/a18/s03",
      "bizu": {
        "summary": [
          "**Condutas do art. 28**: adquirir, guardar, transportar, tiver em depósito ou trazer consigo drogas para consumo pessoal sem autorização legal ou regulamentar.",
          "**Cultivo para uso próprio**: o § 1º sujeita às mesmas sanções o cultivo doméstico de espécimes vegetais voltados ao preparo de substância para uso estritamente individual.",
          "**Rol exaustivo de penas**: admoestação formal sobre os malefícios das substâncias, atribuição de serviços comunitários e comparecimento obrigatório a atividades pedagógicas.",
          "**Vedação à prisão**: não se admite pena privativa de liberdade, prisão em flagrante nem custódia cautelar em nenhuma circunstância no art. 28.",
          "**Duração das sanções educativas**: prestação de serviços e cursos duram no máximo cinco meses; em caso de reincidência específica o prazo amplia-se para até dez meses.",
          "**Prescrição bienal**: a pretensão punitiva e executória dos crimes do art. 28 prescreve no lapso especial de dois anos, conforme o art. 30 da norma.",
          "**Procedimento em TCO**: a autoridade policial lavra Termo Circunstanciado de Ocorrência (TCO) e encaminha o agente ao JECRIM, liberando-o de pronto após compromisso.",
          "**Critérios distintivos**: o juiz avaliará a quantidade e natureza da substância, local e condições da ação, antecedentes e circunstâncias pessoais para diferenciar usuário de traficante."
        ],
        "teoria": [
          {
            "statement": "O indivíduo surpreendido portando entorpecentes para consumo pessoal pode ser submetido à prisão em flagrante e recolhido ao cárcere se recusar assinar o termo de comparecimento.",
            "isTrue": False,
            "explanation": "O art. 48, § 2º, proíbe expressamente a prisão em flagrante e o recolhimento à prisão para o autor do fato do art. 28 da Lei 11.343/2006."
          },
          {
            "statement": "As penas restritivas de comparecimento a curso educativo e prestação de serviços comunitários do art. 28 possuem prazo máximo de cumprimento fixado em cinco meses.",
            "isTrue": True,
            "explanation": "O art. 28, § 3º, estipula o prazo máximo de cinco meses para as penas dos incisos II e III, extensível a dez meses apenas na reincidência específica."
          },
          {
            "statement": "A prescrição da pretensão punitiva do crime de posse de drogas para consumo pessoal rege-se pelo prazo geral de quatro anos estabelecido no Código Penal.",
            "isTrue": False,
            "explanation": "O art. 30 da Lei 11.343/2006 prevê prazo prescricional especial de 2 anos para a prescrição das penas cominadas no art. 28."
          },
          {
            "statement": "Para verificar se a substância destinava-se a consumo pessoal, o magistrado deve analisar conjuntamente a natureza da droga, o local do fato e os antecedentes do autor.",
            "isTrue": True,
            "explanation": "Essa é a determinação do art. 28, § 2º, para distinguir objetiva e subjetivamente o porte de uso próprio da mercancia ilícita."
          }
        ],
        "revisao": [
          {
            "statement": "A conduta de cultivar pequena quantidade de plantas com o desígnio de preparar droga para consumo individual é punida com pena de reclusão de um a três anos.",
            "isTrue": False,
            "explanation": "O cultivo para consumo pessoal (art. 28, § 1º) submete-se às mesmas penas brandas do caput (advertência, prestação de serviços ou medida educativa)."
          },
          {
            "statement": "A reincidência que autoriza a elevação para até dez meses do prazo das penas educativas do art. 28 deve ser obrigatoriamente específica em delitos da mesma natureza.",
            "isTrue": True,
            "explanation": "O § 4º do art. 28 exige a reincidência específica na mesma infração do art. 28 para exasperar o teto temporal para até 10 meses."
          },
          {
            "statement": "A condenação irrecorrível anterior pelo art. 28 da Lei de Drogas gera reincidência capaz de afastar o benefício do tráfico privilegiado em novo processo criminal.",
            "isTrue": False,
            "explanation": "O STF e o STJ consolidaram entendimento de que a condenação prévia pelo art. 28 não gera reincidência para afastar a causa de diminuição do tráfico privilegiado."
          },
          {
            "statement": "Em caso de descumprimento injustificado das medidas educativas do art. 28, o juiz pode impor sucessivamente admoestação verbal e multa cominativa.",
            "isTrue": True,
            "explanation": "Conforme o art. 28, § 6º, o descumprimento das medidas fixadas enseja admoestação verbal e, subsidiariamente, sanção de multa pecuniária."
          }
        ],
        "pointers": [
          {"topic": "Condutas do art. 28 e cultivo para uso pessoal", "pageRef": 22},
          {"topic": "Sanções cominadas e vedação ao cárcere", "pageRef": 25},
          {"topic": "Prescrição bienal do art. 30 e limites de prazo", "pageRef": 29},
          {"topic": "Procedimento sumaríssimo do TCO no art. 48", "pageRef": 32}
        ]
      }
    },
    {
      "id": "legislacao-penal-especial/a18/s04",
      "bizu": {
        "summary": [
          "**Plurinuclearidade do art. 33**: o tráfico de drogas contempla dezoito núcleos verbais autônomos, caracterizando crime de ação múltipla e perigo abstrato.",
          "**Tráfico privilegiado (§ 4º)**: causa de diminuição de pena de um sexto a dois terços concedida ao réu primário, de bons antecedentes, sem vínculo com orcrim.",
          "**Natureza não hedionda**: o tráfico privilegiado não é crime hediondo, aplicando-se regras ordinárias de progressão de regime prisional e substituição restritiva.",
          "**Uso compartilhado (§ 3º)**: ceder substância sem intuito de auferir vantagem pecuniária a pessoa de convívio próximo para fruição compartilhada constitui infração penal de menor potencial ofensivo.",
          "**Petrechos para o tráfico (art. 34)**: fabricar, adquirir ou possuir instrumentos, aparelhos ou objetos destinados à preparação de drogas é crime formal e subsidiário.",
          "**Associação para o tráfico (art. 35)**: reunião estável e permanente de duas ou mais pessoas para a prática reiterada do tráfico ou de seus tipos assemelhados.",
          "**Financiamento do tráfico (art. 36)**: punição autônoma e severa com reclusão de oito a vinte anos para aquele que financia ou custeia o narcotráfico.",
          "**Colaborador informante (art. 37)**: tipifica a conduta de colaborar como informante com grupo, organização ou associação voltada ao tráfico ilícito."
        ],
        "teoria": [
          {
            "statement": "A causa de diminuição de pena do tráfico privilegiado descrita no art. 33, § 4º, desnatura a hediondez do crime de tráfico de entorpecentes.",
            "isTrue": True,
            "explanation": "O STF no HC 118.533 e a jurisprudência sumulada do STJ assentaram que o tráfico privilegiado não ostenta caráter hediondo."
          },
          {
            "statement": "O crime de associação para o tráfico do art. 35 configura-se diante do concurso eventual e transitório de duas pessoas na venda de drogas.",
            "isTrue": False,
            "explanation": "A jurisprudência exige de forma pacífica o dolo de associação estável e permanente (animus associativo); a união ocasional é mero concurso de pessoas."
          },
          {
            "statement": "A conduta de oferecer droga a amigo de relacionamento íntimo para consumo conjunto e sem intuito de lucro configura a infração atenuada do art. 33, § 3º.",
            "isTrue": True,
            "explanation": "Trata-se do delito de uso compartilhado, punido com detenção de seis meses a um ano e classificado como infração de menor potencial ofensivo."
          },
          {
            "statement": "O crime de petrechos para o tráfico (art. 34) mantém sua tipicidade autônoma mesmo quando o agente for flagrado vendendo a droga acabada com os aparelhos.",
            "isTrue": False,
            "explanation": "O crime do art. 34 possui natureza subsidiária, sendo absorvido pelo tráfico de drogas (art. 33) pelo princípio da consunção quando praticados no mesmo contexto."
          }
        ],
        "revisao": [
          {
            "statement": "Para a caracterização do crime de financiamento do tráfico do art. 36, é indispensável que o investidor participe pessoalmente da comercialização das drogas.",
            "isTrue": False,
            "explanation": "O art. 36 pune autonomamente a conduta de financiar ou custear o tráfico, sendo irrelevante a prática de atos materiais de venda pelo financiador."
          },
          {
            "statement": "O informante do tráfico tipificado no art. 37 deve atuar sem integrar diretamente a estrutura estável da respectiva associação criminosa.",
            "isTrue": True,
            "explanation": "O tipo do art. 37 exige que a colaboração seja prestada como informante externo; integrando a estrutura do bando, o agente responde pelo art. 35."
          },
          {
            "statement": "A substituição da pena privativa de liberdade por restritivas de direitos é proibida de forma absoluta a qualquer condenado por tráfico de drogas pelo art. 33.",
            "isTrue": False,
            "explanation": "O STF declarou inconstitucional a vedação genérica e abstrata de conversão de penas no tráfico (HC 97.256 e Resolução nº 5/2012 do Senado Federal)."
          },
          {
            "statement": "O réu condenado por tráfico privilegiado pode progredir de regime prisional observando as frações comuns de cumprimento de pena da LEP.",
            "isTrue": True,
            "explanation": "Por não ser hediondo, o tráfico privilegiado submete-se às regras de execução penal comuns para delitos sem resultado morte."
          }
        ],
        "pointers": [
          {"topic": "Verbos nucleares do art. 33 e tipos equiparados", "pageRef": 35},
          {"topic": "Requisitos e natureza do tráfico privilegiado", "pageRef": 38},
          {"topic": "Associação para o tráfico e estabilidade societária", "pageRef": 40},
          {"topic": "Financiamento do narcotráfico e colaborador informante", "pageRef": 42}
        ]
      }
    },
    {
      "id": "legislacao-penal-especial/a18/s05",
      "bizu": {
        "summary": [
          "**Prescrição culposa médica**: punição autônoma no art. 38 para o médico, dentista ou farmacêutico que ministra ou prescreve culposamente substância controlada.",
          "**Condução náutica ou aérea**: o art. 39 criminaliza conduzir embarcação ou aeronave após consumo de drogas, expondo a dano potencial a segurança de outrem.",
          "**Tráfico transnacional majorado**: o art. 40, I, exaspera a pena de um sexto a dois terços quando a conduta delituosa conectar o território nacional ao exterior.",
          "**Tráfico interestadual**: a majorante do art. 40, V, incide comprovada a destinação interestadual, dispensando a efetiva travessia de fronteiras (Súmula 587 do STJ).",
          "**Imediações de locais sensíveis**: o tráfico nas imediações de presídios, escolas, hospitais ou em transportes públicos sofre aumento penal obrigatório (art. 40, III).",
          "**Prevalência funcional**: o cometimento do delito por agente público prevalecendo-se da função atrai exasperação legal de um sexto a dois terços da sanção.",
          "**Vulnerabilidade da infância**: o tráfico que envolve ou visa atingir criança, adolescente ou inimputável sujeita-se à causa de aumento do art. 40, VI.",
          "**Regime das majorantes**: as causas de aumento do art. 40 aplicam-se a todos os crimes previstos nos arts. 33 a 37 da Lei de Drogas."
        ],
        "teoria": [
          {
            "statement": "Para a incidência da causa de aumento do tráfico interestadual, é indispensável a efetiva transposição física da fronteira entre os estados da Federação.",
            "isTrue": False,
            "explanation": "A Súmula 587 do STJ estabelece que para a incidência da majorante do tráfico interestadual é desnecessária a efetiva transposição de fronteiras estaduais."
          },
          {
            "statement": "O médico que prescreve culposamente quantidade excessiva de medicamento psicotrópico responde por crime formalmente tipificado no art. 38 da lei.",
            "isTrue": True,
            "explanation": "O art. 38 da Lei 11.343/2006 prevê a modalidade culposa consistente em prescrever ou ministrar culposamente drogas sem necessidade terapêutica."
          },
          {
            "statement": "A causa de aumento pelo tráfico cometido nas imediações de presídios exige prova pericial de que a droga destinava-se aos detentos encarcerados no estabelecimento.",
            "isTrue": False,
            "explanation": "O STJ firmou entendimento de que a majorante do art. 40, III, é de natureza objetiva e espacial, bastando a mercancia delituosa nas imediações do presídio."
          },
          {
            "statement": "O cometimento do delito de tráfico com o emprego de violência ou mediante arma de fogo acarreta elevação obrigatória de um sexto a dois terços da pena.",
            "isTrue": True,
            "explanation": "Conforme o art. 40, IV, a utilização de violência, grave ameaça ou armamento bélico opera como causa de aumento da sanção penal."
          }
        ],
        "revisao": [
          {
            "statement": "A causa de aumento de pena da transnacionalidade do tráfico pode ser cumulada licitamente com o crime de contrabando pelo mesmo fato.",
            "isTrue": False,
            "explanation": "A conduta de ingressar com droga no país tipifica tráfico internacional majorado (art. 33 c/c art. 40, I), não havendo concurso com contrabando."
          },
          {
            "statement": "A exasperação penal decorrente de a droga envolver ou atingir criança ou adolescente incide ainda que o menor figure apenas como transportador intermediário da droga.",
            "isTrue": True,
            "explanation": "O art. 40, VI, majora a pena quando a prática visar a atingir ou utilizar criança ou adolescente em qualquer etapa executória da mercancia."
          },
          {
            "statement": "A majorante por crime cometido em transporte público incide em desfavor do passageiro que transporta entorpecente discretamente acondicionado em bagagem lacrada.",
            "isTrue": False,
            "explanation": "O STJ pacificou que a majorante do transporte público exige comercialização no interior do veículo ou disseminação aos demais passageiros."
          },
          {
            "statement": "O funcionário público que pratica o tráfico valendo-se das prerrogativas funcionais de seu cargo tem sua sanção carcerária aumentada de um sexto a dois terços.",
            "isTrue": True,
            "explanation": "O art. 40, II, da Lei de Drogas comina exasperação da pena ao agente estatal que atua com violação funcional de seus deveres institucionais."
          }
        ],
        "pointers": [
          {"topic": "Condutas culposas e condução de embarcações", "pageRef": 44},
          {"topic": "Majorantes do tráfico transnacional e interestadual", "pageRef": 46},
          {"topic": "Tráfico nas imediações de presídios e escolas", "pageRef": 48},
          {"topic": "Envolvimento de crianças e violação funcional", "pageRef": 51}
        ]
      }
    },
    {
      "id": "legislacao-penal-especial/a18/s06",
      "bizu": {
        "summary": [
          "**Prazos dilatados do inquérito**: trinta dias para réu preso e noventa dias para réu solto, admitida duplicação excepcional dos lapsos mediante justificativa acolhida pelo juiz.",
          "**Laudo pericial provisório**: o laudo preliminar de constatação da substância subscrito por perito ou pessoa idônea basta para fundamentar prisão em flagrante e denúncia.",
          "**Laudo pericial definitivo**: o exame químico-toxicológico definitivo é peça indispensável para a prolação de sentença condenatória de mérito no crime de tráfico.",
          "**Incineração em flagrante**: as drogas apreendidas com flagrante são incineradas no prazo de quinze dias, após autorização judicial e resguardo de amostras.",
          "**Incineração sem flagrante**: apreendida substância sem autoria conhecida, a destruição ocorre em trinta dias; plantações ilícitas são destruídas de imediato pela polícia.",
          "**Defesa preliminar prévia**: oferecida a denúncia, o réu é notificado para ofertar defesa prévia por escrito em dez dias, antecedendo o juízo de recebimento.",
          "**Interrogatório ao final**: embora a literalidade da lei especial situe o interrogatório no início da audiência, o STF impõe que seja o último ato da instrução.",
          "**Perdimento e medidas assecuratórias**: bens e veículos empregados habitualmente no narcotráfico sofrem sequestro cautelar e perdimento em prol da União."
        ],
        "teoria": [
          {
            "statement": "O inquérito policial instaurado para apurar crime de tráfico de drogas em face de indiciado preso deve ser concluído no prazo de trinta dias, duplicável por autorização judicial.",
            "isTrue": True,
            "explanation": "O art. 51 prevê o prazo dilatado de 30 dias para réu preso (duplicável) e 90 dias para investigado solto (também duplicável judicialmente)."
          },
          {
            "statement": "A lavratura do auto de prisão em flagrante por tráfico de drogas reclama obrigatoriamente a juntada imediata do laudo pericial definitivo nos autos.",
            "isTrue": False,
            "explanation": "O art. 50, § 1º, dispõe expressamente que o laudo de constatação provisório firmado por perito ou pessoa idônea é suficiente para a lavratura do flagrante."
          },
          {
            "statement": "A destruição por incineração das drogas apreendidas na hipótese de prisão em flagrante delito deve ocorrer no prazo de quinze dias perante autoridade sanitária.",
            "isTrue": True,
            "explanation": "O art. 50, § 3º, estipula o prazo de 15 dias para destruição das drogas com flagrante, com prévia autorização judicial e reserva de contraprova."
          },
          {
            "statement": "A audiência de instrução e julgamento na Lei de Drogas deve manter o interrogatório do acusado como o primeiro ato procedimental em observância ao princípio da especialidade.",
            "isTrue": False,
            "explanation": "O STF fixou tese de que o interrogatório deve ser sempre o último ato da instrução penal (art. 400 do CPP), sob pena de nulidade processual por cerceamento de defesa."
          }
        ],
        "revisao": [
          {
            "statement": "No procedimento da Lei de Drogas, o magistrado recebe a denúncia imediatamente após seu oferecimento antes de notificar o acusado.",
            "isTrue": False,
            "explanation": "O art. 55 institui a notificação prévia do denunciado para apresentação de defesa prévia no prazo de 10 dias, antes de qualquer decisão sobre o recebimento da peça acusatória."
          },
          {
            "statement": "As plantações ilícitas de substâncias psicotrópicas descobertas pela autoridade policial devem ser destruídas de imediato mediante prévia incineração no local.",
            "isTrue": True,
            "explanation": "O art. 32 determina que as glebas cultivadas com plantas entorpecentes ilegais sejam incineradas imediatamente pelas autoridades policiais."
          },
          {
            "statement": "A destruição de entorpecentes apreendidos cuja autoria delitiva seja ignorada deve ser realizada pela polícia no prazo improrrogável de quarenta e oito horas.",
            "isTrue": False,
            "explanation": "O art. 50-A prevê o prazo de 30 dias para a incineração das substâncias ilícitas apreendidas sem ocorrência de prisão em flagrante."
          },
          {
            "statement": "O perdimento de bens móveis utilizados no tráfico de drogas exige demonstração de sua habitualidade na prática do narcotráfico conforme a jurisprudência consolidada.",
            "isTrue": True,
            "explanation": "A jurisprudência exige nexo e utilização habitual ou adulteração do veículo no tráfico para decretar o perdimento definitivo em favor da União."
          }
        ],
        "pointers": [
          {"topic": "Prazos do inquérito policial e laudo preliminar", "pageRef": 53},
          {"topic": "Incineração de drogas e destruição de plantações", "pageRef": 56},
          {"topic": "Defesa prévia em dez dias e recebimento da denúncia", "pageRef": 60},
          {"topic": "Interrogatório como último ato e perda de bens", "pageRef": 66}
        ]
      }
    }
  ]
}

# RESUMOS A18
summaries_a18 = {
  "aula": "legislacao-penal-especial/a18",
  "batch": "pcpe-summary-legislacao-penal-especial",
  "status": "DRAFT",
  "segments": [
    {
      "id": "legislacao-penal-especial/a18/s01",
      "fingerprint": {
        "startPage": 3,
        "endPage": 12,
        "startTopic": "SISNAD e Medidas de Prevenção ao Uso Indevido de Drogas"
      },
      "analytic": """A Lei 11.343/2006 estruturou o Sistema Nacional de Políticas Públicas sobre Drogas, inaugurando no país um marco normativo dualista que separa o tratamento assistencial dispensado aos usuários da repressão penal intransigente ao narcotráfico organizado. O diploma incorporou compromissos internacionais como a Convenção de Viena e diretrizes sanitárias da Anvisa.

### Conceito de Drogas e Norma Penal em Branco
A estrutura típica da legislação especial é indissociável de regulação complementar administrativa:
- **Norma Penal em Branco Heterogênea**: os tipos penais da lei não definem exaustivamente o que é droga, dependendo da integração por portaria infralegal editada pela Agência Nacional de Vigilância Sanitária (Portaria 344/1998 da Anvisa), que disciplina substâncias psicotrópicas, precursoras e plantas sob fiscalização;
- **Efeitos da Desregulamentação**: a exclusão de uma substância do rol oficial da Anvisa acarreta *abolitio criminis*, beneficiando retroativamente acusados e sentenciados;
- **Uso em Rituais Religiosos**: a legislação ressalva a possibilidade de autorização excepcional para o plantio e cultivo de vegetais destinados exclusivamente a ritos religiosos tradicionais, conforme deliberações do CONAD.

### Finalidades e Princípios Estruturantes do SISNAD
O SISNAD congrega órgãos federais, estaduais, distritais e municipais sob princípios específicos:
- **Respeito aos Direitos Humanos Fundamentais**: garantia de cidadania e dignidade, combatendo preconceitos e discriminações contra dependentes químicos;
- **Responsabilidade Compartilhada**: consagra a articulação cooperativa entre Poder Público, família e sociedade organizada na formulação e execução de planos locais e nacionais;
- **Descentralização Operacional**: divisão de competências na atenção psicossocial e na repressão entre os entes da Federação brasileira para coordenar ações de inteligência;
- **Conselho Nacional de Políticas sobre Drogas (CONAD)**: colegiado superior deliberativo encarregado de traçar as diretrizes de prevenção, reinserção social e controle de entorpecentes.

### Estruturação de Políticas e Comunidades Terapêuticas
O sistema preconiza a criação de redes integradas de assistência:
- **Prevenção Universal e Focalizada**: ações pedagógicas contínuas em ambientes educacionais, laborais e comunitários;
- **Comunidades Terapêuticas Acolhedoras**: entidades privadas sem fins lucrativos que prestam apoio voluntário a dependentes em regime residencial transitório, sendo terminantemente proibidas de executar qualquer medida involuntária ou forçada.

### Para fixar
- A Lei de Drogas é norma penal em branco heterogênea integrada pela Anvisa.
- O SISNAD funda-se no princípio da responsabilidade compartilhada entre Estado e sociedade.
- O CONAD exerce função normativa e consultiva na formulação das políticas sobre drogas.
- A exclusão de uma substância do rol da Anvisa gera imediata abolitio criminis.
- A descentralização federativa compele estados e municípios a manterem programas preventivos.
- Comunidades terapêuticas acolhedoras atuam sob estrita adesão voluntária do usuário.""",
      "synthetic": [
        "**Norma penal em branco**: a qualificação dogmática de substância entorpecente reclama integração pela Anvisa.",
        "**Princípio compartilhado**: a prevenção e o controle de entorpecentes envolvem a atuação cooperativa do Estado e da sociedade.",
        "**Papel central do CONAD**: órgão colegiado incumbido de fixar diretrizes e planos nacionais para políticas sobre entorpecentes.",
        "**Retroatividade benéfica**: a retirada de determinada substância da portaria sanitária extingue a punibilidade penal retroativamente.",
        "**Descentralização do SISNAD**: articulação federativa de competências entre União, estados e municípios para saúde pública.",
        "**Comunidades acolhedoras**: atuam na assistência residencial voluntária do dependente químico, sem jamais admitir coação física."
      ]
    },
    {
      "id": "legislacao-penal-especial/a18/s02",
      "fingerprint": {
        "startPage": 13,
        "endPage": 21,
        "startTopic": "Das atividades de prevenção do uso indevido, atenção e reinserção social de usuários e dependentes de drogas"
      },
      "analytic": """A Lei 11.343/2006 dedica extenso capítulo às atividades voltadas à prevenção, tratamento clínico e resgate da cidadania dos usuários e dependentes de drogas, reformulado substancialmente pela Lei 13.840/2019 com a instituição de planos municipais e estaduais para coibir o consumo indevido.

### Eixos da Prevenção e Redução de Danos
As medidas preventivas são orientadas por fundamentos científicos e humanizados:
- **Educação Preventiva**: abordagem nas escolas orientada ao fortalecimento da autoestima e esclarecimento dos riscos e fatores de vulnerabilidade pessoal e social;
- **Redução de Danos e Vulnerabilidades**: promoção de condutas que atenuem os prejuízos individuais e sociais decorrentes do consumo problemático;
- **Integração com o SUS e SUAS**: atuação alinhada à Rede de Atenção Psicossocial (RAPS) e aos Centros de Atenção Psicossocial (CAPS) por meio de projeto terapêutico singular individualizado.

### Modalidades de Internação e Regramentos Médicos
A internação de dependentes de drogas é medida assistencial extrema e residual:
- **Internação Voluntária**: formalizada perante manifestação de vontade expressa do próprio paciente, que assina termo de adesão no ato da admissão e pode postular sua alta clínica a qualquer tempo;
- **Internação Involuntária**: processa-se sem o consentimento do paciente, reclamando requisitos legais cumulativos indispensáveis:
  1. Requerimento subscrito por familiar, responsável legal ou, na ausência, por servidor da área da saúde ou assistência social onde se localize o paciente;
  2. Prévia e indispensável autorização emitida por médico inscrito no Conselho Regional de Medicina (CRM);
  3. Realização exclusiva em unidades de saúde e hospitais gerais estruturados (sendo vedada em comunidades terapêuticas);
  4. Comunicação compulsória ao Ministério Público e à Defensoria Pública no prazo improrrogável de **72 horas** do início e da alta;
  5. Duração limitada estritamente ao tempo de desintoxicação física, perdurará pelo prazo máximo legal de noventa dias.

### Reabilitação Social e Ocupacional
O estatuto preconiza o estímulo à capacitação técnica profissionalizante e reinserção ocupacional de dependentes recuperados, garantindo prioridade de acesso a programas governamentais de fomento ao trabalho.

### Para fixar
- A internação de dependente químico constitui medida de caráter excepcional e residual.
- A internação involuntária exige prévio laudo médico e solicitação formal de familiar.
- É vedada a internação involuntária no ambiente de comunidades terapêuticas.
- O Ministério Público deve ser notificado da internação involuntária em até 72 horas.
- O tempo máximo admitido por lei para a internação involuntária é de 90 dias.
- O tratamento orienta-se pela reinserção familiar, ocupacional e social do indivíduo.""",
      "synthetic": [
        "**Excepcionalidade da internação**: a segregação médica é providência extrema voltada ao restabelecimento físico do dependente.",
        "**Internação involuntária médica**: reclama laudo subscrito por profissional do CRM e solicitação expressa de familiar do paciente.",
        "**Prazo máximo de 90 dias**: a internação forçada perdurará pelo tempo necessário à desintoxicação até o limite de três meses.",
        "**Comunicação ministerial em 72h**: o início e a cessação da internação involuntária devem ser cientificados ao Ministério Público.",
        "**Vedação às comunidades**: é proibida por lei a realização de internações involuntárias em comunidades terapêuticas acolhedoras.",
        "**Integração na RAPS**: os serviços de acolhimento e reinserção social conectam-se às diretrizes operacionais do SUS."
      ]
    },
    {
      "id": "legislacao-penal-especial/a18/s03",
      "fingerprint": {
        "startPage": 22,
        "endPage": 34,
        "startTopic": "Porte de Drogas para Consumo Pessoal (art. 28)"
      },
      "analytic": """O art. 28 da Lei 11.343/2006 inaugurou a despenalização do porte de entorpecentes para consumo pessoal no ordenamento nacional, afastando o cárcere e impondo medidas exclusivamente socioeducativas. O Supremo Tribunal Federal, ao julgar o porte de cannabis, reinterpretou parâmetros quantitativos sem afastar o poder de polícia ostensiva.

### Condutas Típicas e Cultivo para Uso Próprio
- **Núcleos do Caput**: adquirir, guardar, tiver em depósito, transportar ou trazer consigo drogas para consumo pessoal sem autorização ou em desacordo com determinação legal;
- **Cultivo para Uso Pessoal (§ 1º)**: equipara-se à conduta básica aquele que realiza semeadura ou colheita de plantas com o desígnio de preparar entorpecentes em diminuta escala para consumo próprio.

### Sanções Cominadas e Ausência de Cárcere
O legislador baniu as penas privativas de liberdade para o usuário, fixando penas alternativas restritivas:
1. **Advertência solene sobre os efeitos deletérios das drogas**;
2. **Prestação de serviços comunitários em entidades públicas ou de saúde**;
3. **Medida educativa de comparecimento a programa ou curso educativo especializado**.
- **Prazos de Cumprimento (§§ 3º e 4º)**: as medidas de prestação de serviços e cursos vigoram pelo prazo máximo de **5 meses**; em caso de reincidência específica no art. 28, o prazo amplia-se para até **10 meses**;
- **Sucessão por Descumprimento (§ 6º)**: recusando-se o autor injustificadamente a cumprir a pena, o juiz aplicará admoestação verbal e, sucessivamente, sanção de multa pecuniária cominativa. Jamais haverá conversão em prisão.

### Procedimento Policial e Prescrição Especial
- **Procedimento no Art. 48**: é expressamente vedada a prisão em flagrante e o recolhimento ao cárcere. A autoridade policial lavra Termo Circunstanciado de Ocorrência (TCO), apreende a substância e intima o autor a comparecer ao Juizado Especial Criminal (JECRIM);
- **Prazo Prescricional de 2 Anos (art. 30)**: a prescrição da pretensão punitiva e executória do art. 28 opera no lapso temporal bienal;
- **Critérios Judiciais de Diferenciação (§ 2º)**: para aferir se a substância destina-se a uso próprio ou mercancia, o juiz atentará à quantidade e qualidade da droga apreendida, ao local e condições da ação, aos antecedentes e circunstâncias fáticas pessoais e contatos em telefone.

### Para fixar
- O art. 28 baniu categoricamente as penas privativas de liberdade para usuários.
- O cultivo de plantas destinadas ao preparo de pequena quantidade equipara-se ao porte pessoal.
- As medidas de prestação de serviços e cursos educativos vigoram por até cinco meses.
- Na reincidência específica no art. 28, o prazo máximo eleva-se para dez meses.
- É vedada a lavratura de flagrante com encarceramento, adotando-se o Termo Circunstanciado.
- As penas do art. 28 prescrevem no prazo especial de dois anos.""",
      "synthetic": [
        "**Despenalização do usuário**: aboliram-se penas carcerárias para a posse de substâncias destinadas a consumo individual.",
        "**Cultivo em pequena escala**: a semeadura ou colheita para preparo de uso próprio submete-se às mesmas penas brandas.",
        "**Sanções alternativas**: aplicam-se advertência, prestação de serviços comunitários e comparecimento a programas educativos.",
        "**Prazos de cinco e dez meses**: as medidas educativas duram até cinco meses, ampliando-se a dez meses na reincidência específica.",
        "**Vedação à custódia em cela**: é proibida a decretação de prisão em flagrante ou preventiva em desfavor do usuário do art. 28.",
        "**Prescrição bienal especial**: a ação penal e as medidas executórias do art. 28 prescrevem no prazo especial de dois anos."
      ]
    },
    {
      "id": "legislacao-penal-especial/a18/s04",
      "fingerprint": {
        "startPage": 35,
        "endPage": 43,
        "startTopic": "Tráfico Ilícito de Drogas e Tipos Equiparados (arts. 33 a 37)"
      },
      "analytic": """A repressão ao narcotráfico estrutura-se em tipos plurinucleares de alta reprovabilidade social, cominando sanções severas nos arts. 33 a 37 da Lei 11.343/2006. A doutrina e a jurisprudência analisam a presença de balança de precisão, divisão de entorpecentes e atos de mercancia reiterada para alicerçar a acusação.

### O Crime de Tráfico e Tipos Equiparados
- **Tráfico Básico (art. 33, caput)**: pune dezoito condutas alternativas (como importar, exportar, remeter, preparar, produzir, vender, expor à venda, transportar, ter em depósito, guardar e fornecer drogas), com reclusão de 5 a 15 anos e multa. Trata-se de crime de ação múltipla e perigo abstrato;
- **Tipos Equiparados (art. 33, § 1º)**: incorre nas mesmas penas quem comercializa matéria-prima ou insumo para preparação de drogas, semeia plantas entorpecentes em larga escala ou cede imóvel para o tráfico;
- **Uso Compartilhado (art. 33, § 3º)**: o ato de disponibilizar substância sem intuito de auferir ganho a parceiro próximo para consumo concomitante consubstancia crime de menor potencial ofensivo, punido com detenção de seis meses a um ano.

### O Tráfico Privilegiado (§ 4º do art. 33)
Causa especial de diminuição de pena que reduz a sanção carcerária de **1/6 a 2/3**:
- **Requisitos Cumulativos Obrigatórios**:
  1. Primariedade técnica do agente;
  2. Bons antecedentes criminais;
  3. Não se dedicar habitualmente a atividades criminosas;
  4. Não integrar organização criminosa;
- **Natureza Jurídica**: os tribunais superiores e a LEP consolidaram que o **tráfico privilegiado não é crime hediondo**, autorizando a progressão de regime em frações comuns e a substituição da pena privativa de liberdade por restritivas de direitos.

### Petrechos, Associação, Financiamento e Informante
- **Petrechos para o Tráfico (art. 34)**: possuir, fabricar ou guardar instrumentos e maquinários para refino de drogas. Delito subsidiário absorvido pelo art. 33 se no mesmo contexto;
- **Associação para o Tráfico (art. 35)**: ajuste de duas ou mais pessoas com dolo de associação estável e permanente para o cometimento do tráfico (pena: 3 a 10 anos);
- **Financiamento do Tráfico (art. 36)**: financiar ou custear a prática delituosa, com pena reclusiva gravosa de 8 a 20 anos;
- **Colaborador Informante (art. 37)**: colaborar como informante (fogueteiro ou sentinela) com grupo ou organização criminosa voltada ao narcotráfico, sem integrar sua estrutura societária permanente.

### Para fixar
- O art. 33 do tráfico abrange 18 núcleos verbais em crime de ação múltipla.
- O uso compartilhado eventual e sem lucro entre pessoas de relacionamento é crime atenuado.
- O tráfico privilegiado reduz a pena de um sexto a dois terços para réus primários.
- O tráfico privilegiado não é crime hediondo, permitindo penas alternativas.
- A associação para o tráfico exige liame estável e permanente entre duas ou mais pessoas.
- O financiador do tráfico responde por crime autônomo punido com reclusão de 8 a 20 anos.""",
      "synthetic": [
        "**Ação múltipla no tráfico**: o art. 33 congrega dezoito verbos nucleares autônomos punidos com reclusão de cinco a quinze anos.",
        "**Requisitos do privilégio**: o § 4º reclama agente primário, com bons antecedentes e desvinculado de facções criminosas.",
        "**Ausência de hediondez**: o tráfico privilegiado perdeu o caráter hediondo perante a jurisprudência sumulada e a LEP.",
        "**Uso compartilhado suave**: fornecer droga ocasional e sem intuito lucrativo a amigo para consumo comum é delito atenuado.",
        "**Petrechos subsidiários**: a posse de maquinários do art. 34 resta absorvida pelo tráfico quando ocorrida no mesmo cenário fático.",
        "**Estabilidade associativa**: o art. 35 reclama comunhão de desígnios duradoura e permanente entre pelo menos duas pessoas.",
        "**Crime de financiamento**: custear ou injetar recursos no tráfico configura conduta autônoma sancionada com reclusão severa."
      ]
    },
    {
      "id": "legislacao-penal-especial/a18/s05",
      "fingerprint": {
        "startPage": 44,
        "endPage": 52,
        "startTopic": "Da condução de embarcação ou aeronave sob a influência de drogas"
      },
      "analytic": """A Lei 11.343/2006 contempla condutas de perigo em transportes especiais e institui um rol abrangente de causas de aumento de pena aplicáveis às infrações de narcotráfico, reprimindo a circulação de substâncias como cloreto de etila (lança-perfume) e entorpecentes vindos de países vizinhos como a Argentina e Bolívia.

### Condutas em Meios de Transporte e Tipos Culposos
- **Prescrição Culposa de Substâncias (art. 38)**: receitar ou ministrar por imprudência ou negligência medicamentos controlados sem que haja real necessidade clínica do paciente. Exclusivo de profissionais de saúde habilitados (médicos, dentistas e farmacêuticos);
- **Condução Náutica ou Aérea (art. 39)**: pilotar embarcação ou aeronave após ingerir drogas psicotrópicas, expondo a dano potencial a segurança viária e coletiva. Pena: detenção de 6 meses a 3 anos e apreensão da nave;
- **Qualificadora por Transporte Coletivo**: se a embarcação ou aeronave for destinada ao transporte público ou coletivo de passageiros, as penas são aplicadas cumulativamente com sanções aumentadas.

### Causas Especiais de Aumento de Pena (Art. 40)
As penas dos arts. 33 a 37 sofrem exasperação fracionária de **1/6 a 2/3** nas seguintes situações:
- **Transnacionalidade (inciso I)**: quando a conduta delitiva conectar o Brasil a território estrangeiro;
- **Prevalência Funcional (inciso II)**: praticado o crime por agente público no exercício de função ou a pretexto de exercê-la;
- **Locais Sensíveis e Aglomerações (inciso III)**: nas dependências ou imediações de presídios, hospitais, educandários, transporte público ou sedes esportivas e culturais;
- **Emprego de Violência ou Armamento (inciso IV)**: uso de violência, grave ameaça ou arma de fogo;
- **Tráfico Interestadual (inciso V)**: quando evidenciada a destinação interfederativa da substância, sendo **desnecessária a efetiva transposição da fronteira interestadual** (Súmula 587 do STJ);
- **Vulnerabilidade Infantojuvenil (inciso VI)**: quando a prática delituosa envolver ou visar atingir criança, adolescente ou inimputável mental;
- **Financiamento Privilegiado (inciso VII)**: quando o agente exercer papel de liderança ou custeio na associação.

### Para fixar
- A prescrição culposa de substâncias entorpecentes é crime próprio do profissional de saúde.
- Conduzir embarcação ou avião sob efeito de drogas é crime de perigo comum potencial.
- As majorantes do art. 40 exasperam a reprimenda em fração variável de um sexto a dois terços.
- O tráfico interestadual prescinde da transposição física de fronteiras para incidir a majorante.
- O tráfico nas imediações de presídios ou escolas atrai causa de aumento de feição objetiva.
- O envolvimento de menor de dezoito anos na mercância eleva obrigatoriamente a pena aplicada.""",
      "synthetic": [
        "**Prescrição culposa na saúde**: o art. 38 criminaliza o médico ou farmacêutico que receita ou aplica drogas por negligência grave.",
        "**Transportes marítimo e aéreo**: conduzir aeronaves ou embarcações sob efeito químico expondo terceiros é crime autônomo.",
        "**Fração das majorantes**: as hipóteses qualificadoras do art. 40 acarretam exasperação penal de um sexto a dois terços da sanção.",
        "**Dispensabilidade de fronteira**: a Súmula 587 do STJ dispensa a transposição interestadual para incidência da causa de aumento.",
        "**Espaço sensível objetivo**: o tráfico cometido próximo a escolas e estabelecimentos prisionais atrai majorante automática.",
        "**Envolvimento de menores**: a participação ou cooptação de crianças e adolescentes majora a reprimenda do narcotráfico."
      ]
    },
    {
      "id": "legislacao-penal-especial/a18/s06",
      "fingerprint": {
        "startPage": 53,
        "endPage": 69,
        "startTopic": "Procedimento Penal e Investigação do Tráfico de Drogas"
      },
      "analytic": """O rito procedimental da Lei 11.343/2006 contempla prazos dilatados no inquérito policial, garantias de defesa preliminar anterior ao recebimento da denúncia e regras estritas para a incineração de entorpecentes e expropriação de bens, com destinação de valores em moeda nacional ou estrangeira depositados ao Fundo Nacional Antidrogas.

### Inquérito Policial e Prazos Especiais
O art. 51 institui prazos diferenciados para a apuração da polícia judiciária nos crimes dos arts. 33 a 37:
- **Investigado Preso**: conclusão em **30 dias**, prorrogável por igual período (mais 30 dias) perante representação motivada autorizada pelo juiz;
- **Investigado Solto**: conclusão em **90 dias**, igualmente duplicável (mais 90 dias) mediante despacho judicial fundamentado.

### Laudos Periciais e Destruição de Drogas
- **Laudo Preliminar de Constatação (art. 50, § 1º)**: identifica os caracteres da substância entorpecente, subscrito por perito oficial ou pessoa idônea. É suficiente para lavratura de flagrante e oferecimento da denúncia;
- **Laudo Toxicológico Definitivo**: indispensável para embasar o decreto condenatório de mérito;
- **Destruição com Prisão em Flagrante (art. 50, § 3º)**: incineração no prazo de **15 dias**, com prévia autorização judicial, presença do MP e autoridade sanitária e guarda de contraprova;
- **Destruição sem Prisão em Flagrante (art. 50-A)**: prazo de **30 dias** para incineração de drogas apreendidas sem autoria conhecida;
- **Plantações Ilícitas (art. 32)**: devem ser incineradas imediatamente pela autoridade policial no local.

### Rito Processual e Interrogatório do Réu
O procedimento especial da Lei de Drogas organiza-se em fases solenes:
1. Oferecida a denúncia, o juiz notifica o denunciado para oferecer **defesa prévia em 10 dias** (art. 55);
2. Apresentada a resposta, o juiz delibera sobre o recebimento ou rejeição da inicial acusatória;
3. Se recebida a denúncia, designa-se audiência de instrução e julgamento;
4. **Momento do Interrogatório**: a lei especial posicionava o interrogatório no início da audiência (art. 57). Contudo, o Plenário do STF consolidou que **o interrogatório deve ser sempre o último ato da instrução** (art. 400 do CPP), prestigiando a ampla defesa.

### Medidas Assecuratórias e Perdimento de Bens
Bens móveis, imóveis e veículos empregados habitualmente no tráfico ou adquiridos com proveito criminoso sofrem sequestro cautelar, alienação antecipada e decretação de perdimento definitivo em prol do Fundo Nacional Antidrogas (FUNAD), livres de tributos e encargos anteriores.

### Para fixar
- O inquérito policial por tráfico tem prazo de 30 dias para réu preso e 90 dias para réu solto.
- O laudo preliminar de constatação é suficiente para a lavratura do auto de prisão em flagrante.
- A incineração de drogas apreendidas em flagrante dá-se em 15 dias; sem flagrante, em 30 dias.
- As plantações ilícitas encontradas devem ser incineradas de pronto pela polícia judiciária.
- O réu tem prazo de dez dias para protocolizar defesa prévia antes do recebimento da denúncia.
- O interrogatório do acusado deve ser o último ato da audiência conforme tese firmada pelo STF.""",
      "synthetic": [
        "**Prazos investigativos ampliados**: o inquérito policial vigora por trinta dias para preso e noventa dias para indiciado solto.",
        "**Suficiência do laudo preliminar**: a constatação provisória de entorpecentes autoriza o flagrante e o oferecimento da denúncia.",
        "**Incineração em quinze dias**: as drogas apreendidas com flagrante são destruídas em quinze dias, resguardada amostra pericial.",
        "**Defesa preliminar em dez dias**: o denunciado apresenta resposta por escrito antes de o juiz decidir receber a peça acusatória.",
        "**Interrogatório ao final**: a Suprema Corte impôs a realização do interrogatório do acusado como o último ato da instrução penal.",
        "**Perdimento patrimonial integral**: veículos e bens utilizados no narcotráfico sofrem confisco definitivo em favor da União."
      ]
    }
  ]
}

Path("content/items/legislacao-penal-especial/a18.json").write_text(json.dumps(items_a18, ensure_ascii=False, indent=2), encoding="utf-8")
Path("content/summaries/legislacao-penal-especial/a18.json").write_text(json.dumps(summaries_a18, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved a18 files successfully.")
