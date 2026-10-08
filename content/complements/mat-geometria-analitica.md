---
id: mat-geometria-analitica
subject: matematica
title: Geometria analítica plana
short: Geometria analítica
subtitle: Plano cartesiano, distância, ponto médio, baricentro, retas, paralelismo e perpendicularidade, circunferências e sistemas lineares (itens 5.1 a 5.5 do edital de Matemática)
weight: 0.12
order: 1
resolves: mat-geometria-analitica
---

## O que este material cobre e como estudar

Pessoal, o item 5 do edital de Matemática ("conhecimentos algébricos/geométricos") lista: **plano cartesiano; retas; circunferências; paralelismo e perpendicularidade; sistemas de equações**. O curso principal traz o plano cartesiano (par ordenado, produto cartesiano) e a reta **apenas como gráfico da função do 1º grau**. Faltam as ferramentas da geometria analítica propriamente dita. Este complemento fecha essa lacuna, na ordem em que o assunto se constrói:

1. Plano cartesiano: quadrantes e simetrias de pontos (revisão curta);
2. Distância entre dois pontos, ponto médio e baricentro;
3. Condição de alinhamento de três pontos e área do triângulo (determinante);
4. Equações da reta: geral, reduzida, segmentária, paramétrica e ponto-inclinação;
5. Posição relativa de duas retas: paralelas, concorrentes, perpendiculares; ângulo entre retas;
6. Distância de ponto a reta (e entre paralelas);
7. Circunferência: equação reduzida e geral, posições relativas;
8. Sistemas de equações lineares e sua interpretação geométrica;
9. Resumo de fórmulas, pegadinhas e exercícios autorais com gabarito.

> **Como estudar:** geometria analítica é **pouca teoria e muita fórmula aplicada**. Memorize as 8 ou 9 fórmulas do quadro de resumo (seção 9) e treine as contas curtas: quase todo exercício se resolve com substituição direta, e os números costumam ser "bonitos" (3-4-5, 5-12-13, 6-8-10).

> **O que esperar na prova:** no banco de questões de Matemática da AOCP que analisamos para este projeto (39 questões, quase todas com 5 alternativas e cerca de 30% pedindo cálculo), o enunciado é curto (mediana de 46 palavras) e as alternativas são números ou expressões curtas. Não há, nessa amostra, questão de geometria analítica, mas o edital do CBM-PE a lista expressamente. O mais provável, portanto, é a questão **curta e direta**: "qual a distância...", "qual a equação da reta...", "qual o centro e o raio...", "para que valor de k as retas são paralelas/perpendiculares". Esse é o padrão que treinamos aqui.

## 1. Plano cartesiano (revisão curta)

O **plano cartesiano** é formado por dois eixos perpendiculares que se cruzam na **origem** O(0, 0): o eixo horizontal das abscissas (**x**) e o vertical das ordenadas (**y**). Cada ponto é um par ordenado P(x, y). (A teoria de par ordenado, produto cartesiano e relação está no curso principal, Aula 09.)

**Quadrantes** (contados no sentido anti-horário a partir do canto superior direito):

| Quadrante | Sinal de x | Sinal de y | Exemplo |
|---|---|---|---|
| 1º | + | + | (3, 2) |
| 2º | − | + | (−3, 2) |
| 3º | − | − | (−3, −2) |
| 4º | + | − | (3, −2) |

- Ponto **sobre o eixo x**: y = 0, ou seja, (a, 0). Ponto **sobre o eixo y**: x = 0, ou seja, (0, b). Esses pontos **não pertencem a nenhum quadrante**.
- **Bissetriz dos quadrantes ímpares** (1º e 3º): reta y = x (pontos com abscissa igual à ordenada). **Bissetriz dos quadrantes pares** (2º e 4º): reta y = −x.

### Simetrias de um ponto P(a, b)

| Simétrico em relação a | Resultado | Regra |
|---|---|---|
| eixo x | (a, −b) | troca o sinal de y |
| eixo y | (−a, b) | troca o sinal de x |
| origem | (−a, −b) | troca os dois sinais |
| bissetriz y = x | (b, a) | troca x e y de lugar |
| bissetriz y = −x | (−b, −a) | troca de lugar **e** de sinal |

**Exemplo:** P(3, −2). Simétrico em relação ao eixo x: (3, 2). Ao eixo y: (−3, −2). À origem: (−3, 2). À bissetriz y = x: (−2, 3).

> **Macete:** o que muda de sinal é a coordenada "que atravessa o espelho". Espelho no eixo x: quem muda é y.

## 2. Distância entre dois pontos, ponto médio e baricentro

### 2.1 Distância entre dois pontos

Para A(x₁, y₁) e B(x₂, y₂), o triângulo retângulo de catetos |x₂ − x₁| e |y₂ − y₁| e hipotenusa AB dá, por Pitágoras:

