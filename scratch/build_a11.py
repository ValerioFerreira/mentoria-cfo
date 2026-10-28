import json
import subprocess
from pathlib import Path

# AULA 11: Lei 8.072/1990 (Crimes Hediondos)

items_a11 = {
  "aula": "legislacao-penal-especial/a11",
  "batch": "pcpe-bizu-legislacao-penal-especial",
  "status": "DRAFT",
  "stage": "bizu",
  "segments": [
    {
      "id": "legislacao-penal-especial/a11/s01",
      "bizu": {
        "summary": [
          "**Natureza jurídica**: a classificação de um delito como hediondo traduz escolha estritamente política do legislador ordinário, configurando reprovação estatal exacerbada.",
          "**Sistema de definição**: o ordenamento pátrio adotou o modelo legal ou de rotulação, restringindo a hediondez aos tipos taxativamente descritos na lei.",
          "**Crimes equiparados**: a Carta Magna conferiu aos delitos de tortura, narcotráfico e terrorismo o mesmo patamar restritivo dispensado aos hediondos genuínos.",
          "**Vedação constitucional**: veda-se a concessão de fiança, anistia ou graça aos crimes hediondos e assemelhados, estendendo a proibição ao indulto por força de lei ordinária.",
          "**Liberdade provisória**: a jurisprudência consolidou a viabilidade de conceder soltura cautelar sem pagamento de fiança quando ausentes os motivos de cautelaridade.",
          "**Formas de consumação**: a tipificação da hediondez abrange indistintamente os delitos consumados e os tentados, sem abrandamento por essa causa.",
          "**Crimes castrenses**: após inovação normativa, os crimes do Código Penal Militar que guardem identidade material com os tipos hediondos civis passaram a integrar a rotulação.",
          "**Responsabilidade penal**: os mandantes, os executores materiais e aqueles que, tendo dever jurídico de agir para impedi-los, se omitirem respondem pelos crimes hediondos e equiparados."
        ],
        "teoria": [
          {
            "statement": "O sistema jurídico brasileiro acolheu o critério judicial para a caracterização dos crimes hediondos, permitindo que o magistrado avalie a repugnância concreta do fato no julgamento.",
            "isTrue": False,
            "explanation": "O Brasil adotou expressamente o critério legal (ou de etiquetamento), no qual apenas as condutas taxativamente listadas pelo legislador recebem o rótulo de crime hediondo."
          },
          {
            "statement": "O texto constitucional estabelece que o terrorismo, a tortura e o tráfico ilícito de entorpecentes recebem tratamento assemelhado aos delitos hediondos quanto à inafiançabilidade.",
            "isTrue": True,
            "explanation": "Conforme o art. 5º, XLIII, da CF/88, tais delitos equiparados a hediondos são formalmente inafiançáveis e insuscetíveis de graça ou anistia."
          },
          {
            "statement": "A concessão de liberdade provisória com arbitramento de fiança permanece admitida para quem comete crime hediondo, desde que haja fundamentação idônea do juiz.",
            "isTrue": False,
            "explanation": "A concessão de fiança é vedação expressa constitucional; admite-se apenas liberdade provisória sem fiança quando ausentes os pressupostos da custódia preventiva."
          },
          {
            "statement": "A prática de tentativa de crime catalogado no rol da Lei 8.072/1990 submete o agente às mesmas vedações processuais e materiais da infração consumada.",
            "isTrue": True,
            "explanation": "O art. 1º da Lei 8.072/1990 afirma com clareza que são hediondos os crimes catalogados tanto na forma consumada quanto na tentada."
          }
        ],
        "revisao": [
          {
            "statement": "O indulto coletivo outorgado pelo Chefe do Poder Executivo pode beneficiar autores de crimes hediondos por ausência de proibição na redação literal da Constituição.",
            "isTrue": False,
            "explanation": "Ainda que a CF mencione anistia e graça, a jurisprudência do STF e o art. 2º, I, da Lei 8.072/1990 vedam expressamente a concessão de indulto a condenados por crime hediondo."
          },
          {
            "statement": "Os crimes militares que apresentem correspondência típica com as hipóteses descritas no rol de crimes hediondos da legislação comum também assumem natureza hedionda.",
            "isTrue": True,
            "explanation": "Com a reforma legislativa introduzida pela Lei 14.688/2023, os delitos castrenses correlatos ao rol passaram formalmente a ter tratamento de crimes hediondos."
          },
          {
            "statement": "Por expressa determinação da Lei de Crimes Hediondos, a prisão preventiva do agente deve ser decretada de maneira automática pelo simples enquadramento no rol legal.",
            "isTrue": False,
            "explanation": "A prisão preventiva jamais é automática, dependendo obrigatoriamente de demonstração fundamentada do periculum libertatis e dos requisitos do art. 312 do CPP."
          },
          {
            "statement": "A responsabilidade penal pelos crimes hediondos abrange tanto mandantes e executores materiais quanto os partícipes omitentes que possuíam o dever legal de obstar o resultado.",
            "isTrue": True,
            "explanation": "Essa é a exata determinação expressa no texto constitucional (art. 5º, XLIII) e repetida no tratamento penal dos delitos hediondos e equiparados."
          }
        ],
        "pointers": [
          {"topic": "Fundamento constitucional e crimes assemelhados", "pageRef": 3},
          {"topic": "Vedações a anistia, graça, indulto e fiança", "pageRef": 4},
          {"topic": "Sistema legal taxativo de tipificação", "pageRef": 5},
          {"topic": "Inclusão de crimes militares correlatos", "pageRef": 7}
        ]
      }
    },
    {
      "id": "legislacao-penal-especial/a11/s02",
      "bizu": {
        "summary": [
          "**Homicídio qualificado**: qualquer hipótese de homicídio qualificado é hedionda, assim como o praticado em atividade típica de grupo de extermínio mesmo por um único indivíduo.",
          "**Homicídio funcional**: atinge membros das forças de segurança, integrantes prisionais, magistrados, membros do MP, defensores e oficiais de justiça em razão do cargo ou seus parentes consanguíneos até terceiro grau.",
          "**Feminicídio e vicaricídio**: com a evolução legislativa, o feminicídio figura como figura autônoma e hedionda, bem como o assassinato de filhos ou dependentes para infligir dor à mãe.",
          "**Violência patrimonial qualificada**: o roubo é hediondo quando houver restrição de liberdade da vítima, uso de arma de fogo comum, restrita ou proibida, lesão grave ou morte.",
          "**Arma branca no roubo**: o emprego exclusivo de faca ou punhal majora a reprimenda do roubo no Código Penal, porém não confere caráter hediondo à conduta.",
          "**Extorsão e sequestro**: tanto a extorsão qualificada pela privação de liberdade ou resultados gravosos quanto a extorsão mediante sequestro em qualquer modalidade integram a lista.",
          "**Violência sexual**: o estupro e o estupro de vulnerável são integralmente hediondos, sem distinção entre formas básicas ou qualificadas por lesão ou óbito.",
          "**Saúde pública**: enquadra-se como hedionda a epidemia com resultado morte e a adulteração ou falsificação de substâncias terapêuticas e medicamentosas.",
          "**Estatuto do Desarmamento**: apenas o porte e posse de armamento de uso proibido permanecem hediondos no art. 16, ao lado do comércio ilegal e do tráfico internacional de armas.",
          "**Furto com explosivos**: o furto qualificado pela utilização de artefato explosivo ou análogo que ocasione perigo comum ostenta natureza hedionda.",
          "**Organizações criminosas**: a formação de quadrilha ou organização voltada especificamente à consecução de delitos hediondos ou equiparados assume o mesmo status gravoso."
        ],
        "teoria": [
          {
            "statement": "O roubo circunstanciado pelo uso de arma branca ostenta a condição de crime hediondo após as modificações trazidas pelo Pacote Anticrime.",
            "isTrue": False,
            "explanation": "O legislador incluiu no rol hediondo apenas o roubo praticado com arma de fogo (seja de uso permitido, restrito ou proibido), excluindo a arma branca da hediondez."
          },
          {
            "statement": "O homicídio praticado em contexto de atividade de grupo de extermínio é classificado como crime hediondo ainda que tenha sido executado por apenas um único indivíduo.",
            "isTrue": True,
            "explanation": "O art. 1º, I, da Lei 8.072/1990 consigna que o homicídio simples em atividade de grupo de extermínio é hediondo mesmo praticado por um só agente."
          },
          {
            "statement": "A posse ou o porte irregular de arma de fogo de uso restrito configura crime hediondo em qualquer situação com base nas regras vigentes.",
            "isTrue": False,
            "explanation": "Apenas as armas de fogo de uso proibido (art. 16, § 2º, da Lei 10.826/2003) geram crime hediondo no porte ou posse; o armamento restrito deixou de ser hediondo nessa hipótese."
          },
          {
            "statement": "O delito de latrocínio, estruturado como roubo qualificado pelo resultado morte, preserva natureza hedionda tanto em sua execução consumada quanto tentada.",
            "isTrue": True,
            "explanation": "O art. 1º, II, 'c', da Lei 8.072/1990 rotula o roubo qualificado por morte ou lesão corporal grave como crime hediondo, abarcando consumação e tentativa."
          }
        ],
        "revisao": [
          {
            "statement": "O crime de furto qualificado mediante destruição ou rompimento de obstáculo com uso de chave falsa é catalogado como crime hediondo pela lei especial.",
            "isTrue": False,
            "explanation": "Apenas a subtração qualificada mediante uso de detonantes ou artefato detonador que gere perigo comum (art. 155, § 4º-A) possui classificação de hedionda."
          },
          {
            "statement": "A adulteração e a falsificação de produtos voltados a fins terapêuticos ou medicinais constituem delitos hediondos previstos taxativamente no rol legal.",
            "isTrue": True,
            "explanation": "O art. 273 e suas modalidades qualificadas figuram no art. 1º, VII-B, da Lei de Crimes Hediondos desde a inclusão promovida pela Lei 9.695/1998."
          },
          {
            "statement": "A extorsão mediante sequestro simples não é hedionda, reservando-se tal chancela somente aos casos em que sobrevenha lesão grave ou óbito do ofendido.",
            "isTrue": False,
            "explanation": "A extorsão mediante sequestro é hedionda em todas as suas vertentes, incluindo a modalidade simples do caput do art. 159 e suas formas qualificadas."
          },
          {
            "statement": "A lesão corporal gravíssima funcional praticada contra bombeiro militar no exercício funcional é delito hediondo e se estende a seus parentes consanguíneos até terceiro grau.",
            "isTrue": True,
            "explanation": "Conforme o art. 1º, I-A, da Lei 8.072/1990, os integrantes das forças do art. 144 da CF e seus consanguíneos até 3º grau são protegidos pela hediondez funcional."
          }
        ],
        "pointers": [
          {"topic": "Homicídio funcional e grupo de extermínio", "pageRef": 9},
          {"topic": "Violência patrimonial: roubo e furto hediondo", "pageRef": 13},
          {"topic": "Crimes contra a dignidade sexual", "pageRef": 17},
          {"topic": "Estatuto do desarmamento e armas proibidas", "pageRef": 21}
        ]
      }
    },
    {
      "id": "legislacao-penal-especial/a11/s03",
      "bizu": {
        "summary": [
          "**Infância e adolescência**: o rol hediondo abrange condutas do ECA que envolvem produção, direção, registro, venda, distribuição ou posse de material de violência sexual infantojuvenil.",
          "**Prisão temporária elastecida**: nos crimes hediondos e equiparados, o lapso temporal da custódia temporária é de 30 dias, admitindo prorrogação idêntica sob extrema necessidade.",
          "**Progressão na LEP**: o Pacote Anticrime instituiu percentuais progressivos: 40% para primário sem óbito, 50% para primário com óbito ou chefia de organização, 60% para reincidente sem óbito e 70% para reincidente com óbito.",
          "**Vedações no livramento**: veda-se peremptoriamente o livramento condicional a crimes hediondos ou equiparados quando resultar morte da vítima.",
          "**Requisitos do livramento**: nos demais crimes hediondos sem resultado fatal, o livramento reclama cumprimento de mais de dois terços da pena e ausência de reincidência específica na mesma espécie delitiva.",
          "**Colaboração premiada**: o colaborador voluntário coautor ou partícipe de crime hediondo que forneça informes eficazes ao desmonte da associação criminosa faz jus à minoração penal de um a dois terços.",
          "**Independência de benefícios**: a delação em crimes hediondos não opera de modo automático, reclamando validação judicial quanto à utilidade das revelações colhidas.",
          "**Regime prisional inicial**: a exigência legal de cumprimento inicial em regime integralmente fechado foi afastada pelo Supremo Tribunal Federal, mantendo-se a análise casuística do art. 33 do CP."
        ],
        "teoria": [
          {
            "statement": "O prazo da prisão temporária para os delitos hediondos e equiparados corresponde a 15 dias, prorrogável uma única vez por igual intervalo comprovado.",
            "isTrue": False,
            "explanation": "O prazo legal da prisão temporária na Lei 8.072/1990 é de 30 dias, admitindo prorrogação por igual período de 30 dias em caso de extrema e comprovada necessidade."
          },
          {
            "statement": "O condenado por crime hediondo com resultado morte não poderá obter o benefício do livramento condicional em nenhuma fase da execução penal.",
            "isTrue": True,
            "explanation": "A reforma do Pacote Anticrime introduziu expressamente no art. 83 do CP a proibição absoluta de livramento condicional aos crimes hediondos que causem morte."
          },
          {
            "statement": "O apenado primário condenado por crime hediondo sem resultado morte necessita cumprir 50% da reprimenda privativa de liberdade para progredir de regime.",
            "isTrue": False,
            "explanation": "Para o sentenciado primário em crime hediondo ou equiparado sem resultado morte, o percentual exigido pelo art. 112 da LEP é de 40%."
          },
          {
            "statement": "A colaboração premiada do partícipe que viabilize o desmantelamento de quadrilha voltada a crimes hediondos possibilita a diminuição de pena de um a dois terços.",
            "isTrue": True,
            "explanation": "Trata-se da benesse expressa no parágrafo único do art. 8º da Lei 8.072/1990 para a denúncia eficaz que facilite a libertação de sequestrado ou dissolução do bando."
          }
        ],
        "revisao": [
          {
            "statement": "A regra que determinava o cumprimento obrigatório da pena dos crimes hediondos em regime integralmente fechado permanece hígida perante os tribunais superiores.",
            "isTrue": False,
            "explanation": "O Plenário do STF julgou inconstitucional a fixação do regime integralmente fechado por ofensa ao princípio constitucional da individualização da pena."
          },
          {
            "statement": "O agente reincidente genérico que comete delito hediondo com resultado morte terá sua progressão de regime condicionada ao cumprimento de 70% da sanção corporal.",
            "isTrue": True,
            "explanation": "O art. 112, VIII, da LEP fixa o patamar de 70% para o apenado reincidente em crime hediondo ou equiparado com resultado morte, não exigindo reincidência específica."
          },
          {
            "statement": "A simples posse ou o armazenamento de mídia contendo registro de violência sexual infantil não é considerada infração hedionda pelo ordenamento pátrio.",
            "isTrue": False,
            "explanation": "Com as atualizações legais que harmonizaram o ECA e a Lei 8.072/1990, a posse e o armazenamento de pornografia infantil (art. 241-B) foram alçados à hediondez."
          },
          {
            "statement": "Para a concessão de livramento condicional em crimes hediondos sem morte, exige-se o desconto de mais de dois terços da pena e que o réu não seja reincidente específico.",
            "isTrue": True,
            "explanation": "O art. 83, V, do Código Penal impõe o cumprimento de mais de dois terços e veda o benefício caso o condenado ostente reincidência específica em hediondos."
          }
        ],
        "pointers": [
          {"topic": "Proteção infantojuvenil e crimes no ECA", "pageRef": 24},
          {"topic": "Prisão temporária e prazos especiais", "pageRef": 28},
          {"topic": "Execução penal e frações de progressão", "pageRef": 30},
          {"topic": "Livramento condicional e delação premiada", "pageRef": 33}
        ]
      }
    }
  ]
}

