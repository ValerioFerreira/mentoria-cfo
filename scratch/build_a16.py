import json
import subprocess
from pathlib import Path

# AULA 16: Lei 9.503/1997 (Código de Trânsito Brasileiro)

items_a16 = {
  "aula": "legislacao-penal-especial/a16",
  "batch": "pcpe-bizu-legislacao-penal-especial",
  "status": "DRAFT",
  "stage": "bizu",
  "segments": [
    {
      "id": "legislacao-penal-especial/a16/s01",
      "bizu": {
        "summary": [
          "**Prioridade e circulação**: veículos de socorro, emergência e salvamento gozam de livre trânsito e estacionamento quando em serviço urgente e com dispositivos sonoros e ópticos acionados.",
          "**Equipamentos de segurança**: além do cinto e airbag, instituiu-se a exigência de tacógrafo para transporte de escolares, coletivos de passageiros e carga perigosa, além de luzes de rodagem diurna.",
          "**Habilitação de categorias superiores**: para obtenção das categorias D e E, exige-se idade mínima de vinte e um anos e não ter praticado infração gravíssima nos últimos doze meses.",
          "**Interstícios para categoria D**: requer pelo menos dois anos na categoria B ou um ano na categoria C; para a categoria E exige-se um ano na C ou um ano na D.",
          "**Validade do exame de aptidão**: o exame pericial de sanidade física e mental possui vigência de dez anos até cinquenta anos de idade, cinco anos entre cinquenta e sessenta e nove anos, e três anos a partir dos setenta.",
          "**Exame toxicológico periódico**: condutores das categorias C, D e E submetem-se à testagem de larga janela de detecção a cada dois anos e meio se menores de setenta anos.",
          "**Consequência da recusa**: deixar de realizar o toxicológico periódico constitui infração gravíssima autônoma, gerando impedimento temporário na renovação da CNH.",
          "**Sinalização emergencial**: havendo retenção forçada do veículo na pista de rolamento, é obrigatória a advertência luminosa imediata para evitar colisões."
        ],
        "teoria": [
          {
            "statement": "O condutor habilitado na categoria B pode ascender diretamente para a categoria E caso comprove aprovação em curso de direção defensiva e não tenha pontos na carteira.",
            "isTrue": False,
            "explanation": "A habilitação na categoria E exige prévia habilitação há no mínimo 1 ano na categoria C ou há no mínimo 1 ano na categoria D, sendo vedada a ascensão direta da B para a E."
          },
          {
            "statement": "Os veículos destinados à condução coletiva de escolares são obrigados a possuir registrador instantâneo inalterável de velocidade e tempo em pleno funcionamento.",
            "isTrue": True,
            "explanation": "O art. 105, II, do CTB exige o registrador tacógrafo para veículos de transporte escolar, de passageiros com mais de dez lugares e de transporte de carga perigosa."
          },
          {
            "statement": "A validade máxima do exame de aptidão física e mental para condutores com menos de cinquenta anos de idade é de cinco anos conforme a legislação em vigor.",
            "isTrue": False,
            "explanation": "Com as reformas legislativas recentes, o prazo de validade do exame para condutores com menos de 50 anos de idade foi ampliado para 10 anos."
          },
          {
            "statement": "Motoristas habilitados nos grupos C, D e E que não tenham atingido setenta anos de idade devem realizar exame toxicológico periódico a cada trinta meses.",
            "isTrue": True,
            "explanation": "O art. 148-A, § 2º, impõe o exame toxicológico periódico a cada 2 anos e 6 meses para motoristas profissionais dessas categorias com menos de 70 anos."
          }
        ],
        "revisao": [
          {
            "statement": "Veículos precedidos de batedores e ambulâncias de resgate gozam de prioridade irrestrita nas vias mesmo sem acionamento dos dispositivos de alarme sonoro e iluminação intermitente.",
            "isTrue": False,
            "explanation": "O art. 29, VII, condiciona expressamente as prerrogativas de prioridade ao fato de estarem os veículos em efetivo serviço de urgência e devidamente identificados por luzes e sirene."
          },
          {
            "statement": "Para candidatar-se à obtenção de Carteira Nacional de Habilitação na categoria D, o interessado deve ter completado a idade mínima de vinte e um anos.",
            "isTrue": True,
            "explanation": "O art. 145, I, do CTB estabelece a idade mínima de 21 anos como condição legal intransponível para as categorias D e E."
          },
          {
            "statement": "A renovação periódica da habilitação para condutores com idade igual ou superior a setenta anos ocorre no interregno legal ordinário de cinco anos.",
            "isTrue": False,
            "explanation": "Conforme o art. 147, § 2º, III, a validade do exame pericial é reduzida para 3 anos para motoristas com idade igual ou superior a 70 anos."
          },
          {
            "statement": "O exame toxicológico de larga janela busca averiguar o consumo habitual ou eventual de substâncias psicoativas que comprometam a segurança no trânsito viário.",
            "isTrue": True,
            "explanation": "O procedimento laboratorial destina-se a rastrear substâncias estupefacientes no organismo em janela retrospectiva mínima de noventa dias."
          }
        ],
        "pointers": [
          {"topic": "Normas gerais de circulação e veículos de emergência", "pageRef": 3},
          {"topic": "Equipamentos veiculares obrigatórios e tacógrafo", "pageRef": 5},
          {"topic": "Categorias de habilitação e interstícios", "pageRef": 7},
          {"topic": "Validade da CNH e exame toxicológico periódico", "pageRef": 9}
        ]
      }
    },
    {
      "id": "legislacao-penal-especial/a16/s02",
      "bizu": {
        "summary": [
          "**Afastamento da Lei 9.099/1995**: não se aplicam transação penal ou composição civil se o condutor estiver embriagado, disputando racha ou em excesso superior a 50 km/h.",
          "**Socorro à vítima e flagrante**: ao condutor que prestar socorro imediato e integral à vítima de sinistro viário não se imporá prisão em flagrante nem se arbitrará fiança.",
          "**Suspensão ou proibição da CNH**: a penalidade privativa do direito de dirigir varia de dois meses a cinco anos, podendo ser imposta como pena autônoma ou cumulativa.",
          "**Homicídio culposo com embriaguez**: dirigir alcoolizado e causar morte culposa atrai pena reclusiva de cinco a oito anos, sendo vedada a conversão em penas restritivas.",
          "**Lesão culposa qualificada**: a lesão corporal culposa ao volante sob efeito de álcool ou drogas que cause resultado grave ou gravíssimo é apenada com reclusão de dois a cinco anos.",
          "**Embriaguez como perigo abstrato**: o crime do art. 306 consuma-se pela alteração psicomotora comprovada por bafômetro (0,3 mg/L) ou sangue (6 dg/L), sem exigir dano concreto.",
          "**Fuga do local do sinistro**: fugir do local para evitar a responsabilidade civil ou penal tipifica crime do art. 305, reputado plenamente constitucional pelo STF.",
          "**Direção sem habilitação**: o art. 309 exige a geração de perigo concreto de dano para configurar crime, enquanto entregar direção a inabilitado (art. 310) é de perigo abstrato."
        ],
        "teoria": [
          {
            "statement": "O crime de homicídio culposo na direção de veículo qualificado pela ingestão de álcool admite a substituição da pena privativa de liberdade por penas restritivas de direitos.",
            "isTrue": False,
            "explanation": "O art. 312-B do CTB proíbe terminantemente a substituição da pena corporal por penas restritivas nos homicídios e lesões culposas qualificadas pela embriaguez."
          },
          {
            "statement": "O motorista que, após se envolver em sinistro viário com vítimas, presta imediato e integral socorro aos feridos não será submetido à prisão em flagrante delito.",
            "isTrue": True,
            "explanation": "O art. 301 veda a lavratura de auto de prisão em flagrante e a exigência de fiança quando o condutor presta socorro célere e integral aos lesionados."
          },
          {
            "statement": "O crime de conduzir veículo automotor sem possuir Carteira Nacional de Habilitação do art. 309 é de perigo abstrato, consumando-se pela mera falta documental.",
            "isTrue": False,
            "explanation": "O art. 309 exige expressamente a geração de 'perigo de dano' concreto (Súmula 720 do STF); perigo abstrato é a conduta do art. 310 (entregar a direção a outrem)."
          },
          {
            "statement": "A sanção que impõe a suspensão do direito de conduzir veículos automotores ou o impedimento de obter nova permissão estende-se pelo intervalo de dois meses a cinco anos.",
            "isTrue": True,
            "explanation": "Conforme o art. 293 do Código de Trânsito Brasileiro, os limites temporais da sanção de suspensão da habilitação situam-se entre dois meses e cinco anos."
          }
        ],
        "revisao": [
          {
            "statement": "A aplicação dos benefícios da transação penal da Lei 9.099/1995 permanece assegurada ao condutor que praticar lesão culposa no trânsito sob velocidade 60 km/h acima do limite.",
            "isTrue": False,
            "explanation": "O art. 291, § 1º, afasta a incidência da Lei 9.099/1995 quando a velocidade do veículo superar em mais de 50 km/h o limite máximo permitido para o local."
          },
          {
            "statement": "O Supremo Tribunal Federal julgou constitucional o tipo penal do art. 305 do CTB, que pune a conduta de evadir-se do local do sinistro para fugir à responsabilidade.",
            "isTrue": True,
            "explanation": "No julgamento de repercussão geral (Tema 907), o STF assentou que o art. 305 é compatível com o princípio da não autoincriminação."
          },
          {
            "statement": "A embriaguez ao volante descrita no art. 306 do CTB demanda a ocorrência de abalroamento ou condução em zigue-zague para justificar a persecução penal.",
            "isTrue": False,
            "explanation": "O art. 306 constitui crime formal e de perigo abstrato; demonstrada a alteração da capacidade psicomotora nos parâmetros legais, o crime resta aperfeiçoado."
          },
          {
            "statement": "A conduta de franquear a condução de automotor a indivíduo desprovido de habilitação legal ou sem higidez física configura crime de perigo abstrato.",
            "isTrue": True,
            "explanation": "A Súmula 575 do STJ consolidou que o delito do art. 310 do CTB prescinde de demonstração de perigo concreto de dano para sua consumação."
          }
        ],
        "pointers": [
          {"topic": "Afastamento da Lei 9.099 e limites da suspensão", "pageRef": 12},
          {"topic": "Inaplicabilidade do flagrante e socorro à vítima", "pageRef": 15},
          {"topic": "Homicídio e lesão qualificados pela embriaguez", "pageRef": 18},
          {"topic": "Crimes de perigo concreto e abstrato no trânsito", "pageRef": 22}
        ]
      }
    }
  ]
}

