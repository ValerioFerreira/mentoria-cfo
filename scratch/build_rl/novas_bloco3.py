"""Bloco 3 das novas questoes de Raciocinio Logico (33 questoes: q77 a q109).
Trechos: a06/s01 (2), a06/s02 (4), a06/s03 (4), a06/s04 (4),
         a06/s05 (4), a06/s06 (5), a06/s07 (5), a06/s08 (5).
Gabaritos extraidos estritamente de gabaritos_132.json (indices 77 a 109):
['B', 'D', 'E', 'D', 'E', 'C', 'D', 'C', 'D', 'A', 'C', 'D', 'D', 'B', 'E', 'D', 'C', 'D', 'E', 'B', 'B', 'C', 'B', 'E', 'D', 'A', 'A', 'E', 'A', 'A', 'B', 'A', 'D']
"""

QUESTOES_BLOCO3 = [
    # --- a06/s01 (q77 a q78) ---
    {
        "seg": "a06/s01",
        "ans": "B",
        "stem": "Um centro de operações integradas de segurança pública precisa criar códigos de identificação para ocorrências emergenciais. Cada código é formado por 2 letras distintas escolhidas entre as 5 primeiras letras do alfabeto (A, B, C, D, E) seguidas por 3 algarismos distintos escolhidos entre os algarismos pares não nulos (2, 4, 6, 8). Assinale a opção que indica o número total de códigos distintos que podem ser gerados.",
        "opts": [
            ("A", "360"),
            ("B", "480"),
            ("C", "600"),
            ("D", "720"),
            ("E", "960")
        ],
        "expl": "Pelo princípio fundamental da contagem (princípio multiplicativo), multiplica-se a quantidade de escolhas possíveis em cada etapa sucessiva. Para as letras distintas, há 5 opções para a primeira posição e 4 para a segunda, resultando em 5 × 4 = 20 arranjos. Para os algarismos pares distintos em {2, 4, 6, 8}, há 4 possibilidades para a primeira vaga, 3 para a segunda e 2 para a terceira, totalizando 4 × 3 × 2 = 24 arranjos. O número total de códigos possíveis é 20 × 24 = 480."
    },
    {
        "seg": "a06/s01",
        "ans": "D",
        "stem": "Na organização de arquivos de custódia de vestígios periciais, um perito precisa dividir 720 laudos idênticos em lotes de tamanhos iguais, de modo que cada lote contenha uma quantidade inteira de laudos, sem sobras. Assinale a opção que expressa o número total de divisores positivos de 720 que determinam os possíveis tamanhos de lote.",
        "opts": [
            ("A", "18"),
            ("B", "24"),
            ("C", "28"),
            ("D", "30"),
            ("E", "36")
        ],
        "expl": "Para encontrar a quantidade de divisores inteiros positivos de um número natural, realiza-se a decomposição em fatores primos. Tem-se 720 = 2^4 × 3^2 × 5^1. Aplicando a regra prática da contagem de divisores, adiciona-se uma unidade a cada expoente da forma canônica e efetua-se a multiplicação dos fatores obtidos: (4 + 1) × (2 + 1) × (1 + 1) = 5 × 3 × 2 = 30 divisores positivos."
    },

    # --- a06/s02 (q79 a q82) ---
    {
        "seg": "a06/s02",
        "ans": "E",
        "stem": "Uma equipe de busca e salvamento do Corpo de Bombeiros pode ser acionada para atender uma emergência em terreno montanhoso ou em ambiente aquático. Para missões em montanha, o comando dispõe de 4 guias especializados e 3 operadores de rapel (a equipe é formada por 1 guia e 1 operador). Para missões aquáticas, o comando dispõe de 5 mergulhadores e 2 pilotos de embarcação (a equipe é formada por 1 mergulhador e 1 piloto). Considerando que uma mesma ocorrência é exclusivamente terrestre ou aquática, assinale a opção que indica o número total de composições de equipe distintas que o comando pode formar para atender ao chamado.",
        "opts": [
            ("A", "12"),
            ("B", "14"),
            ("C", "18"),
            ("D", "20"),
            ("E", "22")
        ],
        "expl": "Para as missões em ambiente montanhoso, a formação de equipe com 1 guia e 1 operador de rapel resulta em 4 × 3 = 12 composições pelo princípio multiplicativo. Para as missões em ambiente aquático, a composição com 1 mergulhador e 1 piloto resulta em 5 × 2 = 10 possibilidades. Como os dois tipos de missão são mutuamente exclusivos (a ocorrência é montanhosa ou aquática), aplica-se o princípio aditivo somando as alternativas: 12 + 10 = 22 equipes distintas."
    },
    {
        "seg": "a06/s02",
        "ans": "D",
        "stem": "Em uma academia de formação militar, os cadetes estão distribuídos em 4 pelotões distintos (Alfa, Bravo, Charlie e Delta). O instrutor-chefe deseja selecionar um grupo de cadetes para uma comissão técnica. Assinale a opção que indica o número mínimo de cadetes que devem ser convocados ao acaso para que se garanta, com certeza absoluta, a presença de pelo menos 5 cadetes pertencentes a um mesmo pelotão.",
        "opts": [
            ("A", "13"),
            ("B", "15"),
            ("C", "16"),
            ("D", "17"),
            ("E", "21")
        ],
        "expl": "Pelo princípio das gavetas de Dirichlet (casa dos pombos), avalia-se o cenário de máxima dispersão desfavorável. Para não se obter 5 cadetes de um mesmo pelotão, o pior cenário consiste em convocar exatamente 4 cadetes de cada um dos 4 pelotões, acumulando 4 × 4 = 16 cadetes. Qualquer cadete adicional convocado (o 17º militar) pertencerá compulsoriamente a um dos pelotões já preenchidos com 4 integrantes, completando 5 membros do mesmo grupo."
    },
    {
        "seg": "a06/s02",
        "ans": "E",
        "stem": "O departamento esportivo de uma corporação militar organizou um campeonato interno de tiro prático no formato de eliminatória simples (mata-mata), no qual cada confronto elimina exatamente um competidor e não há empates. Inscreveram-se na competição exatamente 48 policiais. Assinale a opção que apresenta o número total de disputas necessárias para sagrar o campeão do torneio.",
        "opts": [
            ("A", "24"),
            ("B", "36"),
            ("C", "44"),
            ("D", "46"),
            ("E", "47")
        ],
        "expl": "Em um torneio disputado pelo sistema de eliminatória simples, cada confronto realizado elimina taxativamente um competidor. Como o torneio culmina com um único campeão invicto, devem ser eliminados ao longo de todas as fases exatamente N − 1 competidores. Portanto, para N = 48 atletas inscritos, realizam-se obrigatoriamente 48 − 1 = 47 partidas, independentemente do chaveamento e de eventuais folgas."
    },
    {
        "seg": "a06/s02",
        "ans": "C",
        "stem": "Um analista de inteligência precisa calcular o valor exato da expressão aritmética E = (10! × 4!) / (8! × 5!) para ajustar parâmetros de um algoritmo criptográfico. Assinale a opção que apresenta o resultado correto dessa operação.",
        "opts": [
            ("A", "12"),
            ("B", "15"),
            ("C", "18"),
            ("D", "20"),
            ("E", "24")
        ],
        "expl": "Desdobrando os fatoriais para simplificar termos correspondentes no numerador e denominador, reescreve-se 10! como 10 × 9 × 8! e 5! como 5 × 4!. Substituindo esses termos na expressão original, tem-se (10 × 9 × 8! × 4!) / (8! × 5 × 4!). Simplificando os fatores comuns 8! e 4!, resta a fração (10 × 9) / 5 = 90 / 5 = 18."
    },

    # --- a06/s03 (q83 a q86) ---
    {
        "seg": "a06/s03",
        "ans": "D",
        "stem": "Cinco viaturas operacionais identificadas pelas siglas V1, V2, V3, V4 e V5 devem ser estacionadas lado a lado em uma fileira de 5 vagas demarcadas. Por razões táticas de pronta resposta, as viaturas V1 e V2 devem permanecer sempre em vagas adjacentes (juntas), em qualquer ordem entre si. Assinale a opção que indica o número de maneiras distintas de posicionar as cinco viaturas.",
        "opts": [
            ("A", "24"),
            ("B", "36"),
            ("C", "40"),
            ("D", "48"),
            ("E", "60")
        ],
        "expl": "Agrupam-se as viaturas V1 e V2 como um único elemento representativo em bloco. Dessa forma, permuta-se um total de 4 elementos (o bloco integrado e as outras 3 viaturas individuais), o que fornece 4! = 24 disposições. Como a ordem interna entre V1 e V2 dentro do bloco pode variar livremente (2! = 2 maneiras), multiplica-se 24 × 2 = 48 configurações possíveis."
    },
    {
        "seg": "a06/s03",
        "ans": "C",
        "stem": "Uma guarnição de bombeiros formada por 4 homens e 3 mulheres deve se organizar em uma fila indiana de 7 posições para uma cerimônia solene, de modo que homens e mulheres fiquem estritamente intercalados (alternados). Assinale a opção que apresenta o número total de ordens distintas em que essa fila pode ser formada.",
        "opts": [
            ("A", "72"),
            ("B", "96"),
            ("C", "144"),
            ("D", "288"),
            ("E", "576")
        ],
        "expl": "Para haver alternância perfeita entre 4 homens e 3 mulheres ao longo de 7 posições, a fila deve iniciar e terminar compulsoriamente com um homem (ocupando as posições ímpares 1ª, 3ª, 5ª e 7ª), enquanto as mulheres ocupam as posições pares (2ª, 4ª e 6ª). A permutação dos 4 homens nos seus postos corresponde a 4! = 24 e a das 3 mulheres corresponde a 3! = 6. O produto multiplicativo resulta em 24 × 6 = 144 filas distintas."
    },
    {
        "seg": "a06/s03",
        "ans": "D",
        "stem": "Oito oficiais superiores devem compor a bancada principal de uma solenidade, ocupando 8 assentos enfileirados numerados de 1 a 8. O Comandante-Geral e o Subcomandante-Geral devem ocupar obrigatoriamente as pontas da fileira (assentos 1 e 8), em qualquer ordem entre si. Assinale a opção que indica de quantas maneiras distintas os oito oficiais podem ser distribuídos nesses assentos.",
        "opts": [
            ("A", "720"),
            ("B", "1080"),
            ("C", "1200"),
            ("D", "1440"),
            ("E", "2880")
        ],
        "expl": "Para os assentos extremos de números 1 e 8, há 2 possibilidades para o assento 1 e 1 para o assento 8, gerando 2! = 2 maneiras de posicionar os dois oficiais de comando. Os 6 assentos intermediários restantes são preenchidos pelos demais 6 oficiais em qualquer ordem, correspondendo a 6! = 720 ordenações. Pelo princípio multiplicativo, obtém-se 2 × 720 = 1.440 maneiras distintas."
    },
    {
        "seg": "a06/s03",
        "ans": "A",
        "stem": "Durante uma vistoria técnica de prevenção contra incêndio, 6 extintores distintos de diferentes classes de fogo devem ser alinhados em um suporte horizontal. Foi estabelecido que 3 extintores específicos de água pressurizada devem permanecer rigorosamente agrupados em uma sequência predeterminada e imutável. Assinale a opção que expressa a quantidade de disposições distintas que esses 6 extintores podem assumir no suporte.",
        "opts": [
            ("A", "24"),
            ("B", "48"),
            ("C", "72"),
            ("D", "120"),
            ("E", "144")
        ],
        "expl": "Como os 3 extintores específicos devem figurar agrupados em uma sequência com ordem interna fixa e congelada, o trio atua como um único bloco indivisível com apenas 1 configuração interna. Reunindo esse bloco aos outros 3 extintores remanescentes, tem-se um total de 4 elementos para permutar em linha: (6 − 3 + 1)! = 4! = 24 disposições distintas."
    },

    # --- a06/s04 (q87 a q90) ---
    {
        "seg": "a06/s04",
        "ans": "C",
        "stem": "Um sistema de radiocomunicação utiliza palavras-código para transmissão de alertas meteorológicos à Defesa Civil. Um dos códigos criptográficos é formado por todos os anagramas possíveis da palavra RESGATE. Sabendo que todas as letras são utilizadas em cada anagrama, assinale a opção que indica o total de códigos distintos que podem ser formados.",
        "opts": [
            ("A", "840"),
            ("B", "1260"),
            ("C", "2520"),
            ("D", "5040"),
            ("E", "10080")
        ],
        "expl": "A palavra RESGATE contém 7 letras no total, apresentando repetição de 2 ocorrências da vogal 'E' e demais caracteres R, S, G, A, T distintos. A quantidade de anagramas únicos é calculada por meio da permutação com repetição: P_7^(2) = 7! / 2! = 5.040 / 2 = 2.520 códigos distintos."
    },
    {
        "seg": "a06/s04",
        "ans": "D",
        "stem": "Uma equipe de gerenciamento de crises da Segurança Pública composta por 6 negociadores reúne-se ao redor de uma mesa redonda para planejar a atuação em um incidente tático. Sabendo que duas disposições são equivalentes quando podem ser obtidas por simples rotação da mesa, assinale a opção que indica o número de maneiras distintas em que os negociadores podem se sentar.",
        "opts": [
            ("A", "24"),
            ("B", "48"),
            ("C", "60"),
            ("D", "120"),
            ("E", "720")
        ],
        "expl": "Em arranjos circulares sem marcos espaciais externos fixos, giros da mesa preservam a posição relativa mútua entre os integrantes. Para calcular as permutações circulares, fixa-se um dos 6 indivíduos como referencial arbitrário e permutam-se os demais 5 ao longo dos assentos: PC_6 = (6 − 1)! = 5! = 120 maneiras distintas."
    },
    {
        "seg": "a06/s04",
        "ans": "D",
        "stem": "Três peritos criminais e três delegados de polícia participam de uma reunião de alinhamento operacional em uma mesa circular com 6 cadeiras equidistantes. Para favorecer a integração entre as especialidades, determinou-se que delegados e peritos devem se sentar em posições alternadas. Assinale a opção que expressa o número de maneiras distintas de dispor esses profissionais à mesa.",
        "opts": [
            ("A", "4"),
            ("B", "6"),
            ("C", "8"),
            ("D", "12"),
            ("E", "36")
        ],
        "expl": "A organização em círculo com alternância estrita entre dois grupos é estruturada em duas fases. Primeiro, dispõem-se os 3 delegados em torno da mesa circular, gerando PC_3 = (3 − 1)! = 2! = 2 maneiras. Definidos os lugares dos delegados, criam-se 3 posições intermediárias perfeitamente diferenciadas pela vizinhança para os 3 peritos, admitindo 3! = 6 permutações lineares. O produto fornece 2 × 6 = 12 arranjos."
    },
    {
        "seg": "a06/s04",
        "ans": "B",
        "stem": "Cinco viaturas táticas identificadas por A, B, C, D e E partem do batalhão em comboio, uma atrás da outra. Em razão do plano de operações, foi estabelecido que a viatura A deve obrigatoriamente trafegar à frente da viatura B, e a viatura B deve trafegar à frente da viatura C no comboio (não necessariamente em posições imediatamente consecutivas). Assinale a opção que indica o número de ordenações possíveis para esse comboio.",
        "opts": [
            ("A", "10"),
            ("B", "20"),
            ("C", "30"),
            ("D", "40"),
            ("E", "60")
        ],
        "expl": "O total de ordenações lineares sem restrições para as 5 viaturas é 5! = 120. Em qualquer ordenação arbitrária, as 3 viaturas A, B e C admitem 3! = 6 ordenações relativas mutuamente exclusivas e equiprováveis. Como exatamente uma dessas 6 ordenações relativas satisfaz a hierarquia imposta (A antes de B e B antes de C), divide-se o número total pelo número de permutações internas do trio: 5! / 3! = 120 / 6 = 20 ordenações possíveis."
    },

    # --- a06/s05 (q91 a q94) ---
    {
        "seg": "a06/s05",
        "ans": "E",
        "stem": "Quatro agentes de trânsito realizaram um sorteio interno para inspecionar os postos de fiscalização da cidade, de modo que cada um deveria fiscalizar um posto diferente do posto em que atua habitualmente. Assinale a opção que apresenta o número de maneiras distintas pelas quais esses quatro agentes podem ser redistribuídos sem que nenhum deles permaneça em seu posto habitual.",
        "opts": [
            ("A", "3"),
            ("B", "4"),
            ("C", "6"),
            ("D", "8"),
            ("E", "9")
        ],
        "expl": "A redistribuição de elementos de modo que nenhum ocupe sua posição original é a definição clássica de permutação caótica ou desarranjo. Para n = 4 elementos, a fórmula de desarranjo é dada por D_4 = 4! × [1/2! − 1/3! + 1/4!] = 24 × (1/2 − 1/6 + 1/24) = 12 − 4 + 1 = 9 maneiras distintas."
    },
    {
        "seg": "a06/s05",
        "ans": "D",
        "stem": "Em um destacamento militar composto por 7 oficiais qualificados, o comandante precisa designar 3 deles para desempenharem, respectivamente, as funções distintas de Chefe de Operações, Oficial de Inteligência e Coordenador de Logística. Assinale a opção que indica a quantidade de maneiras distintas pelas quais essas atribuições podem ser preenchidas.",
        "opts": [
            ("A", "35"),
            ("B", "70"),
            ("C", "140"),
            ("D", "210"),
            ("E", "420")
        ],
        "expl": "Como as três vagas a preencher correspondem a funções técnicas diferenciadas e com responsabilidades específicas, a ordem da escolha altera substancialmente o resultado prático da nomeação. Trata-se, portanto, de um arranjo simples de 7 elementos tomados 3 a 3: A(7, 3) = 7! / (7 − 3)! = 7 × 6 × 5 = 210 maneiras distintas."
    },
    {
        "seg": "a06/s05",
        "ans": "C",
        "stem": "Uma seção técnica de combate a incêndios dispõe de 8 bombeiros militares aptos. O oficial de dia precisa selecionar uma equipe de 3 militares para realizar uma vistoria em uma edificação comercial, sem distinção de funções entre os membros selecionados. Assinale a opção que apresenta o total de equipes distintas que podem ser formadas.",
        "opts": [
            ("A", "24"),
            ("B", "48"),
            ("C", "56"),
            ("D", "112"),
            ("E", "336")
        ],
        "expl": "Como todos os militares desempenharão papéis equivalentes na vistoria e não há distinção de cargos internos na equipe, a ordem dos elementos selecionados é totalmente irrelevante. Configura-se uma combinação simples de 8 elementos tomados 3 a 3: C(8, 3) = (8 × 7 × 6) / (3 × 2 × 1) = 56 equipes distintas."
    },
    {
        "seg": "a06/s05",
        "ans": "D",
        "stem": "Um grupo de voluntários da Defesa Civil é composto por 5 médicos e 4 enfermeiros. Para uma missão de apoio emergencial em área de desastre, deve ser formada uma brigada de saúde com 3 profissionais. Assinale a opção que expressa o número de brigadas distintas que podem ser constituídas contendo pelo menos um médico.",
        "opts": [
            ("A", "64"),
            ("B", "70"),
            ("C", "76"),
            ("D", "80"),
            ("E", "84")
        ],
        "expl": "A contagem de seleções contendo 'pelo menos um' elemento de determinado grupo é efetuada calculando o total irrestrito de comissões e subtraindo as comissões formadas exclusivamente pelo outro grupo. O total de combinações de 3 profissionais escolhidos entre os 9 integrantes é C(9, 3) = (9 × 8 × 7) / 6 = 84. As comissões sem nenhum médico (compostas apenas por 3 enfermeiros escolhidos entre os 4) somam C(4, 3) = 4. Logo, a resposta é 84 − 4 = 80 brigadas."
    },

    # --- a06/s06 (q95 a q99) ---
    {
        "seg": "a06/s06",
        "ans": "E",
        "stem": "Uma equipe de perícia possui 7 equipamentos portáteis de medição distintos. Um perito pode selecionar qualquer subconjunto não vazio desses instrumentos para levar a campo em uma inspeção técnica. Assinale a opção que indica o número total de composições de kits de medição distintos que podem ser formados.",
        "opts": [
            ("A", "35"),
            ("B", "63"),
            ("C", "64"),
            ("D", "120"),
            ("E", "127")
        ],
        "expl": "O número total de subconjuntos de um conjunto com 7 elementos distintos é expresso pela soma dos coeficientes binomiais de ordem 0 a 7, equivalendo a 2^7 = 128 (teorema das linhas do triângulo de Pascal). Como a condição imposta exige kits não vazios, desconta-se a única combinação de ordem zero correspondente a nenhum instrumento selecionado (C(7, 0) = 1), restando 128 − 1 = 127 composições possíveis."
    },
    {
        "seg": "a06/s06",
        "ans": "B",
        "stem": "No desenvolvimento de um modelo analítico para distribuição de viaturas, utilizam-se propriedades do triângulo de Pascal. Pela relação fundamental de Stifel, assinale a opção que expressa a simplificação correta da soma dos binomiais C(11, 4) + C(11, 5).",
        "opts": [
            ("A", "C(12, 4)"),
            ("B", "C(12, 5)"),
            ("C", "C(22, 9)"),
            ("D", "C(11, 9)"),
            ("E", "C(13, 5)")
        ],
        "expl": "A relação de Stifel estipula que a soma de dois números binomiais consecutivos situados na mesma linha n do triângulo de Pascal é igual ao número binomial localizado na linha imediatamente subsequente n + 1 e na coluna de maior índice. Formalmente, C(n, k) + C(n, k + 1) = C(n + 1, k + 1). Aplicando a regra para n = 11 e k = 4, obtém-se diretamente C(11 + 1, 4 + 1) = C(12, 5)."
    },
    {
        "seg": "a06/s06",
        "ans": "B",
        "stem": "Uma força-tarefa de combate a queimadas florestais deve ser composta por exatamente 2 bombeiros militares (escolhidos entre 6 disponíveis), 2 policiais ambientais (escolhidos entre 5 disponíveis) e 1 perito florestal (escolhido entre 3 disponíveis). Assinale a opção que indica o número de maneiras distintas de constituir essa força-tarefa.",
        "opts": [
            ("A", "360"),
            ("B", "450"),
            ("C", "540"),
            ("D", "600"),
            ("E", "900")
        ],
        "expl": "Determina-se o número de combinações simples em cada categoria funcional e realiza-se a multiplicação dos resultados parciais pelo princípio fundamental da contagem. Para os bombeiros militares, há C(6, 2) = 15 opções; para os policiais ambientais, há C(5, 2) = 10 opções; para o perito florestal, há C(3, 1) = 3 opções. O número de composições possíveis da força-tarefa é 15 × 10 × 3 = 450."
    },
    {
        "seg": "a06/s06",
        "ans": "C",
        "stem": "Uma unidade de resgate precisa adquirir 4 cilindros de oxigênio hospitalar, podendo escolher entre 3 marcas homologadas (A, B e C), sem qualquer restrição de quantidade por fabricante e admitindo a repetição de marcas. Assinale a opção que expressa a quantidade de maneiras distintas em que esse lote de 4 cilindros pode ser adquirido.",
        "opts": [
            ("A", "9"),
            ("B", "12"),
            ("C", "15"),
            ("D", "20"),
            ("E", "35")
        ],
        "expl": "Trata-se de um problema clássico de combinação com repetição (combinação completa) de p = 4 objetos escolhidos entre n = 3 categorias distintas. Pelo método das divisórias (barras e estrelas), a fórmula é dada por CR(n, p) = C(n + p − 1, p). Para n = 3 marcas e p = 4 cilindros, tem-se C(3 + 4 − 1, 4) = C(6, 4) = C(6, 2) = (6 × 5) / 2 = 15 maneiras distintas."
    },
    {
        "seg": "a06/s06",
        "ans": "B",
        "stem": "O comando de um batalhão de bombeiros recebeu uma doação de 10 lanternas táticas idênticas para distribuir entre 3 postos avançados de salvamento, de modo que cada posto receba obrigatoriamente pelo menos 2 lanternas. Assinale a opção que indica de quantas maneiras distintas essas 10 lanternas podem ser distribuídas entre os três postos.",
        "opts": [
            ("A", "10"),
            ("B", "15"),
            ("C", "21"),
            ("D", "28"),
            ("E", "36")
        ],
        "expl": "Havendo uma exigência mínima por destinatário, distribui-se de início a quantidade obrigatória e calcula-se a partilha livre do saldo remanescente. Destinando previamente 2 lanternas a cada um dos 3 postos avançados (consumindo 2 × 3 = 6 lanternas), sobram 10 − 6 = 4 lanternas idênticas para serem divididas livremente entre os 3 postos. Isso equivale à combinação completa CR(3, 4) = C(3 + 4 − 1, 4) = C(6, 4) = 15 maneiras."
    },

    # --- a06/s07 (q100 a q104) ---
    {
        "seg": "a06/s07",
        "ans": "E",
        "stem": "Considere a equação linear x + y + z + w = 7. Assinale a opção que indica o número de soluções inteiras e não negativas (com x, y, z, w pertencentes ao conjunto dos números naturais incluindo o zero) que satisfazem a essa igualdade.",
        "opts": [
            ("A", "36"),
            ("B", "64"),
            ("C", "84"),
            ("D", "100"),
            ("E", "120")
        ],
        "expl": "A quantidade de soluções inteiras não negativas de uma equação linear com soma constante corresponde ao cálculo da combinação com repetição. Para n = 4 variáveis e soma p = 7, aplica-se a relação CR(n, p) = C(n + p − 1, p) = C(4 + 7 − 1, 7) = C(10, 7) = C(10, 3) = (10 × 9 × 8) / (3 × 2 × 1) = 120 soluções inteiras não negativas."
    },
    {
        "seg": "a06/s07",
        "ans": "D",
        "stem": "Um oficial de logística dispõe de 8 kits de primeiros socorros idênticos para repartir entre 3 viaturas de resgate, de tal forma que cada viatura receba pelo menos um kit. Assinale a opção que apresenta o número de maneiras distintas de realizar essa divisão.",
        "opts": [
            ("A", "12"),
            ("B", "15"),
            ("C", "18"),
            ("D", "21"),
            ("E", "28")
        ],
        "expl": "A distribuição de 8 objetos idênticos entre 3 entidades com a exigência de que cada uma receba ao menos uma unidade equivale a encontrar o número de soluções inteiras estritamente positivas da equação x + y + z = 8. Alocando previamente 1 unidade para cada entidade, restam 8 − 3 = 5 unidades para partilha livre entre as 3 variáveis, fornecendo CR(3, 5) = C(3 + 5 − 1, 5) = C(7, 5) = C(7, 2) = (7 × 6) / 2 = 21 maneiras distintas."
    },
    {
        "seg": "a06/s07",
        "ans": "A",
        "stem": "Oito peritos criminais recém-empossados devem ser distribuídos em três delegacias especializadas: 4 serão designados para a Delegacia de Homicídios, 2 para a Delegacia de Defraudações e 2 para a Delegacia do Meio Ambiente. Assinale a opção que expressa o total de distribuições distintas possíveis.",
        "opts": [
            ("A", "420"),
            ("B", "560"),
            ("C", "840"),
            ("D", "1260"),
            ("E", "1680")
        ],
        "expl": "Como os grupos de destino possuem identidades e atribuições institucionais perfeitamente diferenciadas (Homicídios, Defraudações e Meio Ambiente), configura-se uma partição ordenada. Pela fórmula do coeficiente multinomial, calcula-se n! / (p1! × p2! × p3!) = 8! / (4! × 2! × 2!) = 40.320 / (24 × 2 × 2) = 40.320 / 96 = 420 maneiras distintas de realizar a lotação dos peritos."
    },
    {
        "seg": "a06/s07",
        "ans": "A",
        "stem": "Seis bombeiros militares devem ser divididos em três duplas de socorristas para patrulhar simultaneamente três setores operacionais idênticos, sem qualquer distinção entre as duplas formadas. Assinale a opção que indica de quantas maneiras distintas essas duplas podem ser constituídas.",
        "opts": [
            ("A", "15"),
            ("B", "30"),
            ("C", "45"),
            ("D", "60"),
            ("E", "90")
        ],
        "expl": "A partição de 6 pessoas em 3 grupos de 2 integrantes sem rótulos, nomes ou diferenciação funcional é uma partição não ordenada. Calcula-se primeiramente a partição ordenada 6! / (2! × 2! × 2!) = 720 / 8 = 90. Em seguida, divide-se pela permutação dos 3 grupos idênticos (3! = 6) para eliminar as contagens redundantes geradas pela troca de ordem entre as duplas, obtendo-se 90 / 6 = 15 maneiras."
    },
    {
        "seg": "a06/s07",
        "ans": "E",
        "stem": "Dez soldados do Corpo de Bombeiros devem ser organizados para um exercício tático em dois grupos de 5 integrantes cada, sendo ambos os grupos de mesma hierarquia e atribuições rigorosamente equivalentes. Assinale a opção que apresenta o número de maneiras distintas de realizar essa divisão.",
        "opts": [
            ("A", "42"),
            ("B", "63"),
            ("C", "84"),
            ("D", "105"),
            ("E", "126")
        ],
        "expl": "Ao dividir 10 elementos em dois grupos equivalentes de 5 pessoas sem identificação entre os grupos, trata-se de partição não ordenada de conjuntos. A seleção de 5 pessoas entre 10 para o primeiro grupo fornece C(10, 5) = 252 combinações. Como a escolha de um grupo automaticamente determina o outro e ambos são equivalentes, cada partição foi calculada duas vezes. Dividindo por 2! = 2, obtém-se 252 / 2 = 126 maneiras distintas."
    },

    # --- a06/s08 (q105 a q109) ---
    {
        "seg": "a06/s08",
        "ans": "A",
        "stem": "Um pelotão possui 7 postos de vigia enfileirados ao longo de um muro perimetral, identificados de 1 a 7. O comandante da guarda deseja posicionar sentinelas em 3 desses postos, com a restrição tática de que não haja postos adjacentes (vizinhos) simultaneamente ocupados. Pelo Primeiro Lema de Kaplansky, assinale a opção que indica o número de maneiras distintas de escolher os 3 postos.",
        "opts": [
            ("A", "10"),
            ("B", "15"),
            ("C", "20"),
            ("D", "25"),
            ("E", "35")
        ],
        "expl": "O Primeiro Lema de Kaplansky determina que o número de subconjuntos de p elementos não consecutivos escolhidos entre n elementos dispostos linearmente em fila é dado por f(n, p) = C(n − p + 1, p). Para n = 7 postos e p = 3 sentinelas, calcula-se C(7 − 3 + 1, 3) = C(5, 3) = (5 × 4) / 2 = 10 maneiras distintas de escolha."
    },
    {
        "seg": "a06/s08",
        "ans": "A",
        "stem": "Um sargento deve escalar um soldado para cumprir 3 plantões durante a semana, escolhendo entre os dias de segunda-feira a sábado (total de 6 dias úteis seguidos). Para evitar a sobrecarga física do militar, foi estabelecido que ele não pode cumprir plantão em dois dias consecutivos. Assinale a opção que apresenta o número de escalas possíveis que atendem a essa restrição.",
        "opts": [
            ("A", "4"),
            ("B", "6"),
            ("C", "8"),
            ("D", "10"),
            ("E", "12")
        ],
        "expl": "Como o período analisado compreende 6 dias dispostos em sequência linear (de segunda a sábado) e o militar não pode atuar em dias adjacentes, aplica-se o Primeiro Lema de Kaplansky com n = 6 e p = 3 plantões. A fórmula fornece f(6, 3) = C(6 − 3 + 1, 3) = C(4, 3) = 4 escalas possíveis."
    },
    {
        "seg": "a06/s08",
        "ans": "B",
        "stem": "Em uma linha reta de proteção patrimonial, há 6 sensores de presença alinhados numerados de 1 a 6. O sistema pode operar com exatamente 2 sensores ativados simultaneamente, desde que nenhum par de sensores ativados seja vizinho imediato. Assinale a opção que indica de quantas maneiras distintas esses 2 sensores podem ser ativados.",
        "opts": [
            ("A", "8"),
            ("B", "10"),
            ("C", "12"),
            ("D", "14"),
            ("E", "15")
        ],
        "expl": "A escolha de 2 elementos não consecutivos entre 6 elementos em disposição linear é dada pelo Primeiro Lema de Kaplansky: f(n, p) = C(n − p + 1, p). Para n = 6 e p = 2, tem-se C(6 − 2 + 1, 2) = C(5, 2) = (5 × 4) / 2 = 10 maneiras. Pode-se também subtrair do total de pares C(6, 2) = 15 os 5 pares consecutivos vizinhos (1-2, 2-3, 3-4, 4-5, 5-6), resultando em 15 − 5 = 10."
    },
    {
        "seg": "a06/s08",
        "ans": "A",
        "stem": "Oito postos de observação militar estão dispostos em círculo ao redor de um heliponto. O comandante deseja selecionar 3 postos para vigilância noturna de tal modo que não haja dois postos vizinhos no círculo selecionados simultaneamente. Pelo Segundo Lema de Kaplansky, assinale a opção que expressa o total de escolhas possíveis.",
        "opts": [
            ("A", "16"),
            ("B", "20"),
            ("C", "24"),
            ("D", "28"),
            ("E", "32")
        ],
        "expl": "Para selecionar p elementos não consecutivos entre n elementos distribuídos ao longo de uma circunferência fechada (em que o primeiro e o último são adjacentes), emprega-se o Segundo Lema de Kaplansky: g(n, p) = [n / (n − p)] × C(n − p, p). Para n = 8 e p = 3, obtém-se [8 / (8 − 3)] × C(8 − 3, 3) = (8 / 5) × C(5, 3) = (8 / 5) × 10 = 16 escolhas possíveis."
    },
    {
        "seg": "a06/s08",
        "ans": "D",
        "stem": "Uma escala de ronda noturna cobre os 7 dias completos da semana (de domingo a sábado, em ciclo circular ininterrupto em que sábado é contíguo a domingo). Um agente deve ser escalado para 2 noites de plantão nessa semana, sem que os dois plantões ocorram em dias consecutivos no ciclo. Assinale a opção que indica o número de opções de escala para esse agente.",
        "opts": [
            ("A", "10"),
            ("B", "11"),
            ("C", "12"),
            ("D", "14"),
            ("E", "15")
        ],
        "expl": "Em um ciclo circular contínuo de 7 dias, no qual sábado e domingo são dias adjacentes, a seleção de 2 dias sem contiguidade é resolvida pelo Segundo Lema de Kaplansky: g(7, 2) = [7 / (7 − 2)] × C(7 − 2, 2) = (7 / 5) × C(5, 2) = (7 / 5) × 10 = 14 opções. Alternativamente, subtrai-se do total de duplas C(7, 2) = 21 os 7 pares adjacentes ao longo da roda semanal, resultando em 21 − 7 = 14."
    }
]
