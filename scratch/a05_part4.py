# -*- coding: utf-8 -*-
"""Part 4 for a05: s12, s13, s14 (Fraudes especiais, Receptação e Escusas - rigorously paraphrased)."""

def get_part4_data(get_fp):
    items = []
    summaries = []

    # -------------------------------------------------------------
    # SEGMENT 12: Fraudes Especiais e Ativos Virtuais (p. 123-138)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a05/s12",
        "bizu": {
            "summary": [
                "**Disposição de Coisa Alheia como Própria (art. 171, § 2º, I)**: vender, permutar, doar ou dar em garantia coisa móvel ou imóvel que sabe pertencer a terceiro.",
                "**Alienação Fraudulenta de Coisa Própria (inciso II)**: alienar bem próprio inalienável, gravado de ônus real ou litigioso, ocultando essa circunstância do adquirente.",
                "**Fraude para Recebimento de Seguro (inciso V)**: destruir coisa própria ou lesar o próprio corpo para auferir indevidamente o valor de apólice de seguro.",
                "**Fraude no Pagamento por Cheque (inciso VI)**: emissão dolosa de ordem bancária de pagamento sem lastro financeiro disponível junto à instituição financeira sacada.",
                "**Súmula 246 do STF**: comprovado não ter havido fraude na emissão, descaracteriza-se a tipicidade do crime de cheque sem fundos.",
                "**Súmula 554 do STF**: o ressarcimento do cheque sem fundos antes do recebimento da denúncia obsta a ação penal extinguindo a punibilidade.",
                "**Cheque Pré-Datado**: a emissão de cheque pré-datado desvirtua sua natureza de ordem à vista, descaracterizando o art. 171, § 2º, VI, na jurisprudência.",
                "**Fraude com Ativos Virtuais (art. 171-A)**: organizar, gerir ou ofertar carteiras de criptoativos visando obter vantagem ilícita mediante fraude financeira (Lei 14.478/2022).",
                "**Duplicata Simulada (art. 172)**: expedição de títulos de crédito mercantis desprovidos de lastro real em vendas concretizadas ou serviços executados."
            ],
            "teoria": [
                {
                    "statement": "O pagamento voluntário do valor de cheque emitido sem fundos realizado antes do recebimento da denúncia criminal extingue a punibilidade.",
                    "isTrue": True,
                    "explanation": "A Súmula 554 do STF assenta, a contrario sensu, que o adimplemento tempestivo do cheque antes da denúncia obsta a instauração da ação penal."
                },
                {
                    "statement": "A emissão desprovida de fraude inicial de cheque pré-datado devolvido por insuficiência de fundos consuma o crime do art. 171, § 2º, VI.",
                    "isTrue": False,
                    "explanation": "O STJ firmou que a emissão de cheque pré-datado desnaturado como garantia de dívida descaracteriza o delito específico de fraude por cheque."
                },
                {
                    "statement": "O agente que queima o próprio automóvel visando receber a indenização da seguradora comete a fraude tipificada no art. 171, § 2º, V, do CP.",
                    "isTrue": True,
                    "explanation": "O tipo do inciso V criminaliza a destruição total ou parcial de bem próprio com o propósito de haver o valor da indenização de seguro."
                },
                {
                    "statement": "O crime de emissão de duplicata simulada exige que o título de crédito mercantil seja devidamente protestado em cartório para sua consumação.",
                    "isTrue": False,
                    "explanation": "O art. 172 é crime formal que se consuma no exato momento da emissão ou aceite da duplicata que não espelhe venda real ou serviço executado."
                }
            ],
            "revisao": [
                {
                    "statement": "A mutilação corporal deliberada praticada pelo próprio segurado visando receber indenização securitária amolda-se ao estelionato qualificado.",
                    "isTrue": True,
                    "explanation": "O art. 171, § 2º, V, segunda parte, prevê expressamente a autolesão corporal voltada ao recebimento ilícito de valor de seguro."
                },
                {
                    "statement": "O ressarcimento financeiro de cheque sem provisão promovido após a prolação da sentença condenatória irrecorrível extingue a punibilidade.",
                    "isTrue": False,
                    "explanation": "Pela Súmula 554 do STF, o pagamento posterior ao recebimento da denúncia não obsta o curso nem extingue a punibilidade da ação penal."
                },
                {
                    "statement": "O tipo penal do artigo 171-A pune esquemas fraudulentos com criptomoedas e carteiras digitais de ativos virtuais com reclusão de quatro a oito anos.",
                    "isTrue": True,
                    "explanation": "A Lei 14.478/2022 inseriu o art. 171-A cominando reclusão de quatro a oito anos e multa para fraudes estruturadas com ativos virtuais."
                },
                {
                    "statement": "A alienação onerosa de imóvel próprio que se encontra gravado com hipoteca prescinde de advertência ao comprador na negociação preliminar.",
                    "isTrue": False,
                    "explanation": "Silenciar sobre o gravame de hipoteca vendendo a coisa como livre constitui o crime expresso do art. 171, § 2º, II, do Código Penal."
                }
            ],
            "pointers": [
                {"topic": "Figuras equiparadas de estelionato no art. 171, § 2º", "pageRef": 124},
                {"topic": "Fraude de seguros e autolesão no inciso V", "pageRef": 127},
                {"topic": "Fraude no pagamento por cheque e Súmulas 246 e 554 do STF", "pageRef": 130},
                {"topic": "Fraude com ativos virtuais e criptomoedas no art. 171-A", "pageRef": 134},
                {"topic": "Duplicata simulada e tutela do comércio no art. 172", "pageRef": 137}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a05/s12",
        "fingerprint": get_fp("direito-penal/a05/s12"),
        "analytic": """Este segmento esmiúça o catálogo das fraudes especiais equiparadas ao estelionato previstas no artigo 171, § 2º, do Código Penal, analisando os contornos da fraude de cheques, a novidade legislativa da fraude com ativos virtuais (artigo 171-A) e o delito de duplicata simulada.

### Modalidades equiparadas de estelionato (artigo 171, § 2º)
O parágrafo 2º estende as sanções básicas do estelionato a condutas fraudulentas típicas discriminadas:
1. *Disposição de Coisa Alheia como Própria (inciso I)*: o agente vende, permuta, aluga ou oferece em hipoteca bem pertencente a terceiro como se seu fosse, ludibriando o adquirente de boa-fé;
2. *Alienação Fraudulenta de Coisa Própria (inciso II)*: alienação de coisa inalienável, hipotecada ou litigiosa, silenciando dolosamente sobre a cláusula restritiva perante o comprador;
3. *Defraudação de Penhor (inciso III)*: defraudação ou desvio de bem móvel gravado com penhor civil mercantil;
4. *Fraude na Entrega de Coisa (inciso IV)*: alteração da substância, pureza ou quantidade da mercadoria prometida no negócio jurídico;
5. *Fraude para Recebimento de Seguro (inciso V)*: destruição deliberada de bem próprio ou autolesão corporal intencional executada para receber a indenização prevista na apólice de seguro privada;
6. *Fraude no Pagamento por Meio de Cheque (inciso VI)*: emissão de ordem bancária sem suficiente provisão de fundos em poder da instituição sacada ou sustação fraudulenta imotivada do pagamento.

### A jurisprudência sumulada e a dinâmica dos cheques
A criminalização da emissão de cheques sem fundos subordina-se a orientações jurisprudenciais consolidadas:
- **Súmula 246 do STF**: demonstrada a boa-fé e ausência de fraude inicial na emissão, descaracteriza-se a tipicidade do crime de cheque sem fundos;
- **Súmula 554 do STF**: o adimplemento tempestivo da cártula antes de recebida a peça acusatória penal obsta a persecução criminal extinguindo a punibilidade. Em contrapartida, se o pagamento ocorrer após a denúncia ter sido formalmente recebida em juízo, o processo penal prossegue normalmente;
- **Cheque Pré-Datado**: a entrega de cártula com data futura estipulada expressamente entre credor e devedor converte a ordem de pagamento à vista em garantia de dívida a prazo, afastando a tipicidade do artigo 171, § 2º, VI, na esteira dos precedentes consolidados do Superior Tribunal de Justiça.

### Fraude com ativos virtuais e criptomoedas (artigo 171-A)
Introduzido pela Lei nº 14.478/2022 (Marco Legal dos Criptoativos), o artigo 171-A comina **reclusão de quatro a oito anos e multa** a quem organiza, gerencia, oferta ou distribui carteiras ou intermedeia operações com **ativos virtuais, valores mobiliários ou ativos financeiros digitais**, induzindo ou mantendo investidores em erro mediante artifícios fraudulentos para auferir vantagem ilícita (esquemas de pirâmides financeiras virtuais com criptomoedas).

A competência penal fixa-se perante a Justiça Federal quando as manobras com criptoativos lesarem o Sistema Financeiro Nacional ou envolverem transnacionalidade de capitais.

### Duplicata simulada (artigo 172)
O artigo 172 comina detenção de dois a quatro anos e multa a quem emite títulos mercantis fictícios sem correspondência com compras reais ou serviços concretos. Trata-se de crime formal que atinge a consumação no instante de sua expedição mercantil, prescindindo de circulação ou protesto cambial em cartório.

### Para fixar
- Dispor de patrimônio alheio como se fosse titularidade própria configura estelionato equiparado.
- Silenciar sobre hipoteca ou penhor ao vender coisa própria tipifica o art. 171, § 2º, II.
- A autolesão física praticada para recebimento de indenização securitária amolda-se ao inciso V.
- A Súmula 554 do STF extingue a punibilidade do cheque sem fundos pago antes do recebimento da denúncia.
- A emissão de cheque pré-datado descaracteriza a fraude específica perante a orientação do STJ.
- O art. 171-A pune fraudes estruturadas com criptoativos com reclusão de quatro a oito anos.
- A fraude com ativos virtuais atrai a competência federal se houver transnacionalidade lesiva.
- A duplicata simulada é crime formal que se consuma no instante de sua expedição sem lastro comercial.""",
        "synthetic": [
            "**Fraudes Equiparadas (§ 2º)**: alcançam a venda enganosa de bens de terceiros, ocultação de gravames e simulação fraudulenta na entrega mercantil.",
            "**Fraude de Seguros**: incrimina a autolesão corporal ou queima voluntária de veículos para percepção ilegítima da apólice indenizatória contratada.",
            "**Cheque sem Provisão**: conduta dolosa que desrespeita a solvência cartular subordinando-se à comprovação da má-fé no momento da emissão.",
            "**Súmula 554 do STF**: assegura a extinção da punibilidade quando o débito do cheque for adimplido anteriormente ao recebimento da peça acusatória.",
            "**Cheque Pré-Datado**: mutação convencional da cártula em promessa de pagamento futuro descaracterizando a infração penal por falta de fraude.",
            "**Criptoativos no Art. 171-A**: reprimenda de quatro a oito anos repreendendo pirâmides e desvios operados por carteiras de moedas virtuais.",
            "**Duplicata Simulada (art. 172)**: tutela a higidez do crédito comercial vedando a circulação de títulos cambiais sem respaldo de entrega de mercadoria.",
            "**Consumação Formal do Art. 172**: perfaz-se de plano com a simples expedição da fatura mercantil fictícia desprovida de lastro econômico real."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 13: Receptação e Escusas Absolutórias (p. 139-145)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a05/s13",
        "bizu": {
            "summary": [
                "**Receptação Dolosa Simples (art. 180, caput)**: aquisição, guarda, condução ou ocultação de patrimônio com ciência inequívoca de sua prévia origem criminosa ilícita.",
                "**Receptação Própria versus Imprópria**: receptação própria recai sobre conduta direta do agente; receptação imprópria traduz influir para que terceiro de boa-fé adquira a coisa.",
                "**Receptação Qualificada (art. 180, § 1º)**: praticada no exercício de atividade comercial ou industrial (inclusive informal ou clandestina), punida com reclusão de três a oito anos.",
                "**Elemento Subjetivo no § 1º**: a norma utiliza a fórmula deve saber ser produto de crime, bastando o dolo eventual na atividade comercial.",
                "**Receptação Culposa (art. 180, § 3º)**: adquirir ou receber coisa que, pela desproporção do preço ou condição de quem oferece, deve presumir-se criminosa (detenção de 1 mês a 1 ano).",
                "**Autonomia da Receptação (art. 180, § 4º)**: subsiste a punibilidade da conduta receptadora mesmo que o autor do delito originário reste desconhecido ou inimputável.",
                "**Escusas Absolutórias (art. 181)**: isenção integral de pena nos crimes patrimoniais sem violência cometidos contra cônjuge na constância do casamento ou ascendentes/descendentes.",
                "**União Estável**: o STF e STJ estendem expressamente a imunidade do art. 181, I, aos companheiros em união estável heteroafetiva ou homoafetiva.",
                "**Imunidades Relativas (art. 182)**: crimes patrimoniais sem violência contra cônjuge separado judicialmente, irmão, ou tio/sobrinho coabitante exigem representação.",
                "**Inaplicabilidade das Imunidades (art. 183)**: não se aplicam se o crime envolve violência à pessoa (roubo), ao partícipe estranho ou se a vítima tiver 60 anos ou mais."
            ],
            "teoria": [
                {
                    "statement": "A receptação qualificada perpetrada no comércio clandestino de peças automotivas comina pena mais severa admitindo a punição a título de dolo eventual.",
                    "isTrue": True,
                    "explanation": "O art. 180, § 1º, pune com reclusão de três a oito anos quem atua em atividade mercantil se a conduta evidenciar que *deve saber* da origem criminosa."
                },
                {
                    "statement": "O filho que comete furto simples de joias pertencentes à sua mãe idosa de sessenta e dois anos de idade desfruta da imunidade penal absoluta do art. 181.",
                    "isTrue": False,
                    "explanation": "O art. 183, III, inserido pelo Estatuto do Idoso, afasta peremptoriamente a aplicação de qualquer escusa absolutória contra vítima com 60 anos ou mais."
                },
                {
                    "statement": "A absolvição formal do autor do crime de furto originário por inimputabilidade afasta a punibilidade do receptador que adquiriu os bens ilícitos.",
                    "isTrue": False,
                    "explanation": "O art. 180, § 4º, consagra a autonomia da receptação: é punível ainda que isento de pena ou desconhecido o autor do crime antecedente."
                },
                {
                    "statement": "A escusa absolutória que beneficia o cônjuge no furto doméstico não se comunica ao comparsa estranho à família que participou da subtração.",
                    "isTrue": True,
                    "explanation": "O art. 183, II, do Código Penal estatui que a imunidade patrimonial não aproveita ao estranho que participa do crime."
                }
            ],
            "revisao": [
                {
                    "statement": "A receptação de bem subtraído mediante emprego de violência física com arma de fogo pode ser acobertada pelas escusas absolutórias do art. 181.",
                    "isTrue": False,
                    "explanation": "O art. 183, I, veda taxativamente a aplicação das imunidades absolutórias em qualquer delito praticado com emprego de violência ou grave ameaça."
                },
                {
                    "statement": "A receptação culposa admite a concessão de perdão judicial pelo magistrado caso o agente seja primário e as circunstâncias sejam favoráveis.",
                    "isTrue": True,
                    "explanation": "O art. 180, § 5º, autoriza o juiz a deixar de aplicar a pena na receptação culposa ao réu primário quando o valor da coisa for diminuto."
                },
                {
                    "statement": "O irmão que pratica furto de dinheiro contra outro irmão com quem reside subordina-se à ação penal pública condicionada à representação.",
                    "isTrue": True,
                    "explanation": "O art. 182, II, estabelece que o delito patrimonial praticado em desfavor de irmão somente se procede mediante representação do ofendido."
                },
                {
                    "statement": "O indivíduo que comete o crime de roubo e posteriormente comercializa a res furtiva com terceiro responde por roubo e receptação dolosa em concurso material.",
                    "isTrue": False,
                    "explanation": "A comercialização pelo próprio autor do crime originário constitui post factum impunível, respondendo ele unicamente pelo crime de roubo."
                }
            ],
            "pointers": [
                {"topic": "Receptação dolosa simples, núcleos e distinção de receptação imprópria", "pageRef": 140},
                {"topic": "Receptação qualificada mercantil e dolo eventual no art. 180, § 1º", "pageRef": 142},
                {"topic": "Autonomia do delito de receptação e prescindibilidade de punição do autor", "pageRef": 143},
                {"topic": "Escusas absolutórias, imunidades absolutas e relativas nos arts. 181 e 182", "pageRef": 144},
                {"topic": "Vedações do art. 183, violência e tutela do idoso", "pageRef": 145}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a05/s13",
        "fingerprint": get_fp("direito-penal/a05/s13"),
        "analytic": """Este segmento estuda as modalidades do crime de receptação catalogadas no artigo 180 do Código Penal e o regime das imunidades patrimoniais familiares disciplinadas nos artigos 181 a 183.

### Receptação simples e qualificada (artigo 180)
O artigo 180 tutela a segurança patrimonial repreendendo a circulação de bens obtidos por vias delituosas:
- **Receptação Dolosa Simples (caput)**: comina reclusão de um a quatro anos e multa. Subdivide-se em:
  - *Receptação Própria*: adquirir, receber, transportar, conduzir ou ocultar patrimônio sabidamente derivado de infração penal anterior (exige dolo direto);
  - *Receptação Imprópria*: influir conscientemente para que terceiro de boa-fé adquira, receba ou oculte o bem criminoso;
- **Receptação Qualificada (§ 1º)**: praticada no exercício de atividade comercial ou industrial, inclusive clandestina ou residencial (*desmanches de veículos*), cominando reclusão severa de **três a oito anos e multa**. O tipo utiliza a locução *deve saber ser produto de crime*, consolidando a punibilidade a título de **dolo eventual** com sanção superior à do dolo direto da forma simples;
- **Receptação Culposa (§ 3º)**: adquirir ou receber coisa que, pela desproporção manifesta entre o preço e o valor de mercado ou pelas condições suspeitas de quem a oferece, impunha o dever de presumir a origem criminosa (detenção de um mês a um ano ou perdão judicial no § 5º);
- **Autonomia da Receptação (§ 4º)**: a receptação consubstancia crime acessório que exige um crime antecedente. Contudo, goza de **autonomia processual**: é punível ainda que o autor do crime originário seja desconhecido, foragido ou isento de pena (como na inimputabilidade).

### Escusas absolutórias e imunidades patrimoniais (artigos 181 a 183)
O ordenamento busca preservar a harmonia da paz familiar nos conflitos puramente patrimoniais desprovidos de violência:
- **Imunidades Absolutas (artigo 181)**: o agente é isento de pena nos crimes patrimoniais sem violência cometidos em prejuízo de:
  1. Cônjuge, na constância da sociedade matrimonial (plenamente estendida à **união estável** pela jurisprudência);
  2. Ascendentes (pais, avós) ou descendentes (filhos, netos), sem distinção de filiação;
- **Imunidades Relativas (artigo 182)**: a ação penal converte-se em pública condicionada à **representação** se cometida em prejuízo de:
  1. Cônjuge desquitado ou separado judicialmente;
  2. Irmão, legítimo ou ilegítimo;
  3. Tio ou sobrinho com quem o agente **coabita** no mesmo lar;
- **Inaplicabilidade das Imunidades (artigo 183)**: afasta-se peremptoriamente a incidência de qualquer escusa:
  - Se o crime for praticado com **violência física ou grave ameaça à pessoa** (roubo e extorsão);
  - Ao estranho (comparsa partícipe) que concorre para o delito patrimonial;
  - Se o crime for praticado contra pessoa que já tenha completado sessenta anos de vida (Estatuto do Idoso).

### Para fixar
- A receptação simples exige conhecimento pleno da origem criminosa com pena de 1 a 4 anos.
- A receptação qualificada mercantil admite dolo eventual cominando reclusão de 3 a 8 anos.
- A receptação culposa pune a negligência perante a desproporção de preço com detenção de 1 mês a 1 ano.
- Pelo art. 180, § 4º, a receptação é autônoma em relação à punição do autor do crime primitivo.
- O art. 181 isenta de pena o crime patrimonial sem violência contra cônjuge e pais/filhos.
- A imunidade do cônjuge aplica-se amplamente aos companheiros em união estável comprovada.
- O art. 182 exige representação no furto contra irmão ou tio com quem coabite na mesma morada.
- As imunidades familiares não se aplicam a crimes com violência nem contra pessoa com 60 anos ou mais.""",
        "synthetic": [
            "**Receptação Dolosa (art. 180)**: acolhimento ou transporte consciente de patrimônio espúrio prevendo modalidades própria direta e imprópria por intermediação.",
            "**Receptação Mercantil (§ 1º)**: reprime o comércio irregular com sanção de três a oito anos chancelando a responsabilização por dolo eventual presumido.",
            "**Receptação Culposa**: negligência fática assentada na aquisição de coisas sob vil valor de mercado sem cautelas mínimas ordinárias de procedência.",
            "**Autonomia Consecutiva**: a persecução do receptador independe formalmente da localização ou responsabilização penal do autor da infração matriz.",
            "**Imunidade Absoluta (art. 181)**: isenta de sanção penal conflitos patrimoniais desprovidos de violência deflagrados entre cônjuges e parentes consanguíneos retos.",
            "**Extensão à Convivência**: o STF e STJ equiparam os conviventes em união estável à tutela absolutória legal conferida aos cônjuges casados.",
            "**Imunidade Relativa (art. 182)**: exige representação para viabilizar ação penal em desvios patrimoniais cometidos contra irmãos e tios coabitantes.",
            "**Vedações do Art. 183**: rechaça imunidades em roubos coativos armados, estendendo plena punibilidade em delitos lesivos praticados contra idosos."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 14: Receptação de Animal e Disposições Finais (p. 146-157)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a05/s14",
        "bizu": {
            "summary": [
                "**Receptação de Semovente de Produção (art. 180-A)**: aquisição, depósito ou transporte comercial de animais de criação furtados, ainda que já abatidos ou esquartejados.",
                "**Pena Cominada**: reclusão de dois a cinco anos e multa, incidindo ainda que o animal esteja abatido ou fracionado em cortes de carne.",
                "**Elemento Subjetivo do Art. 180-A**: a norma utiliza deve saber ser produto de crime, harmonizando o dolo eventual ao propósito de comercialização industrial ou pecuária.",
                "**Finalidade Comercial ou Produtiva**: exige que a posse do semovente destine-se à atividade produtiva ou mercantil agropecuária.",
                "**Distinção Abigeato e Receptação de Animal**: o art. 155, § 6º, pune quem furta o animal; o art. 180-A criminaliza o elo receptador que adquire o rebanho subtraído.",
                "**Post Factum Impunível**: quem subtrai o gado no abigeato e o transporta para comercialização responde exclusivamente pelo furto qualificado.",
                "**Violência Doméstica Patrimonial**: o STJ firmou a tese de que a violência patrimonial contra a mulher afasta as escusas absolutórias do art. 181 do CP.",
                "**Pena Pecuniária e Reparação Civil**: os crimes contra o patrimônio admitem imposição de valor mínimo para reparação de danos civis no édito sentencial penal condenatório."
            ],
            "teoria": [
                {
                    "statement": "O crime de receptação de animal tipificado no artigo 180-A comina pena de reclusão e abrange a conduta ainda que o semovente seja adquirido já abatido.",
                    "isTrue": True,
                    "explanation": "O art. 180-A criminaliza expressamente a conduta ainda que o semovente esteja *abatido ou dividido em partes* no momento da receptação."
                },
                {
                    "statement": "O comerciante de carnes que adquire carcaças de bovinos de procedência clandestina para abastecer açougue responde por receptação culposa mitigada.",
                    "isTrue": False,
                    "explanation": "A conduta enquadra-se no art. 180-A ou art. 180, § 1º, que cominam sanções reclusivas severas em face do exercício comercial irregular."
                },
                {
                    "statement": "A jurisprudência recente do STJ assentou que a escusa absolutória do art. 181 não prevalece sobre condutas caracterizadas como violência patrimonial na Lei Maria da Penha.",
                    "isTrue": True,
                    "explanation": "O STJ firmou que a incidência da Lei Maria da Penha na violência patrimonial contra mulher afasta a isenção de pena do art. 181 do Código Penal."
                },
                {
                    "statement": "O tipo do artigo 180-A tutela semoventes domesticáveis de produção bem como espécimes da fauna silvestre mantidos ilegalmente para exposição.",
                    "isTrue": False,
                    "explanation": "O art. 180-A restringe-se taxativamente aos semoventes domesticáveis de produção e corte pecuário (bovinos, caprinos, equinos)."
                }
            ],
            "revisao": [
                {
                    "statement": "A receptação de animal exige para sua conformação a finalidade específica de produção ou de comercialização do semovente receptado.",
                    "isTrue": True,
                    "explanation": "O art. 180-A exige o especial fim de agir consistente na destinação da res furtiva para a produção agropastoril ou comercialização mercantil."
                },
                {
                    "statement": "O autor do crime de furto de semoventes responde em concurso material pelo delito autônomo de receptação de animal ao ocultar o gado em seu sítio.",
                    "isTrue": False,
                    "explanation": "A ocultação e guarda do bem pelo próprio autor da subtração consubstancia mero exaurimento impunível do furto originário consumado."
                },
                {
                    "statement": "A compra isolada de carne bovina sem nota fiscal por consumidor final para churrasco familiar subsume-se formalmente ao tipo do art. 180-A.",
                    "isTrue": False,
                    "explanation": "O consumidor final não atua com escopo de produção ou comercialização, podendo responder por receptação comum (art. 180) se comprovado dolo."
                },
                {
                    "statement": "O delito de receptação de animal comina pena alternativa exclusiva de prestação de serviços à comunidade sem imposição de reclusão.",
                    "isTrue": False,
                    "explanation": "O art. 180-A comina sanção severa de reclusão de dois a cinco anos e multa, repelindo penas alternativas isoladas na condenação."
                }
            ],
            "pointers": [
                {"topic": "Receptação de semovente domesticável no art. 180-A e Lei 13.330/2016", "pageRef": 147},
                {"topic": "Finalidade de produção e comercialização e animal desossado", "pageRef": 150},
                {"topic": "Concurso aparente de normas com abigeato e post factum impunível", "pageRef": 153},
                {"topic": "Violência patrimonial contra a mulher e afastamento de escusas absolutórias", "pageRef": 156}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a05/s14",
        "fingerprint": get_fp("direito-penal/a05/s14"),
        "analytic": """Este segmento finaliza a Parte Especial relativa aos Crimes contra o Patrimônio analisando a tipificação especializada da receptação de semoventes instituída pelo artigo 180-A e os reflexos transversais da violência patrimonial doméstica contra a mulher.

### Receptação de semovente domesticável de produção (artigo 180-A)
Introduzido pela Lei nº 13.330/2016 para coibir o crime organizado no campo e a pirataria de gado, o artigo 180-A criminaliza a conduta de adquirir, receber, transportar, conduzir, ocultar ou manter em depósito comercial rebanhos e semoventes de criação de procedência ilícita, cominando pena de **reclusão de dois a cinco anos e multa**:
- *Finalidade Específica*: exige que a conduta seja orientada pela **finalidade de produção ou de comercialização** mercantil (abastecimento de açougues clandestinos, feiras ou engorda em pastagens de terceiros);
- *Semovente Abatido*: a lei expressamente equipara a infração à aquisição do animal **ainda que abatido ou dividido em partes** (carcaças, meias-peças desossadas);
- *Elemento Subjetivo*: a norma emprega a fórmula *deve saber ser produto de crime*, harmonizando o apenamento severo perante o dolo direto e o dolo eventual;
- *Distinção com a Receptação Comum*: se a aquisição for realizada por consumidor particular doméstico para simples consumo alimentar individual, afasta-se o artigo 180-A por carência da finalidade comercial produtiva, atraindo a disciplina genérica do artigo 180 do Código Penal.

### Conflito aparente e post factum impunível
No concurso entre crimes de abigeato (artigo 155, § 6º) e receptação de animais (artigo 180-A), incide o princípio da consunção:
- O agente que subtrai as cabeças de gado na fazenda e posteriormente as conduz para ocultação em seu próprio sítio ou para venda direta não responde por furto e receptação em concurso;
- O transporte e a guarda do bem espoliado consubstanciam autêntico **post factum impunível** da subtração patrimonial originária, respondendo o infrator unicamente pelo furto qualificado. O artigo 180-A é vocacionado a punir os terceiros intermediários da cadeia clandestina de abate e comercialização.

### Violência patrimonial e a superação de escusas na Lei Maria da Penha
Relevante debate jurisprudencial assentou-se perante o Superior Tribunal de Justiça quanto à incidência das imunidades patrimoniais familiares (artigo 181 do Código Penal) quando o delito patrimonial for praticado pelo cônjuge ou companheiro contra a mulher em ambiente de violência doméstica:
- A Lei Maria da Penha (Lei nº 11.340/2006, art. 7º, IV) elenca expressamente a **violência patrimonial** como modalidade de agressão doméstica (retenção, subtração ou destruição parcial ou total de seus objetos, instrumentos de trabalho e bens);
- O STJ fixou entendimento vinculante de que **as escusas absolutórias do artigo 181 do Código Penal são inaplicáveis aos crimes patrimoniais cometidos contra a mulher no âmbito doméstico e familiar**, visto que a concessão de isenção de pena esvaziaria a proteção constitucional integral assegurada à mulher contra qualquer forma de opressão no ambiente do lar;
- Consectariamente, a sentença penal condenatória por infrações patrimoniais poderá inclusive arbitrar, a pedido expresso do Ministério Público ou da ofendida, valor indenizatório pecuniário mínimo a título de reparação dos danos materiais e morais experimentados pela vítima no evento delitivo.

### Para fixar
- O art. 180-A pune a receptação de semovente de produção com reclusão de dois a cinco anos e multa.
- A receptação de gado aplica-se ainda que o semovente esteja abatido ou retalhado em cortes.
- Exige-se que o infrator atue com o propósito finalístico de produção pecuária ou comércio.
- A compra de carne por consumidor final para consumo alimentar doméstico afasta o art. 180-A.
- A condução e guarda da rês pelo próprio abigeatário configura post factum impunível do furto.
- O art. 180-A visa punir os terceiros adquirentes e elos comerciais receptadores do gado subtraído.
- A violência patrimonial contra a mulher na Lei Maria da Penha afasta as escusas absolutórias do art. 181.
- A sentença penal condenatória por crimes patrimoniais pode fixar valor mínimo para reparação civil.""",
        "synthetic": [
            "**Receptação de Gado (art. 180-A)**: tipificação autônoma cominando reclusão de dois a cinco anos pela guarda e comércio de semoventes furtados.",
            "**Abrangência do Abate**: tutela penal incidente ainda que as reses apreendidas estejam abatidas, desossadas ou retalhadas em fardos de carne.",
            "**Finalidade Comercial Agropecuária**: o tipo exige destinação mercantil ou incorporação ao ciclo produtivo rural para incidência do preceito especial.",
            "**Consumo Próprio Excluído**: aquisições casuais por particulares para consumo familiar desbordam do art. 180-A amoldando-se à receptação geral.",
            "**Post Factum do Furto**: o ladrão que esconde o rebanho subtraído responde unicamente pelo abigeato sendo a guarda mero exaurimento impunível.",
            "**Responsabilização de Intermediários**: tipo arquitetado para desarticular os receptadores e frigoríficos que fomentam o crime organizado agrário.",
            "**Lei Maria da Penha e Escusas**: o STJ neutraliza as imunidades do art. 181 em crimes patrimoniais contra mulher sob violência doméstica.",
            "**Reparação Mínima Indenizatória**: o título penal judicial autoriza a liquidação compulsória de indenizações patrimoniais aos lesados."
        ]
    })

    return items, summaries
