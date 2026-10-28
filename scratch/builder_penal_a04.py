# -*- coding: utf-8 -*-
"""Builder for direito-penal a04 (items and summaries - 14 segments)."""
import json
import os

ITEMS_FILE = "content/items/direito-penal/a04.json"
SUMMARIES_FILE = "content/summaries/direito-penal/a04.json"

os.makedirs(os.path.dirname(ITEMS_FILE), exist_ok=True)
os.makedirs(os.path.dirname(SUMMARIES_FILE), exist_ok=True)

with open("content/segments/direito-penal.json", "r", encoding="utf-8") as f:
    all_segs = {s["id"]: s for s in json.load(f)["segments"]}

def get_fp(sid):
    s = all_segs[sid]
    return {"startPage": s["startPage"], "endPage": s["endPage"], "startTopic": s["startTopic"]}

# We will construct items_data and summaries_data
items_data = {
    "aula": "direito-penal/a04",
    "batch": "pcpe-bizu-direito-penal",
    "status": "DRAFT",
    "stage": "bizu",
    "segments": []
}

summaries_data = {
    "aula": "direito-penal/a04",
    "batch": "pcpe-summary-direito-penal",
    "status": "DRAFT",
    "segments": []
}

# -------------------------------------------------------------
# SEGMENT 01: Homicídio Simples e Privilegiado (p. 2-8)
# -------------------------------------------------------------
items_data["segments"].append({
    "id": "direito-penal/a04/s01",
    "bizu": {
        "summary": [
            "**Homicídio Simples (art. 121, caput)**: eliminação dolosa da vida de uma pessoa humana viva extrauterina cominada com pena de reclusão de seis a vinte anos.",
            "**Início e Fim da Vida Humana**: o início da proteção penal da vida da pessoa dá-se com o início do trabalho de parto; o término biológico afere-se pela cessação das atividades encefálicas.",
            "**Homicídio Privilegiado (art. 121, § 1º)**: causa legal obrigatória de diminuição da sanção corporal de um sexto a um terço.",
            "**Hipóteses de Privilégio**: relevante valor social (interesse da comunidade), relevante valor moral (sentimento nobre particular, como eutanásia compassiva) ou sob o domínio de violenta emoção logo em seguida a injusta provocação da vítima.",
            "**Domínio versus Influência de Emoção**: o privilégio exige o domínio absoluto da emoção que anuvia a razão; a mera influência emocional atua como atenuante genérica do artigo 65 do CP.",
            "**Requisito Temporal do Privilégio**: exige reação imediata, sem intervalo temporal prolongado que possibilite o resfriamento de ânimos entre a provocação da vítima e o ataque letal.",
            "**Natureza Subjetiva do Privilégio**: os motivos determinantes do privilégio são de natureza estritamente pessoal, não se comunicando a coautores no concurso de pessoas.",
            "**Hediondez e Homicídio Simples**: o homicídio simples, em regra, não é hediondo, tornando-se crime hediondo apenas quando praticado em atividade típica de grupo de extermínio."
        ],
        "teoria": [
            {
                "statement": "O homicídio praticado sob a influência de violenta emoção provocada pela vítima autoriza a incidência da causa de diminuição do homicídio privilegiado.",
                "isTrue": False,
                "explanation": "A causa especial de diminuição exige o domínio de violenta emoção; a mera influência configura atenuante genérica prevista no art. 65 do CP."
            },
            {
                "statement": "O reconhecimento do homicídio privilegiado pelo Conselho de Sentença impõe ao magistrado a diminuição obrigatória da reprimenda na dosimetria.",
                "isTrue": True,
                "explanation": "Trata-se de direito público subjetivo do réu, impondo decote compulsório da pena entre um sexto e um terço."
            },
            {
                "statement": "O relevante valor social do homicídio privilegiado vincula-se a interesses eminentemente individuais e sentimentos compassivos familiares do agente.",
                "isTrue": False,
                "explanation": "O relevante valor social atende a anseios coletivos da comunidade em geral; sentimentos nobres particulares configuram relevante valor moral."
            },
            {
                "statement": "O homicídio simples perpetrado sem concurso de agentes ostenta natureza de crime hediondo por força da gravidade abstrata da violação da vida.",
                "isTrue": False,
                "explanation": "O homicídio simples só atinge o rótulo hediondo se praticado em atividade típica de grupo de extermínio, ainda que por um só agente."
            }
        ],
        "revisao": [
            {
                "statement": "O privilégio decorrente do domínio de violenta emoção admite intervalo prolongado de reflexão entre a ofensa sofrida e a execução dos disparos.",
                "isTrue": False,
                "explanation": "A lei exige que a reação ocorra logo em seguida à injusta provocação, vedando represálias premeditadas após resfriamento anímico."
            },
            {
                "statement": "As circunstâncias atinentes ao motivo de relevante valor moral ostentam índole subjetiva, sendo incomunicáveis aos comparsas no concurso delitivo.",
                "isTrue": True,
                "explanation": "Circunstâncias subjetivas de caráter pessoal não se comunicam aos partícipes por força do art. 30 do Código Penal."
            },
            {
                "statement": "A morte encefálica constitui o marco biológico e científico legalmente adotado para a comprovação do término da vida humana.",
                "isTrue": True,
                "explanation": "A Lei dos Transplantes e a doutrina fixam a cessação definitiva das funções encefálicas como termo da existência da pessoa viva."
            },
            {
                "statement": "A eutanásia praticada a pedido de paciente desenganado com sofrimento intolerável consubstancia causa excludente de ilicitude no direito brasileiro.",
                "isTrue": False,
                "explanation": "No ordenamento penal nacional a eutanásia permanece fato típico e ilícito, podendo caracterizar homicídio privilegiado por valor moral."
            }
        ],
        "pointers": [
            {"topic": "Homicídio simples, balizas de pena e hediondez por extermínio", "pageRef": 3},
            {"topic": "Início da vida extrauterina e cessação encefálica", "pageRef": 4},
            {"topic": "Requisitos do homicídio privilegiado e distinção entre domínio e influência", "pageRef": 6},
            {"topic": "Incomunicabilidade dos motivos de privilégio no concurso de agentes", "pageRef": 8}
        ]
    }
})

