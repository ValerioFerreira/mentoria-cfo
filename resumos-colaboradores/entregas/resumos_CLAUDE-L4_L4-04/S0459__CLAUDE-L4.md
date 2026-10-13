---
id: S0459
agente: CLAUDE-L4
materia: Estatística
aula: Aula 05 — Análise Combinatória
trecho: estatistica/a05/s05
paginas_lidas: 65-78
---
# ANALÍTICO

Este trecho trata de dois tópicos avançados de contagem: as **partições** de um conjunto em subgrupos (ordenadas e não-ordenadas) e os **lemas de Kaplansky**, que contam seleções em que dois elementos vizinhos nunca são escolhidos juntos, em fila (primeiro lema) ou em círculo (segundo lema).

### Partições: a ideia

Particionar um conjunto é repartir todos os seus elementos em subconjuntos, como cortar uma pizza em fatias de tamanhos quaisquer: juntando todas as fatias, volta-se ao todo. Exemplo: 9 trabalhadores divididos em grupos de 5, 2 e 2 (a soma dos grupos é sempre o total).

Essa característica, a **soma dos tamanhos dos grupos igual ao total**, é o que distingue a partição de uma combinação comum, na qual se escolhe só uma parte do conjunto. Problemas de partição podem ser resolvidos com combinações sucessivas, mas a fórmula própria é mais rápida e reduz erros.

Há dois tipos, conforme os grupos sejam diferentes ou equivalentes:

| Tipo | Os grupos são... | A ordem entre os grupos |
| --- | --- | --- |
| Partição **ordenada** | distintos (funções, destinos ou tarefas diferentes) | importa |
| Partição **não-ordenada** | equivalentes (todos fazem a mesma coisa) | não importa |

> ⚠️ **Pegadinha:** em ambos os tipos, a ordem **dentro** de cada grupo não importa. A diferença está só na ordem **entre** os grupos.

### Partição ordenada

Como funciona: escolhe-se o primeiro grupo entre todos os n elementos, o segundo entre os que sobraram, e assim por diante, multiplicando as combinações. Para dividir 10 pessoas em 1 gerente, 2 coordenadores e 7 operadores:

C(10,1) × C(9,2) × C(7,7) = 10 × 36 × 1 = 360

Ao escrever os fatoriais de cada combinação, os termos intermediários se cancelam em cadeia (o (n − p1)! do denominador de uma fração anula o numerador da seguinte) e o último fatorial vira 0! = 1. Sobra a fórmula direta, em que n é o total e p1, p2, ..., pm são os tamanhos dos m grupos, com p1 + p2 + ... + pm = n:

**n! / (p1! × p2! × ... × pm!)**

Essa expressão aparece escrita com n sobre p1, p2, ..., pm entre parênteses, como uma "combinação com várias partes" (coeficiente multinomial). No exemplo: 10!/(1! × 2! × 7!) = 360.

> 💡 **Exemplo próprio:** 12 alunos serão alocados em 3 laboratórios diferentes, com 5, 4 e 3 vagas. Como os laboratórios são distintos, a conta é 12!/(5! × 4! × 3!) = 27.720.

Aplicações de prova: distribuir 7 projetos entre 3 departamentos que recebem 3, 2 e 2 projetos: 7!/(3! × 2! × 2!) = 210. Distribuir 10 estações iguais entre 3 empresas aprovadas, em proporção às pontuações 500, 300 e 200: primeiro acha-se a quantidade de cada uma (cada ponto vale 10/1000 = 1/100 de estação, então 5, 3 e 2), depois conta-se 10!/(5! × 3! × 2!) = 2.520.

> ⚠️ **Pegadinha:** repare no que o enunciado pede. Dividir as 10 estações em proporção às pontuações é um passo de proporcionalidade; só depois vem a partição. E empresas reprovadas (nota insuficiente) ficam fora da conta.

### Partição não-ordenada

Se os grupos são equivalentes, trocar a ordem em que os mesmos grupos são formados não gera um resultado novo. Parte-se da ordenada e **divide-se pelo número de modos de reordenar os grupos**, isto é, por m! (permutação dos m grupos).

Aqui, para que os grupos sejam de fato intercambiáveis, eles precisam ter o **mesmo tamanho p**. Com m grupos de p elementos cada, o total é n = m × p, e a fórmula fica:

**(m × p)! / ( m! × (p!)^m )**

