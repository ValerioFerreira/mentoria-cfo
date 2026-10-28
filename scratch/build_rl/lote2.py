"""Lote 2: Aula 01 (a01/s03, a01/s04, a01/s08) - 18 questoes (q18 a q35)"""

QUESTOES = [
    # --- a01/s03 (q18 a q23) ---
    {
        "seg": "a01/s03",
        "ans": "D",
        "stem": "Considere a proposição condicional P dada por: 'Se o suspeito confessou o delito, então a arma foi localizada e a perícia confirmou a autoria', formalizada como p -> (q e r). Ao analisar a tabela-verdade dessa proposição P, assinale a opção que indica o número de linhas em que P resulta com valor lógico FALSO.",
        "opts": [
            ("A", "Exatamente 1 linha."),
            ("B", "Exatamente 2 linhas."),
            ("C", "Exatamente 4 linhas."),
            ("D", "Exatamente 3 linhas."),
            ("E", "Exatamente 5 linhas.")
        ],
        "expl": "A fórmula tem 3 proposições simples (p, q, r), totalizando 2³ = 8 linhas na tabela-verdade. A condicional p -> (q e r) só é falsa quando o antecedente p é V e o consequente (q e r) é F. O antecedente p é V em 4 linhas; nessas 4 linhas, a conjunção (q e r) é V apenas na linha em que q e r são ambos V, sendo falsa nas outras 3 linhas. Logo, a condicional é falsa em exatamente 3 linhas."
    },
    {
        "seg": "a01/s03",
        "ans": "E",
        "stem": "Na lógica proposicional, as proposições compostas são classificadas de acordo com os valores lógicos que assumem na última coluna de suas respectivas tabelas-verdade. Acerca do conceito de contingência, assinale a opção correta.",
        "opts": [
            ("A", "Contingência é toda proposição cuja tabela-verdade contém exclusivamente valores verdadeiros."),
            ("B", "Contingência é uma proposição que só pode ser valorada caso contenha quantificadores universais."),
            ("C", "Contingência é aquela proposição cuja tabela-verdade é inteiramente preenchida por valores falsos."),
            ("D", "Contingência é uma fórmula lógica que viola os princípios da identidade e da não contradição."),
            ("E", "Contingência é toda proposição composta cuja tabela-verdade apresenta pelo menos um valor verdadeiro e pelo menos um falso.")
        ],
        "expl": "A alternativa E está correta. Por definição, uma contingência (ou proposição contingente) é aquela cujo valor lógico depende dos valores atribuídos às suas proposições simples componentes, apresentando tanto o valor verdadeiro (V) quanto o valor falso (F) na última coluna de sua tabela-verdade. Proposições exclusivamente verdadeiras são tautologias (A) e exclusivamente falsas são contradições (C)."
    },
    {
        "seg": "a01/s03",
        "ans": "A",
        "stem": "Tautologia é toda proposição composta que assume invariavelmente o valor lógico verdadeiro em todas as linhas de sua tabela-verdade. Considerando essa definição, assinale a opção que apresenta uma tautologia.",
        "opts": [
            ("A", "(p e q) -> p"),
            ("B", "(p ou q) -> (p e q)"),
            ("C", "p -> (p e q)"),
            ("D", "(p -> q) -> (q -> p)"),
            ("E", "p <-> ~p")
        ],
        "expl": "A alternativa A está correta. Para a condicional (p e q) -> p ser falsa, o antecedente (p e q) precisaria ser V e o consequente p ser F. Porém, se (p e q) é V, obrigatoriamente p é V e q é V, o que torna impossível o consequente p ser falso. Como nunca ocorre V -> F, a condicional é verdadeira em todas as linhas da tabela-verdade, tratando-se de tautologia. As demais são contingências (B, C, D) ou contradição (E)."
    },
    {
        "seg": "a01/s03",
        "ans": "B",
        "stem": "Sejam p, q e r proposições simples com os seguintes valores lógicos já determinados: p é VERDADEIRA, q é FALSA e r é VERDADEIRA. Diante dessas informações, assinale a opção que apresenta a proposição composta cujo valor lógico é VERDADEIRO.",
        "opts": [
            ("A", "(p e q) ou ~r"),
            ("B", "(p -> q) <-> ~r"),
            ("C", "(p ou q) -> (q e r)"),
            ("D", "(~p ou q) e r"),
            ("E", "p <-> q")
        ],
        "expl": "A alternativa B está correta. Com p = V, q = F e r = V, temos: p -> q resulta V -> F = F; ~r resulta ~V = F. Assim, na alternativa B, temos (p -> q) <-> ~r, o que equivale a F <-> F = V, pois ambos os lados têm o mesmo valor falso. Analisando as outras: A dá (V e F) ou F = F ou F = F; C dá (V ou F) -> (F e V) = V -> F = F; D dá (F ou F) e V = F e V = F; E dá V <-> F = F."
    },
    {
        "seg": "a01/s03",
        "ans": "C",
        "stem": "No estudo das tabelas-verdade, a contradição ocupa papel de destaque na análise de consistência lógica. Em relação à definição e propriedades de uma contradição lógica, assinale a opção correta.",
        "opts": [
            ("A", "Uma contradição é uma proposição que se torna verdadeira quando o antecedente for falso."),
            ("B", "A negação lógica de uma contradição resulta sempre em uma fórmula contingente."),
            ("C", "Uma contradição é uma proposição composta que resulta falsa para qualquer combinação de valores lógicos de suas variáveis."),
            ("D", "Uma contradição requer obrigatoriamente a presença de pelo menos três conectivos condicionais distintos."),
            ("E", "A disjunção inclusiva entre duas proposições simples quaisquer configura sempre uma contradição.")
        ],
        "expl": "A alternativa C está correta. Uma contradição lógica (ou proposição contraditória) é aquela cuja tabela-verdade resulta inteiramente em valores lógicos falsos (F) em todas as suas linhas, independentemente dos valores das proposições atômicas que a integram. A negação de uma contradição é uma tautologia (e não contingência, erro da B). As opções A, D e E trazem conceitos desconexos."
    },
    {
        "seg": "a01/s03",
        "ans": "D",
        "stem": "Diz-se que uma proposição composta P implica logicamente uma proposição Q (P => Q) quando uma determinada condição formal é satisfeita. Com base na teoria da implicação lógica, assinale a opção que descreve corretamente essa condição.",
        "opts": [
            ("A", "A proposição bicondicional P <-> Q deve ser uma contingência."),
            ("B", "A conjunção P e Q deve assumir valor falso em todas as linhas da tabela."),
            ("C", "A disjunção P ou Q deve ser classificada como uma contradição formal."),
            ("D", "A proposição condicional P -> Q deve ser uma tautologia."),
            ("E", "A negação de P deve ser necessariamente equivalente à negação de Q.")
        ],
        "expl": "A alternativa D está correta. Na lógica formal, ocorre implicação lógica de P para Q (simbolizada por P => Q) se, e somente se, a condicional correspondente P -> Q for uma tautologia (ou seja, verdadeira para toda e qualquer linha de sua tabela-verdade). Quando a bicondicional P <-> Q é uma tautologia, diz-se que há equivalência lógica (P <=> Q)."
    },

    # --- a01/s04 (q24 a q29) ---
    {
        "seg": "a01/s04",
        "ans": "E",
        "stem": "O método da prova por absurdo (redução ao absurdo) é amplamente empregado para testar se uma proposição condicional é uma tautologia de forma mais célere que a tabela-verdade. Acerca do procedimento desse método, assinale a opção correta.",
        "opts": [
            ("A", "Supõe-se que a proposição condicional seja verdadeira e busca-se provar que seus termos são equivalentes."),
            ("B", "Atribui-se valor verdadeiro ao consequente e valor falso ao antecedente de modo a forçar a verdade da proposição."),
            ("C", "Determina-se que todas as proposições simples componentes sejam simultaneamente verdadeiras."),
            ("D", "Eliminam-se todos os conectivos lógicos da expressão até restar uma proposição atômica isolada."),
            ("E", "Supõe-se que a proposição condicional seja falsa (antecedente verdadeiro e consequente falso) e busca-se uma contradição lógica decorrente dessa hipótese.")
        ],
        "expl": "A alternativa E está correta. Para demonstrar por absurdo que uma condicional é tautológica, adota-se a hipótese de que ela possa ser falsa, o que só ocorre se o antecedente for verdadeiro (V) e o consequente for falso (F). A partir dessa premissa forçada, deduzem-se os valores das variáveis simples: se essa dedução conduzir a uma contradição lógica incontornável, a hipótese de falsidade é refutada, provando-se que a proposição é tautologia."
    },
    {
        "seg": "a01/s04",
        "ans": "A",
        "stem": "Considere a proposição composta: '[(p -> q) e p] -> q'. Aplicando o método da prova por absurdo para verificar a natureza dessa fórmula lógica, assinale a opção correta.",
        "opts": [
            ("A", "A fórmula é uma tautologia, pois supor a condicional falsa gera a contradição de que q é simultaneamente falso e verdadeiro."),
            ("B", "A fórmula é uma contradição, pois a tentativa de torná-la verdadeira gera incoerência aritmética nos conectivos."),
            ("C", "A fórmula é uma contingência, visto que é possível torná-la falsa atribuindo p = F e q = V sem incorrer em contradição."),
            ("D", "A fórmula não pode ser avaliada pelo método do absurdo por conter mais de um conectivo de implicação."),
            ("E", "A fórmula é logicamente equivalente à negação simples da proposição atômica p.")
        ],
        "expl": "A alternativa A está correta. Trata-se da forma clássica do Modus Ponens em forma condicional. Para supor a fórmula falsa, deve-se ter antecedente V e consequente F: logo, q = F e [(p -> q) e p] = V. Para a conjunção ser V, devemos ter p = V e (p -> q) = V. Mas substituindo p = V e q = F na condicional p -> q, obtemos V -> F = F, contrariando o fato de que ela deveria ser V (ou seja, q teria que ser V e F ao mesmo tempo). Essa contradição prova que a condicional nunca pode ser falsa, sendo tautologia."
    },
    {
        "seg": "a01/s04",
        "ans": "B",
        "stem": "Ao analisar argumentos e fórmulas complexas contendo 4 ou mais variáveis proposicionais distintas, um perito opta pela prova por absurdo em detrimento da tabela-verdade. Assinale a opção que indica a justificativa técnica correta para essa escolha metodológica.",
        "opts": [
            ("A", "A tabela-verdade é matematicamente incapaz de processar expressões que tenham mais de três variáveis proposicionais."),
            ("B", "A tabela-verdade exigiria a construção e o cálculo de 16 ou mais linhas (2^n), enquanto o método por absurdo analisa diretamente a única hipótese de falsidade."),
            ("C", "O método da prova por absurdo transforma automaticamente todas as proposições contingentes em tautologias válidas."),
            ("D", "A prova por absurdo dispensa o conhecimento prévio das tabelas-verdade dos conectivos condicionais e bicondicionais."),
            ("E", "A tabela-verdade clássica não se aplica a argumentos que envolvem investigações criminais ou jurídicas.")
        ],
        "expl": "A alternativa B está correta. Como o número de linhas da tabela-verdade cresce exponencialmente à taxa de 2^n, para 4 variáveis são 16 linhas e para 5 variáveis são 32 linhas. Construir a tabela inteira é demorado e propenso a erros operacionais. O método por absurdo foca exclusivamente na hipótese de a condicional ser falsa (V -> F), resolvendo o problema em poucas deduções diretas."
    },
    {
        "seg": "a01/s04",
        "ans": "C",
        "stem": "Deseja-se verificar se a proposição composta P: '(p ou q) -> (p e q)' é tautologia, contradição ou contingência sem construir a tabela-verdade completa. A respeito dessa verificação, assinale a opção correta.",
        "opts": [
            ("A", "P é tautologia, pois sempre que p for verdadeira a expressão inteira assume valor verdadeiro."),
            ("B", "P é contradição, pois não existe nenhuma atribuição de valores que torne a fórmula verdadeira."),
            ("C", "P é contingência, pois com p = V e q = V a fórmula resulta V, mas com p = V e q = F a fórmula resulta F."),
            ("D", "P é tautologia, visto que supor a fórmula falsa não produz nenhuma linha válida de valoração."),
            ("E", "P é contradição, pois o conectivo condicional não pode ligar uma disjunção a uma conjunção.")
        ],
        "expl": "A alternativa C está correta. Para testar rapidamente contingência, basta encontrar ao menos uma linha que torne P verdadeira e ao menos uma que a torne falsa. Com p = V e q = V: (V ou V) -> (V e V) resulta V -> V = V. Com p = V e q = F: (V ou F) -> (V e F) resulta V -> F = F. Tendo casos V e casos F na tabela, P é classificada inequivocamente como contingência."
    },
    {
        "seg": "a01/s04",
        "ans": "D",
        "stem": "Considere a proposição P: '(p <-> q) e (p e ~q)'. Aplicando a análise dedutiva para determinar a natureza dessa proposição composta, assinale a opção correta.",
        "opts": [
            ("A", "P é uma tautologia, pois a conjunção de bicondicionais preserva a verdade em qualquer hipótese."),
            ("B", "P é uma contingência, pois resulta verdadeira quando p e q forem ambos verdadeiros."),
            ("C", "P é uma contingência, pois assume valor verdadeiro quando p for falsa e q for verdadeira."),
            ("D", "P é uma contradição lógica, pois as exigências de seus dois blocos conjuntivos são mutuamente incompatíveis."),
            ("E", "P é uma tautologia, visto que sua negação resulta em uma proposição identicamente falsa.")
        ],
        "expl": "A alternativa D está correta. A proposição é uma conjunção entre dois termos: (p <-> q) e (p e ~q). Para a conjunção ser verdadeira, ambos os termos precisam ser verdadeiros simultaneamente. O segundo termo (p e ~q) só é verdadeiro se p = V e q = F. Porém, com p = V e q = F, o primeiro termo (p <-> q) assume valor falso (V <-> F = F). Dessa forma, é absolutamente impossível que ambos sejam verdadeiros ao mesmo tempo, resultando em valor falso em todas as linhas, o que configura contradição."
    },
    {
        "seg": "a01/s04",
        "ans": "E",
        "stem": "Analise a proposição composta: '[(p e q) e r] -> [p <-> (q ou r)]'. Ao realizar a verificação lógica dessa estrutura condicional, assinale a opção correta.",
        "opts": [
            ("A", "Trata-se de uma contradição, pois a bicondicional interna nunca se harmoniza com a conjunção tripla."),
            ("B", "Trata-se de uma contingência que se torna falsa quando p, q e r assumem valores lógicos falsos."),
            ("C", "Trata-se de uma contingência que assume valor falso exatamente quando p é verdadeira e q é falsa."),
            ("D", "Trata-se de uma contradição, pois sua tabela-verdade possui 8 linhas todas com valor lógico F."),
            ("E", "Trata-se de uma tautologia, pois a única hipótese de antecedente verdadeiro força o consequente a ser igualmente verdadeiro.")
        ],
        "expl": "A alternativa E está correta. A expressão é uma condicional cujo antecedente é a conjunção tripla [(p e q) e r]. Essa conjunção só é verdadeira em um único caso: quando p = V, q = V e r = V. Substituindo essa única valoração no consequente [p <-> (q ou r)], temos: q ou r é V ou V = V; e p é V. Assim, temos V <-> V = V. Portanto, no único caso em que o antecedente é verdadeiro, o consequente também é verdadeiro (V -> V = V). Em todos os outros casos o antecedente é falso, tornando a condicional automaticamente verdadeira (F -> algo = V). Logo, a fórmula é uma tautologia."
    },

    # --- a01/s08 (q30 a q35) ---
    {
        "seg": "a01/s08",
        "ans": "A",
        "stem": "Considere a afirmação declarada por um investigador de polícia: 'O laudo papiloscópico foi concluído ou o laudo papiloscópico não foi concluído'. Do ponto de vista estritamente lógico-formal, assinale a opção correta.",
        "opts": [
            ("A", "A frase possui a estrutura formal p ou ~p, tratando-se de uma tautologia decorrente do princípio do terceiro excluído."),
            ("B", "A frase possui a estrutura de uma contradição lógica, pois une uma afirmação e sua própria negação por meio do conectivo ou."),
            ("C", "A frase é uma contingência empírica cujo valor de verdade depende exclusivamente da data de entrega do laudo."),
            ("D", "A frase expressa uma disjunção exclusiva que resulta falsa se o laudo papiloscópico de fato tiver sido concluído."),
            ("E", "A frase não se enquadra na lógica proposicional por conter repetição de termos em suas orações componentes.")
        ],
        "expl": "A alternativa A está correta. A frase tem a forma simbólica p ou ~p (disjunção inclusiva entre uma proposição e sua negação). Pela tabela-verdade: se p é V, ~p é F, logo V ou F = V; se p é F, ~p é V, logo F ou V = V. Como resulta invariavelmente verdadeira em qualquer circunstância, constitui uma tautologia formal, consagração do princípio clássico do terceiro excluído."
    },
    {
        "seg": "a01/s08",
        "ans": "B",
        "stem": "No contexto da lógica proposicional, assinale a opção que apresenta uma fórmula que exemplifica, por definição, uma contradição lógica clássica fundamentada no princípio da não contradição.",
        "opts": [
            ("A", "p ou ~p"),
            ("B", "p e ~p"),
            ("C", "p -> p"),
            ("D", "p <-> p"),
            ("E", "~(~p) <-> p")
        ],
        "expl": "A alternativa B está correta. A fórmula p e ~p representa a afirmação simultânea de uma proposição e de sua negação conectadas por conjunção. Se p é V, ~p é F, logo V e F = F; se p é F, ~p é V, logo F e V = F. Em todas as hipóteses a fórmula resulta invariavelmente falsa, constituindo o exemplo elementar de contradição na lógica formal. As demais opções são tautologias clássicas."
    },
    {
        "seg": "a01/s08",
        "ans": "C",
        "stem": "Considere a proposição composta formada pelo conectivo de disjunção exclusiva entre uma proposição simples p e sua respectiva negação: 'Ou p, ou ~p'. A respeito da classificação lógica dessa proposição composta, assinale a opção correta.",
        "opts": [
            ("A", "É uma contradição lógica, pois a disjunção exclusiva não admite proposições com sentidos opostos."),
            ("B", "É uma contingência, pois assume valor falso quando p for atribuída como verdadeira."),
            ("C", "É uma tautologia, pois as duas parcelas têm obrigatoriamente valores lógicos opostos, tornando a disjunção exclusiva sempre verdadeira."),
            ("D", "É uma sentença aberta, haja vista que a ausência de conectivos condicionais impede o fechamento da tabela."),
            ("E", "É equivalente a uma condicional cujo antecedente e consequente são ambos falsos.")
        ],
        "expl": "A alternativa C está correta. Na disjunção exclusiva (ou... ou), a proposição só é verdadeira quando as parcelas componentes possuem valores lógicos distintos (uma verdadeira e outra falsa). Como p e ~p possuem invariavelmente valores opostos (se p é V, ~p é F; se p é F, ~p é V), a disjunção exclusiva entre elas será sempre verdadeira em qualquer linha da tabela-verdade, tratando-se, portanto, de uma tautologia."
    },
    {
        "seg": "a01/s08",
        "ans": "D",
        "stem": "Considere uma proposição simples atômica isolada, tal como: 'O agente de polícia participou da operação na capital pernambucana'. Em relação à sua classificação lógica formal, assinale a opção correta.",
        "opts": [
            ("A", "Classifica-se como uma tautologia, pois relata um fato inserido em contexto institucional oficial."),
            ("B", "Classifica-se como uma contradição lógica, visto que não apresenta conectivos que sustentem sua dedução."),
            ("C", "Classifica-se como uma equivalência lógica, uma vez que toda proposição simples é idêntica a si mesma."),
            ("D", "Classifica-se como uma contingência, pois seu valor lógico depende de averiguação fática no mundo real, podendo ser verdadeira ou falsa."),
            ("E", "Classifica-se como um argumento dedutivo válido de premissa única e conclusão autoevidente.")
        ],
        "expl": "A alternativa D está correta. Uma proposição simples isolada que relata um evento do mundo empírico não é logicamente necessária nem logicamente impossível. Ela pode ser verdadeira (se o fato ocorreu) ou falsa (se o fato não ocorreu), o que caracteriza exatamente uma contingência na classificação das proposições."
    },
    {
        "seg": "a01/s08",
        "ans": "E",
        "stem": "Em um depoimento pericial, o perito declarou: 'O relatório pericial entregue ao delegado é conclusivo, mas não é conclusivo'. Sob a perspectiva da lógica formal das proposições, assinale a opção correta.",
        "opts": [
            ("A", "Trata-se de uma proposição contingente, pois depende da leitura dos anexos do documento pericial."),
            ("B", "Trata-se de uma tautologia, haja vista que a conjunção adversativa atenua o rigor lógico da contradição."),
            ("C", "Trata-se de uma sentença imperativa que solicita esclarecimentos complementares à corregedoria."),
            ("D", "Trata-se de uma equivalência lógica direta entre duas orações subordinadas consecutivas."),
            ("E", "Trata-se de uma contradição lógica, pois o conectivo adversativo 'mas' funciona como conjunção aditiva ligando uma proposição à sua própria negação.")
        ],
        "expl": "A alternativa E está correta. Na lógica proposicional, conjunções adversativas da língua portuguesa como 'mas', 'porém', 'contudo' e 'todavia' funcionam com valor lógico de conjunção aditiva (e). Assim, a declaração se estrutura simbolicamente como p e ~p ('o relatório é conclusivo e o relatório não é conclusivo'), o que configura uma contradição lógica absoluta, assumindo valor falso em qualquer circunstância."
    },
    {
        "seg": "a01/s08",
        "ans": "A",
        "stem": "Considere a proposição composta: 'p <-> ~p', que conecta uma proposição simples à sua negação por meio de um conectivo bicondicional. Em relação à classificação dessa fórmula na lógica clássica, assinale a opção correta.",
        "opts": [
            ("A", "É uma contradição lógica, pois a bicondicional só é verdadeira quando ambos os lados possuem o mesmo valor lógico, o que nunca ocorre entre p e ~p."),
            ("B", "É uma tautologia, visto que a bicondicional preserva a relação de simetria reflexiva de qualquer proposição."),
            ("C", "É uma contingência, pois resulta verdadeira quando p é verdadeira e falsa quando p é falsa."),
            ("D", "É uma proposição condicional disfarçada que assume valor verdadeiro em exatamente duas linhas."),
            ("E", "É uma sentença aberta que carece de quantificador existencial para definir seu valor lógico.")
        ],
        "expl": "A alternativa A está correta. A proposição bicondicional p <-> q só é verdadeira se p e q tiverem exatamente o mesmo valor de verdade (ambas V ou ambas F). Como p e ~p têm sempre valores lógicos opostos (se p é V, ~p é F; se p é F, ~p é V), a bicondicional p <-> ~p é falsa em todas as linhas possíveis de sua tabela-verdade, tratando-se rigorosamente de uma contradição lógica."
    }
]