# RESUMOS A11
summaries_a11 = {
  "aula": "legislacao-penal-especial/a11",
  "batch": "pcpe-summary-legislacao-penal-especial",
  "status": "DRAFT",
  "segments": [
    {
      "id": "legislacao-penal-especial/a11/s01",
      "fingerprint": {
        "startPage": 3,
        "endPage": 8,
        "startTopic": "Lei nº 8.072/1990 — Disposições Gerais e Conceito de Hediondez"
      },
      "analytic": """A Lei 8.072/1990 instrumentalizou o mandado de criminalização insculpido no art. 5º, XLIII, da Constituição da República de 1988, instituindo um estatuto processual e material mais severo para infrações que despertam intensa repulsa na coletividade.

### Critério Legal de Fixação da Hediondez
Doutrinariamente, existem três modelos para definir quais infrações assumem a roupagem de hediondas:
1. **Critério Judicial**: outorga ao julgador a prerrogativa de definir, no caso concreto, se a gravidade real do fato merece tratamento hediondo;
2. **Critério Constitucional ou Administrativo**: atribui a instâncias diretivas a eleição de parâmetros genéricos de reprovabilidade;
3. **Critério Legal (ou de Rotulação)**: foi o expressamente adotado no ordenamento brasileiro. Somente os crimes catalogados taxativamente pelo legislador ordinário na Lei 8.072/1990 recebem a nota de hediondez, sendo irrelevante o grau de crueldade de condutas não tipificadas no rol.

> ⚖️ Base normativa: O rol do art. 1º da Lei 8.072/1990 possui natureza taxativa (*numerus clausus*), repelindo qualquer integração por analogia prejudicial ao réu.

### Delitos Hediondos e Infrações Equiparadas
A Carta da República distinguiu formalmente duas categorias de ilícitos sujeitos à disciplina rigorosa:
- **Crimes Hediondos em Sentido Estrito**: são aqueles positivados no corpo da Lei 8.072/1990, abrangendo tipos do Código Penal e de legislações extravagantes;
- **Crimes Equiparados (ou Assemelhados)**: a tríade formada pela **Tortura**, pelo **Tráfico Ilícito de Drogas** e pelo **Terrorismo** (conhecida pelo mnemônico TTT). Esses delitos não compõem a lista hedionda em si, mas recebem tratamento jurídico idêntico por ordem direta do poder constituinte.

Ambas as categorias incidem sobre os sujeitos em qualquer etapa do iter criminis:
- **Consumação e Tentativa**: a lei expressamente disciplina que o crime tentado conserva a mesma qualidade hedionda daquele que atinge a consumação;
- **Concurso de Pessoas**: respondem com rigor paritário os mandantes, os executores materiais e as pessoas que, dispondo de capacidade jurídica e dever para obstar a infração, quedaram-se voluntariamente omissas.

### Efeitos Constitucionais e Vedações Legais
A submissão de uma infração ao regime da Lei 8.072/1990 desencadeia restrições substantivas imediatas:
- **Inafiançabilidade**: não se admite o pagamento de caução pecuniária em sede policial ou judicial para a recuperação da liberdade;
- **Insuscetibilidade de Graça, Anistia e Indulto**: a Constituição veda expressamente anistia (competência do Congresso) e graça (clemência individual presidencial). O art. 2º da Lei 8.072/1990 agregou a vedação ao indulto coletivo, disposição reputada plenamente constitucional pelos tribunais de cúpula;
- **Admissibilidade de Liberdade Provisória**: a proibição originária de soltura provisória foi revogada, alinhando a legislação à garantia do art. 5º, LXVI, da CF. O acusado pode responder ao processo em liberdade se não estiverem presentes os vetores autorizadores da segregação cautelar preventiva;
- **Inclusão Castrense**: reformas normativas contemporâneas integraram os crimes descritos no Código Penal Militar que guardem simetria com as infrações catalogadas na lei comum, suprimindo antiga lacuna de punibilidade;
- **Novas figuras e marco legal**: atualizações legislativas adicionaram condutas de domínio social estruturado de organizações criminosas e tutela severa contra violações graves.

### Para fixar
- O Brasil acolheu o critério legal taxativo, não admitindo analogia para rotular condutas fora da lista normativa.
- Os delitos de tortura, tráfico de drogas e terrorismo compõem os crimes equiparados a hediondos.
- A vedação à fiança, graça, anistia e indulto atinge tanto as condutas consumadas quanto as tentadas.
- Mandantes, executores materiais e partícipes omitentes que deveriam impedir o fato sofrem o mesmo tratamento.
- Admite-se a liberdade provisória desprovida de fiança quando ausentes os pressupostos da custódia preventiva.
- Delitos militares que possuam espelho típico no rol da Lei 8.072/1990 assumem expressamente a natureza hedionda.""",
      "synthetic": [
        "**Critério de definição**: o Brasil adotou o sistema legal taxativo, no qual apenas condutas tipificadas na norma são hediondas.",
        "**Tríade equiparada**: tortura, tráfico de entorpecentes e terrorismo recebem idêntico rigor repressivo por ordem constitucional.",
        "**Extensão aos tentados**: a classificação hedionda atinge tanto os crimes integralmente consumados quanto as formas tentadas.",
        "**Impedimentos de clemência**: veda-se terminantemente a concessão de fiança, anistia legislativa, graça individual e indulto coletivo.",
        "**Viabilidade de soltura**: é cabível a concessão de liberdade provisória sem fiança se ausentes os requisitos da preventiva.",
        "**Alcance dos sujeitos**: submetem-se ao regime agravado os autores executores, os mandantes e os garantidores omitentes.",
        "**Repercussão militar**: infrações militares idênticas em conteúdo material aos crimes da lei comum tornaram-se legalmente hediondas."
      ]
    },
    {
      "id": "legislacao-penal-especial/a11/s02",
      "fingerprint": {
        "startPage": 9,
        "endPage": 23,
        "startTopic": "Rol dos Crimes Hediondos no Código Penal e Leis Especiais"
      },
      "analytic": """O catálogo de crimes hediondos congrega violações extremas à vida, integridade corporal, patrimônio, dignidade sexual e segurança pública. A compreensão de cada hipótese exige rigor na identificação das circunstâncias elementares do art. 121, art. 129 e dispositivos especiais.

### Crimes Contra a Vida e a Integridade Corporal
No âmbito do homicídio e das agressões físicas, a hediondez não recai sobre todas as condutas, dependendo de qualificadoras expressas:
- **Homicídio Simples em Grupo de Extermínio**: o homicídio simples apenas é hediondo quando praticado em atividade típica de grupo de extermínio, incidindo a hediondez ainda que o crime seja perpetrado por um único executor;
- **Homicídio Qualificado**: todas as qualificadoras do art. 121, § 2º, atraem a hediondez (motivo fútil, torpe mediante paga ou promessa, veneno, fogo, asfixia, emboscada, traição, conexão para assegurar impunidade, contra menor de catorze anos ou em instituições educacionais);
- **Homicídio Funcional**: praticado contra autoridades e membros das Forças Armadas, segurança pública, sistema penitenciário, Força Nacional, magistratura, Ministério Público, Defensoria, Advocacia Pública e oficiais de justiça, estendendo-se ao cônjuge, companheiro ou parente até terceiro grau por consanguinidade;
- **Feminicídio e Vicaricídio**: tipificados nos arts. 121-A e 121-B do Código Penal, preservam natureza hedionda pela deliberada motivação de gênero ou intenção de atingir a mulher pela violência contra seus filhos;
- **Lesão Corporal Gravíssima e Morte Funcional**: a hediondez alcança a lesão gravíssima (art. 129, § 2º) e a lesão seguida de morte (art. 129, § 3º) cometidas em desfavor das autoridades mencionadas ou em escolas.

### Crimes Contra o Patrimônio
A proteção do patrimônio pela Lei 8.072/1990 concentra-se nos delitos perpetrados com violência expressiva ou risco coletivo:
- **Roubo Hediondo**: nem todo roubo qualificado ou circunstanciado é hediondo. A hediondez incide restritamente em três situações:
  1. Circunstanciado pela privação ou restrição da liberdade da vítima (art. 157, § 2º, V);
  2. Circunstanciado pelo uso de artefato bélico disparador (art. 157, §§ 2º-A, I e 2º-B). O roubo cometido com arma branca (faca) não integra a lista;
  3. Qualificado pelo resultado lesão corporal grave ou morte (latrocínio, art. 157, § 3º).
- **Extorsão Qualificada**: enquadra-se como hedionda a extorsão qualificada pela restrição da liberdade da vítima com resultado lesão corporal grave ou óbito (sequestro-relâmpago grave);
- **Extorsão Mediante Sequestro**: o art. 159 do Código Penal é integralmente hediondo, abarcando a forma básica e as modalidades qualificadas pela duração, vítima menor de dezoito ou maior de sessenta anos, bando, lesão grave ou morte;
- **Furto com Explosivo**: o art. 155, § 4º-A, qualificado pelo emprego de artefato explosivo ou congênere que provoque perigo comum, integra taxativamente o rol legal.

| Espécie Delitiva | Requisito para Hediondez | Não Hediondo |
|---|---|---|
| Homicídio | Qualificado ou grupo de extermínio | Homicídio simples comum e culposo |
| Roubo | Arma de fogo, restrição da vítima ou lesão grave/morte | Emprego exclusivo de arma branca |
| Extorsão | Mediante sequestro (todas) ou relâmpago com dano grave/morte | Extorsão simples sem privação |
| Furto | Emprego de artefato explosivo | Escalar ou arrombar sem explosivos |

### Dignidade Sexual e Saúde Coletiva
- **Estupro e Estupro de Vulnerável**: os arts. 213 e 217-A do Código Penal são hediondos em todas as suas configurações típicas, desde a conjunção carnal e atos libidinosos simples até as formas que acarretam lesão corporal gravíssima ou óbito;
- **Exploração Sexual Infantojuvenil**: o art. 218-B pune com hediondez o favorecimento da prostituição ou outras condutas de exploração sexual contra menores de dezoito anos ou vulneráveis;
- **Epidemia com Morte**: no art. 267 do CP, apenas a modalidade qualificada pelo resultado morte atrai o estatuto hediondo;
- **Falsificação de Medicamentos**: a adulteração, corrupção ou alteração de produtos terapêuticos e medicinais (art. 273) constitui infração hedionda formal.

### Legislação Penal Extravagante
- **Estatuto do Desarmamento**: são crimes hediondos o porte ou posse clandestina de armamento de uso restritamente proibido (art. 16, § 2º), o comércio ilegal de armamentos (art. 17) e o tráfico internacional de armas (art. 18). O porte ou posse de material restrito comum deixou de configurar hediondez isolada nessa conduta básica;
- **Organização Criminosa**: a conduta de integrar organização criminosa voltada diretamente à consecução de crimes hediondos ou equiparados assume idêntica tipicidade restritiva;
- **Genocídio**: as condutas descritas nos arts. 1º, 2º e 3º da Lei 2.889/1956 compõem o catálogo de delitos hediondos.

### Para fixar
- O homicídio simples somente atrai hediondez se praticado em atividade típica de grupo de extermínio.
- No crime de roubo, o emprego de arma branca não configura hediondez, exigindo-se arma de fogo ou restrição de liberdade.
- O latrocínio e o roubo com lesão grave são hediondos tanto consumados quanto tentados.
- O estupro e o estupro de vulnerável ostentam natureza hedionda em todas as formas, simples e qualificadas.
- O furto com emprego de explosivo é hediondo; outras qualificadoras do furto não integram a lista.
- No desarmamento, apenas a posse ou porte de arma de fogo de uso proibido atrai a chancela da Lei 8.072/1990.""",
      "synthetic": [
        "**Homicídio qualificado**: todas as qualificadoras conferem hediondez, incluindo hipóteses funcionais e feminicídio.",
        "**Grupo de extermínio**: o homicídio simples é hediondo quando cometido em grupo de extermínio, ainda que por um só sujeito.",
        "**Armamento no roubo**: exige-se emprego de arma de fogo para a hediondez no roubo, sendo atípica a hediondez por arma branca.",
        "**Resultados patrimoniais**: o roubo e a extorsão qualificados por morte ou lesão grave assumem caráter hediondo absoluto.",
        "**Furto com explosivos**: apenas o furto qualificado pelo uso de explosivo gerador de perigo comum integra a Lei 8.072/1990.",
        "**Dignidade sexual**: estupro comum e estupro de vulnerável são hediondos em todas as modalidades do Código Penal.",
        "**Armas de fogo**: configuram hediondez o comércio ilegal, tráfico de armas e a posse ou porte de arma de uso proibido."
      ]
    },
    {
      "id": "legislacao-penal-especial/a11/s03",
      "fingerprint": {
        "startPage": 24,
        "endPage": 34,
        "startTopic": "Crimes Hediondos no ECA, Pacote Anticrime e Regras Processuais"
      },
      "analytic": """A sistemática de repressão aos crimes hediondos transcende a tipificação do Código Penal, irradiando consequências processuais e executórias fixadas no Estatuto da Criança e do Adolescente, na Lei de Execução Penal e na legislação processual geral.

### Tutela da Infância no Estatuto da Criança e do Adolescente
Com as constantes atualizações legislativas, a Lei 8.072/1990 passou a incorporar frontalmente as práticas delitivas mais gravosas do Estatuto da Criança e do Adolescente:
- **Produção e Direção de Pornografia (art. 240)**: envolve registrar, filmar, fotografar ou produzir violência sexual contra menores de dezoito anos, bem como intermediar ou transmitir essas condutas pela rede digital e telemática;
- **Comercialização e Exposição (art. 241)**: punição com natureza hedionda da venda ou exposição de material contendo abuso sexual infantojuvenil em qualquer mídia física ou ambiente virtual;
- **Distribuição e Publicação (art. 241-A)**: oferta, compartilhamento ou veiculação em redes sociais e plataformas informáticas;
- **Posse e Armazenamento (art. 241-B)**: a guarda em arquivos digitais ou mídias eletrônicas de fotografia ou vídeo contendo abuso sexual de menores também ostenta feição hedionda autônoma;
- **Aliciamento e Agenciamento (arts. 241-D e 244-A)**: facilitação e captação de vulneráveis para a prostituição ou exploração sexual comercial.

### Prisão Temporária e Prerrogativas Processuais
A Lei de Crimes Hediondos instituiu disciplina temporal diferenciada para a prisão temporária (Lei 7.960/1989):
- **Prazo Ordinário**: em regra, a custódia temporária nos delitos comuns dura 5 dias prorrogáveis por mais 5 dias;
- **Prazo Hediondo e Equiparado**: nas infrações da Lei 8.072/1990, o prazo é fixado em **30 dias**, prorrogável por igual período (mais 30 dias) perante demonstração inequívoca de extrema e comprovada necessidade;
- **Inconstitucionalidade do Regime Fechado Obrigatório**: o STF declarou inconstitucional a redação originária que impunha o cumprimento da reprimenda em regime integralmente fechado e, sucessivamente, o início obrigatório no fechado, devendo o juiz observar o art. 33 do CP.

### Execução Penal e Frações de Progressão de Regime
O Pacote Anticrime (Lei 13.964/2019) substituiu as antigas frações da LEP por patamares percentuais objetivos no art. 112 da Lei 7.210/1984:
- **40% da Pena**: exigido para apenado primário em condenação por crime hediondo ou equiparado **sem resultado morte**;
- **50% da Pena**: aplicável nas hipóteses de agente primário em crime hediondo **com resultado morte**, ou que exerça comando individual ou coletivo em organização criminosa voltada a crimes hediondos;
- **60% da Pena**: exigido para sentenciado **reincidente** em crime hediondo ou equiparado sem resultado morte;
- **70% da Pena**: reservado ao condenado **reincidente** em crime hediondo ou equiparado com resultado morte.

> ⚠️ Pegadinha: A reincidência para atrair os patamares de 60% e 70% não precisa ser específica; a reincidência genérica em combinação com a natureza hedionda do fato autoriza a incidência do percentual legal.

### Livramento Condicional e Colaboração Premiada
- **Livramento Condicional**: o art. 83, V, do Código Penal autoriza a benesse após o cumprimento de **mais de dois terços** da sanção carcerária, desde que o condenado não seja reincidente específico em crimes hediondos ou equiparados;
- **Proibição Absoluta de Livramento**: havendo condenação por crime hediondo ou equiparado com resultado morte, o apenado está formalmente impossibilitado de alcançar o livramento condicional em qualquer circunstância;
- **Colaboração Premiada (art. 8º da Lei 8.072/1990)**: o partícipe ou coautor que colaborar voluntariamente com os órgãos de persecução, prestando depoimento que viabilize o desmantelamento de bando ou quadrilha voltada ao cometimento de hediondos, terá sua sanção minorada de um a dois terços.

### Para fixar
- A produção, o armazenamento e a divulgação de pornografia infantojuvenil no ECA são crimes hediondos.
- A prisão temporária em delitos hediondos e equiparados tem duração de 30 dias prorrogáveis por mais 30.
- A progressão sem morte exige 40% para agente primário e 60% para condenado reincidente.
- A progressão nos casos de hediondez com resultado morte demanda 50% para primário e 70% para reincidente.
- O livramento condicional exige mais de dois terços de cumprimento e inocorrência de reincidência específica.
- É categoricamente proibido conceder livramento condicional para delitos hediondos qualificados por morte.""",
      "synthetic": [
        "**Proteção pelo ECA**: armazenar, produzir ou difundir material pornográfico infantojuvenil constitui conduta hedionda taxativa.",
        "**Prazo da temporária**: a prisão temporária nos crimes hediondos fixa-se em 30 dias, prorrogável uma vez por igual lapso temporal.",
        "**Progressão sem morte**: o cumprimento exige patamar de 40% da sanção corporal ao primário e 60% ao apenado reincidente.",
        "**Progressão com morte**: havendo resultado morte, a progressão submete-se ao índice de 50% para primário e 70% ao reincidente.",
        "**Vedação do livramento**: veda-se terminantemente conceder livramento condicional ao condenado por crime hediondo com óbito.",
        "**Regra do livramento**: nos hediondos sem morte, o livramento reclama mais de 2/3 da sanção e ausência de reincidência específica.",
        "**Delação premiada**: o partícipe que fornece dados aptos a dissolver a quadrilha faz jus à diminuição de um a dois terços da pena."
      ]
    }
  ]
}

Path("content/items/legislacao-penal-especial/a11.json").write_text(json.dumps(items_a11, ensure_ascii=False, indent=2), encoding="utf-8")
Path("content/summaries/legislacao-penal-especial/a11.json").write_text(json.dumps(summaries_a11, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved a11 files successfully.")