**d(A, B) = √[(x₂ − x₁)² + (y₂ − y₁)²]**

**Exemplo 1.** A(1, 2) e B(7, 10): d = √(6² + 8²) = √100 = **10**.

**Exemplo 2 (ponto equidistante).** Qual ponto do eixo x é equidistante de A(1, 2) e B(5, 4)?

O ponto é P(x, 0). Igualando os **quadrados** das distâncias (para evitar raiz):

(x − 1)² + (0 − 2)² = (x − 5)² + (0 − 4)²
x² − 2x + 1 + 4 = x² − 10x + 25 + 16
−2x + 5 = −10x + 41 → 8x = 36 → x = 4,5

Logo P(4,5; 0). Conferência: PA² = 3,5² + 4 = 16,25 e PB² = 0,5² + 16 = 16,25.

**Exemplo 3 (classificar triângulo).** A(0, 0), B(4, 0), C(2, 3): AB = 4; AC = √(4 + 9) = √13; BC = √(4 + 9) = √13. Dois lados iguais: triângulo **isósceles** (não é equilátero; e, como AB² = 16 ≠ 13 + 13 = 26, não é retângulo).

> **Dica de prova:** para saber se um triângulo é retângulo, calcule os **quadrados** dos três lados e teste Pitágoras (maior = soma dos outros dois). Não precisa tirar raiz.

### 2.2 Ponto médio

O ponto médio M de AB tem coordenadas que são as **médias** das coordenadas:

**M = ( (x₁ + x₂)/2 ; (y₁ + y₂)/2 )**

**Exemplo 1.** A(2, −4) e B(8, 6): M = (5, 1).

**Exemplo 2 (extremo desconhecido).** M(3, 1) é ponto médio de AB e A(−1, 4). Então (−1 + x_B)/2 = 3 → x_B = 7 e (4 + y_B)/2 = 1 → y_B = −2. Logo **B(7, −2)**.

> **Macete do extremo:** B = 2M − A (coordenada a coordenada). Aqui: 2·3 − (−1) = 7 e 2·1 − 4 = −2.

O ponto médio também resolve: **centro de um segmento-diâmetro**, **diagonais de um paralelogramo** (as diagonais se cortam no ponto médio) e **quarto vértice do paralelogramo**.

**Exemplo 3 (paralelogramo).** Três vértices consecutivos de um paralelogramo: A(1, 1), B(5, 2), C(6, 5). O vértice D, oposto a B, satisfaz: ponto médio de AC = ponto médio de BD. M_AC = (3,5; 3). Então D = 2M − B = (7 − 5; 6 − 2) = **D(2, 4)**. Conferência: AB = (4, 1) e DC = (4, 1), vetores iguais, como deve ser.

### 2.3 Baricentro

O **baricentro** G de um triângulo é o encontro das medianas e fica a 2/3 de cada vértice em relação à mediana (propriedade vista na Aula 15 do curso principal). Em coordenadas, é a **média aritmética dos três vértices**:

**G = ( (x_A + x_B + x_C)/3 ; (y_A + y_B + y_C)/3 )**

**Exemplo 1.** A(1, 2), B(5, 6), C(3, −2): G = (9/3; 6/3) = **(3, 2)**. Conferência pela mediana: M (ponto médio de BC) = (4, 2). G = A + (2/3)(M − A) = (1 + 2; 2 + 0) = (3, 2). Confere.

**Exemplo 2 (vértice desconhecido).** Dado G(2, 3), A(1, 1), B(4, 5): x_C = 3·2 − 1 − 4 = 1 e y_C = 3·3 − 1 − 5 = 3. **C(1, 3).**

## 3. Alinhamento de três pontos e área do triângulo

### 3.1 Determinante de três pontos

Para A, B, C, define-se o determinante

<pre>
    | x_A  y_A  1 |
D = | x_B  y_B  1 |
    | x_C  y_C  1 |
</pre>

que, desenvolvido, vale **D = x_A(y_B − y_C) + x_B(y_C − y_A) + x_C(y_A − y_B)**.

(Para quem prefere a regra de Sarrus: some as três diagonais "descendo" e subtraia as três "subindo".)

- **Condição de alinhamento (colinearidade): D = 0.**
- Se D ≠ 0, os três pontos formam triângulo, e **Área = |D| / 2**.

**Exemplo 1 (alinhamento com incógnita).** Para que valor de k os pontos A(1, 1), B(2, 3) e C(4, k) estão alinhados?

D = 1(3 − k) + 2(k − 1) + 4(1 − 3) = 3 − k + 2k − 2 − 8 = k − 7. D = 0 → **k = 7**.