> 💡 **Exemplo do trecho, reformulado:** 6 pessoas em 3 duplas que farão o mesmo trabalho. Ordenada: 6!/(2! × 2! × 2!) = 90. Cada formação de duplas aparece repetida 3! = 6 vezes (as mesmas duplas listadas em ordens diferentes), então a não-ordenada vale 90/6 = 15.

> 💡 **Exemplo próprio:** dividir 8 pessoas em duas equipes de 4 que jogam o mesmo jogo: 8!/(2! × (4!)^2) = 40.320/(2 × 576) = 35. E 12 pessoas em 4 grupos de 3 indistintos: 12!/(4! × (3!)^4) = 15.400.

Mais um caso clássico de prova: dividir 10 pessoas em dois grupos de 5 dá 10!/(2! × (5!)^2) = 126.

> ⚠️ **Pegadinha:** dividir por m! só é correto quando os grupos trocáveis têm o mesmo tamanho. Se alguns grupos têm tamanhos diferentes, eles já são distinguíveis pelo tamanho; a divisão ocorre apenas para os grupos de tamanho igual (por exemplo, 7 pessoas em grupos de 3, 2 e 2 em que os dois grupos de 2 são equivalentes: 210/2 = 105). Confira sempre se o enunciado trata os grupos como diferentes (com nomes ou funções) ou iguais.

### Lemas de Kaplansky

Os lemas contam as formas de **selecionar p elementos de um conjunto de n elementos dispostos em ordem, sem que dois vizinhos sejam escolhidos**. A ordem da seleção não importa. A diferença entre os dois lemas:

| Lema | Disposição | Os extremos (1º e n-ésimo) |
| --- | --- | --- |
| 1º lema, f(n, p) | fila | **não** são vizinhos |
| 2º lema, g(n, p) | círculo | **são** vizinhos |

#### Primeiro lema

Sem o lema, calcularia-se o total C(n, p) e subtrairiam-se os casos com vizinhos; isso é viável para p = 2 (de 8 elementos: C(8,2) = 28, menos 7 pares consecutivos, dá 21) mas fica penoso para p maior.

O raciocínio de Kaplansky evita isso. Marque cada elemento escolhido por S e cada não escolhido por N. Os n − p elementos N são colocados em fila, e deixa-se um espaço antes, entre e depois deles: ficam **n − p + 1 espaços**. Cada elemento escolhido ocupa um espaço diferente, de modo que nunca há dois S juntos. Portanto, basta escolher em quais p desses espaços ficam os S:

**f(n, p) = C(n − p + 1, p)**

Conferindo: n = 8, p = 2 dá C(7,2) = 21, igual ao cálculo direto. Entender o raciocínio vale mais do que decorar a fórmula.

> 💡 **Exemplo próprio:** em uma fileira de 10 cadeiras, de quantas formas 4 pessoas se sentam sem ficar lado a lado? f(10,4) = C(7,4) = 35. Já o caso do estagiário que escolhe 3 dias entre segunda e sábado (6 dias), sem dias seguidos: f(6,3) = C(4,3) = 4.

Observações úteis:
- Se p é grande demais, a combinação dá zero (não existe seleção possível): cinco lâmpadas em fila não admitem 4 acesas sem adjacentes.
- Para p = 0 e p = 1 o lema nem é necessário (C(n,0) = 1 e C(n,1) = n).
- Problemas "acender lâmpadas sem duas adjacentes" pedem a soma de todos os tamanhos possíveis de seleção, pelo princípio aditivo. Com 5 lâmpadas: nenhuma acesa (1) + uma (5) + duas, f(5,2) = C(4,2) = 6 + três, f(5,3) = C(3,3) = 1, totalizando 13 configurações. Os casos são excludentes, por isso se soma.

#### Segundo lema

Quando o conjunto forma um círculo (mesa redonda, dias da semana de segunda a domingo, meses do ano, fatias de pizza), o primeiro e o último elemento também são vizinhos. A fórmula é:

**g(n, p) = [ n / (n − p) ] × C(n − p, p)**

> 💡 **Exemplo do trecho:** 3 fatias de queijo entre 8 fatias de pizza, sem duas vizinhas: g(8,3) = (8/5) × C(5,3) = (8/5) × 10 = 16.

Por que funciona: separa-se em dois casos, escolhendo ou não o elemento 1.
- Elemento 1 **escolhido**: seus vizinhos (2 e n) ficam proibidos; sobra uma fila de n − 3 elementos em que se escolhem p − 1, e os extremos dessa fila já não são vizinhos: f(n − 3, p − 1). Para n = 8 e p = 3: f(5,2) = 6.
- Elemento 1 **não escolhido**: ele sai do círculo, que vira uma fila de n − 1 elementos com p escolhas: f(n − 1, p). Para n = 8 e p = 3: f(7,3) = 10.

