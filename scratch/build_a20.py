import json
from pathlib import Path

# AULA 20: Crimes Ambientais (Lei 9.605/1998)

ref_segs = {s["id"]: s for s in json.loads(Path("content/segments/legislacao-penal-especial.json").read_text(encoding="utf-8"))["segments"]}

items_a20 = {
  "aula": "legislacao-penal-especial/a20",
  "batch": "pcpe-bizu-legislacao-penal-especial",
  "status": "DRAFT",
  "stage": "bizu",
  "segments": [
    {
      "id": "legislacao-penal-especial/a20/s01",
      "bizu": {
        "summary": [
          "**Responsabilidade penal autônoma da PJ**: a pessoa jurídica pode ser processada e punida independentemente da responsabilização concomitante da pessoa física.",
          "**Requisitos de imputação societária**: a conduta deve decorrer de decisão de órgão de direção ou diretoria e ser praticada no interesse ou proveito da entidade.",
          "**Sanções aplicáveis à pessoa jurídica**: sujeita-se a penas de multa, restritivas de direitos (interdição, suspensão) e prestação de serviços à comunidade ecológica.",
          "**Desconsideração da personalidade**: autoriza-se afastar o manto societário sempre que for obstáculo ao ressarcimento dos prejuízos infligidos ao meio ambiente.",
          "**Circunstâncias atenuantes próprias**: rol do art. 14 elenca baixo grau de instrução do agente, arrependimento com reparação espontânea e comunicação prévia de perigo.",
          "**Circunstâncias agravantes específicas**: rol do art. 15 contempla reincidência, dolo de obter vantagem pecuniária, ação noturna ou em domingos e feriados.",
          "**Penas alternativas a pessoas físicas**: admitem-se prestação pecuniária, perda de bens, prestação de serviços comunitários, recolhimento domiciliar e interdição.",
          "**Aplicação subsidiária codificada**: as disposições da legislação penal comum e da legislação adjetiva aplicam-se subsidiariamente aos crimes ambientais."
        ],
        "teoria": [
          {
            "statement": "O Superior Tribunal de Justiça e o Supremo Tribunal Federal mantêm a exigência da teoria da dupla imputação como condição de procedibilidade da ação penal ambiental contra pessoas jurídicas.",
            "isTrue": False,
            "explanation": "A jurisprudência consolidou a superação da dupla imputação, admitindo a responsabilização penal isolada da pessoa jurídica sem a pessoa física."
          },
          {
            "statement": "A desconsideração da personalidade jurídica no âmbito ambiental pode ser decretada sempre que sua existência representar óbice ao ressarcimento integral dos prejuízos causados ao meio ambiente.",
            "isTrue": True,
            "explanation": "O art. 4º da Lei 9.605/1998 expressamente autoriza a desconsideração quando a pessoa jurídica for obstáculo à reparação ecológica."
          },
          {
            "statement": "A Lei 9.605/1998 comina pena privativa de liberdade carcerária para a pessoa jurídica condenada por crime ambiental continuado.",
            "isTrue": False,
            "explanation": "À pessoa jurídica aplicam-se somente penas de multa, restritivas de direitos e prestação de serviços comunitários, inexistindo cárcere para entes morais."
          },
          {
            "statement": "A reparação espontânea e cabal do dano ambiental antes do julgamento é consagrada como circunstância atenuante de pena na Lei 9.605/1998.",
            "isTrue": True,
            "explanation": "O estatuto elenca no art. 14 a voluntária recomposição ecológica do prejuízo infligido antes da condenação como atenuante legal genérica."
          }
        ],
        "revisao": [
          {
            "statement": "A responsabilidade penal da pessoa jurídica exclui e imuniza integralmente a responsabilidade penal dos administradores e executivos autores materiais do fato delituoso.",
            "isTrue": False,
            "explanation": "O art. 3º, parágrafo único, deixa claro que a responsabilidade da entidade não exclui a das pessoas físicas coautoras ou partícipes."
          },
          {
            "statement": "A interdição temporária de direitos e a prestação pecuniária configuram penas restritivas de direitos legalmente cabíveis a pessoas físicas na lei ambiental.",
            "isTrue": True,
            "explanation": "O art. 8º da lei lista expressamente as modalidades de penas restritivas substitutivas da privação de liberdade do autor natural."
          },
          {
            "statement": "O baixo nível de escolaridade do agente infrator não pode ser valorado pelo magistrado para fins de atenuação da pena nos crimes ambientais.",
            "isTrue": False,
            "explanation": "O art. 14, I, elenca explicitamente o baixo grau de instrução ou escolaridade do agente como causa atenuante subjetiva."
          },
          {
            "statement": "O cometimento de crime ambiental em domingos, feriados ou durante o repouso noturno consubstancia circunstância agravante legal expressa.",
            "isTrue": True,
            "explanation": "O art. 15, II, 'm', agrava a reprimenda quando a prática delituosa ocorrer em período de menor vigilância, como domingos e noites."
          }
        ],
        "pointers": [
          {"topic": "Responsabilidade penal de pessoas físicas e jurídicas", "pageRef": 3},
          {"topic": "Penas aplicáveis às pessoas jurídicas e desconsideração", "pageRef": 7},
          {"topic": "Penas restritivas de direitos para pessoas físicas", "pageRef": 11},
          {"topic": "Circunstâncias atenuantes e agravantes da lei ambiental", "pageRef": 15}
        ]
      }
    },
    {
      "id": "legislacao-penal-especial/a20/s02",
      "bizu": {
        "summary": [
          "**Tutela da fauna silvestre**: incrimina matar, caçar, perseguir ou utilizar espécimes da fauna nativa ou em rota migratória sem licença do órgão ambiental.",
          "**Perdão judicial na guarda doméstica**: faculta ao magistrado deixar de aplicar a pena na posse doméstica não comercial de espécie silvestre não ameaçada.",
          "**Maus-tratos e qualificadora qualificada**: maltratar animais é punido com detenção; tratando-se de cão ou gato, a pena é reclusão de dois a cinco anos (Lei Sansão).",
          "**Introdução de espécie exótica**: punição criminal ao ingresso desautorizado de animal exótico em território nacional sem parecer técnico e licença expedida.",
          "**Pesca predatória e proibida**: tipifica a pesca em épocas de defeso, em locais interditados ou mediante o emprego de explosivos ou substâncias tóxicas.",
          "**Excludentes especiais de abate**: o abate não é punível se praticado em estado de necessidade para saciar fome, para proteger lavouras ou se animal for nocivo.",
          "**Majorantes gerais na fauna**: penas exasperadas se o crime for perpetrado contra espécie ameaçada de extinção, em unidade de conservação ou à noite.",
          "**Guarda e apreensão de petrechos**: redes, armadilhas, embarcações e instrumentos utilizados na caça ilegal sofrem apreensão e descarte ou doação pública."
        ],
        "teoria": [
          {
            "statement": "O abate de espécimes da fauna silvestre praticado para debelar a inanição e fome pessoal ou de familiares configura crime ambiental com pena mitigada.",
            "isTrue": False,
            "explanation": "O art. 37, I, consagra excludente de criminalidade quando o abate objetivar exclusivamente assegurar a subsistência alimentar imediata da família necessitada."
          },
          {
            "statement": "A prática de abuso ou maus-tratos praticada contra cães ou gatos submete o infrator a pena privativa de liberdade sob a modalidade de reclusão de dois a cinco anos.",
            "isTrue": True,
            "explanation": "A Lei Sansão incluiu o § 1º-A no art. 32 da Lei 9.605/1998, cominando reclusão de 2 a 5 anos quando a vítima for cão ou gato."
          },
          {
            "statement": "O perdão judicial previsto na Lei de Crimes Ambientais pode ser concedido pelo juiz mesmo que o animal silvestre sob guarda doméstica esteja listado como ameaçado de extinção.",
            "isTrue": False,
            "explanation": "O art. 29, § 2º, veda a concessão do perdão judicial se a espécie silvestre mantida domesticamente figurar na lista oficial de animais ameaçados de extinção."
          },
          {
            "statement": "A pesca realizada mediante a utilização de explosivos ou de substâncias tóxicas é apenada mais severamente em face do perigo comum de destruição da biomassa aquática.",
            "isTrue": True,
            "explanation": "O art. 35 tipifica como forma qualificada a pesca predatória com explosivos ou substâncias venenosas, cominando reclusão de 1 a 5 anos."
          }
        ],
        "revisao": [
          {
            "statement": "Animais nascidos em criadouros comerciais legalizados e devidamente registrados são equiparados aos espécimes da fauna silvestre livre para fins do art. 29.",
            "isTrue": False,
            "explanation": "O § 3º do art. 29 ressalva que os espécimes provenientes de criadouros autorizados e devidamente anilhados ou marcados não caracterizam fauna silvestre clandestina."
          },
          {
            "statement": "A conduta de introduzir espécime animal no território brasileiro sem o prévio parecer técnico favorável e licença governamental configura crime ambiental autônomo.",
            "isTrue": True,
            "explanation": "O art. 31 criminaliza a introdução de espécime animal exótico no país sem parecer técnico oficial favorável e licença da autoridade ambiental."
          },
          {
            "statement": "A exportação de peles e couros de anfíbios e répteis em estado bruto é conduta lícita no país independentemente de controle fazendário ou sanitário.",
            "isTrue": False,
            "explanation": "O art. 30 da lei tipifica criminalmente a exportação de peles e couros em bruto de anfíbios e répteis sem expressa autorização legal."
          },
          {
            "statement": "O cometimento de crime contra a fauna silvestre em unidade de conservação constitui causa especial de aumento da reprimenda penal.",
            "isTrue": True,
            "explanation": "O art. 29, § 4º, V, prevê o aumento da pena de metade se o crime for perpetrado no interior de unidade de conservação."
          }
        ],
        "pointers": [
          {"topic": "Tipicidade e excludentes no crime contra a fauna", "pageRef": 18},
          {"topic": "Maus-tratos e qualificadora para cães e gatos", "pageRef": 21},
          {"topic": "Pesca predatória e modalidades proibidas", "pageRef": 24},
          {"topic": "Causas de justificação e aumento de pena na fauna", "pageRef": 26}
        ]
      }
    },
    {
      "id": "legislacao-penal-especial/a20/s03",
      "bizu": {
        "summary": [
          "**Destruição de APP**: destruir ou danificar florestas de preservação permanente configura delito grave apenado com detenção de um a três anos.",
          "**Incêndio em mata ou floresta**: provocar queimadas deliberadas em florestas sujeita o autor a reclusão de dois a quatro anos; admite modalidade culposa.",
          "**Fabricação e soltura de balões**: fabricar, vender, transportar ou soltar balões que possam ocasionar incêndios é crime formal de perigo abstrato (art. 42).",
          "**Dano a plantas ornamentais**: destruir ou maltratar vegetação de logradouro público ou propriedade privada alheia consubstancia crime punido com detenção.",
          "**Comércio ilegal de madeira**: adquirir ou transportar lenha, carvão ou madeira sem licença válida do vendedor e guia de transporte florestal válida.",
          "**Exploração de floresta nativa**: desmatar ou explorar economicamente floresta de domínio público ou nativa sem autorização do órgão competente.",
          "**Corte de árvores em APP**: cortar árvores em área de preservação permanente sem autorização prévia atrai sanção privativa de detenção e multa.",
          "**Penalidades administrativas conexas**: as condutas contra a flora desencadeiam autos de infração ambiental, embargo de obra e recuperação compulsória."
        ],
        "teoria": [
          {
            "statement": "O crime de fabricar, vender, transportar ou soltar balões do art. 42 exige comprovação de incêndio florestal efetivo para que se tenha consumado.",
            "isTrue": False,
            "explanation": "Trata-se de crime formal e de perigo abstrato, consumando-se com a simples conduta de fabricar, vender, transportar ou soltar balão que possa provocar fogo."
          },
          {
            "statement": "O delito de provocar incêndio em mata ou floresta previsto no art. 41 admite expressamente a modalidade culposa na legislação ambiental.",
            "isTrue": True,
            "explanation": "O parágrafo único do art. 41 expressamente pune a modalidade culposa de incêndio com detenção de seis meses a um ano e multa."
          },
          {
            "statement": "O corte de árvores isoladas em propriedade privada urbana é sempre atípico na esfera criminal, gerando unicamente penalidades tributárias municipais.",
            "isTrue": False,
            "explanation": "O corte ou dano a árvores em locais especialmente protegidos, praças ou vias públicas configura infração penal ambiental (arts. 39 e 49)."
          },
          {
            "statement": "A aquisição ou estocagem comercial de madeira e carvão vegetal sem a licença outorgada pela autoridade ambiental competente tipifica infração criminal.",
            "isTrue": True,
            "explanation": "O art. 46, parágrafo único, criminaliza a conduta de receber ou adquirir madeira, lenha ou carvão para fins industriais sem licença válida."
          }
        ],
        "revisao": [
          {
            "statement": "A destruição dolosa de floresta de preservação permanente pode ser praticada exclusivamente por pessoas jurídicas industriais de grande porte.",
            "isTrue": False,
            "explanation": "Trata-se de crime comum que pode ser cometido por qualquer pessoa física ou jurídica que execute a destruição ou dano à área protegida."
          },
          {
            "statement": "A destruição ou danificação de plantas ornamentais de logradouros públicos ou praças municipais configura crime ambiental punido com detenção.",
            "isTrue": True,
            "explanation": "O art. 49 tipifica a conduta de destruir, danificar, lesar ou maltratar plantas de ornamentação de logradouros públicos ou propriedade alheia."
          },
          {
            "statement": "A comercialização de motosserras prescinde de qualquer registro ou controle cadastral perante os órgãos de fiscalização ambiental do Sisnama.",
            "isTrue": False,
            "explanation": "O art. 51 criminaliza a comercialização, posse ou porte de motosserra sem licença ou registro expedido pelo órgão ambiental competente."
          },
          {
            "statement": "O desmatamento não autorizado de floresta nativa atrai incidência penal sancionatória cumulada com a obrigação de recomposição integral da vegetação nativa.",
            "isTrue": True,
            "explanation": "O art. 50-A e os preceitos civis e penais impõem sanções reclusivas cumuladas com a reparação material ecológica da área desmatada."
          }
        ],
        "pointers": [
          {"topic": "Proteção a florestas de preservação permanente (APP)", "pageRef": 28},
          {"topic": "Incêndios florestais e tipicidade da soltura de balões", "pageRef": 31},
          {"topic": "Comércio de produtos florestais, lenha e carvão", "pageRef": 34},
          {"topic": "Dano a plantas ornamentais e porte de motosserra", "pageRef": 36}
        ]
      }
    },
    {
      "id": "legislacao-penal-especial/a20/s04",
      "bizu": {
        "summary": [
          "**Crime de poluição qualificada**: causar poluição de qualquer natureza que resulte ou possa resultar em danos à saúde humana ou mortandade de animais (art. 54).",
          "**Modalidades culposas de poluição**: o art. 54 admite a forma culposa se a poluição for decorrente de negligência técnica ou imperícia operacional.",
          "**Mineração e extração em APP**: extrair minerais, areia ou cal em florestas públicas ou de preservação permanente sem licença configura delito autônomo.",
          "**Pichação e grafite artístico**: pichar edificação urbana é crime; a prática de grafite não constitui delito se tiver finalidade artística e consentimento expresso.",
          "**Funcionário público prevaricador**: o servidor público que emite licença ambiental em desconformidade com a lei ou faz afirmação falsa responde criminalmente.",
          "**Obstaculização da fiscalização**: criar embaraços ou impedir a fiscalização dos órgãos ambientais (IBAMA, ICMBio) configura delito próprio do art. 69.",
          "**Laudo ou relatório pericial falso**: apresentar laudo ambiental falso ou enganoso em processo de licenciamento sujeita o autor a reclusão e multa (art. 69-A).",
          "**Competência e tutela administrativa**: infrações contra ordenamento urbano e patrimônio cultural harmonizam-se com a fiscalização urbanística municipal."
        ],
        "teoria": [
          {
            "statement": "A Lei 9.605/1998 criminaliza de forma idêntica a pichação e o grafite urbano, não admitindo qualquer excludente de tipicidade em favor do grafite artístico.",
            "isTrue": False,
            "explanation": "O art. 65, § 2º, descriminaliza expressamente o grafite quando praticado com finalidade artística, valorização do patrimônio e consentimento do titular."
          },
          {
            "statement": "O crime de poluição do art. 54 admite responsabilização criminal tanto a título de conduta dolosa quanto na modalidade culposa.",
            "isTrue": True,
            "explanation": "O § 1º do art. 54 expressamente sanciona a modalidade culposa de poluição com detenção de seis meses a um ano e multa."
          },
          {
            "statement": "O servidor público que expede licença ou autorização ambiental contrariando normas legais comete mera infração administrativa imune a processo penal.",
            "isTrue": False,
            "explanation": "O art. 67 pune com detenção o agente público que defere chancela ou outorga ambiental infringindo comandos normativos e regulamentares."
          },
          {
            "statement": "Elaborar ou apresentar laudo ou estudo ambiental falso ou enganoso no âmbito de procedimento de licenciamento consubstancia crime autônomo punido com reclusão.",
            "isTrue": True,
            "explanation": "O art. 69-A pune a elaboração ou apresentação de estudo ou laudo ambiental falso ou enganoso com pena de reclusão de três a seis anos e multa."
          }
        ],
        "revisao": [
          {
            "statement": "A extração de areia e minerais em leito de rio ou floresta de preservação permanente é tolerada no país para agentes que atuam sem autorização prévia.",
            "isTrue": False,
            "explanation": "O art. 44 criminaliza a extração mineral em florestas públicas ou de preservação permanente sem prévia e indispensável autorização ambiental."
          },
          {
            "statement": "A conduta de obstar ou dificultar a fiscalização praticada por agentes do órgão ambiental tipifica o crime previsto no art. 69 da Lei 9.605/1998.",
            "isTrue": True,
            "explanation": "O art. 69 da lei tipifica criminalmente a conduta de criar obstáculos ou dificultar a fiscalização desempenhada pelo Poder Público ambiental."
          },
          {
            "statement": "A poluição em recursos hídricos que provoque o corte no fornecimento urbano de água potável à coletividade é desprovida de previsão qualificada.",
            "isTrue": False,
            "explanation": "O art. 54, § 2º, III, qualifica a infração de poluição caso cause a cessação do suprimento de água à comunidade local."
          },
          {
            "statement": "O depósito ou descarte clandestino de substâncias tóxicas ou perigosas em desacordo com as exigências técnicas regulamentares atrai sancionamento penal.",
            "isTrue": True,
            "explanation": "O art. 56 pune a produção, processamento, estocagem, transporte ou abandono de substâncias tóxicas ou perigosas à saúde humana ou ao meio ambiente."
          }
        ],
        "pointers": [
          {"topic": "Poluição ambiental e modalidades culposas", "pageRef": 38},
          {"topic": "Pichação, ordenamento urbano e descriminalização do grafite", "pageRef": 41},
          {"topic": "Crimes contra a administração ambiental e licença ilegal", "pageRef": 43},
          {"topic": "Obstrução da fiscalização e falsidade em estudo ambiental", "pageRef": 45}
        ]
      }
    }
  ]
}

