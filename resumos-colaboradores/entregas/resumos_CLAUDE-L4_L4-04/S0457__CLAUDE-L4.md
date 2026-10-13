---
id: S0457
agente: CLAUDE-L4
materia: Estatística
aula: Aula 05 — Análise Combinatória
trecho: estatistica/a05/s01
paginas_lidas: 4-17
---
# ANALÍTICO

Este trecho abre a Análise Combinatória com os princípios fundamentais de contagem (multiplicativo e aditivo), uma aplicação deles (quantidade de divisores de um número), o princípio da casa dos pombos (garantias no pior cenário) e a contagem de jogos de um torneio de eliminação.

### O que é a análise combinatória

É o conjunto de técnicas para **contar** as possibilidades de um conjunto finito sem listar uma a uma. Com os algarismos 2, 5 e 7, dá para escrever 6 números de 3 algarismos sem repeti-los (257, 275, 527, 572, 725, 752); mas com os nove algarismos de 1 a 9 listar tudo é inviável. A combinatória resolve isso e também conta subconjuntos com certa característica (por exemplo, só os números pares ou só os primos). Os princípios abaixo aparecem em praticamente todas as questões do assunto.

### Princípio multiplicativo (evento A **e** evento B)

Se uma escolha pode ser feita de m maneiras e, para cada uma delas, uma segunda escolha pode ser feita de n maneiras, o total de maneiras de fazer **as duas** é **m × n**. Vale para qualquer quantidade de etapas: com etapas de p1, p2, ..., pk possibilidades, o total é o produto p1 × p2 × ... × pk.

- Palavra-chave: **"e"** (as etapas ocorrem juntas, em sequência), então **multiplique**.
- Se o número de opções de uma etapa depende de uma escolha anterior, use o número de opções que resta em cada etapa (restrições).

> 💡 **Exemplo próprio:** um aluno monta uma senha com 1 letra entre 5 possíveis seguida de 1 algarismo entre 10: 5 × 10 = 50 senhas.

> 💡 **Exemplo próprio (com restrição):** pintar 3 faixas de uma bandeira com 4 cores, de modo que faixas vizinhas tenham cores diferentes. A 1ª faixa tem 4 escolhas; a 2ª, 3 (qualquer cor, menos a da 1ª); a 3ª, 3 (qualquer, menos a da 2ª): 4 × 3 × 3 = 36 maneiras.

> ⚠️ **Pegadinha:** quando só algumas posições têm restrição, a contagem multiplicativa vale desde que se conte, em cada etapa, apenas as opções realmente permitidas. Quando as restrições são independentes entre pares de posições (um par não depende do outro), os pares simplesmente se multiplicam: com c cores, cada par que deve ter cores diferentes contribui com c × (c − 1).

### Contagem de divisores de um número

Para achar quantos divisores positivos um número natural tem:

1. **Fatore** em primos: N = p1^a · p2^b · p3^c ... (os expoentes são a, b, c...).
2. Cada divisor é obtido escolhendo, para cada primo, um expoente entre 0 e o expoente de N. Assim, o primo p1 tem (a + 1) escolhas, p2 tem (b + 1) etc.
3. Pelo princípio multiplicativo: **número de divisores = (a + 1) × (b + 1) × (c + 1) × ...**

> 💡 **Exemplo próprio:** 360 = 2³ · 3² · 5¹. Divisores: (3 + 1) × (2 + 1) × (1 + 1) = 4 × 3 × 2 = 24.

Esse resultado resolve problemas disfarçados: "de quantas formas um produto de dois inteiros positivos dá 216, com ordem importando?" é o mesmo que contar os divisores de 216 (cada divisor d define o par d × 216/d). Como 216 = 2³ · 3³, o total é 4 × 4 = 16.

### Princípio aditivo (evento A **ou** evento B)

