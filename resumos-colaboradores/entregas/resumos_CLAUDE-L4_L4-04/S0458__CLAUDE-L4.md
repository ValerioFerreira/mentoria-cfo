---
id: S0458
agente: CLAUDE-L4
materia: Estatística
aula: Aula 05 — Análise Combinatória
trecho: estatistica/a05/s02
paginas_lidas: 18-31
---
# ANALÍTICO

Este trecho apresenta a ferramenta de cálculo central da análise combinatória, o fatorial, e a sua principal aplicação, a permutação simples: contar de quantos modos é possível ordenar elementos distintos, com ou sem restrições de posição ou de vizinhança.

### Fatorial de um número natural

O **fatorial** de um número natural n, escrito **n!**, é o produto de n por todos os inteiros positivos menores que ele, até chegar ao 1:

n! = n × (n − 1) × (n − 2) × ... × 2 × 1

Valores que convém saber de cabeça: 2! = 2; 3! = 6; 4! = 24; 5! = 120; 6! = 720; 7! = 5.040; 8! = 40.320.

O fatorial cresce muito rápido, mas pode sempre ser "aberto" até o ponto que interessar, parando num fatorial menor que fica "pendurado" no final:

- 7! = 7 × 6! = 7 × 6 × 5!
- 10! = 10 × 9 × 8 × 7!

Esse truque é a chave para **simplificar divisões de fatoriais**: abre-se o fatorial maior até igualar o menor e cortam-se os iguais.

> 💡 **Exemplo:** 12!/10! = (12 × 11 × 10!)/10! = 12 × 11 = 132. E (8! × 5!)/(6! × 7!): como 8! = 8 × 7! e 6! = 6 × 5!, após cancelar 7! e 5! sobra 8/6 = 4/3.

Em frações com fatoriais no numerador e no denominador, basta reescrever o maior de cada lado em função do menor e cancelar; o resultado costuma ser uma fração pequena (por exemplo, 1/70 numa expressão do tipo 9! × 6! sobre 7! × 10!, em que 10! = 10 × 9! e 7! = 7 × 6!).

#### Cuidado com a posição do sinal de fatorial

O fatorial vale **só para o número ao qual está colado**. Usar parênteses muda completamente o resultado:

| Expressão | Como se calcula | Resultado |
| --- | --- | --- |
| 6!/3! | fatoriais primeiro, depois divide | 6 × 5 × 4 = 120 |
| (6/3)! | divide primeiro, depois o fatorial | 2! = 2 |
| 2 × 4! | fatorial de 4, depois multiplica | 2 × 24 = 48 |
| (2 × 4)! | multiplica, depois o fatorial | 8! = 40.320 |
| 2 + 4! | fatorial de 4, depois soma | 2 + 24 = 26 |
| (2 + 4)! | soma, depois o fatorial | 6! = 720 |
| 8 − 3! | fatorial de 3, depois subtrai | 8 − 6 = 2 |
| (8 − 3)! | subtrai, depois o fatorial | 5! = 120 |

Conclusão: o fatorial **não é distributivo** em relação a soma, subtração, multiplicação nem divisão. (a ± b)! e a! ± b! são coisas diferentes; (a × b)! e a! × b! também.

#### Casos especiais: 1! e 0!

Por definição, **1! = 1** (o único fator é o próprio 1) e, por convenção, **0! = 1**. A convenção é coerente com a regra n! = (n + 1)!/(n + 1): 4! = 5!/5, 1! = 2!/2 = 1 e 0! = 1!/1 = 1. Em prova, 0! = 1 aparece muito como armadilha em expressões com fatoriais.

### Permutação simples

Permutar é trocar de lugar; logo, as técnicas de permutação contam as **maneiras de ordenar** elementos. Na **permutação simples** os elementos são todos **distintos** entre si.

Raciocínio por posições: com 3 pessoas a ranquear, qualquer das 3 pode ficar em 1º; sobram 2 candidatas ao 2º lugar; resta 1 para o 3º. As escolhas são sucessivas e simultâneas (a 1ª **e** a 2ª **e** a 3ª), então vale o princípio multiplicativo: 3 × 2 × 1 = 6. Com n elementos, cada posição seguinte tem uma opção a menos que a anterior, e o produto é exatamente o fatorial:

