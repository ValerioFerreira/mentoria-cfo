import json
import subprocess
from pathlib import Path

# AULA 12: Lei 7.716/1989 (Crimes de Preconceito de Raça ou de Cor)

items_a12 = {
  "aula": "legislacao-penal-especial/a12",
  "batch": "pcpe-bizu-legislacao-penal-especial",
  "status": "DRAFT",
  "stage": "bizu",
  "segments": [
    {
      "id": "legislacao-penal-especial/a12/s01",
      "bizu": {
        "summary": [
          "**Mandado constitucional**: o art. 5º, XLII, da Carta Magna define a prática do racismo como infração inafiançável e imprescritível, punida com pena de reclusão.",
          "**Vetores discriminatórios**: a Lei 7.716/1989 abrange condutas motivadas por intolerância ligada a cor, etnia, credo religioso ou região de nascimento.",
          "**Injúria racial equiparada**: a ofensa à honra subjetiva vinculada a elementos raciais ou étnicos configura espécie do gênero racismo, sendo inafiançável, imprescritível e de ação pública incondicionada.",
          "**Homotransfobia pelo STF**: atos discriminatórios contra orientação sexual e identidade de gênero foram enquadrados pelo STF como racismo social por omissão legislativa.",
          "**Segregação escolar**: recusar matrícula ou negar acesso a educandário público ou privado gera crime autônomo, com aumento de um terço se a vítima for menor de dezoito anos.",
          "**Acesso a serviços e espaços**: configura ilícito penal impedir entrada em estabelecimentos comerciais, transportes públicos, hotéis, restaurantes ou impor uso exclusivo de elevadores de serviço por motivo preconceituoso.",
          "**Discurso de ódio e símbolos**: praticar, induzir ou incitar a discriminação por meios de comunicação ou internet constitui modalidade qualificada, assim como veicular a cruz suástica para propaganda do nazismo.",
          "**Efeitos da condenação**: a perda do cargo público e a interdição temporária de estabelecimento privado dependem de expressa e motivada declaração na sentença, não operando de forma automática."
        ],
        "teoria": [
          {
            "statement": "Os efeitos extrapenais de perda de cargo público decorrentes de condenação pela Lei 7.716/1989 operam de modo automático logo após o trânsito em julgado.",
            "isTrue": False,
            "explanation": "O art. 18 da Lei 7.716/1989 expressamente determina que os efeitos da condenação não são automáticos, dependendo de fundamentação motivada na sentença."
          },
          {
            "statement": "O Supremo Tribunal Federal firmou tese de que a injúria racial constitui espécie do gênero racismo, ostentando natureza jurídica inafiançável e imprescritível.",
            "isTrue": True,
            "explanation": "No julgamento do HC 154.248 e com as reformas da Lei 14.532/2023, consolidou-se que a injúria preconceituosa é racismo, submetendo-se à imprescritibilidade."
          },
          {
            "statement": "A prática de recusar admissão de empregado em empresa privada por preconceito de cor é punida exclusivamente na esfera cível e trabalhista.",
            "isTrue": False,
            "explanation": "O art. 4º da Lei 7.716/1989 tipifica criminalmente a conduta de negar emprego em estabelecimento privado em razão de preconceito de raça ou cor."
          },
          {
            "statement": "A fabricação ou veiculação de suástica ou gamada com o desígnio de disseminar preceitos nazistas configura tipo autônomo punido com reclusão e multa.",
            "isTrue": True,
            "explanation": "Trata-se da infração capitulada no § 1º do art. 20 da Lei 7.716/1989, voltada a punir a divulgação de símbolos vinculados à ideologia nazista."
          }
        ],
        "revisao": [
          {
            "statement": "A tipificação das condutas discriminatórias da Lei 7.716/1989 restringe-se estritamente à cor da pele, não contemplando discriminação religiosa ou procedência nacional.",
            "isTrue": False,
            "explanation": "O art. 1º da lei estende a tutela penal a atos discriminatórios ancorados em cor, etnia, crença religiosa ou origem de procedência geográfica."
          },
          {
            "statement": "No delito de recusar ou impedir o ingresso de aluno em estabelecimento de ensino, a sanção penal sofre majoração caso a vítima seja menor de dezoito anos.",
            "isTrue": True,
            "explanation": "O art. 6º, parágrafo único, impõe elevação de pena de 1/3 quando a conduta segregatória for cometida contra menor de 18 anos."
          },
          {
            "statement": "A ação penal para processar e julgar o delito de injúria racial disciplinado no art. 2º-A da lei depende de representação formal do ofendido.",
            "isTrue": False,
            "explanation": "Com o advento da Lei 14.532/2023, todos os delitos descritos na Lei 7.716/1989, inclusive a injúria racial, são processados mediante ação penal pública incondicionada."
          },
          {
            "statement": "No histórico julgamento do caso Ellwanger, a Suprema Corte reconheceu que a veiculação de escritos antissemitas traduz manifestação de racismo imprescritível.",
            "isTrue": True,
            "explanation": "No HC 82.424/RS, o STF adotou a dimensão político-social do racismo, assentando a imprescritibilidade de publicações dirigidas contra o povo judeu."
          }
        ],
        "pointers": [
          {"topic": "Mandado constitucional e tutela de raça e cor", "pageRef": 3},
          {"topic": "Equiparação da homotransfobia e injúria racial", "pageRef": 6},
          {"topic": "Condutas segregatórias no trabalho e ensino", "pageRef": 8},
          {"topic": "Divulgação de nazismo e efeitos da condenação", "pageRef": 10}
        ]
      }
    }
  ]
}

