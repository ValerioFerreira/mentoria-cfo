"""Lote 3: Aula 02 (a02/s02, a02/s05, a02/s06, a02/s08, a02/s09) - 30 questoes (q36 a q65)"""

QUESTOES = [
    # --- a02/s02 (q36 a q41) ---
    {
        "seg": "a02/s02",
        "ans": "B",
        "stem": "Considere a proposição condicional: 'Se o perito conclui o laudo técnico, então o delegado indicia o investigado'. Assinale a opção que apresenta uma proposição logicamente equivalente a essa condicional sob a forma de disjunção inclusiva.",
        "opts": [
            ("A", "O perito conclui o laudo técnico ou o delegado indicia o investigado."),
            ("B", "O perito não conclui o laudo técnico ou o delegado indicia o investigado."),
            ("C", "O perito não conclui o laudo técnico e o delegado indicia o investigado."),
            ("D", "O delegado indicia o investigado ou o perito conclui o laudo técnico."),
            ("E", "Se o perito não conclui o laudo técnico, então o delegado indicia o investigado.")
        ],
        "expl": "A alternativa B está correta. A transformação clássica da condicional em disjunção inclusiva obedece à regra de equivalência p -> q <=> ~p ou q (nega-se o antecedente, troca-se o condicional por disjunção e mantém-se o consequente). Portanto, 'Se o perito conclui o laudo, então o delegado indicia o investigado' equivale logicamente a 'O perito não conclui o laudo técnico ou o delegado indicia o investigado'."
    },
    {
        "seg": "a02/s02",
        "ans": "C",
        "stem": "Considere a condicional: 'Se o alarme de segurança dispara, então a viatura policial se desloca até o local'. Assinale a opção que expressa a proposição logicamente equivalente obtida por contraposição (contrapositiva).",
        "opts": [
            ("A", "Se a viatura policial se desloca até o local, então o alarme de segurança dispara."),
            ("B", "Se o alarme de segurança não dispara, então a viatura policial não se desloca até o local."),
            ("C", "Se a viatura policial não se desloca até o local, então o alarme de segurança não dispara."),
            ("D", "O alarme de segurança não dispara ou a viatura policial não se desloca até o local."),
            ("E", "A viatura policial se desloca até o local se e somente se o alarme de segurança dispara.")
        ],
        "expl": "A alternativa C está correta. A contrapositiva de uma proposição condicional p -> q é dada pela fórmula ~q -> ~p (inverte-se a ordem das proposições e negam-se ambas). Assim, a equivalente contrapositiva de 'Se o alarme dispara, então a viatura se desloca' é 'Se a viatura policial não se desloca até o local, então o alarme de segurança não dispara'. A opção A é a recíproca, B é a inversa e D e E trazem outros conectivos."
    },
    {
        "seg": "a02/s02",
        "ans": "D",
        "stem": "A proposição disjuntiva 'O agente realiza a ronda noturna ou atende ao chamado na delegacia' pode ser convertida em uma proposição condicional equivalente. Com base nas regras de equivalência lógica, assinale a opção que apresenta essa conversão correta.",
        "opts": [
            ("A", "Se o agente realiza a ronda noturna, então atende ao chamado na delegacia."),
            ("B", "Se o agente atende ao chamado na delegacia, então realiza a ronda noturna."),
            ("C", "O agente realiza a ronda noturna se e somente se atende ao chamado na delegacia."),
            ("D", "Se o agente não realiza a ronda noturna, então atende ao chamado na delegacia."),
            ("E", "Se o agente não atende ao chamado na delegacia, então não realiza a ronda noturna.")
        ],
        "expl": "A alternativa D está correta. A equivalência entre a disjunção inclusiva e a condicional é dada por p ou q <=> ~p -> q. Aplicando essa regra à frase 'O agente realiza a ronda (p) ou atende ao chamado (q)', nega-se a primeira parcela (~p) e mantém-se a segunda (q) sob a condicional: 'Se o agente não realiza a ronda noturna, então atende ao chamado na delegacia'."
    },
    {
        "seg": "a02/s02",
        "ans": "E",
        "stem": "No cálculo proposicional clássico, uma proposição condicional da forma p -> q admite duas estruturas equivalentes fundamentais. A esse respeito, assinale a opção correta.",
        "opts": [
            ("A", "A condicional p -> q equivale à conjunção p e q e à disjunção exclusiva p ou exclusivo q."),
            ("B", "A condicional p -> q equivale unicamente à sua recíproca q -> p em qualquer situação."),
            ("C", "A condicional p -> q pode ser transformada em conjunção adversativa por meio da regra ~p e ~q."),
            ("D", "A condicional p -> q equivale à bicondicional p <-> q sempre que q for uma proposição simples."),
            ("E", "A condicional p -> q tem como equivalentes lógicas apenas a sua contrapositiva (~q -> ~p) e a disjunção (~p ou q).")
        ],
        "expl": "A alternativa E está correta. As duas únicas equivalências lógicas diretas e universais de uma proposição condicional p -> q são: (1) a contrapositiva, expressa por outra condicional (~q -> ~p); e (2) a disjunção inclusiva (~p ou q). Nenhuma conjunção ou disjunção exclusiva possui a mesma tabela-verdade de uma condicional clássica."
    },
    {
        "seg": "a02/s02",
        "ans": "A",
        "stem": "A negação de uma proposição condicional p -> q possui estrutura lógica específica que a difere da negação de outros conectivos. Acerca da negação de p -> q, assinale a opção correta.",
        "opts": [
            ("A", "A negação de p -> q é a conjunção p e ~q, obtida mantendo-se o antecedente e negando-se o consequente."),
            ("B", "A negação de p -> q é a condicional ~p -> ~q, obtida negando-se simultaneamente ambos os termos."),
            ("C", "A negação de p -> q é a disjunção ~p ou ~q, decorrente da aplicação direta das leis de De Morgan."),
            ("D", "A negação de p -> q é a bicondicional ~p <-> ~q, pois a negação preserva a implicação mútua."),
            ("E", "A negação de p -> q resulta invariavelmente em uma proposição condicional com os termos invertidos.")
        ],
        "expl": "A alternativa A está correta. Como p -> q equivale a ~p ou q, ao negar ~(p -> q) aplica-se De Morgan sobre ~(~p ou q), obtendo-se ~(~p) e ~q, ou seja, p e ~q. Na linguagem prática, preserva-se o antecedente (p) e nega-se o consequente (~q), unindo-os pelo conectivo 'e' (conjunção)."
    },
    {
        "seg": "a02/s02",
        "ans": "B",
        "stem": "Em um termo de depoimento, consta a seguinte afirmação: 'Se a testemunha comparecer à audiência, o réu será interrogado'. Assinale a opção que expressa corretamente a NEGAÇÃO lógica dessa afirmação.",
        "opts": [
            ("A", "Se a testemunha não comparecer à audiência, o réu não será interrogado."),
            ("B", "A testemunha comparece à audiência e o réu não é interrogado."),
            ("C", "A testemunha não comparece à audiência ou o réu não é interrogado."),
            ("D", "A testemunha não comparece à audiência e o réu é interrogado."),
            ("E", "Se o réu não for interrogado, a testemunha não comparece à audiência.")
        ],
        "expl": "A alternativa B está correta. Para negar a condicional p -> q, mantém-se a primeira proposição (p: 'A testemunha comparece à audiência') e nega-se a segunda (~q: 'o réu não é interrogado'), conectando-as por conjunção (e). A opção A traz a inversa, C traz De Morgan indevido, D inverte a negação e E é a contrapositiva."
    },

    # --- a02/s05 (q42 a q47) ---
    {
        "seg": "a02/s05",
        "ans": "C",
        "stem": "Na álgebra de proposições, a negação lógica da proposição bicondicional p <-> q pode ser expressa de diversas maneiras equivalentes. Assinale a opção que indica a negação da bicondicional sob a forma de disjunção exclusiva.",
        "opts": [
            ("A", "p ou q"),
            ("B", "p e ~q"),
            ("C", "Ou p, ou q"),
            ("D", "~p <-> ~q"),
            ("E", "(p -> q) e (q -> p)")
        ],
        "expl": "A alternativa C está correta. A bicondicional p <-> q é verdadeira quando p e q possuem valores lógicos iguais (ambas V ou ambas F). Sua negação lógica, portanto, deve ser verdadeira quando p e q possuírem valores lógicos distintos (uma V e outra F). Essa é exatamente a definição da disjunção exclusiva (p ou exclusivo q, ou 'Ou p, ou q'). Logo, ~(p <-> q) <=> p ou exclusivo q."
    },
    {
        "seg": "a02/s05",
        "ans": "D",
        "stem": "Além da disjunção exclusiva, a negação de uma bicondicional p <-> q pode ser obtida mantendo-se o conectivo bicondicional e negando-se termos. A esse respeito, assinale a opção correta.",
        "opts": [
            ("A", "A negação de p <-> q é obtida negando-se simultaneamente os dois termos: ~p <-> ~q."),
            ("B", "A negação de p <-> q exige a troca do conectivo por uma conjunção simples de termos afirmativos."),
            ("C", "A negação de p <-> q resulta em uma condicional simples cuja antecedente é sempre verdadeira."),
            ("D", "A negação de p <-> q pode ser formulada negando-se apenas um dos termos: ~p <-> q ou p <-> ~q."),
            ("E", "A negação de p <-> q é logicamente impossível na ausência de quantificadores existenciais.")
        ],
        "expl": "A alternativa D está correta. Para inverter os valores de uma tabela-verdade da bicondicional preservando o conectivo bicondicional, basta inverter o valor lógico de apenas uma das proposições componentes: ~(p <-> q) <=> (~p <-> q) <=> (p <-> ~q). Negar ambos os termos simultaneamente (~p <-> ~q) resulta em uma proposição equivalente à original p <-> q (erro clássico da opção A)."
    },
    {
        "seg": "a02/s05",
        "ans": "E",
        "stem": "A proposição bicondicional p <-> q equivale a (p -> q) e (q -> p). Ao aplicar as leis de De Morgan e as negações de condicionais para negar essa estrutura, assinale a opção que expressa a negação da bicondicional formulada unicamente com os conectivos 'e', 'ou' e 'não'.",
        "opts": [
            ("A", "(p ou q) e (~p ou ~q)"),
            ("B", "(p e q) ou (~p e ~q)"),
            ("C", "(~p e q) e (p e ~q)"),
            ("D", "(p ou ~q) e (q ou ~p)"),
            ("E", "(p e ~q) ou (q e ~p)")
        ],
        "expl": "A alternativa E está correta. Sendo p <-> q <=> (p -> q) e (q -> p), ao negar ~(p <-> q) aplica-se De Morgan: ~(p -> q) ou ~(q -> p). Negando cada uma das condicionais, obtém-se (p e ~q) ou (q e ~p). Essa fórmula expressa a negação da bicondicional usando exclusivamente conjunção, disjunção e negação."
    },
    {
        "seg": "a02/s05",
        "ans": "A",
        "stem": "A propriedade comutativa estabelece que a troca da ordem dos operandos não altera o valor lógico da proposição composta. Considerando os conectivos lógicos usuais, assinale a opção que apresenta um conectivo para o qual a propriedade comutativa NÃO é válida.",
        "opts": [
            ("A", "Condicional (->)"),
            ("B", "Conjunção (e)"),
            ("C", "Disjunção inclusiva (ou)"),
            ("D", "Disjunção exclusiva (ou... ou)"),
            ("E", "Bicondicional (<->)")
        ],
        "expl": "A alternativa A está correta. A condicional não é comutativa: p -> q não é logicamente equivalente a q -> p (sua recíproca). Por exemplo, com p = V e q = F, p -> q é F, mas q -> p (F -> V) é V. Os demais conectivos (conjunção, disjunção inclusiva, disjunção exclusiva e bicondicional) são todos comutativos: a ordem de seus termos é intercambiável sem alteração do valor de verdade."
    },
    {
        "seg": "a02/s05",
        "ans": "B",
        "stem": "A propriedade associativa permite reagrupar proposições compostas unidas pelo mesmo conectivo sem necessidade de parênteses delimitadores. Acerca dessa propriedade na lógica formal, assinale a opção correta.",
        "opts": [
            ("A", "A propriedade associativa permite associar livremente uma conjunção a uma condicional sem alterar o valor final."),
            ("B", "A propriedade associativa é válida para a conjunção e para a disjunção: (p e q) e r <=> p e (q e r), bem como (p ou q) ou r <=> p ou (q ou r)."),
            ("C", "A propriedade associativa autoriza a permuta de conectivos distintos sem alteração da tabela-verdade."),
            ("D", "A propriedade associativa aplica-se irrestritamente à operação condicional: (p -> q) -> r <=> p -> (q -> r)."),
            ("E", "A propriedade associativa só pode ser empregada em fórmulas que resultem comprovadamente em contradições.")
        ],
        "expl": "A alternativa B está correta. A associatividade é válida para operadores de mesma precedência e natureza idêntica, como a conjunção e a disjunção: (p e q) e r <=> p e (q e r) e (p ou q) ou r <=> p ou (q ou r). A condicional (D) não é associativa: (p -> q) -> r não equivale a p -> (q -> r)."
    },
    {
        "seg": "a02/s05",
        "ans": "C",
        "stem": "Um candidato a concurso público deparou-se com a seguinte proposição bicondicional: 'O réu é absolvido se e somente se as provas forem declaradas nulas'. Ele propôs como sua negação a frase: 'O réu não é absolvido se e somente se as provas não forem declaradas nulas'. Do ponto de vista estritamente lógico, assinale a opção correta.",
        "opts": [
            ("A", "A proposta do candidato é uma negação válida, pois negou os dois lados da bicondicional."),
            ("B", "A proposta do candidato resultou em uma contradição lógica insustentável."),
            ("C", "A proposta do candidato está incorreta, pois negar ambos os termos gera uma proposição equivalente à original (~p <-> ~q <=> p <-> q), e não a sua negação."),
            ("D", "A proposta do candidato transformou a bicondicional em uma sentença aberta por duplicidade de negações."),
            ("E", "A proposta do candidato é equivalente a uma disjunção exclusiva entre as proposições originais.")
        ],
        "expl": "A alternativa C está correta. A expressão ~p <-> ~q tem a mesma tabela-verdade de p <-> q (quando p e q são V, ~p e ~q são F, logo F <-> F = V; quando p e q são F, ~p e ~q são V, logo V <-> V = V; e quando diferem, continuam diferindo). Portanto, negar ambos os termos produz uma equivalência lógica, e não a negação da bicondicional."
    },

    # --- a02/s06 (q48 a q53) ---
    {
        "seg": "a02/s06",
        "ans": "D",
        "stem": "Na álgebra proposicional, a propriedade distributiva da conjunção em relação à disjunção inclusiva expressa uma importante equivalência estrutural. Assinale a opção que apresenta a correta aplicação dessa propriedade sobre a fórmula: p e (q ou r).",
        "opts": [
            ("A", "(p ou q) e (p ou r)"),
            ("B", "(p e q) e (p e r)"),
            ("C", "(p ou q) ou (p ou r)"),
            ("D", "(p e q) ou (p e r)"),
            ("E", "p e (q e r)")
        ],
        "expl": "A alternativa D está correta. A propriedade distributiva da conjunção sobre a disjunção funciona de modo análogo à multiplicação sobre a adição na aritmética: p e (q ou r) distribui o conectivo de conjunção para cada termo dentro dos parênteses, unindo os blocos resultantes pela disjunção, o que resulta na fórmula (p e q) ou (p e r)."
    },
    {
        "seg": "a02/s06",
        "ans": "E",
        "stem": "Diferentemente da aritmética comum, na lógica proposicional a disjunção inclusiva também é distributiva em relação à conjunção. Assinale a opção que expressa a equivalência distributiva da fórmula: p ou (q e r).",
        "opts": [
            ("A", "(p e q) ou (p e r)"),
            ("B", "(p ou q) ou (p ou r)"),
            ("C", "(p e q) e (p e r)"),
            ("D", "p ou (q ou r)"),
            ("E", "(p ou q) e (p ou r)")
        ],
        "expl": "A alternativa E está correta. A distributiva do 'ou' sobre o 'e' é uma propriedade essencial da álgebra booleana: p ou (q e r) distribui o 'p ou' para cada um dos termos da conjunção interna, unindo-os por meio de uma conjunção: (p ou q) e (p ou r)."
    },
    {
        "seg": "a02/s06",
        "ans": "A",
        "stem": "Ao simplificar fórmulas lógicas, é frequente aplicar a propriedade distributiva em sentido inverso, técnica conhecida como 'colocar em evidência'. Assinale a opção que expressa a fatoração correta da fórmula: (p e q) ou (p e r).",
        "opts": [
            ("A", "p e (q ou r)"),
            ("B", "p ou (q e r)"),
            ("C", "(p ou q) e r"),
            ("D", "(p e r) ou q"),
            ("E", "p <-> (q e r)")
        ],
        "expl": "A alternativa A está correta. Na expressão (p e q) ou (p e r), o termo 'p e' é comum a ambos os blocos disjuntivos. Ao colocá-lo em evidência, extrai-se 'p e', restando dentro dos parênteses os termos q e r unidos pelo conectivo central da disjunção, resultando exatamente em p e (q ou r)."
    },
    {
        "seg": "a02/s06",
        "ans": "B",
        "stem": "A propriedade da absorção é muito útil para a redução e simplificação de expressões proposicionais. Considerando essa propriedade na álgebra lógica, assinale a opção correta.",
        "opts": [
            ("A", "A expressão p e (p ou q) simplifica-se para p e q."),
            ("B", "A expressão p e (p ou q) equivale simplesmente à proposição p."),
            ("C", "A expressão p ou (p e q) simplifica-se para a disjunção p ou q."),
            ("D", "A propriedade da absorção transforma qualquer conjunção em uma contradição."),
            ("E", "A absorção exige que as variáveis p e q possuam quantificadores universais.")
        ],
        "expl": "A alternativa B está correta. Pela lei da absorção da álgebra proposicional, temos duas formas fundamentais: p e (p ou q) <=> p, e p ou (p e q) <=> p. De fato, se p é V, (V ou q) é V, e V e V = V; se p é F, F e (algo) é F. O resultado coincide rigorosamente com o valor de p, absorvendo a variável q."
    },
    {
        "seg": "a02/s06",
        "ans": "C",
        "stem": "A propriedade da idempotência estabelece o comportamento de proposições idênticas operadas entre si por conectivos lógicos. A esse respeito, assinale a opção correta.",
        "opts": [
            ("A", "A conjunção de uma proposição consigo mesma, p e p, resulta sempre em uma tautologia independente de p."),
            ("B", "A disjunção inclusiva p ou p resulta em uma contradição lógica."),
            ("C", "Pela idempotência, as expressões p e p bem como p ou p equivalem ambas à própria proposição p."),
            ("D", "A idempotência só é válida quando aplicada sobre proposições compostas por três ou mais variáveis."),
            ("E", "A operação p -> p é um exemplo de idempotência que se reduz a p.")
        ],
        "expl": "A alternativa C está correta. A lei da idempotência estabelece que a repetição de uma mesma proposição ligada a si mesma por conjunção ou disjunção não altera seu valor lógico: p e p <=> p e p ou p <=> p. A opção A erra pois se p for F, p e p é F; a opção B erra pois p ou p tem o valor de p; e a opção E erra pois p -> p é tautologia (V), e não p."
    },
    {
        "seg": "a02/s06",
        "ans": "D",
        "stem": "Na álgebra de proposições, certas constantes lógicas (V para tautologia/verdade e F para contradição/falsidade) atuam como elementos neutros ou dominantes nas propriedades de identidade. A respeito dessas propriedades, assinale a opção correta.",
        "opts": [
            ("A", "A conjunção de qualquer proposição p com a verdade, p e V, resulta invariavelmente em V."),
            ("B", "A disjunção de qualquer proposição p com a falsidade, p ou F, resulta sempre em F."),
            ("C", "A conjunção de qualquer proposição p com a falsidade, p e F, resulta na própria proposição p."),
            ("D", "A disjunção de qualquer proposição p com a verdade, p ou V, assume sempre o valor lógico V."),
            ("E", "A disjunção de qualquer proposição p com a falsidade, p ou F, assume sempre o valor lógico V.")
        ],
        "expl": "A alternativa D está correta. Na disjunção inclusiva, a presença de uma parcela verdadeira é suficiente para tornar a expressão inteira verdadeira, logo p ou V <=> V (a verdade é elemento absorvente ou dominante da disjunção). Já p e V <=> p (V é elemento neutro da conjunção); p ou F <=> p (F é elemento neutro da disjunção); e p e F <=> F (F é elemento absorvente da conjunção)."
    },

    # --- a02/s08 (q54 a q59) ---
    {
        "seg": "a02/s08",
        "ans": "E",
        "stem": "Considere a condicional: 'Se o suspeito for flagrado no local, então será preso em flagrante ou prestará esclarecimentos imediatos'. Assinale a opção que expressa a NEGAÇÃO lógica dessa proposição composta.",
        "opts": [
            ("A", "Se o suspeito não for flagrado no local, então não será preso nem prestará esclarecimentos."),
            ("B", "O suspeito não é flagrado no local ou é preso em flagrante e presta esclarecimentos."),
            ("C", "O suspeito é flagrado no local, mas é preso em flagrante ou presta esclarecimentos."),
            ("D", "O suspeito não é flagrado no local e não é preso em flagrante nem presta esclarecimentos."),
            ("E", "O suspeito é flagrado no local, não é preso em flagrante e não presta esclarecimentos imediatos.")
        ],
        "expl": "A alternativa E está correta. A condicional tem a forma p -> (q ou r). Sua negação lógica mantém o antecedente (p) e nega o consequente ~(q ou r), unindo-os por conjunção: p e ~(q ou r). Aplicando as leis de De Morgan em ~(q ou r), obtém-se ~q e ~r. Assim, a fórmula final da negação é p e ~q e ~r: 'O suspeito é flagrado no local, não é preso em flagrante e não presta esclarecimentos imediatos'."
    },
    {
        "seg": "a02/s08",
        "ans": "A",
        "stem": "Considere a proposição condicional P: 'Se o mandado for cumprido, então o acusado será conduzido à delegacia e os bens serão apreendidos'. Assinale a opção que expressa a correta NEGAÇÃO lógica de P.",
        "opts": [
            ("A", "O mandado é cumprido, e o acusado não é conduzido à delegacia ou os bens não são apreendidos."),
            ("B", "Se o mandado não for cumprido, então o acusado não é conduzido nem os bens são apreendidos."),
            ("C", "O mandado não é cumprido, o acusado não é conduzido e os bens não são apreendidos."),
            ("D", "O mandado é cumprido se e somente se o acusado não for conduzido à delegacia."),
            ("E", "O mandado não é cumprido ou o acusado é conduzido à delegacia e os bens são apreendidos.")
        ],
        "expl": "A alternativa A está correta. A proposição é p -> (q e r). Para negá-la, mantém-se o antecedente p e nega-se o consequente ~(q e r) sob conjunção: p e ~(q e r). Pela lei de De Morgan, ~(q e r) <=> ~q ou ~r. A estrutura completa da negação resulta em p e (~q ou ~r): 'O mandado é cumprido, e o acusado não é conduzido à delegacia ou os bens não são apreendidos'."
    },
    {
        "seg": "a02/s08",
        "ans": "B",
        "stem": "Considere a seguinte condicional com antecedente composto: 'Se o agente portar identificação ou estiver uniformizado, terá acesso ao recinto reservado'. Assinale a opção que expressa uma proposição logicamente equivalente obtida pela contrapositiva.",
        "opts": [
            ("A", "Se o agente não portar identificação ou não estiver uniformizado, não terá acesso ao recinto."),
            ("B", "Se o agente não tiver acesso ao recinto reservado, então não porta identificação e não está uniformizado."),
            ("C", "Se o agente tiver acesso ao recinto reservado, então porta identificação ou está uniformizado."),
            ("D", "O agente tem acesso ao recinto reservado se e somente se estiver uniformizado."),
            ("E", "Se o agente não tiver acesso ao recinto reservado, então não porta identificação ou não está uniformizado.")
        ],
        "expl": "A alternativa B está correta. A condicional é (p ou q) -> r. Sua contrapositiva é ~r -> ~(p ou q). Aplicando a lei de De Morgan na negação do antecedente original, temos ~(p ou q) <=> ~p e ~q. Assim, a proposição contrapositiva completa é ~r -> (~p e ~q): 'Se o agente não tiver acesso ao recinto reservado, então não porta identificação e não está uniformizado'."
    },
    {
        "seg": "a02/s08",
        "ans": "C",
        "stem": "Deseja-se encontrar uma proposição equivalente à condicional '~p -> q' utilizando o conectivo de disjunção inclusiva. Aplicando a regra de transformação de condicional em disjunção, assinale a opção correta.",
        "opts": [
            ("A", "~p ou q"),
            ("B", "~p ou ~q"),
            ("C", "p ou q"),
            ("D", "p e q"),
            ("E", "~q -> ~p")
        ],
        "expl": "A alternativa C está correta. A regra de equivalência da condicional em disjunção é: A -> B <=> ~A ou B. No caso de ~p -> q, o antecedente A é ~p e o consequente B é q. Negando o antecedente, temos ~(~p), que pela dupla negação resulta em p. Mantendo o consequente q, temos p ou q. Portanto, ~p -> q equivale a p ou q."
    },
    {
        "seg": "a02/s08",
        "ans": "D",
        "stem": "Considere a proposição composta: '(p e q) ou ~r'. Ao aplicar as leis de De Morgan para calcular a NEGAÇÃO lógica dessa proposição, assinale a opção correta.",
        "opts": [
            ("A", "(~p e ~q) e r"),
            ("B", "(p ou q) e ~r"),
            ("C", "(~p ou ~q) ou r"),
            ("D", "(~p ou ~q) e r"),
            ("E", "~p e (~q ou r)")
        ],
        "expl": "A alternativa D está correta. Queremos negar a disjunção ~[ (p e q) ou ~r ]. Pela lei de De Morgan, a negação de uma disjunção é a conjunção das negações: ~(p e q) e ~(~r). Negando a conjunção interna por De Morgan, temos ~(p e q) <=> ~p ou ~q. Pela dupla negação, ~(~r) <=> r. Unindo os termos por conjunção, obtém-se (~p ou ~q) e r."
    },
    {
        "seg": "a02/s08",
        "ans": "E",
        "stem": "Considere a condicional que possui termos negativos: '~p -> ~q'. Ao calcular a proposição logicamente equivalente obtida pela aplicação da contrapositiva, assinale a opção correta.",
        "opts": [
            ("A", "p -> q"),
            ("B", "~q -> ~p"),
            ("C", "p ou ~q"),
            ("D", "~p e q"),
            ("E", "q -> p")
        ],
        "expl": "A alternativa E está correta. A contrapositiva de uma condicional A -> B é dada por ~B -> ~A. Aplicando à proposição ~p -> ~q, temos que o antecedente é ~p e o consequente é ~q. Invertendo e negando ambos os termos, obtemos ~(~q) -> ~(~p). Pela lei da dupla negação, ~(~q) é q e ~(~p) é p, resultando diretamente na condicional equivalente q -> p."
    },

    # --- a02/s09 (q60 a q65) ---
    {
        "seg": "a02/s09",
        "ans": "A",
        "stem": "Considere a proposição: 'Ou o acusado confessa a autoria, ou o juiz determina a prisão preventiva'. Assinale a opção que expressa a NEGAÇÃO lógica dessa disjunção exclusiva.",
        "opts": [
            ("A", "O acusado confessa a autoria se e somente se o juiz determinar a prisão preventiva."),
            ("B", "O acusado confessa a autoria e o juiz determina a prisão preventiva."),
            ("C", "O acusado não confessa a autoria ou o juiz não determina a prisão preventiva."),
            ("D", "Se o acusado confessa a autoria, então o juiz determina a prisão preventiva."),
            ("E", "Nem o acusado confessa a autoria, nem o juiz determina a prisão preventiva.")
        ],
        "expl": "A alternativa A está correta. A negação lógica da disjunção exclusiva (p ou exclusivo q) é a proposição bicondicional p <-> q. Isso decorre do fato de que a disjunção exclusiva é verdadeira quando os valores lógicos das proposições diferem, e a bicondicional é verdadeira exatamente na situação oposta, ou seja, quando os valores lógicos são idênticos. Logo, ~(p ou exclusivo q) <=> p <-> q."
    },
    {
        "seg": "a02/s09",
        "ans": "B",
        "stem": "A negação de uma conjunção ~(p e q) equivale a ~p ou ~q pelas leis de De Morgan. Se essa disjunção for convertida em uma condicional equivalente, assinale a opção que expressa essa nova formulação.",
        "opts": [
            ("A", "~p -> q"),
            ("B", "p -> ~q"),
            ("C", "q -> p"),
            ("D", "~q -> p"),
            ("E", "p -> q")
        ],
        "expl": "A alternativa B está correta. Pela lei de De Morgan, ~(p e q) <=> ~p ou ~q. Como qualquer disjunção A ou B pode ser convertida na condicional equivalente ~A -> B, aplicando para A = ~p e B = ~q temos: ~(~p) -> ~q, que resulta em p -> ~q ('se p, então não q')."
    },
    {
        "seg": "a02/s09",
        "ans": "C",
        "stem": "Considere a proposição com quantificador universal: 'Todos os agentes de polícia civil são habilitados para dirigir viatura'. Assinale a opção que expressa corretamente a NEGAÇÃO lógica dessa proposição.",
        "opts": [
            ("A", "Nenhum agente de polícia civil é habilitado para dirigir viatura."),
            ("B", "Todos os agentes de polícia civil não são habilitados para dirigir viatura."),
            ("C", "Pelo menos um agente de polícia civil não é habilitado para dirigir viatura."),
            ("D", "Existe pelo menos um agente de polícia civil que é habilitado para dirigir viatura."),
            ("E", "Qualquer agente de polícia civil pode recusar-se a dirigir viatura.")
        ],
        "expl": "A alternativa C está correta. A negação lógica de uma proposição universal afirmativa ('Todo A é B') é a proposição existencial negativa ('Algum A não é B', 'Pelo menos um A não é B' ou 'Existe A que não é B'). A afirmativa 'Nenhum A é B' (opção A) é uma contrária e não a negação contraditória estrita de 'Todo A é B'."
    },
    {
        "seg": "a02/s09",
        "ans": "D",
        "stem": "Considere a proposição com quantificador existencial: 'Algum delegado da comarca reside na capital'. Assinale a opção que apresenta a NEGAÇÃO lógica correta dessa afirmativa.",
        "opts": [
            ("A", "Algum delegado da comarca não reside na capital."),
            ("B", "A maioria dos delegados da comarca não reside na capital."),
            ("C", "Pelo menos um delegado da comarca reside no interior do estado."),
            ("D", "Nenhum delegado da comarca reside na capital."),
            ("E", "Todos os delegados da comarca residem na capital.")
        ],
        "expl": "A alternativa D está correta. A negação lógica de uma proposição existencial afirmativa ('Existe algum A que é B' ou 'Pelo menos um A é B') é a proposição universal negativa ('Nenhum A é B' ou 'Todo A não é B'). Para negar que exista ao menos um delegado residindo na capital, deve-se afirmar categoricamente que nenhum delegado da comarca reside na capital."
    },
    {
        "seg": "a02/s09",
        "ans": "E",
        "stem": "Em uma reunião de planejamento operacional, foi proferida a frase: 'Nenhum policial faltou ao treinamento tático'. Assinale a opção que expressa a NEGAÇÃO lógica dessa sentença.",
        "opts": [
            ("A", "Todos os policiais faltaram ao treinamento tático."),
            ("B", "Nenhum policial compareceu ao treinamento tático."),
            ("C", "Todos os policiais compareceram pontualmente ao treinamento tático."),
            ("D", "Mais da metade dos policiais faltou ao treinamento tático."),
            ("E", "Pelo menos um policial faltou ao treinamento tático.")
        ],
        "expl": "A alternativa E está correta. A proposição dada é universal negativa ('Nenhum A é B'). Para quebrar a verdade de 'nenhum faltou', basta a existência de um único caso em que o fato tenha ocorrido, ou seja, 'pelo menos um policial faltou ao treinamento tático' (existencial afirmativa). Dizer que 'todos faltaram' (A) é um erro comum de generalização indevida."
    },
    {
        "seg": "a02/s09",
        "ans": "A",
        "stem": "Considere a conjunção de duas condicionais independentes: '(p -> q) e (r -> s)'. Assinale a opção que expressa uma proposição logicamente equivalente formulada pela contraposição simultânea de seus termos.",
        "opts": [
            ("A", "(~q -> ~p) e (~s -> ~r)"),
            ("B", "(~p -> ~q) e (~r -> ~s)"),
            ("C", "(q -> p) e (s -> r)"),
            ("D", "(~q -> ~p) ou (~s -> ~r)"),
            ("E", "~(p -> q) ou ~(r -> s)")
        ],
        "expl": "A alternativa A está correta. Como a conjunção conecta duas condicionais, a substituição de cada condicional por sua equivalente contrapositiva preserva rigorosamente a equivalência global da fórmula: p -> q <=> ~q -> ~p e r -> s <=> ~s -> ~r. Mantendo o conectivo de conjunção ('e'), obtém-se (~q -> ~p) e (~s -> ~r)."
    }
]