Conferência pelo coeficiente angular: AB tem inclinação (3 − 1)/(2 − 1) = 2 e AC tem (7 − 1)/(4 − 1) = 2. Iguais: alinhados.

> **Atalho:** três pontos estão alinhados quando o coeficiente angular de AB é igual ao de AC (seção 4.3). Use o que for mais rápido.

**Exemplo 2 (área).** A(2, 1), B(7, 3), C(4, 8):

D = 2(3 − 8) + 7(8 − 1) + 4(1 − 3) = −10 + 49 − 8 = 31 → Área = **15,5**.

**Exemplo 3 (conferindo por base × altura).** A(1, 1), B(5, 1), C(3, 4): AB é horizontal, base 4; altura 3. Área = 4·3/2 = 6. Pelo determinante: D = 1(1 − 4) + 5(4 − 1) + 3(1 − 1) = −3 + 15 + 0 = 12 → 12/2 = **6**. Confere.

> **Pegadinha:** o determinante pode dar **negativo** (depende da ordem dos vértices, horário ou anti-horário). A área usa o **módulo**. Resposta de área nunca é negativa.

### 3.2 Área de polígono (regra do "cadarço")

Para um polígono de vértices P₁, P₂, ..., Pₙ listados em ordem, no sentido horário ou anti-horário:

**Área = ½ · | Σ (xᵢ·yᵢ₊₁ − xᵢ₊₁·yᵢ) |**, com Pₙ₊₁ = P₁.

**Exemplo.** Quadrilátero (0, 0), (4, 0), (5, 3), (1, 4):

- (0·0 − 4·0) = 0
- (4·3 − 5·0) = 12
- (5·4 − 1·3) = 17
- (1·0 − 0·4) = 0

Soma = 29 → Área = **14,5**. (Para o triângulo, a regra reproduz o determinante da seção 3.1.)

## 4. Equações da reta

### 4.1 As formas da equação

Uma reta do plano (não vertical) fica determinada por **dois pontos** ou por **um ponto e a inclinação**. Cada forma de escrever a equação tem seu uso.

| Forma | Equação | O que revela de imediato |
|---|---|---|
| **Geral** | ax + by + c = 0 (a e b não ambos nulos) | vale para qualquer reta, inclusive vertical |
| **Reduzida** | y = mx + n | m = coeficiente angular; n = coeficiente linear (corta o eixo y em (0, n)) |
| **Ponto-inclinação** | y − y₀ = m(x − x₀) | reta com inclinação m passando por (x₀, y₀) |
| **Segmentária** | x/p + y/q = 1 | corta os eixos em (p, 0) e (0, q) (p e q ≠ 0) |
| **Paramétrica** | x = x₀ + u·t ; y = y₀ + v·t | ponto (x₀, y₀) e vetor-direção (u, v); t é o parâmetro |

**Retas especiais:**

- **Horizontal**: y = k (coeficiente angular 0; paralela ao eixo x).
- **Vertical**: x = k (**não tem** coeficiente angular; paralela ao eixo y).
- **Eixo x**: y = 0. **Eixo y**: x = 0.
- **Passa pela origem**: c = 0 na forma geral (ou n = 0 na reduzida).

### 4.2 Coeficientes angular e linear

O **coeficiente angular** m é a tangente do ângulo α que a reta forma com o **eixo x**, medido no sentido anti-horário (0° ≤ α < 180°, α ≠ 90°):

**m = tg α = (y₂ − y₁)/(x₂ − x₁)** (para dois pontos da reta)

| Inclinação α | Coeficiente angular | Reta |
|---|---|---|
| 0° | 0 | horizontal |
| 30° | √3/3 | crescente |
| 45° | 1 | crescente |
| 60° | √3 | crescente |
| 90° | não existe | vertical |
| 120° | −√3 | decrescente |
| 135° | −1 | decrescente |

- m > 0: reta **crescente** (α agudo). m < 0: **decrescente** (α obtuso). m = 0: horizontal.
- O **coeficiente linear** n é a ordenada do ponto onde a reta corta o eixo y.

**Da forma geral para a reduzida:** em ax + by + c = 0 com b ≠ 0, isole y: **m = −a/b** e **n = −c/b**.

**Exemplo.** 2x + 3y − 12 = 0 → y = −(2/3)x + 4. Logo m = −2/3 e n = 4. Forma segmentária: 2x + 3y = 12 → **x/6 + y/4 = 1**, ou seja, corta os eixos em (6, 0) e (0, 4).

### 4.3 Como obter a equação da reta

**(a) Por dois pontos.** Calcule m e use ponto-inclinação.

Exemplo: A(1, 2) e B(3, 8). m = (8 − 2)/(3 − 1) = 3. Então y − 2 = 3(x − 1) → y = 3x − 1 → **3x − y − 1 = 0**.