**Pn = n!**

A permutação simples serve para contar filas, rankings, anagramas de palavras sem letras repetidas, números formados com algarismos todos diferentes, etc.

> 💡 **Exemplo:** os anagramas da sigla PMS (3 letras distintas) são P3 = 3! = 6. Uma fila com 8 crianças pode ser montada de P8 = 8! = 40.320 modos. Já 9 pessoas numa fila admitem 9! arranjos.

### Permutação simples com restrição

Quando o enunciado impõe condições, nem todos os elementos circulam livremente. Há dois grandes tipos de restrição: (i) **designar posições** para certos elementos e (ii) obrigar certos elementos a **ficarem juntos**.

#### (i) Elementos designados a posições

**a) Elementos fixos em posições específicas.** Se p dos n elementos já têm lugar certo e definido, eles saem do problema e permutam-se apenas os n − p restantes nos lugares que sobram:

**Pn−p = (n − p)!**

> 💡 **Exemplo:** com os algarismos de 1 a 8 e o 1 cravado na primeira casa e o 8 na última, os seis restantes ocupam as seis casas do meio: 6! = 720 ordenações. Outro caso: cinco aprovados em cinco cidades, com o primeiro colocado já alocado na cidade A, deixa 4 pessoas para 4 cidades, ou seja, 4! = 24.

Vale para quaisquer p elementos em quaisquer p posições: o que importa é o número de elementos que restam.

**b) Elementos reservados a certas posições, mas sem fixar quem fica onde.** Se os p elementos devem ocupar um grupo de p posições previamente determinado, mas podem trocar de lugar entre si dentro do grupo, calculam-se duas permutações separadas e multiplicam-se:

**Pn−p × Pp = (n − p)! × p!**

> 💡 **Exemplo:** o 1 e o 8 nas extremidades, em qualquer ordem: P6 × P2 = 720 × 2 = 1.440 (as duas formas de arrumar as pontas dobram as 720). Com os algarismos 1, 2 e 3 devendo ocupar as três primeiras casas em qualquer ordem e os outros cinco as casas restantes: 3! × 5! = 6 × 120 = 720.

Raciocínio equivalente para **grupos alternados**: se, em 8 algarismos, os ímpares precisam ficar nas posições ímpares e os pares nas posições pares, são 4! para os ímpares e 4! para os pares: 24 × 24 = 576.

> ⚠️ **Pegadinha:** a ordem dentro de cada grupo muda o resultado. Quando o enunciado diz "nas três primeiras posições, **não necessariamente nessa ordem**", o fator é 3! × 7!, e não apenas 3 × 7!. Alternativas que trazem "3 × 7!" ou "7 × 7!" costumam ser a versão errada do valor correto.

**Alternância de dois grupos numa fila.** Com 5 meninas e 4 meninos em fila, alternados, a única disposição possível é começar e terminar por menina (A O A O A O A O A). Meninas: 5! = 120; meninos: 4! = 24; total 120 × 24 = 2.880. Se os grupos tivessem o mesmo tamanho, haveria duas opções de quem começa, e o resultado dobraria; nesse caso, 2 × (permutações de um grupo) × (permutações do outro).

#### (ii) Elementos que devem ficar juntos

A técnica é **colar os elementos num bloco** e tratá-lo como se fosse um único elemento.

**a) Juntos, em determinada ordem.** Se j dos n elementos precisam ficar lado a lado numa ordem pré-fixada, o bloco conta como 1 elemento. Permutam-se, então, n − j + 1 elementos (os n − j livres mais o bloco):

**Pn−j+1 = (n − j + 1)!**

> 💡 **Exemplo:** entre 8 algarismos, se o 1 e o 2 vão sempre juntos nessa ordem, ordenam-se 7 objetos: 7! = 5.040. Se três algarismos formam o bloco, ordenam-se 6 objetos. Numa fila de 10 animais, com leão, camelo e elefante juntos e nessa sequência, os objetos são 7 animais livres + 1 bloco = 8, e o total é 8! (que é igual a 8 × 7!, e não a 7 × 7!).

**b) Juntos, em qualquer ordem.** Faz-se a conta do caso anterior e multiplica-se pelas maneiras de arrumar os j elementos dentro do bloco:

