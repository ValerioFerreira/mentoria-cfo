"""Lote 5: Aula 05 (a05/s01, a05/s02, a05/s04, a05/s05, a05/s06, a05/s07, a05/s08, a05/s09, a05/s10) - 54 questoes (q120 a q173)"""

QUESTOES = [
    # --- a05/s01 (q120 a q125) ---
    {
        "seg": "a05/s01",
        "ans": "A",
        "stem": "No estudo do raciocínio crítico, um argumento é conceituado como uma estrutura de pensamento orientada a fundamentar uma tese. A respeito da estrutura básica de um argumento, assinale a opção correta.",
        "opts": [
            ("A", "Um argumento é composto por premissas que fornecem razões ou evidências para sustentar uma conclusão."),
            ("B", "Um argumento é constituído por proposições independentes sem qualquer vínculo inferencial entre si."),
            ("C", "Um argumento dispensa conclusão formal sempre que suas premissas forem empiricamente comprovadas."),
            ("D", "Um argumento é classificado como uma oração exclamativa que visa demonstrar indignação social."),
            ("E", "Um argumento possui estrutura válida apenas quando formulado por autoridade judiciária competente.")
        ],
        "expl": "A alternativa A está correta. A estrutura essencial de qualquer argumento consiste na articulação de premissas (razões ou evidências) direcionadas a respaldar logicamente a verdade ou aceitabilidade de uma conclusão. As demais opções distorcem os conceitos de premissa, conclusão e inferência."
    },
    {
        "seg": "a05/s01",
        "ans": "B",
        "stem": "Na análise textual de relatórios e depoimentos, conectivos e expressões linguísticas atuam como indicadores de premissa ou de conclusão. Assinale a opção que apresenta exclusivamente indicadores típicos de PREMISSA.",
        "opts": [
            ("A", "Portanto, por conseguinte, logo e desta forma."),
            ("B", "Porque, visto que, já que e dado que."),
            ("C", "Conclui-se que, assim sendo, logo e portanto."),
            ("D", "Em suma, por consequência, de modo que e desse modo."),
            ("E", "Então, segue-se que, daí decorre e por isso.")
        ],
        "expl": "A alternativa B está correta. Expressões como porque, visto que, já que, dado que e pois introduzem as justificativas ou razões que sustentam a conclusão, sendo indicadores clássicos de premissa. As demais opções trazem indicadores típicos de conclusão."
    },
    {
        "seg": "a05/s01",
        "ans": "C",
        "stem": "Considere o texto: 'O acusado não se encontrava na cidade no horário do fato delituoso, conforme atestam os registros de embarque aéreo e as imagens do aeroporto. Portanto, é materialmente impossível que tenha participado da execução direta do homicídio'. Assinale a opção que indica a CONCLUSÃO do argumento exposto.",
        "opts": [
            ("A", "O acusado se encontrava na cidade vizinha durante o horário do delito apurado."),
            ("B", "Os registros de embarque aéreo e as imagens de monitoramento foram adulterados."),
            ("C", "É materialmente impossível que o acusado tenha participado da execução do homicídio."),
            ("D", "A autoridade policial dispensou a oitiva das testemunhas oculares do caso em tela."),
            ("E", "O crime de homicídio foi cometido por comparsas não identificados pela polícia.")
        ],
        "expl": "A alternativa C está correta. A conclusão é a tese sustentada pelas evidências apresentadas, introduzida explicitamente pelo conectivo 'Portanto'. As alegações de que ele não estava na cidade e os registros do aeroporto constituem as premissas fáticas."
    },
    {
        "seg": "a05/s01",
        "ans": "D",
        "stem": "O raciocínio crítico diferencia rigorosamente um argumento de uma simples explicação. A respeito da diferença funcional entre essas duas estruturas discursivas, assinale a opção correta.",
        "opts": [
            ("A", "Uma explicação busca convencer o leitor sobre a veracidade de uma tese controversa e disputada."),
            ("B", "Um argumento trata o fato central como incontroverso e apenas expõe suas causas biológicas ou físicas."),
            ("C", "Argumentos e explicações possuem a mesma função lógica e utilizam os mesmos critérios formais de validade."),
            ("D", "O argumento visa convencer de que uma conclusão é verdadeira; a explicação elucida como um fato incontroverso ocorreu."),
            ("E", "Toda explicação científica constitui formalmente um silogismo dedutivo categórico de três termos.")
        ],
        "expl": "A alternativa D está correta. No argumento, o ponto central é a controvérsia sobre a conclusão, usando-se premissas para provar sua verdade. Na explicação, o fato já é aceito como ocorrido e verdadeiro, e o objetivo do texto é expor as razões causais ou mecanismos de como aquilo veio a acontecer."
    },
    {
        "seg": "a05/s01",
        "ans": "E",
        "stem": "Em uma manifestação técnica, o analista forense escreveu: 'A impressão digital do investigado foi identificada na arma do crime; ademais, o veículo dele foi visto nas imediações do local minutos antes da ocorrência. Logo, há fortes indícios de sua participação no evento criminoso'. Considerando a estrutura lógica desse texto, assinale a opção que indica o papel exercido pelas afirmações sobre a digital e o veículo.",
        "opts": [
            ("A", "Conclusões principais do raciocínio analítico."),
            ("B", "Sentenças abertas desprovidas de valor probatório."),
            ("C", "Contradições formais derivadas de pressupostos falsos."),
            ("D", "Indicadores de conclusão por subordinação aditiva."),
            ("E", "Premissas probatórias destinadas a dar suporte à conclusão final.")
        ],
        "expl": "A alternativa E está correta. As declarações factuais sobre a impressão digital na arma e o veículo visto nas imediações atuam como premissas (razões probatórias) que dão suporte à tese final ('Logo, há fortes indícios de sua participação...'), introduzida pelo conectivo de conclusão 'Logo'."
    },
    {
        "seg": "a05/s01",
        "ans": "A",
        "stem": "Considere o seguinte trecho: 'Visto que a perícia grafotécnica comprovou que a assinatura no cheque não partiu do punho do réu, impõe-se a declaração de sua inocência quanto ao crime de estelionato'. Assinale a opção que identifica corretamente a PREMISSA desse raciocínio.",
        "opts": [
            ("A", "A perícia grafotécnica comprovou que a assinatura no cheque não partiu do punho do réu."),
            ("B", "Impõe-se a declaração de sua inocência quanto ao crime de estelionato."),
            ("C", "O crime de estelionato prescreveu em razão do decurso do prazo legal."),
            ("D", "O cheque em questão não possuía provisão suficiente de fundos bancários."),
            ("E", "O réu cometeu o crime de falsidade ideológica em outro documento público.")
        ],
        "expl": "A alternativa A está correta. A premissa é a razão justificadora introduzida pelo indicador de premissa 'Visto que'. A oração 'impõe-se a declaração de sua inocência...' é a conclusão que se extrai a partir dessa premissa."
    },

    # --- a05/s02 (q126 a q131) ---
    {
        "seg": "a05/s02",
        "ans": "B",
        "stem": "A lógica clássica e a teoria da argumentação dividem as inferências em analíticas (dedutivas) e sintéticas (indutivas e abdutivas). A respeito dessa classificação, assinale a opção correta.",
        "opts": [
            ("A", "Inferências dedutivas produzem conhecimento empírico substancialmente novo em relação às premissas."),
            ("B", "Inferências analíticas explicitam dados das premissas, enquanto inferências sintéticas ampliam o conhecimento."),
            ("C", "Inferências indutivas são sempre avaliadas sob os critérios absolutos de validade ou invalidade dedutiva."),
            ("D", "Inferências abdutivas operam por necessidade lógica formal sem admitir explicações concorrentes."),
            ("E", "Argumentos dedutivos dependem de generalizações empíricas obtidas por amostragem probabilística.")
        ],
        "expl": "A alternativa B está correta. A dedução é uma inferência analítica: a verdade das premissas garante necessariamente a conclusão, sem introduzir fatos novos. As inferências sintéticas (indução e abdução) expandem o conhecimento gerando conclusões prováveis ou explicativas."
    },
    {
        "seg": "a05/s02",
        "ans": "C",
        "stem": "Um investigador observou que, nos últimos vinte arrombamentos a caixas eletrônicos registrados no estado, os autores utilizaram maçaricos de oxiacetileno da mesma marca e modelo. A partir disso, ele concluiu que o próximo arrombamento a ser registrado provavelmente envolverá o uso desse mesmo equipamento. Considerando a natureza dessa inferência, assinale a opção que indica a classificação correta desse raciocínio.",
        "opts": [
            ("A", "Dedutivo válido e necessariamente verdadeiro em qualquer circunstância."),
            ("B", "Silogismo categórico de premissas particulares negativas."),
            ("C", "Indutivo, cuja conclusão é provável e apoiada na regularidade de casos observados."),
            ("D", "Falácia formal de afirmação do antecedente de primeira ordem."),
            ("E", "Tautologia lógica decorrente do princípio do terceiro excluído.")
        ],
        "expl": "A alternativa C está correta. O raciocínio parte da regularidade em casos particulares passados para inferir uma projeção sobre um caso futuro ('provavelmente envolverá o mesmo equipamento'). Trata-se de um raciocínio indutivo típico, que gera probabilidade e não certeza dedutiva."
    },
    {
        "seg": "a05/s02",
        "ans": "D",
        "stem": "Ao chegar ao local de um arrombamento, o perito encontra marcas de sapato de número 42 sobre a lama úmida, ausência de sinais de violação de fechaduras e o sistema de alarme desconectado por código mestre. O perito formula a hipótese de que o crime foi cometido por alguém com acesso interno ao prédio. No âmbito do raciocínio crítico, assinale a opção que indica o nome dessa modalidade de inferência explicativa.",
        "opts": [
            ("A", "Dedução analítica formal."),
            ("B", "Indução estatística pura."),
            ("C", "Falácia do falso dilema."),
            ("D", "Abdução (inferência da melhor explicação)."),
            ("E", "Silogismo disjuntivo exclusivo.")
        ],
        "expl": "A alternativa D está correta. O raciocínio abdutivo parte de vestígios e fatos observados surpreendentes e formula a hipótese mais plausível para explicá-los. É a inferência da melhor explicação, própria da investigação forense preliminar."
    },
    {
        "seg": "a05/s02",
        "ans": "E",
        "stem": "O argumento por analogia sustenta que, se dois elementos compartilham semelhanças relevantes em certos aspectos conhecidos, é provável que compartilhem também outra característica específica. Para que um argumento por analogia seja avaliado como forte no raciocínio crítico, assinale a opção que indica o requisito fundamental a ser atendido.",
        "opts": [
            ("A", "A presença de quantificadores universais em todas as orações comparadas no argumento."),
            ("B", "A ausência de qualquer diferença contextual entre os casos contrapostos no texto."),
            ("C", "A demonstração formal de que a conclusão obtida é uma proposição tautológica."),
            ("D", "A formulação prévia de um silogismo hipotético formado por duas premissas falsas."),
            ("E", "A relevância lógica das semelhanças apontadas e a inexistência de dessemelhanças cruciais.")
        ],
        "expl": "A alternativa E está correta. A força de um argumento por analogia depende da relevância causal e material das semelhanças entre os termos comparados em relação à conclusão, além da ausência de diferenças substanciais que desautorizem o paralelo."
    },
    {
        "seg": "a05/s02",
        "ans": "A",
        "stem": "Considere o seguinte argumento: 'Examinamos 1.500 boletins de ocorrência de furtos em transportes coletivos registrados na região metropolitana durante o último semestre e constatamos que 88% deles ocorreram em horários de pico. Portanto, na região metropolitana, a grande maioria dos furtos em transportes coletivos ocorre nos horários de pico'. A respeito dessa inferência, assinale a opção correta.",
        "opts": [
            ("A", "Trata-se de um argumento indutivo por generalização estatística com conclusão provável."),
            ("B", "Trata-se de um argumento dedutivo formalmente válido com premissas analíticas."),
            ("C", "Trata-se de uma falácia de generalização apressada em razão da exiguidade da amostra."),
            ("D", "Trata-se de um raciocínio abdutivo fundamentado unicamente na intuição do perito."),
            ("E", "Trata-se de um argumento inválido por violação do princípio clássico do terceiro excluído.")
        ],
        "expl": "A alternativa A está correta. O argumento adota uma amostragem ampla e representativa (1.500 ocorrências registradas em um semestre) para inferir uma conclusão probabilística sobre o fenômeno geral na região, constituindo uma generalização indutiva estatística forte."
    },
    {
        "seg": "a05/s02",
        "ans": "B",
        "stem": "Um argumento indutivo é avaliado como FORTE ou FRACO dependendo da sustentação que suas premissas conferem à conclusão. A respeito dos critérios que determinam a força de um argumento indutivo, assinale a opção correta.",
        "opts": [
            ("A", "Um argumento indutivo torna-se dedutivo caso sua amostra represente exatamente metade da população estudada."),
            ("B", "A força indutiva aumenta à medida que a amostra observada é ampla, diversificada e representativa da população."),
            ("C", "A força de um argumento indutivo depende exclusivamente da presença de conectivos de disjunção exclusiva."),
            ("D", "Todo argumento indutivo baseado em mais de dez casos particulares passa a ser necessariamente dedutivo."),
            ("E", "Argumentos indutivos fortes garantem de forma definitiva que sua conclusão nunca poderá ser refutada.")
        ],
        "expl": "A alternativa B está correta. A força indutiva varia em grau: quanto maior, mais representativa e menos enviesada for a amostra examinada, maior será a probabilidade de a conclusão ser verdadeira. Mesmo uma indução forte não gera certeza absoluta dedutiva."
    },

    # --- a05/s04 (q132 a q137) ---
    {
        "seg": "a05/s04",
        "ans": "C",
        "stem": "Durante uma acareação, o defensor de um investigado declarou: 'Não devemos dar crédito ao depoimento da testemunha de acusação, pois ela já foi autuada por contravenção penal no passado e possui conduta pessoal reprovável'. Sob a perspectiva do raciocínio crítico, assinale a opção que indica a falácia informal cometida.",
        "opts": [
            ("A", "Falácia do apelo à autoridade (ad verecundiam)."),
            ("B", "Falácia da afirmação do consequente."),
            ("C", "Falácia do ataque à pessoa (ad hominem)."),
            ("D", "Falácia da petição de princípio circular."),
            ("E", "Falácia da causa falsa (post hoc).")
        ],
        "expl": "A alternativa C está correta. A falácia Ad Hominem ocorre quando se tenta desqualificar uma declaração atacando o caráter, os antecedentes ou a conduta pessoal do emissor, em vez de examinar e refutar o conteúdo das afirmações e evidências apresentadas."
    },
    {
        "seg": "a05/s04",
        "ans": "D",
        "stem": "Em um debate sobre procedimentos de perícia balística, um dos interlocutores afirmou: 'O procedimento adotado pela polícia técnica é falho porque um renomado escritor de novelas policiais declarou publicamente que aquele método não funciona'. Com base no raciocínio crítico, assinale a opção que indica a falácia presente nessa declaração.",
        "opts": [
            ("A", "Falácia do apelo à ignorância (ad ignorantiam)."),
            ("B", "Falácia do falso dilema por exclusão."),
            ("C", "Falácia do espantalho por distorção de depoimento."),
            ("D", "Falácia do apelo à autoridade (ad verecundiam)."),
            ("E", "Falácia do acidente por aplicação de regra geral.")
        ],
        "expl": "A alternativa D está correta. O apelo à autoridade (Ad Verecundiam) torna-se falacioso quando se invoca a opinião de uma figura famosa ou autoridade em uma área (ficção literária) para justificar uma conclusão em um campo técnico que foge à sua competência especializada (perícia balística)."
    },
    {
        "seg": "a05/s04",
        "ans": "E",
        "stem": "Um relatório investigativo continha a seguinte assertiva: 'Não foram encontradas provas conclusivas de que o investigado recebeu vantagem indevida; portanto, está cabalmente provado que ele é completamente inocente e íntegro'. Sob o ponto de vista do raciocínio crítico, assinale a opção que indica a falácia cometida nessa conclusão.",
        "opts": [
            ("A", "Falácia do apelo à autoridade judiciária."),
            ("B", "Falácia do falso dilema por redução de opções."),
            ("C", "Falácia do ataque à pessoa circunstancial."),
            ("D", "Falácia do espantalho por caricaturização."),
            ("E", "Falácia do apelo à ignorância (ad ignorantiam).")
        ],
        "expl": "A alternativa E está correta. A falácia do apelo à ignorância (Ad Ignorantiam) consiste em afirmar que uma proposição é verdadeira apenas porque ainda não foi provada falsa. A ausência temporária de provas incriminatórias não comprova cabalmente a inocência de alguém."
    },
    {
        "seg": "a05/s04",
        "ans": "A",
        "stem": "Um palestrante asseverou aos agentes de segurança: 'Ou nós endurecemos as penas sem qualquer garantia processual, ou a criminalidade tomará conta de todas as instituições públicas do país'. Com base na teoria das falácias, assinale a opção que indica o vício de argumentação presente nessa fala.",
        "opts": [
            ("A", "Falácia do Falso Dilema, ao apresentar apenas duas alternativas extremas excluindo outras opções viáveis."),
            ("B", "Falácia da Petição de Princípio, por apresentar premissas e conclusões estritamente sinônimas."),
            ("C", "Falácia do Apelo à Piedade, por despertar sentimentos de misericórdia e comoção pública."),
            ("D", "Falácia da Conclusão Irrelevante, ao fugir completamente do tema da segurança pública."),
            ("E", "Falácia do Termo Médio Não Distribuído, decorrente de uma inadequação no silogismo categórico.")
        ],
        "expl": "A alternativa A está correta. O Falso Dilema polariza a discussão em duas alternativas radicais e opostas, ignorando deliberadamente que existem outras opções intermediárias razoáveis e legítimas (como inteligência policial e cumprimento regular das normas legais)."
    },
    {
        "seg": "a05/s04",
        "ans": "B",
        "stem": "Durante uma oitiva, o interrogador perguntou ao suspeito: 'Você já parou de esconder o produto do roubo no quintal da sua residência?'. No contexto do raciocínio crítico, assinale a opção que classifica corretamente essa estratégia interrogativa.",
        "opts": [
            ("A", "Falácia da Petição de Princípio por raciocínio circular."),
            ("B", "Falácia da Pergunta Complexa (ou interrogação capciosa)."),
            ("C", "Falácia da Generalização Apressada a partir de caso isolado."),
            ("D", "Falácia da Conclusão Irrelevante com apelo emocional à ordem."),
            ("E", "Falácia da Negação do Antecedente em silogismo condicional.")
        ],
        "expl": "A alternativa B está correta. A Pergunta Complexa (plurium interrogationum) pressupõe um fato não admitido nem provado: qualquer resposta direta ('sim' ou 'não') força o interrogado a validar o pressuposto implícito de que ele escondia o produto do roubo."
    },
    {
        "seg": "a05/s04",
        "ans": "C",
        "stem": "Considere a distinção entre falácias formais e falácias informais. A respeito da falácia formal da afirmação do consequente, assinale a opção correta.",
        "opts": [
            ("A", "A afirmação do consequente decorre exclusivamente do uso de termos ambíguos na língua natural."),
            ("B", "A afirmação do consequente só ocorre em argumentos indutivos que utilizam dados estatísticos enviesados."),
            ("C", "A afirmação do consequente é um vício estrutural dedutivo que independe do conteúdo das proposições."),
            ("D", "A afirmação do consequente decorre de um apelo emocional a sentimentos de medo ou piedade."),
            ("E", "A afirmação do consequente exige a presença obrigatória de quatro premissas afirmativas no argumento.")
        ],
        "expl": "A alternativa C está correta. Falácias formais são defeitos na própria estrutura lógica dedutiva do argumento (como p -> q; q; logo, p), que violam regras de inferência independente do tema tratado. Falácias informais decorrem de defeitos no conteúdo, contexto ou ambiguidade das premissas."
    },

    # --- a05/s05 (q138 a q143) ---
    {
        "seg": "a05/s05",
        "ans": "D",
        "stem": "Em um debate sobre protocolos de segurança, o debatedor A propôs: 'Devemos aumentar o controle biométrico na entrada das delegacias para evitar acessos indevidos'. O debatedor B rebateu dizendo: 'Meu oponente quer transformar as delegacias em fortalezas medievais intransponíveis, impedindo que a população busque socorro policial'. Assinale a opção que indica a falácia cometida pelo debatedor B.",
        "opts": [
            ("A", "Falácia do apelo à autoridade técnica corporativa."),
            ("B", "Falácia do argumento ad hominem abusivo."),
            ("C", "Falácia da petição de princípio por redundância."),
            ("D", "Falácia do espantalho (homem de palha)."),
            ("E", "Falácia do falso escocês por exclusão de cidadãos.")
        ],
        "expl": "A alternativa D está correta. A falácia do Espantalho consiste em distorcer, exagerar ou caricaturar o argumento do adversário para atacar essa versão inventada e frágil, esquivando-se da proposta real originalmente formulada."
    },
    {
        "seg": "a05/s05",
        "ans": "E",
        "stem": "Considere a declaração: 'O relatório produzido pela comissão de sindicância é perfeitamente fidedigno e verdadeiro porque seus autores são funcionários íntegros; e sabemos que seus autores são íntegros porque eles produziram um relatório de sindicância perfeitamente fidedigno e verdadeiro'. Assinale a opção que indica a falácia presente nesse raciocínio.",
        "opts": [
            ("A", "Falácia da conclusão irrelevante (ignoratio elenchi)."),
            ("B", "Falácia da falsa causa por ordenação temporal."),
            ("C", "Falácia do apelo à ignorância por ausência pericial."),
            ("D", "Falácia da generalização apressada documental."),
            ("E", "Falácia da petição de princípio (raciocínio circular).")
        ],
        "expl": "A alternativa E está correta. A Petição de Princípio (raciocínio circular) ocorre quando a conclusão a ser provada é usada como premissa de si mesma de forma disfarçada. Prova-se o relatório pela integridade dos autores e a integridade pelo relatório, sem evidência externa independente."
    },
    {
        "seg": "a05/s05",
        "ans": "A",
        "stem": "Durante uma sindicância para apurar o extravio de armas de um depósito, o sindicado discursou longamente sobre a bravura histórica dos combatentes da corporação e a beleza do brasão institucional, concluindo que o inquérito deveria ser arquivado. Assinale a opção que indica a falácia cometida pelo sindicado.",
        "opts": [
            ("A", "Falácia da conclusão irrelevante (ignoratio elenchi)."),
            ("B", "Falácia da pergunta complexa com pressuposto embutido."),
            ("C", "Falácia da afirmação do consequente em disjunção."),
            ("D", "Falácia da falsa analogia entre forças de segurança."),
            ("E", "Falácia da composição lógica por agregação de dados.")
        ],
        "expl": "A alternativa A está correta. A falácia da Conclusão Irrelevante (Ignoratio Elenchi) manifesta-se quando o orador apresenta razões que podem ser verdadeiras em si mesmas, mas que são irrelevantes para fundamentar a tese em discussão (a apuração do sumiço das armas)."
    },
    {
        "seg": "a05/s05",
        "ans": "B",
        "stem": "Um policial afirmou: 'Nenhum verdadeiro agente de polícia civil aceita cumprir escala extraordinária sem reclamar'. Ao ser lembrado de que o agente Carlos cumpriu a escala sem nenhuma reclamação, o interlocutor retrucou: 'Sim, mas Carlos não é um verdadeiro agente de polícia civil'. Assinale a opção que indica a falácia cometida nessa réplica.",
        "opts": [
            ("A", "Falácia do espantalho por hiperbolização de termos."),
            ("B", "Falácia do falso escocês (nenhum escocês verdadeiro)."),
            ("C", "Falácia do apelo à autoridade das lideranças de classe."),
            ("D", "Falácia do acidente por aplicação de exceção legal."),
            ("E", "Falácia da petição de princípio por redundância vocabular.")
        ],
        "expl": "A alternativa B está correta. A falácia do 'Falso Escocês' ocorre quando uma generalização é desmentida por um contraexemplo concreto e o argumentador, em vez de rever a tese, redefini arbitrariamente o conceito ('verdadeiro agente') apenas para desconsiderar o contraexemplo."
    },
    {
        "seg": "a05/s05",
        "ans": "C",
        "stem": "Em suas alegações finais, o defensor solicitou a absolvição do réu sustentando exclusivamente que: 'O réu é pai de família humilde, possui filhos pequenos que dependem de seu sustento financeiro e sua prisão trará imensa dor e sofrimento a todos os seus parentes'. Sob o ponto de vista do raciocínio crítico, assinale a opção que indica a falácia presente nesse apelo.",
        "opts": [
            ("A", "Falácia do apelo à força ou coação (ad baculum)."),
            ("B", "Falácia do apelo ao consenso popular (ad populum)."),
            ("C", "Falácia do apelo à piedade (ad misericordiam)."),
            ("D", "Falácia do ataque à pessoa circunstancial."),
            ("E", "Falácia do equívoco semântico em termos emotivos.")
        ],
        "expl": "A alternativa C está correta. O apelo à piedade (Argumentum ad Misericordiam) tenta obter concordância ou veredito favorável mobilizando a compaixão ou o sofrimento dos envolvidos, em vez de discutir provas materiais ou fundamentos de direito."
    },
    {
        "seg": "a05/s05",
        "ans": "D",
        "stem": "Considere o raciocínio: 'É dever de todo motorista respeitar o limite de velocidade na via pública; portanto, a viatura policial em perseguição a criminosos armados cometeu ilícito ao ultrapassar o limite de velocidade da avenida'. Assinale a opção que indica a falácia presente nesse argumento.",
        "opts": [
            ("A", "Falácia do apelo à ignorância da autoridade de trânsito."),
            ("B", "Falácia da divisão ao imputar culpa à equipe policial."),
            ("C", "Falácia do falso dilema entre legalidade e perseguição."),
            ("D", "Falácia do acidente (dicto simpliciter)."),
            ("E", "Falácia da petição de princípio na tipificação do ato.")
        ],
        "expl": "A alternativa D está correta. A falácia do Acidente (Dicto Simpliciter) consiste em aplicar rigidamente uma regra geral a uma situação excepcional em que circunstâncias atípicas justificam o afastamento da regra (viatura em perseguição com prerrogativa legal de trânsito)."
    },

    # --- a05/s06 (q144 a q149) ---
    {
        "seg": "a05/s06",
        "ans": "E",
        "stem": "Um relatório apontou: 'Logo após a instalação dos novos refletores de iluminação no pátio da delegacia, o número de boletins de ocorrência registrados diminuiu em 15%. Portanto, a nova iluminação foi a causa direta da redução da criminalidade na região'. Assinale a opção que indica a falácia causal presente nessa conclusão.",
        "opts": [
            ("A", "Falácia da causa insignificante por proporcionalidade."),
            ("B", "Falácia da composição por agregação de patrulhas."),
            ("C", "Falácia do equívoco por ambiguidade vocabular."),
            ("D", "Falácia da anfibologia decorrente da redação do texto."),
            ("E", "Falácia da causa falsa (post hoc ergo propter hoc).")
        ],
        "expl": "A alternativa E está correta. A falácia post hoc ergo propter hoc assume precipitadamente que, por ter ocorrido no tempo antes de outro evento, o primeiro fato é necessariamente a causa do segundo, desconsiderando outras explicações ou fatores concomitantes."
    },
    {
        "seg": "a05/s06",
        "ans": "A",
        "stem": "Em uma entrevista, um gestor atribuiu a queda dos índices de criminalidade em determinado município unicamente à pintura das fachadas dos prédios policiais, ignorando a contratação de quinhentos novos policiais e a integração dos bancos de dados periciais. Assinale a opção que indica a falácia presente nessa explicação causal.",
        "opts": [
            ("A", "Falácia da causa complexa (simplificação excessiva)."),
            ("B", "Falácia da falsa analogia estrutural."),
            ("C", "Falácia da pergunta complexa eleitoral."),
            ("D", "Falácia da divisão de méritos da corporação."),
            ("E", "Falácia do apelo à ignorância documental.")
        ],
        "expl": "A alternativa A está correta. A falácia da Causa Complexa ocorre quando um fenômeno complexo e decorrente de múltiplos fatores interdependentes é simplisticamente atribuído a uma única causa isolada e insuficiente."
    },
    {
        "seg": "a05/s06",
        "ans": "B",
        "stem": "Um perito ambiental constatou que uma fábrica derramou 500 ml de óleo em uma baía que já recebia toneladas de esgoto industrial pesado diariamente. O relatório concluiu que o derramamento dos 500 ml foi a causa principal da mortandade maciça de peixes ocorrida no local. Assinale a opção que aponta a falácia cometida nessa conclusão.",
        "opts": [
            ("A", "Falácia do espantalho contra os réus."),
            ("B", "Falácia da causa insignificante."),
            ("C", "Falácia da petição de princípio técnica."),
            ("D", "Falácia do apelo à piedade ambiental."),
            ("E", "Falácia do acidente na legislação vigente.")
        ],
        "expl": "A alternativa B está correta. A falácia da Causa Insignificante ocorre quando um fator realmente contribui de modo mínimo para um resultado, mas seu impacto é desprezível e secundário quando confrontado com as causas determinantes primárias."
    },
    {
        "seg": "a05/s06",
        "ans": "C",
        "stem": "Considere as afirmações: I. 'Cada um dos policiais deste batalhão é extremamente disciplinado; portanto, este batalhão atuará como a equipe mais integrada do estado'. II. 'A polícia civil é uma instituição secular; logo, todo e qualquer agente policial é um cidadão secular'. Sob o prisma das falácias de ambiguidade estrutural, assinale a opção que identifica, respectivamente, as falácias de I e II.",
        "opts": [
            ("A", "Divisão e Composição."),
            ("B", "Espantalho e Petição de princípio."),
            ("C", "Composição e Divisão."),
            ("D", "Falso dilema e Falsa causa."),
            ("E", "Equívoco e Anfibologia.")
        ],
        "expl": "A alternativa C está correta. A afirmação I comete a falácia da Composição (atribuir ao todo uma característica individual de suas partes). A afirmação II comete a falácia da Divisão (atribuir a cada indivíduo uma propriedade que pertence exclusivamente ao todo institucional)."
    },
    {
        "seg": "a05/s06",
        "ans": "D",
        "stem": "Considere o argumento: 'Todo homem comete faltas funcionais. O presidente do tribunal de ética é homem. Logo, o presidente do tribunal de ética comete faltas funcionais em seus julgamentos'. Sabendo que o termo 'falta' foi utilizado no sentido amplo de falibilidade humana na premissa e no sentido estrito de ilícito funcional na conclusão, assinale a opção que indica a falácia cometida.",
        "opts": [
            ("A", "Falácia da anfibologia sintática por inversão de termos."),
            ("B", "Falácia do apelo à autoridade judiciária competente."),
            ("C", "Falácia da causa complexa por multiplicidade de condutas."),
            ("D", "Falácia do equívoco (ambiguidade lexical)."),
            ("E", "Falácia do falso dilema entre ética e natureza humana.")
        ],
        "expl": "A alternativa D está correta. A falácia do Equívoco ocorre quando uma palavra-chave é empregada com significados semânticos diferentes em premissas distintas ou entre premissa e conclusão, gerando uma conexão puramente aparente e falsa."
    },
    {
        "seg": "a05/s06",
        "ans": "E",
        "stem": "Em um termo de oitiva constava a seguinte frase redigida pelo escrivão: 'O policial viu o suspeito correndo com os seus óculos escuros'. A redação defeituosa não permite esclarecer se os óculos pertenciam ao policial ou ao suspeito. No estudo das falácias de linguagem, assinale a opção que indica o nome desse defeito de ambiguidade estrutural.",
        "opts": [
            ("A", "Petição de princípio processual."),
            ("B", "Generalização apressada fática."),
            ("C", "Equívoco vocabular dicionarizado."),
            ("D", "Falso dilema de identificação visual."),
            ("E", "Anfibologia (ambiguidade sintática).")
        ],
        "expl": "A alternativa E está correta. A Anfibologia é o vício de clareza gerado pela má estruturação sintática da frase, que permite dupla interpretação gramatical do mesmo enunciado decorrente da ambiguidade do pronome possessivo 'seus'."
    },

    # --- a05/s07 (q150 a q155) ---
    {
        "seg": "a05/s07",
        "ans": "A",
        "stem": "Em raciocínio crítico, um 'entimema' é um argumento no qual uma ou mais premissas não foram expressas explicitamente, permanecendo subentendidas como pressupostos. A respeito da identificação de premissas ocultas em argumentos, assinale a opção correta.",
        "opts": [
            ("A", "A premissa oculta é a suposição tácita necessária para que a conclusão decorra com lógica das premissas expressas."),
            ("B", "A premissa oculta é sempre uma contradição lógica que invalida irremediavelmente o argumento formulado."),
            ("C", "A premissa oculta deve constar expressamente nos anexos documentais de todo relatório policial oficial."),
            ("D", "A presença de premissas ocultas transforma automaticamente qualquer dedução em uma falácia formal."),
            ("E", "Identificar premissas ocultas é desnecessário caso a conclusão utilize conectivos de bicondicionalidade.")
        ],
        "expl": "A alternativa A está correta. No raciocínio crítico, a premissa oculta é o pressuposto implícito necessário para que o salto entre premissas declaradas e conclusão faça sentido lógico e sustente a inferência pretendida."
    },
    {
        "seg": "a05/s07",
        "ans": "B",
        "stem": "Considere o argumento: 'O acusado foi visto fugindo do prédio logo após os disparos; logo, foi ele quem realizou os disparos'. Assinale a opção que apresenta a PREMISSA OCULTA essencial para que esse argumento tenha força inferencial.",
        "opts": [
            ("A", "O acusado é residente na comarca onde ocorreram os disparos de arma de fogo."),
            ("B", "Quem fugiu do prédio logo após os disparos foi a pessoa que realizou os disparos."),
            ("C", "A arma do crime foi apreendida dias depois em poder de terceiros não identificados."),
            ("D", "As testemunhas que presenciaram a fuga eram plenamente capacitadas civilmente."),
            ("E", "O prédio contava com sistema de alarme sonoro que não foi acionado durante o delito.")
        ],
        "expl": "A alternativa B está correta. O argumento parte da constatação de que o réu fugiu e conclui que ele foi o atirador. Isso só faz sentido se assumirmos tacitamente que a pessoa em fuga era de fato o atirador (e não alguém fugindo do tiroteio)."
    },
    {
        "seg": "a05/s07",
        "ans": "C",
        "stem": "Considere o argumento: 'O programa de rondas ostensivas nos bairros periféricos reduziu em 30% os roubos de carga naquelas áreas; portanto, a ampliação desse programa extinguirá os roubos de carga em Pernambuco'. Assinale a opção que expressa uma constatação que ENFRAQUECE esse argumento.",
        "opts": [
            ("A", "Os motoristas de carga declararam sentir maior segurança com o aumento do patrulhamento viário."),
            ("B", "A corporação policial dispõe de viaturas modernas aptas a rodar em rodovias e áreas urbanas."),
            ("C", "As quadrilhas adaptaram sua rota para rodovias rurais desprovidas de patrulhamento viável."),
            ("D", "A redução de roubos de carga nos bairros periféricos foi confirmada por auditoria externa independente."),
            ("E", "O custo operacional da ampliação das rondas é compatível com a dotação orçamentária do estado.")
        ],
        "expl": "A alternativa C está correta. Se as quadrilhas apenas migraram de rota para rodovias rurais, o programa não extingue o crime, apenas o desloca, enfraquecendo a tese de que a expansão acabará com o problema no estado."
    },
    {
        "seg": "a05/s07",
        "ans": "D",
        "stem": "Considere o argumento: 'O projeto piloto que instalou câmeras nos uniformes dos policiais em três delegacias reduziu as reclamações por abuso de autoridade em 50%. Logo, a implantação das câmeras em todas as unidades reduzirá tais queixas no estado'. Assinale a opção que FORTALECE esse argumento.",
        "opts": [
            ("A", "O custo das baterias das câmeras aumentou consideravelmente nos últimos dois meses."),
            ("B", "Os policiais das delegacias piloto solicitaram treinamento extra em tecnologia da informação."),
            ("C", "As três delegacias do projeto piloto possuíam perfil administrativo muito discrepante das demais."),
            ("D", "Estudos em outros estados demonstraram que a redução de abusos ocorre em delegacias de perfis variados."),
            ("E", "Alguns cidadãos manifestaram desconfiança quanto ao armazenamento sigiloso das gravações.")
        ],
        "expl": "A alternativa D está correta. A demonstração de que o efeito positivo se repete de forma consistente em contextos heterogêneos valida a generalização pretendida pelo argumento, fortalecendo sua conclusão."
    },
    {
        "seg": "a05/s07",
        "ans": "E",
        "stem": "Um delegado declarou: 'Se intensificarmos o treinamento em técnicas de interrogatório com base em evidências, o índice de confissões falsas diminuirá substancialmente'. Assinale a opção que expressa o pressuposto implícito dessa declaração.",
        "opts": [
            ("A", "Todo investigado submetido a interrogatório policial confessa necessariamente o delito apurado."),
            ("B", "As confissões falsas decorrem exclusivamente da má-fé intencional de todos os investigadores."),
            ("C", "A legislação processual penal brasileira proíbe qualquer modalidade de confissão voluntária."),
            ("D", "O treinamento em técnicas de interrogatório é a única atribuição funcional das academias de polícia."),
            ("E", "Parte relevante das confissões falsas decorre do uso de técnicas inadequadas que o treinamento mitigará.")
        ],
        "expl": "A alternativa E está correta. Para que o treinamento diminua as confissões falsas, é indispensável assumir a premissa de que tais confissões decorrem, em medida substancial, de métodos de interrogatório deficientes que serão aperfeiçoados pelo novo treinamento."
    },
    {
        "seg": "a05/s07",
        "ans": "A",
        "stem": "Em uma avaliação crítica de argumentos, assinale a opção que expressa uma técnica metodológica legítima para demonstrar a fraqueza de uma premissa causal defendida pelo interlocutor.",
        "opts": [
            ("A", "Apresentar uma causa alternativa plausível capaz de explicar o efeito sem a necessidade do fator apontado."),
            ("B", "Proferir insultos pessoais acerca da reputação profissional do autor do argumento causal."),
            ("C", "Reescrever o argumento causal substituindo os substantivos por termos arcaicos da língua portuguesa."),
            ("D", "Ignorar o conteúdo empírico das premissas e exigir que a conclusão seja formulada como tautologia."),
            ("E", "Afirmar que toda relação de causa e efeito viola os princípios da lógica formal bivalente.")
        ],
        "expl": "A alternativa A está correta. Demonstrar a viabilidade de uma causa alternativa plausível enfraquece o argumento causal original, pois desfaz o suposto vínculo necessário ou exclusivo entre o fator alegado e o efeito ocorrido."
    },

    # --- a05/s08 (q156 a q161) ---
    {
        "seg": "a05/s08",
        "ans": "B",
        "stem": "Em uma plenária pública sobre reformas legislativas, um debatedor afirmou: 'A população inteira acredita que as penalidades devem ser aumentadas sumariamente para qualquer delito; portanto, essa medida é juridicamente justa e logicamente irrefutável'. Assinale a opção que indica a falácia cometida nesse argumento.",
        "opts": [
            ("A", "Falácia do apelo à piedade (ad misericordiam)."),
            ("B", "Falácia do apelo ao povo (ad populum)."),
            ("C", "Falácia do apelo à autoridade judiciária."),
            ("D", "Falácia do termo médio não distribuído."),
            ("E", "Falácia da generalização apressada laboratorial.")
        ],
        "expl": "A alternativa B está correta. O Argumentum ad Populum apela à aceitação geral ou crença da maioria para validar a verdade ou justeza de uma tese, confundindo popularidade com veracidade factual e validade lógica."
    },
    {
        "seg": "a05/s08",
        "ans": "C",
        "stem": "Um articulista argumentou: 'Se autorizarmos o uso de termos simplificados em memorandos administrativos da delegacia, logo os agentes deixarão de usar o vernáculo culto; em seguida, os inquéritos serão redigidos em gírias de rua; e, ao final, o sistema de persecução penal ruirá por completo'. Assinale a opção que indica a falácia presente nessa alegação.",
        "opts": [
            ("A", "Falácia da petição de princípio por redundância."),
            ("B", "Falácia da falsa dicotomia por exclusão."),
            ("C", "Falácia da ladeira escorregadia (slippery slope)."),
            ("D", "Falácia da conclusão irrelevante universal."),
            ("E", "Falácia do espantalho por desqualificação sintática.")
        ],
        "expl": "A alternativa C está correta. A Ladeira Escorregadia (Slippery Slope) assume indevidamente que uma concessão inicial moderada desencadeará uma reação em cadeia inexorável culminando em um desastre extremo, sem demonstrar a necessidade lógica de cada etapa."
    },
    {
        "seg": "a05/s08",
        "ans": "D",
        "stem": "Considere o diálogo em uma comissão disciplinar: O membro A apontou: 'Os dados apontam que o agente cometeu desvio de conduta ao faltar três plantões sem justificativa médica'. O membro B rebateu: 'Não podemos admitir essa conclusão, pois o agente é o presidente do nosso grêmio recreativo e sua punição causará revolta nos associados'. Assinale a opção que indica a falácia da manifestação de B.",
        "opts": [
            ("A", "Falácia do apelo à ignorância por carência de laudos."),
            ("B", "Falácia do acidente por aplicação de regra geral."),
            ("C", "Falácia do equívoco semântico em termos funcionais."),
            ("D", "Falácia do apelo às consequências (ad consequentiam)."),
            ("E", "Falácia da composição por somatório de condutas.")
        ],
        "expl": "A alternativa D está correta. O Argumentum ad Consequentiam rejeita um fato ou tese objetiva com base no desconforto ou nas consequências indesejáveis que decorreriam de sua admissão, sem refutar a veracidade fática da acusação."
    },
    {
        "seg": "a05/s08",
        "ans": "E",
        "stem": "Durante uma acareação, o suspeito A declarou ao suspeito B: 'Você cometeu o furto porque foi flagrado na cena do crime'. O suspeito B rebateu: 'Você não tem moral para me acusar disso, pois você também foi indiciado por estelionato no ano passado'. Assinale a opção que indica a modalidade de falácia presente na resposta de B.",
        "opts": [
            ("A", "Falácia do apelo à autoridade policial da comarca."),
            ("B", "Falácia do falso dilema por exclusão de comparsas."),
            ("C", "Falácia da pergunta complexa com pressuposto embutido."),
            ("D", "Falácia do espantalho por caricaturização de dados."),
            ("E", "Falácia do tu quoque (você também).")
        ],
        "expl": "A alternativa E está correta. O argumento 'Tu Quoque' (você também) é uma espécie de ad hominem que busca desviar uma acusação devolvendo uma acusação equivalente contra o próprio acusador, sem refutar a verdade da imputação feita."
    },
    {
        "seg": "a05/s08",
        "ans": "A",
        "stem": "Em um debate sobre admissibilidade de provas, o promotor alegou: 'Devemos aceitar as provas obtidas por interceptação telefônica sem autorização judicial prévia, porque, se não o fizermos, criminosos de alta periculosidade serão soltos nas ruas'. Sob a ótica do raciocínio crítico, assinale a opção que indica a falácia cometida nesse argumento.",
        "opts": [
            ("A", "Falácia do apelo às consequências e ao medo (ad baculum / ad consequentiam)."),
            ("B", "Falácia da afirmação do consequente em silogismo."),
            ("C", "Falácia da generalização precipitada por amostra nula."),
            ("D", "Falácia do falso escocês por preconceito regional."),
            ("E", "Falácia da petição de princípio com termos anfibológicos.")
        ],
        "expl": "A alternativa A está correta. O argumento apela ao medo das consequências sociais (soltura de criminosos) para coagir a aceitação de uma conduta que afronta preceitos de legalidade, esquivando-se da discussão jurídica sobre a validade da prova."
    },
    {
        "seg": "a05/s08",
        "ans": "B",
        "stem": "Um perito assistente contestou o laudo oficial emitido pelo perito criminal afirmando: 'O laudo oficial deve ser totalmente desconsiderado porque o perito oficial é funcionário público concursado e, portanto, tem interesse em defender a posição do Estado'. Assinale a opção que identifica a falácia cometida nessa manifestação.",
        "opts": [
            ("A", "Falácia do apelo à ignorância da acusação."),
            ("B", "Falácia ad hominem circunstancial."),
            ("C", "Falácia do falso dilema entre Estado e sociedade."),
            ("D", "Falácia do acidente por generalização pericial."),
            ("E", "Falácia da composição por somatório de laudos.")
        ],
        "expl": "A alternativa B está correta. O Ad Hominem Circunstancial ataca o cargo, vínculo ou circunstâncias da pessoa para invalidar suas conclusões técnicas, sem demonstrar nenhuma falha material no conteúdo do laudo emitido."
    },

    # --- a05/s09 (q162 a q167) ---
    {
        "seg": "a05/s09",
        "ans": "C",
        "stem": "Na análise estrutural de argumentos complexos presentes em inquéritos policiais, é comum encontrar premissas intermediárias (ou subconclusões). A respeito das premissas intermediárias, assinale a opção correta.",
        "opts": [
            ("A", "Premissas intermediárias são proposições contingentes que não possuem relação lógica com o texto."),
            ("B", "Premissas intermediárias são sentenças abertas que dependem de quantificadores existenciais."),
            ("C", "Premissas intermediárias decorrem de premissas prévias e servem de premissa para a conclusão final."),
            ("D", "Premissas intermediárias atuam sempre como falácias formais de afirmação do consequente."),
            ("E", "Premissas intermediárias devem ser eliminadas do raciocínio por violarem o princípio da identidade.")
        ],
        "expl": "A alternativa C está correta. Em argumentos complexos, uma subconclusão é derivada de premissas básicas anteriores e funciona, por sua vez, como premissa para embasar a conclusão final do raciocínio."
    },
    {
        "seg": "a05/s09",
        "ans": "D",
        "stem": "O raciocínio crítico classifica as premissas de um argumento de acordo com sua articulação lógica em 'dependentes' (copulativas) ou 'independentes' (convergentes). Assinale a opção que descreve a característica das premissas DEPENDENTES.",
        "opts": [
            ("A", "Premissas dependentes fornecem sustentação autônoma, de modo que a refutação de uma não afeta as demais."),
            ("B", "Premissas dependentes só podem ser empregadas em argumentos indutivos fracos."),
            ("C", "Premissas dependentes decorrem obrigatoriamente de falácias de ambiguidade semântica."),
            ("D", "Premissas dependentes atuam de forma conjunta, de modo que a falsidade de uma compromete o suporte da conclusão."),
            ("E", "Premissas dependentes operam como contradições dialéticas que se anulam mutuamente.")
        ],
        "expl": "A alternativa D está correta. Premissas dependentes (ou conjuntas) precisam uma da outra para fornecer suporte à conclusão. Se uma delas for falsa, a linha inferencial inteira é comprometida."
    },
    {
        "seg": "a05/s09",
        "ans": "E",
        "stem": "Em contraposição às premissas dependentes, as premissas INDEPENDENTES (ou convergentes) em um argumento crítico caracterizam-se por uma propriedade específica. A esse respeito, assinale a opção correta.",
        "opts": [
            ("A", "Dependerem exclusivamente do princípio de explosão da lógica clássica bivalente."),
            ("B", "Exigirem a presença mútua de conectivos bicondicionais em todas as proposições componentes."),
            ("C", "Formarem um raciocínio circular fechado desprovido de conclusão verificável."),
            ("D", "Serem idênticas entre si na redação de suas orações declarativas componentes."),
            ("E", "Fornecerem linhas autônomas de sustentação, subsistindo o suporte mesmo caso uma delas seja refutada.")
        ],
        "expl": "A alternativa E está correta. Em argumentos convergentes, cada premissa fornece uma razão independente para sustentar a conclusão. A queda ou descarte de uma das premissas não destrói o apoio oferecido pelas demais."
    },
    {
        "seg": "a05/s09",
        "ans": "A",
        "stem": "Considere o texto: 'As câmeras de segurança filmaram o momento da subtração dos bens (P1). Além disso, duas testemunhas idôneas reconheceram formalmente o suspeito na delegacia (P2). Ademais, a res furtiva foi apreendida na posse direta dele sem justificativa lícita (P3). Conclui-se, com absoluta segurança, pela autoria delitiva do suspeito (C)'. Em relação à articulação das premissas P1, P2 e P3, assinale a opção correta.",
        "opts": [
            ("A", "P1, P2 e P3 são premissas independentes (convergentes), pois cada uma delas oferece suporte probatório autônomo."),
            ("B", "P1, P2 e P3 são premissas dependentes, cuja queda de uma desqualifica integralmente as outras duas."),
            ("C", "P1 atua como premissa maior e P2 atua como termo médio de um silogismo aristotélico puro."),
            ("D", "P3 é uma premissa oculta que decorre por dedução analítica necessária da premissa P1."),
            ("E", "O argumento é logicamente nulo por apresentar excesso de razões probatórias convergentes.")
        ],
        "expl": "A alternativa A está correta. P1 (filmagens), P2 (reconhecimento testemunhal) e P3 (apreensão do bem) constituem linhas de prova autônomas que convergem para fundamentar a mesma conclusão de autoria delitiva."
    },
    {
        "seg": "a05/s09",
        "ans": "B",
        "stem": "Considere o seguinte trecho de relatório pericial: 'O veículo foi abastecido com combustível adulterado. Logo, os bicos injetores sofreram corrosão severa. Por conseguinte, o motor sofreu pane mecânica irreversível que paralisou o veículo na via pública'. Assinale a opção que identifica corretamente a CONCLUSÃO PRINCIPAL desse argumento complexo.",
        "opts": [
            ("A", "O veículo foi abastecido com combustível adulterado."),
            ("B", "O motor sofreu pane mecânica irreversível que paralisou o veículo na via pública."),
            ("C", "Os bicos injetores sofreram corrosão severa."),
            ("D", "O posto de combustíveis cometeu infração contra as relações de consumo."),
            ("E", "O motorista agiu com imperícia ao trafegar com o veículo em pane.")
        ],
        "expl": "A alternativa B está correta. A conclusão principal é o objetivo final do argumento ('o motor sofreu pane mecânica irreversível...'), introduzida por 'Por conseguinte'. A corrosão dos bicos atua como conclusão intermediária."
    },
    {
        "seg": "a05/s09",
        "ans": "C",
        "stem": "Em um texto de argumentação crítica, saber localizar a tese central é essencial para avaliar sua consistência. A respeito dos métodos para identificar a CONCLUSÃO PRINCIPAL de um texto longo, assinale a opção correta.",
        "opts": [
            ("A", "A conclusão principal deve sempre constar obrigatoriamente na primeira oração do primeiro parágrafo do texto."),
            ("B", "A conclusão principal é sempre a sentença mais curta e que não contém substantivos abstratos."),
            ("C", "A conclusão principal é a afirmação central que todas as demais premissas e subconclusões visam sustentar."),
            ("D", "A conclusão principal coincide sempre com a definição dicionarizada dos termos empregados nas premissas."),
            ("E", "A conclusão principal só pode ser identificada se o texto tiver sido redigido por autoridade judicial.")
        ],
        "expl": "A alternativa C está correta. A conclusão principal é a tese basilar e definitiva defendida pelo autor, para a qual convergem e se subordinam todas as premissas e conclusões intermediárias do texto."
    },

    # --- a05/s10 (q168 a q173) ---
    {
        "seg": "a05/s10",
        "ans": "D",
        "stem": "O método do contraexemplo é um dos recursos mais decisivos para a refutação crítica de argumentos dedutivos ou teses universais. Acerca do emprego do contraexemplo no raciocínio crítico, assinale a opção correta.",
        "opts": [
            ("A", "Um contraexemplo serve para confirmar a validade universal de uma tese dedutiva."),
            ("B", "Para refutar uma condicional, o contraexemplo deve apresentar antecedente falso e consequente verdadeiro."),
            ("C", "O contraexemplo é uma falácia informal que não tem aceitação na lógica clássica."),
            ("D", "A exibição de um único caso com premissas verdadeiras e conclusão falsa refuta a validade de um argumento dedutivo."),
            ("E", "Contraexemplos só são aceitos caso fundamentados em dados estatísticos com amostra superior a mil casos.")
        ],
        "expl": "A alternativa D está correta. Um argumento dedutivo só é válido se for impossível ter premissas verdadeiras e conclusão falsa. Um único caso em que as premissas ocorrem e a conclusão não ocorre (contraexemplo) prova categoricamente que o argumento é inválido."
    },
    {
        "seg": "a05/s10",
        "ans": "E",
        "stem": "Em uma análise crítica de depoimentos testemunhais contraditórios, o perito avalia a consistência lógica interna das narrativas. A respeito de um conjunto de afirmações classificado como INTERNAMENTE INCONSISTENTE, assinale a opção correta.",
        "opts": [
            ("A", "Todas as suas proposições possuem mais de dez palavras por oração."),
            ("B", "Contém orações afirmativas e orações negativas no mesmo parágrafo."),
            ("C", "Foi formulado por mais de duas testemunhas oculares simultaneamente."),
            ("D", "Apresenta termos da língua falada coloquial não dicionarizados."),
            ("E", "Contém afirmações que geram contradição mútua, não podendo ser todas verdadeiras simultaneamente.")
        ],
        "expl": "A alternativa E está correta. A inconsistência interna decorre da presença de proposições mutuamente incompatíveis ou contraditórias dentro do próprio relato, de modo que é impossível que todas sejam verdadeiras sob qualquer interpretação."
    },
    {
        "seg": "a05/s10",
        "ans": "A",
        "stem": "Um estudo estatístico concluiu que '95% dos aprovados no concurso da polícia civil estudaram por materiais digitais'. O analista crítico questionou a força desse argumento apontando que a pesquisa entrevistou apenas 20 candidatos aprovados, todos pertencentes a uma mesma turma de curso online especializado. Diante disso, assinale a opção que aponta o foco correto dessa refutação.",
        "opts": [
            ("A", "O tamanho exíguo e o viés da amostra utilizada, demonstrando a fragilidade da generalização indutiva realizada."),
            ("B", "A validade formal dedutiva da tabela-verdade do argumento por absurdo."),
            ("C", "O caráter ético e moral dos candidatos que participaram do certame público."),
            ("D", "A legalidade do concurso público homologado pela banca organizadora."),
            ("E", "A natureza tautológica intrínseca das conclusões probabilísticas.")
        ],
        "expl": "A alternativa A está correta. O analista questionou a representatividade da amostra: 20 pessoas colhidas em um curso online é uma amostra reduzida e altamente enviesada para fundamentar uma generalização universal sobre todos os aprovados."
    },
    {
        "seg": "a05/s10",
        "ans": "B",
        "stem": "Para refutar um argumento por analogia, o método do raciocínio crítico orienta a apontar dessemelhanças fundamentais entre os casos comparados. Considere o argumento: 'Assim como um comandante militar em guerra não deve pedir autorização judicial para atacar o inimigo, a autoridade policial não deveria precisar de mandado para invadir domicílios suspeitos'. Diante disso, assinale a opção que indica a refutação crítica adequada.",
        "opts": [
            ("A", "A corporação policial não possui efetivo compatível com as forças armadas do país."),
            ("B", "A analogia confunde guerra externa entre Estados com segurança pública sob garantias constitucionais do cidadão."),
            ("C", "Os comandantes militares sempre dependem de mandados expedidos pela justiça militar comum."),
            ("D", "O mandado de busca e apreensão só pode ser cumprido por equipes de operações especiais."),
            ("E", "A analogia comete a falácia formal de afirmação do antecedente dedutivo.")
        ],
        "expl": "A alternativa B está correta. A refutação ataca a dessemelhança essencial entre as situações: o regime extraordinário da guerra externa não serve de paradigma para a atividade policial ordinária em um Estado Democrático de Direito, no qual impera a garantia constitucional da inviolabilidade do domicílio."
    },
    {
        "seg": "a05/s10",
        "ans": "C",
        "stem": "Um parecer policial sobre o desarmamento de suspeitos continha premissas sólidas sobre a periculosidade do porte ilegal de armas, mas concluiu propondo o cancelamento das folgas compensatórias dos escrivães de polícia da comarca. Sob a ótica da avaliação crítica de argumentos, assinale a opção que indica a falha metodológica desse parecer.",
        "opts": [
            ("A", "Ambiguidade sintática na definição dos termos funcionais."),
            ("B", "Inconsistência empírica por ausência de dados estatísticos."),
            ("C", "Falta de relevância lógica, pois as premissas não guardam pertinência temática com a conclusão."),
            ("D", "Violação do princípio do terceiro excluído da lógica clássica."),
            ("E", "Falsa causa post hoc ergo propter hoc nos prazos recursais.")
        ],
        "expl": "A alternativa C está correta. O parecer comete grave falha de relevância temática (non sequitur): ainda que as premissas sobre desarmamento sejam verdadeiras, elas são totalmente impertinentes para justificar a supressão de folgas compensatórias de escrivães."
    },
    {
        "seg": "a05/s10",
        "ans": "D",
        "stem": "Na síntese dos critérios de avaliação de argumentos no raciocínio crítico, o protocolo clássico de verificação exige o cumprimento de três condições fundamentais para que um argumento seja aceitável. Assinale a opção que indica corretamente essas três condições.",
        "opts": [
            ("A", "Conectivos condicionais, quantificadores universais e ausência de orações subordinadas."),
            ("B", "Reconhecimento notarial das premissas, autoridade hierárquica e fé pública do autor."),
            ("C", "Formulação em linguagem jurídica formal, extensão curta das frases e sinonímia dicionarizada."),
            ("D", "Aceitabilidade das premissas, relevância lógica das premissas e suficiência das premissas para a conclusão."),
            ("E", "Tabela-verdade tautológica, ausência de sentenças declarativas e comprovação empírica em laboratório.")
        ],
        "expl": "A alternativa D está correta. O modelo clássico de raciocínio crítico (critérios ARS) estabelece que um argumento só é cogente se atender a três exigências: (1) aceitabilidade de suas premissas; (2) relevância lógica e temática das premissas para a tese; e (3) suficiência das premissas para fundamentar a conclusão."
    }
]