summaries_data["segments"].append({
    "id": "direito-penal/a04/s01",
    "fingerprint": get_fp("direito-penal/a04/s01"),
    "analytic": """Este segmento inaugura a tutela da vida humana na Parte Especial do Código Penal, analisando os balizadores do homicídio simples, os marcos temporais de início e fim da existência biológica, os contornos do homicídio privilegiado e os reflexos penais do relevante valor social e moral.

### Homicídio simples e delimitação do objeto jurídico
O artigo 121, caput, do Código Penal incrimina a ação voluntária de ceifar a existência de outra pessoa humana (*matar alguém*), cominando reprimenda reclusiva de seis a vinte anos. O bem jurídico protegido consubstancia a vida humana extrauterina, direito fundamental indisponível que prevalece no topo do ordenamento jurídico constitucional.

O início da vida da pessoa sob a proteção do homicídio coincide com a deflagração do trabalho de parto (ruptura de membranas ou início das contrações expulsivas no parto normal, ou incisão abdominal na cesariana). Ataques lesivos anteriores a esse marco caracterizam o crime de aborto. O termo final da vida afere-se pelo critério da morte encefálica com cessação definitiva e irreversível das funções do tronco cerebral, conforme as diretrizes da Lei nº 9.434/1997.

Quanto ao regime de hediondez, o homicídio simples não figura no rol da Lei nº 8.072/1990, ressalvada a hipótese estrita em que é executado em atividade típica de grupo de extermínio, ainda que por um só indivíduo.

### Homicídio privilegiado: hipóteses e natureza jurídica
O artigo 121, § 1º, estabelece que se o agente comete o crime impelido por motivo de relevante valor social ou moral, ou sob o domínio de violenta emoção, logo em seguida a injusta provocação da vítima, o juiz pode reduzir a pena de um sexto a um terço. Trata-se de autêntica causa especial de diminuição de pena de aplicação compulsória:
- **Relevante Valor Social**: o móvel da conduta atende a interesses coletivos ou anseios preponderantes da comunidade (ex.: cidadão que elimina líder criminoso sanguinário que aterrorizava bairro isolado);
- **Relevante Valor Moral**: o motivo decorre de sentimentos nobres individuais e compreensíveis do autor (ex.: pai que pratica eutanásia compassiva para cessar dores atrozes de filho desenganado);
- **Domínio de Violenta Emoção Logo Após Provocação**: exige a concorrência concomitante de três requisitos:
  1. Estado de choque psíquico agudo que assuma o comando das ações do indivíduo (*domínio* e não simples influência);
  2. Injusta provocação desencadeada pela conduta da própria vítima (não se exige agressão física, bastando ato provocador injustificado);
  3. Reação imediata (*logo em seguida*), sob calor dos acontecimentos, sem espaço temporal para resfriamento anímico.

### Comunicabilidade e repercussão no Tribunal do Júri
Os motivos determinantes do privilégio guardam natureza estritamente subjetiva, vinculados à personalidade e à motivação interna do agente. Consoante a disciplina do artigo 30 do Código Penal, essas circunstâncias pessoais não se comunicam a eventuais comparsas no concurso de agentes.

No rito do Tribunal do Júri, caso os jurados respondam afirmativamente ao quesito do privilégio, o magistrado presidente fica obrigado a reduzir a sanção no patamar legal de um sexto a um terço na terceira etapa da dosimetria penal.

### Para fixar
- O homicídio simples protege a vida extrauterina desde a deflagração do parto até a morte encefálica.
- O homicídio simples só é hediondo se praticado em atividade típica de grupo de extermínio.
- O privilégio decorre de relevante valor social, relevante valor moral ou domínio de violenta emoção.
- O domínio emocional exige atuação incontinente logo em seguida à provocação injusta da vítima.
- A mera influência de emoção não qualifica privilégio, atuando como atenuante genérica do art. 65 do CP.
- O homicídio privilegiado constitui causa de diminuição com decote compulsório de um sexto a um terço.
- As circunstâncias subjetivas do privilégio são incomunicáveis no concurso de pessoas.
- A eutanásia no ordenamento brasileiro permanece conduta punível, amparada pelo privilégio por valor moral.""",
    "synthetic": [
        "**Homicídio Simples (art. 121)**: tutela a vida extrauterina desde as contrações do parto até a parada encefálica, com pena reclusiva ordinária de seis a vinte anos.",
        "**Hediondez no Homicídio Simples**: afasta-se a hediondez da figura básica ordinária, incidindo apenas quando praticado em atividade própria de grupo de extermínio.",
        "**Relevante Valor Social e Moral**: valor social atende a desígnios coletivos da comunidade; valor moral ampara-se em sentimentos nobres individuais de compaixão.",
        "**Domínio de Violenta Emoção**: demanda perturbação emocional aguda e reação letal imediata perante provocação injusta sem lapso temporal de resfriamento.",
        "**Influência versus Domínio**: a simples influência anímica atua como atenuante genérica; o domínio efetivo viabiliza a diminuição fracionária do privilégio.",
        "**Natureza Subjetiva do Privilégio**: por expressarem motivações estritamente pessoais do infrator, os fatores privilegiantes não se transferem a coautores.",
        "**Decote Obrigatório de Pena**: constatado o privilégio pelo Conselho de Sentença, impõe-se a diminuição sancionatória compulsória de um sexto a um terço."
    ]
})

