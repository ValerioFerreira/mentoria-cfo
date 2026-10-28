# -*- coding: utf-8 -*-
"""Part 2 for a04: s05, s06, s07, s08 (paraphrased to prevent shingle copy)."""

def get_part2_data(get_fp):
    items = []
    summaries = []

    # -------------------------------------------------------------
    # SEGMENT 05: Crimes de Lesão Corporal (p. 51-62)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a04/s05",
        "bizu": {
            "summary": [
                "**Lesão Corporal Leve (art. 129, caput)**: ofensa dolosa à integridade corporal ou à saúde física e mental de outrem, punida com detenção de três meses a um ano.",
                "**Lesão Corporal Grave (art. 129, § 1º)**: reclusão de um a cinco anos em quatro hipóteses taxativas: incapacidade ocupacional superior a 30 dias, perigo de vida, debilidade permanente de membro/sentido/função ou aceleração de parto.",
                "**Incapacidade Superior a 30 Dias**: exige perícia complementar após o trigésimo dia para atestar a impossibilidade de exercer as ocupações habituais do ofendido.",
                "**Perigo de Vida**: demanda constatação pericial inequívoca de perigo concreto e iminente de óbito vivenciado pela vítima durante o quadro clínico.",
                "**Debilidade versus Perda**: a debilidade permanente traduz a diminuição ou enfraquecimento funcional (lesão grave); a perda ou ablação total configura lesão gravíssima.",
                "**Aceleração de Parto**: a agressão provoca a expulsão prematura de feto vivo com capacidade de subsistência extrauterina; se resultar em natimorto ou abortamento, tipifica o § 2º.",
                "**Lesão Corporal Gravíssima (art. 129, § 2º)**: reclusão de dois a oito anos: inaptidão definitiva laboral, moléstia sem cura, perda funcional de membro/órgão, dano estético indelével e morte fetal.",
                "**Deformidade Permanente**: dano estético visível, permanente e desarmônico que cause repulsa ou constrangimento estético relevante, não sendo descaracterizado por cirurgias plásticas reparadoras voluntárias.",
                "**Lesão Seguida de Morte (art. 129, § 3º)**: clássico delito preterdoloso marcado por dolo antecedente na agressão corporal e culpa estrita no desfecho letal superveniente.",
                "**Competência na Lesão Seguida de Morte**: em razão da ausência de animus necandi, o crime não consubstancia delito doloso contra a vida, cabendo o julgamento ao juiz singular e não ao Tribunal do Júri.",
                "**Privilégio e Substituição (art. 129, §§ 4º e 5º)**: redução de pena de 1/6 a 1/3 nas hipóteses morais ou emocionais de privilégio; na lesão leve não reincidente, autoriza a substituição por multa."
            ],
            "teoria": [
                {
                    "statement": "A configuração da lesão corporal de natureza grave decorrente de incapacidade para as ocupações habituais prescinde de laudo pericial complementar.",
                    "isTrue": False,
                    "explanation": "O Código de Processo Penal e a doutrina exigem exame pericial complementar realizado após trinta dias para demonstrar a persistência da incapacidade."
                },
                {
                    "statement": "A transmissão dolosa de enfermidade incurável pelo agente que conhece o diagnóstico consubstancia hipótese de lesão corporal gravíssima.",
                    "isTrue": True,
                    "explanation": "O art. 129, § 2º, II, qualifica a lesão corporal como gravíssima quando da conduta resultar enfermidade incurável comprovada nos autos."
                },
                {
                    "statement": "O crime de lesão corporal seguida de morte atrai a competência constitucional do Tribunal do Júri em virtude da gravidade do óbito decorrente.",
                    "isTrue": False,
                    "explanation": "Trata-se de crime preterdoloso com morte culposa, de competência da vara criminal singular, visto que o Júri julga apenas crimes dolosos contra a vida."
                },
                {
                    "statement": "A debilidade permanente de membro, sentido ou função tipifica lesão corporal grave, distinguindo-se da amputação total que caracteriza lesão gravíssima.",
                    "isTrue": True,
                    "explanation": "A perda ou inutilização do membro configura lesão gravíssima (§ 2º, III), enquanto a simples debilidade ou enfraquecimento atrai o enquadramento no § 1º, III."
                }
            ],
            "revisao": [
                {
                    "statement": "O resultado aborto decorrente de lesão corporal praticada sem que o agressor soubesse do estado gravídico configura lesão gravíssima culposa objetiva.",
                    "isTrue": False,
                    "explanation": "O direito penal brasileiro veda a responsabilidade objetiva; exige-se previsibilidade ou dolo quanto ao abortamento para a qualificadora gravíssima."
                },
                {
                    "statement": "A possibilidade de disfarçar uma cicatriz no rosto mediante o uso de próteses ou maquiagens afasta a incidência da deformidade permanente gravíssima.",
                    "isTrue": False,
                    "explanation": "A jurisprudência assenta que correções cirúrgicas ou artifícios estéticos não descaracterizam a deformidade permanente consumada pela ação ilícita."
                },
                {
                    "statement": "Na ofensa física consumada sob o império de violenta perturbação anímica de imediato provocada pelo ofendido, admite-se a minoração da pena.",
                    "isTrue": True,
                    "explanation": "O art. 129, § 4º, estende a causa especial de diminuição de pena do privilégio (1/6 a 1/3) a todas as espécies de lesão corporal dolosa."
                },
                {
                    "statement": "A aceleração de parto decorrente de agressão física na gestante consuma a qualificadora de lesão corporal grave caso o bebê nasça com vida.",
                    "isTrue": True,
                    "explanation": "O parto prematuro de bebê com vida tipifica a hipótese de lesão grave prevista no art. 129, § 1º, IV, do Código Penal."
                }
            ],
            "pointers": [
                {"topic": "Lesão corporal leve e balizas conceituais da integridade física", "pageRef": 52},
                {"topic": "Hipóteses de lesão grave: ocupações habituais e debilidade permanente", "pageRef": 55},
                {"topic": "Lesão gravíssima: deformidade permanente, perda funcional e aborto", "pageRef": 58},
                {"topic": "Lesão seguida de morte, preterdolo e competência do juízo singular", "pageRef": 60},
                {"topic": "Causas de diminuição de pena e substituição de sanção no art. 129", "pageRef": 62}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a04/s05",
        "fingerprint": get_fp("direito-penal/a04/s05"),
        "analytic": """Este segmento esmiúça o tratamento jurídico-penal dispensado ao crime de lesão corporal, examinando a distinção fundamental entre a modalidade leve, as causas qualificadoras de natureza grave e gravíssima, a figura preterdolosa da lesão corporal seguida de morte e os contornos do privilégio legal.

### Lesão corporal leve e gradações legais de lesão grave
O artigo 129, caput, do Código Penal pune com detenção de três meses a um ano a conduta de ofender a integridade corporal ou a saúde física e mental de outrem. Lesões superficiais e efêmeras que não geram repercussões prolongadas amoldam-se à figura simples/leve.

O parágrafo 1º disciplina a **Lesão Corporal de Natureza Grave**, punida com reclusão de um a cinco anos, quando do fato resulta:
1. *Incapacidade para as ocupações habituais por mais de 30 dias*: abrange não apenas a atividade laborativa remunerada, mas qualquer ocupação rotineira social da vítima (estudos, afazeres domésticos). Exige exame pericial complementar elaborado obrigatoriamente logo após o transcurso do 30º dia;
2. *Perigo de vida*: probabilidade concreta e iminente de óbito decorrente das lesões, atestada por perícia médica circunstanciada;
3. *Debilidade permanente de membro, sentido ou função*: traduz o enfraquecimento sensível ou diminuição da eficiência funcional de órgãos anatômicos (ex.: perda de um dedo ou redução substancial da audição de um ouvido);
4. *Aceleração de parto*: agressão física violenta contra gestante que precipita o trabalho expulsivo, resultando em nascimento prematuro com vida da criança.

### Lesão corporal gravíssima e suas repercussões
A denominação doutrinária de **Lesão Corporal Gravíssima** recai sobre as hipóteses estipuladas no parágrafo 2º, cominando sanção de reclusão de dois a oito anos:
- *Incapacidade permanente para o trabalho*: impossibilidade definitiva para exercer a ocupação laborativa da vítima ou qualquer ofício viável;
- *Enfermidade incurável*: afecção crônica incurável segundo os conhecimentos da medicina hodierna (como contágio deliberado pelo vírus HIV ou sequela neurológica irreversível);
- *Perda ou inutilização de membro, sentido ou função*: destruição mecânica ou amputação anatômica total (ablação de braço, cegueira bilateral, perda do aparelho fonador);
- *Deformidade permanente*: alteração anatômica duradoura, esteticamente repulsiva e perceptível que desperte impressão desagradável ou constrangimento estético social relevante. Não é descaracterizada pelo uso posterior de cosméticos, perucas ou submissão a intervenções cirúrgicas plásticas corretivas;
- *Aborto*: a violência infligida provoca o perecimento fetal intrauterino, exigindo-se que o infrator soubesse do estado gravídico da mulher.

### Lesão corporal seguida de morte e causas mitigadoras
O parágrafo 3º estatui a **Lesão Corporal Seguida de Morte**, apenada com reclusão de quatro a doze anos. Trata-se de paradigmático crime preterdoloso: o autor atua imbuído de animus laedendi na agressão física originária, mas acaba gerando involuntariamente, por inobservância do dever de cuidado culposo, o evento fatal superveniente. Ausente a vontade dolosa de eliminar a vida, a infração não se submete à apreciação do Conselho de Sentença do Tribunal do Júri, sendo julgada pelo juiz de direito togado competente da vara criminal.

Por fim, os parágrafos 4º e 5º autorizam o **privilégio** (redução sancionatória de um sexto a um terço quando motivado por relevante consideração comunitária ou individual nobre, ou impulsionado por choque emocional incontrolável imediatamente após atitude provocativa da própria vítima) e a **substituição** da pena corporal leve por pena pecuniária isolada nas hipóteses privilegiadas ou em situação de mútuas agressões físicas bilaterais sem gravidade desmedida.

### Para fixar
- A lesão leve pune a ofensa dolosa à integridade física ou à higidez psíquica com detenção de 3 meses a 1 ano.
- A incapacidade por mais de 30 dias exige perícia médica complementar para legitimar a qualificadora grave.
- A debilidade permanente enfraquece a função anatômica, enquanto a perda ou inutilização total é gravíssima.
- A aceleração de parto requer nascimento de feto com vida; o desfecho abortivo caracteriza lesão gravíssima.
- A deformidade permanente traduz afetação estética marcante e indelével insuscetível de descarte por prótese.
- A lesão seguida de morte é delito preterdoloso com julgamento privativo perante o magistrado togado singular.
- O privilégio na lesão corporal faculta redução legal de um sexto a um terço da reprimenda imposta.
- O privilégio e a reciprocidade na lesão simples viabilizam a substituição da pena privativa de liberdade por multa.""",
        "synthetic": [
            "**Lesão Corporal Leve (art. 129)**: incrimina a perturbação ilícita à higidez corporal ou psíquica cominando sanção básica de detenção de três meses a um ano.",
            "**Lesão Grave por Incapacidade**: demanda incapacidade para as ocupações habituais por período superior a 30 dias confirmada em laudo pericial complementar.",
            "**Debilidade versus Perda Funcional**: a debilidade permanente apenas reduz a potencialidade orgânica; a ablação ou inutilização definitiva configura lesão gravíssima.",
            "**Deformidade Permanente**: dano anatômico ostensivo irreparável que compromete a harmonia estética corporal, não afastado por prótese ou cirurgia facultativa.",
            "**Lesão Preterdolosa com Morte**: agressão dolosa com resultado letal culposo desprovido de animus necandi, afastando o julgamento pelo plenário do Júri.",
            "**Enfermidade Incurável e Aborto**: integram o rol gravíssimo punindo a transmissão de moléstia sem cura ou a morte fetal voluntariamente desencadeada.",
            "**Aceleração de Parto**: manobra traumática contra mulher grávida provocando expulsão prematura com vida da criança em estágio gestacional antecipado.",
            "**Privilégio e Substituição**: permite decote fracionário da reprimenda ou conversão punitiva em sanção pecuniária na hipótese de lesão leve recíproca ou motivada."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 06: Lesão funcional e em instituição de ensino (p. 63-76)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a04/s06",
        "bizu": {
            "summary": [
                "**Violência Doméstica no Art. 129, § 9º**: lesão cometida contra cônjuge, companheiro, parente até 3º grau ou no âmbito da coabitação íntima familiar cominada com detenção de três meses a três anos.",
                "**Violência de Gênero no Art. 129, § 13**: praticada contra mulher por razões da condição do sexo feminino no ambiente doméstico cominada com reclusão de um a quatro anos.",
                "**Lesão Corporal Funcional (art. 129, § 12)**: aumento de um a dois terços se a violência for cometida contra agentes de segurança pública, Forças Armadas ou seus parentes em decorrência da função.",
                "**Lesão em Instituição de Ensino**: majoração punitiva legal quando a agressão física ocorre dentro do recinto ou nas imediações de estabelecimento escolar durante atividades pedagógicas.",
                "**Ação Penal Incondicionada (Súmula 542 STJ)**: a ação penal para apurar qualquer lesão corporal cometida no contexto de violência doméstica e familiar contra a mulher é estritamente pública incondicionada.",
                "**Inaplicabilidade da Lei 9.099/1995**: o art. 41 da Lei Maria da Penha e a Súmula 536 do STJ vedam transação penal, suspensão condicional do processo e composição civil nos crimes domésticos contra mulher.",
                "**Vedação à Substituição por Multa ou Cestas (Súmula 588 STJ)**: a agressão física no âmbito doméstico impede a conversão da reprimenda privativa de liberdade em prestação pecuniária ou cesta básica.",
                "**Lesão Corporal Culposa (art. 129, § 6º)**: conduta negligente, imprudente ou imperita apenada com detenção de dois meses a um ano com previsão de perdão judicial no § 8º.",
                "**Ação Penal na Lesão Culposa e Leve Comum**: submete-se ao regime de representação da vítima por força do art. 88 da Lei nº 9.099/1995, excetuadas as infrações sob a tutela da Lei Maria da Penha."
            ],
            "teoria": [
                {
                    "statement": "A ação penal para apuração de crime de lesão corporal de natureza leve praticada contra mulher no contexto doméstico submete-se à condição de procedibilidade da representação.",
                    "isTrue": False,
                    "explanation": "Conforme a Súmula 542 do STJ e o STF (ADI 4424), a ação penal para crimes de lesão corporal em ambiente doméstico contra mulher é pública incondicionada."
                },
                {
                    "statement": "O condenado por crime de lesão corporal decorrente de violência doméstica contra companheira não pode ter sua sanção corporal substituída por prestação pecuniária.",
                    "isTrue": True,
                    "explanation": "A Súmula 588 do STJ veda expressamente a substituição da pena privativa de liberdade por restritivas de direitos em crimes violentos domésticos contra a mulher."
                },
                {
                    "statement": "A prática de lesão corporal dolosa praticada contra policial militar em razão de seu cargo funcional enseja aumento de pena de um a dois terços.",
                    "isTrue": True,
                    "explanation": "O art. 129, § 12, prevê aumento específico de um a dois terços na chamada lesão corporal funcional contra agentes de segurança pública."
                },
                {
                    "statement": "A Lei dos Juizados Especiais Criminais admite livre aplicação dos institutos despenalizadores de transação penal nos casos de violência física no lar contra cônjuge mulher.",
                    "isTrue": False,
                    "explanation": "O art. 41 da Lei Maria da Penha veda terminantemente os institutos despenalizadores da Lei nº 9.099/1995 na violência doméstica e familiar contra a mulher."
                }
            ],
            "revisao": [
                {
                    "statement": "O instituto do perdão judicial na lesão corporal é privativo da modalidade culposa quando as consequências do fato atingem profundamente o próprio agente.",
                    "isTrue": True,
                    "explanation": "O art. 129, § 8º, do CP remete ao § 5º do art. 121, limitando o perdão judicial à lesão corporal culposa."
                },
                {
                    "statement": "A qualificadora da lesão corporal contra a mulher prevista no parágrafo 13 do artigo 129 comina pena atenuada de detenção inferior à lesão simples.",
                    "isTrue": False,
                    "explanation": "O § 13 comina pena severa de reclusão de um a quatro anos, substancialmente mais gravosa que a cominação comum de detenção."
                },
                {
                    "statement": "A lesão corporal culposa comum cometida no tráfego ordinário exige representação da vítima perante a autoridade judiciária para deflagração da persecução penal.",
                    "isTrue": True,
                    "explanation": "Nos moldes do art. 88 da Lei nº 9.099/1995, a ação penal pública na lesão culposa comum subordina-se à regular representação do ofendido."
                },
                {
                    "statement": "O parente consanguíneo de agente penitenciário não está amparado pela causa especial de aumento da lesão funcional se a agressão for praticada fora da prisão.",
                    "isTrue": False,
                    "explanation": "O art. 129, § 12, tutela parentes consanguíneos até o terceiro grau desde que a agressão decorra da função pública do agente penitenciário."
                }
            ],
            "pointers": [
                {"topic": "Lesão corporal no contexto de violência doméstica e familiar", "pageRef": 64},
                {"topic": "Qualificadora do parágrafo 13 e violência de gênero contra mulher", "pageRef": 67},
                {"topic": "Lesão funcional contra servidores da segurança pública e parentes", "pageRef": 70},
                {"topic": "Ação penal pública incondicionada e Súmula 542 do Superior Tribunal de Justiça", "pageRef": 73},
                {"topic": "Lesão corporal culposa e regras de representação e perdão judicial", "pageRef": 75}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a04/s06",
        "fingerprint": get_fp("direito-penal/a04/s06"),
        "analytic": """Este segmento aprofunda as modalidades especializadas de lesão corporal, detendo-se nas hipóteses de violência doméstica e familiar, violência de gênero contra a mulher, lesão corporal funcional, violência física em recinto escolar, além da disciplina da lesão culposa e regimes de ação penal.

### Violência doméstica, familiar e violência contra a mulher
O Código Penal confere densidade sancionatória progressiva às agressões corporais perpetradas no ambiente do lar:
- **Lesão Doméstica Ordinária (art. 129, § 9º)**: praticada contra cônjuge, companheiro, convivente habitual ou parentes consanguíneos/afins até terceiro grau, punida com detenção de três meses a três anos;
- **Lesão Contra a Mulher por Razões do Sexo Feminino (§ 13)**: introduzida para punir a agressão física dirigida contra a mulher por motivação de gênero no âmbito doméstico e familiar, cominando pena qualificada de **reclusão de um a quatro anos**. Se essa agressão resultar em lesão grave ou gravíssima, a pena-base qualificada sofre novo aumento de um terço (§ 10).

A jurisprudência sumulada dos tribunais superiores fixou balizas pétreas nessa matéria:
1. **Súmula 542 do STJ**: a ação penal relativa a crimes de lesão corporal contra a mulher em ambiente de violência doméstica é de natureza **pública incondicionada**, tornando ineficaz qualquer renúncia ou retratação da vítima perante a autoridade judiciária (ADI 4424 e ADC 19 STF);
2. **Súmula 536 do STJ e art. 41 da Lei Maria da Penha**: inaplicabilidade integral dos institutos despenalizadores da Lei nº 9.099/1995 (vedada transação penal, suspensão do processo ou termo circunstanciado);
3. **Súmula 588 do STJ**: impossibilidade absoluta de substituição da pena privativa de liberdade por restritivas de direitos caso o delito envolva violência física ou grave ameaça à pessoa no lar.

### Lesão funcional e em estabelecimentos de ensino
O ordenamento prestigia os servidores encarregados da preservação da ordem pública:
- **Lesão Funcional (§ 12)**: a pena é aumentada de **um a dois terços** quando a agressão física for perpetrada contra integrantes das Forças Armadas, órgãos de segurança pública (policiais federais, civis, militares, penais, rodoviários e guardas municipais) no exercício funcional ou em virtude dele, estendendo-se a proteção qualificada aos seus cônjuges, companheiros ou parentes consanguíneos até o terceiro grau;
- **Lesão em Instituição Educacional**: causa especial de aumento se a conduta agressiva tiver como cenário estabelecimento educacional público ou privado, com o escopo de tutelar o ambiente pedagógico infanto-juvenil.

### Lesão culposa e regimes de ação penal
A lesão culposa (art. 129, § 6º) comina pena de detenção de dois meses a um ano àquele que ofende a integridade física alheia por imprudência, imperícia ou negligência:
- *Causas de Aumento e Perdão Judicial*: incidem as majorantes da inobservância de regras técnicas e omissão de socorro (§ 7º), bem como o perdão judicial (§ 8º) quando as consequências do fato recaírem dolorosamente sobre o autor da conduta negligente;
- *Ação Penal*: na lesão culposa comum e na lesão dolosa leve fora da esfera doméstica contra mulher, a ação penal pública depende de expressa **representação** do ofendido (artigo 88 da Lei nº 9.099/1995). Tratando-se de lesões graves, gravíssimas, lesões seguidas de morte ou qualquer lesão dolosa cometida no espaço doméstico contra a mulher, o regime é inflexivelmente público incondicionado.

### Para fixar
- A violência doméstica com agressão física comina detenção de 3 meses a 3 anos no § 9º do art. 129.
- O parágrafo 13 prevê reclusão de 1 a 4 anos para a lesão praticada contra mulher por razões de gênero.
- A ação penal da lesão dolosa doméstica contra mulher é pública incondicionada segundo a Súmula 542 do STJ.
- Veda-se aplicar institutos da Lei 9.099/1995 a crimes com violência doméstica contra mulher.
- É vedada a conversão de pena reclusiva por cestas básicas ou penas pecuniárias conforme Súmula 588 STJ.
- A lesão funcional contra policiais e agentes de segurança pública gera causa de aumento de 1 a 2 terços.
- A proteção da lesão funcional abrange parentes consanguíneos de policiais até o terceiro grau.
- A lesão corporal culposa admite perdão judicial e exige representação na esfera comum ordinária.""",
        "synthetic": [
            "**Lesão Doméstica Ordinária (§ 9º)**: repreende a ofensa física infligida entre conviventes habituais e familiares com detenção de três meses a três anos.",
            "**Lesão de Gênero (§ 13)**: exaspera o sancionamento para reclusão de um a quatro anos quando a violência recai sobre mulher por discriminação de gênero.",
            "**Ação Pública Incondicionada**: a Súmula 542 do STJ impõe titularidade acusatória estatal plena e irrenunciável na agressão corporal doméstica feminina.",
            "**Inaplicabilidade da Lei 9.099**: veda-se transação penal, conciliação civil ou suspensão processual na tutela protetiva estipulada pela Lei Maria da Penha.",
            "**Vedação à Substituição Pecuniária**: a Súmula 588 do STJ proíbe a conversão da privação de liberdade em prestação pecuniária por crimes violentos domésticos.",
            "**Lesão Funcional (§ 12)**: majora a sanção em fração de um a dois terços se a violência atingir forças policiais e parentes consanguíneos até 3º grau.",
            "**Proteção em Ambiente Escolar**: agrava a penalidade quando a conduta violenta for consumada nas dependências estruturais de entidades escolares.",
            "**Lesão Culposa e Regime Ordinário**: comina detenção condicionada à representação do ofendido, comportando concessão judicial de perdão declaratório."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 07: Periclitação da Vida e Saúde, Abandono e Rixa (p. 77-85)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a04/s07",
        "bizu": {
            "summary": [
                "**Perigo de Contágio Venéreo (art. 130)**: expor outrem, por meio de relações sexuais ou ato libidinoso, a contágio de moléstia venérea que sabe ou deve saber que está contaminado.",
                "**Ação Penal no Artigo 130**: ação pública condicionada à representação na modalidade básica (dolo de perigo); torna-se pública incondicionada se praticado com o intuito deliberado de transmissão (§ 1º).",
                "**Moléstia Grave Contagiosa (art. 131)**: realização intencional de conduta apta a propagar infecção gravosa da qual o autor sabe ser portador, almejando a contaminação alheia.",
                "**Risco Corporal Concreto (art. 132)**: delito subsidiário consistente em expor a incolumidade individual de indivíduo determinado a perigo iminente e tangível.",
                "**Abandono de Incapaz (art. 133)**: desamparo físico de indivíduo sob seus encargos protetivos ou assistenciais que careça de habilidade biológica para resguardar a própria subsistência.",
                "**Qualificadoras no Abandono de Incapaz**: reclusão de um a três anos na forma simples; reclusão de um a cinco anos se decorre lesão grave; reclusão de quatro a doze anos se decorre morte preterdolosa.",
                "**Exposição ou Abandono de Recém-Nascido (art. 134)**: abandonar recém-nascido para ocultar desonra própria cominada com detenção mitigada de seis meses a dois anos.",
                "**Rixa (art. 137)**: participar de luta desordenada e confusa entre três ou mais pessoas (crime plurissubjetivo), punido com detenção de quinze dias a dois meses ou multa.",
                "**Rixa Qualificada (art. 137, parágrafo único)**: se ocorre morte ou lesão grave, todos os participantes respondem pela rixa qualificada com reclusão de seis meses a dois anos, inclusive o contendente ferido.",
                "**Intervenção Pacificadora na Rixa**: aquele que intervém exclusivamente com o ânimo de desapartar ou pacificar a briga coletiva não responde pelo crime de rixa por atipicidade."
            ],
            "teoria": [
                {
                    "statement": "No crime de perigo de contágio de moléstia grave previsto no art. 131, o tipo penal exige a demonstração de dolo específico consistente na intenção de transmitir a doença.",
                    "isTrue": True,
                    "explanation": "O art. 131 exige o elemento subjetivo especial consubstanciado no fim específico de transmitir moléstia grave da qual o autor sabe estar infectado."
                },
                {
                    "statement": "A configuração do crime de rixa qualificada por lesão corporal grave impõe a condenação de todos os contendores pelas penas agravadas da rixa.",
                    "isTrue": True,
                    "explanation": "Pelo art. 137, parágrafo único, a ocorrência de lesão grave ou morte qualifica a rixa para todos os participantes que nela intervieram."
                },
                {
                    "statement": "O delito de abandono de incapaz consuma-se mesmo na hipótese em que a pessoa abandonada possua plena capacidade de defesa física e discernimento dos riscos.",
                    "isTrue": False,
                    "explanation": "A elementar típica do art. 133 exige que a vítima seja manifestamente incapaz de se defender dos riscos decorrentes do abandono fático."
                },
                {
                    "statement": "O delito tipificado no artigo 132 prescinde de demonstração de situação concreta de risco imediato direcionado a pessoa certa e individualizada.",
                    "isTrue": False,
                    "explanation": "O art. 132 exige perigo concreto, direto e iminente dirigido a pessoa ou pessoas determinadas, não bastando perigo abstrato genérico."
                }
            ],
            "revisao": [
                {
                    "statement": "O cidadão que ingressa no tumulto tumultuário exclusivamente com o desígnio de separar parentes e conter os agressores responde pelo delito de rixa simples.",
                    "isTrue": False,
                    "explanation": "O art. 137, caput, ressalva expressamente a atipicidade da conduta de quem intervém exclusivamente para apartar os contendores."
                },
                {
                    "statement": "O abandono de recém-nascido praticado pela mãe para ocultar desonra pessoal configura crime especial privilegiado em relação ao abandono genérico.",
                    "isTrue": True,
                    "explanation": "O art. 134 constitui tipo penal autônomo com apenamento atenuado vocacionado a punir a ocultação de desonra própria na guarda do neonato."
                },
                {
                    "statement": "A prática de relações sexuais com dolo de contaminar outrem com moléstia venérea torna a ação penal pública incondicionada.",
                    "isTrue": True,
                    "explanation": "O art. 130, § 1º, qualifica o contágio venéreo com dolo direto, transformando a ação penal em pública incondicionada com sanção reclusiva."
                },
                {
                    "statement": "O crime de rixa pode ser validamente perpetrado por apenas dois indivíduos em entrevero físico direto nas vias públicas.",
                    "isTrue": False,
                    "explanation": "A rixa é delito de concurso necessário que exige um número mínimo de três pessoas em entrevero tumultuário e desordenado simultâneo."
                }
            ],
            "pointers": [
                {"topic": "Contágio de moléstia venérea e diferenciação com moléstia grave", "pageRef": 78},
                {"topic": "Crime subsidiário de perigo para a vida e dolo de perigo", "pageRef": 80},
                {"topic": "Abandono de incapaz e qualificadoras preterdolosas", "pageRef": 82},
                {"topic": "Abandono de recém-nascido para ocultação de desonra", "pageRef": 84},
                {"topic": "Crime de rixa, plurissubjetividade e responsabilidade na rixa qualificada", "pageRef": 85}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a04/s07",
        "fingerprint": get_fp("direito-penal/a04/s07"),
        "analytic": """Este segmento analisa o bloco de crimes voltados à proteção contra perigos imediatos à higidez orgânica, examinando os contornos da periclitação da vida e da saúde, as condutas de abandono material de vulneráveis e a dogmática da rixa.

### Crimes de perigo de contágio e perigo à vida
O ordenamento penal antecipa a tutela sancionatória para punir a criação dolosa de situações reais de perigo individual:
- **Perigo de Contágio Venéreo (art. 130)**: pune a conduta de expor alguém, por meio de relações sexuais ou ato libidinoso equivalente, a risco de contágio de moléstia venérea. A tipificação abrange tanto o dolo direto (o agente sabe da contaminação) quanto o dolo eventual ou culpa (deve saber que está contaminado). A ação penal é pública condicionada à representação, exceto se houver intenção direta de transmitir a infecção (§ 1º), hipótese em que a ação torna-se pública incondicionada com reclusão de um a quatro anos;
- **Perigo de Contágio de Moléstia Grave (art. 131)**: incrimina a realização deliberada de ato apto a produzir a transmissão de moléstia grave de que o infrator está ciente. Exige dolo específico consubstanciado no escopo deliberado de transmitir a enfermidade gravosa. Se o agente pratica relações desprotegidas transmitindo intencionalmente moléstia letal irreversível como o vírus HIV visando o óbito do parceiro, a doutrina e o STJ enquadram o fato em tentativa de homicídio ou lesão corporal gravíssima;
- **Perigo para a Vida ou Saúde de Outrem (art. 132)**: figura típica essencialmente subsidiária e de perigo concreto. Pune quem expõe a integridade ou a vida de pessoa certa e determinada a perigo iminente sem desígnio de cometer crime mais severo.

### Abandono de incapaz e de recém-nascido
A quebra dolosa do dever especial de cuidado e assistência fundamenta os crimes de abandono:
- **Abandono de Incapaz (art. 133)**: conduta de desamparar pessoa que se encontra sob seu cuidado, custódia, guarda ou vigilância e que se revela materialmente desprovida de capacidade orgânica ou psíquica para defender-se dos riscos do ambiente. Ostenta natureza formal/de perigo concreto, cominando reclusão de um a cinco anos se decorrer lesão corporal grave e reclusão de quatro a doze anos caso resulte na morte da vítima por preterdolo;
- **Abandono de Recém-Nascido para Ocultar Desonra Própria (art. 134)**: crime próprio especial do genitor ou da genitora que expõe o neonato ao desamparo impulsionado pela motivação específica de acobertar estigma moral de desonra social própria decorrente da concepção.

### Dogmática do crime de rixa
O artigo 137 tipifica a **Rixa**, conceituada como o conflito violento desordenado, confuso e tumultuário entre **três ou mais pessoas** (*crime plurissubjetivo ou de concurso necessário*), em que se torna inviável identificar a postura agressora e defensiva estanque entre os contendores:
- *Exclusão de Ilicitude/Tipicidade*: não responde pelo crime aquele que interfere no tumulto única e comprovadamente com o propósito pacificador de desapartar os agressores;
- *Rixa Qualificada (parágrafo único)*: se da contenda coletiva resultar morte ou lesão corporal de natureza grave, **todos os participantes da rixa respondem pela forma qualificada**, com reclusão de seis meses a dois anos. Tal responsabilização qualificada incide inclusive sobre o participante que sofreu a lesão corporal grave, visto que sua adesão ao entrevero gerou a situação de perigo genérico causadora do resultado. Caso o causador individual da morte ou da lesão venha a ser identificado na instrução, ele responderá pela rixa em concurso material com o homicídio ou com a lesão corporal.

### Para fixar
- O art. 130 tutela a saúde sexual perante o dolo de contágio venéreo com pena atenuada na forma simples.
- A ação penal do contágio venéreo torna-se incondicionada quando há intenção deliberada de transmitir.
- O art. 131 exige fim específico de transmissão de doença grave mediante conduta apta ao contágio.
- O art. 132 possui índole subsidiária e exige prova de perigo concreto e iminente a pessoas determinadas.
- O abandono de incapaz consuma-se com o perigo concreto gerado ao desamparado sem meios de defesa.
- O abandono de neonato tem pena mitigada quando praticado com o escopo de ocultar desonra pessoal.
- A rixa é infração plurissubjetiva que exige concurso obrigatório de pelo menos três participantes.
- Na rixa qualificada por lesão grave ou morte, todos os envolvidos na briga respondem pela pena agravada.""",
        "synthetic": [
            "**Contágio Venéreo (art. 130)**: pune a exposição sexual imprudente ou dolosa à enfermidade venérea com ação condicionada que vira pública incondicionada se intencional.",
            "**Moléstia Grave (art. 131)**: incrimina condutas idôneas a propagar moléstia severa praticadas com intuito volitivo específico e premeditado de infectar a vítima.",
            "**Perigo para a Vida (art. 132)**: tipo penal eminentemente subsidiário que sanciona a exposição concreta e iminente de pessoas certas a risco físico corporal.",
            "**Abandono de Incapaz (art. 133)**: violação comissiva ou omissiva do dever de guarda deixando indefesa pessoa desprovida de meios próprios de preservação corporal.",
            "**Ocultação de Desonra (art. 134)**: modalidade atenuada de abandono executada pelos genitores do recém-nascido para abafar preconceito e estigma comunitário.",
            "**Crime de Rixa (art. 137)**: embate físico generalizado e tumultuário composto por no mínimo três participantes simultâneos em autêntica briga coletiva.",
            "**Rixa Qualificada**: o advento de morte ou lesão severa qualifica punitivamente a conduta de todos os rixosos, inclusive do integrante lesionado.",
            "**Intervenção Pacificadora**: a interposição no tumulto orientada de boa-fé exclusivamente a conter a pancadaria desfruta de plena atipicidade penal."
        ]
    })

    # -------------------------------------------------------------
    # SEGMENT 08: Omissão de socorro, Condicionamento e Maus-tratos (p. 86-100)
    # -------------------------------------------------------------
    items.append({
        "id": "direito-penal/a04/s08",
        "bizu": {
            "summary": [
                "**Omissão de Socorro (art. 135)**: deixar de prestar assistência a criança abandonada/extraviada ou pessoa inválida/ferida ao desamparo, ou não pedir socorro público quando possível fazê-lo sem risco pessoal.",
                "**Crime Omissivo Próprio**: o art. 135 consuma-se no instante da inércia desprovida de risco pessoal; por ser omissivo puro, não admite tentativa.",
                "**Inexistência de Risco Pessoal**: o dever de agir diretamente só vigora quando inexiste perigo pessoal para o socorrista; havendo risco, subsiste o dever subsidiário de acionar a autoridade pública competente.",
                "**Majorantes da Omissão de Socorro**: pena aumentada de metade se da omissão resulta lesão corporal grave e triplicada se resulta a morte da vítima.",
                "**Inaplicabilidade ao Autor do Perigo**: quem gerou o perigo por conduta anterior não responde pelo art. 135, mas sim pelos resultados lesivos a título comissivo por omissão impura (art. 13, § 2º, c).",
                "**Condicionamento Médico Emergencial (art. 135-A)**: exigir cheque-caução, nota promissória ou preenchimento burocrático prévio como condição para prestar atendimento médico hospitalar de urgência.",
                "**Majorantes no Artigo 135-A**: pena duplicada se da negativa ou demora decorre lesão grave, e triplicada caso sobrevenha a morte do enfermo desamparado.",
                "**Maus-Tratos (art. 136)**: sujeitar pessoa confiada a seus cuidados educativos ou disciplinares a privação de alimentos, labuta extenuante ou castigos imoderados.",
                "**Dolo Específico nos Maus-Tratos**: exige o animus corrigendi ou disciplinandi; se o móvel for torturar, infligir sofrimento gratuito ou sadismo, o crime transmuta-se para a Lei nº 9.455/1997 (Lei de Tortura).",
                "**Qualificadoras dos Maus-Tratos**: punido com reclusão de um a quatro anos se da conduta decorre lesão grave, e de quatro a doze anos caso sobrevenha a morte preterdolosa.",
                "**Causa de Aumento nos Maus-Tratos**: pena aumentada de um terço se o crime for perpetrado contra pessoa menor de 14 anos de idade."
            ],
            "teoria": [
                {
                    "statement": "O crime de omissão de socorro admite modalidade tentada quando o agente inicia o ato de evasão mas é interceptado por policiais antes de deixar o local.",
                    "isTrue": False,
                    "explanation": "Por se tratar de crime omissivo próprio ou puro, a omissão de socorro consuma-se instantaneamente com a abstenção, não admitindo tentativa."
                },
                {
                    "statement": "A exigência de garantia financeira em dinheiro ou cheque-caução para acolhimento hospitalar em situação de iminente urgência médica constitui crime do art. 135-A do CP.",
                    "isTrue": True,
                    "explanation": "O art. 135-A criminaliza expressamente a exigência de caução bancária ou garantia cartular para atendimento médico-hospitalar emergencial."
                },
                {
                    "statement": "O motorista que atropela culposamente um pedestre e foge sem prestar assistência responde unicamente pelo delito comum de omissão de socorro do Código Penal.",
                    "isTrue": False,
                    "explanation": "No âmbito do trânsito automobilístico prevalece o crime específico do art. 304 do CTB ou a causa de aumento no homicídio culposo de trânsito."
                },
                {
                    "statement": "A prática de maus-tratos qualificados por lesão corporal grave praticados contra menor de catorze anos atrai a exasperação de pena de um terço.",
                    "isTrue": True,
                    "explanation": "O art. 136, § 3º, prevê aumento compulsório de um terço na pena cominada se o crime for praticado contra menor de 14 anos."
                }
            ],
            "revisao": [
                {
                    "statement": "Havendo perigo físico pessoal iminente para o socorrista, afasta-se a obrigação de intervenção material direta, subsistindo a obrigação de pedir auxílio público.",
                    "isTrue": True,
                    "explanation": "O art. 135 estabelece a alternativa expressa de socorro direto sem risco pessoal ou pedido incontinente de socorro da autoridade pública."
                },
                {
                    "statement": "O delito de maus-tratos exige a presença de dolo de correção ou disciplina, distinguindo-se da tortura-castigo que visa martírio e padecimento desmedido.",
                    "isTrue": True,
                    "explanation": "O animus corrigendi é o divisor de águas entre os maus-tratos (art. 136) e o crime hediondo de tortura da Lei nº 9.455/1997."
                },
                {
                    "statement": "O hospital particular tem a prerrogativa legal de condicionar o atendimento clínico emergencial ao depósito caução prévio de diárias de internação.",
                    "isTrue": False,
                    "explanation": "Tal conduta é criminalizada pelo art. 135-A do Código Penal, protegendo a vida de pacientes sob iminente gravidade médica."
                },
                {
                    "statement": "Se da omissão de socorro resultar a morte previsível do ofendido, a sanção privativa de liberdade do socorrista omisso sofrerá diminuição pela metade.",
                    "isTrue": False,
                    "explanation": "O art. 135, parágrafo único, estatui que a pena da omissão é triplicada quando da ausência de assistência decorre o desfecho letal."
                }
            ],
            "pointers": [
                {"topic": "Omissão de socorro, natureza omissiva pura e impossibilidade de tentativa", "pageRef": 87},
                {"topic": "Exigência de risco pessoal e atuação subsidiária junto à autoridade", "pageRef": 90},
                {"topic": "Condicionamento de atendimento médico emergencial no art. 135-A", "pageRef": 93},
                {"topic": "Maus-tratos, limites da custódia educativa e diferenciação com tortura", "pageRef": 96},
                {"topic": "Qualificadoras de lesão e morte e majorante para menores de 14 anos", "pageRef": 99}
            ]
        }
    })

    summaries.append({
        "id": "direito-penal/a04/s08",
        "fingerprint": get_fp("direito-penal/a04/s08"),
        "analytic": """Este segmento verticaliza a análise dos delitos omissivos e funcionais de solidariedade social inseridos na tutela da pessoa humana: o crime de omissão de socorro, a vedação ao condicionamento de atendimento médico-hospitalar emergencial e o delito de maus-tratos no contexto familiar e pedagógico.

### Omissão de socorro e solidariedade pública
O artigo 135 do Código Penal erige a assistência comunitária em dever jurídico geral, incriminando o ato de:
- Deixar de prestar socorro a criança desamparada, extraviada ou a pessoa ferida, inválida ou em grave e iminente risco vital; ou
- Deixar de solicitar incontinente a assistência das autoridades competentes quando não puder atuar diretamente sem sofrer risco pessoal.

Trata-se de autêntico **crime omissivo próprio ou puro**: consuma-se pela simples inércia injustificada do transeunte no momento em que toma ciência da situação de desamparo alheia. Em face de sua mecânica unissubsistente e instantânea, a tentativa é inadmitida pela unanimidade doutrinária. Caso o socorro físico direto acarrete ameaça real à integridade corporal do socorrista (ex.: vítima se afogando em corredeira turbulenta e o transeunte não domina a natação), o dever direto cessa, surgindo o dever subsidiário irrevogável de telefonar e acionar o corpo de bombeiros ou a polícia.

Se da falta de assistência derivar lesão corporal de feição grave, a reprimenda é **aumentada pela metade**; caso resulte na morte da pessoa necessitada, a sanção é **triplicada** (parágrafo único). Cumpre salientar que aquele que criou a situação perigosa antecedente assume posição de garante (art. 13, § 2º, c) e responderá pelo crime comissivo por omissão imprópria (homicídio culposo ou lesão), e não pelo artigo 135.

### Condicionamento de atendimento médico emergencial
O artigo 135-A criminaliza a conduta de exigir cheque-caução, nota promissória, depósito bancário antecipado ou preenchimento de cadastros administrativos burocráticos como pré-requisito condicionante para deflagrar socorro médico-hospitalar emergencial em favor de pacientes sob risco concreto.

O crime comina pena básica de detenção de três meses a um ano e multa. Trata-se de infração de natureza formal que visa neutralizar o mercantilismo desumano na rede de saúde privada. Caso da demora burocrática abusiva sobrevenha lesão grave, a pena cominada **duplica-se**; se ocasionar o óbito do enfermo, a sanção penal é **triplicada** (parágrafo único).

### Maus-tratos versus crime hediondo de tortura
O artigo 136 tipifica o crime de **Maus-Tratos**, consistente em expor a perigo concreto a higidez corporal ou mental de pessoa subordinada à sua autoridade, guarda ou vigilância para fins de educação, aprendizado, tratamento clínico ou custódia, sujeitando-a a alimentação inadequada, privação de cuidados imperiosos, trabalho desumano extenuante ou violência física corretiva imoderada.

A distinção dogmática nodal entre os maus-tratos e o delito gravíssimo de **Tortura-Castigo** (Lei nº 9.455/1997, art. 1º, II) assenta-se no elemento volitivo subjetivo:
- *Maus-Tratos*: o autor atua dominado pelo **animus corrigendi ou disciplinandi**, isto é, intenta genuinamente educar ou impor disciplina ao sujeito tutelado, extrapolando culposa ou dolosamente os limites do razoável;
- *Tortura*: o autor não pretende educar, mas infligir martírio, castigo doloroso atroz, sofrimento físico ou mental desmedido decorrente de sadismo ou vingança desumanizadora.

O delito de maus-tratos é qualificado caso decorra lesão corporal grave (reclusão de um a quatro anos) ou morte preterdolosa (reclusão de quatro a doze anos), prevendo-se no parágrafo 3º causa de aumento de **um terço** se o fato criminoso for perpetrado contra pessoa menor de 14 anos.

### Para fixar
- A omissão de socorro é crime omissivo puro e formal, não admitindo a figura da tentativa penal.
- A presença de risco pessoal desonera o socorro físico, mas impõe o imediato acionamento da autoridade.
- A sanção da omissão de socorro é exasperada em metade por lesão grave e triplicada em caso de óbito.
- O causador inicial do perigo responde por crime de resultado na qualidade de garante e não pelo art. 135.
- O art. 135-A veda exigir cheque-caução ou preenchimentos burocráticos prévios para urgência hospitalar.
- O condicionamento médico emergencial tem sanção duplicada por lesão grave e triplicada se resultar morte.
- O delito de maus-tratos reclama a presença do animus corrigendi nos atos disciplinares imoderados.
- Se o objetivo for martírio atroz ou sofrimento sádico do tutelado, a conduta transmuta-se para a Lei de Tortura.""",
        "synthetic": [
            "**Omissão de Socorro (art. 135)**: crime omissivo próprio sem tentativa que pune a abstenção solidária perante pessoa desamparada quando ausente risco individual.",
            "**Dever Subsidiário**: constatado o perigo à higidez do socorrista, o socorro mecânico converte-se no dever incontinente de acionar a autoridade policial.",
            "**Majoração no Desfecho Lesivo**: a pena da omissão eleva-se pela metade se decorre lesão grave e triplica-se na hipótese de superveniência de desfecho fatal.",
            "**Condicionamento Médico (art. 135-A)**: tipifica a exigência abusiva de cauções pecuniárias ou formulários para deferir acolhimento de urgência em saúde.",
            "**Agravação da Recusa Hospitalar**: duplica a reprimenda punitiva se sobrevier debilidade corporal grave e triplica na ocorrência de morte do paciente.",
            "**Maus-Tratos (art. 136)**: disciplina abusiva de pessoa sob custódia exercida com excesso disciplinar ou privação de amparo com dolo de correção pedagógica.",
            "**Distinção com a Tortura**: a tortura visa o martírio impiedoso e a dor sádica, distanciando-se do escopo educacional desvirtuado dos maus-tratos.",
            "**Qualificadoras dos Maus-Tratos**: pune o resultado grave preterdoloso com reclusão, elevando a reprimenda em um terço se vitimar menor de 14 anos."
        ]
    })

    return items, summaries