# RESUMOS A16
summaries_a16 = {
  "aula": "legislacao-penal-especial/a16",
  "batch": "pcpe-summary-legislacao-penal-especial",
  "status": "DRAFT",
  "segments": [
    {
      "id": "legislacao-penal-especial/a16/s01",
      "fingerprint": {
        "startPage": 3,
        "endPage": 10,
        "startTopic": "Código de Trânsito Brasileiro — Disposições Gerais e Infrações"
      },
      "analytic": """A Lei 9.503/1997 disciplina o trânsito de qualquer natureza nas vias terrestres do território nacional abertas à circulação. Além de instituir as diretrizes do Sistema Nacional de Trânsito, o Código estabelece preceitos cogentes sobre circulação, segurança veicular e requisitos de habilitação técnica.

### Normas Fundamentais de Circulação e Conduta
O Código de Trânsito adota regras basilares para salvaguardar a incolumidade dos usuários das vias:
- **Prioridade de Passagem (art. 29, VII)**: os veículos de socorro de incêndio e salvamento, os de polícia, os de fiscalização e operação de trânsito e as ambulâncias gozam de livre circulação, estacionamento e parada quando em efetivo serviço de urgência e devidamente identificados por alarme sonoro e iluminação vermelha intermitente;
- **Sinalização em Emergência (art. 46)**: sempre que for forçosa a parada ou imobilização emergencial de veículo sobre o leito viário, incumbe ao motorista acionar imediatamente o pisca-alerta e posicionar o dispositivo de sinalização retrorrefletor na distância regulamentar;
- **Preferência em Cruzamentos e Rotatórias**: nos cruzamentos desprovidos de semáforo, a preferência assiste ao condutor que trafega por rodovia, ao que circula por rotatória ou, nos demais casos, àquele que provém pela direita do condutor.

### Equipamentos Obrigatórios de Segurança
O art. 105 da norma lista equipamentos imperativos estabelecidos pelo legislador e complementados pelas resoluções do CONTRAN:
- **Cinto de Segurança e Encostos de Cabeça**: de uso compulsório para todos os ocupantes do veículo automotor;
- **Airbag Duplo Frontal**: exigência técnica para proteção do condutor e do passageiro dianteiro;
- **Registrador Tacógrafo**: instrumento registrador inalterável de velocidade e tempo, compulsório para transporte escolar, transporte coletivo com mais de 10 passageiros e carga perigosa;
- **Luzes de Rodagem Diurna (DRL)**: inovação tecnológica inserida para elevar a visualização do veículo durante o período diurno em rodovias.

### Regime de Habilitação e Controle Toxicológico
O processo de formação e renovação da Carteira Nacional de Habilitação contempla requisitos rigorosos:
- **Requisitos para Categorias D e E (arts. 143 e 145)**: demandam idade mínima de 21 anos, não ter incorrido em infração gravíssima nos últimos doze meses e prévio cumprimento de interstícios temporais:
  1. Para categoria D: mínimo de 2 anos na B ou 1 ano na C;
  2. Para categoria E: mínimo de 1 ano na C ou 1 ano na D;
- **Validade do Exame Pericial de Aptidão (art. 147)**:
  - Condutores com idade inferior a 50 anos: validade máxima de **10 anos**;
  - Condutores com idade igual ou superior a 50 anos e inferior a 70 anos: validade de **5 anos**;
  - Condutores com idade igual ou superior a 70 anos: validade de **3 anos**;
- **Exame Toxicológico Periódico (art. 148-A)**: exigido dos condutores habilitados nas categorias C, D e E para flagrar uso de substâncias entorpecentes em janela laboratorial mínima de 90 dias. Para motoristas profissionais com menos de 70 anos, a renovação deve ocorrer no intervalo de **2 anos e 6 meses**. A recusa em realizá-lo gera infração gravíssima com suspensão do direito de dirigir.

### Para fixar
- Veículos de emergência só possuem prioridade quando em serviço urgente e com sinais ligados.
- A imobilização do veículo no leito carroçável exige pronta sinalização de advertência.
- O tacógrafo é de uso obrigatório no transporte de escolares e coletivo de passageiros.
- A categoria D exige 21 anos e prévia habilitação há dois anos na B ou um ano na C.
- A CNH tem validade máxima de dez anos para motoristas com idade inferior a cinquenta anos.
- Condutores das categorias C, D e E devem renovar o toxicológico a cada dois anos e meio.""",
      "synthetic": [
        "**Prioridade de socorro**: ambulâncias e viaturas gozam de trânsito livre quando em socorro urgente com sirene e luzes acionadas.",
        "**Equipamento tacógrafo**: impõe-se o uso de tacógrafo a veículos de condução escolar e transporte coletivo de passageiros.",
        "**Requisitos categoria D**: reclama vinte e um anos completos e habilitação prévia de dois anos na classe B ou um ano na C.",
        "**Validade decenal da CNH**: o exame de aptidão vigora por dez anos para motoristas jovens com idade menor que cinquenta anos.",
        "**Periodicidade idosa**: a partir dos setenta anos de idade a renovação pericial da habilitação reduz-se para três anos.",
        "**Exame toxicológico C, D e E**: a testagem periódica de substâncias psicoativas deve ser feita no intervalo de dois anos e meio.",
        "**Infração pela recusa**: recusar submeter-se ao exame toxicológico periódico gera sanção gravíssima e suspensão da CNH."
      ]
    },
    {
      "id": "legislacao-penal-especial/a16/s02",
      "fingerprint": {
        "startPage": 11,
        "endPage": 24,
        "startTopic": "Crimes de Trânsito em Geral e em Espécie"
      },
      "analytic": """A disciplina penal do trânsito combina normas gerais sancionatórias e tipos penais especiais destinados a tutelar a segurança viária coletiva e a vida humana nas vias terrestres.

### Disposições Gerais e Exceções à Lei 9.099/1995
Aplica-se aos crimes de trânsito a disciplina subsidiária do Código Penal e do Código de Processo Penal:
- **Incidência dos Juizados Especiais Criminais**: a regra geral do art. 291 prevê a aplicação da Lei 9.099/1995 às infrações penais de trânsito com menor potencial ofensivo;
- **Vedações Expressas (§ 1º do art. 291)**: afastam-se os benefícios da Lei 9.099/1995 (exigindo-se inquérito policial e impossibilitando transação penal ou composição civil) nos crimes de lesão corporal culposa se o motorista estiver:
  1. Com a capacidade afetada por bebidas alcoólicas ou substâncias químicas inebriantes;
  2. Participando de racha, disputa ou competição não autorizada na via pública;
  3. Trafegando em velocidade superior à máxima admitida em mais de 50 km/h;
- **Inaplicabilidade da Prisão em Flagrante (art. 301)**: não se imporá prisão em flagrante nem se exigirá fiança ao motorista que, participando de sinistro com vítima, prestar pronto e integral socorro ao ofendido;
- **Penalidade de Suspensão do Direito de Dirigir (art. 293)**: tem vigência fixada entre **2 meses e 5 anos**, cominada isolada ou cumulativamente com penas carcerárias.

### Crimes em Espécie e Qualificadoras Gravosas
- **Homicídio Culposo na Direção (art. 302)**: punido com detenção de 2 a 4 anos. A pena é aumentada de 1/3 à metade se o agente não tiver CNH, praticar o ato sobre faixa de pedestres, deixar de prestar socorro ou conduzir transporte coletivo. O **§ 3º qualifica o homicídio** com reclusão de 5 a 8 anos se cometido sob influência alcoólica ou química;
- **Lesão Corporal Culposa (art. 303)**: detenção de 6 meses a 2 anos. O **§ 2º qualifica a conduta** com reclusão de 2 a 5 anos se resultar lesão grave ou gravíssima e o condutor estiver embriagado;
- **Proibição de Substituição por Penas Alternativas (art. 312-B)**: é vedada a conversão da pena privativa de liberdade em restritivas de direitos aos condenados pelos arts. 302, § 3º e 303, § 2º;
- **Embriaguez ao Volante (art. 306)**: tipifica conduzir com capacidade psicomotora alterada por álcool, aferida por índice alcóolico de ao menos seis decigramas por litro sanguíneo ou 0,3 miligrama por litro de ar alveolar. Trata-se de **crime formal e de perigo abstrato**, dispensando a ocorrência de direção perigosa concreta.

| Tipo Penal | Classificação Dogmática | Elemento Chave |
|---|---|---|
| Art. 302, § 3º | Homicídio culposo com embriaguez | Reclusão de 5 a 8 anos (sem penas restritivas) |
| Art. 303, § 2º | Lesão culposa grave com álcool | Reclusão de 2 a 5 anos (sem penas restritivas) |
| Art. 306 | Embriaguez ao volante | Perigo abstrato (0,3 mg/L ar ou 6 dg/L sangue) |
| Art. 309 | Direção inabilitada | Perigo concreto de dano (Súmula 720 STF) |
| Art. 310 | Entregar veículo a inabilitado | Perigo abstrato (Súmula 575 STJ) |

### Crimes de Fuga, Omissão e Perigo
- **Omissão de Socorro (art. 304)**: punida a abstenção de prestar socorro à vítima quando o motorista não foi o causador do evento letal ou lesivo;
- **Fuga do Local (art. 305)**: afastar-se o motorista do ponto de colisão para eximir-se de consequências jurídicas reparatórias ou sancionatórias. A constitucionalidade do tipo foi chancelada pelo STF no Tema 907;
- **Direção sem Habilitação (art. 309)**: constitui infração penal de **perigo concreto**, dependendo de demonstração de risco efetivo à coletividade (Súmula 720 do STF);
- **Entrega de Veículo a Inabilitado (art. 310)**: ceder veículo a quem não possui CNH configura **crime de perigo abstrato**, prescindindo de dano real (Súmula 575 do STJ).

### Para fixar
- A Lei 9.099/1995 não se aplica se houver embriaguez, racha ou excesso de velocidade acima de 50 km/h.
- O motorista que presta socorro integral à vítima não é preso em flagrante nem paga fiança.
- É proibido converter em penas restritivas o homicídio ou lesão grave culposa com embriaguez.
- A embriaguez ao volante do art. 306 é infração formal e de perigo abstrato.
- Dirigir sem habilitação somente configura crime se gerar perigo concreto de dano.
- Entregar veículo automotor a pessoa sem habilitação é crime de perigo abstrato.""",
      "synthetic": [
        "**Exceções à Lei 9.099**: embriaguez, racha e excesso veloz superior a 50 km/h impedem transação penal e exigem inquérito.",
        "**Vedação à prisão no socorro**: quem socorre integralmente a vítima no acidente não sofre flagrante nem paga fiança.",
        "**Suspensão temporária da CNH**: a inabilitação administrativa ou judicial para dirigir vigora pelo período de dois meses a cinco anos.",
        "**Embriaguez qualificada fatal**: homicídio sob embriaguez atrai reclusão de cinco a oito anos sem conversão em penas restritivas.",
        "**Perigo abstrato na embriaguez**: o art. 306 consuma-se pelo índice de 0,3 mg/L de ar alveolar sem exigir manobra arriscada.",
        "**Direção sem permissão**: conduzir sem CNH reclama geração de perigo concreto de dano conforme a Súmula 720 do STF.",
        "**Entrega irresponsável de veículo**: confiar a direção a condutor desabilitado é crime de perigo abstrato consoante Súmula 575 do STJ."
      ]
    }
  ]
}

Path("content/items/legislacao-penal-especial/a16.json").write_text(json.dumps(items_a16, ensure_ascii=False, indent=2), encoding="utf-8")
Path("content/summaries/legislacao-penal-especial/a16.json").write_text(json.dumps(summaries_a16, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved a16 files successfully.")