# RESUMOS A12
summaries_a12 = {
  "aula": "legislacao-penal-especial/a12",
  "batch": "pcpe-summary-legislacao-penal-especial",
  "status": "DRAFT",
  "segments": [
    {
      "id": "legislacao-penal-especial/a12/s01",
      "fingerprint": {
        "startPage": 3,
        "endPage": 15,
        "startTopic": "Lei nº 7.716/1989 — Crimes Resultantes de Preconceito de Raça ou de Cor"
      },
      "analytic": """A Lei 7.716/1989 densifica a diretriz fundamental do art. 5º, XLII, da Carta Constitucional, que elevou o racismo ao patamar de infração inafiançável e imprescritível, sancionada com pena de reclusão. O diploma protege a dignidade da pessoa humana e a igualdade substancial contra agressões fundadas em diferenciações discriminatórias.

### Abrangência Típica e Vetores do Preconceito
O art. 1º da Lei Caó estabelece que serão punidos os crimes resultantes de discriminação ou preconceito fundamentados em:
- **Raça e Cor**: engloba fenótipos, tonalidade da pele e ascendência étnica de grupos historicamente vulnerabilizados;
- **Etnia e Procedência Nacional**: abrange nacionalidades, povos tradicionais e regiões de origem (incluindo xenofobia interna contra migrantes de estados brasileiros ou estrangeiros);
- **Religião**: protege liturgias, cultos, símbolos e instituições de fé contra perseguições intolerantes e atos hostis.

> ⚖️ Base normativa: O racismo não exige segregação biológica — categoria inexistente nas ciências naturais —, consubstanciando construção sociopolítica de dominação ou menoscabo de seres humanos agrupados sob pretensa inferioridade.

### A Evolução da Injúria Racial e o Racismo Social
A disciplina repressiva sofreu transformações axiológicas determinantes na jurisprudência e na legislação penal brasileira:
- **Caso Ellwanger (HC 82.424/RS)**: o Pleno do Supremo Tribunal Federal julgou que a propaganda antissemita e a apologia de teorias segregacionistas integram o gênero racismo, confirmando a imprescritibilidade penal da conduta de veicular livros negacionistas do holocausto;
- **Homotransfobia (ADO 26 e MI 4.733)**: sob a relatoria dos ministros e perante a inércia do Congresso Nacional, reconheceu-se que ofensas motivadas por orientação sexual e identidade de gênero consubstanciam racismo social, subsumindo-se aos preceitos da Lei 7.716/1989, preservada a liberdade religiosa pastoral que não descambe para discurso de ódio;
- **Equiparação e Migração da Injúria Racial**: historicamente fixada no art. 140, § 3º, do Código Penal, a injúria racial foi proclamada pelo STF no célebre voto relatado pelo ministro Edson Fachin (HC 154.248) como modalidade indissociável de racismo imprescritível. Subsequentemente, o Congresso editou a Lei 14.532/2023, introduzindo o art. 2º-A na Lei 7.716/1989, cominando reprimenda de 2 a 5 anos de reclusão e multa, além de formalizar a ação penal pública incondicionada.

### Tipos Penais em Espécie
A estrutura incriminadora da norma visa a coibir a segregação nas mais diversas órbitas da vida pública e privada:
- **Acesso ao Trabalho e Serviço Público (arts. 3º e 4º)**: obstar o ingresso a cargos públicos ou recusar admissão de empregado e ascensão funcional em empresas privadas em virtude de preconceitos;
- **Acesso ao Ensino (art. 6º)**: vetar a matrícula ou permanência de educando em estabelecimento de ensino público ou particular. Trata-se de hipótese qualificada pelo parágrafo único com aumento de um terço da sanção se praticada contra vítima menor de dezoito anos;
- **Fruição de Serviços Comerciais e Espaços Públicos (arts. 5º, 7º a 11)**: impedir o atendimento em hotéis, restaurantes, bares, transportes coletivos, clubes sociais ou impor distinção de elevadores prediais e entradas sociais;
- **Discurso de Ódio e Símbolos do Nazismo (art. 20)**: praticar, induzir ou incitar discriminação pelos meios de comunicação ou redes telemáticas. O § 1º criminaliza autônomamente o ato de produzir, comercializar ou expor a cruz suástica para veiculação nazista.

| Infrações em Espécie | Objeto da Tutela | Causa de Aumento / Detalhe |
|---|---|---|
| Art. 3º e 4º | Mercado de trabalho e função pública | Reclusão de 2 a 5 anos |
| Art. 6º | Acesso a colégios e universidades | Majorante de 1/3 se vítima menor de 18 anos |
| Art. 2º-A | Injúria racial e étnica | Ação penal pública incondicionada |
| Art. 20, § 1º | Disseminação da cruz suástica nazista | Reclusão de 2 a 5 anos e multa |

### Efeitos Extrapenais da Sentença Condenatória
Os arts. 16 e 17 preveem sanções adicionais graves ao condenado:
- **Servidor Público**: a perda da função ou destituição de cargo público;
- **Estabelecimento Comercial Privado**: a interdição e suspensão temporária do funcionamento comercial por intervalo de até 3 meses.

> ⚠️ Pegadinha: Por imperativo categórico do art. 18, esses efeitos **não são automáticos**, exigindo expressa, congruente e circunstanciada fundamentação motivadora pelo juízo prolator do veredicto na sentença penal condenatória.

### Para fixar
- O crime de racismo é formalmente inafiançável e imprescritível, apenado obrigatoriamente com reclusão.
- A tutela penal abrange atos motivados por preconceito de cor, etnia, religião e procedência nacional.
- A injúria racial consubstancia espécie do gênero racismo, sendo inafiançável, imprescritível e pública incondicionada.
- O Supremo Tribunal Federal enquadrou a homotransfobia na Lei 7.716/1989 sob a vertente do racismo social.
- A recusa de ingresso escolar a aluno menor de dezoito anos enseja aumento de pena de um terço.
- Os efeitos extrapenais da condenação exigem motivação expressa na sentença, inexistindo perda automática do cargo.""",
      "synthetic": [
        "**Matriz constitucional**: a conduta discriminatória de racismo é imprescritível e inafiançável, apenada com reclusão.",
        "**Dimensão do preconceito**: protege indivíduos contra discriminações calcadas em raça, cor, etnia, credo e origem territorial.",
        "**Injúria racial hodierna**: constitui crime autônomo da Lei 7.716/1989, sob ação incondicionada, sem prescrição e sem fiança.",
        "**Racismo social homotransfóbico**: condutas homofóbicas subsumem-se à lei especial até que intervenha disciplina parlamentar.",
        "**Segregação em escolas**: negar matrícula educacional a menores de dezoito anos atrai causa de exasperação penal de um terço.",
        "**Símbolos nazistas**: punem-se a exibição e difusão da cruz suástica com o propósito deliberado de propagar o nazismo.",
        "**Efeitos não automáticos**: a destituição do cargo público depende de fundamentação explícita na sentença judicial."
      ]
    }
  ]
}

Path("content/items/legislacao-penal-especial/a12.json").write_text(json.dumps(items_a12, ensure_ascii=False, indent=2), encoding="utf-8")
Path("content/summaries/legislacao-penal-especial/a12.json").write_text(json.dumps(summaries_a12, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved a12 files successfully.")