**Pn−j+1 × Pj = (n − j + 1)! × j!**

> 💡 **Exemplo:** de 8 algarismos, os três primeiros (1, 2 e 3) colados em qualquer ordem: 6! × 3! = 720 × 6 = 4.320. Com apenas dois algarismos colados em qualquer ordem em números de 5 dígitos formados por 1, 2, 3, 4 e 5, o bloco entra como 1 objeto entre 4 (4!) e se multiplica por 2! das trocas internas: 24 × 2 = 48.

> ⚠️ **Pegadinha:** esquecer o fator das trocas internas do bloco é o erro mais comum. Ao ler "juntos", pergunte-se se a ordem interna é fixa (só n − j + 1 elementos) ou livre (multiplica por j!).

#### Quadro-resumo das restrições

| Situação | Quantas permutações |
| --- | --- |
| p elementos fixos em posições determinadas | (n − p)! |
| p elementos reservados a p posições, trocando entre si | (n − p)! × p! |
| j elementos juntos, em ordem fixa | (n − j + 1)! |
| j elementos juntos, em qualquer ordem | (n − j + 1)! × j! |

### Para fixar
- n! é o produto de n até 1; 0! = 1 e 1! = 1; valores a memorizar: 5! = 120, 6! = 720, 7! = 5.040.
- Para dividir fatoriais, abra o maior até o menor e cancele (10!/7! = 10 × 9 × 8 = 720).
- O fatorial não se distribui sobre soma, subtração, produto ou divisão: (2 + 4)! = 720, mas 2 + 4! = 26.
- Permutação simples de n elementos distintos: Pn = n!, deduzida pelo princípio multiplicativo (n × (n − 1) × ... × 1).
- Elementos fixos em p posições saem do problema: (n − p)!. Se só são reservados a um grupo de posições, multiplica-se por p!.
- Elementos que ficam juntos formam um bloco: (n − j + 1)! se a ordem é fixa; multiplica-se por j! se a ordem interna é livre.
- Grupos alternados: calcule a permutação de cada grupo e multiplique; atenção a quem pode abrir a fila.

# SINTÉTICO

- **Fatorial**: n! = n × (n − 1) × ... × 1, com 0! = 1 e 1! = 1; decorar 5! = 120, 6! = 720, 7! = 5.040.
- **Simplificação**: abra o fatorial maior até o menor e cancele; 10!/7! = 10 × 9 × 8 = 720.
- **Parênteses importam**: (2 + 4)! = 720, porém 2 + 4! = 26; (6/3)! = 2, mas 6!/3! = 120.
- **Permutação simples**: elementos distintos, Pn = n!; vale para filas, rankings, anagramas e números sem algarismo repetido.
- **Elementos fixos**: p elementos com posição determinada saem do cálculo, restando (n − p)!.
- **Grupo reservado a posições**: se os p elementos trocam entre si dentro das posições reservadas, (n − p)! × p!; exemplo: pontas com 1 e 8 em 8 algarismos, 6! × 2! = 1.440.
- **Alternância**: 5 meninas e 4 meninos alternados exigem começar por menina, 5! × 4! = 2.880.
- **Juntos em ordem fixa**: o bloco vira 1 elemento, (n − j + 1)!; três animais seguidos numa ordem, em fila de 10, dá 8!.
- **Juntos em qualquer ordem**: (n − j + 1)! × j!; três algarismos colados entre 8 dá 6! × 3! = 4.320.
- **Erro típico**: esquecer a permutação interna do bloco ou o fator p! do grupo reservado, e trocar 3! × 7! por 3 × 7!.

# NOTAS

Páginas 18-31 legíveis; fórmulas aparecem embaralhadas na extração, mas foram recompostas com segurança pelo contexto. No quadro final do material há um erro de numeração na lista (aparece "i.b" no lugar de "ii.b"); o conteúdo está correto e foi apresentado de forma arrumada. A última questão da página 31 (algarismos 1 e 2 juntos em qualquer ordem, "inferior a 25") tem o comentário na página seguinte, fora do intervalo; o resumo usa o caso 4! × 2! = 48 como exemplo próprio, resolvido pela regra do bloco. Metade do trecho contém questões comentadas; o resumo extrai delas os métodos e as pegadinhas.