Também pelo determinante de alinhamento: um ponto P(x, y) está na reta AB quando A, B, P estão alinhados:

<pre>
    | x  y  1 |
    | 1  2  1 | = 0   →   −6x + 2y + 2 = 0   →   3x − y − 1 = 0   (mesma reta)
    | 3  8  1 |
</pre>

**(b) Por um ponto e o coeficiente angular.** A reta que passa por (1, −2) com m = 3: y + 2 = 3(x − 1) → y = 3x − 5.

**(c) Pelos interceptos.** Corta o eixo x em (5, 0) e o eixo y em (0, 2): x/5 + y/2 = 1 → 2x + 5y − 10 = 0.

**(d) Da forma paramétrica.** x = 2 + 3t, y = −1 + 4t. O vetor-direção é (3, 4), logo m = 4/3. Eliminando t: t = (x − 2)/3 → y + 1 = (4/3)(x − 2) → 3y + 3 = 4x − 8 → **4x − 3y − 11 = 0**. Conferência: t = 0 dá (2, −1): 8 + 3 − 11 = 0 ✓; t = 1 dá (5, 3): 20 − 9 − 11 = 0 ✓.

### 4.4 Interseção de duas retas

O ponto comum é a solução do **sistema** formado pelas duas equações.

**Exemplo.** r: x + y = 5 e s: 2x − y = 1. Somando: 3x = 6 → x = 2 e y = 3. As retas se cortam em **(2, 3)**.

**Área entre a reta e os eixos.** A reta 2x + 5y − 10 = 0 corta os eixos em (5, 0) e (0, 2), formando com eles um triângulo retângulo de catetos 5 e 2: área = 5·2/2 = **5**. (Com a forma segmentária x/p + y/q = 1, a área é |p·q|/2.)

## 5. Posição relativa de duas retas, paralelismo e perpendicularidade

Sejam r: y = m₁x + n₁ e s: y = m₂x + n₂ (retas não verticais).

| Posição | Condição na forma reduzida |
|---|---|
| **Paralelas distintas** | m₁ = m₂ e n₁ ≠ n₂ |
| **Coincidentes** | m₁ = m₂ e n₁ = n₂ |
| **Concorrentes** | m₁ ≠ m₂ (cortam-se num único ponto) |
| **Perpendiculares** | m₁ · m₂ = −1 (caso particular de concorrentes) |

**Na forma geral** (a₁x + b₁y + c₁ = 0 e a₂x + b₂y + c₂ = 0), sem precisar isolar y:

| Posição | Condição |
|---|---|
| Paralelas distintas | a₁/a₂ = b₁/b₂ ≠ c₁/c₂ |
| Coincidentes | a₁/a₂ = b₁/b₂ = c₁/c₂ |
| Concorrentes | a₁/a₂ ≠ b₁/b₂ (ou a₁b₂ − a₂b₁ ≠ 0) |
| **Perpendiculares** | **a₁a₂ + b₁b₂ = 0** |

> **Macetes:**
>
> - **Paralela** a ax + by + c = 0: mesma "parte esquerda" ax + by e **troca o termo constante**. Descubra o novo c substituindo o ponto.
> - **Perpendicular** a ax + by + c = 0: troque a e b de lugar e **inverta um sinal**: bx − ay + c′ = 0. Descubra c′ substituindo o ponto.
> - Perpendicularidade com reta vertical: a perpendicular a x = k é horizontal (y = k′), e vice-versa. O produto m₁m₂ = −1 **não se aplica**, pois uma delas não tem m.

**Exemplo 1 (paralela e perpendicular por um ponto).** r: 2x − 3y + 5 = 0 e ponto P(1, 1).

- Paralela por P: 2x − 3y + c = 0; em P: 2 − 3 + c = 0 → c = 1. **2x − 3y + 1 = 0.**
- Perpendicular por P: 3x + 2y + c′ = 0; em P: 3 + 2 + c′ = 0 → c′ = −5. **3x + 2y − 5 = 0.** Conferência: a₁a₂ + b₁b₂ = 2·3 + (−3)·2 = 0 ✓.

**Exemplo 2 (parâmetro k).** As retas kx + 2y − 3 = 0 e 3x + y + 1 = 0:

- **Paralelas:** k/3 = 2/1 → k = 6. Os termos constantes têm razão −3/1 = −3, diferente de 2, então são paralelas distintas.
- **Perpendiculares:** 3k + 2·1 = 0 → **k = −2/3**.

**Exemplo 3 (retas "quase" paralelas).** kx + y − 1 = 0 e 4x + ky + 3 = 0. Paralelas: k/4 = 1/k → k² = 4 → k = ±2. Em ambos os casos a razão dos termos constantes é −1/3, diferente de ±1/2: paralelas distintas. Perpendiculares: 4k + k = 0 → **k = 0**.

