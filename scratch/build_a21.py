import json
from pathlib import Path

# AULA 21: Estatuto do Desarmamento (Lei 10.826/2003)

ref_segs = {s["id"]: s for s in json.loads(Path("content/segments/legislacao-penal-especial.json").read_text(encoding="utf-8"))["segments"]}

items_a21 = {
  "aula": "legislacao-penal-especial/a21",
  "batch": "pcpe-bizu-legislacao-penal-especial",
  "status": "DRAFT",
  "stage": "bizu",
  "segments": [
    {
      "id": "legislacao-penal-especial/a21/s01",
      "bizu": {
        "summary": [
          "**Competência do SINARM**: órgão da Polícia Federal responsável por cadastrar e controlar armas civis permitidas em território nacional.",
          "**Divisão com o SIGMA**: o Exército Brasileiro gerencia o SIGMA, controlando armamentos militares, policiais militares e atiradores desportivos.",
          "**Requisitos de aquisição civil**: idade mínima de 25 anos, idoneidade sem antecedentes, capacidade técnica, aptidão psicológica e ocupação lícita.",
          "**Certificado de registro (CRAF)**: autoriza manter o armamento exclusivamente no interior da residência ou na sede do local de trabalho do titular.",
          "**Restrição espacial da posse**: o registro predial não autoriza o proprietário a circular ou transitar com a arma em vias ou logradouros públicos.",
          "**Natureza jurídica do porte**: concessão precária e discricionária da Polícia Federal condicionada à demonstração de risco profissional concreto.",
          "**Comunicação de extravio**: o proprietário deve comunicar furto, roubo ou extravio de arma ou munição à polícia em até vinte e quatro horas.",
          "**Perda de eficácia temporal**: o registro e o porte submetem-se a renovações periódicas obrigatórias sob pena de irregularidade administrativa."
        ],
        "teoria": [
          {
            "statement": "O Certificado de Registro de Arma de Fogo confere ao cidadão autorização automática para transportar o armamento municiado em vias públicas urbanas.",
            "isTrue": False,
            "explanation": "O registro predial (CRAF) autoriza unicamente a posse intramuros no domicílio residencial ou no local de trabalho do responsável legal."
          },
          {
            "statement": "A aquisição de arma de fogo de uso permitido no comércio nacional exige idade mínima de vinte e cinco anos e comprovação de aptidão psicológica.",
            "isTrue": True,
            "explanation": "O art. 4º da Lei 10.826/2003 elenca como requisitos obrigatórios a idade mínima de 25 anos, higidez mental e capacidade técnica de tiro."
          },
          {
            "statement": "O Sistema Nacional de Armas (SINARM) foi instituído no âmbito do Ministério da Defesa para centralizar privativamente o cadastro das Forças Armadas.",
            "isTrue": False,
            "explanation": "O SINARM situa-se no âmbito da Polícia Federal (Ministério da Justiça), cabendo ao SIGMA (Exército) o controle de armas militares."
          },
          {
            "statement": "O responsável legal por estabelecimento comercial pode manter legalmente arma registrada no local onde exerce a gerência da empresa.",
            "isTrue": True,
            "explanation": "O art. 5º, § 5º, estende a posse regular ao local de trabalho, desde que o agente seja o titular ou o encarregado legal do negócio."
          }
        ],
        "revisao": [
          {
            "statement": "A declaração de efetiva necessidade para aquisição de arma de fogo de uso permitido é de apreciação vinculada obrigatória pelo delegado federal.",
            "isTrue": False,
            "explanation": "A análise da efetiva necessidade e da concessão do porte possui feição discricionária pela Polícia Federal conforme critérios de conveniência."
          },
          {
            "statement": "O extravio ou furto de arma de fogo de propriedade particular deve ser formalmente comunicado à polícia judiciária no prazo de vinte e quatro horas.",
            "isTrue": True,
            "explanation": "O art. 13, parágrafo único, impõe o dever de lavrar ocorrência e comunicar as autoridades policiais em até 24 horas da subtração."
          },
          {
            "statement": "A autorização para aquisição de arma de fogo de uso permitido pode ser concedida regularmente a quem responda a inquérito policial por roubo.",
            "isTrue": False,
            "explanation": "O art. 4º, I, exige comprovação de idoneidade mediante certidões negativas de antecedentes criminais e ausência de inquérito ou ação penal."
          },
          {
            "statement": "A licença de porte de arma concedida pela Polícia Federal possui abrangência territorial delimitada e eficácia temporal sujeita a renovação.",
            "isTrue": True,
            "explanation": "O porte tem vigência temporária e âmbito territorial adstrito ao deferido na autorização expedida pela autoridade competente."
          }
        ],
        "pointers": [
          {"topic": "Atribuições do SINARM e diferenciação do SIGMA", "pageRef": 3},
          {"topic": "Requisitos legais para aquisição de arma de fogo", "pageRef": 6},
          {"topic": "Certificado de registro predial e local de trabalho", "pageRef": 9},
          {"topic": "Requisitos e discricionariedade do porte de arma", "pageRef": 12}
        ]
      }
    },
    {
      "id": "legislacao-penal-especial/a21/s02",
      "bizu": {
        "summary": [
          "**Porte funcional em serviço e folga**: policiais federais, civis, militares, penais e bombeiros possuem porte funcional integral por prerrogativa de cargo.",
          "**Porte irrestrito para Guardas Municipais**: o STF declarou inconstitucional a restrição populacional, assegurando porte a todas as guardas municipais.",
          "**Membros da Magistratura e MP**: juízes e promotores possuem prerrogativa funcional de porte garantida em suas respectivas leis orgânicas de regência.",
          "**Caçadores para subsistência**: moradores rurais que dependam do abate para sustento familiar podem obter porte de espingarda de calibre permitido.",
          "**Atestado de capacitação periódica**: servidores com porte funcional submetem-se a avaliações técnicas e psicológicas periódicas institucionais.",
          "**Trânsito de atiradores e caçadores**: CACs dependem de guia de tráfego expedida pelo Comando do Exército para transportar armas aos clubes.",
          "**Anistia na entrega voluntária**: a entrega espontânea de armas à polícia afasta a tipicidade e garante indenização pecuniária governamental.",
          "**Fiscalização da segurança privada**: empresas de vigilância armada respondem administrativamente e penalmente pelo controle de seu arsenal balístico."
        ],
        "teoria": [
          {
            "statement": "O direito ao porte de arma de fogo de integrantes das guardas municipais submete-se a restrição proporcional ao número de habitantes da comarca.",
            "isTrue": False,
            "explanation": "O Pleno do STF (ADI 5948 e ADPF 524) invalidou a trava demográfica, deferindo o porte em serviço e fora dele a todas as guardas municipais."
          },
          {
            "statement": "A entrega voluntária de arma de fogo irregular perante posto credenciado da Polícia Federal opera a extinção da punibilidade e afasta o crime.",
            "isTrue": True,
            "explanation": "A entrega espontânea a qualquer tempo consubstancia causa extintiva ou atipicidade da posse/porte durante o transporte com guia expedida."
          },
          {
            "statement": "O caçador de subsistência residente em zona urbana pode obter porte legal de fuzil semiautomático de grosso calibre para consumo doméstico.",
            "isTrue": False,
            "explanation": "O porte de subsistência é privativo de morador rural maior de 25 anos e restringe-se a arma de tiro simples de calibre permitido (espingarda)."
          },
          {
            "statement": "Integrantes do quadro efetivo da polícia penal possuem porte de arma de fogo funcional inclusive fora do horário de serviço em todo o país.",
            "isTrue": True,
            "explanation": "A legislação assegura porte institucional pleno aos policiais penais em razão da atividade de custódia e vigilância prisional."
          }
        ],
        "revisao": [
          {
            "statement": "O porte funcional de armas de policiais militares e civis depende de prévia autorização remunerada renovada anualmente junto ao SINARM.",
            "isTrue": False,
            "explanation": "O porte funcional decorre de expressa previsão legal corporativa, dispensando pagamento de taxas ou autorização casuística da PF."
          },
          {
            "statement": "Membros das carreiras de auditoria da Receita Federal possuem prerrogativa legal de porte de arma para defesa institucional e pessoal.",
            "isTrue": True,
            "explanation": "O art. 6º, X, estende o porte de arma aos auditores e analistas tributários no desempenho de suas missões fiscalizatórias aduaneiras."
          },
          {
            "statement": "A prática de tiro desportivo em clubes credenciados autoriza o transporte de arma de fogo ostensiva e municiada na cintura em vias públicas.",
            "isTrue": False,
            "explanation": "O transporte de armas de CACs dá-se desmuniciado e acondicionado em estojo, acobertado por estrita guia de tráfego expedida pelo Exército."
          },
          {
            "statement": "O descumprimento dos requisitos técnicos periódicos de tiro pode ensejar a suspensão administrativa do porte funcional do agente público.",
            "isTrue": True,
            "explanation": "As corporações exigem revalidação periódica de aptidão psicológica e tiro sob pena de recolhimento da cautela funcional da arma."
          }
        ],
        "pointers": [
          {"topic": "Porte funcional de carreiras policiais e guardas municipais", "pageRef": 15},
          {"topic": "Porte de subsistência rural e regras para atiradores", "pageRef": 18},
          {"topic": "Entrega voluntária de armas e anistia permanente", "pageRef": 21},
          {"topic": "Regras da segurança privada e deveres de fiscalização", "pageRef": 23}
        ]
      }
    },
    {
      "id": "legislacao-penal-especial/a21/s03",
      "bizu": {
        "summary": [
          "**Posse irregular permitida (art. 12)**: manter arma ou munição permitida dentro de casa ou no trabalho; crime afiançável apenado com detenção.",
          "**Omissão de cautela (art. 13)**: negligenciar cautela facilitando apoderamento de arma por menor de 18 anos ou pessoa com enfermidade mental.",
          "**Disparo de arma (art. 15)**: atirar em via pública ou local habitado; crime subsidiário punido com reclusão de dois a quatro anos e multa.",
          "**Porte ilegal permitido (art. 14)**: circular com arma de uso permitido sem autorização fora do domicílio; crime inafiançável na polícia (reclusão).",
          "**Arma de uso restrito (art. 16)**: portar ou possuir arma de uso restrito sujeita o agente a reclusão de três a seis anos (não hediondo).",
          "**Arma raspada equiparada (§ 1º)**: suprimir numeração ou sinal identificador equipara-se à infração do art. 16 independentemente do calibre originário.",
          "**Arma de uso proibido (§ 2º)**: portar ou possuir arma proibida acarreta reclusão de 4 a 12 anos, constituindo crime hediondo na Lei 8.072/1990.",
          "**Comércio ilegal e tráfico (arts. 17 e 18)**: comércio clandestino e tráfico internacional consubstanciam crimes hediondos punidos com reclusão severa."
        ],
        "teoria": [
          {
            "statement": "O crime de posse ou porte ilegal de arma de fogo de uso restrito comum mantém-se classificado como crime hediondo após a Lei Anticrime.",
            "isTrue": False,
            "explanation": "O Pacote Anticrime (Lei 13.964/2019) restringiu a hediondez exclusivamente às condutas envolvendo arma de fogo de uso proibido (art. 16, § 2º)."
          },
          {
            "statement": "A conduta de portar arma de fogo com numeração de série raspada é equiparada ao porte de uso restrito, ainda que o calibre seja originalmente permitido.",
            "isTrue": True,
            "explanation": "O art. 16, § 1º, I, equipara ao crime de uso restrito qualquer arma com numeração, marca ou sinal de identificação raspado ou adulterado."
          },
          {
            "statement": "O disparo de arma de fogo em via pública é delito de feição primária que prevalece mesmo quando praticado como meio para a consumação de roubo.",
            "isTrue": False,
            "explanation": "O art. 15 consagra delito expressamente subsidiário ('desde que a conduta não tenha por fim outro crime'), restando absorvido pelo roubo."
          },
          {
            "statement": "O comércio ilegal de armas de fogo e o tráfico internacional de armamento consubstanciam crimes hediondos no ordenamento penal brasileiro.",
            "isTrue": True,
            "explanation": "A Lei 8.072/1990 elenca categoricamente os crimes dos arts. 17 e 18 do Estatuto do Desarmamento no rol taxativo de delitos hediondos."
          }
        ],
        "revisao": [
          {
            "statement": "A posse irregular de arma de fogo de uso permitido praticada no interior da residência do agente é sancionada com reclusão inafiançável.",
            "isTrue": False,
            "explanation": "O art. 12 comina pena de detenção de 1 a 3 anos e multa, sendo infração afiançável diretamente pela autoridade policial em sede de flagrante."
          },
          {
            "statement": "A entrega ou fornecimento desautorizado de arma de fogo a criança ou adolescente configura figura equiparada do art. 16 da lei especial.",
            "isTrue": True,
            "explanation": "O art. 16, § 1º, V, equipara expressamente a entrega ou cessão de arma a menor de dezoito anos às penas do porte de uso restrito."
          },
          {
            "statement": "O crime de omissão de cautela do art. 13 pode ser praticado dolosamente mediante ajuste prévio com menor infrator para a prática de homicídio.",
            "isTrue": False,
            "explanation": "A omissão de cautela é crime culposo puro de negligência; havendo adesão intencional, o proprietário responderá em concurso pelo crime-fim."
          },
          {
            "statement": "A pena dos crimes de comércio ilegal e tráfico internacional de armas é aumentada de metade se o autor for reincidente específico.",
            "isTrue": True,
            "explanation": "O art. 20 estabelece que as penas dos arts. 14 a 18 são aumentadas da metade se o agente for reincidente específico em crimes da lei."
          }
        ],
        "pointers": [
          {"topic": "Distinção dogmática entre posse e porte ilegal de arma", "pageRef": 25},
          {"topic": "Omissão de cautela e subsidiariedade do disparo", "pageRef": 28},
          {"topic": "Uso restrito, numeração raspada e hediondez de uso proibido", "pageRef": 32},
          {"topic": "Comércio ilegal, tráfico internacional e majorantes", "pageRef": 36}
        ]
      }
    }
  ]
}