# RESUMOS A20
summaries_a20 = {
  "aula": "legislacao-penal-especial/a20",
  "batch": "pcpe-summary-legislacao-penal-especial",
  "status": "DRAFT",
  "segments": [
    {
      "id": "legislacao-penal-especial/a20/s01",
      "fingerprint": {
        "startPage": ref_segs["legislacao-penal-especial/a20/s01"]["startPage"],
        "endPage": ref_segs["legislacao-penal-especial/a20/s01"]["endPage"],
        "startTopic": ref_segs["legislacao-penal-especial/a20/s01"].get("startTopic")
      },
      "analytic": """A Lei 9.605/1998 representou um marco dogmático pioneiro ao conferir efetividade ao mandamento do art. 225, § 3º, da Carta Constitucional brasileira, sistematizando a repressão criminal e as sanções administrativas voltadas a conter agressões ao equilíbrio ecológico. O diploma inovou ao introduzir a responsabilização penal da pessoa jurídica e estruturar um sistema autônomo de sanções alternativas orientadas à recomposição do patrimônio coletivo lesado em ilícitos contra a flora e a fauna.

### Responsabilidade Penal Societária e Superação da Dupla Imputação
A tutela ambiental estruturou diretrizes próprias para responsabilizar criminalmente entidades corporativas:
- **Requisitos de Imputação Societária (art. 3º)**: a responsabilização penal do ente moral exige que o ilícito derive de deliberação de seus gestores estatutários ou colegiado diretivo superior, e que a atuação seja consumada em proveito direto ou econômico da entidade coletiva;
- **Superação Definitiva da Teoria da Dupla Imputação**: no passado doutrinário, sustentava-se que a corporação não poderia ser demandada sem a concomitante presença física de seus diretores no polo passivo da ação. Contudo, o Pleno do Supremo Tribunal Federal e o Superior Tribunal de Justiça consolidaram o entendimento de que **a pessoa jurídica pode ser denunciada, processada e condenada de forma autônoma**, prescindindo de acusação conjunta contra os sócios ou administradores;
- **Desconsideração da Personalidade Jurídica (art. 4º)**: autoriza-se afastar o escudo corporativo sempre que sua estrutura societária configurar embaraço ou obstáculo material à satisfação indenizatória das ofensas infligidas ao ecossistema.

### Regime Sancionatório e Penas Especiais
O sistema ambiental diversificou os instrumentos coercitivos admitidos:
- **Sanções Aplicáveis a Pessoas Jurídicas (arts. 21 a 24)**: vedada a imposição de penas privativas de liberdade, cominam-se multas financeiras graduadas, sanções restritivas consubstanciadas na paralisação de linhas industriais, interdição temporária de estabelecimentos e impedimento de contratar com o Poder Público por lapso de 3 a 5 anos, além da prestação de serviços à comunidade (custeio de fundos ecológicos e restauração física de sítios degradados);
- **Penas Substitutivas para Autores Individuais (art. 8º)**: prestação pecuniária destinada a vítimas ou entidades protetivas, confisco de maquinários e embarcações de pesca, recolhimento domiciliar monitorado e interdições de direitos de caça e pesca.

### Dosimetria, Circunstâncias Atenuantes e Agravantes
A fixação da reprimenda judicial observa vetores legais expressos:
- **Atenuantes Próprias (art. 14)**: precária instrução formal do agente; voluntário arrependimento materializado na pronta restauração do dano ecológico; comunicação prévia de risco às autoridades; e colaboração efetiva na fiscalização ambiental;
- **Agravantes Específicas (art. 15)**: reincidência delitiva ambiental; finalidade lucrativa desmedida; induzimento de subordinados; prática no período noturno, domingos ou feriados; emprego de métodos cruéis contra animais; e perpetração em unidades de conservação ou períodos de defeso e seca.

### Para fixar
- A pessoa jurídica responde penalmente por delitos ambientais praticados em seu benefício por órgão diretivo.
- O STF e o STJ superaram a dupla imputação, admitindo persecução exclusiva contra a empresa.
- É proibida a cominação de penas carcerárias para pessoas jurídicas, recaindo penas de multa e restritivas.
- A desconsideração da personalidade é deferida sempre que obstar a reparação dos prejuízos ambientais.
- O baixo grau de escolaridade do agente figura expressamente como atenuante genérica da reprimenda.
- A prática de infração ambiental durante a noite ou feriados atrai agravamento sancionatório obrigatório.""",
      "synthetic": [
        "**Responsabilidade autônoma da pessoa jurídica**: o ente societário pode ser processado e punido isoladamente por infração ambiental sem a pessoa física.",
        "**Requisitos de imputação societária**: a conduta delitiva deve emanar de deliberação diretiva e produzir benefício concreto à pessoa jurídica.",
        "**Sanções societárias exclusivas**: aplicam-se à pessoa jurídica multas pecuniárias, interdições de atividades e prestação de serviços comunitários ecológicos.",
        "**Desconsideração patrimonial protetiva**: o véu corporativo é afastado sempre que impedir a restauração econômica integral do ambiente degradado.",
        "**Atenuante de baixo grau de instrução**: a reduzida escolaridade do infrator e o pronto arrependimento atenuam compulsoriamente a resposta punitiva.",
        "**Agravantes de tempo e vulnerabilidade**: a execução de delitos ambientais no período noturno, feriados ou épocas de seca agrava a sanção penal.",
        "**Penas substitutivas a pessoas físicas**: o diploma prioriza prestação pecuniária, recolhimento domiciliar e tarefas comunitárias substitutivas ao cárcere.",
        "**Aplicação subsidiária codificada**: os preceitos gerais do Código Penal e Código de Processo Penal incidem supletivamente nos crimes ambientais."
      ]
    },
    {
      "id": "legislacao-penal-especial/a20/s02",
      "fingerprint": {
        "startPage": ref_segs["legislacao-penal-especial/a20/s02"]["startPage"],
        "endPage": ref_segs["legislacao-penal-especial/a20/s02"]["endPage"],
        "startTopic": ref_segs["legislacao-penal-especial/a20/s02"].get("startTopic")
      },
      "analytic": """A seção dos crimes contra a fauna tutelou de maneira abrangente os animais silvestres nativos, espécimes em rota migratória e animais domésticos, cominando sanções aos atos de caça clandestina, cativeiro desautorizado, tráfico zoológico e práticas degradantes de crueldade e abusos corporais.

### Tipificação Básica da Fauna Silvestre e Perdão Judicial
- **Condutas Vedadas do Art. 29**: matar, perseguir, caçar, apanhar ou utilizar espécimes da fauna silvestre nativos ou em rota migratória sem a devida licença, autorização ou permissão da autoridade competente, com pena de detenção de seis meses a um ano e multa;
- **Equiparações Típicas (§ 1º)**: incorre nas mesmas sanções quem impede a procriação da fauna sem autorização; quem modifica, danifica ou destrói ninho, abrigo ou criadouro natural; ou quem vende, expõe à venda, adquire, guarda ou transporta ovos, larvas ou espécimes da fauna silvestre sem comprovação de procedência legal;
- **Faculdade do Perdão Judicial (§ 2º)**: na manutenção doméstica de animais nativos desprovida de intuito mercantil, pode o magistrado prescindir da imposição penal se o animal não integrar a lista oficial de espécies sob risco extintivo. Se o espécime estiver ameaçado, o perdão judicial é categoricamente vedado;
- **Majorantes na Fauna (§ 4º)**: a resposta sancionatória é exasperada pela metade quando cometida contra animais raros, em horários noturnos, em áreas de reserva ecológica ou mediante descumprimento dos limites da permissão concedida.

### Maus-Tratos a Animais e Inovação da Lei Sansão
- **Ofensas à Integridade Animal (art. 32)**: comete infração quem comete atos degradantes, castigos imoderados ou mutilações contra seres da fauna urbana ou silvestre, com pena de detenção de três meses a um ano e multa;
- **Qualificadora Específica para Cães e Gatos (Lei 14.064/2020 - § 1º-A)**: quando a agressão violenta for direcionada expressamente contra cão ou gato, a sanção corporal transmuda-se para **reclusão de dois a cinco anos**, multa e cominação obrigatória de proibição da guarda do animal vitimado. A alteração elevou a infração para patamar de gravidade incompatível com os institutos da Lei dos Juizados Especiais.

### Modalidades de Pesca Ilegal e Causas de Exclusão do Abate
- **Pesca Predatória (arts. 34 e 35)**: pescar em períodos nos quais a pesca seja proibida (defeso) ou em locais interditados atrai detenção de um a três anos. A modalidade é qualificada com reclusão de 1 a 5 anos se executada com dinamite, explosivos ou substâncias venenosas na água;
- **Causas Especiais de Justificação do Abate (Art. 37)**: não consubstancia crime o abate de animal quando realizado:
  1. Em estado de necessidade estrito, para saciar a fome do agente infrator ou de sua família;
  2. Para proteger lavouras, pomares ou rebanhos da ação predatória ou destruidora de animais, desde que formalmente autorizado pela autoridade administrativa competente;
  3. Por ser comprovadamente nocivo o animal, desde que assim caracterizado pelo órgão competente de saúde ou agricultura.

### Para fixar
- A caça ou perseguição de espécimes da fauna silvestre sem licença constitui delito do art. 29.
- O perdão judicial é cabível na guarda doméstica de animais que não estejam ameaçados de extinção.
- Maus-tratos contra cães e gatos sujeitam o autor a reclusão de 2 a 5 anos e perda da guarda.
- A pesca predatória com explosivos ou substâncias tóxicas é delito punido com reclusão de um a cinco anos.
- O abate de animal para saciar a fome do agente ou de sua família configura excludente de ilicitude.
- Crimes contra a fauna cometidos em unidades de conservação ou à noite sofrem aumento de pena.""",
      "synthetic": [
        "**Proteção penal da fauna silvestre**: é proibido caçar, apanhar ou manter animais silvestres nativos sem autorização do órgão ambiental.",
        "**Perdão judicial restrito na guarda**: faculta-se ao juiz deixar de apenar a posse doméstica se o animal silvestre não for ameaçado de extinção.",
        "**Qualificadora severa para cães e gatos**: agressões cruéis a caninos e felinos atraem reclusão de dois a cinco anos e perda legal da guarda.",
        "**Pesca predatória qualificada**: o uso de explosivos ou venenos na pesca consubstancia crime punido gravosamente com reclusão.",
        "**Excludente de fome e necessidade**: abater espécime animal para matar a fome do agente ou de sua entidade familiar afasta a tipicidade criminal.",
        "**Abate de animal nocivo autorizado**: a neutralização de espécimes nocivos ou predadores de lavouras exige autorização técnica governamental.",
        "**Exasperação em áreas protegidas**: delitos contra a fauna cometidos no interior de unidades de conservação ensejam aumento de metade da pena.",
        "**Repressão ao comércio de criadouros**: a comercialização clandestina de ovos e crias sem anilhas de controle oficial tipifica infração criminal autônoma."
      ]
    },
    {
      "id": "legislacao-penal-especial/a20/s03",
      "fingerprint": {
        "startPage": ref_segs["legislacao-penal-especial/a20/s03"]["startPage"],
        "endPage": ref_segs["legislacao-penal-especial/a20/s03"]["endPage"],
        "startTopic": ref_segs["legislacao-penal-especial/a20/s03"].get("startTopic")
      },
      "analytic": """Os crimes contra a flora constituem o núcleo mais extenso da tutela penal ecológica na Lei 9.605/1998, conferindo blindagem punitiva rigorosa às áreas de preservação permanente (APP), florestas de domínio público, unidades de conservação e à circulação mercantil de produtos de origem florestal.

### Preservação Permanente e Incêndios Florestais
- **Destruição de Área de Preservação Permanente (art. 38)**: destruir ou danificar floresta considerada de preservação permanente, mesmo que em formação, ou utilizá-la infringindo as normas de proteção legal, com pena de detenção de 1 a 3 anos e multa. Se o fato for culposo, a pena é reduzida à metade;
- **Corte Ilegal de Vegetação em APP (art. 39)**: cortar árvores em floresta de preservação permanente sem a devida autorização formal da autoridade competente;
- **Crime de Incêndio em Mata ou Floresta (art. 41)**: provocar incêndio em mata ou floresta, cominando severa pena de reclusão de 2 a 4 anos e multa. O preceito admite expressamente modalidade culposa no parágrafo único (detenção de seis meses a um ano), sancionando quem ateia queimadas descuidadas que se alastram incontrolavelmente;
- **Soltura e Fabricação de Balões (art. 42)**: fabricar, vender, transportar ou soltar balões que possam provocar incêndios em florestas e demais formas de vegetação, em áreas urbanas ou assentamentos rurais. Trata-se de crime formal e de perigo abstrato, cuja consumação aperfeiçoa-se com o manuseio ou lançamento do artefato, sendo irrelevante a verificação de queimada real.

### Extração Mineral e Comércio Clandestino de Madeira
- **Mineração Clandestina em Vegetação Nativa (art. 44)**: retirar areia, calcário, saibro ou recursos minerais de reservas públicas ou APPs sem chancela estatal prévia (detenção de 6 meses a um ano e multa);
- **Transporte e Comércio Florestal sem Licença (art. 46)**: receber ou adquirir, para fins industriais, comerciais, energéticos ou para consumo, madeira, lenha, carvão vegetal ou outros derivados florestais, sem exigir a exibição de licença válida outorgada pelo vendedor e sem portar a guia de controle ambiental correspondente durante o percurso rodoviário ou hidroviário.

### Plantas Ornamentais e Controle de Motosserras
- **Vandalismo contra Espécimes Paisagísticos (art. 49)**: vilipendiar, arrancar ou estragar mudas e arborização estética de praças municipais ou jardins particulares, prevendo sanção de detenção e causa de diminuição se praticado culposamente;
- **Comercialização e Posse de Motosserras (art. 51)**: comercializar motosserra ou utilizá-la em floresta ou vegetação sem registro ou licença do órgão competente, viabilizando o monitoramento preventivo do desmatamento.

### Para fixar
- Destruir ou danificar floresta de preservação permanente configura crime doloso ou culposo do art. 38.
- Provocar incêndio em mata ou floresta é punido com reclusão de 2 a 4 anos, admitindo forma culposa.
- Fabricar, transportar ou soltar balões é delito formal de perigo abstrato que prescinde de incêndio.
- A extração clandestina de areia ou minerais em floresta pública ou APP configura crime do art. 44.
- Adquirir madeira ou carvão para indústria sem licença e guia ambiental válida é infração penal do art. 46.
- Destruir plantas ornamentais de vias e praças públicas consubstancia crime ambiental autônomo.
- O porte ou uso de motosserra em ambiente florestal exige registro compulsório expedido pelo órgão competente.""",
      "synthetic": [
        "**Proteção de florestas de preservação**: destruir ou degradar áreas de preservação permanente atrai detenção cumulada com recomposição ecológica.",
        "**Incêndio florestal punido com reclusão**: provocar incêndios em matas acarreta reclusão de dois a quatro anos, admitindo modalidade culposa atenuada.",
        "**Perigo abstrato na soltura de balões**: o art. 42 criminaliza formalmente a confecção, transporte ou soltura de balões independentemente de fogo efetivo.",
        "**Mineração ilegal em áreas florestais**: extrair areia, cal ou minerais em florestas públicas e APPs sem licença é crime ambiental específico.",
        "**Controle da cadeia de madeira e carvão**: receber ou transportar insumos florestais sem guia e licença válida do vendedor tipifica o art. 46.",
        "**Tutela de plantas ornamentais públicas**: danificar vegetação paisagística de vias urbanas ou praças configura infração penal autônoma.",
        "**Registro obrigatório de motosserras**: possuir ou operar motosserras em matas sem autorização governamental é conduta criminalizada.",
        "**Desmatamento não autorizado de nativas**: a exploração econômica predatória de florestas nativas atrai sanções reclusivas e embargo administrativo."
      ]
    },
    {
      "id": "legislacao-penal-especial/a20/s04",
      "fingerprint": {
        "startPage": ref_segs["legislacao-penal-especial/a20/s04"]["startPage"],
        "endPage": ref_segs["legislacao-penal-especial/a20/s04"]["endPage"],
        "startTopic": ref_segs["legislacao-penal-especial/a20/s04"].get("startTopic")
      },
      "analytic": """O diploma ambiental conclui seu sistema incriminador tutelando a incolumidade sanitária coletiva contra a poluição perigosa, resguardando o ordenamento urbanístico e o patrimônio cultural urbano, e sancionando condutas violadoras da probidade da administração ambiental desempenhada pelos órgãos do Sisnama.

### Crime de Poluição e Riscos à Incolumidade Coletiva
- **Degradação Tóxica Potencial (art. 54)**: gerar contaminação atmosférica, hídrica ou do solo em patamares graves com aptidão para lesionar a incolumidade sanitária da população ou provocar mortandade na fauna local. Trata-se de crime formal e de perigo comum abstrato ou concreto conforme o grau verificado;
- **Formas Qualificadas e Modalidade Culposa**: o delito admite a modalidade culposa no § 1º (detenção de seis meses a um ano). As penas privativas de liberdade são exasperadas para reclusão de 1 a 5 anos se a poluição tornar uma área imprópria para ocupação humana, causar poluição hídrica que interrompa o abastecimento público de água potável, ou decorrer de lançamento clandestino de efluentes e resíduos industriais perigosos;
- **Resíduos Perigosos (art. 56)**: fabricar, guardar, estocar ou dispensar produtos químicos nocivos à saúde sem observância aos padrões de controle ambiental previstos na regulação legal ou infralegal.

### Ordenamento Urbano, Pichação e Descriminalização do Grafite
- **Pichação de Fachadas e Monumentos (art. 65)**: conspurcar edificações urbanas ou muros com inscrições sem autorização, sujeitando o autor a pena de detenção de 3 meses a um ano e multa. Se o ato for perpetrado contra monumento tombado em virtude de seu valor artístico, arqueológico ou histórico, a pena eleva-se para detenção de seis meses a um ano e multa qualificada;
- **Descriminalização Expressa do Grafite (§ 2º)**: o estatuto expressamente retirou a tipicidade criminal de manifestações visuais de grafite destinadas a embelezar o espaço urbano, exigindo autorização formal do proprietário e harmonia com posturas municipais vigentes.

### Crimes contra a Administração Ambiental
- **Falsidade em Licenciamento (art. 66)**: funcionário público que faz afirmação falsa ou enganosa, omite a verdade, sonega informações ou dados técnico-científicos em procedimentos de autorização, licença ou concessão ambiental;
- **Outorga Administrativa Ilícita (art. 67)**: responsabiliza com detenção o funcionário que concede ato autorizativo ou parecer ambiental vulnerando preceitos legais e regulamentos vigentes;
- **Obstrução à Fiscalização (art. 69)**: criar embaraços ou dificultar a ação fiscalizadora exercida pelos agentes públicos ambientais competentes;
- **Estudo e Laudo Ambiental Falso (art. 69-A)**: elaborar ou apresentar, no processo de licenciamento, concessão ou autorização ambiental, estudo, laudo ou relatório ambiental total ou parcialmente falso ou enganoso, inclusive por omissão, punido severamente com reclusão de 3 a 6 anos e multa.

### Para fixar
- O crime de poluição do art. 54 é punido nas modalidades dolosa e culposa.
- A poluição hídrica que interrompe o abastecimento urbano de água constitui forma qualificada.
- Manusear ou estocar substâncias tóxicas violando regulamentos técnicos é delito do art. 56.
- Pichar patrimônio urbano tombado atrai causa qualificadora específica na Lei de Crimes Ambientais.
- O grafite com viés artístico e prévio consentimento do titular não consubstancia crime.
- A concessão de licença ambiental em desconformidade com a lei por servidor público é crime autônomo.
- Apresentar estudo ambiental falso ou omisso em licenciamento atrai reclusão de 3 a 6 anos.""",
      "synthetic": [
        "**Crime de poluição e formas culposas**: causar poluição danosa à saúde humana ou fauna atrai punição dolosa e modalidade culposa atenuada.",
        "**Qualificadora no abastecimento de água**: a contaminação hídrica que suspenda o abastecimento de água potável urbana qualifica a poluição.",
        "**Substâncias tóxicas clandestinas**: produzir, transportar ou descartar resíduos perigosos sem autorização técnica constitui delito do art. 56.",
        "**Pichação contra patrimônio tombado**: conspurcar edificações urbanas ou monumentos históricos protegidos acarreta sancionamento corporal estrito.",
        "**Descriminalização formal do grafite**: manifestações de grafite artístico autorizadas pelo proprietário não configuram infração penal.",
        "**Emissão ilícita de licença pública**: o servidor que expede autorização ambiental violando a legislação comete crime funcional autônomo.",
        "**Embargos à fiscalização ambiental**: criar obstáculos operacionais aos agentes do Sisnama no exercício fiscalizatório tipifica o art. 69.",
        "**Falsidade em estudos de licenciamento**: apresentar laudos periciais enganosos ou omissos atrai severa pena de reclusão de três a seis anos."
      ]
    }
  ]
}

Path("content/items/legislacao-penal-especial/a20.json").write_text(json.dumps(items_a20, ensure_ascii=False, indent=2), encoding="utf-8")
Path("content/summaries/legislacao-penal-especial/a20.json").write_text(json.dumps(summaries_a20, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved a20 files successfully.")
