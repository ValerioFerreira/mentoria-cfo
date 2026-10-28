"""Bloco 2 das novas questoes de Raciocinio Logico (34 questoes: q43 a q76).
Trechos: a02/s03 (2), a02/s04 (5), a02/s07 (2), a02/s11 (3), a03/s01 (3),
         a04/s03 (5), a04/s05 (4), a04/s06 (5), a05/s03 (5).
Gabaritos extraidos estritamente de gabaritos_132.json (indices 43 a 76).
"""

QUESTOES_BLOCO2 = [
    # --- a02/s03 (q43 a q44) ---
    {
        "seg": "a02/s03",
        "ans": "D",
        "stem": "Considere a proposição: 'O delegado deferiu o pedido e o mandado de busca foi expedido'. Aplicando as leis de De Morgan para negar essa conjunção, assinale a opção que expressa a negação correta.",
        "opts": [
            ("A", "O delegado deferiu o pedido ou o mandado de busca não foi expedido."),
            ("B", "O delegado não deferiu o pedido e o mandado de busca não foi expedido."),
            ("C", "Se o delegado deferiu o pedido, então o mandado de busca foi expedido."),
            ("D", "O delegado não deferiu o pedido ou o mandado de busca não foi expedido."),
            ("E", "O delegado deferiu o pedido se e somente se o mandado foi expedido.")
        ],
        "expl": "Pela primeira lei de De Morgan, a negação de uma conjunção (p e q) é a disjunção inclusiva das negações (~p ou ~q). Assim, nega-se a primeira parcela ('o delegado não deferiu o pedido'), nega-se a segunda parcela ('o mandado de busca não foi expedido') e conecta-se ambas pelo conectivo disjuntivo 'ou'."
    },
    {
        "seg": "a02/s03",
        "ans": "E",
        "stem": "Considere a condicional: 'Se a perícia técnica for inconclusiva, então o inquérito policial será prorrogado'. Assinale a opção que expressa a NEGAÇÃO lógica dessa proposição condicional.",
        "opts": [
            ("A", "Se a perícia técnica não for inconclusiva, o inquérito não será prorrogado."),
            ("B", "A perícia técnica não é inconclusiva ou o inquérito não será prorrogado."),
            ("C", "A perícia técnica não é inconclusiva e o inquérito policial será prorrogado."),
            ("D", "Se o inquérito policial não for prorrogado, a perícia não é inconclusiva."),
            ("E", "A perícia técnica é inconclusiva e o inquérito policial não será prorrogado.")
        ],
        "expl": "A negação de uma proposição condicional da forma p -> q é a conjunção p e ~q. Preserva-se o antecedente na forma original ('a perícia técnica é inconclusiva') e nega-se o consequente ('o inquérito policial não será prorrogado'), unindo as proposições pelo conectivo conjuntivo 'e'."
    },

    # --- a02/s04 (q45 a q49) ---
    {
        "seg": "a02/s04",
        "ans": "E",
        "stem": "No estudo da negação da disjunção exclusiva (ou... ou), a álgebra proposicional estabelece uma equivalência fundamental com outro conectivo clássico. Assinale a opção que apresenta a correta negação da proposição: 'Ou o suspeito é liberado, ou o suspeito é autuado'.",
        "opts": [
            ("A", "O suspeito não é liberado e o suspeito não é autuado pela autoridade."),
            ("B", "O suspeito é liberado ou o suspeito é autuado pela autoridade policial."),
            ("C", "Se o suspeito é liberado, então o suspeito é autuado pela autoridade."),
            ("D", "Nem o suspeito é liberado, nem o suspeito é autuado na delegacia."),
            ("E", "O suspeito é liberado se e somente se o suspeito for autuado.")
        ],
        "expl": "A negação lógica da disjunção exclusiva (p ou exclusivo q) é a proposição bicondicional (p se e somente se q). A disjunção exclusiva só é verdadeira quando as proposições componentes possuem valores lógicos opostos; sua negação, portanto, deve ser verdadeira quando ambas tiverem valores lógicos idênticos, o que caracteriza a bicondicional."
    },
    {
        "seg": "a02/s04",
        "ans": "B",
        "stem": "Considere a conjunção de duas condicionais: '(p -> q) e (r -> s)'. Ao aplicar a regra da contrapositiva a cada uma das condicionais componentes, assinale a opção que expressa uma proposição logicamente equivalente.",
        "opts": [
            ("A", "(~p -> ~q) e (~r -> ~s)"),
            ("B", "(~q -> ~p) e (~s -> ~r)"),
            ("C", "(q -> p) e (s -> r)"),
            ("D", "(~q -> ~p) ou (~s -> ~r)"),
            ("E", "~(p -> q) e ~(r -> s)")
        ],
        "expl": "Como a proposição composta consiste na conjunção de dois blocos condicionais independentes, a substituição de cada condicional por sua respectiva contrapositiva preserva a equivalência lógica estrita: p -> q equivale a ~q -> ~p, e r -> s equivale a ~s -> ~r, mantendo-se a conjunção 'e' entre os blocos."
    },
    {
        "seg": "a02/s04",
        "ans": "E",
        "stem": "A respeito das equivalências lógicas da proposição bicondicional p <-> q, assinale a opção correta.",
        "opts": [
            ("A", "A bicondicional equivale logicamente à disjunção inclusiva p ou q."),
            ("B", "A bicondicional p <-> q equivale à negação conjunta ~p e ~q."),
            ("C", "A bicondicional equivale à condicional simples com antecedentes invertidos."),
            ("D", "A negação da bicondicional é uma proposição tautológica clássica."),
            ("E", "A bicondicional p <-> q equivale logicamente à conjunção de duas condicionais: (p -> q) e (q -> p).")
        ],
        "expl": "Por definição fundamental da lógica formal clássica, a bicondicional p <-> q ('p se e somente se q') expressa uma dupla implicação mútua, sendo rigorosamente equivalente à conjunção das duas condicionais recíprocas (p -> q) e (q -> p)."
    },
    {
        "seg": "a02/s04",
        "ans": "B",
        "stem": "Considere a proposição disjuntiva exclusiva: 'Ou o veículo foi furtado, ou o veículo foi clonado'. Assinale a opção que apresenta uma proposição equivalente à sua NEGAÇÃO expressa exclusivamente por meio de conjunções e disjunções.",
        "opts": [
            ("A", "(v e c) e (~v e ~c)"),
            ("B", "(v e c) ou (~v e ~c)"),
            ("C", "(v ou c) e (~v ou ~c)"),
            ("D", "(v e ~c) ou (~v e c)"),
            ("E", "(v ou ~c) e (~v ou c)")
        ],
        "expl": "A negação da disjunção exclusiva é a bicondicional v <-> c. Uma bicondicional é verdadeira quando ambas as proposições componentes são simultaneamente verdadeiras (v e c) ou quando ambas são simultaneamente falsas (~v e ~c). Unindo esses dois cenários possíveis por disjunção, obtém-se a expressão equivalente (v e c) ou (~v e ~c)."
    },
    {
        "seg": "a02/s04",
        "ans": "A",
        "stem": "Em um termo circunstanciado, consta a seguinte proposição composta: 'O acusado permaneceu em silêncio ou prestou depoimento circunstanciado', com sentido de disjunção exclusiva. Assinale a opção que indica a condição necessária e suficiente para que essa afirmação seja verdadeira.",
        "opts": [
            ("A", "Exatamente uma das duas ações ter ocorrido, sendo a outra comprovadamente falsa."),
            ("B", "Ambas as ações terem ocorrido simultaneamente na mesma assentada judicial."),
            ("C", "Nenhuma das duas ações ter sido praticada pelo acusado durante a oitiva."),
            ("D", "A declaração ter sido homologada previamente pelo Ministério Público estadual."),
            ("E", "O acusado ter confessado integralmente a prática delitiva apurada nos autos.")
        ],
        "expl": "A disjunção exclusiva (ou... ou) exige para sua veracidade que as proposições componentes possuam valores lógicos distintos: exatamente uma das parcelas deve ser verdadeira e a outra deve ser falsa. Se ambas ocorrerem ou se nenhuma ocorrer, a disjunção exclusiva resulta falsa."
    },

    # --- a02/s07 (q50 a q51) ---
    {
        "seg": "a02/s07",
        "ans": "B",
        "stem": "Considere a fórmula lógica envolvendo bicondicionais: '(p <-> q) <-> (~p <-> ~q)'. Ao avaliar a classificação dessa proposição composta por meio de suas propriedades lógicas, assinale a opção correta.",
        "opts": [
            ("A", "Trata-se de uma contradição lógica em razão do conflito entre negações."),
            ("B", "Trata-se de uma tautologia, pois p <-> q e ~p <-> ~q são fórmulas logicamente equivalentes."),
            ("C", "Trata-se de uma contingência que resulta falsa quando p é verdadeira e q é falsa."),
            ("D", "Trata-se de uma contingência que assume valor verdadeiro em apenas uma linha."),
            ("E", "Trata-se de uma contradição resultante da aplicação inadequada de De Morgan.")
        ],
        "expl": "A expressão ~p <-> ~q possui rigorosamente a mesma tabela-verdade da fórmula original p <-> q (negar ambos os lados de uma bicondicional preserva seu valor lógico em todas as linhas). Como os dois lados da bicondicional principal têm sempre valores lógicos idênticos, a fórmula global resulta invariavelmente verdadeira, sendo uma tautologia."
    },
    {
        "seg": "a02/s07",
        "ans": "E",
        "stem": "Deseja-se verificar a equivalência lógica entre duas proposições compostas P e Q. Assinale a opção que expressa o critério técnico universal de equivalência no cálculo proposicional.",
        "opts": [
            ("A", "A conjunção P e Q deve assumir valor falso em todas as linhas da tabela."),
            ("B", "A disjunção P ou Q deve ser classificada como uma contradição formal."),
            ("C", "O antecedente P deve conter exatamente o dobro de operadores do consequente Q."),
            ("D", "As duas proposições devem ser formuladas com as mesmas palavras da língua natural."),
            ("E", "As proposições P e Q devem apresentar tabelas-verdade idênticas para as mesmas atribuições de valores.")
        ],
        "expl": "Duas proposições P e Q são ditas logicamente equivalentes (P <=> Q) se, e somente se, apresentarem exatamente os mesmos valores lógicos em todas as linhas correspondentes de suas respectivas tabelas-verdade. Isso equivale a demonstrar que a proposição bicondicional P <-> Q é uma tautologia."
    },

    # --- a02/s11 (q52 a q54) ---
    {
        "seg": "a02/s11",
        "ans": "E",
        "stem": "Considere a condicional: 'Se o policial porta distintivo funcional, então tem livre acesso aos recintos sujeitos a fiscalização'. Assinale a opção que expressa uma proposição logicamente equivalente sob a forma de disjunção inclusiva.",
        "opts": [
            ("A", "O policial porta distintivo funcional ou não tem livre acesso aos recintos."),
            ("B", "O policial não porta distintivo funcional e tem livre acesso aos recintos."),
            ("C", "O policial tem livre acesso aos recintos ou porta distintivo funcional."),
            ("D", "O policial não porta distintivo funcional e não tem livre acesso aos recintos."),
            ("E", "O policial não porta distintivo funcional ou tem livre acesso aos recintos sujeitos a fiscalização.")
        ],
        "expl": "Pela regra fundamental de equivalência lógica, uma condicional p -> q pode ser convertida na disjunção inclusiva equivalente ~p ou q (nega-se o antecedente, substitui-se o conectivo por 'ou' e mantém-se o consequente). Assim, 'se porta distintivo, tem acesso' equivale a 'não porta distintivo ou tem acesso'."
    },
    {
        "seg": "a02/s11",
        "ans": "C",
        "stem": "A contrapositiva é a principal equivalência lógica que transforma uma condicional em outra condicional. Considere a proposição: 'Se o laudo cadavérico apontar asfixia, a autoridade policial tipificará o fato como homicídio'. Assinale a opção que apresenta sua contrapositiva correta.",
        "opts": [
            ("A", "Se o laudo cadavérico não apontar asfixia, a autoridade não tipificará o fato como homicídio."),
            ("B", "Se a autoridade tipificar o fato como homicídio, o laudo apontou asfixia mecânica."),
            ("C", "Se a autoridade não tipificar o fato como homicídio, o laudo não apontou asfixia."),
            ("D", "O laudo cadavérico não apontou asfixia ou a autoridade tipificou o fato como homicídio."),
            ("E", "A autoridade policial tipifica o fato como homicídio se e somente se o laudo apontar asfixia.")
        ],
        "expl": "A contrapositiva de uma condicional p -> q constrói-se invertendo a ordem das proposições e negando simultaneamente ambos os termos: ~q -> ~p. Assim, a equivalente contrapositiva de 'Se o laudo aponta asfixia, a autoridade tipifica como homicídio' é 'Se a autoridade não tipifica como homicídio, então o laudo não apontou asfixia'."
    },
    {
        "seg": "a02/s11",
        "ans": "C",
        "stem": "Considere a proposição disjuntiva: 'O agente redige o expediente administrativo ou cumpre a intimação judicial'. Assinale a opção que apresenta uma proposição condicional equivalente a essa disjunção inclusiva.",
        "opts": [
            ("A", "Se o agente redige o expediente administrativo, então cumpre a intimação judicial."),
            ("B", "Se o agente cumpre a intimação judicial, então redige o expediente administrativo."),
            ("C", "Se o agente não redige o expediente administrativo, então cumpre a intimação judicial."),
            ("D", "Se o agente não cumpre a intimação judicial, então não redige o expediente administrativo."),
            ("E", "O agente redige o expediente se e somente se cumprir a intimação judicial da comarca.")
        ],
        "expl": "A disjunção inclusiva p ou q equivale à condicional ~p -> q (nega-se o primeiro termo e mantém-se o segundo sob condicional). Aplicando à frase 'O agente redige o expediente (p) ou cumpre a intimação (q)', obtém-se a condicional equivalente 'Se o agente não redige o expediente administrativo, então cumpre a intimação judicial'."
    },

    # --- a03/s01 (q55 a q57) ---
    {
        "seg": "a03/s01",
        "ans": "B",
        "stem": "Na lógica de predicados e diagramas lógicos, os quantificadores ligam variáveis e atribuem sentido completo a sentenças abertas. A respeito do quantificador universal, simbolizado por ∀, assinale a opção correta.",
        "opts": [
            ("A", "O quantificador universal afirma que a propriedade é satisfeita por pelo menos um indivíduo."),
            ("B", "O quantificador universal afirma que a propriedade aplica-se a todos os elementos do conjunto universo."),
            ("C", "O quantificador universal equivale logicamente ao quantificador de inexistência absoluta."),
            ("D", "A aplicação de um quantificador universal transforma uma proposição em sentença aberta."),
            ("E", "O quantificador universal é incompatível com proposições que contenham negações internas.")
        ],
        "expl": "O quantificador universal (simbolizado por ∀ e lido como 'para todo', 'qualquer que seja' ou 'todos') estabelece que determinada propriedade ou predicado é válido e verificado para todo e qualquer elemento pertencente ao conjunto do universo considerado."
    },
    {
        "seg": "a03/s01",
        "ans": "A",
        "stem": "O quantificador existencial, simbolizado por ∃, expressa a existência de elementos que satisfazem determinado predicado lógico. Assinale a opção que expressa uma formulação em linguagem natural equivalente a ∃x P(x).",
        "opts": [
            ("A", "Existe pelo menos um elemento que satisfaz o predicado P."),
            ("B", "Nenhum elemento pertencente ao conjunto universo satisfaz o predicado P."),
            ("C", "Todos os elementos do conjunto universo satisfazem integralmente o predicado P."),
            ("D", "Todo e qualquer indivíduo deixa de apresentar a propriedade enunciada por P."),
            ("E", "A propriedade P é formalmente indeterminada para todos os entes do universo.")
        ],
        "expl": "O quantificador existencial (simbolizado por ∃ e lido como 'existe', 'existe pelo menos um' ou 'algum') assevera a existência de ao menos um elemento no universo do discurso que torna verdadeira a condição expressa pelo predicado P(x)."
    },
    {
        "seg": "a03/s01",
        "ans": "D",
        "stem": "Considere a proposição quantificada universal: 'Todos os escrivães de polícia possuem diploma de curso superior'. Assinale a opção que expressa a NEGAÇÃO lógica dessa afirmativa.",
        "opts": [
            ("A", "Nenhum escrivão de polícia possui diploma de curso superior."),
            ("B", "Todos os escrivães de polícia não possuem diploma de curso superior."),
            ("C", "Qualquer cidadão com curso superior pode ser investido como escrivão de polícia."),
            ("D", "Existe pelo menos um escrivão de polícia que não possui diploma de curso superior."),
            ("E", "Mais da metade dos escrivães de polícia não concluiu o curso superior.")
        ],
        "expl": "A negação de uma proposição universal afirmativa ('Todo A é B') constrói-se com o quantificador existencial associado à negação do predicado ('Algum A não é B', 'Pelo menos um A não é B' ou 'Existe A que não é B'). A afirmativa 'Nenhum A é B' constitui a proposição contrária e não a negação contraditória da sentença."
    },

    # --- a04/s03 (q58 a q62) ---
    {
        "seg": "a04/s03",
        "ans": "A",
        "stem": "No estudo da lógica de argumentação, os argumentos dedutivos distinguem-se em categóricos e hipotéticos conforme a natureza de suas premissas. Assinale a opção que caracteriza um argumento hipotético.",
        "opts": [
            ("A", "Argumento que contém pelo menos uma premissa condicional, disjuntiva ou bicondicional."),
            ("B", "Argumento formado unicamente por proposições universais afirmativas da lógica de classes."),
            ("C", "Argumento indutivo baseado na repetição probabilística de dados estatísticos."),
            ("D", "Argumento que dispensa premissas por possuir uma conclusão autoevidente no mundo real."),
            ("E", "Argumento cuja validade formal depende exclusivamente da opinião da autoridade emissora.")
        ],
        "expl": "Um argumento hipotético (ou proposicional) é aquele que contém em sua estrutura pelo menos uma premissa composta por conectivos lógicos hipotéticos (como o condicional 'se... então', a disjunção 'ou' ou a bicondicional 'se e somente se'). O argumento categórico, por sua vez, opera com relações puras de inclusão ou exclusão entre classes."
    },
    {
        "seg": "a04/s03",
        "ans": "E",
        "stem": "A lógica formal estabelece uma separação técnica entre a validade de um argumento dedutivo e a veracidade empírica de suas proposições componentes. A esse respeito, assinale a opção correta.",
        "opts": [
            ("A", "A validade é uma propriedade exclusiva das proposições declarativas isoladas."),
            ("B", "A verdade é uma propriedade da estrutura dedutiva do argumento como um todo."),
            ("C", "Todo argumento dedutivo composto por premissas verdadeiras é necessariamente válido."),
            ("D", "Um argumento dedutivo que apresente premissas falsas é classificado como inválido."),
            ("E", "A validade é uma propriedade puramente relacional e formal entre as premissas e a conclusão.")
        ],
        "expl": "A validade é uma característica estritamente formal e estrutural que qualifica o encadeamento do argumento: um argumento dedutivo é válido se a verdade de suas premissas garante de modo necessário e inescapável a verdade de sua conclusão. Proposições isoladas são verdadeiras ou falsas; argumentos são válidos ou inválidos."
    },
    {
        "seg": "a04/s03",
        "ans": "B",
        "stem": "Considere o argumento dedutivo: Premissa 1: 'Todas as viaturas policiais são aeronaves supersônicas'. Premissa 2: 'O automóvel modelo X é uma viatura policial'. Conclusão: 'Logo, o automóvel modelo X é uma aeronave supersônica'. Avaliando esse argumento sob a perspectiva da lógica dedutiva, assinale a opção correta.",
        "opts": [
            ("A", "O argumento é inválido porque a primeira premissa é factualmente falsa no mundo real."),
            ("B", "O argumento é dedutivamente VÁLIDO, embora não seja um argumento materialmente sólido."),
            ("C", "O argumento é inválido porque comete a falácia do termo médio não distribuído."),
            ("D", "O argumento é classificado como uma indução empírica de conclusão improvável."),
            ("E", "O argumento é nulo em razão da impossibilidade mecânica de viaturas voarem.")
        ],
        "expl": "A forma do silogismo é perfeitamente válida: 'Todo A é B; X é A; logo, X é B'. Se as premissas fossem verdadeiras, a conclusão decorreria de modo obrigatório e necessário. A falsidade factual da premissa no mundo empírico retira a solidez do argumento, mas preserva intacta a sua validade dedutiva formal."
    },
    {
        "seg": "a04/s03",
        "ans": "E",
        "stem": "Um argumento dedutivo é considerado formalmente INVÁLIDO quando ocorre qual circunstância técnica? Assinale a opção correta.",
        "opts": [
            ("A", "Quando as premissas e a conclusão forem simultaneamente verdadeiras."),
            ("B", "Quando a conclusão for uma proposição tautológica clássica demonstrada."),
            ("C", "Quando todas as suas premissas forem proposições empíricas contingentes."),
            ("D", "Quando contiver exatamente três termos categóricos e duas premissas afirmativas."),
            ("E", "Quando for logicamente possível que todas as premissas sejam verdadeiras e a conclusão seja falsa.")
        ],
        "expl": "O critério definidor e universal da invalidade dedutiva é a possibilidade de um contraexemplo lógico: se existir qualquer cenário ou atribuição de valores em que todas as premissas sejam verdadeiras e, concomitantemente, a conclusão resulte falsa, o argumento é categoricamente inválido."
    },
    {
        "seg": "a04/s03",
        "ans": "C",
        "stem": "A representação formal padrão de um argumento dedutivo organiza premissas e conclusão em uma estrutura canônica. Assinale a opção que expressa corretamente a representação de um argumento de premissas P1, P2 e conclusão C na forma condicional associada.",
        "opts": [
            ("A", "(P1 ou P2) -> C"),
            ("B", "(P1 e P2) <-> C"),
            ("C", "(P1 e P2) -> C"),
            ("D", "C -> (P1 e P2)"),
            ("E", "(P1 -> P2) -> C")
        ],
        "expl": "A condicional associada a um argumento dedutivo une a conjunção de todas as suas premissas como antecedente e coloca a conclusão do argumento como consequente: (P1 e P2 e ... e Pn) -> C. Um argumento é dedutivamente válido se, e somente se, a sua condicional associada for uma tautologia."
    },

    # --- a04/s05 (q63 a q66) ---
    {
        "seg": "a04/s05",
        "ans": "E",
        "stem": "O método da conclusão falsa é uma técnica ágil para testar a validade de argumentos dedutivos sem a necessidade de desenhar a tabela-verdade completa. Acerca do procedimento desse método, assinale a opção correta.",
        "opts": [
            ("A", "Atribui-se valor verdadeiro à conclusão e busca-se provar que as premissas são contingentes."),
            ("B", "Atribui-se valor falso a todas as premissas para forçar a veracidade da conclusão dedutiva."),
            ("C", "Eliminam-se as premissas que contenham conectivos disjuntivos para simplificar a prova."),
            ("D", "Supõe-se que a conclusão seja uma sentença aberta para aplicar quantificadores universais."),
            ("E", "Supõe-se que a conclusão seja FALSA e tenta-se tornar todas as premissas simultaneamente VERDADEIRAS.")
        ],
        "expl": "No método da conclusão falsa, busca-se intencionalmente construir um contraexemplo: assume-se que a conclusão é falsa e tenta-se encontrar valores para as variáveis simples que tornem todas as premissas verdadeiras. Se isso for possível, o argumento é inválido; se essa tentativa gerar contradição inevitável, o argumento é válido."
    },
    {
        "seg": "a04/s05",
        "ans": "D",
        "stem": "Considere o argumento: Premissa 1: 'Se o alarme toca, o vigilante comparece'. Premissa 2: 'O vigilante compareceu'. Conclusão: 'Logo, o alarme tocou'. Aplicando o método do teste de validade, assinale a opção correta.",
        "opts": [
            ("A", "O argumento é dedutivamente válido por aplicação da regra do Modus Ponens."),
            ("B", "O argumento é dedutivamente válido por aplicação da regra do Modus Tollens."),
            ("C", "O argumento é válido porque premissas e conclusão possuem conectivos de mesma ordem."),
            ("D", "O argumento é INVÁLIDO, pois é possível que o vigilante compareça por outro motivo sem o alarme tocar."),
            ("E", "O argumento é uma tautologia que independe da atribuição de valores lógicos às premissas.")
        ],
        "expl": "O argumento comete a falácia formal da afirmação do consequente (a -> v; v; logo, a). Atribuindo falsidade à conclusão ('alarme tocou' = F) e verdade à premissa 2 ('vigilante compareceu' = V), a premissa 1 (F -> V) resulta verdadeira. Como foi possível ter premissas verdadeiras e conclusão falsa sem contradição, o argumento é inválido."
    },
    {
        "seg": "a04/s05",
        "ans": "B",
        "stem": "Para verificar a validade de um argumento dedutivo contendo três proposições simples pelo método da tabela-verdade, o analista constrói as colunas das premissas e da conclusão. Com base nessa técnica, assinale a condição necessária para o argumento ser considerado VÁLIDO:",
        "opts": [
            ("A", "A conclusão for verdadeira em pelo menos uma linha em que todas as premissas são falsas."),
            ("B", "Em todas as linhas da tabela em que todas as premissas forem verdadeiras, a conclusão for igualmente verdadeira."),
            ("C", "A conclusão apresentar valor verdadeiro na maioria absoluta das oito linhas da tabela."),
            ("D", "Existir pelo menos uma linha na qual as premissas sejam verdadeiras e a conclusão seja falsa."),
            ("E", "A conjunção de todas as premissas resultar em uma contradição lógica absoluta.")
        ],
        "expl": "Pelo método da tabela-verdade, examinam-se exclusivamente as linhas críticas (aquelas em que todas as premissas são simultaneamente verdadeiras). Para o argumento ser dedutivamente válido, a conclusão deve ser obrigatoriamente verdadeira em todas essas linhas críticas. Se em alguma linha crítica a conclusão for falsa, o argumento é inválido."
    },
    {
        "seg": "a04/s05",
        "ans": "A",
        "stem": "Considere o argumento dedutivo: Premissa 1: 'Se chove, a pista fica molhada'. Premissa 2: 'A pista não está molhada'. Conclusão: 'Logo, não choveu'. Aplicando o método da conclusão falsa para testar sua validade, assinale a opção correta.",
        "opts": [
            ("A", "O argumento é VÁLIDO, pois supor a conclusão falsa gera contradição lógica insuperável na primeira premissa."),
            ("B", "O argumento é inválido, pois é possível que a pista permaneça seca durante uma chuva torrencial."),
            ("C", "O argumento é inválido por cometer a falácia da negação do antecedente em silogismo."),
            ("D", "O argumento é contingente e necessita de verificação meteorológica empírica para ser validado."),
            ("E", "O argumento é inválido porque a conclusão expressa uma proposição negativa simples.")
        ],
        "expl": "Para testar por conclusão falsa: supõe-se que a conclusão 'não choveu' é F, logo 'choveu' é V. Para a premissa 2 ('pista não molhada') ser V, 'pista molhada' deve ser F. Substituindo na premissa 1 ('se chove, pista molhada'), temos V -> F, que resulta F, contrariando a premissa de que ela deveria ser verdadeira. Essa contradição prova que o argumento é válido (Modus Tollens)."
    },

    # --- a04/s06 (q67 a q71) ---
    {
        "seg": "a04/s06",
        "ans": "C",
        "stem": "A regra de inferência válida do Silogismo Hipotético fundamenta-se na transitividade da implicação lógica condicional. Assinale a opção que expressa a formulação canônica dessa regra dedutiva.",
        "opts": [
            ("A", "Se p -> q e p, então q."),
            ("B", "Se p -> q e ~q, então ~p."),
            ("C", "Se p -> q e q -> r, então p -> r."),
            ("D", "Se p ou q e ~p, então q."),
            ("E", "Se p -> q e r -> s, então (p e r) -> (q e s).")
        ],
        "expl": "O Silogismo Hipotético representa a transitividade do conectivo condicional: se a premissa p implica a premissa q (p -> q) e a premissa q implica a premissa r (q -> r), então decorre com validade dedutiva necessária que a premissa p implica diretamente a premissa r (p -> r)."
    },
    {
        "seg": "a04/s06",
        "ans": "B",
        "stem": "Considere as premissas verdadeiras: (1) 'Se o agente conclui o relatório, o mandado é requerido'; (2) 'Se o mandado é requerido, o juiz defere a ordem'; (3) 'O juiz não deferiu a ordem'. Utilizando as regras de inferência dedutiva, assinale a opção que apresenta a conclusão válida.",
        "opts": [
            ("A", "O agente concluiu o relatório e o mandado foi requerido pela autoridade."),
            ("B", "O agente não concluiu o relatório e o mandado não foi requerido."),
            ("C", "O mandado foi requerido pelo Ministério Público com parecer favorável."),
            ("D", "O juiz deferiu a ordem judicial com restrições de horário noturno."),
            ("E", "Não é possível deduzir se o agente concluiu ou não o relatório técnico.")
        ],
        "expl": "Pela transitividade (Silogismo Hipotético) entre as premissas 1 e 2, tem-se: 'Se o agente conclui o relatório, o juiz defere a ordem' (c -> j). Como a premissa 3 afirma que o juiz não deferiu (~j), aplica-se Modus Tollens para concluir que o agente não concluiu o relatório (~c). Aplicando Modus Tollens na premissa 2 com ~j, conclui-se que o mandado não foi requerido (~m)."
    },
    {
        "seg": "a04/s06",
        "ans": "D",
        "stem": "A regra do Silogismo Disjuntivo é empregada com frequência na resolução de problemas de lógica de argumentação. Assinale a opção que descreve a aplicação válida dessa regra de inferência.",
        "opts": [
            ("A", "A partir das premissas 'p e q' e 'p', conclui-se validamente 'q'."),
            ("B", "A partir das premissas 'p -> q' e '~p', conclui-se validamente '~q'."),
            ("C", "A partir das premissas 'p ou q' e 'p', conclui-se validamente 'q'."),
            ("D", "A partir das premissas 'p ou q' e '~p', conclui-se validamente 'q'."),
            ("E", "A partir das premissas 'p <-> q' e 'p', conclui-se validamente '~q'.")
        ],
        "expl": "O Silogismo Disjuntivo estabelece que, se uma disjunção inclusiva p ou q é verdadeira e uma das alternativas é negada como falsa (~p), a outra alternativa restante (q) deve ser obrigatoriamente verdadeira para manter a proposição disjuntiva satisfeita."
    },
    {
        "seg": "a04/s06",
        "ans": "A",
        "stem": "Considere o argumento: 'A arma apreendida era de fogo ou era simulacro de arma de fogo. Peritos constataram que a arma apreendida não era de fogo. Logo, a arma apreendida era simulacro de arma de fogo'. A respeito desse argumento dedutivo, assinale a opção correta.",
        "opts": [
            ("A", "O argumento é dedutivamente VÁLIDO por aplicação direta da regra do Silogismo Disjuntivo."),
            ("B", "O argumento é inválido porque a disjunção apresentada não possui caráter exclusivo."),
            ("C", "O argumento é dedutivamente inválido por cometer a falácia da afirmação do consequente."),
            ("D", "O argumento é uma indução estatística que carece de laudo pericial complementar."),
            ("E", "O argumento é inválido por violar a regra de distribuição dos termos silogísticos.")
        ],
        "expl": "O argumento possui a estrutura formal canônica do Silogismo Disjuntivo: p ou q; ~p; logo, q. Sendo verdadeira a disjunção e confirmada a negação de uma das alternativas pela perícia (~p), a conclusão de que a outra alternativa é verdadeira (q) decorre com estrita necessidade lógica e matemática."
    },
    {
        "seg": "a04/s06",
        "ans": "A",
        "stem": "Entre as regras clássicas de inferência da lógica proposicional, o Modus Ponens ocupa posição de destaque na derivação de sentenças. Assinale a opção que expressa a estrutura correta dessa regra.",
        "opts": [
            ("A", "Se p -> q e p, então q."),
            ("B", "Se p -> q e q, então p."),
            ("C", "Se p -> q e ~p, então ~q."),
            ("D", "Se p -> q e ~q, então p."),
            ("E", "Se p ou q e p, então ~q.")
        ],
        "expl": "O Modus Ponens (modo de afirmar pelo antecedente) estabelece que, dada a condicional verdadeira p -> q e a afirmação do seu antecedente p, conclui-se de forma válida e necessária o consequente q. Estruturas que invertem a ordem incorrem na falácia da afirmação do consequente ou na falácia da negação do antecedente."
    },

    # --- a05/s03 (q72 a q76) ---
    {
        "seg": "a05/s03",
        "ans": "B",
        "stem": "No estudo do raciocínio crítico segundo a taxonomia de Charles Sanders Peirce, as inferências classificam-se em dedução, indução e abdução. A respeito da abdução, assinale a opção correta.",
        "opts": [
            ("A", "A abdução garante necessariamente a verdade da conclusão a partir de regras universais consolidadas."),
            ("B", "A abdução parte de vestígios ou fatos surpreendentes para inferir a hipótese explicativa mais plausível."),
            ("C", "A abdução opera por enumeração exaustiva de todos os casos particulares observados em laboratório."),
            ("D", "A abdução é um argumento puramente dedutivo que dispensa confirmação empírica posterior."),
            ("E", "A abdução é classificada como uma falácia formal dedutiva pela lógica proposicional clássica.")
        ],
        "expl": "Segundo Peirce, a abdução é a inferência que formula uma hipótese explicativa diante de um fato observado surpreendente ou vestígio enigmático ('inferência para a melhor explicação'). Diferentemente da dedução (analítica e necessária) e da indução (generalizadora de hábitos), a abdução introduz ideias explicativas plausíveis."
    },
    {
        "seg": "a05/s03",
        "ans": "A",
        "stem": "Considere o seguinte raciocínio: 'Regra: Todos os feijões deste saco são brancos. Premissa fática: Estes feijões foram retirados deste saco. Conclusão: Logo, estes feijões são brancos'. Conforme a classificação de Peirce, assinale a opção que categoriza esse raciocínio:",
        "opts": [
            ("A", "Dedução."),
            ("B", "Indução."),
            ("C", "Abdução."),
            ("D", "Analogia."),
            ("E", "Falácia do espantalho.")
        ],
        "expl": "No exemplo clássico dos feijões de Charles S. Peirce, a dedução parte da regra geral combinada com o caso específico para derivar com necessidade matemática o resultado: Regra + Caso => Resultado. Toda a informação da conclusão já estava implícita na regra geral e no caso fático."
    },
    {
        "seg": "a05/s03",
        "ans": "D",
        "stem": "Considere o raciocínio: 'Premissa fática: Estes feijões foram retirados deste saco. Resultado observado: Estes feijões são brancos. Conclusão: Logo, todos os feijões deste saco são brancos'. Segundo a conceituação de Peirce, assinale a modalidade que classifica esse raciocínio:",
        "opts": [
            ("A", "Dedução analítica necessária."),
            ("B", "Silogismo disjuntivo categórico."),
            ("C", "Abdução explicativa de indícios."),
            ("D", "Indução generalizadora a partir da observação de casos particulares."),
            ("E", "Falácia formal de negação do antecedente.")
        ],
        "expl": "Conforme a sistematização de Peirce, a indução parte do caso particular associado ao resultado observado na amostra para inferir e postular uma regra geral para toda a população: Caso + Resultado => Regra. A conclusão tem natureza provável e ampliativa."
    },
    {
        "seg": "a05/s03",
        "ans": "A",
        "stem": "Considere o raciocínio: 'Regra conhecida: Todos os feijões deste saco são brancos. Fato surpreendente observado: Estes feijões sobre a mesa são brancos. Conclusão: Logo, é plausível supor que estes feijões tenham vindo deste saco'. Sob a ótica de Peirce, assinale o tipo de inferência exemplificado:",
        "opts": [
            ("A", "Abdução (formulação de uma hipótese explicativa para o fato observado)."),
            ("B", "Dedução analítica de premissas universais necessárias."),
            ("C", "Indução estatística pura de amostragem representativa."),
            ("D", "Falácia formal de afirmação do antecedente de primeira ordem."),
            ("E", "Tautologia lógica decorrente do princípio da não contradição.")
        ],
        "expl": "Na tríade de Peirce, a abdução opera associando a regra conhecida a um resultado empírico surpreendente para propor a hipótese que melhor elucida a origem do fato: Regra + Resultado => Caso hipotético. É a inferência típica da investigação e do diagnóstico."
    },
    {
        "seg": "a05/s03",
        "ans": "C",
        "stem": "Considere o argumento: 'Se o indivíduo é o autor do roubo, então possui o objeto furtado em sua posse. O indivíduo possui o objeto furtado em sua posse. Logo, ele é o autor do roubo'. No âmbito da lógica de argumentação e raciocínio crítico, assinale a opção correta.",
        "opts": [
            ("A", "O argumento é dedutivamente válido por aplicação da regra do Modus Ponens."),
            ("B", "O argumento é dedutivamente válido por aplicação da regra do Modus Tollens."),
            ("C", "O argumento é dedutivamente INVÁLIDO, configurando a falácia formal da afirmação do consequente."),
            ("D", "O argumento é dedutivamente INVÁLIDO, configurando a falácia formal da negação do antecedente."),
            ("E", "O argumento é uma indução estatística com nível de significância de cinco por cento.")
        ],
        "expl": "A estrutura do argumento é: p -> q; q; logo, p. Trata-se da clássica falácia formal da afirmação do consequente. O fato de o indivíduo estar na posse da coisa (consequente) não implica com necessidade dedutiva que ele tenha sido o autor direto do roubo (ele pode ter receptado a coisa de terceiros ou achado o bem). O argumento é dedutivamente inválido."
    }
]