# -------------------------------------------------------------
# SEGMENT 02: Homicídio Qualificado (p. 9-21)
# -------------------------------------------------------------
items_data["segments"].append({
    "id": "direito-penal/a04/s02",
    "bizu": {
        "summary": [
            "**Homicídio Qualificado (art. 121, § 2º)**: comina sanção severa de reclusão de doze a trinta anos em virtude de circunstâncias gravosas de motivação, meios ou modos de execução.",
            "**Hediondez Legal**: todas as modalidades de homicídio qualificado ostentam natureza de crime hediondo nos termos da Lei nº 8.072/1990.",
            "**Qualificadoras Subjetivas**: abrangem a motivação do agente, tais como motivo torpe (inciso I: repugnante, abjeto, mesquinho, mediante paga ou promessa de recompensa) e motivo fútil (inciso II: desproporcional, insignificante, desarrazoado).",
            "**Incompatibilidade entre Torpe e Fútil**: são qualificadoras de motivação excludentes entre si; a conduta é torpe ou fútil, não podendo cumular ambas no mesmo crime.",
            "**Ausência de Motivo e Futilidade**: a ausência de motivo apurado não se equipara automaticamente ao motivo fútil, sob pena de analogia prejudicial indevida.",
            "**Qualificadoras Objetivas de Meio**: inciso III (veneno, fogo, explosivo, asfixia, tortura ou outro meio insidioso ou cruel, ou de que possa resultar perigo comum).",
            "**Qualificadoras Objetivas de Modo**: inciso IV (traição, emboscada, dissimulação ou outro recurso que dificulte ou torne impossível a defesa do ofendido).",
            "**Conexão Teleológica e Consequencial (inciso V)**: matar para assegurar a execução de outro delito vindouro (teleológica) ou para assegurar ocultação, impunidade ou vantagem de crime passado (consequencial).",
            "**Homicídio Funcional (inciso VII)**: praticado contra membros das forças de segurança pública, Forças Armadas, sistema prisional ou seus cônjuges/parentes até o 3º grau em razão da função.",
            "**Emprego de Arma de Fogo Proibida/Restrita (inciso VIII)**: qualificadora objetiva caracterizada pelo uso de armamento de uso restrito ou proibido na execução letal.",
            "**Homicídio Contra Menor de 14 Anos (inciso IX)**: qualificadora autônoma pelo critério etário com causas de aumento específicas.",
            "**Homicídio Qualificado-Privilegiado**: perfeitamente admitido na jurisprudência quando concorrerem circunstância de privilégio subjetivo e qualificadora de natureza estritamente objetiva."
        ],
        "teoria": [
            {
                "statement": "O homicídio praticado mediante promessa de pagamento em dinheiro consubstancia circunstância qualificadora objetiva que se comunica compulsoriamente a todos os comparsas.",
                "isTrue": False,
                "explanation": "A paga ou promessa de recompensa é qualificadora de motivo torpe (índole subjetiva), só se comunicando se ingressar na esfera de volição do comparsa."
            },
            {
                "statement": "É pacificamente admitida a figura do homicídio qualificado-privilegiado quando concorrerem qualificadora objetiva de meio e motivo de relevante valor moral.",
                "isTrue": True,
                "explanation": "O STF e STJ admitem a concorrência entre privilégio (sempre subjetivo) e qualificadora de natureza objetiva (meio ou modo de execução)."
            },
            {
                "statement": "A ausência de motivação delitiva apurada na instrução criminal autoriza o reconhecimento automático da qualificadora do motivo fútil.",
                "isTrue": False,
                "explanation": "A jurisprudência veda equiparar a ausência de motivo ao motivo fútil, sendo este caracterizado pela flagrante desproporção evidente."
            },
            {
                "statement": "O homicídio funcional protege integrantes das corporações de segurança pública bem como seus parentes consanguíneos até o terceiro grau em razão do cargo.",
                "isTrue": True,
                "explanation": "O art. 121, § 2º, VII, abrange os agentes de segurança e cônjuges, companheiros ou parentes consanguíneos até o terceiro grau por motivação funcional."
            }
        ],
        "revisao": [
            {
                "statement": "O homicídio qualificado por emboscada e dissimulação perde o caráter de hediondez quando reconhecido o privilégio do relevante valor social.",
                "isTrue": True,
                "explanation": "A jurisprudência dominante assenta que o homicídio híbrido qualificado-privilegiado não ostenta natureza de crime hediondo."
            },
            {
                "statement": "A qualificadora da conexão teleológica incide quando o agente comete o homicídio para assegurar a impunidade de infração penal cometida no passado.",
                "isTrue": False,
                "explanation": "A garantia de impunidade de delito pretérito traduz conexão consequencial; conexão teleológica visa assegurar a prática de crime futuro."
            },
            {
                "statement": "O emprego de arma de fogo de uso permitido afasta a incidência da qualificadora específica do inciso VIII do parágrafo segundo do artigo 121.",
                "isTrue": True,
                "explanation": "A qualificadora do inciso VIII restringe-se estritamente ao emprego de armas de fogo de uso restrito ou proibido."
            },
            {
                "statement": "O motivo torpe e o motivo fútil podem ser cumulados conjuntamente na pronúncia como qualificadoras aplicáveis ao mesmo assassinato.",
                "isTrue": False,
                "explanation": "Motivo torpe e motivo fútil são ontologicamente incompatíveis, não podendo incidir de forma simultânea sobre a mesma ação homicida."
            }
        ],
        "pointers": [
            {"topic": "Homicídio qualificado, balizas de pena e rol hediondo", "pageRef": 10},
            {"topic": "Qualificadoras subjetivas de motivo torpe e fútil", "pageRef": 13},
            {"topic": "Qualificadoras objetivas de meio e modo e conexão de crimes", "pageRef": 16},
            {"topic": "Homicídio funcional contra agentes da segurança e familiares", "pageRef": 19},
            {"topic": "Homicídio qualificado-privilegiado e afastamento de hediondez", "pageRef": 21}
        ]
    }
})

