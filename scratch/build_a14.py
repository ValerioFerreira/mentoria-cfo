import json
import subprocess
from pathlib import Path

# AULA 14: Lei 9.455/1997 (Crimes de Tortura)

items_a14 = {
  "aula": "legislacao-penal-especial/a14",
  "batch": "pcpe-bizu-legislacao-penal-especial",
  "status": "DRAFT",
  "stage": "bizu",
  "segments": [
    {
      "id": "legislacao-penal-especial/a14/s01",
      "bizu": {
        "summary": [
          "**Natureza constitucional**: a tortura constitui delito equiparado a hediondo por mandamento constitucional, inafiançável e insuscetível de graça, anistia ou indulto.",
          "**Tortura-prova e tortura-crime**: a tortura voltada à obtenção de confissão ou declaração e a destinada a provocar ação delitiva são crimes comuns, praticáveis por qualquer pessoa.",
          "**Tortura discriminatória**: pune a causação de sofrimento físico ou psíquico motivada restritivamente por preconceito racial ou confessional.",
          "**Tortura-castigo**: exige vínculo prévio de guarda, poder ou autoridade sobre o ofendido, demandando a produção de intenso sofrimento como punição pessoal ou prevenção.",
          "**Tortura da pessoa presa**: tipifica a imposição de sofrimento físico ou mental a indivíduo detido mediante a execução de atos não previstos nem autorizados em lei.",
          "**Tortura por omissão**: quem tem o dever jurídico de obstar ou apurar a tortura e se omite responde por crime autônomo com pena branda de detenção de um a quatro anos.",
          "**Modalidades qualificadas**: a tortura é qualificada exclusivamente quando sobrevier resultado preterdoloso de lesão corporal grave, gravíssima ou óbito da vítima.",
          "**Efeitos da condenação**: a perda do cargo público e a interdição para novo exercício funcional pelo dobro do tempo da pena aplicada são efeitos automáticos da sentença."
        ],
        "teoria": [
          {
            "statement": "O crime de tortura-prova voltado a arrancar confissão da vítima é classificado pela doutrina como crime próprio, exigindo a qualidade funcional de policial no agressor.",
            "isTrue": False,
            "explanation": "A tortura-prova (art. 1º, I, 'a') constitui crime comum, podendo ser perpetrada por qualquer pessoa (como seguranças particulares ou particulares comuns)."
          },
          {
            "statement": "A condenação definitiva pela prática de crime de tortura acarreta a perda do cargo público e a interdição funcional pelo dobro do prazo da sanção penal fixada.",
            "isTrue": True,
            "explanation": "O art. 1º, § 5º, determina a perda do cargo e a inabilitação pelo dobro da pena imposta, tratando-se de efeito extrapenal automático."
          },
          {
            "statement": "A autoridade que presencia a tortura e se omite do dever legal de agir para evitá-la responde pelas mesmas penas de reclusão cominadas aos torturadores executores.",
            "isTrue": False,
            "explanation": "A tortura omissiva (art. 1º, § 2º) consubstancia tipo subsidiário apenado com detenção de 1 a 4 anos, sanção mais branda do que a dos autores da tortura."
          },
          {
            "statement": "A aplicação da Lei 9.455/1997 alcança fatos cometidos fora do território nacional quando a vítima for brasileira ou o agente estiver sob jurisdição do Brasil.",
            "isTrue": True,
            "explanation": "O art. 2º da Lei consagra hipótese expressa de extraterritorialidade incondicionada da lei penal brasileira."
          }
        ],
        "revisao": [
          {
            "statement": "A produção de lesões corporais de natureza leve qualifica formalmente o crime de tortura, elevando as balizas mínimas e máximas da reprimenda legal.",
            "isTrue": False,
            "explanation": "As lesões leves são absorvidas pelo próprio tipo de tortura; a qualificadora do § 3º incide somente perante lesão grave, gravíssima ou resultado morte."
          },
          {
            "statement": "A sanção sofre exasperação fracionária de um sexto a um terço quando o crime de tortura é perpetrado em face de criança, adolescente, gestante ou pessoa idosa.",
            "isTrue": True,
            "explanation": "Trata-se da majorante expressamente prevista no art. 1º, § 4º, II, da Lei de Tortura para vítimas hipervulneráveis."
          },
          {
            "statement": "A imposição legal originária de cumprimento inicial da reprimenda em regime obrigatoriamente fechado para o crime de tortura foi mantida íntegra pelo STF.",
            "isTrue": False,
            "explanation": "O STF declarou inconstitucional a obrigatoriedade do regime inicial fechado no HC 111.840, aplicando-se os critérios do art. 33 do Código Penal."
          },
          {
            "statement": "A tortura praticada com a finalidade de coagir a vítima a praticar uma contravenção penal não se amolda à hipótese de tortura-crime do art. 1º, I, 'b'.",
            "isTrue": True,
            "explanation": "O dispositivo exige expressamente a finalidade de provocar 'ação ou omissão de natureza criminosa', afastando a subsunção quando se tratar de mera contravenção."
          }
        ],
        "pointers": [
          {"topic": "Conceito constitucional e modalidades de tortura", "pageRef": 3},
          {"topic": "Tortura-castigo e tortura do custodiado", "pageRef": 5},
          {"topic": "Tortura omissiva e formas qualificadas", "pageRef": 7},
          {"topic": "Efeitos automáticos e extraterritorialidade", "pageRef": 10}
        ]
      }
    }
  ]
}