Se o evento A pode ocorrer de m maneiras, o evento B de n maneiras e A e B são **mutuamente excludentes** (se um ocorre, o outro não), o número de maneiras de ocorrer **um deles** é **m + n**. Com vários eventos excludentes, soma-se tudo: p1 + p2 + ... + pk.

- Palavra-chave: **"ou"** (alternativas que não acontecem juntas), então **some**.
- Regra de ouro: **"e" multiplica; "ou" (excludente) soma.**

> 💡 **Exemplo próprio:** para ir ao trabalho há 3 linhas de ônibus ou 2 linhas de metrô; escolhe-se um só meio: 3 + 2 = 5 maneiras.

#### Combinando os dois princípios

Problemas complexos misturam "e" e "ou": divida em etapas, descubra quais são concomitantes (multiplicar) e quais são alternativas (somar), calculando de dentro para fora.

> 💡 **Exemplo próprio:** em uma lanchonete, a pessoa escolhe uma comida (5 salgados ou 3 doces) e uma bebida (4 sucos ou 2 refrigerantes). Comidas: 5 + 3 = 8. Bebidas: 4 + 2 = 6. Total: 8 × 6 = 48.

> 💡 **Exemplo próprio (opções alternativas com pares):** escolher dois livros de assuntos diferentes numa estante com 5 de Direito, 3 de Estatística e 2 de Informática. Os pares possíveis de assuntos são alternativas excludentes: Direito+Estatística (5 × 3 = 15), Direito+Informática (5 × 2 = 10) ou Estatística+Informática (3 × 2 = 6). Total: 15 + 10 + 6 = 31.

### Princípio da casa dos pombos

Enunciado: se n objetos ("pombos") são colocados em m compartimentos ("casas") e n > m, **pelo menos um compartimento recebe mais de um objeto**. É a base de questões que pedem o número **mínimo** de elementos para **garantir** algo, e a lógica é sempre a do **pior cenário**: imagine que a sorte ajuda ao máximo o evento contrário e some mais um elemento.

- Garantir **pelo menos 2** no mesmo compartimento, com m compartimentos: m + 1 elementos (o pior caso é um em cada casa; o seguinte repete).
- Garantir **pelo menos k** no mesmo compartimento: **m × (k − 1) + 1** elementos (o pior caso deixa k − 1 em cada casa).
- "Menor número que garante" é a pergunta típica, porque com mais do que esse número a garantia continua valendo, mas não é mais o mínimo.

> 💡 **Exemplo próprio:** quantas pessoas são necessárias para garantir que pelo menos 2 nasceram no mesmo dia da semana? São 7 dias; no pior caso, 7 pessoas nascem em dias diferentes; a 8ª repete. Resposta: 8. Para garantir 3 no mesmo dia: 7 × 2 + 1 = 15.

> 💡 **Exemplo próprio (grupos com tamanhos diferentes):** uma urna tem 10 bolas vermelhas, 3 azuis e 2 verdes. Para garantir 2 da mesma cor, o pior caso é uma de cada cor (3 bolas), então 4 retiradas. Já para garantir pelo menos **uma azul**, o pior caso é tirar todas as 12 não azuis antes, e a 13ª é azul: 13 retiradas. Em geral, defina quem são os "compartimentos" (cores, meses, cargos) antes de calcular.

> ⚠️ **Pegadinha:** conte os compartimentos reais. Se o enunciado dá objetos numerados, agrupe pela característica que interessa (por exemplo, a cor), e não pelo número: números diferentes com a mesma cor formam um só compartimento, e uma cor que aparece uma única vez também é um compartimento. Uma retirada a menos do que o necessário não garante o resultado (com 9 compartimentos, 9 retiradas ainda podem dar todos diferentes; a 10ª garante a repetição).

### Contagem de jogos num torneio de eliminação

Em um torneio em que cada jogo reúne dois jogadores, o perdedor sai e o vencedor segue, terminando com um único campeão:

