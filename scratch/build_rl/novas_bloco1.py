"""Bloco 1 das novas questoes de Raciocinio Logico (43 questoes: q0 a q42).
Trechos: a00/s03 (4), a00/s04 (2), a00/s05 (2), a00/s07 (4), a00/s08 (4), a00/s12 (5),
         a01/s01 (5), a01/s02 (1), a01/s05 (5), a01/s06 (5), a01/s07 (4), a01/s09 (2).
Gabaritos extraidos estritamente de gabaritos_132.json.
"""

QUESTOES_BLOCO1 = [
    # --- a00/s03 (q0 a q3) ---
    {
        "seg": "a00/s03",
        "ans": "A",
        "stem": "No estudo da lógica bivalente clássica, uma proposição simples caracteriza-se por admitir um único valor lógico verdadeiro ou falso. Acerca da negação de uma proposição simples afirmativa P, assinale a opção correta.",
        "opts": [
            ("A", "A negação de P assume valor falso sempre que P for verdadeira, e valor verdadeiro sempre que P for falsa."),
            ("B", "A negação de P depende da inclusão obrigatória de quantificadores universais para alterar seu sentido lógico."),
            ("C", "A negação de P preserva inalterado o valor lógico original da proposição em respeito à lei da identidade."),
            ("D", "A negação de P transforma automaticamente uma oração declarativa em uma sentença de natureza imperativa."),
            ("E", "A negação de P produz uma proposição composta que admite simultaneamente valores verdadeiros e falsos.")
        ],
        "expl": "A negação lógica inverte estritamente o valor de verdade da proposição original. Quando a proposição inicial é verdadeira, sua negação resulta falsa; quando a proposição inicial é falsa, sua negação resulta verdadeira. Esse comportamento decorre dos princípios lógicos fundamentais da não contradição e do terceiro excluído."
    },
    {
        "seg": "a00/s03",
        "ans": "C",
        "stem": "Considere a proposição simples: 'O agente de polícia lavrou o auto de prisão em flagrante'. Assinale a opção que expressa corretamente a NEGAÇÃO dessa proposição por meio de uma expressão correlata.",
        "opts": [
            ("A", "O agente de polícia lavrou o boletim de ocorrência circunstanciado."),
            ("B", "O escrivão de polícia lavrou o auto de prisão em flagrante delito."),
            ("C", "Não é verdade que o agente de polícia lavrou o auto de prisão em flagrante."),
            ("D", "O agente de polícia com certeza não deixou de lavrar o auto de prisão."),
            ("E", "O auto de prisão em flagrante foi assinado por duas testemunhas idôneas.")
        ],
        "expl": "A negação de uma proposição simples afirmativa pode ser perfeitamente formulada antepondo-se expressões como 'não é verdade que' ou 'é falso que' à oração original completa. Substituir o sujeito ou o objeto não constitui negação lógica contraditória da declaração, mas mera alteração factual do conteúdo."
    },
    {
        "seg": "a00/s03",
        "ans": "B",
        "stem": "A lógica formal clássica apoia-se em princípios que regem a validade dos pensamentos e das proposições bivalentes. A respeito do princípio do terceiro excluído, assinale a opção correta.",
        "opts": [
            ("A", "Uma proposição pode apresentar simultaneamente os dois valores lógicos sob perspectivas diferentes."),
            ("B", "Toda proposição assume o valor verdadeiro ou o valor falso, não admitindo um terceiro valor lógico."),
            ("C", "A negação de uma proposição falsa resulta em um valor lógico indeterminado até prova em contrário."),
            ("D", "Duas proposições contraditórias podem ser ambas verdadeiras desde que expressas em tempos verbais distintos."),
            ("E", "Uma proposição sem verbo conjugado pode ser classificada como verdadeira em circunstâncias especiais.")
        ],
        "expl": "O princípio do terceiro excluído estabelece taxativamente que uma proposição ou é verdadeira ou é falsa, sendo excluída qualquer terceira possibilidade de valoração na lógica bivalente. Proposições não comportam estados intermediários de incerteza formal nem duplicidade de juízo simultâneo."
    },
    {
        "seg": "a00/s03",
        "ans": "C",
        "stem": "Em relação à distinção entre sentença, proposição e expressão na lógica clássica, assinale a opção correta.",
        "opts": [
            ("A", "Toda expressão numérica sem predicado verbal constitui uma proposição lógica fechada."),
            ("B", "Sentenças exclamativas e interrogativas admitem atribuição unívoca de valor verdadeiro ou falso."),
            ("C", "Proposição é o conteúdo declarativo expresso por uma oração que possui verbo e sentido completo."),
            ("D", "Uma sentença declarativa de sentido vago é considerada tautologia formal por expressar opinião."),
            ("E", "Toda oração na voz passiva perde a condição de proposição por ausência de sujeito ativo.")
        ],
        "expl": "Uma proposição consiste no significado expresso por uma oração declarativa que possui verbo, sujeito identificável ou quantificado e predicação completa, sendo apta a receber um único valor de verdade (verdadeiro ou falso). Frases nominais, perguntas, ordens e exclamações não constituem proposições lógicas."
    },

    # --- a00/s04 (q4 a q5) ---
    {
        "seg": "a00/s04",
        "ans": "E",
        "stem": "Considere o princípio lógico da dupla negação e sua generalização na linguagem proposicional. A respeito do valor lógico de uma proposição submetida a sucessivas negações, assinale a opção correta.",
        "opts": [
            ("A", "A aplicação de um número par de negações sobre uma proposição resulta sempre em valor indeterminado."),
            ("B", "A aplicação de três negações sucessivas sobre uma proposição verdadeira resulta em valor verdadeiro."),
            ("C", "Cada negação aplicada reduz o número de linhas da tabela-verdade da proposição composta."),
            ("D", "Um número ímpar de negações preserva o mesmo valor lógico original da proposição declarativa."),
            ("E", "A aplicação de um número par de negações sobre uma proposição equivale logicamente à própria proposição original.")
        ],
        "expl": "Pela lei da dupla negação, duas negações consecutivas se anulam mutualmente: ~(~P) é logicamente equivalente a P. Generalizando esse raciocínio, qualquer quantidade par de negações mantém inalterado o valor lógico da proposição de partida, enquanto uma quantidade ímpar de negações inverte seu valor de verdade."
    },
    {
        "seg": "a00/s04",
        "ans": "A",
        "stem": "Ao realizar a negação de uma proposição expressa por período composto com oração subordinada, a lógica clássica adota regra técnica específica. Com base nessa regra, assinale a opção correta.",
        "opts": [
            ("A", "Nega-se o verbo da oração principal, preservando-se inalterada a oração subordinada integrante."),
            ("B", "Nega-se exclusivamente a oração subordinada, mantendo-se a oração principal na forma afirmativa."),
            ("C", "Negam-se simultaneamente as duas orações, convertendo o conectivo integrante em disjunção inclusiva."),
            ("D", "Elimina-se o conectivo de subordinação e substitui-se o verbo principal por um pronome indefinido."),
            ("E", "Transforma-se o período subordinado em uma condicional simples com antecedentes invertidos.")
        ],
        "expl": "Na negação lógica de sentenças que contêm orações subordinadas substantivas integrantes (como 'O perito declarou que a arma disparou'), nega-se a oração principal ('O perito não declarou que a arma disparou'), mantendo-se o conteúdo da oração subordinada preservado, de modo a negar o juízo central emitido."
    },

    # --- a00/s05 (q6 a q7) ---
    {
        "seg": "a00/s05",
        "ans": "E",
        "stem": "No estudo dos conectivos lógicos fundamentais, a disjunção inclusiva e a disjunção exclusiva possuem tabelas-verdade distintas. A esse respeito, assinale a opção correta.",
        "opts": [
            ("A", "A disjunção inclusiva resulta verdadeira somente quando ambas as proposições forem simultaneamente verdadeiras."),
            ("B", "A disjunção exclusiva resulta verdadeira se ambas as proposições componentes tiverem o mesmo valor lógico."),
            ("C", "A disjunção inclusiva é falsa sempre que exatamente uma das proposições componentes for verdadeira."),
            ("D", "A disjunção exclusiva assume valor falso quando as proposições componentes possuem valores lógicos distintos."),
            ("E", "A disjunção inclusiva só é falsa quando ambas as proposições são falsas; a exclusiva só é verdadeira com valores opostos.")
        ],
        "expl": "A disjunção inclusiva (p ou q) só assume valor falso na única hipótese em que ambas as parcelas são falsas; bastando uma verdadeira para que seja verdadeira. A disjunção exclusiva (ou p, ou q) é verdadeira quando as parcelas têm valores lógicos diferentes (uma V e outra F) e falsa quando ambas são iguais (ambas V ou ambas F)."
    },
    {
        "seg": "a00/s05",
        "ans": "C",
        "stem": "Considere a condicional: 'Se o suspeito confessou a autoria, então o delegado concluiu o inquérito'. Sabendo-se que o suspeito NÃO confessou a autoria e que o delegado concluiu o inquérito, assinale a opção que indica o valor lógico dessa condicional.",
        "opts": [
            ("A", "Falso, pois a ausência de confissão anula a validade da conclusão policial."),
            ("B", "Indeterminado, visto que o consequente ocorreu sem respaldo do antecedente."),
            ("C", "Verdadeiro, pois uma condicional com antecedente falso resulta sempre em valor lógico verdadeiro."),
            ("D", "Falso, pois o consequente verdadeiro torna a estrutura contraditória no plano formal."),
            ("E", "Indeterminado, pois depende de homologação prévia da autoridade judicial competente.")
        ],
        "expl": "Na tabela-verdade da condicional p -> q, a proposição só é falsa quando o antecedente é verdadeiro e o consequente é falso (caso V -> F). Se o antecedente é falso (o suspeito não confessou), a condicional é invariavelmente verdadeira, independentemente de o consequente ser verdadeiro ou falso (casos F -> V e F -> F resultam V)."
    },

    # --- a00/s07 (q8 a q11) ---
    {
        "seg": "a00/s07",
        "ans": "C",
        "stem": "Na análise preliminar de relatórios de diligência, o investigador deve isolar as proposições lógicas legítimas de outras manifestações linguísticas. Considerando os critérios da lógica formal, assinale a opção que apresenta uma proposição lógica.",
        "opts": [
            ("A", "Mantenha a viatura abastecida e pronta para o deslocamento!"),
            ("B", "Quantos agentes participaram da operação policial integrada?"),
            ("C", "A delegacia especializada apreendeu cinquenta quilos de entorpecentes ontem."),
            ("D", "Que excelente trabalho desempenhado pela perícia criminal no local!"),
            ("E", "Favor apresentar a documentação pessoal no balcão de atendimento.")
        ],
        "expl": "A afirmativa declarativa que descreve a apreensão de entorpecentes possui verbo, sujeito determinado, sentido completo e expressa um fato factual que pode ser categoricamente classificado como verdadeiro ou falso. Frases imperativas, interrogativas, exclamativas e pedidos formais não constituem proposições lógicas."
    },
    {
        "seg": "a00/s07",
        "ans": "C",
        "stem": "Considere as sentenças a seguir registradas em um inquérito policial: I. 'Ele confessou a prática do crime'. II. '3 + 8 = 11'. III. 'O homicídio qualificado é um delito repugnante'. IV. 'Recife é a capital de Pernambuco'. Assinale a opção que apresenta apenas proposições lógicas fechadas.",
        "opts": [
            ("A", "I e II."),
            ("B", "I e III."),
            ("C", "II e IV."),
            ("D", "II e III."),
            ("E", "III e IV.")
        ],
        "expl": "As sentenças II (igualdade aritmética fechada) e IV (fato geográfico objetivo) são orações declarativas com sentido completo e fechado, valoradas objetivamente como verdadeiras. A sentença I é sentença aberta devido ao pronome indefinido 'Ele' sem referente no contexto, e a sentença III encerra juízo moral subjetivo/opinativo."
    },
    {
        "seg": "a00/s07",
        "ans": "E",
        "stem": "Acerca das frases optativas, interrogativas e imperativas no contexto das estruturas lógicas, assinale a opção correta.",
        "opts": [
            ("A", "Frases interrogativas transformam-se em proposições verdadeiras quando respondidas com clareza."),
            ("B", "Frases imperativas admitem valor falso se a ordem emitida for descumprida pelo destinatário."),
            ("C", "Frases optativas que expressam desejos pessoais são valoradas conforme a intenção do emissor."),
            ("D", "Perguntas judiciais constituem proposições compostas por conterem subordinação sintática."),
            ("E", "Frases que expressam ordens, perguntas ou votos de desejo não são proposições lógicas.")
        ],
        "expl": "Ordens (imperativas), perguntas (interrogativas) e expressões de desejo ou votos (optativas) não formulam asserções factuais sobre o mundo. Como não afirmam nem negam nada a respeito da realidade, não são suscetíveis de julgamento como verdadeiras ou falsas, ficando fora do conceito de proposição lógica."
    },
    {
        "seg": "a00/s07",
        "ans": "B",
        "stem": "Um analista deparou-se com a seguinte oração em um texto técnico: 'Esta frase é absolutamente falsa'. Sob a perspectiva da lógica proposicional clássica, assinale a opção que classifica corretamente essa frase.",
        "opts": [
            ("A", "Proposição simples de valor lógico verdadeiro."),
            ("B", "Paradoxo lógico autorreferencial, que não se qualifica como proposição lógica."),
            ("C", "Sentença aberta com quantificador existencial implícito."),
            ("D", "Proposição composta por duas orações coordenadas assindéticas."),
            ("E", "Contradição formal demonstrada por tabela-verdade de duas linhas.")
        ],
        "expl": "A declaração é o clássico paradoxo do mentiroso: se for considerada verdadeira, conclui-se que é falsa; se for considerada falsa, conclui-se que é verdadeira. Como gera inconsistência insolúvel e não pode assumir um valor de verdade estável e único, não constitui proposição lógica no sistema clássico."
    },

    # --- a00/s08 (q12 a q15) ---
    {
        "seg": "a00/s08",
        "ans": "B",
        "stem": "Considere a proposição simples afirmativa P: 'O policial civil estava escalado para o plantão de domingo'. Assinale a opção que apresenta uma proposição simples logicamente CONTRADITÓRIA com P.",
        "opts": [
            ("A", "O policial militar estava escalado para o plantão de domingo."),
            ("B", "O policial civil não estava escalado para o plantão de domingo."),
            ("C", "O policial civil estava de folga regulamentar no sábado à noite."),
            ("D", "O policial civil foi promovido por ato de bravura profissional."),
            ("E", "O comissário de polícia supervisionou o plantão de domingo.")
        ],
        "expl": "A proposição contraditória em relação a uma proposição afirmativa P é a sua negação estrita ~P. Sendo P 'o policial estava escalado', sua contraditória exata é 'o policial não estava escalado'. Duas contraditórias não podem ser simultaneamente verdadeiras nem simultaneamente falsas."
    },
    {
        "seg": "a00/s08",
        "ans": "E",
        "stem": "Em raciocínio lógico, as proposições simples caracterizam-se pela ausência de conectivos lógicos integradores. A esse respeito, assinale a opção correta.",
        "opts": [
            ("A", "Uma proposição simples admite receber dois valores lógicos verdadeiros em instantes consecutivos."),
            ("B", "Toda proposição simples é necessariamente formada por termos com quantificadores existenciais."),
            ("C", "Proposições simples não podem conter adjuntos adverbiais de tempo ou de lugar em sua redação."),
            ("D", "A conjunção aditiva 'e' pode integrar uma proposição simples sem transformá-la em composta."),
            ("E", "Uma proposição simples encerra um único juízo declarativo e não pode ser subdividida em outras proposições menores.")
        ],
        "expl": "A proposição simples (ou atômica) transmite uma declaração completa e indivisível dotada de um único verbo principal ou locução verbal, sem a presença de conectivos lógicos unindo duas orações declarativas distintas. Caso seja desmembrada, perde sua estrutura judicativa com sentido completo."
    },
    {
        "seg": "a00/s08",
        "ans": "E",
        "stem": "Considere as seguintes afirmativas sobre a valoração de proposições simples: I. 'O número 13 é primo' é uma proposição verdadeira. II. 'O Brasil é um país da Europa' é uma proposição falsa. III. 'x + 3 = 10' é uma proposição verdadeira. A respeito dessas afirmativas, assinale a opção correta.",
        "opts": [
            ("A", "Todas as afirmativas I, II e III estão corretas."),
            ("B", "Apenas a afirmativa III está correta."),
            ("C", "Apenas as afirmativas II e III estão corretas."),
            ("D", "Apenas a afirmativa I está correta."),
            ("E", "Apenas as afirmativas I e II estão corretas.")
        ],
        "expl": "A afirmativa I é proposição verdadeira (13 só é divisível por 1 e por ele mesmo). A afirmativa II é proposição falsa (o Brasil localiza-se na América do Sul). A afirmativa III não é proposição fechada, mas sim uma sentença aberta cujo valor de verdade depende do valor atribuído à variável x."
    },
    {
        "seg": "a00/s08",
        "ans": "B",
        "stem": "Um texto argumentativo afirma: 'O investigador é experiente'. Assinale a opção que apresenta uma forma válida de negar logicamente essa afirmação sem alterar o sentido formal de contradição.",
        "opts": [
            ("A", "O investigador é inexperiente e comete equívocos com frequência."),
            ("B", "É falso que o investigador seja experiente."),
            ("C", "O delegado de polícia que chefia a unidade é muito experiente."),
            ("D", "O investigador tem pouca experiência em crimes patrimoniais."),
            ("E", "O investigador participou de diversos cursos de capacitação técnica.")
        ],
        "expl": "A negação de 'O investigador é experiente' constrói-se formalmente negando o predicado ('O investigador não é experiente') ou antepondo o operador 'É falso que o investigador seja experiente'. Substituir por antônimos da língua cotidiana pode restringir o universo semântico ou introduzir gradações subjetivas."
    },

    # --- a00/s12 (q16 a q20) ---
    {
        "seg": "a00/s12",
        "ans": "C",
        "stem": "Na lógica proposicional, o valor lógico de uma proposição composta depende dos valores lógicos das proposições simples que a compõem e do conectivo empregado. Assinale a opção que apresenta uma proposição composta com valor lógico VERDADEIRO.",
        "opts": [
            ("A", "Se 2 + 2 = 5, então 3 + 3 = 7 e 4 + 4 = 9, sendo todas as parcelas verdadeiras."),
            ("B", "O número 8 é ímpar ou o número 6 é primo, com disjunção inclusiva."),
            ("C", "Se o número 10 é ímpar, então o número 12 é par."),
            ("D", "O número 5 é menor do que 3 se e somente se o número 4 for maior do que 1."),
            ("E", "O número 7 é par e o número 9 é divisível por três.")
        ],
        "expl": "Na condicional 'Se 10 é ímpar, então 12 é par', o antecedente é falso (10 é par) e o consequente é verdadeiro (12 é par). Pela tabela-verdade da condicional, o caso F -> V resulta em valor lógico verdadeiro. As demais expressões resultam falsas: disjunção de duas falsas (F), bicondicional de F e V (F) e conjunção com parcela falsa (F)."
    },
    {
        "seg": "a00/s12",
        "ans": "C",
        "stem": "Sabe-se que a proposição condicional: 'Se o alarme dispara, então o vigilante aciona a central' é FALSA. Diante dessa constatação fática, assinale a opção que apresenta uma proposição com valor lógico necessariamente VERDADEIRO.",
        "opts": [
            ("A", "O alarme não disparou."),
            ("B", "O vigilante acionou a central de monitoramento."),
            ("C", "O alarme disparou."),
            ("D", "O alarme disparou se e somente se o vigilante acionou a central."),
            ("E", "O alarme não disparou e o vigilante acionou a central.")
        ],
        "expl": "A condicional p -> q só assume valor falso em uma única linha da tabela-verdade: quando o antecedente p é verdadeiro e o consequente q é falso. Portanto, deduz-se necessariamente que 'o alarme disparou' é uma proposição verdadeira e 'o vigilante acionou a central' é uma proposição falsa."
    },
    {
        "seg": "a00/s12",
        "ans": "A",
        "stem": "Considere as proposições simples: p: 'Recife é uma cidade litorânea' e q: 'Caruaru fica situada no litoral pernambucano'. Sabendo-se que p é verdadeira e q é falsa, assinale a opção que apresenta a proposição composta de valor VERDADEIRO.",
        "opts": [
            ("A", "p ou q"),
            ("B", "p e q"),
            ("C", "p -> q"),
            ("D", "p <-> q"),
            ("E", "~p ou q")
        ],
        "expl": "Com p = V e q = F, a disjunção inclusiva p ou q resulta V ou F = V, pois basta uma das parcelas ser verdadeira para que a disjunção seja verdadeira. A conjunção resulta V e F = F; a condicional resulta V -> F = F; a bicondicional resulta V <-> F = F; e a disjunção ~p ou q resulta F ou F = F."
    },
    {
        "seg": "a00/s12",
        "ans": "D",
        "stem": "Sabe-se que a proposição conjuntiva 'A testemunha foi ouvida e o laudo foi anexado' é VERDADEIRA. A respeito das proposições componentes, assinale a opção correta.",
        "opts": [
            ("A", "A testemunha não foi ouvida, mas o laudo foi devidamente anexado aos autos."),
            ("B", "O laudo não foi anexado aos autos do inquérito policial da comarca."),
            ("C", "Basta que a testemunha tenha sido ouvida para garantir a verdade da frase."),
            ("D", "Tanto a oitiva da testemunha quanto a anexação do laudo são fatos verdadeiros."),
            ("E", "A proposição composta possui valor lógico falso na metade de sua tabela-verdade.")
        ],
        "expl": "A conjunção p e q só assume valor verdadeiro na única hipótese em que ambas as proposições componentes são simultaneamente verdadeiras. Assim, da veracidade da conjunção decorre obrigatoriamente que a testemunha foi ouvida e o laudo foi anexado, sendo ambas verdadeiras."
    },
    {
        "seg": "a00/s12",
        "ans": "C",
        "stem": "A respeito do conectivo de disjunção exclusiva (ou... ou) na análise de estruturas lógicas, assinale a opção correta.",
        "opts": [
            ("A", "A disjunção exclusiva é verdadeira quando ambas as componentes são verdadeiras."),
            ("B", "A disjunção exclusiva resulta verdadeira se ambas as componentes forem falsas."),
            ("C", "A disjunção exclusiva assume valor falso quando as componentes possuem o mesmo valor lógico."),
            ("D", "A disjunção exclusiva é equivalente à disjunção inclusiva em qualquer circunstância."),
            ("E", "A disjunção exclusiva não permite a inversão comutativa de seus termos componentes.")
        ],
        "expl": "A disjunção exclusiva (ou p, ou q) é falsa exatamente quando ambas as proposições apresentam o mesmo valor lógico: tanto no caso em que ambas são verdadeiras quanto no caso em que ambas são falsas. Ela resulta verdadeira apenas quando uma das parcelas é verdadeira e a outra é falsa."
    },

    # --- a01/s01 (q21 a q25) ---
    {
        "seg": "a01/s01",
        "ans": "B",
        "stem": "Na formalização simbólica de proposições da lógica proposicional, a ordem de precedência dos conectivos lógicos define quais operações devem ser processadas prioritariamente na ausência de parênteses. Assinale a opção que indica o conectivo de MAIOR precedência hierárquica.",
        "opts": [
            ("A", "Condicional (->)"),
            ("B", "Negação (~)"),
            ("C", "Disjunção inclusiva (ou)"),
            ("D", "Bicondicional (<->)"),
            ("E", "Disjunção exclusiva (ou exclusivo)")
        ],
        "expl": "Na convenção padrão da lógica proposicional, o operador de negação (~) possui a mais alta precedência entre os conectivos, aplicando-se imediatamente sobre a variável ou subexpressão adjacente. Seguem-se os conectivos de conjunção e disjunção, depois o condicional e, por fim, o bicondicional."
    },
    {
        "seg": "a01/s01",
        "ans": "C",
        "stem": "Em textos em língua natural, o emprego de vírgulas e pontuação sintática é determinante para identificar os parênteses da fórmula lógica. Considere a frase: 'Se o agente faz a ronda e o escrivão atende ao público, então a delegacia opera normalmente'. Assinale a opção que apresenta a correta simbolização dessa estrutura, considerando as proposições simples p, q e r.",
        "opts": [
            ("A", "p e (q -> r)"),
            ("B", "(p -> q) e r"),
            ("C", "(p e q) -> r"),
            ("D", "p -> (q e r)"),
            ("E", "(p ou q) -> r")
        ],
        "expl": "A vírgula após 'público' encerra a oração subordinada condicional composta pela conjunção das ações do agente e do escrivão, funcionando como delimitador do antecedente completo. Assim, o bloco antecedente é (p e q) e o consequente é r, resultando na fórmula condicional (p e q) -> r."
    },
    {
        "seg": "a01/s01",
        "ans": "D",
        "stem": "Considere a proposição composta simbolizada por: ~p e q -> r. Obedecendo à ordem padrão de precedência estrita dos conectivos lógicos, assinale a opção que apresenta o correto posicionamento dos parênteses implícitos.",
        "opts": [
            ("A", "~(p e (q -> r))"),
            ("B", "~p e (q -> r)"),
            ("C", "(~p) e (q -> r)"),
            ("D", "((~p) e q) -> r"),
            ("E", "~((p e q) -> r)")
        ],
        "expl": "Pela hierarquia padrão dos conectivos lógicos: primeiro atua a negação sobre p, resultando em (~p); em seguida atua a conjunção com q, formando a subfórmula ((~p) e q); por último, atua a condicional de menor precedência em direção a r, estruturando a expressão como ((~p) e q) -> r."
    },
    {
        "seg": "a01/s01",
        "ans": "B",
        "stem": "A correta conversão de enunciados da linguagem natural para a linguagem simbólica exige atenção ao escopo das negações. Considere a declaração: 'Não é o caso que o suspeito mentiu e a testemunha se omitiu'. Sendo m: 'O suspeito mentiu' e o: 'A testemunha se omitiu', assinale a opção que representa adequadamente essa declaração.",
        "opts": [
            ("A", "~m e o"),
            ("B", "~(m e o)"),
            ("C", "~m e ~o"),
            ("D", "m e ~o"),
            ("E", "~(m ou o)")
        ],
        "expl": "A expressão introdutória 'Não é o caso que' nega o período composto conjuntivo em sua totalidade, abrangendo o escopo inteiro da conjunção subsequente. Essa relação de escopo global exige o emprego de parênteses englobando ambos os termos: ~(m e o)."
    },
    {
        "seg": "a01/s01",
        "ans": "A",
        "stem": "Considere a frase: 'O réu será condenado se, e somente se, confessar o delito ou as provas periciais forem conclusivas'. Definindo c: 'O réu será condenado', d: 'O réu confessa o delito' e p: 'As provas periciais são conclusivas', assinale a opção que expressa a tradução simbólica dessa proposição.",
        "opts": [
            ("A", "c <-> (d ou p)"),
            ("B", "(c <-> d) ou p"),
            ("C", "c -> (d e p)"),
            ("D", "(c e d) <-> p"),
            ("E", "c <-> (d e p)")
        ],
        "expl": "A locução 'se, e somente se' estabelece um conectivo bicondicional entre a primeira proposição simples c e a proposição composta subsequente, que consiste em uma disjunção inclusiva indicada pelo 'ou' entre d e p. Assim, a representação formal rigorosa é c <-> (d ou p)."
    },

    # --- a01/s02 (q26) ---
    {
        "seg": "a01/s02",
        "ans": "D",
        "stem": "Ao iniciar a construção da tabela-verdade de uma proposição composta contendo 5 proposições simples distintas, o analista deve determinar a quantidade exata de linhas necessárias. Com base na regra do cálculo de linhas, assinale a opção correta.",
        "opts": [
            ("A", "10 linhas."),
            ("B", "16 linhas."),
            ("C", "25 linhas."),
            ("D", "32 linhas."),
            ("E", "64 linhas.")
        ],
        "expl": "O número total de linhas de uma tabela-verdade com n variáveis proposicionais distintas é calculado pela fórmula exponencial 2^n. Para n = 5 proposições simples distintas, tem-se 2^5 = 2 * 2 * 2 * 2 * 2 = 32 linhas necessárias para cobrir todas as combinações possíveis de valores verdadeiros e falsos."
    },

    # --- a01/s05 (q27 a q31) ---
    {
        "seg": "a01/s05",
        "ans": "C",
        "stem": "No cálculo proposicional clássico, diz-se que uma proposição P implica logicamente uma proposição Q quando ocorre uma relação formal específica entre elas. Assinale a opção que define essa relação de implicação lógica.",
        "opts": [
            ("A", "A proposição bicondicional P <-> Q é classificada como contingente."),
            ("B", "A conjunção P e Q assume valor verdadeiro em exatamente metade das linhas."),
            ("C", "A proposição condicional P -> Q é uma tautologia."),
            ("D", "A disjunção P ou Q resulta em uma contradição lógica absoluta."),
            ("E", "A negação de P equivale logicamente à própria proposição Q.")
        ],
        "expl": "Ocorre implicação lógica de P para Q (indicada por P => Q) se, e somente se, a condicional associada P -> Q for uma tautologia (isto é, verdadeira em todas as linhas de sua tabela-verdade). Nesse caso, é logicamente impossível que P seja verdadeira e Q seja falsa simultaneamente."
    },
    {
        "seg": "a01/s05",
        "ans": "C",
        "stem": "Considere a condicional P: 'p e q -> p'. Para verificar se a conjunção p e q implica logicamente a proposição simples p, assinale a opção correta.",
        "opts": [
            ("A", "A condicional resulta falsa quando p é verdadeira e q é falsa."),
            ("B", "A condicional é contingente, pois assume valor falso quando p e q forem falsas."),
            ("C", "A condicional é uma tautologia, confirmando que a conjunção p e q implica logicamente p."),
            ("D", "A condicional é uma contradição, pois antecedente e consequente repetem a letra p."),
            ("E", "A implicação inexiste porque o consequente não contém conectivos de disjunção.")
        ],
        "expl": "Para que (p e q) -> p fosse falsa, o antecedente (p e q) precisaria ser verdadeiro e o consequente p ser falso. Contudo, se (p e q) é verdadeiro, p é obrigatoriamente verdadeiro, tornando impossível o consequente ser falso. Logo, a condicional resulta verdadeira em todas as linhas, configurando tautologia e provando a implicação."
    },
    {
        "seg": "a01/s05",
        "ans": "D",
        "stem": "Um relatório policial continha a seguinte frase: 'Quando o suspeito é abordado em flagrante, ele é conduzido à delegacia'. Assinale a opção que expressa a correta conversão dessa oração para a estrutura condicional padrão da lógica formal.",
        "opts": [
            ("A", "O suspeito é abordado em flagrante e é conduzido à delegacia."),
            ("B", "O suspeito é abordado em flagrante ou é conduzido à delegacia."),
            ("C", "O suspeito é abordado em flagrante se e somente se for conduzido à delegacia."),
            ("D", "Se o suspeito é abordado em flagrante, então ele é conduzido à delegacia."),
            ("E", "Se o suspeito é conduzido à delegacia, então foi abordado em flagrante.")
        ],
        "expl": "A conjunção temporal 'Quando...' atua semanticamente na linguagem natural como um indicador de hipótese ou condição suficiente, equivalendo à estrutura do condicional padrão 'Se..., então...'. O fato temporal introduz o antecedente da implicação, resultando em 'Se o suspeito é abordado em flagrante, então é conduzido à delegacia'."
    },
    {
        "seg": "a01/s05",
        "ans": "C",
        "stem": "Em lógica formal, a expressão 'p é condição suficiente para q' descreve a relação de implicação expressa pelo conectivo condicional. Com base nessa definição conceitual, assinale a opção correta.",
        "opts": [
            ("A", "A relação é expressa simbolicamente por q -> p."),
            ("B", "A relação exige que p e q sejam simultaneamente falsas para ocorrer implicação."),
            ("C", "A relação é expressa simbolicamente por p -> q."),
            ("D", "A relação indica que a ocorrência de q é indispensável para que p possa existir."),
            ("E", "A relação equivale à disjunção inclusiva p ou q.")
        ],
        "expl": "Afirmar que 'p é condição suficiente para q' significa que a ocorrência ou veracidade de p basta para garantir com certeza a ocorrência de q, o que se formaliza exatamente pela condicional p -> q (na qual p é o antecedente e condição suficiente, e q é o consequente e condição necessária)."
    },
    {
        "seg": "a01/s05",
        "ans": "D",
        "stem": "Deseja-se verificar se uma proposição composta A implica a proposição B por meio do teste de falsidade. Assinale a opção que indica o procedimento correto para esse teste.",
        "opts": [
            ("A", "Supor que A e B são ambas falsas e verificar se surge tautologia."),
            ("B", "Atribuir valor verdadeiro a B e buscar uma contradição lógica nas premissas."),
            ("C", "Atribuir valor falso a A e demonstrar que B assume obrigatoriamente valor verdadeiro."),
            ("D", "Supor que A é verdadeira e B é falsa; se essa hipótese gerar uma contradição lógica, a implicação é válida."),
            ("E", "Inverter a ordem das proposições e testar se B -> A é uma contingência empírica.")
        ],
        "expl": "A implicação A => B equivale a demonstrar que a condicional A -> B nunca é falsa. Para testar isso de forma direta, assume-se a única hipótese que tornaria a condicional falsa: antecedente A verdadeiro e consequente B falso. Se dessa hipótese decorrer uma contradição lógica incontornável, prova-se que o caso falso é impossível, validando a implicação."
    },

    # --- a01/s06 (q32 a q36) ---
    {
        "seg": "a01/s06",
        "ans": "A",
        "stem": "Ao construir a tabela-verdade da proposição composta: ~(p -> ~q), o preenchimento das colunas intermediárias deve obedecer à ordem das operações. Assinale a opção que indica a quantidade de linhas em que essa proposição assume valor VERDADEIRO.",
        "opts": [
            ("A", "Exatamente 1 linha."),
            ("B", "Exatamente 2 linhas."),
            ("C", "Exatamente 3 linhas."),
            ("D", "Exatamente 4 linhas."),
            ("E", "Nenhuma linha.")
        ],
        "expl": "Com duas variáveis simples (p e q), a tabela possui 4 linhas. A expressão interna p -> ~q só é falsa quando o antecedente p é verdadeiro e o consequente ~q é falso (isto é, quando q é verdadeiro). Isso ocorre em exatamente 1 linha: p = V e q = V. Como a proposição final é a negação ~(p -> ~q), ela será verdadeira exatamente onde a condicional interna foi falsa, ou seja, em 1 linha."
    },
    {
        "seg": "a01/s06",
        "ans": "A",
        "stem": "Considere a tabela-verdade da proposição P: '(p ou q) e (~p)'. Analisando os valores obtidos na coluna final dessa proposição para as 4 linhas possíveis, assinale a opção correta.",
        "opts": [
            ("A", "P assume valor verdadeiro em apenas uma linha, exatamente quando p é falsa e q é verdadeira."),
            ("B", "P assume valor verdadeiro em todas as linhas, configurando uma tautologia clássica."),
            ("C", "P assume valor falso em todas as linhas, caracterizando uma contradição lógica absoluta."),
            ("D", "P assume valor verdadeiro em duas linhas, quando p for verdadeira independentemente de q."),
            ("E", "P resulta verdadeira sempre que ambas as proposições componentes forem verdadeiras.")
        ],
        "expl": "Para a conjunção final ser verdadeira, ambas as parcelas precisam ser verdadeiras: ~p deve ser V (logo, p deve ser F) e (p ou q) deve ser V. Com p = F, a disjunção (F ou q) só é verdadeira se q for V. Essa combinação (p = F e q = V) ocorre em exatamente uma linha da tabela-verdade, resultando em V apenas nesse caso."
    },
    {
        "seg": "a01/s06",
        "ans": "B",
        "stem": "Ao preencher a tabela-verdade de uma proposição com três variáveis simples (p, q e r), a técnica padrão de alternância de valores distribui os valores lógicos nas colunas iniciais. A esse respeito, assinale a opção correta.",
        "opts": [
            ("A", "A primeira coluna varia de um em um, a segunda de dois em dois e a terceira de três em três."),
            ("B", "A primeira coluna alterna blocos de quatro valores, a segunda de dois em dois e a terceira de um em um."),
            ("C", "Todas as três colunas iniciais devem alternar valores individuais de um em um de modo idêntico."),
            ("D", "A quantidade de valores verdadeiros deve ser rigorosamente o dobro da quantidade de falsos na tabela."),
            ("E", "A alternância de valores nas colunas iniciais é arbitrária e dispensa qualquer padrão regular.")
        ],
        "expl": "Em uma tabela de 8 linhas (2³), para cobrir sistematicamente todas as 8 combinações de valoração sem repetições nem omissões, a primeira variável recebe 4 V seguidos de 4 F; a segunda variável alterna de 2 em 2 (VV, FF, VV, FF); e a terceira variável alterna de 1 em 1 (V, F, V, F, V, F, V, F)."
    },
    {
        "seg": "a01/s06",
        "ans": "B",
        "stem": "Considere a proposição composta: '(p <-> q) ou r'. Ao calcular a coluna final dessa proposição em sua tabela-verdade de 8 linhas, assinale a opção que indica a quantidade de linhas que resultarão com valor lógico FALSO.",
        "opts": [
            ("A", "Exatamente 1 linha."),
            ("B", "Exatamente 2 linhas."),
            ("C", "Exatamente 3 linhas."),
            ("D", "Exatamente 4 linhas."),
            ("E", "Exatamente 5 linhas.")
        ],
        "expl": "A disjunção final só é falsa quando ambas as parcelas são falsas: r deve ser F e (p <-> q) deve ser F. A bicondicional (p <-> q) é falsa quando p e q possuem valores lógicos opostos (em 4 das 8 linhas). Dessas 4 linhas, em exatamente metade (2 linhas) a variável r assume o valor falso. Logo, a disjunção final resulta falsa em exatamente 2 linhas."
    },
    {
        "seg": "a01/s06",
        "ans": "A",
        "stem": "Analise a tabela-verdade da fórmula: 'p e ~p'. A respeito do resultado encontrado na última coluna dessa proposição composta, assinale a opção correta.",
        "opts": [
            ("A", "Todas as linhas da coluna final apresentam valor lógico falso, caracterizando uma contradição."),
            ("B", "Todas as linhas da coluna final apresentam valor lógico verdadeiro, caracterizando uma tautologia."),
            ("C", "A coluna final apresenta alternância entre valores verdadeiros e falsos, sendo uma contingência."),
            ("D", "O valor lógico da última coluna depende estritamente do número de proposições do contexto."),
            ("E", "A tabela-verdade não pode ser concluída por violar o princípio do terceiro excluído.")
        ],
        "expl": "Na fórmula p e ~p, quando p é V, ~p é F, resultando V e F = F; quando p é F, ~p é V, resultando F e V = F. Em todas as linhas da tabela-verdade, a conjunção de uma proposição com sua própria negação assume invariavelmente valor falso, constituindo o exemplo clássico de contradição lógica."
    },

    # --- a01/s07 (q37 a q40) ---
    {
        "seg": "a01/s07",
        "ans": "D",
        "stem": "No estudo da classificação de proposições compostas, uma proposição é classificada como TAUTOLOGIA quando atende a um requisito específico. Assinale a opção que descreve esse requisito.",
        "opts": [
            ("A", "Apresentar valor verdadeiro na maioria simples das linhas de sua tabela-verdade."),
            ("B", "Ser formada unicamente por proposições simples que versem sobre fatos históricos verídicos."),
            ("C", "Conter obrigatoriamente um conectivo de disjunção exclusiva associado a uma condicional."),
            ("D", "Assumir invariavelmente o valor lógico verdadeiro em todas as linhas possíveis de sua tabela-verdade."),
            ("E", "Resultar em valor falso sempre que todas as proposições simples componentes forem falsas.")
        ],
        "expl": "Uma tautologia (ou proposição tautológica) é aquela proposição composta cuja tabela-verdade encerra exclusivamente o valor lógico verdadeiro (V) em todas as suas linhas, independentemente dos valores de verdade que sejam atribuídos às proposições atômicas que a integram."
    },
    {
        "seg": "a01/s07",
        "ans": "D",
        "stem": "Deseja-se classificar a fórmula: 'p -> (p ou q)' sem construir a tabela-verdade completa. Utilizando a análise das propriedades lógicas da condicional, assinale a opção correta.",
        "opts": [
            ("A", "Trata-se de uma contradição, pois a condicional liga uma simples a uma disjunção inclusiva."),
            ("B", "Trata-se de uma contingência, visto que resulta falsa quando p for verdadeira e q for falsa."),
            ("C", "Trata-se de uma contingência, pois assume valor falso quando p e q forem ambas falsas."),
            ("D", "Trata-se de uma tautologia, pois sempre que o antecedente p for verdadeiro, o consequente (p ou q) será verdadeiro."),
            ("E", "Trata-se de uma contradição, visto que supor a fórmula verdadeira gera incoerência formal.")
        ],
        "expl": "Para a condicional p -> (p ou q) ser falsa, o antecedente p deveria ser V e o consequente (p ou q) ser F. Porém, se p é V, a disjunção (p ou q) é obrigatoriamente V. Logo, a situação de antecedente V e consequente F é absolutamente impossível, tornando a condicional verdadeira em todos os casos, ou seja, uma tautologia."
    },
    {
        "seg": "a01/s07",
        "ans": "E",
        "stem": "Considere a proposição composta: '(p -> q) e (p e ~q)'. Ao avaliar a classificação dessa fórmula na lógica proposicional, assinale a opção correta.",
        "opts": [
            ("A", "É uma tautologia, pois a conjunção preserva o valor lógico da condicional precedente."),
            ("B", "É uma contingência, pois assume valor verdadeiro quando p e q são ambas verdadeiras."),
            ("C", "É uma contingência, pois assume valor verdadeiro quando p é falsa e q é verdadeira."),
            ("D", "É uma proposição equivalente à simples negação da variável atômica p."),
            ("E", "É uma contradição lógica, pois as duas parcelas da conjunção não podem ser verdadeiras simultaneamente.")
        ],
        "expl": "A conjunção é formada por dois termos: a condicional (p -> q) e a fórmula (p e ~q). O segundo termo (p e ~q) representa exatamente a negação da condicional (o único caso em que ela é falsa). Dessa forma, a expressão tem a estrutura A e ~A, o que resulta em valor falso para toda e qualquer linha da tabela-verdade, tratando-se de uma contradição."
    },
    {
        "seg": "a01/s07",
        "ans": "E",
        "stem": "Na lógica proposicional, o conceito de CONTINGÊNCIA opõe-se tanto ao de tautologia quanto ao de contradição. Assinale a opção que apresenta um exemplo de fórmula contingente.",
        "opts": [
            ("A", "p ou ~p"),
            ("B", "p -> p"),
            ("C", "p e ~p"),
            ("D", "p <-> p"),
            ("E", "p -> q")
        ],
        "expl": "Uma contingência é aquela fórmula que não é sempre verdadeira nem sempre falsa, apresentando pelo menos um V e pelo menos um F na última coluna da tabela-verdade. A condicional simples p -> q assume valor falso quando p é V e q é F, e valor verdadeiro nos demais casos, sendo uma contingência. As expressões p ou ~p, p -> p e p <-> p são tautologias, e p e ~p é contradição."
    },

    # --- a01/s09 (q41 a q42) ---
    {
        "seg": "a01/s09",
        "ans": "B",
        "stem": "Considere a proposição: 'Se o agente participa do curso de aperfeiçoamento, então obtém a certificação operacional'. Sabendo que essa afirmação é verdadeira e que o agente NÃO obteve a certificação operacional, assinale a opção que expressa uma dedução correta.",
        "opts": [
            ("A", "O agente participou do curso de aperfeiçoamento e foi reprovado no exame final."),
            ("B", "O agente não participou do curso de aperfeiçoamento."),
            ("C", "O agente participou do curso de aperfeiçoamento com dispensa de frequência."),
            ("D", "O agente obteve outra certificação técnica em instituição privada conveniada."),
            ("E", "Não é possível deduzir se o agente participou ou não do curso de aperfeiçoamento.")
        ],
        "expl": "Pela regra de inferência válida do Modus Tollens, dada uma condicional verdadeira p -> q e a negação do seu consequente (~q), decorre necessariamente a negação do seu antecedente (~p). Como o agente não obteve a certificação (~q), deduz-se obrigatoriamente que ele não participou do curso (~p)."
    },
    {
        "seg": "a01/s09",
        "ans": "B",
        "stem": "Em uma investigação sobre crimes cibernéticos, verificou-se que a proposição: 'O arquivo suspeito foi deletado ou a senha de acesso foi modificada' é FALSA. Diante dessa constatação fática sobre a disjunção inclusiva, assinale a opção correta.",
        "opts": [
            ("A", "O arquivo suspeito foi deletado e a senha de acesso não foi modificada."),
            ("B", "O arquivo suspeito não foi deletado e a senha de acesso não foi modificada."),
            ("C", "O arquivo suspeito não foi deletado, mas a senha de acesso foi modificada."),
            ("D", "O arquivo suspeito foi deletado e a senha de acesso foi modificada."),
            ("E", "Pelo menos um dos dois eventos investigados ocorreu com certeza no sistema.")
        ],
        "expl": "Uma disjunção inclusiva p ou q só assume valor falso na tabela-verdade quando ambas as proposições componentes são simultaneamente falsas. Assim, sendo a disjunção falsa, decorre taxativamente que 'o arquivo foi deletado' é falso (logo, não foi deletado) e 'a senha foi modificada' é falso (logo, não foi modificada), configurando a conjunção de duas negações."
    }
]
