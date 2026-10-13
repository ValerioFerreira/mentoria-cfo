---
id: S0416
agente: CLAUDE-L4
materia: Estatística
aula: Aula 05 — Análise Combinatória
trecho: estatistica/a05/s03
paginas_lidas: 32-48
---
# ANALÍTICO

Este trecho amplia a permutação simples para os casos em que há elementos repetidos, disposição em círculo, elementos que precisam respeitar uma ordem e deslocamentos "sem ninguém no lugar de origem" (desarranjo). Em seguida, introduz o arranjo, em que se escolhe um subconjunto e a ordem da escolha importa, e o contrasta com a combinação.

### Revisão: permutação simples

Permutar é ordenar todos os elementos. Com n elementos **distintos**, há **Pn = n!** ordenações (n! = n · (n−1) · ... · 1). Por exemplo, 3 elementos distintos geram 3! = 6 ordens. Os demais casos deste trecho derivam dessa ideia: conta-se como se tudo fosse distinto e **divide-se** pelas repetições que o problema considera iguais.

### Permutação com repetição

Se alguns elementos são iguais, trocar dois deles de lugar não produz uma ordem nova. Por isso a permutação simples **superconta**, e o excesso é eliminado dividindo pela permutação de cada grupo de elementos iguais:

**Pn (m1, m2, ..., mk) = n! / (m1! · m2! · ... · mk!)**

em que n é o total de elementos e m1, m2, ..., mk são as quantidades de cada elemento repetido (elementos que aparecem uma única vez não precisam ser listados, pois 1! = 1).

> 💡 **Exemplo:** anagramas da palavra BANANA: 6 letras, com A repetido 3 vezes e N repetido 2 vezes (B aparece uma vez). Total = 6! / (3! · 2!) = 720 / 12 = **60**.

> 💡 **Exemplo:** anagramas de ARARA: 5! / (3! · 2!) = 10.

> ⚠️ **Pegadinha:** conte as letras com cuidado (acentos não mudam a letra) e divida pelo fatorial de **cada** letra repetida, não só da mais frequente. Uma palavra sem letras repetidas é permutação simples.

### Permutação circular

Em círculo não existem "primeira", "segunda" posições nem noção de esquerda ou direita fixas. Girar a mesa inteira não gera uma disposição nova; só importa a posição de cada elemento **em relação aos demais**.

Para contar, **fixa-se um elemento** (em qualquer lugar) e permutam-se os outros n − 1:

**PCn = (n − 1)!**

> 💡 **Exemplo:** 6 amigos em uma mesa redonda: PC6 = 5! = 120 formas.

#### Com restrições

Resolve-se em **etapas** e multiplica-se (princípio multiplicativo). Em geral, senta-se primeiro um dos grupos como permutação circular; depois, os lugares dos demais grupos ficam **distinguíveis** (cada vaga fica entre vizinhos específicos) e são permutados como uma permutação simples.

> 💡 **Exemplo:** 3 homens e 3 mulheres numa mesa redonda, sempre alternados. Homens: PC3 = 2! = 2. Mulheres nos 3 vãos entre eles: 3! = 6. Total: 2 × 6 = **12**.

### Permutação com elementos ordenados

Alguns elementos devem aparecer numa **ordem prefixada** (não necessariamente lado a lado). A lógica é a da repetição: na permutação simples, as k posições desses elementos admitem k! arranjos entre si, mas só **um** é aceito. Então:

**n! / k!**

> 💡 **Exemplo:** 6 pessoas em fila, com A antes de B: 6!/2! = 360 (metade das 720). Com A antes de B e este antes de C: 6!/3! = 120.

Se houver **dois grupos** que precisam de ordem própria (k1 elementos numa ordem e k2 noutra), divide-se pelos dois fatoriais: **n! / (k1! · k2!)**.

> 💡 **Exemplo:** anagramas de LIVROS (6 letras) com L, I, V nessa ordem e O, S nessa ordem: 6! / (3! · 2!) = 60.

> ⚠️ **Pegadinha:** "A antes de B" **não** significa "A e B juntos". Se a questão exigir a ordem **e** a adjacência, trate o par como um único elemento. A conta é a mesma da permutação com repetição, mas o raciocínio é outro: aqui os elementos são distintos e só a ordem relativa é imposta.

### Permutação caótica (desarranjo)

Parte-se de uma ordem original e conta-se quantas reordenações deixam **todos os elementos fora da posição de origem**. Notação: **Dn**.

**Dn = n! · [1/2! − 1/3! + 1/4! − ... + (−1)^n / n!]**

Os sinais alternam; (−1)^n é +1 para n par e −1 para n ímpar, determinando o sinal do último termo. Os termos 1/0! − 1/1! se cancelam e por isso ficam fora da fórmula.

| n | Dn | Cálculo |
| --- | --- | --- |
| 2 | 1 | 2! · (1/2) |
| 3 | 2 | 3! · (1/2 − 1/6) = 3 − 1 |
| 4 | 9 | 4! · (1/2 − 1/6 + 1/24) = 12 − 4 + 1 |
| 5 | 44 | 5! · (1/2 − 1/6 + 1/24 − 1/120) = 60 − 20 + 5 − 1 |

> 💡 **Exemplo:** 4 funcionários trocam de mesa e ninguém pode ficar na mesa que ocupava. Resposta: D4 = 9. Com 3 elementos A, B, C, as únicas ordens sem ninguém no lugar de origem são C A B e B C A (D3 = 2).