**Exemplo 4 (mediatriz).** A **mediatriz** de AB é a reta perpendicular a AB pelo ponto médio (é o conjunto dos pontos equidistantes de A e B). Para A(1, 2) e B(5, 4): M = (3, 3); m_AB = 2/4 = 1/2; a mediatriz tem m = −2: y − 3 = −2(x − 3) → **2x + y − 9 = 0**. Conferência: o ponto (4, 1) está na mediatriz (8 + 1 − 9 = 0) e sua distância a A é √(9 + 1) = √10, a B é √(1 + 9) = √10 ✓.

### 5.1 Ângulo entre duas retas

O menor ângulo θ entre duas retas concorrentes, não perpendiculares e não verticais, é dado por

**tg θ = | (m₁ − m₂) / (1 + m₁·m₂) |** (0° < θ ≤ 90°)

Se 1 + m₁m₂ = 0, as retas são perpendiculares (θ = 90°).

**Exemplo 1.** y = 2x + 1 e y = (1/3)x − 4: tg θ = |(2 − 1/3)/(1 + 2/3)| = (5/3)/(5/3) = 1 → **θ = 45°**.

**Exemplo 2.** y = x (inclinação 45°) e y = √3·x (inclinação 60°): o ângulo entre elas é a diferença das inclinações, **15°**. Pela fórmula: tg θ = (√3 − 1)/(1 + √3) = 2 − √3 = tg 15° ✓.

> **Dica:** se você conhece as inclinações α₁ e α₂ (m = tg α), o ângulo entre as retas é |α₁ − α₂| (ou o suplemento, se passar de 90°). A fórmula acima é só a tangente dessa diferença.

## 6. Distância de ponto a reta

A distância do ponto P(x₀, y₀) à reta r: ax + by + c = 0 é

**d(P, r) = | a·x₀ + b·y₀ + c | / √(a² + b²)**

**Importante:** a reta precisa estar na **forma geral** (tudo de um lado, igual a zero) antes de aplicar a fórmula.

**Exemplo 1.** P(2, 3) e r: 3x + 4y − 5 = 0. Numerador: |6 + 12 − 5| = 13. Denominador: √(9 + 16) = 5. **d = 13/5 = 2,6.**

**Exemplo 2 (de P à reta y = x + 2).** Em forma geral: x − y + 2 = 0. P(4, 0): |4 − 0 + 2|/√2 = 6/√2 = **3√2**.

**Exemplo 3 (entre paralelas).** A distância entre r: 3x + 4y − 5 = 0 e s: 3x + 4y + 10 = 0 é a distância de **um ponto qualquer** de r a s. Fórmula direta, com mesmos a e b: |c₁ − c₂|/√(a² + b²) = |−5 − 10|/5 = **3**.

**Exemplo 4 (altura de triângulo).** A altura relativa ao lado BC é a distância de A à reta BC. Com isso, a **área = (BC · h)/2**, alternativa ao determinante.

> **Pegadinha:** esquecer o valor absoluto (distância não é negativa) e esquecer de passar para a forma geral. Se P está **sobre** a reta, o numerador é 0.

## 7. Circunferência

A **circunferência** é o conjunto dos pontos do plano que distam r (o **raio**) de um ponto fixo C(a, b), o **centro**. Pela fórmula da distância, P(x, y) pertence a ela quando d(P, C) = r. Elevando ao quadrado:

**Equação reduzida: (x − a)² + (y − b)² = r²**

Casos particulares:

- Centro na origem: **x² + y² = r²**.
- Passa pela origem: o ponto (0, 0) satisfaz a equação (a² + b² = r²).
- **Tangente ao eixo x**: |b| = r. **Tangente ao eixo y**: |a| = r.

### 7.1 Equação geral e como achar centro e raio

Desenvolvendo a reduzida, obtém-se a **equação geral**:

**x² + y² + Dx + Ey + F = 0** (coeficientes de x² e y² iguais a 1, **sem termo xy**)

com **centro C(−D/2 ; −E/2)** e **raio r = √(D²/4 + E²/4 − F)**.

Para ser mesmo uma circunferência, é preciso que **D²/4 + E²/4 − F > 0**. Se o resultado for 0, o "lugar geométrico" é um único ponto; se for negativo, é o conjunto vazio.

**Exemplo 1.** x² + y² − 6x + 4y − 12 = 0. Aqui D = −6, E = 4, F = −12. Centro: (3, −2). r² = 9 + 4 + 12 = 25 → **r = 5**. Pelo método de completar quadrados: (x² − 6x + 9) + (y² + 4y + 4) = 12 + 9 + 4 = 25 → (x − 3)² + (y + 2)² = 25 ✓.

