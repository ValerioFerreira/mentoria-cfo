import json
from pathlib import Path

# COMPLEMENTO C01: Aspectos Penais do ECA (Lei 8.069/1990)

ref_segs = {s["id"]: s for s in json.loads(Path("content/segments/legislacao-penal-especial.json").read_text(encoding="utf-8"))["segments"]}

items_c01 = {
  "aula": "legislacao-penal-especial/c01",
  "batch": "pcpe-bizu-legislacao-penal-especial",
  "status": "DRAFT",
  "stage": "bizu",
  "segments": [
    {
      "id": "legislacao-penal-especial/c01/s01",
      "bizu": {
        "summary": [
          "**Conceito de ato infracional**: conduta análoga a crime ou contravenção penal perpetrada por criança ou adolescente inimputável.",
          "**Critério do tempus regit actum**: afere-se a imputabilidade penal considerando estritamente a data do fato delituoso (Súmula 605/STJ).",
          "**Tratamento à criança**: menores de doze anos submetem-se exclusivamente a medidas de proteção, sendo vedada internação socioeducativa.",
          "**Internação provisória cautelar**: a segregação anterior à sentença definitiva submete-se ao prazo improrrogável de quarenta e cinco dias.",
          "**Flagrante com violência**: ato infracional com violência ou grave ameaça reclama lavratura de Auto de Apreensão em Flagrante.",
          "**Ato infracional sem violência**: condutas sem violência admitem substituição por Boletim de Ocorrência Circunstanciado (BOC).",
          "**Ação penal incondicionada**: todos os crimes tipificados no Estatuto da Criança e do Adolescente são de ação pública incondicionada.",
          "**Formalidade da corrupção**: a configuração do crime do art. 244-B independe de prova da efetiva corrupção (Súmula 500 do STJ)."
        ],
        "teoria": [
          {
            "statement": "A criança de dez anos que pratica conduta análoga a homicídio qualificado submete-se à aplicação judicial de medida socioeducativa de internação.",
            "isTrue": False,
            "explanation": "A crianças (menores de 12 anos incompletos) aplicam-se unicamente medidas protetivas do art. 101, jamais medidas socioeducativas ou internação."
          },
          {
            "statement": "O crime de corrupção de menores tipificado no art. 244-B do ECA consuma-se ainda que o adolescente aliciado já seja reincidente na prática de infrações.",
            "isTrue": True,
            "explanation": "A Súmula 500 do STJ consolidou que o delito é formal, prescindindo de comprovação da efetiva degradação moral do jovem envolvido."
          },
          {
            "statement": "A internação provisória de adolescente infrator decretada antes da prolação da sentença definitiva pode perdurar por até noventa dias úteis.",
            "isTrue": False,
            "explanation": "O art. 108 estabelece o prazo máximo e improrrogável de quarenta e cinco dias para a decretação da internação provisória."
          },
          {
            "statement": "A prática de ato infracional praticado sem violência ou grave ameaça à pessoa autoriza a substituição do auto de apreensão por Boletim de Ocorrência Circunstanciado.",
            "isTrue": True,
            "explanation": "O art. 173 faculta a lavratura de BOC em infrações sem violência ou grave ameaça, liberando-se o adolescente aos pais."
          }
        ],
        "revisao": [
          {
            "statement": "A ação penal para apurar os crimes tipificados na parte especial do Estatuto da Criança e do Adolescente depende de representação da vítima.",
            "isTrue": False,
            "explanation": "O art. 227 estabelece que as infrações penais catalogadas no ECA processam-se mediante ação penal pública incondicionada."
          },
          {
            "statement": "Para a aferição da condição de inimputabilidade e aplicação das normas do ECA, adota-se a teoria da atividade considerando a idade na data da conduta.",
            "isTrue": True,
            "explanation": "O art. 104, parágrafo único, e a Súmula 605 do STJ estipulam que a idade do autor é considerada na data do fato criminoso."
          },
          {
            "statement": "A posse ou o simples armazenamento de imagens pornográficas de menores em dispositivos eletrônicos é atípica se ausente o intuito de mercancia.",
            "isTrue": False,
            "explanation": "O art. 241-B pune com reclusão a simples conduta de adquirir, possuir ou armazenar material pornográfico infanto-juvenil."
          },
          {
            "statement": "A entrega voluntária de adolescente infrator aos pais pela autoridade policial pode ser obstada quando evidenciado risco à ordem pública.",
            "isTrue": True,
            "explanation": "O art. 174, in fine, autoriza a retenção do adolescente quando a gravidade da conduta demandar sua manutenção sob custódia estatal."
          }
        ],
        "pointers": [
          {"topic": "Ato infracional, inimputabilidade e Súmula 605 do STJ", "pageRef": 1},
          {"topic": "Procedimento policial em flagrante, Auto de Apreensão e BOC", "pageRef": 2},
          {"topic": "Corrupção de menores do art. 244-B e Súmula 500 do STJ", "pageRef": 3},
          {"topic": "Crimes sexuais, armazenamento de pornografia e bebidas", "pageRef": 4}
        ]
      }
    }
  ]
}

