"""Lote 1: Aula 00 (a00/s02, a00/s06, a00/s11) - 18 questoes (q0 a q17)"""

QUESTOES = [
    # --- a00/s02 (q0 a q5) ---
    {
        "seg": "a00/s02",
        "ans": "A",
        "stem": "No contexto da lógica proposicional clássica, proposição é definida como toda oração declarativa que admite um único valor lógico: verdadeiro ou falso. Considerando essa definição, assinale a opção que apresenta uma proposição lógica.",
        "opts": [
            ("A", "O laudo pericial foi protocolado na delegacia dentro do prazo legal."),
            ("B", "Apresente imediatamente a arma do crime à autoridade policial!"),
            ("C", "Quem foi o responsável pelo arrombamento do cofre da agência?"),
            ("D", "Que trabalho de investigação pericial brilhante e extraordinário!"),
            ("E", "Esta frase escrita no relatório é uma completa mentira.")
        ],
        "expl": "A alternativa A é a única oração declarativa com sentido completo que pode ser valorada objetivamente em verdadeiro ou falso. As demais são imperativa (B), interrogativa (C), exclamativa (D) e um paradoxo que não admite valor lógico consistente (E)."
    },
    {
        "seg": "a00/s02",
        "ans": "B",
        "stem": "Em relação às sentenças abertas e equações matemáticas na lógica proposicional, assinale a opção que apresenta uma proposição lógica fechada e não uma sentença aberta.",
        "opts": [
            ("A", "x + 7 = 15, sendo x uma variável real não especificada."),
            ("B", "2x + 5 - 2x = 9, sendo x um número real qualquer."),
            ("C", "Ele foi indiciado pela prática de crime de peculato no mês passado."),
            ("D", "Aquele agente da polícia civil participou da operação na comunidade."),
            ("E", "y - 4 > 10, com y pertencente ao conjunto dos inteiros positivos.")
        ],
        "expl": "Na alternativa B, simplificando os termos em x, obtém-se 5 = 9, uma igualdade aritmética fechada e objetivamente falsa, constituindo proposição lógica. As alternativas A e E dependem de incógnita e C e D têm pronomes sem referência determinada, sendo sentenças abertas."
    },
    {
        "seg": "a00/s02",
        "ans": "C",
        "stem": "Os quantificadores lógicos têm a função de ligar variáveis e transformar sentenças abertas em proposições lógicas passíveis de valoração. Acerca desse tema, assinale a opção correta.",
        "opts": [
            ("A", "A aplicação do quantificador universal transforma uma sentença aberta em uma sentença imperativa."),
            ("B", "Sentenças que contêm quantificadores existenciais não podem ser classificadas como proposições lógicas."),
            ("C", "A sentença 'Existe pelo menos um servidor do órgão que possui porte de arma' é uma proposição lógica fechada."),
            ("D", "A expressão 'Nenhum cidadão deve descumprir as normas' é uma sentença aberta por não ter sujeito determinado."),
            ("E", "Os quantificadores lógicos eliminam a possibilidade de uma oração ser valorada como falsa.")
        ],
        "expl": "A alternativa C está correta, pois o quantificador existencial fecha a sentença aberta, atribuindo-lhe sentido completo passível de valoração lógica em verdadeiro ou falso. As opções A e B erram sobre a natureza dos quantificadores, D erra pois nenhum é quantificador e fecha a frase, e E erra pois proposições quantificadas podem ser falsas."
    },
    {
        "seg": "a00/s02",
        "ans": "D",
        "stem": "Na análise textual de relatórios policiais, o raciocínio lógico distingue proposições fechadas de sentenças abertas decorrentes da indefinição de termos. Com base nisso, assinale a opção que indica uma sentença aberta.",
        "opts": [
            ("A", "O estado de Pernambuco situa-se na Região Nordeste do Brasil."),
            ("B", "O número 17 é um número primo e maior do que 10."),
            ("C", "Todos os agentes de polícia presentes na reunião assinaram a ata."),
            ("D", "Ela prestou depoimento como testemunha ocular do homicídio em 2024."),
            ("E", "Recife é a capital administrativa do estado de Pernambuco.")
        ],
        "expl": "A alternativa D apresenta o pronome Ela sem referência contextual que determine a pessoa referida, não permitindo julgamento objetivo em verdadeiro ou falso e caracterizando sentença aberta. As opções A, B, C e E possuem sujeitos definidos ou quantificados, sendo proposições lógicas fechadas."
    },
    {
        "seg": "a00/s02",
        "ans": "E",
        "stem": "A lógica formal clássica apoia-se em três princípios fundamentais que regem o pensamento e a valoração das proposições. A respeito desses princípios, assinale a opção correta.",
        "opts": [
            ("A", "O princípio da identidade postula que uma proposição pode ser verdadeira e falsa ao mesmo tempo."),
            ("B", "O princípio do terceiro excluído estabelece que uma proposição pode admitir um terceiro valor de incerteza."),
            ("C", "O princípio da não contradição afirma que toda proposição falsa é necessariamente uma sentença aberta."),
            ("D", "O princípio da identidade assevera que uma proposição verdadeira pode tornar-se falsa sem alteração de contexto."),
            ("E", "O princípio da não contradição estabelece que uma proposição não pode ser verdadeira e falsa simultaneamente.")
        ],
        "expl": "A alternativa E está correta, pois o princípio da não contradição estabelece que nenhuma proposição pode ser simultaneamente verdadeira e falsa sob o mesmo aspecto. As opções A e D distorcem o princípio da identidade, B contraria o terceiro excluído e C confunde contradição com sentença aberta."
    },
    {
        "seg": "a00/s02",
        "ans": "A",
        "stem": "Considere a seguinte frase atribuída a um investigado durante audiência: 'A declaração que estou fazendo agora perante a autoridade policial é falsa'. Acerca dessa declaração no âmbito da lógica formal, assinale a opção correta.",
        "opts": [
            ("A", "Trata-se de um paradoxo lógico e, por conseguinte, não se classifica como proposição lógica."),
            ("B", "Trata-se de uma proposição lógica simples cujo valor de verdade é comprovadamente falso."),
            ("C", "Trata-se de uma sentença aberta, pois depende da apuração de provas testemunhais posteriores."),
            ("D", "Trata-se de uma proposição lógica composta formada por duas orações com valor verdadeiro."),
            ("E", "Trata-se de uma oração exclamativa que expressa unicamente uma opinião subjetiva do investigado.")
        ],
        "expl": "A alternativa A está correta. A frase é um paradoxo autorreferencial (paradoxo do mentiroso): se for verdadeira, é falsa; se for falsa, é verdadeira. Por violar os princípios da não contradição e do terceiro excluído, não admite valor lógico consistente e não é proposição lógica."
    },

    # --- a00/s06 (q6 a q11) ---
    {
        "seg": "a00/s06",
        "ans": "B",
        "stem": "Em relação à tabela-verdade do conectivo bicondicional (simbolizado por p <-> q, lido como 'p se e somente se q'), assinale a opção correta.",
        "opts": [
            ("A", "A proposição bicondicional resulta verdadeira sempre que a primeira proposição for verdadeira."),
            ("B", "A proposição bicondicional é verdadeira se, e somente se, ambas as proposições tiverem valores lógicos iguais."),
            ("C", "A proposição bicondicional assume valor lógico falso quando ambas as proposições forem simultaneamente falsas."),
            ("D", "A proposição bicondicional equivale logicamente à disjunção inclusiva entre as duas proposições componentes."),
            ("E", "A proposição bicondicional será falsa caso as proposições componentes tenham ambas o mesmo valor lógico.")
        ],
        "expl": "A alternativa B está correta. A bicondicional p <-> q é verdadeira quando suas componentes possuem o mesmo valor lógico (V <-> V = V e F <-> F = V) e falsa quando possuem valores lógicos distintos (V <-> F = F e F <-> V = F). As demais opções contradizem as regras da tabela-verdade da bicondicional."
    },
    {
        "seg": "a00/s06",
        "ans": "C",
        "stem": "No estudo das estruturas lógicas, as noções de condição suficiente e condição necessária são essenciais na análise de condicionais e bicondicionais. A esse respeito, assinale a opção correta.",
        "opts": [
            ("A", "Na condicional 'se p, então q', a proposição q é condição suficiente para a ocorrência da proposição p."),
            ("B", "Na condicional 'se p, então q', a proposição p é condição necessária para a ocorrência da proposição q."),
            ("C", "Na bicondicional 'p se e somente se q', a proposição p é condição necessária e suficiente para q, e vice-versa."),
            ("D", "Em qualquer condicional, antecedente e consequente representam mutuamente condições necessárias e suficientes."),
            ("E", "O conectivo de disjunção exclusiva estabelece uma relação de condição suficiente e necessária mútua.")
        ],
        "expl": "A alternativa C está correta. Na bicondicional p <-> q ocorre implicação mútua (p -> q e q -> p), de modo que p é condição necessária e suficiente para q, e vice-versa. Na condicional simples p -> q, p é apenas suficiente para q, e q é necessária para p, tornando incorretas as opções A, B e D."
    },
    {
        "seg": "a00/s06",
        "ans": "D",
        "stem": "Um agente de polícia registrou a seguinte norma operacional: 'O plantão será reforçado se, e somente se, houver operação programada ou ocorrer manifestação pública na cidade'. Considerando P como 'O plantão será reforçado', O como 'Há operação programada' e M como 'Ocorre manifestação pública', assinale a opção que representa corretamente a estrutura simbólica dessa proposição.",
        "opts": [
            ("A", "P -> (O e M)"),
            ("B", "(P ou O) <-> M"),
            ("C", "(O ou M) -> P"),
            ("D", "P <-> (O ou M)"),
            ("E", "P e (O <-> M)")
        ],
        "expl": "A alternativa D está correta. A expressão se, e somente se conecta bicondicionalmente a proposição simples P à proposição composta subsequente, que consiste na disjunção inclusiva indicada pela conjunção alternativa ou entre O e M, resultando na fórmula P <-> (O ou M)."
    },
    {
        "seg": "a00/s06",
        "ans": "E",
        "stem": "Considere as seguintes proposições simples: p: '7 + 5 = 12'; q: 'O número 9 é um número par'; r: '3 elevado ao quadrado é igual a 6'. A respeito da valoração de proposições compostas com esses termos, assinale a opção que apresenta uma proposição com valor lógico VERDADEIRO.",
        "opts": [
            ("A", "p <-> q"),
            ("B", "p -> r"),
            ("C", "q <-> p"),
            ("D", "p e q"),
            ("E", "q <-> r")
        ],
        "expl": "A alternativa E está correta. Os valores lógicos são: p é V (7 + 5 = 12); q é F (9 é ímpar); r é F (3² = 9). Na opção E, temos q <-> r, ou seja, F <-> F = V, pois ambas possuem o mesmo valor lógico falso. Nas demais: A resulta V <-> F = F; B resulta V -> F = F; C resulta F <-> V = F; D resulta V e F = F."
    },
    {
        "seg": "a00/s06",
        "ans": "A",
        "stem": "Em raciocínio lógico, uma proposição bicondicional p <-> q pode ser desdobrada na conjunção de duas proposições condicionais. Diante disso, assinale a opção que expressa uma formulação logicamente equivalente a p <-> q.",
        "opts": [
            ("A", "(p -> q) e (q -> p)"),
            ("B", "(p -> q) ou (q -> p)"),
            ("C", "(~p -> q) e (~q -> p)"),
            ("D", "(p e q) -> (p ou q)"),
            ("E", "~(p -> q) e ~(q -> p)")
        ],
        "expl": "A alternativa A está correta. A proposição bicondicional p <-> q afirma simultaneamente que p implica q e que q implica p, sendo logicamente equivalente à conjunção das duas condicionais recíprocas (p -> q) e (q -> p). As demais opções apresentam disjunções ou negações não equivalentes à bicondicional."
    },
    {
        "seg": "a00/s06",
        "ans": "B",
        "stem": "Em um manual de instruções da corporação policial, lê-se a seguinte determinação: 'O policial terá direito a folga compensatória se e somente se realizar plantão extraordinário em feriado oficial'. A partir dessa determinação, assinale a opção que expressa uma dedução logicamente correta.",
        "opts": [
            ("A", "O policial realizou plantão extraordinário em feriado oficial e não obteve folga compensatória."),
            ("B", "Se o policial obteve a folga compensatória, então ele realizou plantão extraordinário em feriado oficial."),
            ("C", "Se o policial não realizou plantão extraordinário no feriado, ele ainda assim terá a folga garantida."),
            ("D", "A realização do plantão extraordinário em feriado oficial é condição suficiente, mas não necessária, para a folga."),
            ("E", "Ter direito a folga compensatória não garante que o policial tenha realizado o plantão no feriado.")
        ],
        "expl": "A alternativa B está correta. A bicondicional F <-> P engloba duas condicionais verdadeiras: P -> F e F -> P. Portanto, se o policial obteve a folga (F), então necessariamente realizou o plantão (P). A opção A viola a regra (tornaria a bicondicional falsa), C nega a condição necessária e D e E ignoram a reciprocidade lógica."
    },

    # --- a00/s11 (q12 a q17) ---
    {
        "seg": "a00/s11",
        "ans": "C",
        "stem": "Ao construir a tabela-verdade de uma proposição lógica composta formada por 4 proposições simples distintas (p, q, r e s), o número total de linhas dessa tabela-verdade deve ser indicado corretamente. Com base nessa regra, assinale a opção correta.",
        "opts": [
            ("A", "8 linhas."),
            ("B", "12 linhas."),
            ("C", "16 linhas."),
            ("D", "24 linhas."),
            ("E", "32 linhas.")
        ],
        "expl": "A alternativa C está correta. O número total de linhas da tabela-verdade de uma proposição composta é calculado pela fórmula 2^n, em que n é a quantidade de proposições simples distintas. Com n = 4, temos 2^4 = 16 linhas. As demais opções trazem cálculos aritméticos incorretos."
    },
    {
        "seg": "a00/s11",
        "ans": "D",
        "stem": "Sabe-se que a proposição composta 'O suspeito foi detido ou a arma foi apreendida' é FALSA. Diante dessa informação acerca da disjunção inclusiva, assinale a opção que apresenta uma conclusão logicamente necessária.",
        "opts": [
            ("A", "O suspeito foi detido e a arma foi apreendida."),
            ("B", "O suspeito foi detido, mas a arma não foi apreendida."),
            ("C", "O suspeito não foi detido, porém a arma foi apreendida."),
            ("D", "O suspeito não foi detido e a arma não foi apreendida."),
            ("E", "Ao menos uma das duas ocorrências de fato aconteceu.")
        ],
        "expl": "A alternativa D está correta. Na tabela-verdade da disjunção inclusiva (p ou q), a proposição só é falsa quando ambas as parcelas são simultaneamente falsas. Logo, p é F (o suspeito não foi detido) e q é F (a arma não foi apreendida), configurando a conjunção de que nenhuma das duas ocorreu."
    },
    {
        "seg": "a00/s11",
        "ans": "E",
        "stem": "Em uma investigação preliminar, foram apurados como VERDADEIROS os seguintes fatos: (1) O cofre foi violado; (2) O alarme não tocou; (3) As câmeras de segurança não foram desligadas. Considerando a veracidade desses fatos, assinale a opção que apresenta uma proposição composta com valor lógico VERDADEIRO.",
        "opts": [
            ("A", "O alarme tocou ou as câmeras foram desligadas."),
            ("B", "Se o cofre foi violado, então o alarme tocou."),
            ("C", "O cofre foi violado e as câmeras foram desligadas."),
            ("D", "As câmeras foram desligadas se e somente se o cofre foi violado."),
            ("E", "Se o alarme tocou, então o cofre não foi violado.")
        ],
        "expl": "A alternativa E está correta. Pelos fatos dados: 'alarme tocou' é F e 'câmeras desligadas' é F. Na condicional da opção E, o antecedente 'o alarme tocou' é F, e qualquer condicional com antecedente falso é verdadeira (F -> F = V). As opções A, B, C e D resultam todas em proposições falsas."
    },
    {
        "seg": "a00/s11",
        "ans": "A",
        "stem": "No raciocínio lógico formal, deve-se ter rigor quanto ao significado da negação e ao uso de palavras antônimas da linguagem cotidiana. A esse respeito, assinale a opção correta.",
        "opts": [
            ("A", "Dizer que 'o procedimento não é legal' não é logicamente equivalente a afirmar que 'o procedimento é ilegal', caso existam condutas extralegais ou atípicas."),
            ("B", "A negação lógica de uma proposição verdadeira resulta sempre em uma proposição de valor lógico indeterminado."),
            ("C", "Duas proposições são logicamente contrárias se, e somente se, forem formadas por termos rigorosamente sinônimos."),
            ("D", "Em termos estritamente formais, a negação de uma sentença é obtida apenas pela troca do adjetivo por seu antônimo dicionarizado."),
            ("E", "A afirmação 'o réu não é culpado' implica necessariamente que ele foi declarado inocente por sentença irrecorrível.")
        ],
        "expl": "A alternativa A está correta. A negação lógica de p é simplesmente ~p (não-p). A substituição de um termo por seu antônimo dicionarizado frequentemente ignora gradações intermediárias ou universos conceituais distintos. A opção B é falsa pois ~V = F, C e D trazem regras linguísticas alheias à lógica formal e E extrapola a inferência."
    },
    {
        "seg": "a00/s11",
        "ans": "B",
        "stem": "Considere que a proposição condicional 'Se o perito concluiu o laudo, então o mandado de busca foi expedido' é sabidamente FALSA. Com base nessa constatação, assinale a opção correta.",
        "opts": [
            ("A", "O perito não concluiu o laudo e o mandado de busca não foi expedido."),
            ("B", "O perito concluiu o laudo e o mandado de busca não foi expedido."),
            ("C", "O perito não concluiu o laudo e o mandado de busca foi expedido."),
            ("D", "O perito concluiu o laudo e o mandado de busca foi expedido."),
            ("E", "Não é possível determinar se o perito concluiu ou não o laudo pericial.")
        ],
        "expl": "A alternativa B está correta. Uma condicional p -> q só é falsa na tabela-verdade em uma única situação: quando o antecedente (p) é verdadeiro e o consequente (q) é falso (V -> F = F). Portanto, é forçoso concluir que o perito concluiu o laudo (V) e o mandado não foi expedido (F)."
    },
    {
        "seg": "a00/s11",
        "ans": "C",
        "stem": "Considere verdadeira a seguinte premissa condicional: 'Se o sistema de monitoramento detecta invasão, então a sirene de emergência é acionada'. Sabendo-se que a sirene de emergência NÃO foi acionada, assinale a opção que apresenta a conclusão logicamente válida por Modus Tollens.",
        "opts": [
            ("A", "O sistema de monitoramento certamente detectou a invasão no perímetro."),
            ("B", "A equipe de vigilância desligou manualmente os sensores externos."),
            ("C", "O sistema de monitoramento não detectou invasão no perímetro."),
            ("D", "Houve falha elétrica generalizada na central de alarmes do prédio."),
            ("E", "A sirene será acionada nos minutos subsequentes à ocorrência.")
        ],
        "expl": "A alternativa C está correta. Pela regra de inferência do Modus Tollens, dada a condicional verdadeira p -> q e a veracidade da negação do consequente (~q), decorre necessariamente a negação do antecedente (~p), ou seja, o sistema não detectou invasão. As demais opções introduzem conjecturas fáticas sem respaldo lógico."
    }
]