- Com N jogadores, devem sair N − 1 (restar só o campeão).
- Cada jogo elimina exatamente 1 jogador.
- Logo, o número de jogos é **N − 1**.

Isso vale mesmo com número ímpar de jogadores numa fase (alguém espera para a fase seguinte): a conta por fases chega ao mesmo resultado, mas é desnecessária.

> 💡 **Exemplo próprio:** torneio com 10 jogadores: 9 jogos. Por fases: 5 jogos (restam 5), 2 jogos (restam 3, contando quem esperou), 1 jogo (restam 2), 1 jogo final: 5 + 2 + 1 + 1 = 9. Com 64 jogadores, são 63 jogos (32 + 16 + 8 + 4 + 2 + 1).

Atenção a variações: se o torneio permitir, por exemplo, jogos de ida e volta ou fase de grupos, as contas mudam; a regra N − 1 vale apenas para eliminação direta, em que cada jogo elimina um participante.

### Para fixar
- Combinatória conta possibilidades sem listá-las; os princípios multiplicativo e aditivo estão na base de tudo.
- "E" (etapas sucessivas) multiplica; "ou" (alternativas excludentes) soma.
- Com restrições, conte em cada etapa só as opções permitidas naquele momento.
- Número de divisores: fatore em primos e multiplique (expoente + 1) de cada primo.
- Casa dos pombos: com mais objetos que compartimentos, algum compartimento terá mais de um objeto.
- Para garantir k no mesmo compartimento com m compartimentos: m × (k − 1) + 1.
- Em questões de garantia, pense no pior cenário e some um.
- Torneio de eliminação com N participantes tem N − 1 jogos, pois cada jogo elimina um jogador.

# SINTÉTICO

- **Objetivo da combinatória**: contar possibilidades em conjuntos finitos sem listá-las, inclusive subconjuntos com certa característica (pares, primos).
- **Princípio multiplicativo**: etapas sucessivas com m, n, p opções dão m × n × p maneiras; a palavra-chave é "e".
- **Restrições**: conte em cada etapa só as opções permitidas; por exemplo, em faixas vizinhas de cores diferentes, 4 cores dão 4 × 3 × 3.
- **Divisores**: fatore em primos e multiplique os expoentes mais 1; 360 = 2³ · 3² · 5 tem 4 × 3 × 2 = 24 divisores.
- **Princípio aditivo**: eventos mutuamente excludentes somam suas opções; a palavra-chave é "ou".
- **Misturando**: monte etapas, multiplique as concomitantes e some as alternativas, resolvendo de dentro para fora.
- **Casa dos pombos**: com n > m, algum compartimento recebe mais de um objeto; dá a garantia sobre repetição.
- **Pior cenário**: para garantir k no mesmo compartimento, m × (k − 1) + 1 elementos; é a conta do "menor número que garante".
- **Torneio de eliminação**: com N jogadores há N − 1 jogos, porque cada jogo elimina um e só o campeão fica.

# NOTAS

- O texto das páginas 4 a 17 foi lido por inteiro; nenhuma página vazia. As figuras (desenho de casas e pombos, quadro de meses, esquemas de fatoração) não foram extraídas, mas as explicações estão no texto.
- Página 7: o exemplo do quadrado pintado assume que as cores dos vértices opostos (diagonais) são as únicas restrições; usei o resultado do material para o método (pares de vértices), sem copiar a questão.
- Página 9: a quantidade de tabelas com 216 campos é tratada como número de divisores de 216 (16); conferi: 216 = 2³ · 3³, logo 4 × 4 = 16.
- Página 16: a tabela do torneio de 10 jogadores deixa implícito que quem sobra numa fase ímpar "espera"; o resultado N − 1 independe disso.
- A fórmula m × (k − 1) + 1 para garantir k elementos num mesmo compartimento é a generalização usual do princípio (o material a mostra por exemplos: 4 casas e 3 pombos dão 9, e 4 cargos com 4 iguais dão 13).