**Exemplo 2 (não é circunferência).** x² + y² + 2x − 2y + 5 = 0: r² = 1 + 1 − 5 = −3 < 0. Não representa circunferência (conjunto vazio).

**Exemplo 3 (diâmetro dado).** Circunferência com diâmetro AB, A(1, 2) e B(7, 10): centro = ponto médio = (4, 6); raio = AB/2 = 10/2 = 5. **(x − 4)² + (y − 6)² = 25.**

**Exemplo 4 (por três pontos).** A circunferência que passa por (0, 0), (6, 0) e (0, 8). O ângulo no vértice (0, 0) é reto, então o segmento que liga (6, 0) a (0, 8) é um **diâmetro**: centro (3, 4), raio = √(36 + 64)/2 = 5. Equação: (x − 3)² + (y − 4)² = 25, isto é, **x² + y² − 6x − 8y = 0**. Conferência: (6, 0): 36 − 36 = 0 ✓; (0, 8): 64 − 64 = 0 ✓.

**Exemplo 5 (tangente a uma reta).** Circunferência de centro C(2, −1) tangente à reta 4x + 3y − 20 = 0. O raio é a distância do centro à reta: |8 − 3 − 20|/5 = 15/5 = 3. **(x − 2)² + (y + 1)² = 9.**

> **Regra de ouro:** circunferência tangente a uma reta ⇒ raio = distância do centro à reta.

### 7.2 Posição de um ponto em relação à circunferência

Calcule d² = (x₀ − a)² + (y₀ − b)² e compare com r²:

| Comparação | Posição do ponto |
|---|---|
| d² < r² | **interior** |
| d² = r² | **sobre** a circunferência |
| d² > r² | **exterior** |

**Exemplo.** Circunferência (x − 1)² + (y − 1)² = 9 e P(3, 3): d² = 4 + 4 = 8 < 9 → P é **interior**. Para Q(5, 2): d² = 16 + 1 = 17 > 9 → exterior.

### 7.3 Posição de uma reta em relação à circunferência

Há duas formas de decidir. Seja d a distância do centro à reta.

| Comparação | Posição | Pontos em comum |
|---|---|---|
| d < r | **secante** | 2 |
| d = r | **tangente** | 1 |
| d > r | **exterior** | 0 |

Alternativa: substituir a reta na circunferência e olhar o **discriminante Δ** da equação do 2º grau resultante (Δ > 0 secante; Δ = 0 tangente; Δ < 0 sem ponto comum).

**Exemplo 1 (substituição).** Circunferência x² + y² = 25 e reta y = x + 1:
x² + (x + 1)² = 25 → 2x² + 2x − 24 = 0 → x² + x − 12 = 0 → x = 3 ou x = −4.
Pontos: (3, 4) e (−4, −3). A reta é **secante**. O comprimento da corda é √(7² + 7²) = **7√2**. Conferência pela distância: d(O, reta) = 1/√2, e corda = 2√(r² − d²) = 2√(25 − 1/2) = 2√24,5 = 7√2 ✓.

**Exemplo 2 (valor de k para tangência).** y = x + k tangente a x² + y² = 8: d = |k|/√2 = r = 2√2 → |k| = 4 → **k = 4 ou k = −4**.

**Exemplo 3 (reta tangente por um ponto da circunferência).** Circunferência x² + y² = 25 e ponto T(3, 4) sobre ela. O raio OT tem inclinação 4/3; a tangente é perpendicular ao raio, logo m = −3/4: y − 4 = −(3/4)(x − 3) → 4y − 16 = −3x + 9 → **3x + 4y = 25**. (Macete: para x² + y² = r² e T(x₀, y₀), a tangente é **x₀·x + y₀·y = r²**.)

**Eixos.** A circunferência (x − 3)² + (y − 4)² = 25 tem r = 5 e distância do centro ao eixo x igual a 4 < 5: **secante** ao eixo x. Fazendo y = 0: (x − 3)² = 9 → x = 0 ou x = 6. Corta o eixo x em (0, 0) e (6, 0).

### 7.4 Posição relativa de duas circunferências

Com centros C₁, C₂, raios r₁, r₂ e d = distância entre os centros:

| Condição | Posição |
|---|---|
| d > r₁ + r₂ | exteriores (sem ponto comum) |
| d = r₁ + r₂ | **tangentes externamente** (1 ponto) |
| &#124;r₁ − r₂&#124; < d < r₁ + r₂ | **secantes** (2 pontos) |
| d = &#124;r₁ − r₂&#124; | **tangentes internamente** (1 ponto) |
| d < &#124;r₁ − r₂&#124; | uma dentro da outra (sem ponto comum) |
| d = 0 | concêntricas |

**Exemplo.** x² + y² = 4 (centro (0, 0), r = 2) e (x − 5)² + y² = 9 (centro (5, 0), r = 3): d = 5 = 2 + 3 → tangentes externas. Já x² + y² = 25 e (x − 1)² + y² = 16: d = 1 = 5 − 4 → tangentes internas (ponto comum (5, 0)).