Padrão de enunciado: "cada um deve receber algo que **não** seja o seu", "nenhum fica na posição original", "ninguém analisa o parente".

### Arranjo e combinação: quando a ordem importa

Agora se **escolhe um subconjunto** de k elementos entre n:

| | Ordem da escolha | Escolher A e B ou B e A |
| --- | --- | --- |
| **Arranjo** | importa | possibilidades diferentes |
| **Combinação** | não importa | mesma possibilidade |

#### Arranjo simples (sem reposição)

Sorteia-se um elemento por vez, sem repetir: n opções para o primeiro, n−1 para o segundo, e assim por diante até k fatores (é um fatorial "interrompido"). Corta-se o fatorial dividindo por um fatorial menor:

**A(n, k) = n! / (n − k)!**, com k ≤ n (também escrito como A com n embaixo e k em cima)

> 💡 **Exemplo:** 8 candidatos disputam três prêmios distintos (1º, 2º e 3º lugares): A(8,3) = 8!/5! = 8 · 7 · 6 = **336**. Para 10 pessoas e 4 sorteios, 10 · 9 · 8 · 7 = 5.040.

Atenção a situações em que a ordem aparece disfarçada: escolher, entre 10 pessoas, 1 supervisor, 1 coordenador e 1 técnico é arranjo (a mesma pessoa em cargos diferentes forma casos diferentes). Números formados com algarismos também: 357 e 573 são distintos.

#### Arranjo com reposição

Se o mesmo elemento pode ser escolhido mais de uma vez, sempre há n opções por etapa: **n^k**. Por exemplo, senhas de 3 dígitos (0 a 9) podem repetir algarismos: 10 · 10 · 10 = 1.000. A fórmula n!/(n−k)! é só para o caso **sem reposição**.

#### Combinação

Quando a ordem não interessa (comissões, grupos), divide-se o arranjo pelas k! ordens internas de cada grupo:

**C(n, k) = n! / (k! · (n − k)!)**

> 💡 **Exemplo:** comissão de 3 pessoas escolhidas entre 8: C(8,3) = 336 / 3! = 56.

### Para fixar

- Permutação simples: n!. Com repetição: n! dividido pelo fatorial de cada grupo de iguais.
- Circular: (n − 1)!; com restrições, resolva em etapas e multiplique.
- Elementos em ordem prefixada: n!/k!; dois grupos: n!/(k1!·k2!); não implica elementos juntos.
- Desarranjo: D2 = 1, D3 = 2, D4 = 9, D5 = 44; reconhecível por "ninguém no seu lugar original".
- Arranjo (ordem importa): n!/(n−k)!; com reposição, n^k.
- Combinação (ordem não importa): n!/(k!(n−k)!), isto é, o arranjo dividido por k!.
- Teste prático: troque a ordem dos escolhidos; se a situação mudar, é arranjo; se não mudar, é combinação.

# SINTÉTICO

- **Permutação com repetição**: Pn = n! / (m1! · m2! · ...); divide-se pelo fatorial de cada grupo de elementos iguais; BANANA tem 6!/(3!·2!) = 60 anagramas.
- **Permutação circular**: PCn = (n − 1)!, pois se fixa um elemento e se permutam os outros; girar a mesa não gera disposição nova.
- **Circular com restrições**: divide-se em etapas (por exemplo, alternar homens e mulheres) e multiplica-se: PC dos primeiros vezes P dos demais.
- **Elementos em ordem**: n!/k! quando k elementos seguem uma ordem fixa, não necessariamente juntos; para dois grupos, n!/(k1!·k2!).
- **Desarranjo**: Dn = n! · [1/2! − 1/3! + ... + (−1)^n/n!]; valores D2 = 1, D3 = 2, D4 = 9, D5 = 44.
- **Arranjo simples**: A(n,k) = n!/(n−k)!, escolha sem reposição em que a ordem importa (por exemplo, prêmios distintos).
- **Arranjo com reposição**: n^k, porque em cada etapa há sempre n opções.
- **Arranjo × combinação**: no arranjo a ordem diferencia os casos; na combinação, C(n,k) = A(n,k)/k!, a ordem é irrelevante.

# NOTAS

- Páginas 32, 34, 37 a 39, 42, 44 a 45 e 48 trazem questões comentadas; só a teoria foi aproveitada. As figuras (círculos numerados, mesa de meninos e meninas, diagramas de pais e filhos) foram descartadas; todos os exemplos numéricos são próprios.
- O assunto "Combinação" consta do roteiro do trecho, mas nas páginas 32 a 48 só aparecem a distinção entre arranjo e combinação (pág. 46); a fórmula C(n,k) foi acrescentada por conhecimento padrão e deve ser conferida/ complementada com o trecho seguinte, caso ele traga a combinação por extenso. A página 48 termina no meio de uma questão (senha de 6 dígitos), cortada.
- O valor D5 = 44 e a tabela de desarranjos foram calculados pela fórmula do trecho; o texto só traz D3 e D4. 
- Erro de notação no material (pág. 45): a questão de 3 servidores escreve "D4 = 3! ×..." em vez de D3; o resultado (2) está certo para n = 3.
- Na pág. 32, a lista das 6 ordens com A repetido traz "IV) B A A" no lugar de uma ordem correspondente; irrelevante ao método (a contagem 3 está correta).