# RESUMOS A21
summaries_a21 = {
  "aula": "legislacao-penal-especial/a21",
  "batch": "pcpe-summary-legislacao-penal-especial",
  "status": "DRAFT",
  "segments": [
    {
      "id": "legislacao-penal-especial/a21/s01",
      "fingerprint": {
        "startPage": ref_segs["legislacao-penal-especial/a21/s01"]["startPage"],
        "endPage": ref_segs["legislacao-penal-especial/a21/s01"]["endPage"],
        "startTopic": ref_segs["legislacao-penal-especial/a21/s01"].get("startTopic")
      },
      "analytic": """A Lei 10.826/2003, denominada Estatuto do Desarmamento, estabeleceu a disciplina jurídica sobre o registro, controle da posse e restrição ao porte de armas de fogo e munições em âmbito nacional. O diploma estruturou uma rígida política de fiscalização armamentista, delineando esferas de atribuição administrativa entre órgãos civis e militares para restringir a circulação clandestina de armamentos no país.

### Sistema Nacional de Armas e Repartição de Atribuições com o SIGMA
O modelo de controle armamentista assenta-se em uma bifurcação orgânica de competências:
- **Atribuições do SINARM (arts. 1º e 2º)**: instituído no âmbito da Polícia Federal e vinculado ao Ministério da Justiça, congrega atribuições de identificação pericial e cadastro geral de armas de fogo produzidas, comercializadas, transferidas ou apreendidas em território brasileiro; cadastra as autorizações de porte e registro emitidas a cidadãos civis, policiais civis, guardas municipais e empresas de segurança privada;
- **Esfera de Atuação do SIGMA**: gerido pelo Comando do Exército sob a égide do Ministério da Defesa, detém competência privativa para autorizar e registrar armamentos bélicos das Forças Armadas, das Polícias Militares e Corpos de Bombeiros Militares, além de supervisionar as atividades de atiradores desportivos, colecionadores e caçadores cadastrados (CACs).

### Requisitos Substanciais para Aquisição Civil de Arma de Fogo
A aquisição de armamento de uso permitido no comércio regular depende de comprovação de pressupostos cumulativos:
- **Idade Mínima de 25 Anos**: exigência de maturidade etária civil, ressalvados os integrantes de carreiras institucionais de segurança pública;
- **Declaração de Efetiva Necessidade**: apresentação de motivos concretos que justifiquem a detenção da arma;
- **Idoneidade Pessoal Comprovada**: juntada de certidões negativas de antecedentes criminais das Justiças Federal, Estadual, Militar e Eleitoral, além da demonstração cabal de ausência de inquérito policial ou ação penal condenatória em andamento;
- **Capacidade Técnica e Psicológica**: aprovação em testes de tiro e laudo conclusivo de aptidão mental emitido por psicólogo credenciado na Polícia Federal;
- **Comprovação de Ocupação Lícita e Domicílio Certo**: demonstração documental de trabalho regular e residência fixa.

### Distinção entre Registro Predial e Autorização de Porte
- **Certificado de Registro de Arma de Fogo (CRAF - art. 5º)**: autorização meramente predial, expedida pela Polícia Federal, que faculta ao titular manter o armamento exclusivamente no interior de sua moradia residencial ou dependências fechadas desta, ou ainda em seu local de trabalho, desde que figure como titular da empresa ou responsável legal pelo estabelecimento;
- **Porte de Arma de Fogo (art. 10)**: autorização excepcionalíssima e precária outorgada pelo Diretor-Geral da Polícia Federal, exigindo demonstração inequívoca de risco profissional ou ameaça concreta à integridade física do postulante.

### Para fixar
- O SINARM funciona no âmbito da Polícia Federal e controla armamentos de uso permitido civis.
- O SIGMA é administrado pelo Exército Brasileiro para gerir arsenais militares e de CACs.
- A aquisição de arma de fogo exige idade mínima de vinte e cinco anos e aptidão psicológica.
- O registro (CRAF) autoriza a guarda da arma exclusivamente em domicílio ou no local de trabalho do titular.
- O porte de arma constitui concessão precária e discricionária outorgada pela Polícia Federal.
- O furto ou extravio de arma particular deve ser comunicado à polícia em até vinte e quatro horas.""",
      "synthetic": [
        "**Gestão dual de armamentos**: o SINARM controla armas de uso permitido civis na Polícia Federal e o SIGMA gerencia armas militares no Exército.",
        "**Idade mínima de 25 anos**: a compra regular de armamento exige maturidade etária, capacidade técnica de tiro e higidez psicológica comprovada.",
        "**Idoneidade sem antecedentes**: o interessado deve comprovar inexistência de inquérito policial ou ação criminal mediante certidões negativas.",
        "**Restrição predial do registro**: o CRAF permite manter a arma apenas dentro da residência ou no trabalho do responsável legal do negócio.",
        "**Caráter excepcional do porte**: a licença de circulação é concessão precária e discricionária outorgada pela autoridade policial federal.",
        "**Dever de comunicação de extravio**: o furto ou desvio de arma de fogo deve ser registrado formalmente na polícia judiciária em 24 horas.",
        "**Declaração de efetiva necessidade**: o comprador deve expor fatos concretos que demonstrem a utilidade de possuir arma em domicílio.",
        "**Eficácia temporal delimitada**: autorizações de registro e porte sujeitam-se a revalidação periódica de habilitação e tiro sob fiscalização."
      ]
    },
    {
      "id": "legislacao-penal-especial/a21/s02",
      "fingerprint": {
        "startPage": ref_segs["legislacao-penal-especial/a21/s02"]["startPage"],
        "endPage": ref_segs["legislacao-penal-especial/a21/s02"]["endPage"],
        "startTopic": ref_segs["legislacao-penal-especial/a21/s02"].get("startTopic")
      },
      "analytic": """O Estatuto do Desarmamento estabeleceu prerrogativas institucionais para o exercício do porte funcional de armas de fogo, conferindo autorização legal direta a corporações policiais e carreiras estatais encarregadas da preservação da ordem pública e da soberania nacional, além de disciplinar o porte de subsistência e a entrega espontânea de armamentos.

### Rol de Agentes com Porte de Arma Funcional
O art. 6º da Lei 10.826/2003 elenca taxativamente as categorias profissionais detentoras de porte por prerrogativa funcional do cargo:
- **Integrantes das Forças Armadas**: membros da Marinha, Exército e Aeronáutica;
- **Órgãos de Segurança Pública Constitucionais (art. 144 da CF)**: integrantes da Polícia Federal, Polícia Rodoviária Federal, Polícia Ferroviária Federal, Polícias Civis, Polícias Militares, Corpos de Bombeiros Militares e Polícias Penais distrital, estaduais e federal, possuindo porte funcional com validade nacional mesmo fora do serviço;
- **Guardas Municipais e Pacificação pelo STF**: o legislador originário tentou graduar o porte das guardas conforme a densidade populacional do município. Contudo, o Plenário do Supremo Tribunal Federal (julgamento conjunto das ADIs 5948, 5538 e ADPF 524) **declarou inconstitucionais todas as travas demográficas**, reconhecendo que **todos os integrantes das Guardas Municipais do país têm direito ao porte de arma de fogo**, em serviço operacional e fora dele;
- **Outras Categorias Autorizadas**: agentes da Agência Brasileira de Inteligência (ABIN), agentes do Gabinete de Segurança Institucional (GSI), auditores-fiscais e analistas da Receita Federal e da Auditoria Fiscal do Trabalho.

### Porte de Subsistência e Trânsito de Desportistas
- **Porte de Subsistência Rural (art. 6º, § 5º)**: outorga especial concedida a moradores rurais maiores de 25 anos que comprovem depender do emprego de arma de fogo para prover a alimentação de sua família, restrito a uma espingarda de alma lisa de calibre permitido;
- **Caçadores, Atiradores e Colecionadores (CACs)**: o deslocamento de armamento de tiro desportivo e coleção submete-se à estrita expedição de guia de tráfego pelo Comando do Exército, devendo a arma ser transportada desmuniciada em estojo ou embalagem de resguardo.

### Política de Desarmamento e Entrega Espontânea de Armas
Os arts. 31 e 32 consagraram uma política permanente de anistia indenizada. Qualquer cidadão que possua arma irregular, com registro vencido ou sem origem documentada, pode entregá-la espontaneamente nos postos credenciados da Polícia Federal. A legislação assegura sigilo absoluto ao entregador, indenização financeira fixada em tabela ministerial e atipicidade penal absoluta do transporte do artefato, desde que acobertado por prévia guia de trânsito retirada via internet.

### Para fixar
- Policiais civis, militares, federais e penais possuem porte de arma funcional em serviço e folga.
- O STF julgou inconstitucional o critério populacional, garantindo porte a todas as guardas municipais.
- Integrantes da Receita Federal e do Trabalho possuem porte funcional para missões fiscalizatórias.
- O porte de subsistência é reservado a residentes rurais que dependem da caça para alimentar a família.
- Atiradores desportivos e CACs devem transportar armas desmuniciadas sob guia de tráfego do Exército.
- A entrega voluntária de arma de fogo perante a autoridade afasta o crime e confere indenização estatal.""",
      "synthetic": [
        "**Porte institucional corporativo**: integrantes das polícias federal, civis, militares e penais possuem porte em serviço e durante a folga.",
        "**Isomia para guardas municipais**: a Suprema Corte baniu as limitações populacionais, estendendo porte a todas as guardas municipais.",
        "**Porte rural de subsistência**: assegura porte de espingarda de alma lisa a morador do campo que necessite caçar para sustento doméstico.",
        "**Regramento estrito para CACs**: armas esportivas transitam obrigatoriamente desmuniciadas em recipientes protegidos sob guia do Exército.",
        "**Prerrogativa funcional tributária**: auditores e analistas da Receita Federal exercem porte funcional de defesa pessoal e fiscalizatória.",
        "**Anistia na entrega espontânea**: entregar armas nos postos federais extingue responsabilidade criminal e garante indenização pecuniária.",
        "**Fiscalização de segurança privada**: empresas de vigilância respondem diretamente pela guarda e acervo de armas de fogo utilizadas.",
        "**Capacitação psicológica periódica**: a manutenção do porte funcional exige avaliações técnicas e psicológicas institucionais contínuas."
      ]
    },
    {
      "id": "legislacao-penal-especial/a21/s03",
      "fingerprint": {
        "startPage": ref_segs["legislacao-penal-especial/a21/s03"]["startPage"],
        "endPage": ref_segs["legislacao-penal-especial/a21/s03"]["endPage"],
        "startTopic": ref_segs["legislacao-penal-especial/a21/s03"].get("startTopic")
      },
      "analytic": """O capítulo incriminador da Lei 10.826/2003 tutela a incolumidade pública contra a circulação, comércio e guarda desautorizada de armas, acessórios e munições, escalonando as sanções criminais de acordo com o potencial lesivo do artefato e a gravidade social da conduta, com reflexos diretos na Lei de Crimes Hediondos.

### Posse Irregular e Porte Ilegal de Arma de Fogo de Uso Permitido
- **Posse Irregular de Uso Permitido (art. 12)**: manter sob guarda arma, acessório ou munição de calibre permitido no interior da residência ou dependência desta, ou no local de trabalho do responsável legal, sem autorização ou com registro vencido. Trata-se de infração de perigo abstrato punida com **detenção de um a três anos e multa**, permitindo fiança diretamente na delegacia;
- **Porte Ilegal de Uso Permitido (art. 14)**: portar, transportar, ter em depósito ou circular com arma, acessório ou munição permitida fora dos limites residenciais ou funcionais sem autorização. Delito formal punido com **reclusão de dois a quatro anos e multa**, cuja fiança sujeita-se à esfera judicial;
- **Omissão de Cautela (art. 13)**: deixar de observar cautelas necessárias para impedir que menor de 18 anos ou pessoa portadora de deficiência mental se apodere de arma de fogo sob sua posse (detenção de 1 a 2 anos e multa).

### Disparo em Via Pública e Subsidiariedade Expressa
O art. 15 incrimina disparar arma de fogo ou detonar munição em lugar habitado, nas suas adjacências, em via pública ou em direção a ela, cominando pena de **reclusão de 2 a 4 anos e multa**. O tipo expressamente encerra cláusula de subsidiariedade expressa (*desde que a conduta não tenha por finalidade a prática de outro crime*), sendo absorvido se configurar crime-meio para homicídio, lesão corporal, roubo ou ameaça.

### Armas de Uso Restrito, Raspadas e Hediondez de Uso Proibido
- **Uso Restrito Comum (art. 16, caput)**: possuir ou portar arma de uso restrito atrai **reclusão de três a seis anos e multa**. A Lei 13.964/2019 (Pacote Anticrime) **retirou a natureza hedionda do porte de arma de uso restrito comum**;
- **Armas com Numeração Raspada (art. 16, § 1º, I)**: raspar, suprimir ou adulterar sinal de identificação ou numeração de série equipara a conduta às penas do art. 16, independentemente de a arma ser de calibre originalmente permitido;
- **Arma de Fogo de Uso Proibido (art. 16, § 2º)**: portar ou possuir arma, acessório ou munição de uso proibido (como armas dissimuladas ou bélicas) atrai severa pena de **reclusão de 4 a 12 anos**. Essa conduta específica é **expressamente catalogada como crime hediondo** na Lei 8.072/1990.

### Comércio Clandestino, Tráfico Internacional e Majorantes
- **Comércio Ilegal de Arma de Fogo (art. 17)**: comercializar clandestinamente armas, acessórios ou munições em atividade industrial ou comercial ilícita, com pena de **reclusão de 6 a 12 anos e multa**, qualificado como **crime hediondo**;
- **Tráfico Internacional de Arma de Fogo (art. 18)**: importar ou exportar armamento, acessórios ou munição transpondo fronteiras sem autorização, punido com **reclusão de 8 a 16 anos e multa**, igualmente dotado de **natureza hedionda**;
- **Causas Especiais de Exasperação de Pena (arts. 19 e 20)**: aumento de metade nas penas se a infração for praticada por integrante de forças policiais, guardas armadas ou empresas de segurança privada, ou se o agente for reincidente específico em crimes da lei.

### Para fixar
- A posse irregular do art. 12 ocorre no interior da residência ou trabalho, punida com detenção.
- O porte ilegal do art. 14 perfaz-se fora do ambiente domiciliar, punido com reclusão de 2 a 4 anos.
- O disparo de arma de fogo é delito expressamente subsidiário punido com reclusão de 2 a 4 anos.
- A arma com numeração de série raspada equipara-se à arma de uso restrito em qualquer hipótese.
- O porte ou posse de arma de fogo de uso proibido é crime hediondo na Lei 8.072/1990.
- O comércio ilegal e o tráfico internacional de armas são crimes hediondos punidos com penas gravosas.
- As penas sofrem aumento da metade se cometidas por servidores da segurança pública ou reincidentes específicos.""",
      "synthetic": [
        "**Dicotomia entre posse e porte**: a posse irregular tutela o ambiente domiciliar ou comercial, enquanto o porte ilegal reprime a circulação externa.",
        "**Subsidiariedade expressa no disparo**: o art. 15 criminaliza tiros em vias públicas desde que a conduta não consubstancie crime-meio para outro delito.",
        "**Equiparação da numeração raspada**: adulterar marcas identificadoras sujeita o agente às penas do art. 16 mesmo em armamento de uso permitido.",
        "**Hediondez restrita ao uso proibido**: o Pacote Anticrime manteve o caráter hediondo exclusivamente para armas, acessórios e munições de uso proibido.",
        "**Comércio clandestino hediondo**: a comercialização ilegal de armamentos atrai reclusão de seis a doze anos e tratamento penitenciário hediondo.",
        "**Tráfico transfronteiriço gravíssimo**: a importação não autorizada de armas de fogo transpondo limites territoriais tipifica o art. 18 da lei.",
        "**Negligência na omissão de cautela**: omitir-se e permitir acesso de menores a armas é crime culposo específico do proprietário do artefato.",
        "**Causa de aumento funcional**: cometer delitos da lei especial prevalecendo-se da condição de policial ou agente de segurança eleva a pena pela metade."
      ]
    }
  ]
}

Path("content/items/legislacao-penal-especial/a21.json").write_text(json.dumps(items_a21, ensure_ascii=False, indent=2), encoding="utf-8")
Path("content/summaries/legislacao-penal-especial/a21.json").write_text(json.dumps(summaries_a21, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved a21 files successfully.")
