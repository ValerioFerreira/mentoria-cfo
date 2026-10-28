"""Bloco 4 das novas questoes de Raciocinio Logico (22 questoes: q110 a q131).
Trechos: a07/s01 (4), a07/s02 (4), a07/s03 (3),
         a07/s04 (3), a07/s05 (4), a07/s06 (4).
Gabaritos extraidos estritamente de gabaritos_132.json (indices 110 a 131):
['E', 'B', 'C', 'A', 'E', 'B', 'C', 'A', 'C', 'B', 'A', 'A', 'D', 'C', 'D', 'E', 'D', 'A', 'E', 'C', 'D', 'E']
"""

QUESTOES_BLOCO4 = [
    # --- a07/s01 (q110 a q113) ---
    {
        "seg": "a07/s01",
        "ans": "E",
        "stem": "No plantão de um quartel do Corpo de Bombeiros, uma central de despacho recebe chamados de socorro classificados em três naturezas possíveis: Resgate (R), Incêndio (I) ou Salvamento (S). Ao analisar o registro dos dois primeiros chamados consecutivos recebidos em determinada manhã, assinale a opção que indica a probabilidade de ambos os chamados serem de naturezas rigorosamente distintas, considerando que todas as 9 combinações do espaço amostral são equiprováveis.",
        "opts": [
            ("A", "1/9"),
            ("B", "1/3"),
            ("C", "4/9"),
            ("D", "5/9"),
            ("E", "2/3")
        ],
        "expl": "O espaço amostral completo dos dois chamados sucessivos é composto por 3 × 3 = 9 pares ordenados equiprováveis. Os casos em que os dois chamados possuem a mesma natureza correspondem a 3 pares: (R,R), (I,I) e (S,S). Logo, os casos favoráveis ao evento em que os dois chamados possuem naturezas distintas totalizam 9 − 3 = 6 pares. Pela definição clássica de probabilidade, tem-se P = 6 / 9 = 2/3."
    },
    {
        "seg": "a07/s01",
        "ans": "B",
        "stem": "Em um levantamento de vistoria predial realizado pela Seção de Atividades Técnicas dos Bombeiros, foram inspecionadas 80 edificações comerciais. Constatou-se que 48 possuíam extintores dentro do prazo de validade, 32 apresentavam sinalização de emergência adequada e 16 possuíam ambos os itens em conformidade. Sorteando-se ao acaso uma dessas edificações, assinale a opção que apresenta a probabilidade de ela NÃO apresentar nenhuma dessas duas conformidades.",
        "opts": [
            ("A", "15%"),
            ("B", "20%"),
            ("C", "25%"),
            ("D", "30%"),
            ("E", "40%")
        ],
        "expl": "Pelo princípio da inclusão-exclusão, o número de edificações que apresentam pelo menos uma das duas conformidades inspecionadas é dado por n(E ∪ S) = n(E) + n(S) − n(E ∩ S) = 48 + 32 − 16 = 64 edificações. Consequentemente, a quantidade de edificações que não possuem nenhuma dessas conformidades é 80 − 64 = 16. A probabilidade de selecionar aleatoriamente uma dessas edificações é 16 / 80 = 1/5 = 20%."
    },
    {
        "seg": "a07/s01",
        "ans": "C",
        "stem": "Um pelotão é composto por 6 bombeiros homens e 4 bombeiras mulheres. O comandante selecionará por sorteio uma comissão de 3 bombeiros para representar a corporação em um congresso nacional. Assinale a opção que expressa a probabilidade de a comissão sorteada ser formada exclusivamente por mulheres.",
        "opts": [
            ("A", "1/120"),
            ("B", "1/60"),
            ("C", "1/30"),
            ("D", "1/15"),
            ("E", "1/10")
        ],
        "expl": "O total de comissões possíveis de 3 integrantes escolhidos sem distinção de ordem entre os 10 membros do pelotão é dado por C(10, 3) = (10 × 9 × 8) / 6 = 120 comissões equiprováveis. Os casos favoráveis, consistindo em comissões compostas unicamente por mulheres, correspondem a escolher 3 dentre as 4 mulheres disponíveis: C(4, 3) = 4. Aplicando a definição de probabilidade, obtém-se 4 / 120 = 1/30."
    },
    {
        "seg": "a07/s01",
        "ans": "A",
        "stem": "Cinco policiais civis (identificados como P1, P2, P3, P4 e P5) concorrem a dois cargos distintos em um conselho disciplinar: Presidente e Secretário, definidos por sorteio sucessivo sem reposição. Assinale a opção que indica a probabilidade de P1 ser sorteado como Presidente e P2 como Secretário.",
        "opts": [
            ("A", "1/20"),
            ("B", "1/10"),
            ("C", "1/5"),
            ("D", "2/5"),
            ("E", "1/25")
        ],
        "expl": "Como os cargos a serem preenchidos são distintos (Presidente e Secretário), a ordem do sorteio é determinante, configurando um arranjo simples. O espaço amostral de atribuições é A(5, 2) = 5 × 4 = 20 pares ordenados possíveis e equiprováveis. O evento específico no qual P1 assume a presidência e P2 assume a secretaria corresponde a exatamente 1 resultado favorável no espaço amostral. Assim, a probabilidade é 1/20."
    },

    # --- a07/s02 (q114 a q117) ---
    {
        "seg": "a07/s02",
        "ans": "E",
        "stem": "Durante um programa de controle de qualidade de equipamentos de proteção individual (EPI), um laboratório de perícia submeteu 5.000 mosquetões de salvamento a testes rigorosos de tração mecânica, registrando defeito estrutural em 40 dessas peças. Com base nesse histórico experimental e no conceito de probabilidade como limite da frequência relativa, assinale a opção que expressa a estimativa da probabilidade de um mosquetão do mesmo lote apresentar defeito de tração.",
        "opts": [
            ("A", "0,08%"),
            ("B", "0,2%"),
            ("C", "0,4%"),
            ("D", "0,5%"),
            ("E", "0,8%")
        ],
        "expl": "A probabilidade empírica (ou estatística) de um evento é estimada pela frequência relativa observada em uma amostra de grande porte sob condições estáveis: f = n / N. Tendo ocorrido 40 defeitos em N = 5.000 ensaios, a estimativa pontual da probabilidade de falha é 40 / 5.000 = 0,008, o que equivale a 0,8%."
    },
    {
        "seg": "a07/s02",
        "ans": "B",
        "stem": "Em uma corporação de bombeiros, 60% do efetivo possui habilitação para condução de veículos de emergência (evento A) e 50% possui curso de resgate em estruturas colapsadas (evento B). Sabendo que 30% do efetivo possui ambas as qualificações, assinale a opção que apresenta a probabilidade de um militar sorteado ao acaso possuir habilitação para veículos de emergência OU curso de estruturas colapsadas.",
        "opts": [
            ("A", "70%"),
            ("B", "80%"),
            ("C", "85%"),
            ("D", "90%"),
            ("E", "95%")
        ],
        "expl": "Pelo teorema da probabilidade da união de dois eventos, a probabilidade de ocorrência de pelo menos um dos eventos é expressa por P(A ∪ B) = P(A) + P(B) − P(A ∩ B). Substituindo os valores informados, tem-se P(A ∪ B) = 0,60 + 0,50 − 0,30 = 0,80, correspondendo a 80% do efetivo."
    },
    {
        "seg": "a07/s02",
        "ans": "C",
        "stem": "Durante uma operação de resgate rodoviário, as vítimas socorridas são triadas no método START por gravidade imediata em três categorias mutuamente exclusivas: Vermelha (imediata, com probabilidade de 0,25), Amarela (urgente, com probabilidade de 0,45) ou Verde (leve, com probabilidade de 0,30). Assinale a opção que indica a probabilidade de uma vítima selecionada ao acaso ser classificada como Vermelha OU Amarela.",
        "opts": [
            ("A", "55%"),
            ("B", "60%"),
            ("C", "70%"),
            ("D", "75%"),
            ("E", "80%")
        ],
        "expl": "Quando dois eventos são mutuamente excludentes (disjuntos), a interseção entre eles é vazia (probabilidade nula), de modo que a ocorrência de um impede a do outro. Nesses casos, a probabilidade da união é a simples soma das probabilidades individuais: P(Vermelha ∪ Amarela) = P(Vermelha) + P(Amarela) = 0,25 + 0,45 = 0,70 (ou 70%)."
    },
    {
        "seg": "a07/s02",
        "ans": "A",
        "stem": "Uma pesquisa com 100 cadetes sobre aptidões esportivas revelou que 50 praticam natação (N), 40 praticam corrida (C) e 35 praticam tiro (T). Além disso, 20 praticam N e C, 15 praticam N e T, 10 praticam C e T, e todos os 100 cadetes praticam pelo menos uma dessas três modalidades. Assinale a opção que expressa a probabilidade de um cadete sorteado ao acaso praticar as três modalidades simultaneamente.",
        "opts": [
            ("A", "20%"),
            ("B", "15%"),
            ("C", "10%"),
            ("D", "25%"),
            ("E", "30%")
        ],
        "expl": "Pelo princípio da inclusão-exclusão para três conjuntos, tem-se n(N ∪ C ∪ T) = n(N) + n(C) + n(T) − [n(N ∩ C) + n(N ∩ T) + n(C ∩ T)] + n(N ∩ C ∩ T). Substituindo os valores: 100 = 50 + 40 + 35 − (20 + 15 + 10) + n(tripla), o que simplifica para 100 = 125 − 45 + n(tripla) = 80 + n(tripla). Logo, a quantidade de praticantes das três modalidades é 20, representando uma probabilidade de 20 / 100 = 20%."
    },

    # --- a07/s03 (q118 a q120) ---
    {
        "seg": "a07/s03",
        "ans": "C",
        "stem": "Em um depósito de equipamentos táticos, há 50 rádios transmissores, dos quais 8 apresentam falha intermitente de bateria e os demais operam com carga perfeita. Sorteando-se ao acaso um transmissor para uma viatura em saída rápida, assinale a opção que indica a probabilidade de o rádio escolhido NÃO apresentar falha de bateria.",
        "opts": [
            ("A", "76%"),
            ("B", "80%"),
            ("C", "84%"),
            ("D", "88%"),
            ("E", "92%")
        ],
        "expl": "A probabilidade do evento complementar de A é definida por P(não A) = 1 − P(A). Como a probabilidade de selecionar um rádio com defeito de bateria é P(falha) = 8 / 50 = 0,16 (ou 16%), a probabilidade de o aparelho sorteado estar em perfeitas condições operacionais (não defeituoso) é 1 − 0,16 = 0,84, correspondendo a 84%."
    },
    {
        "seg": "a07/s03",
        "ans": "B",
        "stem": "Dois sistemas automáticos de alarme de incêndio, Alfa e Beta, monitoram um galpão logístico. A probabilidade de o sistema Alfa disparar em um simulado é de 70% e a probabilidade de Beta disparar é de 60%, ocorrendo o disparo conjunto de ambos em 45% dos ensaios. Assinale a opção que expressa a probabilidade de NENHUM dos dois sistemas disparar durante o simulado.",
        "opts": [
            ("A", "10%"),
            ("B", "15%"),
            ("C", "20%"),
            ("D", "25%"),
            ("E", "30%")
        ],
        "expl": "Pela lei de De Morgan para probabilidades, o evento correspondente a nenhum dos sistemas disparar equivale à interseção dos complementares (~Alfa ∩ ~Beta), cuja probabilidade é o complemento da união: P(~Alfa ∩ ~Beta) = 1 − P(Alfa ∪ Beta). Pelo teorema da união, P(Alfa ∪ Beta) = 0,70 + 0,60 − 0,45 = 0,85 (85%). Logo, a probabilidade de nenhum alarme disparar é 1 − 0,85 = 0,15, ou seja, 15%."
    },
    {
        "seg": "a07/s03",
        "ans": "A",
        "stem": "No âmbito da teoria axiomática da probabilidade formulada por Kolmogorov, assinale a opção que expressa uma afirmativa teoricamente CORRETA sobre os axiomas e suas propriedades derivadas.",
        "opts": [
            ("A", "Se dois eventos A e B são mutuamente excludentes, a probabilidade de sua união é igual à soma de suas probabilidades individuais."),
            ("B", "Um evento que possui probabilidade igual a zero é necessariamente um evento impossível sob qualquer modelo amostral contínuo."),
            ("C", "A probabilidade de ocorrência de qualquer evento simples em um espaço amostral discreto finito pode assumir valor estritamente superior a 1."),
            ("D", "Se um evento A está estritamente contido em um evento B, então a probabilidade de A é necessariamente estritamente superior à de B."),
            ("E", "A soma das probabilidades atribuídas a todos os pontos elementares de um espaço amostral discreto pode ser estritamente inferior a 1.")
        ],
        "expl": "O terceiro axioma fundamental de Kolmogorov estabelece que, se dois eventos A e B são mutuamente excludentes (disjuntos, com interseção vazia), a probabilidade da união é a soma das probabilidades: P(A ∪ B) = P(A) + P(B). Vale frisar que probabilidade zero não torna o evento ontologicamente impossível em espaços contínuos, probabilidades jamais superam 1 nem somam menos que 1 no espaço amostral, e a inclusão de eventos implica P(A) ≤ P(B)."
    },

    # --- a07/s04 (q121 a q123) ---
    {
        "seg": "a07/s04",
        "ans": "A",
        "stem": "Em um destacamento operacional com 100 bombeiros, há 60 socorristas (dos quais 45 atuam no plantão diurno e 15 no noturno) e 40 combatentes de incêndio (dos quais 20 atuam no plantão diurno e 20 no noturno). Sorteando-se um militar ao acaso e sabendo-se que ele atua no plantão noturno, assinale a opção que indica a probabilidade de ele ser um socorrista.",
        "opts": [
            ("A", "3/7"),
            ("B", "1/4"),
            ("C", "3/8"),
            ("D", "4/7"),
            ("E", "3/5")
        ],
        "expl": "A probabilidade condicional P(Socorrista | Noturno) restringe o universo amostral exclusivamente aos militares que atuam no plantão noturno. O número total de militares noturnos é 15 + 20 = 35. Dentre esses 35 integrantes, exatamente 15 são socorristas. Logo, P(Socorrista | Noturno) = 15 / 35 = 3/7."
    },
    {
        "seg": "a07/s04",
        "ans": "D",
        "stem": "Uma gaveta de evidências periciais contém 8 estojos de munição de calibre 9 mm e 4 estojos de calibre .40. Um perito retira sucessivamente e sem reposição 2 estojos dessa gaveta ao acaso. Assinale a opção que expressa a probabilidade de ambos os estojos retirados serem do calibre 9 mm.",
        "opts": [
            ("A", "7/22"),
            ("B", "8/33"),
            ("C", "12/33"),
            ("D", "14/33"),
            ("E", "16/33")
        ],
        "expl": "Pelo teorema da multiplicação de probabilidades para eventos dependentes (extração sem reposição), tem-se P(A ∩ B) = P(A) × P(B | A). Na primeira retirada, a probabilidade de selecionar munição 9 mm é 8 / 12 = 2/3. Havendo sucesso, restam na gaveta 7 munições de 9 mm em um total de 11 estojos, de modo que P(B | A) = 7 / 11. Multiplicando as probabilidades, obtém-se (2/3) × (7/11) = 14/33."
    },
    {
        "seg": "a07/s04",
        "ans": "C",
        "stem": "Um candidato a soldado do Corpo de Bombeiros submetido a uma prova de conhecimentos gerais sabe resolver com certeza 70% das questões do programa. Quando não sabe a resposta de uma questão, ele assinala ao acaso uma das 5 alternativas (chute aleatório com probabilidade de acerto de 1/5). Assinale a opção que indica a probabilidade de esse candidato acertar uma questão sorteada da prova por ter chutado a resposta.",
        "opts": [
            ("A", "2%"),
            ("B", "4%"),
            ("C", "6%"),
            ("D", "8%"),
            ("E", "14%")
        ],
        "expl": "O evento correspondente a acertar por meio de chute aleatório ocorre quando duas condições concomitantes se verificam: o candidato não sabe o conteúdo da questão E acerta a resposta escolhida ao acaso. A probabilidade de não saber o item é 1 − 0,70 = 0,30. Diante do desconhecimento, a probabilidade de acertar no chute entre 5 opções equiprováveis é 1/5 = 0,20. Pelo teorema da multiplicação, P(acertar por chute) = 0,30 × 0,20 = 0,06 (ou 6%)."
    },

    # --- a07/s05 (q124 a q127) ---
    {
        "seg": "a07/s05",
        "ans": "D",
        "stem": "Dois atiradores de elite do Batalhão de Operações Policiais Especiais disparam de forma independente contra um alvo distante. A probabilidade de o primeiro atirador atingir o alvo é de 0,80 e a do segundo atirador é de 0,90. Assinale a opção que apresenta a probabilidade de AMBOS os atiradores acertarem simultaneamente o alvo.",
        "opts": [
            ("A", "45%"),
            ("B", "50%"),
            ("C", "64%"),
            ("D", "72%"),
            ("E", "85%")
        ],
        "expl": "Sendo os disparos efetuados de forma estritamente independente, a ocorrência de acerto por parte de um dos policiais não altera a probabilidade de acerto do outro. Em tais circunstâncias, a probabilidade da interseção é dada diretamente pelo produto das probabilidades simples: P(A ∩ B) = P(A) × P(B) = 0,80 × 0,90 = 0,72 (72%)."
    },
    {
        "seg": "a07/s05",
        "ans": "E",
        "stem": "Um centro de comunicações do Corpo de Bombeiros opera com 3 geradores elétricos auxiliares independentes para garantir energia durante tempestades. A probabilidade de falha individual de cada um dos geradores em um determinado dia é de 10% (0,10). Assinale a opção que indica a probabilidade de PELO MENOS UM dos geradores funcionar adequadamente caso ocorra uma queda da rede elétrica principal.",
        "opts": [
            ("A", "90,0%"),
            ("B", "97,0%"),
            ("C", "98,5%"),
            ("D", "99,0%"),
            ("E", "99,9%")
        ],
        "expl": "A probabilidade de que pelo menos um componente opere com sucesso é calculada de forma direta pelo evento complementar correspondente à falha simultânea de todos os equipamentos: P(pelo menos um operar) = 1 − P(todos falharem). Sendo os geradores independentes, a probabilidade de os três falharem conjuntamente é 0,10 × 0,10 × 0,10 = 0,001. Logo, a probabilidade de funcionamento de pelo menos um gerador é 1 − 0,001 = 0,999 (99,9%)."
    },
    {
        "seg": "a07/s05",
        "ans": "D",
        "stem": "Sejam A e B dois eventos associados a um mesmo experimento aleatório tais que P(A) = 0,40, P(B) = 0,50 e P(A ∩ B) = 0,20. Sabendo que esses eventos são estocasticamente independentes, assinale a opção que indica a probabilidade de NÃO ocorrer A e NÃO ocorrer B simultaneamente.",
        "opts": [
            ("A", "10%"),
            ("B", "15%"),
            ("C", "20%"),
            ("D", "30%"),
            ("E", "50%")
        ],
        "expl": "Quando dois eventos A e B são independentes, os seus respectivos eventos complementares (~A e ~B) também são obrigatoriamente independentes. Assim, a probabilidade da interseção dos complementares é dada pelo produto de suas probabilidades individuais: P(~A ∩ ~B) = P(~A) × P(~B) = (1 − 0,40) × (1 − 0,50) = 0,60 × 0,50 = 0,30 (30%). De forma equivalente, pelas leis de De Morgan, tem-se 1 − P(A ∪ B) = 1 − (0,40 + 0,50 − 0,20) = 0,30."
    },
    {
        "seg": "a07/s05",
        "ans": "A",
        "stem": "Três eventos aleatórios A, B e C definidos no mesmo espaço de probabilidade são considerados mutuamente independentes se, e somente se, satisfizerem a certas condições matemáticas. Assinale a opção que expressa uma condição necessária e verdadeira acerca dessa independência.",
        "opts": [
            ("A", "A igualdade P(A ∩ B ∩ C) = P(A)P(B)P(C) é condição necessária, mas não suficiente por si só para garantir a independência mútua dos três eventos."),
            ("B", "A independência entre os pares (A, B) e (B, C) garante automaticamente e em qualquer caso a independência entre A e C."),
            ("C", "Se três eventos são independentes dois a dois, decorre necessariamente que eles formam um conjunto mutuamente independente."),
            ("D", "A independência de dois eventos impede terminantemente que os seus respectivos complementares sejam independentes."),
            ("E", "A interseção de três eventos independentes possui probabilidade identicamente nula em todos os modelos probabilísticos.")
        ],
        "expl": "Para que três eventos sejam mutuamente independentes, exige-se a validade simultânea de quatro igualdades: as três independências dois a dois [P(A ∩ B) = P(A)P(B), P(A ∩ C) = P(A)P(C), P(B ∩ C) = P(B)P(C)] e o produto triplo P(A ∩ B ∩ C) = P(A)P(B)P(C). Portanto, a igualdade do produto triplo isoladamente é necessária, porém insuficiente para atestar a independência conjunta, assim como a independência dois a dois não acarreta necessariamente a independência mútua nem possui transitividade."
    },

    # --- a07/s06 (q128 a q131) ---
    {
        "seg": "a07/s06",
        "ans": "E",
        "stem": "Três batalhões operacionais (B1, B2 e B3) respondem por 50%, 30% e 20% das ocorrências de combate a incêndio de uma região metropolitana, respectivamente. Auditorias técnicas indicam que a probabilidade de tempo de resposta superior a 15 minutos é de 4% no B1, 6% no B2 e 10% no B3. Selecionando-se aleatoriamente uma ocorrência atendida nessa região, assinale a opção que expressa a probabilidade total de ela ter registrado tempo de resposta superior a 15 minutos.",
        "opts": [
            ("A", "3,4%"),
            ("B", "4,2%"),
            ("C", "4,8%"),
            ("D", "5,0%"),
            ("E", "5,8%")
        ],
        "expl": "Pelo teorema da probabilidade total, a probabilidade global de uma ocorrência apresentar tempo de resposta superior a 15 minutos é calculada pela soma ponderada das probabilidades condicionais em cada batalhão: P(T) = P(B1)P(T | B1) + P(B2)P(T | B2) + P(B3)P(T | B3) = (0,50 × 0,04) + (0,30 × 0,06) + (0,20 × 0,10) = 0,020 + 0,018 + 0,020 = 0,058, o que equivale a 5,8%."
    },
    {
        "seg": "a07/s06",
        "ans": "C",
        "stem": "Em uma central pericial, 70% dos laudos são elaborados no formato eletrônico padronizado e 30% são redigidos no formato físico tradicional. A probabilidade de um laudo eletrônico necessitar de retificação técnica é de 5%, enquanto para os laudos físicos essa probabilidade sobe para 15%. Assinale a opção que indica a probabilidade de um laudo pericial selecionado ao acaso ser aprovado sem qualquer necessidade de retificação técnica.",
        "opts": [
            ("A", "84%"),
            ("B", "88%"),
            ("C", "92%"),
            ("D", "94%"),
            ("E", "96%")
        ],
        "expl": "Calcula-se inicialmente a probabilidade total de um laudo necessitar de retificação técnica: P(Retificação) = (0,70 × 0,05) + (0,30 × 0,15) = 0,035 + 0,045 = 0,080 (8%). Como a aprovação sem retificação é o evento complementar à necessidade de ajuste, aplica-se a subtração fundamental: P(Sem retificação) = 1 − 0,080 = 0,920, o que equivale a 92%."
    },
    {
        "seg": "a07/s06",
        "ans": "D",
        "stem": "Um teste sorológico rápido para detecção de substância tóxica em bombeiros resgatistas apresenta sensibilidade de 90% (detecta a substância em 90% dos indivíduos contaminados) e taxa de falsos positivos de 5% (acusa positivo em 5% dos não contaminados). Sabe-se que 10% dos militares expostos ao sinistro foram efetivamente contaminados. Diante de um militar que testou POSITIVO no exame rápido, assinale a opção que expressa a probabilidade de ele estar de fato contaminado.",
        "opts": [
            ("A", "1/3"),
            ("B", "1/2"),
            ("C", "3/5"),
            ("D", "2/3"),
            ("E", "4/5")
        ],
        "expl": "Aplicando o Teorema de Bayes para inverter o condicionamento e determinar a probabilidade a posteriori P(Contaminado | Positivo), divide-se a probabilidade conjunta favorável pela probabilidade total de resultado positivo. O numerador é P(+ ∩ C) = P(+ | C) × P(C) = 0,90 × 0,10 = 0,090. O denominador é P(+) = (0,90 × 0,10) + (0,05 × 0,90) = 0,090 + 0,045 = 0,135. Logo, P(C | +) = 0,090 / 0,135 = 90 / 135 = 2/3 (aproximadamente 66,7%)."
    },
    {
        "seg": "a07/s06",
        "ans": "E",
        "stem": "Três delegacias (D1, D2 e D3) encaminham inquéritos para um núcleo de perícia forense nas proporções de 50%, 30% e 20% do volume total, respectivamente. A taxa histórica de inquéritos que necessitam de diligências complementares é de 2% para D1, 4% para D2 e 6% para D3. Sabendo que um inquérito sorteado ao acaso no núcleo necessitou de diligências complementares, assinale a opção que apresenta a probabilidade de ele ter sido originado na delegacia D3.",
        "opts": [
            ("A", "1/17"),
            ("B", "2/17"),
            ("C", "3/17"),
            ("D", "5/17"),
            ("E", "6/17")
        ],
        "expl": "Pelo Teorema de Bayes, a probabilidade a posteriori de a investigação ter origem na delegacia D3 dado que exigiu complementação pericial é P(D3 | C) = P(D3 ∩ C) / P(C). A probabilidade conjunta para D3 é 0,20 × 0,06 = 0,012. A probabilidade total no denominador é (0,50 × 0,02) + (0,30 × 0,04) + (0,20 × 0,06) = 0,010 + 0,012 + 0,012 = 0,034. A razão fornece 0,012 / 0,034 = 12 / 34 = 6/17."
    }
]