## 8. Sistemas de equações lineares e a interpretação geométrica

O item 5 do edital termina com "sistemas de equações". A técnica de resolução (substituição, adição, comparação) está na Aula 08 do curso principal. Aqui interessa **o significado geométrico**.

### 8.1 Sistema 2 × 2: duas retas

Cada equação ax + by = c é uma **reta**. A solução do sistema é a **interseção** das duas retas:

| Situação das retas | Classificação do sistema | Soluções |
|---|---|---|
| **Concorrentes** | possível e determinado (SPD) | uma só (x, y) |
| **Coincidentes** | possível e indeterminado (SPI) | infinitas |
| **Paralelas distintas** | impossível (SI) | nenhuma |

Pelos coeficientes: com **D = a₁b₂ − a₂b₁**:

- **D ≠ 0** → SPD (retas concorrentes).
- **D = 0** → SPI se as razões a₁/a₂ = b₁/b₂ = c₁/c₂, e SI caso contrário.

**Exemplo 1.** x + y = 5 e 2x − y = 1: D = 1·(−1) − 2·1 = −3 ≠ 0 → SPD, solução (2, 3).

**Exemplo 2.** 2x + 4y = 6 e x + 2y = 3: a segunda, multiplicada por 2, dá a primeira. Retas **coincidentes** → SPI (infinitas soluções, todos os pontos da reta x + 2y = 3).

**Exemplo 3.** x + 2y = 3 e 2x + 4y = 7: mesmos coeficientes de x e y proporcionais, mas 3·2 = 6 ≠ 7. Retas **paralelas distintas** → SI.

**Exemplo 4 (parâmetro).** kx + 2y = 4 e 3x + y = 2: D = k·1 − 3·2 = k − 6.

- Se k ≠ 6: SPD.
- Se k = 6: as equações 6x + 2y = 4 e 3x + y = 2 são proporcionais (a primeira é o dobro da segunda): SPI.
- Não existe k que torne o sistema impossível: quando k = 6, o lado direito (4 e 2) também acompanha a proporção 2 : 1.

### 8.2 Sistema 3 × 3 (visão geométrica)

Cada equação ax + by + cz = d representa um **plano** no espaço. A solução é a interseção dos três planos: um **ponto** (SPD, determinante dos coeficientes ≠ 0), uma **reta** ou um **plano** (SPI), ou nenhum ponto comum (SI). O cálculo continua sendo por escalonamento, substituição ou regra de Cramer; o determinante dos coeficientes diferente de zero garante solução única.

### 8.3 Sistema com uma equação do 2º grau

Quando o sistema mistura uma reta e uma circunferência (ou parábola), substitui-se a reta na outra equação (seção 7.3). O número de soluções é o número de pontos de interseção.

## 9. Resumo, pegadinhas e exercícios

### 9.1 Quadro de fórmulas

| Assunto | Fórmula |
|---|---|
| Distância entre pontos | d = √[(x₂ − x₁)² + (y₂ − y₁)²] |
| Ponto médio | M = ((x₁ + x₂)/2 ; (y₁ + y₂)/2) |
| Baricentro | G = ((x_A + x_B + x_C)/3 ; (y_A + y_B + y_C)/3) |
| Alinhamento | det[x y 1] = 0 |
| Área do triângulo | S = ½ · &#124;det[x y 1]&#124; |
| Coef. angular | m = (y₂ − y₁)/(x₂ − x₁) = tg α |
| Ponto-inclinação | y − y₀ = m(x − x₀) |
| Geral → reduzida | m = −a/b ; n = −c/b |
| Paralelas | m₁ = m₂ ; (geral) a₁/a₂ = b₁/b₂ |
| Perpendiculares | m₁·m₂ = −1 ; (geral) a₁a₂ + b₁b₂ = 0 |
| Ângulo entre retas | tg θ = &#124;(m₁ − m₂)/(1 + m₁m₂)&#124; |
| Distância ponto-reta | &#124;ax₀ + by₀ + c&#124; / √(a² + b²) |
| Circunferência (reduzida) | (x − a)² + (y − b)² = r² |
| Circunferência (geral) | x² + y² + Dx + Ey + F = 0 ; C(−D/2, −E/2) ; r² = D²/4 + E²/4 − F |

### 9.2 Pegadinhas frequentes