summaries_data["segments"].append({
    "id": "direito-penal/a04/s02",
    "fingerprint": get_fp("direito-penal/a04/s02"),
    "analytic": """Este segmento detalha as circunstâncias qualificadoras do delito de homicídio elencadas no artigo 121, § 2º, do Código Penal, analisando sua taxonomia doutrinária em subjetivas e objetivas, as hipóteses de conexão delitiva, o homicídio funcional e as balizas do homicídio qualificado-privilegiado.

### Qualificadoras subjetivas: torpeza e futilidade
O homicídio qualificado comina pena de reclusão de doze a trinta anos e ostenta natureza hedionda obrigatória. As qualificadoras dividem-se quanto à sua essência em subjetivas (atinentes aos motivos internos do agente) e objetivas (atinentes aos meios e modos mecânicos de execução):
- **Motivo Torpe (inciso I)**: motivo vil, abjeto, ignóbil ou repugnante que suscita profunda repulsa moral na comunidade. Abrange a prática delitiva mediante paga ou promessa de recompensa (*homicídio mercenário ou por mandato*). A paga comunica-se ao mandante e ao executor desde que do plano de ambos participe o elemento pecuniário;
- **Motivo Fútil (inciso II)**: motivo insignificante, mesquinho, flagrantemente desproporcional à gravidade da conduta letal desencadeada (ex.: matar alguém por briga de trânsito banal ou cobrança de dívida de valor irrisório).

As qualificadoras de motivo torpe e fútil são **mutuamente excludentes**: uma conduta não pode ser qualificada concomitantemente por ambas. Ademais, a jurisprudência sumulada repele a tentativa de equiparar a simples ausência de motivo demonstrado ao motivo fútil, visto que a ausência de motivo não autoriza a agravação.

### Qualificadoras objetivas de meio e de modo de execução
- **Meio Insidioso ou Cruel, ou de Perigo Comum (inciso III)**:
  - *Veneno*: substância química ou biológica insidiosa ministrada dissimuladamente;
  - *Fogo e Explosivo*: meios de destruição em massa dotados de poder vulnerante difuso;
  - *Asfixia*: supressão mecânica ou química da função respiratória (enforcamento, afogamento, esganadura);
  - *Tortura ou Meio Cruel*: causa sofrimento desnecessário, desmedido e atroz à vítima antes da morte;
  - *Perigo Comum*: meio executório apto a colocar em risco indeterminadas pessoas (detonação em via pública).
- **Recurso que Dificulte ou Torne Impossível a Defesa (inciso IV)**:
  - *Traição*: ataque pérfido com quebra de prévia relação de confiança;
  - *Emboscada*: tocaia ou espreita física dissimulada aguardando a passagem da vítima;
  - *Dissimulação*: ocultação do intento homicida sob falsa atitude amistosa;
  - *Fórmula genérica*: ataque inesperado e repentino pelas costas desprovido de qualquer chance defensiva.
- **Conexão Criminosa (inciso V)**: praticado para assegurar a execução de outro delito futuro (*conexão teleológica*) ou para garantir a ocultação, impunidade ou vantagem econômica de infração pretérita (*conexão consequencial*).

### Homicídio funcional e a figura qualificada-privilegiada
O inciso VII positiva o **Homicídio Funcional**: praticado contra integrantes das Forças Armadas, das polícias civis, militares, federal e rodoviária, penais, guardas municipais ou agentes do sistema prisional no exercício da função ou em decorrência dela, estendendo-se a tutela a cônjuges, companheiros ou parentes consanguíneos até o terceiro grau em razão dessa condição funcional.

O ordenamento contempla ainda o emprego de arma de fogo de uso restrito ou proibido (inciso VIII) e o assassinato contra menor de 14 anos (inciso IX).

Por fim, consolidou-se na doutrina e jurisprudência dos tribunais superiores a admissibilidade do **Homicídio Qualificado-Privilegiado**: ocorre quando coexistem no mesmo fato uma circunstância atinente ao privilégio (que é sempre subjetiva: valor social, moral ou violenta emoção) e uma qualificadora de natureza estritamente objetiva (meio cruel, asfixia, emboscada). O homicídio híbrido assim reconhecido afasta o regime de hediondez, privilegiando o caráter benevolente do veredito popular.

### Para fixar
- O homicídio qualificado possui pena de doze a trinta anos e ostenta natureza hedionda integral.
- Motivo torpe e motivo fútil são circunstâncias subjetivas mutuamente excludentes na denúncia.
- A falta de motivo comprovado nos autos não pode ser equiparada juridicamente ao motivo fútil.
- O meio cruel é qualificador objetivo marcado pelo sofrimento físico desnecessário e martirizante.
- A traição e a emboscada constituem modos objetivos que suprimem a capacidade de reação do ofendido.
- A conexão teleológica visa viabilizar delito futuro; a conexão consequencial busca encobrir crime passado.
- O homicídio funcional tutela agentes das forças de segurança e parentes consanguíneos até 3º grau.
- O homicídio qualificado-privilegiado demanda qualificadora objetiva e privilégio subjetivo, afastando a hediondez.""",
    "synthetic": [
        "**Homicídio Qualificado (art. 121, § 2º)**: comina reclusão de doze a trinta anos e enquadra-se como infração hedionda por imperativo da lei especial repressiva.",
        "**Qualificadoras Subjetivas**: abrangem a motivação torpe abjeta repugnante e a motivação fútil desproporcional, revelando-se inconciliáveis entre si no mesmo fato.",
        "**Ausência de Motivação**: a carência de identificação do motivo fático não legitima o reconhecimento mecânico da futilidade típica do comportamento.",
        "**Qualificadoras Objetivas de Meio**: recaem sobre o emprego de veneno dissimulado, asfixia, explosivo, fogo e métodos que submetam a vítima a martírio cruel.",
        "**Qualificadoras de Modo**: traição, emboscada oculta e ardis mecânicos que anulem de forma imprevisível a capacidade reativa de defesa da vítima.",
        "**Conexão Teleológica e Consequencial**: matar para propiciar delito futuro traduz conexão teleológica; matar para encobrir delito pretérito traduz conexão consequencial.",
        "**Homicídio Funcional**: tutela agentes de segurança pública e parentes consanguíneos até o 3º grau atingidos em virtude da atividade institucional.",
        "**Figura Qualificada-Privilegiada**: harmoniza qualificadora objetiva de meio com privilégio subjetivo, descaracterizando a índole hedionda originária."
    ]
})

# Write current partial to disk
with open(ITEMS_FILE, "w", encoding="utf-8") as f:
    json.dump(items_data, f, ensure_ascii=False, indent=2)
print("Saved partial items a04")

with open(SUMMARIES_FILE, "w", encoding="utf-8") as f:
    json.dump(summaries_data, f, ensure_ascii=False, indent=2)
print("Saved partial summaries a04")