# RESUMOS C01
summaries_c01 = {
  "aula": "legislacao-penal-especial/c01",
  "batch": "pcpe-summary-legislacao-penal-especial",
  "status": "DRAFT",
  "segments": [
    {
      "id": "legislacao-penal-especial/c01/s01",
      "fingerprint": {
        "startPage": ref_segs["legislacao-penal-especial/c01/s01"]["startPage"],
        "endPage": ref_segs["legislacao-penal-especial/c01/s01"]["endPage"],
        "startTopic": ref_segs["legislacao-penal-especial/c01/s01"].get("startTopic")
      },
      "analytic": """O Estatuto da Criança e do Adolescente (Lei 8.069/1990) estruturou um microssistema protetivo integral que compatibiliza as garantias constitucionais do jovem com a disciplina da apuração policial de atos infracionais e a tutela punitiva contra abusos praticados por adultos.

### Ato Infracional, Inimputabilidade e Teoria da Atividade
A resposta estatal frente à conduta infracional fundamenta-se na distinção etária dos autores:
- **Conceito Dogmático (art. 103)**: consubstancia ato infracional o comportamento descrito em lei como crime ou contravenção penal;
- **Inimputabilidade Penal Absoluta (art. 104)**: os menores de dezoito anos são penalmente inimputáveis, submetendo-se exclusivamente às normas e medidas pedagógicas do estatuto;
- **Teoria da Atividade (*Tempus Regit Actum*)**: para a apuração da responsabilidade infracional, considera-se a exata idade do autor na data da conduta delituosa (art. 104, parágrafo único e **Súmula 605 do STJ**), sendo irrelevante o momento do resultado;
- **Diferenciação entre Criança e Adolescente**:
  1. **Criança (até 12 anos incompletos)**: sujeita-se exclusivamente a medidas de proteção (art. 101), sendo juridicamente vedada a imposição de medidas socioeducativas ou qualquer modalidade de internação;
  2. **Adolescente (entre 12 e 18 anos incompletos)**: submete-se a medidas socioeducativas pedagógicas (advertência, prestação de serviços, liberdade assistida, semiliberdade e internação) e tutelas protetivas;
- **Internação Provisória Cautelar (art. 108)**: a privação cautelar de liberdade anterior à prolação de sentença pode ser fixada pelo magistrado pelo prazo máximo, improrrogável e estrito de **45 dias**.

### Procedimentos Policiais na Apuração de Flagrante Infracional
O estatuto delineia o agir da polícia judiciária no momento da apreensão:
- **Flagrante com Violência ou Grave Ameaça (art. 172)**: havendo violência contra pessoa, a autoridade policial lavra compulsória e formalmente o **Auto de Apreensão em Flagrante**, ouvindo testemunhas, vítima e menor, apreendendo os instrumentos e requisitando perícias técnicas;
- **Flagrante sem Violência ou Grave Ameaça (art. 173)**: ocorrendo infração desprovida de violência pessoal (como furto simples ou posse de entorpecentes), o delegado de polícia pode substituir o auto formal pela confecção de **Boletim de Ocorrência Circunstanciado (BOC)**, procedendo à desinternação imediata;
- **Liberação sob Compromisso ou Manutenção Custodial (art. 174)**: comparecendo genitores ou responsável idôneo, o jovem é liberado sob termo formal de compromisso e apresentação perante o Ministério Público. Excepcionalmente, se a gravidade do fato e a repercussão social gerarem risco à ordem pública ou à segurança do próprio apreendido, a polícia deve mantê-lo sob custódia e conduzi-lo desde logo ao Ministério Público.

### Tipos Penais Próprios e Súmula 500 do STJ
- **Ação Penal Pública Incondicionada (art. 227)**: todos os delitos previstos na parte penal do ECA processam-se sem dependência de representação;
- **Corrupção de Menores (art. 244-B)**: punido com reclusão de 1 a 4 anos quem corrompe ou facilita a corrupção de menor de 18 anos, praticando com ele infração penal ou induzindo-o a executá-la. Conforme a **Súmula 500 do STJ**, trata-se de **crime formal**, cuja consumação independe de prova da efetiva corrupção do jovem ou de seu histórico anterior de infrações;
- **Crimes Sexuais e Pornografia Infanto-Juvenil (arts. 240 a 241-E)**: sanciona a produção de cena pornográfica (delito hediondo), a divulgação pública e a simples posse ou armazenamento digital de material ilícito (art. 241-B);
- **Fornecimento de Bebidas e Substâncias Nocivas (art. 243)**: pune a entrega ou venda de bebidas alcoólicas a menores. Tratando-se de entorpecentes ilícitos, incide a legislação especial do tráfico de drogas majorado pelo envolvimento de crianças.

### Para fixar
- Ato infracional é a conduta descrita em lei como crime ou contravenção penal.
- Considera-se a idade do jovem na data do fato conforme consagra a Súmula 605 do STJ.
- Crianças submetem-se unicamente a medidas de proteção, sendo vedada a internação.
- A internação provisória decretada pelo juiz antes da sentença não pode ultrapassar 45 dias.
- Infrações cometidas sem violência pessoal autorizam a confecção de BOC pela autoridade policial.
- A corrupção de menores do art. 244-B é crime formal de acordo com a Súmula 500 do STJ.
- Todos os crimes tipificados no Estatuto da Criança e do Adolescente são de ação pública incondicionada.""",
      "synthetic": [
        "**Equiparação do ato infracional**: define-se como conduta análoga a crime ou contravenção imputada a menores de dezoito anos.",
        "**Teoria da atividade e Súmula 605**: afere-se a maioridade considerando categoricamente a idade do jovem no exato momento da ação.",
        "**Proteção exclusiva à infância**: crianças menores de doze anos incompletos recebem somente medidas protetivas, repelindo qualquer internação.",
        "**Limite improrrogável de 45 dias**: a internação provisória cautelar do adolescente infrator não pode superar quarenta e cinco dias.",
        "**Dicotomia entre auto e BOC**: infrações com violência exigem Auto de Apreensão em Flagrante, admitindo-se BOC nas hipóteses sem violência.",
        "**Súmula 500 e corrupção formal**: o crime do art. 244-B consuma-se formalmente sem necessidade de comprovar prévia inocência do menor.",
        "**Tutela contra pornografia digital**: a legislação incrimina a produção, difusão e o armazenamento eletrônico de cenas envolvendo menores.",
        "**Ação pública incondicionada**: as infrações penais catalogadas na parte especial do ECA processam-se sem dependência de representação."
      ]
    }
  ]
}

Path("content/items/legislacao-penal-especial/c01.json").write_text(json.dumps(items_c01, ensure_ascii=False, indent=2), encoding="utf-8")
Path("content/summaries/legislacao-penal-especial/c01.json").write_text(json.dumps(summaries_c01, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved c01 files successfully.")