# RESUMOS A14
summaries_a14 = {
  "aula": "legislacao-penal-especial/a14",
  "batch": "pcpe-summary-legislacao-penal-especial",
  "status": "DRAFT",
  "segments": [
    {
      "id": "legislacao-penal-especial/a14/s01",
      "fingerprint": {
        "startPage": 3,
        "endPage": 11,
        "startTopic": "Lei nº 9.455/1997 — Crimes de Tortura, Modalidades e Penas"
      },
      "analytic": """A Lei 9.455/1997 regulamentou o postulado da dignidade da pessoa humana e o mandado expresso de criminalização estatuído no art. 5º, III e XLIII, da Constituição da República. O ordenamento brasileiro pune com severidade extrema a imposição deliberada de dores agudas contra o ser humano, repudiando tratamentos degradantes e cruéis que marcaram precedentes históricos como o célebre caso da Favela Naval.

### Modalidades Típicas Fundamentais
A legislação pátria estabeleceu distinções precisas entre as formas executórias do delito de tortura:
- **Tortura-Confissão ou Tortura-Prova (art. 1º, I, 'a')**: constranger alguém com meio violento ou intimidação séria provocadora de padecimentos corpóreos ou psicológicos com o escopo de obter informação, declaração ou confissão da vítima ou de terceiro. Cuida-se de crime comum, que independe da condição funcional do sujeito ativo;
- **Tortura para Prática de Crime (art. 1º, I, 'b')**: constranger outrem para provocar ação ou omissão de natureza criminosa. Se o intuito do agressor for compelir a vítima à prática de mera contravenção penal (ex.: jogo do bicho), o fato refugirá da tortura, configurando constrangimento ilegal comum (art. 146 do CP);
- **Tortura Discriminatória (art. 1º, I, 'c')**: impor suplício físico ou psíquico motivado exclusivamente por fatores de raça ou religião. A discriminação por outros vieses não foi contemplada expressamente na redação literal desse dispositivo;
- **Tortura Punitiva ou Castigo (art. 1º, II)**: constranger quem se encontre sob subordinação jurídica, custódia disciplinar ou autoridade do autor, mediante sevícias físicas ou psicológicas severas, visando infligir reprimenda pessoal ou ação profilática. É crime próprio, dependendo de relação preexistente e dor de intensidade manifesta;
- **Tortura do Preso ou Sujeito a Medida Cautelar (art. 1º, § 1º)**: infligir sofrimento a indivíduo encarcerado mediante a imposição de atos vexatórios não autorizados em normas legais ou regulamentares.

### A Omissão Perante a Tortura e Formas Qualificadas
A estrutura típica reserva disciplina excepcional à conduta omissiva:
- **Tortura Omissiva ou Imprópria (art. 1º, § 2º)**: aquele que se omite em face das condutas anteriores, tendo o dever legal de evitá-las ou de apurá-las, responde com reprimenda autônoma atenuada de **detenção de 1 a 4 anos**. O preceito alcança tanto os garantes quanto autoridades com atribuição correicional;
- **Formas Qualificadas pelo Resultado (art. 1º, § 3º)**: a tortura é qualificada unicamente pelo resultado preterdoloso de lesão corporal grave ou gravíssima (reclusão de 4 a 10 anos) ou morte da vítima (reclusão de 8 a 16 anos). O resultado gravoso reclama nexo de imputação a título de culpa. As lesões de natureza leve restam integralmente absorvidas pela violência elementar do tipo básico.

| Modalidade | Natureza do Crime | Pena Cominada |
|---|---|---|
| Tortura clássica (arts. 1º, I e II) | Comum / Próprio | Reclusão de 2 a 8 anos |
| Tortura omissiva (art. 1º, § 2º) | Omissivo próprio | Detenção de 1 a 4 anos |
| Qualificada por lesão grave | Preterdoloso | Reclusão de 4 a 10 anos |
| Qualificada por morte | Preterdoloso | Reclusão de 8 a 16 anos |

### Causas de Aumento e Efeitos Específicos da Condenação
- **Majorantes Gerais (§ 4º)**: a pena é exasperada de 1/6 a 1/3 se o crime for cometido:
  1. Por agente público no exercício ou pretexto da função;
  2. Contra criança, adolescente, gestante, pessoa com deficiência ou maior de sessenta anos;
  3. Mediante privação de liberdade na modalidade de sequestro;
- **Efeitos da Condenação (§ 5º)**: a condenação penal definitiva gera a perda compulsória da titularidade de função, posto ou trabalho público e o afastamento inabilitador para novo provimento estatal pelo dobro do prazo da sanção corporal imposta. Diferentemente do abuso de autoridade, esse efeito é **automático**, dispensando fundamentação individualizada na sentença;
- **Inconstitucionalidade do Regime Fechado Obrigatório**: o Plenário do STF afastou no HC 111.840 o rigor do § 7º (regime inicial fechado cogente), franqueando a individualização judicial das penas conforme o art. 33 do Código Penal;
- **Extraterritorialidade Incondicionada (art. 2º)**: o diploma aplica-se a delitos perpetrados no estrangeiro se o sujeito passivo for cidadão brasileiro ou se o autor for localizado em área sob jurisdição do país.

### Para fixar
- A tortura para obtenção de confissão é crime comum, podendo ser cometida por particular.
- A tortura-crime exige a finalidade de praticar crime, não alcançando contravenções penais.
- A tortura omissiva é apenada com detenção de um a quatro anos, em patamar inferior aos executores.
- A produção de lesões leves na vítima é absorvida pela própria violência da tortura.
- A perda do cargo público e a interdição funcional pelo dobro da pena são efeitos automáticos.
- A extraterritorialidade incondicionada incide quando a vítima for brasileira ou o agente estiver no país.""",
      "synthetic": [
        "**Tortura-prova comum**: a conduta de torturar visando confissão ou informe é crime comum praticável por particular.",
        "**Tortura-crime restrita**: a coação deve destinar-se à prática de crime, excluída a subsunção de contravenções.",
        "**Intenso sofrimento no castigo**: a tortura-castigo pressupõe subordinação funcional e dor física ou mental intensa.",
        "**Tortura por omissão atenuada**: quem se omite diante do dever de impedir ou apurar sofre pena atenuada de detenção.",
        "**Absorção da lesão leve**: ofensas corporais leves integram a tortura básica; qualificadoras reclamam dano grave ou óbito.",
        "**Efeitos automáticos na condenação**: a perda do posto funcional e o banimento pelo dobro da pena operam automaticamente.",
        "**Extraterritorialidade**: a lei incide no estrangeiro quando a vítima for brasileira ou o autor estiver em solo pátrio."
      ]
    }
  ]
}

Path("content/items/legislacao-penal-especial/a14.json").write_text(json.dumps(items_a14, ensure_ascii=False, indent=2), encoding="utf-8")
Path("content/summaries/legislacao-penal-especial/a14.json").write_text(json.dumps(summaries_a14, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved a14 files successfully.")
