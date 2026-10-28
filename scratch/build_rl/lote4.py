"""Lote 4: Aula 04 (a04/s01, a04/s02, a04/s04, a04/s07, a04/s08, a04/s09, a04/s10, a04/s11, a04/s12) - 54 questoes (q66 a q119)"""

QUESTOES = [
    # --- a04/s01 (q66 a q71) ---
    {
        "seg": "a04/s01",
        "ans": "B",
        "stem": "Nas questões clássicas de raciocínio lógico envolvendo conectivos, o enunciado apresenta proposições que devem ser consideradas verdadeiras para se deduzir uma consequência necessária. Acerca do método sistemático de resolução desse tipo de problema, assinale a opção correta.",
        "opts": [
            ("A", "Deve-se atribuir aleatoriamente o valor falso a todas as proposições para encontrar um contraexemplo."),
            ("B", "Deve-se buscar inicialmente uma proposição simples isolada, uma conjunção verdadeira ou uma disjunção falsa para fixar valores lógicos unívocos."),
            ("C", "Deve-se construir obrigatoriamente a tabela-verdade com todas as combinações possíveis antes de analisar as premissas."),
            ("D", "As condicionais presentes no enunciado devem ser invertidas para transformar todas as proposições em bicondicionais."),
            ("E", "A ordem em que os valores lógicos são atribuídos não guarda qualquer relevância para a consistência da dedução.")
        ],
        "expl": "A alternativa B está correta. O método eficiente em questões clássicas de conectivos consiste em buscar o ponto de partida que determine valores lógicos únicos: proposições simples dadas como verdadeiras, conjunções verdadeiras (em que ambas as parcelas são V) ou disjunções falsas (em que ambas são F). A partir desse ponto seguro, propagam-se os valores para as demais condicionais e disjunções."
    },
    {
        "seg": "a04/s01",
        "ans": "C",
        "stem": "Considere verdadeiras as seguintes afirmações sobre a rotina da delegacia: (1) Se Carlos é agente de plantão, então Marcos é o escrivão responsável; (2) Carlos é agente de plantão. Com base nessas premissas, assinale a opção que expressa uma conclusão logicamente necessária.",
        "opts": [
            ("A", "Carlos não é agente de plantão."),
            ("B", "Marcos não é o escrivão responsável."),
            ("C", "Marcos é o escrivão responsável."),
            ("D", "Carlos e Marcos faltaram ao plantão policial."),
            ("E", "Não é possível deduzir a função exercida por Marcos.")
        ],
        "expl": "A alternativa C está correta. A estrutura dada é a aplicação direta da regra de inferência válida Modus Ponens: se temos p -> q verdadeira e a premissa afirmativa p verdadeira ('Carlos é agente de plantão'), decorre com certeza lógica e matemática que o consequente q é verdadeiro ('Marcos é o escrivão responsável')."
    },
    {
        "seg": "a04/s01",
        "ans": "D",
        "stem": "Considere verdadeiras as seguintes afirmações apuradas pela corregedoria: (1) Ou o agente Bruno realizou a diligência, ou o agente Tiago realizou a diligência; (2) O agente Bruno realizou a diligência. Sabendo que a primeira afirmação é uma disjunção exclusiva, assinale a opção correta.",
        "opts": [
            ("A", "O agente Tiago também realizou a diligência."),
            ("B", "Nenhum dos dois agentes realizou a diligência apurada."),
            ("C", "A declaração do agente Bruno é comprovadamente falsa."),
            ("D", "O agente Tiago não realizou a diligência."),
            ("E", "Ambos os agentes participaram conjuntamente da operação policial.")
        ],
        "expl": "A alternativa D está correta. Em uma disjunção exclusiva verdadeira (p ou exclusivo q), exatamente uma das proposições é verdadeira e a outra é obrigatoriamente falsa. Como foi dado como verdadeiro que o agente Bruno realizou a diligência (p = V), decorre necessariamente que a proposição referente ao agente Tiago deve ser falsa (q = F), isto é, Tiago não realizou a diligência."
    },
    {
        "seg": "a04/s01",
        "ans": "E",
        "stem": "Considere verdadeiras as seguintes afirmações: (1) Se o suspeito estava armado, então cometeu crime de porte ilegal; (2) O suspeito não cometeu crime de porte ilegal. Com base nessas premissas, assinale a opção que expressa uma dedução logicamente válida.",
        "opts": [
            ("A", "O suspeito cometeu outro crime afiançável."),
            ("B", "O suspeito foi liberado mediante fiança arbitrada pela autoridade policial."),
            ("C", "O suspeito estava armado no momento da abordagem policial."),
            ("D", "Não se pode extrair nenhuma conclusão sobre o fato de o suspeito estar ou não armado."),
            ("E", "O suspeito não estava armado.")
        ],
        "expl": "A alternativa E está correta. Temos a condicional p -> q verdadeira e a negação do consequente ~q verdadeira ('o suspeito não cometeu crime de porte ilegal'). Pela regra de inferência válida do Modus Tollens, a conclusão necessária e inquestionável é a negação do antecedente ~p: 'O suspeito não estava armado'."
    },
    {
        "seg": "a04/s01",
        "ans": "A",
        "stem": "Em uma investigação policial, sabe-se que a afirmação: 'O mandado foi expedido e a equipe tática foi acionada' é VERDADEIRA. A partir dessa informação, assinale a opção que expressa uma conclusão logicamente correta.",
        "opts": [
            ("A", "O mandado foi expedido e a equipe tática foi acionada, sendo ambas as proposições simples verdadeiras."),
            ("B", "A equipe tática não foi acionada, mas o mandado foi devidamente expedido."),
            ("C", "Basta que o mandado tenha sido expedido para justificar a falsidade da segunda parte."),
            ("D", "A proposição é uma disjunção que admite a falsidade de uma das orações."),
            ("E", "A proposição composta acima classifica-se formalmente como uma contradição lógica.")
        ],
        "expl": "A alternativa A está correta. Uma conjunção p e q só assume valor lógico verdadeiro em sua tabela-verdade quando ambas as proposições componentes são verdadeiras simultaneamente. Assim, 'o mandado foi expedido' é uma proposição verdadeira e 'a equipe tática foi acionada' é igualmente uma proposição verdadeira."
    },
    {
        "seg": "a04/s01",
        "ans": "B",
        "stem": "Considere verdadeiras as afirmações: (1) Se Lucas estuda a legislação, é aprovado no concurso; (2) Se Lucas é aprovado no concurso, toma posse no cargo policial; (3) Lucas não tomou posse no cargo policial. A partir dessas afirmações, assinale a opção que apresenta uma conclusão verdadeira.",
        "opts": [
            ("A", "Lucas foi aprovado no concurso público."),
            ("B", "Lucas não estudou a legislação."),
            ("C", "Lucas tomou posse no cargo com atraso justificado."),
            ("D", "Lucas estudou a legislação, mas recusou a posse."),
            ("E", "Não é possível deduzir se Lucas estudou ou não a legislação.")
        ],
        "expl": "A alternativa B está correta. A premissa 3 afirma que Lucas não tomou posse (~t). Na premissa 2 (a -> t), aplicando Modus Tollens com ~t, conclui-se que Lucas não foi aprovado (~a). Na premissa 1 (e -> a), aplicando Modus Tollens com ~a, conclui-se com rigor dedutivo que Lucas não estudou a legislação (~e)."
    },

    # --- a04/s02 (q72 a q77) ---
    {
        "seg": "a04/s02",
        "ans": "C",
        "stem": "No âmbito do raciocínio lógico, um argumento é composto por premissas e por uma conclusão. A respeito da definição estrutural de um argumento dedutivo, assinale a opção correta.",
        "opts": [
            ("A", "Um argumento dedutivo é válido quando sua conclusão for uma proposição faticamente verdadeira no mundo real."),
            ("B", "Um argumento dedutivo é classificado como uma proposição simples que não admite conectivos."),
            ("C", "Um argumento dedutivo é uma construção lógica em que a verdade das premissas pretende garantir de forma necessária a verdade da conclusão."),
            ("D", "Um argumento dedutivo sempre produz conhecimento novo e empírico não contido nas premissas."),
            ("E", "Um argumento dedutivo torna-se inválido sempre que contiver proposições com valores falsos.")
        ],
        "expl": "A alternativa C está correta. Em um argumento dedutivo, a relação entre premissas e conclusão é de necessidade lógica estrita: a verdade das premissas fornece garantia definitiva e conclusiva para a verdade da conclusão, de modo que toda a informação da conclusão já se encontra implícita nas premissas."
    },
    {
        "seg": "a04/s02",
        "ans": "D",
        "stem": "A lógica de argumentação estabelece uma distinção rigorosa entre a validade de um argumento e a verdade de suas proposições componentes. A esse respeito, assinale a opção correta.",
        "opts": [
            ("A", "Validade é propriedade das proposições individuais, enquanto verdade é propriedade do argumento como um todo."),
            ("B", "Todo argumento composto por premissas verdadeiras é necessariamente um argumento dedutivo válido."),
            ("C", "A validade de um argumento dedutivo depende estritamente da veracidade empírica de seus dados históricos."),
            ("D", "A validade é uma propriedade puramente formal da estrutura do argumento, enquanto a verdade diz respeito ao conteúdo das proposições em relação aos fatos."),
            ("E", "Um argumento que possua premissas falsas é obrigatoriamente classificado como inválido.")
        ],
        "expl": "A alternativa D está correta. A validade é um conceito estritamente formal e estrutural que qualifica argumentos (não proposições): um argumento é válido quando é impossível que sua conclusão seja falsa caso suas premissas sejam verdadeiras. A verdade ou falsidade, por sua vez, é propriedade exclusiva das proposições (juízos declarativos sobre a realidade)."
    },
    {
        "seg": "a04/s02",
        "ans": "E",
        "stem": "Um argumento dedutivo é considerado INVÁLIDO quando ocorre uma determinada situação na valoração lógica de seus elementos estruturais. Assinale a opção que define com exatidão essa situação.",
        "opts": [
            ("A", "Quando todas as suas premissas forem proposições falsas."),
            ("B", "Quando a conclusão for uma tautologia lógica comprovada."),
            ("C", "Quando as premissas e a conclusão forem simultaneamente verdadeiras."),
            ("D", "Quando contiver exatamente três termos e duas premissas afirmativas."),
            ("E", "Quando for logicamente possível que todas as suas premissas sejam verdadeiras e a sua conclusão seja falsa.")
        ],
        "expl": "A alternativa E está correta. O critério definidor da invalidade em um argumento dedutivo é a possibilidade de um contraexemplo: se existir qualquer cenário ou combinação de valores lógicos em que todas as premissas sejam verdadeiras e a conclusão seja falsa, o argumento é categoricamente inválido. Se esse cenário for impossível, o argumento é válido."
    },
    {
        "seg": "a04/s02",
        "ans": "A",
        "stem": "Considere o seguinte argumento: Premissa 1: 'Todos os réus confessos são astronautas'. Premissa 2: 'O investigado Mário é réu confesso'. Conclusão: 'Logo, o investigado Mário é astronauta'. Sob a ótica da lógica formal dedutiva, assinale a opção correta.",
        "opts": [
            ("A", "O argumento é dedutivamente válido, muito embora contenha uma premissa materialmente falsa no mundo real."),
            ("B", "O argumento é dedutivamente inválido, visto que réus não exercem a profissão de astronauta no mundo empírico."),
            ("C", "O argumento não é dedutivo por não conter conectivos lógicos da disjunção inclusiva."),
            ("D", "O argumento é uma falácia formal decorrente da negação indevida do termo médio."),
            ("E", "O argumento é inválido porque sua conclusão não possui relação gramatical com as premissas.")
        ],
        "expl": "A alternativa A está correta. A estrutura formal do argumento é: 'Todo A é B; M é A; logo, M é B'. Essa forma silogística é perfeitamente válida. Se as premissas fossem verdadeiras, a conclusão decorreria necessariamente. A falsidade fática da premissa ('réus são astronautas') afeta a solidez do argumento, mas não anula sua validade lógico-formal."
    },
    {
        "seg": "a04/s02",
        "ans": "B",
        "stem": "Na teoria da argumentação, um argumento dedutivo é denominado 'sólido' (sound argument) quando atende a dois requisitos simultâneos. Assinale a opção que indica corretamente esses requisitos.",
        "opts": [
            ("A", "Ser composto exclusivamente por proposições contingentes e conter pelo menos um quantificador universal."),
            ("B", "Ser um argumento dedutivamente válido e possuir todas as suas premissas factualmente verdadeiras."),
            ("C", "Possuir conclusão que seja uma tautologia e premissas que contenham apenas conectivos bicondicionais."),
            ("D", "Ter sido formulado por uma autoridade policial no exercício estrito de suas atribuições legais."),
            ("E", "Apresentar validade indutiva comprovada por amostragem probabilística representativa.")
        ],
        "expl": "A alternativa B está correta. Um argumento dedutivo sólido (sound) combina duas virtudes essenciais: (1) validade formal (sua estrutura lógica é impecável) e (2) veracidade material (todas as suas premissas são verdadeiras no mundo real). Consequentemente, a conclusão de um argumento sólido é garantidamente verdadeira."
    },
    {
        "seg": "a04/s02",
        "ans": "C",
        "stem": "Considere as afirmações verdadeiras: (1) Se Paulo viaja, então Amanda fica no plantão; (2) Se Amanda fica no plantão, então Roberto folga; (3) Amanda não ficou no plantão. A respeito dessa situação, assinale a opção que apresenta a dedução logicamente correta.",
        "opts": [
            ("A", "Roberto certamente tirou folga."),
            ("B", "Roberto não tirou folga no período."),
            ("C", "Paulo não viajou."),
            ("D", "Paulo viajou e Roberto tirou folga."),
            ("E", "Não se pode determinar a situação de Paulo.")
        ],
        "expl": "A alternativa C está correta. A premissa 3 informa que Amanda não ficou no plantão (~a). Na premissa 1 (p -> a), com a negação do consequente (~a), conclui-se por Modus Tollens que Paulo não viajou (~p). Quanto a Roberto, na premissa 2 (a -> r), sabendo-se que o antecedente é falso (~a), a condicional é satisfeita independentemente de Roberto folgar ou não, não se podendo concluir o estado de Roberto."
    },

    # --- a04/s04 (q78 a q83) ---
    {
        "seg": "a04/s04",
        "ans": "D",
        "stem": "O silogismo categórico clássico é uma forma tradicional de argumento dedutivo estruturado com premissas e termos específicos. Em relação à composição canônica do silogismo categórico, assinale a opção correta.",
        "opts": [
            ("A", "É composto por três premissas condicionais e uma conclusão disjuntiva."),
            ("B", "É formado por quatro termos distintos que devem figurar na conclusão final."),
            ("C", "É constituído por uma premissa simples e duas conclusões independentes."),
            ("D", "É composto por exatamente duas premissas categóricas e uma conclusão, contendo ao todo três termos."),
            ("E", "É estruturado sem termo médio, apoiando-se exclusivamente em analogias empíricas.")
        ],
        "expl": "A alternativa D está correta. Por definição aristotélica, o silogismo categórico padrão é composto por exatamente duas premissas (premissa maior e premissa menor) e uma conclusão, envolvendo exatamente três termos: termo maior (predicado da conclusão), termo menor (sujeito da conclusão) e termo médio (que faz a ponte entre as premissas)."
    },
    {
        "seg": "a04/s04",
        "ans": "E",
        "stem": "No silogismo categórico, o 'termo médio' exerce um papel lógico crucial para a articulação do raciocínio dedutivo. A respeito do termo médio, assinale a opção correta.",
        "opts": [
            ("A", "O termo médio deve obrigatoriamente figurar como predicado da conclusão do silogismo."),
            ("B", "O termo médio é o termo que aparece unicamente na premissa menor do argumento."),
            ("C", "O termo médio deve ser uma proposição condicional completa em si mesma."),
            ("D", "O termo médio pode ser eliminado das premissas se a conclusão for uma tautologia."),
            ("E", "O termo médio aparece em ambas as premissas, mas nunca deve constar na conclusão do silogismo.")
        ],
        "expl": "A alternativa E está correta. A função lógica do termo médio (M) é estabelecer a ligação conceitual entre o termo maior e o termo menor nas duas premissas. Por essa razão técnica, ele comparece em ambas as premissas, mas jamais deve figurar na conclusão. Sua presença na conclusão constitui vício formal de silogismo."
    },
    {
        "seg": "a04/s04",
        "ans": "A",
        "stem": "Entre as regras clássicas de validade do silogismo categórico, destaca-se a restrição referente a premissas de natureza negativa. Com base nessas regras formais, assinale a opção correta.",
        "opts": [
            ("A", "De duas premissas negativas nada se pode concluir com validade lógica."),
            ("B", "Se uma premissa for negativa, a conclusão deve ser obrigatoriamente afirmativa."),
            ("C", "Duas premissas negativas geram sempre uma conclusão universal afirmativa."),
            ("D", "A presença de uma premissa negativa anula a exigência de distribuição do termo médio."),
            ("E", "Premissas negativas só podem ser utilizadas caso contenham termos sinônimos.")
        ],
        "expl": "A alternativa A está correta. Uma das regras fundamentais da silogística estabelece que duas premissas negativas não geram conexão lógica válida entre o termo maior e o termo menor, pois ambos são excluídos do termo médio, nada se podendo inferir sobre a relação recíproca entre eles. Além disso, se uma premissa for negativa, a conclusão deve ser negativa (erro da opção B)."
    },
    {
        "seg": "a04/s04",
        "ans": "B",
        "stem": "Outra regra fundamental da silogística refere-se à quantidade e à qualidade das premissas em relação à conclusão. A respeito dessa regra, assinale a opção correta.",
        "opts": [
            ("A", "A conclusão de um silogismo deve sempre expressar a proposição mais forte do conjunto de premissas."),
            ("B", "A conclusão deve sempre seguir a parte mais fraca das premissas: sendo uma premissa negativa ou particular, a conclusão será negativa ou particular."),
            ("C", "Se ambas as premissas forem afirmativas, a conclusão resultante pode ser validamente negativa."),
            ("D", "De duas premissas particulares é sempre possível deduzir validamente uma conclusão universal."),
            ("E", "A conclusão deve ser universal afirmativa mesmo que ambas as premissas sejam particulares negativas.")
        ],
        "expl": "A alternativa B está correta. Conforme a regra clássica 'conclusio sequitur partem debiliorem', a conclusão sempre acompanha a premissa mais fraca: o particular é mais fraco que o universal, e o negativo é mais fraco que o afirmativo. Logo, havendo premissa particular ou negativa, a conclusão será obrigatoriamente particular ou negativa."
    },
    {
        "seg": "a04/s04",
        "ans": "C",
        "stem": "Considere o argumento: 'Todo agente da segurança pública possui porte de arma; alguns instrutores de tiro são agentes da segurança pública; logo, alguns instrutores de tiro possuem porte de arma'. Utilizando a análise por diagramas de Euler-Venn, assinale a opção correta.",
        "opts": [
            ("A", "O argumento é inválido, pois o termo médio não permite inferir qualquer interseção."),
            ("B", "O argumento é inválido, porque a conclusão deveria ser expressa de forma universal afirmativa."),
            ("C", "O argumento é dedutivamente válido, pois a interseção parcial entre instrutores e agentes está inteiramente contida no conjunto daqueles que possuem porte."),
            ("D", "O argumento é uma falácia formal originada de duas premissas afirmativas contraditórias."),
            ("E", "O argumento é falacioso em razão da regra que proíbe conclusões particulares na lógica formal.")
        ],
        "expl": "A alternativa C está correta. Sejam os conjuntos: P = possuem porte de arma, A = agentes de segurança, e I = instrutores de tiro. Premissa 1: A está contido em P. Premissa 2: a interseção entre I e A é não vazia (existe elemento que é I e A). Como todo elemento de A pertence a P, os elementos de I que estão em A pertencem obrigatoriamente a P. Logo, alguns instrutores de tiro possuem porte de arma. O argumento é perfeitamente válido."
    },
    {
        "seg": "a04/s04",
        "ans": "D",
        "stem": "Considere o silogismo: 'Todos os cães são mamíferos; todos os gatos são mamíferos; logo, todos os gatos são cães'. Assinale a opção que aponta corretamente a falácia formal que torna esse argumento dedutivo inválido.",
        "opts": [
            ("A", "Falácia das quatro premissas universais independentes."),
            ("B", "Falácia do apelo à autoridade biológica não qualificada."),
            ("C", "Falácia da conclusão negativa derivada de premissas afirmativas."),
            ("D", "Falácia do termo médio não distribuído em nenhuma das premissas."),
            ("E", "Falácia da negação do antecedente no termo menor da conclusão.")
        ],
        "expl": "A alternativa D está correta. O termo médio é 'mamíferos'. Em proposições universais afirmativas ('Todo A é B'), o sujeito é distribuído (tomado em toda a sua extensão), mas o predicado não é distribuído. Como o termo médio 'mamíferos' é predicado em ambas as premissas afirmativas, ele não foi distribuído em nenhuma delas. Por isso, cães e gatos podem pertencer a partes inteiramente distintas do conjunto dos mamíferos sem se tocarem, tornando o argumento inválido."
    },

    # --- a04/s07 (q84 a q89) ---
    {
        "seg": "a04/s07",
        "ans": "E",
        "stem": "A regra de inferência dedutiva conhecida como Dilema Construtivo é uma poderosa ferramenta de dedução. Assinale a opção que expressa a estrutura canônica e válida do Dilema Construtivo.",
        "opts": [
            ("A", "Se p -> q e r -> s, e sabe-se que ~q ou ~s, conclui-se validamente que p ou r."),
            ("B", "Se p -> q e p, conclui-se validamente que ~q."),
            ("C", "Se p ou q e p, conclui-se validamente que q."),
            ("D", "Se p -> q e q -> r, conclui-se validamente que ~p -> ~r."),
            ("E", "Se p -> q e r -> s, e sabe-se que p ou r, conclui-se validamente que q ou s.")
        ],
        "expl": "A alternativa E está correta. O Dilema Construtivo tem a estrutura clássica: dadas duas condicionais p -> q e r -> s, e a disjunção dos antecedentes (p ou r), decorre necessariamente a disjunção dos consequentes (q ou s). Se qualquer um dos antecedentes ocorrer, seu respectivo consequente ocorrerá."
    },
    {
        "seg": "a04/s07",
        "ans": "A",
        "stem": "Em contraposição ao Dilema Construtivo, a regra de inferência dedutiva denominada Dilema Destrutivo opera pela negação dos consequentes. Assinale a opção que expressa a estrutura válida do Dilema Destrutivo.",
        "opts": [
            ("A", "Se p -> q e r -> s, e sabe-se que ~q ou ~s, conclui-se validamente que ~p ou ~r."),
            ("B", "Se p -> q e r -> s, e sabe-se que q ou s, conclui-se validamente que p ou r."),
            ("C", "Se p -> q e r -> s, e sabe-se que ~p ou ~r, conclui-se validamente que ~q ou ~s."),
            ("D", "Se p ou q e ~p, conclui-se validamente que ~q."),
            ("E", "Se p -> q e ~q, conclui-se validamente que p.")
        ],
        "expl": "A alternativa A está correta. O Dilema Destrutivo é a generalização do Modus Tollens para duas condicionais: tendo p -> q e r -> s, e sabendo-se que pelo menos um dos consequentes não ocorreu (~q ou ~s), conclui-se necessariamente que pelo menos um dos antecedentes não ocorreu (~p ou ~r)."
    },
    {
        "seg": "a04/s07",
        "ans": "B",
        "stem": "A regra do Silogismo Disjuntivo é frequentemente aplicada na apuração de fatos por exclusão de hipóteses. Assinale a opção que expressa corretamente a estrutura válida do Silogismo Disjuntivo.",
        "opts": [
            ("A", "Dadas as premissas 'p ou q' e 'p', conclui-se validamente 'q'."),
            ("B", "Dadas as premissas 'p ou q' e '~p', conclui-se validamente 'q'."),
            ("C", "Dadas as premissas 'p e q' e '~p', conclui-se validamente '~q'."),
            ("D", "Dadas as premissas 'p -> q' e '~p', conclui-se validamente '~q'."),
            ("E", "Dadas as premissas 'p <-> q' e 'p', conclui-se validamente '~q'.")
        ],
        "expl": "A alternativa B está correta. O Silogismo Disjuntivo estabelece que, se uma disjunção inclusiva p ou q é verdadeira e uma de suas parcelas é eliminada pela veracidade de sua negação (~p), a outra parcela (q) deve ser necessariamente verdadeira para manter a proposição disjuntiva verdadeira."
    },
    {
        "seg": "a04/s07",
        "ans": "C",
        "stem": "A propriedade de encadeamento entre proposições condicionais na lógica de argumentação é formalizada pelo Silogismo Hipotético. Assinale a opção que expressa essa regra de inferência.",
        "opts": [
            ("A", "Se p -> q e q, então p."),
            ("B", "Se p -> q e ~p, então ~q."),
            ("C", "Se p -> q e q -> r, então p -> r."),
            ("D", "Se p ou q e q -> r, então p -> r."),
            ("E", "Se p -> q e r -> s, então (p e r) -> (q ou s).")
        ],
        "expl": "A alternativa C está correta. O Silogismo Hipotético representa a transitividade da implicação condicional: se a ocorrência de p garante a ocorrência de q (p -> q), e a ocorrência de q garante a ocorrência de r (q -> r), então a ocorrência de p garante de forma necessária a ocorrência de r (p -> r)."
    },
    {
        "seg": "a04/s07",
        "ans": "D",
        "stem": "Em uma operação policial, o comandante formulou as seguintes diretrizes: (1) Se os agentes atuarem na área leste, a via principal será interditada; (2) Se os agentes atuarem na área oeste, o posto de controle será ativado; (3) Os agentes atuarão na área leste ou atuarão na área oeste. Com base nessas diretrizes, assinale a opção que apresenta a conclusão válida obtida por Dilema Construtivo.",
        "opts": [
            ("A", "A via principal e o posto de controle serão ambos interditados simultaneamente."),
            ("B", "Os agentes não atuarão em nenhuma das duas áreas operacionais designadas."),
            ("C", "A via principal será interditada e o posto de controle não será ativado."),
            ("D", "A via principal será interditada ou o posto de controle será ativado."),
            ("E", "O posto de controle será ativado somente se a via principal não for interditada.")
        ],
        "expl": "A alternativa D está correta. Trata-se de uma aplicação direta do Dilema Construtivo: temos p -> q ('leste -> via interditada'), r -> s ('oeste -> posto ativado') e a disjunção dos antecedentes p ou r ('atuarão no leste ou no oeste'). A dedução válida incontestável é a disjunção dos consequentes: q ou s ('A via principal será interditada ou o posto de controle será ativado')."
    },
    {
        "seg": "a04/s07",
        "ans": "E",
        "stem": "Considere verdadeiras as premissas: (1) Se o laudo papiloscópico for positivo, o inquérito é remetido à Justiça; (2) O laudo papiloscópico foi positivo ou houve confissão espontânea; (3) Não houve confissão espontânea. A partir dessas informações, assinale a opção correta.",
        "opts": [
            ("A", "O inquérito não será remetido à Justiça."),
            ("B", "O laudo papiloscópico resultou negativo."),
            ("C", "O inquérito foi arquivado na delegacia por ausência de indícios."),
            ("D", "Houve confissão espontânea e o réu foi absolvido sumariamente."),
            ("E", "O laudo papiloscópico foi positivo e o inquérito é remetido à Justiça.")
        ],
        "expl": "A alternativa E está correta. Na premissa 2 temos a disjunção p ou c. A premissa 3 nega c (~c). Pelo Silogismo Disjuntivo, conclui-se obrigatoriamente p ('o laudo papiloscópico foi positivo'). Aplicando agora esse fato p na condicional da premissa 1 (p -> j), conclui-se por Modus Ponens que j é verdadeiro ('o inquérito é remetido à Justiça'). Portanto, ambas as afirmativas são verdadeiras."
    },

    # --- a04/s08 (q90 a q95) ---
    {
        "seg": "a04/s08",
        "ans": "A",
        "stem": "Considere a cadeia de condicionais verdadeiras: (1) Se Antônio viaja, Bernardo assume a chefia; (2) Se Bernardo assume a chefia, Cláudio redige a portaria; (3) Se Cláudio redige a portaria, Danilo protocola o documento. Sabe-se com certeza que Danilo NÃO protocolou o documento. Diante dessas informações, assinale a opção que expressa uma dedução correta.",
        "opts": [
            ("A", "Antônio não viajou, Bernardo não assumiu a chefia e Cláudio não redigiu a portaria."),
            ("B", "Antônio viajou, mas Cláudio não redigiu a portaria."),
            ("C", "Bernardo assumiu a chefia da unidade policial."),
            ("D", "Cláudio redigiu a portaria sem a autorização de Antônio."),
            ("E", "Não é possível deduzir se Antônio viajou ou não.")
        ],
        "expl": "A alternativa A está correta. A cadeia é a -> b -> c -> d, com d falso (~d). Pelo Modus Tollens sucessivo de trás para frente: de c -> d e ~d, conclui-se ~c (Cláudio não redigiu); de b -> c e ~c, conclui-se ~b (Bernardo não assumiu); de a -> b e ~b, conclui-se ~a (Antônio não viajou). Todos são falsos."
    },
    {
        "seg": "a04/s08",
        "ans": "B",
        "stem": "Considere verdadeiras as afirmações: (1) Diva é investigadora ou Dori não é perita; (2) Se Tiago é escrivão, então Dori é perita; (3) Tiago é escrivão e Diva não é investigadora. A partir dessas afirmações, assinale a opção que aponta uma conclusão logicamente necessária.",
        "opts": [
            ("A", "Diva é investigadora policial e participou da diligência."),
            ("B", "O conjunto de premissas é inconsistente por contradição interna."),
            ("C", "Dori certamente não é perita e faltou ao expediente."),
            ("D", "Tiago não é escrivão da delegacia daquela comarca."),
            ("E", "Todas as pessoas citadas exercem funções na corregedoria.")
        ],
        "expl": "A alternativa B está correta. Da premissa 3 decorre que Tiago é escrivão (t = V) e Diva não é investigadora (i = F). Com t = V, a premissa 2 (t -> d) exige que Dori seja perita (d = V). Porém, na premissa 1 (i ou ~d), com i = F exige-se ~d = V, isto é, Dori não é perita (d = F). Há uma contradição direta e insolúvel entre exigir d = V e d = F simultaneamente, revelando a inconsistência lógica do conjunto de premissas."
    },
    {
        "seg": "a04/s08",
        "ans": "C",
        "stem": "Considere verdadeiras as premissas: (1) Se o suspeito fugiu pelo telhado ou rompeu o portão, então o alarme disparou; (2) O alarme não disparou. A partir dessas premissas, assinale a opção que expressa uma conclusão logicamente necessária.",
        "opts": [
            ("A", "O suspeito fugiu pelo telhado, mas não rompeu o portão."),
            ("B", "O suspeito não fugiu pelo telhado, mas rompeu o portão dos fundos."),
            ("C", "O suspeito não fugiu pelo telhado e não rompeu o portão."),
            ("D", "O suspeito rompeu o portão e fugiu pelo telhado."),
            ("E", "O alarme disparou nos minutos seguintes à fuga.")
        ],
        "expl": "A alternativa C está correta. A estrutura é (t ou p) -> a. Sabe-se que ~a é verdadeira. Aplicando Modus Tollens, obtém-se a negação do antecedente: ~(t ou p). Pela lei de De Morgan, ~(t ou p) <=> ~t e ~p. Conclui-se, assim, com certeza absoluta, que o suspeito não fugiu pelo telhado e não rompeu o portão."
    },
    {
        "seg": "a04/s08",
        "ans": "D",
        "stem": "Considere verdadeiras as seguintes premissas: (1) Mariana é delegada se e somente se Carla for escrivã; (2) Carla é escrivã ou Patrícia é perita; (3) Patrícia não é perita. Com base nessas informações, assinale a opção que expressa a conclusão correta.",
        "opts": [
            ("A", "Carla não é escrivã."),
            ("B", "Mariana não é delegada."),
            ("C", "Patrícia é perita criminal."),
            ("D", "Mariana é delegada e Carla é escrivã."),
            ("E", "Nenhuma das três servidoras ocupa cargo policial.")
        ],
        "expl": "A alternativa D está correta. Da premissa 3, sabemos que ~p (Patrícia não é perita). Na premissa 2 (c ou p), como p é falsa, pelo Silogismo Disjuntivo conclui-se obrigatoriamente que c é verdadeira (Carla é escrivã). Na premissa 1 (m <-> c), como c é verdadeira, a bicondicional verdadeira exige que m seja igualmente verdadeira (Mariana é delegada). Logo, Mariana é delegada e Carla é escrivã."
    },
    {
        "seg": "a04/s08",
        "ans": "E",
        "stem": "Considere as seguintes premissas verdadeiras sobre três agentes: (1) Se Alice participa da diligência, Bruna não participa; (2) Se Camila participa da diligência, Bruna participa; (3) Camila participou da diligência. Assinale a opção que indica quem participou da diligência.",
        "opts": [
            ("A", "Alice e Bruna participaram da diligência."),
            ("B", "Apenas Alice participou da diligência."),
            ("C", "As três agentes participaram conjuntamente da diligência."),
            ("D", "Nenhuma das três agentes participou da diligência."),
            ("E", "Bruna e Camila participaram, e Alice não participou.")
        ],
        "expl": "A alternativa E está correta. Pela premissa 3, Camila participou (c = V). Na premissa 2 (c -> b), como c é V, por Modus Ponens Bruna participou (b = V). Na premissa 1 (a -> ~b), aplicando a contrapositiva ou Modus Tollens: como b é V, ~b é F, logo a deve ser F (Alice não participou). Assim, Bruna e Camila participaram, enquanto Alice não participou."
    },
    {
        "seg": "a04/s08",
        "ans": "A",
        "stem": "Considere verdadeiras as premissas: (1) Se Rogério é titular da delegacia, então Sérgio é adjunto; (2) Se Valter é comissário, então Rogério é titular; (3) Sérgio não é adjunto. Assinale a opção que apresenta a dedução logicamente válida.",
        "opts": [
            ("A", "Rogério não é titular da delegacia e Valter não é comissário."),
            ("B", "Rogério é titular da delegacia e Valter é comissário."),
            ("C", "Sérgio é adjunto na delegacia da comarca."),
            ("D", "Valter é comissário de polícia em atividade."),
            ("E", "Não é possível determinar a situação funcional de Valter.")
        ],
        "expl": "A alternativa A está correta. A premissa 3 informa ~s. Na premissa 1 (r -> s), por Modus Tollens com ~s decorre ~r (Rogério não é titular). Na premissa 2 (v -> r), por Modus Tollens com ~r decorre ~v (Valter não é comissário). Logo, deduz-se com certeza que Rogério não é titular e Valter não é comissário."
    },

    # --- a04/s09 (q96 a q101) ---
    {
        "seg": "a04/s09",
        "ans": "B",
        "stem": "Em uma investigação de furto com cinco suspeitos (A, B, C, D e E), o delegado apurou as seguintes afirmações verdadeiras: (1) Se D participou, então E participou; (2) Se D não participou, então C participou; (3) Se B ou C participou, então A não participou; (4) E não participou. Sabendo dessas premissas, assinale a opção que indica quem NÃO participou do furto entre esses suspeitos.",
        "opts": [
            ("A", "Apenas o suspeito D não participou."),
            ("B", "Com certeza, os suspeitos A, D e E não participaram do furto."),
            ("C", "Todos os cinco suspeitos participaram conjuntamente do delito."),
            ("D", "Apenas o suspeito A participou do furto qualificado."),
            ("E", "Não é possível definir a participação de nenhum suspeito.")
        ],
        "expl": "A alternativa B está correta. Pela premissa 4, E não participou (~e). Na premissa 1 (d -> e), por Modus Tollens decorre ~d (D não participou). Na premissa 2 (~d -> c), como ~d é V, por Modus Ponens decorre c (C participou). Na premissa 3 ((b ou c) -> ~a), o antecedente é verdadeiro (pois c é V), logo decorre ~a (A não participou). O envolvimento de B permanece indeterminado, mas é certo que A, D e E não participaram."
    },
    {
        "seg": "a04/s09",
        "ans": "C",
        "stem": "Em um processo administrativo disciplinar, apurou-se que a afirmação: 'Se o servidor acessou o banco de dados sigiloso, então transferiu arquivos para mídia externa' é sabidamente FALSA. Diante dessa constatação fática, assinale a opção correta.",
        "opts": [
            ("A", "O servidor não acessou o banco de dados sigiloso e não transferiu arquivos."),
            ("B", "O servidor não acessou o banco de dados sigiloso, mas transferiu arquivos."),
            ("C", "O servidor acessou o banco de dados sigiloso e não transferiu arquivos para mídia externa."),
            ("D", "O servidor acessou o banco de dados sigiloso e transferiu arquivos para mídia externa."),
            ("E", "Não é possível concluir se o servidor acessou ou não o sistema informatizado.")
        ],
        "expl": "A alternativa C está correta. Uma condicional p -> q só é falsa em uma situação exclusiva da tabela-verdade: antecedente verdadeiro e consequente falso (V -> F = F). Dessa forma, decorre taxativamente que o antecedente 'o servidor acessou o banco de dados sigiloso' é verdadeiro e o consequente 'transferiu arquivos' é falso (ou seja, não transferiu arquivos para mídia externa)."
    },
    {
        "seg": "a04/s09",
        "ans": "D",
        "stem": "Quatro agentes (I, J, K e L) foram ouvidos em sindicância e declararam premissas verdadeiras: (1) Se I estava presente, J não estava; (2) K estava presente se e somente se L estivesse presente; (3) J ou K estava presente; (4) L não estava presente. A partir dessas afirmações, assinale a opção correta.",
        "opts": [
            ("A", "K e L estavam presentes na ocasião."),
            ("B", "J não estava presente no local da sindicância."),
            ("C", "I estava presente e J não estava presente."),
            ("D", "J estava presente e I não estava presente."),
            ("E", "Nenhum dos quatro agentes estava presente no evento apurado.")
        ],
        "expl": "A alternativa D está correta. Premissa 4: L não estava (~l). Na premissa 2 (k <-> l), como l é falsa, k deve ser falsa (~k). Na premissa 3 (j ou k), como k é falsa, por Silogismo Disjuntivo decorre que j é verdadeira (J estava presente). Na premissa 1 (i -> ~j), pela contrapositiva j -> ~i: como j é verdadeira, conclui-se ~i (I não estava presente). Assim, J estava presente e I não estava presente."
    },
    {
        "seg": "a04/s09",
        "ans": "E",
        "stem": "Considere que duas testemunhas prestaram depoimentos contraditórios: o depoimento da testemunha 1 é dado por P, e o depoimento da testemunha 2 é a negação exata ~P. Sabendo-se que o princípio do terceiro excluído e o da não contradição regem o raciocínio formal, assinale a opção correta.",
        "opts": [
            ("A", "Ambas as testemunhas podem estar declarando a verdade sob o mesmo prisma."),
            ("B", "Ambas as testemunhas podem estar mentindo simultaneamente."),
            ("C", "O juiz deve concluir que os dois depoimentos são sentenças abertas."),
            ("D", "A contradição entre P e ~P demonstra que ambas são tautologias jurídicas."),
            ("E", "Exatamente uma das duas testemunhas disse a verdade e a outra mentiu.")
        ],
        "expl": "A alternativa E está correta. Duas proposições em que uma é a estrita negação da outra (P e ~P) são contraditórias. Pelos princípios da não contradição e do terceiro excluído, não podem ser simultaneamente verdadeiras nem simultaneamente falsas. Uma delas é necessariamente verdadeira e a outra é forçosamente falsa."
    },
    {
        "seg": "a04/s09",
        "ans": "A",
        "stem": "Um perito constatou que: 'Se o veículo colidiu com o poste, a fiação foi rompida' é verdadeira, e 'A fiação não foi rompida' é verdadeira. Além disso, 'Ou o motorista trafegava em alta velocidade, ou o veículo colidiu com o poste' é verdadeira (disjunção exclusiva). Assinale a opção que expressa uma dedução correta.",
        "opts": [
            ("A", "O motorista trafegava em alta velocidade e o veículo não colidiu com o poste."),
            ("B", "O veículo colidiu com o poste e a fiação foi rompida."),
            ("C", "O motorista não trafegava em alta velocidade."),
            ("D", "A fiação foi rompida e o poste permaneceu intacto."),
            ("E", "Não é possível deduzir a velocidade empregada pelo motorista.")
        ],
        "expl": "A alternativa A está correta. Da condicional c -> f e da premissa ~f, decorre por Modus Tollens que ~c (o veículo não colidiu com o poste). Na disjunção exclusiva (v ou exclusivo c), como c é falsa, para que a exclusiva seja verdadeira, a outra parcela deve ser obrigatoriamente verdadeira, logo v é verdadeira (o motorista trafegava em alta velocidade). Conclusão: o motorista trafegava em alta velocidade e o veículo não colidiu com o poste."
    },
    {
        "seg": "a04/s09",
        "ans": "B",
        "stem": "Três policiais (Marcos, Nivaldo e Otávio) prestaram depoimento. Sabe-se que exatamente um deles diz a verdade e os outros dois mentem. Marcos disse: 'Nivaldo mente'. Nivaldo disse: 'Otávio mente'. Otávio disse: 'Marcos e Nivaldo mentem'. Com base nessa situação lógica, assinale a opção correta.",
        "opts": [
            ("A", "Marcos é o único que diz a verdade."),
            ("B", "Nivaldo é o único que diz a verdade."),
            ("C", "Otávio é o único que diz a verdade."),
            ("D", "Marcos e Otávio dizem a verdade conjuntamente."),
            ("E", "A situação descrita é logicamente impossível e inconsistente.")
        ],
        "expl": "A alternativa B está correta. Testando hipóteses: (1) Se Marcos fala a verdade (V): então Nivaldo mente (F). Se Nivaldo mente, a frase 'Otávio mente' é falsa, logo Otávio fala a verdade (V). Mas aí teríamos dois falando a verdade (Marcos e Otávio), contrariando a regra de que apenas um fala a verdade. (2) Se Nivaldo fala a verdade (V): então Marcos mente (F) (pois Marcos disse que Nivaldo mente, o que é falso) e Otávio mente (F) (pois Nivaldo disse a verdade ao afirmar que Otávio mente). Se Otávio mente, sua frase de que ambos mentem é falsa (pois Nivaldo não mente, o que é consistente). Temos exatamente um falando a verdade: Nivaldo. (3) Se Otávio falasse a verdade, sua frase exigiria que Marcos e Nivaldo mentissem, gerando contradição entre Marcos e Nivaldo."
    },

    # --- a04/s10 (q102 a q107) ---
    {
        "seg": "a04/s10",
        "ans": "C",
        "stem": "Considere o argumento: 'Se chove torrencialmente, o trânsito da cidade fica congestionado. O trânsito da cidade está congestionado. Logo, choveu torrencialmente'. Sob a ótica da lógica dedutiva formal, assinale a opção correta.",
        "opts": [
            ("A", "O argumento é dedutivamente válido por aplicação da regra de inferência Modus Ponens."),
            ("B", "O argumento é dedutivamente válido por aplicação da regra de inferência Modus Tollens."),
            ("C", "O argumento é dedutivamente INVÁLIDO, configurando a falácia formal da afirmação do consequente."),
            ("D", "O argumento é dedutivamente INVÁLIDO, configurando a falácia formal da negação do antecedente."),
            ("E", "O argumento é uma tautologia que não comporta análise de validade formal.")
        ],
        "expl": "A alternativa C está correta. A estrutura do argumento é: p -> q; q; logo, p. Trata-se da clássica falácia formal da afirmação do consequente. O fato de o consequente ser verdadeiro ('trânsito congestionado') não garante que o antecedente ('chuva') tenha ocorrido, pois o trânsito pode estar congestionado por inúmeros outros motivos (como acidentes ou obras na via). O argumento é, portanto, inválido."
    },
    {
        "seg": "a04/s10",
        "ans": "D",
        "stem": "Considere o argumento: 'Se o motor esquenta, o ventilador de arrefecimento é acionado. O motor não esquentou. Portanto, o ventilador de arrefecimento não foi acionado'. No âmbito da lógica de argumentação, assinale a opção correta.",
        "opts": [
            ("A", "O argumento é dedutivamente válido pela regra de contraposição universal."),
            ("B", "O argumento é válido porque a negação da causa anula de imediato todo e qualquer efeito."),
            ("C", "O argumento é válido por se tratar de um silogismo hipotético perfeito."),
            ("D", "O argumento é dedutivamente INVÁLIDO, pois comete a falácia formal da negação do antecedente."),
            ("E", "O argumento é válido por força do princípio da identidade entre antecedente e consequente.")
        ],
        "expl": "A alternativa D está correta. A estrutura é p -> q; ~p; logo, ~q. Trata-se da falácia formal da negação do antecedente. Em uma condicional simples p -> q, p é apenas condição suficiente, não necessária. O consequente q (acionamento do ventilador) poderia ser acionado por acionamento manual, teste de circuito ou defeito no sensor, mesmo sem o motor ter esquentado. Por isso, o raciocínio é inválido."
    },
    {
        "seg": "a04/s10",
        "ans": "E",
        "stem": "Considere o argumento: 'Se o agente passar no exame psicológico, será convocado para o curso de formação policial. O agente passou no exame psicológico. Logo, será convocado para o curso de formação policial'. Assinale a opção que classifica corretamente esse argumento.",
        "opts": [
            ("A", "Argumento inválido por afirmação do consequente."),
            ("B", "Argumento inválido por negação do antecedente."),
            ("C", "Argumento indutivo fraco por amostragem insuficiente."),
            ("D", "Argumento dedutivo inválido por vício formal de silogismo."),
            ("E", "Argumento dedutivamente VÁLIDO por aplicação da regra de inferência Modus Ponens.")
        ],
        "expl": "A alternativa E está correta. A forma lógica do argumento é rigorosamente: p -> q; p; logo, q. Essa é a formulação clássica e paradigmática do Modus Ponens (modo de afirmar pelo antecedente). As premissas sendo verdadeiras, a conclusão decorre com necessidade absoluta e inquestionável, tornando o argumento dedutivamente válido."
    },
    {
        "seg": "a04/s10",
        "ans": "A",
        "stem": "Considere o argumento: 'Se o alarme de segurança detectar invasão, o protocolo de emergência é ativado. O protocolo de emergência não foi ativado. Logo, o alarme de segurança não detectou invasão'. A respeito desse argumento, assinale a opção correta.",
        "opts": [
            ("A", "O argumento é dedutivamente VÁLIDO por aplicação da regra de inferência Modus Tollens."),
            ("B", "O argumento é dedutivamente inválido por falácia da negação do consequente."),
            ("C", "O argumento é dedutivamente inválido por cometer a falácia da petição de princípio."),
            ("D", "O argumento é uma indução estatística que necessita de dados empíricos confirmatórios."),
            ("E", "O argumento é inválido porque condicionais não admitem conclusões negativas.")
        ],
        "expl": "A alternativa A está correta. A estrutura do argumento é: p -> q; ~q; logo, ~p. Essa regra de inferência é o Modus Tollens (modo de negar pelo consequente). Como a consequência necessária do antecedente não ocorreu (~q), é logicamente impossível que a condição suficiente p tenha ocorrido. Logo, o argumento é formalmente válido."
    },
    {
        "seg": "a04/s10",
        "ans": "B",
        "stem": "Considere o argumento categórico: 'Todos os recifenses são pernambucanos. Todos os pernambucanos são brasileiros. Logo, todos os recifenses são brasileiros'. Sob a perspectiva dos diagramas de conjuntos lógicos (Euler-Venn), assinale a opção correta.",
        "opts": [
            ("A", "O argumento é dedutivamente inválido porque um diagrama de inclusão não permite conclusões universais válidas."),
            ("B", "O argumento é dedutivamente VÁLIDO, pois os recifenses estão contidos nos pernambucanos e estes nos brasileiros."),
            ("C", "O argumento é dedutivamente inválido em virtude da falácia da generalização apressada dos termos médios."),
            ("D", "O argumento é dedutivamente inválido, visto que decorre unicamente de uma observação empírica contingente."),
            ("E", "O argumento é dedutivamente inválido porque comete a falácia silogística do termo médio não distribuído.")
        ],
        "expl": "A alternativa B está correta. Sejam os conjuntos R (recifenses), P (pernambucanos) e B (brasileiros). Premissa 1: R está contido em P. Premissa 2: P está contido em B. Pela propriedade transitiva da inclusão de conjuntos, todo elemento de R pertence obrigatoriamente a B (R está contido em B). O argumento possui forma silogística perfeitamente válida."
    },
    {
        "seg": "a04/s10",
        "ans": "C",
        "stem": "A distinção entre argumentos dedutivos e argumentos indutivos é um dos pilares do raciocínio lógico. Acerca dessa classificação dos argumentos, assinale a opção correta.",
        "opts": [
            ("A", "Tanto argumentos dedutivos quanto indutivos admitem juízo formal de validade ou de invalidade."),
            ("B", "Nos argumentos dedutivos a conclusão é provável e nos indutivos decorre com necessidade absoluta."),
            ("C", "Apenas dedutivos são válidos ou inválidos; indutivos são avaliados como fortes ou fracos."),
            ("D", "Argumentos dedutivos ampliam o conteúdo empírico das premissas gerando conhecimentos novos."),
            ("E", "A validade dedutiva requer testes de hipótese estatísticos com nível de significância fixado.")
        ],
        "expl": "A alternativa C está correta. Os conceitos técnicos de validade e invalidade são exclusivos dos argumentos dedutivos, nos quais a conclusão pretende decorrer necessariamente das premissas. Já os argumentos indutivos (generalizações, previsões, analogias) estabelecem conclusões apenas prováveis ou plausíveis, sendo avaliados segundo seu grau de sustentação como fortes ou fracos (ou cogentes e não cogentes)."
    },

    # --- a04/s11 (q108 a q113) ---
    {
        "seg": "a04/s11",
        "ans": "D",
        "stem": "Considere verdadeiras as premissas: (1) Se a equipe técnica e a perícia balística forem aprovadas, o mandado de prisão preventiva será expedido; (2) O mandado de prisão preventiva NÃO foi expedido. Aplicando Modus Tollens e as leis de De Morgan, assinale a opção que expressa a conclusão válida.",
        "opts": [
            ("A", "A equipe técnica foi aprovada e a perícia balística não foi aprovada."),
            ("B", "A equipe técnica e a perícia balística foram ambas reprovadas com certeza."),
            ("C", "A equipe técnica não foi aprovada e a perícia balística foi aprovada."),
            ("D", "A equipe técnica não foi aprovada ou a perícia balística não foi aprovada."),
            ("E", "O mandado de prisão preventiva será expedido nos dias seguintes.")
        ],
        "expl": "A alternativa D está correta. A premissa 1 é (t e b) -> m, e a premissa 2 é ~m. Pelo Modus Tollens, conclui-se a negação do antecedente: ~(t e b). Pela lei de De Morgan, a negação de uma conjunção é a disjunção das negações: ~t ou ~b ('A equipe técnica não foi aprovada ou a perícia balística não foi aprovada'). Afirmar categoricamente que ambas foram reprovadas (opção B) seria incorreto, pois a disjunção garante apenas que pelo menos uma delas não foi aprovada."
    },
    {
        "seg": "a04/s11",
        "ans": "E",
        "stem": "Em uma audiência judicial, constatou-se que a afirmação: 'O suspeito foi reconhecido pela vítima e a arma foi encontrada em seu veículo' é comprovadamente FALSA. Diante dessa constatação lógica, assinale a opção que expressa uma certeza necessária.",
        "opts": [
            ("A", "O suspeito não foi reconhecido pela vítima e a arma não foi encontrada no veículo."),
            ("B", "O suspeito foi reconhecido pela vítima, mas a arma não estava no veículo."),
            ("C", "A arma foi encontrada no veículo, mas o suspeito não foi reconhecido."),
            ("D", "Ambas as orações que compõem a frase são obrigatoriamente falsas."),
            ("E", "O suspeito não foi reconhecido pela vítima ou a arma não foi encontrada em seu veículo.")
        ],
        "expl": "A alternativa E está correta. Dizer que uma conjunção p e q é falsa equivale a afirmar a sua negação lógica ~(p e q). Pelas leis de De Morgan, ~(p e q) <=> ~p ou ~q. Ou seja, basta que uma das parcelas seja falsa (ou ambas o sejam) para que a conjunção seja falsa. Logo, a certeza necessária é que 'O suspeito não foi reconhecido pela vítima ou a arma não foi encontrada em seu veículo'."
    },
    {
        "seg": "a04/s11",
        "ans": "A",
        "stem": "Considere verdadeiras as premissas: (1) Se Flávio for promovido, Gilberto assume a coordenadoria; (2) Gilberto não assumiu a coordenadoria; (3) Flávio foi promovido ou Heitor foi transferido. Com base exclusivamente nessas premissas, assinale a opção que apresenta a dedução logicamente válida.",
        "opts": [
            ("A", "Flávio não foi promovido e Heitor foi transferido."),
            ("B", "Flávio foi promovido e Heitor não foi transferido."),
            ("C", "Gilberto assumiu a coordenadoria por decisão judicial."),
            ("D", "Heitor não foi transferido para outra comarca."),
            ("E", "Flávio e Gilberto foram promovidos simultaneamente.")
        ],
        "expl": "A alternativa A está correta. Na premissa 1 (f -> g), com a premissa 2 (~g), aplica-se Modus Tollens e conclui-se que Flávio não foi promovido (~f). Na premissa 3 (f ou h), sabendo que f é falsa, aplica-se o Silogismo Disjuntivo e conclui-se obrigatoriamente que Heitor foi transferido (h = V). Portanto, Flávio não foi promovido e Heitor foi transferido."
    },
    {
        "seg": "a04/s11",
        "ans": "B",
        "stem": "Um texto argumentativo apresenta o seguinte raciocínio: 'Sempre que o delegado defere a diligência, o mandado é cumprido no mesmo dia. Se o mandado é cumprido no mesmo dia, o suspeito presta depoimento imediato. Hoje, o suspeito não prestou depoimento imediato'. Assinale a opção que expressa a conclusão válida do argumento.",
        "opts": [
            ("A", "O delegado deferiu a diligência investigativa."),
            ("B", "O delegado não deferiu a diligência e o mandado não foi cumprido no mesmo dia."),
            ("C", "O mandado foi cumprido no mesmo dia após o meio-dia."),
            ("D", "O suspeito prestou depoimento na presença de seu defensor público."),
            ("E", "Não é possível deduzir se o mandado foi ou não cumprido.")
        ],
        "expl": "A alternativa B está correta. A cadeia é: d -> m, m -> s, e sabe-se que ~s. Pelo Modus Tollens em m -> s com ~s, obtém-se ~m (o mandado não foi cumprido no mesmo dia). Em seguida, pelo Modus Tollens em d -> m com ~m, obtém-se ~d (o delegado não deferiu a diligência). Conclusão: o delegado não deferiu a diligência e o mandado não foi cumprido."
    },
    {
        "seg": "a04/s11",
        "ans": "C",
        "stem": "Considere as seguintes premissas operacionais: (1) Se a operação for deflagrada na zona rural, a equipe tática usará viaturas traçadas; (2) Se a operação for deflagrada na zona urbana, a equipe tática usará motocicletas de patrulha; (3) A equipe tática não usou viaturas traçadas ou não usou motocicletas de patrulha. Aplicando o Dilema Destrutivo, assinale a opção que apresenta a conclusão válida.",
        "opts": [
            ("A", "A operação foi deflagrada em ambas as zonas simultaneamente."),
            ("B", "A equipe tática cancelou a realização de toda a operação."),
            ("C", "A operação não foi deflagrada na zona rural ou não foi deflagrada na zona urbana."),
            ("D", "A operação foi deflagrada exclusivamente na zona portuária."),
            ("E", "A equipe tática usou helicópteros para o cumprimento das ordens judiciais.")
        ],
        "expl": "A alternativa C está correta. Trata-se da aplicação exata da regra do Dilema Destrutivo: dadas as condicionais r -> v e u -> m, e a disjunção das negações dos consequentes (~v ou ~m), conclui-se necessariamente a disjunção das negações dos antecedentes: ~r ou ~u ('A operação não foi deflagrada na zona rural ou não foi deflagrada na zona urbana')."
    },
    {
        "seg": "a04/s11",
        "ans": "D",
        "stem": "Na lógica formal dedutiva clássica, caso um argumento contenha em seu conjunto de premissas uma contradição explícita (premissas mutuamente inconsistentes, como p e ~p), assinale a opção que expressa o que decorre logicamente desse conjunto segundo o princípio da explosão (ex contradictione sequitur quodlibet).",
        "opts": [
            ("A", "O argumento torna-se uma tautologia independente da conclusão."),
            ("B", "Nenhuma conclusão pode ser derivada, tornando o argumento uma sentença aberta."),
            ("C", "A conclusão deve ser obrigatoriamente a negação do antecedente das premissas."),
            ("D", "Qualquer proposição arbitrária decorre validamente do conjunto de premissas contraditórias."),
            ("E", "O argumento perde a sua natureza dedutiva e transforma-se em uma indução fraca.")
        ],
        "expl": "A alternativa D está correta. Na lógica clássica, o princípio da explosão ('ex contradictione sequitur quodlibet') estabelece que, a partir de premissas logicamente contraditórias (que nunca podem ser simultaneamente verdadeiras), é impossível que as premissas sejam verdadeiras e a conclusão falsa (pois o antecedente 'todas as premissas verdadeiras' nunca se verifica). Dessa forma, qualquer conclusão que seja proposta decorre validamente no sentido formal da dedução clássica."
    },

    # --- a04/s12 (q114 a q119) ---
    {
        "seg": "a04/s12",
        "ans": "E",
        "stem": "Ao revisar os métodos de teste de validade de um argumento dedutivo composto por premissas condicionais e disjuntivas, assinale a opção que indica o roteiro técnico mais seguro e conclusivo.",
        "opts": [
            ("A", "Verificar se os termos empregados nas premissas possuem sinonímia completa no dicionário oficial."),
            ("B", "Contar as orações subordinadas do texto e converter as conjunções adversativas em disjunções."),
            ("C", "Substituir todas as proposições por sentenças abertas dotadas de quantificadores universais."),
            ("D", "Aceitar o argumento como válido caso tenha sido proferido por autoridade pública competente."),
            ("E", "Assumir premissas verdadeiras e conclusão falsa; se gerar contradição, o argumento é válido.")
        ],
        "expl": "A alternativa E está correta. O roteiro canônico mais rigoroso para testar a validade dedutiva consiste em assumir que todas as premissas são simultaneamente verdadeiras e supor que a conclusão possa ser falsa. Se essa suposição forçar uma contradição nos valores lógicos das proposições componentes, prova-se que não existe contraexemplo, consolidando a validade formal do argumento."
    },
    {
        "seg": "a04/s12",
        "ans": "A",
        "stem": "Analise os três argumentos dedutivos a seguir: I. 'Se o suspeito mente, então fica nervoso. O suspeito não ficou nervoso. Logo, o suspeito não mente'. II. 'Se o réu é culpado, então estava no local do crime. O réu estava no local do crime. Logo, o réu é culpado'. III. 'O laudo pericial é inconclusivo ou a arma é falsa. O laudo pericial não é inconclusivo. Logo, a arma é falsa'. Entre esses três argumentos, assinale a opção que aponta corretamente os argumentos dedutivamente VÁLIDOS.",
        "opts": [
            ("A", "Apenas os argumentos I e III são válidos."),
            ("B", "Apenas os argumentos I e II são válidos."),
            ("C", "Apenas o argumento I é válido."),
            ("D", "Apenas o argumento II é válido."),
            ("E", "Todos os três argumentos são dedutivamente válidos.")
        ],
        "expl": "A alternativa A está correta. O argumento I é válido por aplicação direta do Modus Tollens (m -> n; ~n; logo, ~m). O argumento II é INVÁLIDO porque comete a falácia da afirmação do consequente (c -> l; l; logo, c, pois estar no local não prova culpa). O argumento III é válido por Silogismo Disjuntivo (i ou f; ~i; logo, f). Portanto, apenas I e III são válidos."
    },
    {
        "seg": "a04/s12",
        "ans": "B",
        "stem": "Considere o conjunto de proposições declaradas verdadeiras: (1) Se a perícia técnica for conclusiva, o inquérito é concluído; (2) Se o inquérito é concluído, o promotor oferece denúncia; (3) O promotor não ofereceu denúncia. Com base nessas premissas, assinale a opção que expressa uma dedução logicamente necessária.",
        "opts": [
            ("A", "A perícia técnica foi conclusiva e o inquérito foi arquivado."),
            ("B", "A perícia técnica não foi conclusiva e o inquérito não foi concluído."),
            ("C", "O inquérito foi concluído após o oferecimento da denúncia."),
            ("D", "O suspeito confessou o crime perante a autoridade judicial."),
            ("E", "Não é possível deduzir o resultado da perícia técnica.")
        ],
        "expl": "A alternativa B está correta. As premissas formam a cadeia p -> i e i -> d, com ~d como fato comprovado. Pelo Modus Tollens em i -> d, obtém-se ~i (o inquérito não foi concluído). Pelo Modus Tollens em p -> i com ~i, obtém-se ~p (a perícia técnica não foi conclusiva). Ambas as proposições negativas são conclusões necessárias."
    },
    {
        "seg": "a04/s12",
        "ans": "C",
        "stem": "Na avaliação da consistência lógica de um conjunto de premissas em um processo de investigação, assinale a opção que define com precisão técnica quando um conjunto de proposições é classificado como 'consistente'.",
        "opts": [
            ("A", "Quando todas as proposições do conjunto forem compostas exclusivamente por quantificadores universais."),
            ("B", "Quando a conjunção de todas as proposições resultar em uma contradição lógica evidente."),
            ("C", "Quando existe pelo menos uma atribuição de valores lógicos que torne todas as proposições do conjunto verdadeiras ao mesmo tempo."),
            ("D", "Quando todas as proposições componentes forem orações interrogativas da língua natural."),
            ("E", "Quando o número de proposições simples for rigorosamente igual ao número de conectivos condicionais.")
        ],
        "expl": "A alternativa C está correta. Na lógica formal, um conjunto de proposições (ou premissas) é dito logicamente consistente (ou satisfatível) se, e somente se, existir ao menos uma linha na tabela-verdade ou uma interpretação possível em que todas as proposições sejam verdadeiras simultaneamente. Se não existir nenhuma combinação que as torne verdadeiras ao mesmo tempo, o conjunto é inconsistente."
    },
    {
        "seg": "a04/s12",
        "ans": "D",
        "stem": "Em uma escala de serviço operacional, foram estabelecidas as seguintes regras verdadeiras: (1) André está de plantão ou Bruno está de plantão; (2) Se Bruno está de plantão, então Caio está de plantão; (3) Caio não está de plantão. Assinale a opção que indica quem está de plantão.",
        "opts": [
            ("A", "Caio e Bruno estão de plantão."),
            ("B", "Bruno está de plantão e André não está."),
            ("C", "Nenhum dos três policiais está de plantão."),
            ("D", "André está de plantão e Bruno não está de plantão."),
            ("E", "Os três policiais estão de plantão conjuntamente.")
        ],
        "expl": "A alternativa D está correta. A premissa 3 afirma que Caio não está (~c). Na premissa 2 (b -> c), aplicando Modus Tollens com ~c, decorre que Bruno não está de plantão (~b). Na premissa 1 (a ou b), como b é falsa, pelo Silogismo Disjuntivo decorre obrigatoriamente que a é verdadeira (André está de plantão). Conclusão: André está de plantão e Bruno não está."
    },
    {
        "seg": "a04/s12",
        "ans": "E",
        "stem": "Na lógica formal clássica, a verificação da validade de um argumento dedutivo pode ser realizada por diferentes técnicas formais. A esse respeito, assinale a opção correta.",
        "opts": [
            ("A", "A tabela-verdade completa só é capaz de avaliar argumentos com exatamente duas premissas afirmativas."),
            ("B", "O método da prova por absurdo só tem utilidade prática em argumentos com premissas contraditórias."),
            ("C", "O emprego de diagramas de Euler-Venn é restrito a argumentos que não contenham termos quantificados."),
            ("D", "As regras de inferência são válidas apenas quando aplicadas a proposições da linguagem jurídica oficial."),
            ("E", "Tabela-verdade, prova por absurdo e aplicação de regras de inferência são métodos formais válidos e intercambiáveis para demonstrar a validade dedutiva de um argumento.")
        ],
        "expl": "A alternativa E está correta. A validade de um argumento dedutivo pode ser demonstrada por diferentes métodos formais equivalentes: a tabela-verdade completa (que exaure todos os casos), o método indireto da prova por absurdo (que busca a impossibilidade de premissas V e conclusão F) e a dedução natural por aplicação sucessiva de regras de inferência válidas (Modus Ponens, Modus Tollens, Silogismo Disjuntivo, etc.)."
    }
]