Os casos se excluem, então somam-se: 6 + 10 = 16, o mesmo da fórmula. Essa via serve de conferência: com n = 10 e p = 4, f(7,3) + f(9,4) = 10 + 15 = 25, e a fórmula dá (10/6) × C(6,4) = (10/6) × 15 = 25.

> ⚠️ **Pegadinha:** antes de escolher o lema, pergunte se o primeiro e o último elemento são vizinhos na situação do enunciado. Fila de dias de segunda a sábado: 1º lema. Semana inteira em ciclo, mesa redonda ou pizza: 2º lema. Usar o lema errado altera o resultado (para 8 elementos e 3 escolhas, 20 contra 16).

### Para fixar
- Partição: o conjunto é dividido por completo em grupos; a soma dos tamanhos dos grupos é o total de elementos.
- Ordenada (grupos distintos): n!/(p1! × p2! × ... × pm!); a ordem dentro do grupo não conta.
- Não-ordenada (grupos iguais e de mesmo tamanho p): (m × p)!/(m! × (p!)^m); é a ordenada dividida por m!.
- Grupos de tamanhos diferentes já são distinguíveis; só se divide pelo fatorial da quantidade de grupos de mesmo tamanho que sejam equivalentes.
- 1º lema de Kaplansky (fila, extremos não vizinhos): f(n,p) = C(n − p + 1, p). Ideia: n − p elementos não escolhidos criam n − p + 1 espaços.
- 2º lema (círculo, extremos vizinhos): g(n,p) = n/(n − p) × C(n − p, p); equivale a f(n − 3, p − 1) + f(n − 1, p).
- Se a contagem total de configurações permite várias quantidades de elementos, calcule cada quantidade e some.

# SINTÉTICO

- **Partição**: divide todos os elementos do conjunto em grupos; a soma dos tamanhos é o total, o que a diferencia de uma combinação comum.
- **Ordenada**: grupos distintos (funções, destinos); número de modos = n!/(p1! × p2! × ... × pm!), equivalente a multiplicar combinações sucessivas.
- **Exemplo ordenado**: 7 projetos em departamentos que recebem 3, 2 e 2 dão 7!/(3! × 2! × 2!) = 210.
- **Não-ordenada**: grupos equivalentes e de mesmo tamanho p; divide-se a ordenada por m!: (m × p)!/(m! × (p!)^m). Dez pessoas em dois grupos de 5: 126.
- **Ordem dentro do grupo**: nunca conta; só a ordem entre os grupos muda de um tipo para o outro.
- **1º lema de Kaplansky**: fila, sem vizinhos selecionados e com extremos não vizinhos; f(n,p) = C(n − p + 1, p); 3 dias de 6 sem seguidos dá 4.
- **Raciocínio dos espaços**: os n − p não escolhidos geram n − p + 1 lugares, e escolhem-se p deles para os escolhidos.
- **2º lema**: círculo, com extremos vizinhos; g(n,p) = n/(n − p) × C(n − p, p); 3 fatias de 8 sem vizinhas dão 16.
- **Decomposição do círculo**: elemento 1 escolhido, f(n − 3, p − 1); não escolhido, f(n − 1, p); soma = g(n,p).
- **Várias quantidades**: quando se aceitam seleções de 0, 1, 2... elementos, soma-se cada caso (5 lâmpadas sem adjacentes acesas: 1 + 5 + 6 + 1 = 13).

# NOTAS

Páginas 65-78 legíveis; fórmulas (coeficiente multinomial, frações) foram recompostas pelo contexto, pois a extração as embaralha, e todos os valores numéricos foram refeitos e conferidos. A tabela de pontuações da questão de metrô (página 68) não foi extraída, mas a resolução comentada informa que as empresas aprovadas têm 500, 300 e 200 pontos, e o resumo usa só isso. O material afirma que a partição não-ordenada exige grupos de mesmo tamanho; incluí, como complemento matemático correto, a observação sobre grupos equivalentes entre outros de tamanho diferente (ex.: 3, 2, 2 com os dois grupos de 2 equivalentes dá 105), que o texto não desenvolve. Cerca de um quarto do trecho é de questões comentadas; os métodos foram extraídos delas.