1. **Sinal na equação reduzida da circunferência.** (x + 2)² + (y − 3)² = 16 tem centro **(−2, 3)**, não (2, −3).
2. **Raio × raio ao quadrado.** Em (x − 1)² + y² = 9, o raio é 3, não 9.
3. **Reta vertical** não tem coeficiente angular: não use m.
4. **Distância ponto-reta:** reta na forma geral; módulo no numerador.
5. **Área de triângulo:** módulo do determinante, dividido por 2 (esquecer o ½ é erro clássico).
6. **Paralelas × coincidentes:** m₁ = m₂ não basta; compare também o termo constante.
7. **Perpendicular:** m₂ = −1/m₁ (inverte **e** troca o sinal). Se m₁ = 2, m₂ = −1/2.
8. **Equação geral de circunferência:** os coeficientes de x² e y² devem ser iguais (e não pode haver xy). Se vierem iguais mas diferentes de 1, divida tudo por esse valor antes de aplicar as fórmulas.
9. **Ponto médio × baricentro:** o ponto médio tem divisão por 2 (dois pontos); o baricentro, por 3 (três vértices).
10. **Dados incompatíveis com o enunciado:** se o discriminante da circunferência der negativo, não existe circunferência.

### 9.3 Exercícios autorais (gabarito e resolução)

**1.** A distância entre A(−2, 1) e B(4, 9) é: (A) 6 (B) 8 (C) 10 (D) 12 (E) 14.
**Resolução:** √(6² + 8²) = 10. **Gabarito C.**

**2.** O ponto médio do segmento de extremos (3, −1) e (−5, 7) é: (A) (−1, 3) (B) (1, 3) (C) (−1, −3) (D) (−4, 3) (E) (2, 3).
**Resolução:** ((3 − 5)/2 ; (−1 + 7)/2) = (−1, 3). **Gabarito A.**

**3.** A reta que passa por (1, −2) e tem coeficiente angular 3 tem equação: (A) y = 3x + 5 (B) y = 3x − 5 (C) y = −3x + 1 (D) y = 3x − 1 (E) y = x/3 − 2.
**Resolução:** y + 2 = 3(x − 1) → y = 3x − 5. **Gabarito B.**

**4.** A área do triângulo formado pela reta 2x + 5y − 10 = 0 e pelos eixos coordenados é: (A) 2 (B) 5 (C) 7 (D) 10 (E) 20.
**Resolução:** interceptos (5, 0) e (0, 2): 5·2/2 = 5. **Gabarito B.**

**5.** As retas kx + y − 1 = 0 e 4x + ky + 3 = 0 são paralelas distintas para: (A) k = 0 (B) k = 2 apenas (C) k = ±2 (D) k = 4 (E) k = −1.
**Resolução:** k/4 = 1/k → k² = 4. Para k = 2: razões 1/2 = 1/2 ≠ −1/3 (paralelas distintas). Para k = −2: −1/2 = −1/2 ≠ −1/3 (idem). **Gabarito C.**

**6.** A distância do ponto P(1, 2) à reta 5x + 12y − 3 = 0 é: (A) 1 (B) 2 (C) 13/5 (D) 26 (E) 3.
**Resolução:** |5 + 24 − 3|/13 = 26/13 = 2. **Gabarito B.**

**7.** O centro e o raio da circunferência x² + y² − 4x + 6y − 3 = 0 são: (A) C(2, −3) e r = 4 (B) C(−2, 3) e r = 4 (C) C(2, −3) e r = 16 (D) C(4, −6) e r = 3 (E) C(2, 3) e r = 4.
**Resolução:** C = (−D/2, −E/2) = (2, −3); r² = 4 + 9 + 3 = 16 → r = 4. **Gabarito A.**

**8.** O ponto P(3, 3) em relação à circunferência (x − 1)² + (y − 1)² = 9 é: (A) exterior (B) interior (C) pertencente à circunferência (D) o centro (E) não é possível decidir.
**Resolução:** d² = 4 + 4 = 8 < 9. **Gabarito B.**

**9.** Os valores de k para que a reta y = x + k seja tangente à circunferência x² + y² = 8 são: (A) ±2 (B) ±4 (C) ±8 (D) ±2√2 (E) 0.
**Resolução:** |k|/√2 = 2√2 → |k| = 4. **Gabarito B.**

**10.** O sistema kx + 2y = 4, 3x + y = 2 é possível e determinado se, e somente se: (A) k = 6 (B) k ≠ 6 (C) k ≠ 3 (D) k ≠ −6 (E) k = 0.
**Resolução:** D = k − 6 ≠ 0. **Gabarito B.**

## Fontes

Conteúdo didático padrão de geometria analítica plana (nível médio), redigido de forma original. Todas as fórmulas são resultados clássicos e foram conferidas por cálculo (exemplos numéricos verificados em Python em 08/10/2026). Edital: Anexo II do edital do cargo de 2º Tenente do CBMPE (Matemática, item 5). Panorama de estilo da banca: levantamento interno de questões de Matemática da AOCP do projeto (`content/style/aocp-profile.json`).
