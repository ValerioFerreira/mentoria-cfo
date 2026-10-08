---
id: mat-complementos-edital
subject: matematica
title: Complementos de Matemática do edital
short: Complementos do edital
subtitle: Simetrias de figuras, retas no espaço, divisibilidade, fatoração, MDC e MMC, divisão proporcional, polinômios, funções racionais e equações exponenciais (itens 1.3, 1.8, 2.5, 2.6, 4.4, 4.5 e 4.6 do edital de Matemática)
weight: 0.08
order: 2
resolves: mat-simetrias-polinomios-divisibilidade
---

## O que este material cobre e como estudar

Pessoal, a auditoria do curso principal de Matemática encontrou itens do edital que ele **não ensina** ou ensina só de passagem. Este complemento reúne os que sobraram, na ordem do edital:

| Item do edital | Assunto | Seção |
|---|---|---|
| 2.6 | Simetrias de figuras planas ou espaciais | 1 |
| 2.5 | Posições de retas (no espaço) | 2 |
| 1.3 | Divisibilidade, fatoração, MDC e MMC | 3 |
| 1.8 | Divisão proporcional (complemento de razões e proporções) | 4 |
| 4.4 | Funções polinomiais (grau 3 ou mais) | 5 |
| 4.5 | Funções racionais | 6 |
| 4.6 / 4.8 | Equações e inequações exponenciais como tópico | 7 |

O que o curso principal já traz e **não é repetido aqui**: Girard para o 2º grau e equações biquadradas (Aula 08), expressões algébricas e operações com polinômios (Aula 01), MMC por decomposição e a ideia de primo (Aula 03), paralelas cortadas por transversal (Aula 15) e a função exponencial, com gráficos e propriedades (Aula 12). A geometria analítica (distância, retas, circunferência) está em outro complemento.

> **Como estudar:** são sete blocos pequenos e independentes. Em cada um, leia a regra, refaça os exemplos **sem olhar** e, ao final, faça os 12 exercícios da seção 8. A prova costuma cobrar esses temas em questões curtas, com uma ideia só por questão.

> **Sobre a prova:** no banco de questões de Matemática da AOCP que analisamos para o projeto (39 questões), o padrão é enunciado curto, 5 alternativas e alternativas numéricas curtas, com cerca de 30% pedindo cálculo. Nenhum desses sete temas aparece nessa amostra, mas todos estão no edital do CBM-PE. Treine a versão **direta** de cada um (aplicar a regra, uma conta).

## 1. Simetrias de figuras planas e espaciais (item 2.6)

### 1.1 Os quatro movimentos que deixam a figura "igual"

Uma **simetria** de uma figura é um movimento que a leva **exatamente sobre ela mesma**. Para o edital, importam:

| Tipo | O que é | Como reconhecer |
|---|---|---|
| **Simetria axial** (reflexão) | A figura "dobra" sobre uma reta (**eixo de simetria**) e as duas metades coincidem | cada ponto tem um "par" do outro lado do eixo, à mesma distância, e o segmento que os une é perpendicular ao eixo |
| **Simetria central** | Rotação de **180°** em torno de um ponto (**centro de simetria**) | cada ponto P tem um par P′ tal que o centro é o **ponto médio** de PP′ |
| **Simetria rotacional** | Rotação de um ângulo menor que 360° em torno de um ponto que leva a figura nela mesma | a figura "se repete" ao girar; um polígono regular de n lados repete a cada **360°/n** |
| **Translação** | Deslocamento sem girar (padrões e frisos) | a figura se repete a intervalos regulares ao longo de uma direção |

A simetria central é um caso particular de simetria rotacional (a de 180°). Quando se diz que uma figura "tem simetria rotacional de ordem n", quer-se dizer que ela coincide consigo mesma em n posições (contando a original) ao girar de 360°/n em 360°/n.

> **Macete 1:** dois eixos de simetria **perpendiculares** implicam a existência de centro de simetria (a composição das duas dobras é a rotação de 180°). A recíproca é falsa: o paralelogramo tem centro e nenhum eixo.
>
> **Macete 2:** figura com **centro de simetria** tem, para cada ponto, o seu oposto: por isso, em polígonos, os lados opostos são paralelos e iguais.

### 1.2 Simetria de figuras planas

| Figura | Eixos de simetria | Centro de simetria | Menor rotação que a repete |
|---|---|---|---|
| Segmento de reta | 2 (a mediatriz e a reta que o contém) | sim (ponto médio) | 180° |
| Círculo / circunferência | infinitos (qualquer diâmetro) | sim (o centro) | qualquer ângulo |
| Triângulo equilátero | 3 | não | 120° |
| Triângulo isósceles (não equilátero) | 1 | não | — |
| Triângulo escaleno | 0 | não | — |
| Quadrado | 4 | sim | 90° |
| Retângulo (não quadrado) | 2 | sim | 180° |
| Losango (não quadrado) | 2 (as diagonais) | sim | 180° |
| Paralelogramo (nem retângulo, nem losango) | **0** | **sim** | 180° |
| Trapézio isósceles | 1 | não | — |
| Trapézio escaleno ou retângulo | 0 | não | — |
| Pipa (deltoide) | 1 (a diagonal principal) | não | — |
| Pentágono regular | 5 | não | 72° |
| Hexágono regular | 6 | sim | 60° |
| Octógono regular | 8 | sim | 45° |
| Elipse (não círculo) | 2 | sim | 180° |

**Polígono regular de n lados:** tem **n eixos de simetria** (se n é ímpar, cada eixo liga um vértice ao ponto médio do lado oposto; se n é par, há n/2 eixos pelos vértices opostos e n/2 pelos pontos médios dos lados opostos); gira em **360°/n**; tem **centro de simetria apenas quando n é par**.

> **Pegadinhas clássicas:**
>
> - O **paralelogramo** não tem eixo de simetria (quem diz o contrário confunde com o losango). Mas tem centro.
> - Os eixos do **retângulo** são as **mediatrizes dos lados**, não as diagonais. Os do **losango** são as **diagonais**, não as mediatrizes.
> - Polígono regular de lados ímpares (triângulo equilátero, pentágono) **não** tem centro de simetria.

**Letras como figuras** (alfabeto de bastão, maiúsculo): com eixo vertical: A H I M O T U V W X Y. Com eixo horizontal: B C D E H I K O X. Com centro de simetria (rotação de 180°): H I N O S X Z. As letras **N, S e Z** têm centro, mas **nenhum eixo**.

### 1.3 Simetria em coordenadas e em gráficos

Para um ponto P(a, b), os simétricos em relação aos eixos, à origem e às bissetrizes seguem as regras do quadro do complemento de Geometria analítica (por exemplo: eixo x → (a, −b); origem → (−a, −b); bissetriz y = x → (b, a)). Nos gráficos de funções:

| Operação sobre f(x) | Efeito no gráfico |
|---|---|
| f(−x) | reflexão em relação ao **eixo y** |
| −f(x) | reflexão em relação ao **eixo x** |
| f(x) é **par** (f(−x) = f(x)) | o gráfico é simétrico em relação ao **eixo y** |
| f(x) é **ímpar** (f(−x) = −f(x)) | o gráfico é simétrico em relação à **origem** |
| função inversa f⁻¹ | reflexão do gráfico de f em relação à reta **y = x** |
| parábola y = ax² + bx + c | simétrica em relação à reta vertical **x = −b/2a** |

**Exemplo.** y = x² − 4x + 3 tem eixo x = −(−4)/(2·1) = 2. Suas raízes são 1 e 3, simétricas em relação a x = 2 (ambas a distância 1), e o vértice é (2, −1).

### 1.4 Simetria de figuras espaciais

No espaço há três tipos: **simetria em relação a um plano** (plano de simetria: cada metade é a "imagem no espelho" da outra), **em relação a um eixo** (rotação em torno de uma reta) e **em relação a um ponto** (centro de simetria).

| Sólido | Planos de simetria | Eixos de rotação | Centro de simetria |
|---|---|---|---|
| **Cubo** | **9** (3 paralelos às faces + 6 que contêm duas arestas opostas) | 13 (3 pelos centros de faces opostas, 4 pelas diagonais, 6 pelos pontos médios de arestas opostas) | sim |
| Octaedro regular | 9 | 13 | sim |
| Paralelepípedo reto-retângulo (3 dimensões diferentes) | 3 (paralelos às faces, pelo meio) | 3 | sim |
| Tetraedro regular | 6 | 7 | não |
| Prisma reto de base regular de n lados | n + 1 | — | sim, se n é par |
| Pirâmide regular de base de n lados | n | 1 (pelo vértice e centro da base) | não |
| Cilindro reto circular | infinitos (os que contêm o eixo) + 1 (o perpendicular ao eixo, pelo meio) | infinitos | sim |
| Cone reto circular | infinitos (os que contêm o eixo) | 1 | não |
| Esfera | infinitos | infinitos | sim (o centro) |

(As contagens do cubo e do tetraedro foram conferidas por computador, listando todas as transformações que levam o sólido nele mesmo: cubo, 9 planos e 13 eixos; tetraedro regular, 6 planos.)

> **O que mais cai:** "quantos planos de simetria tem o cubo?" (**9**), "o paralelepípedo reto-retângulo tem centro de simetria?" (sim) e "a pirâmide quadrangular regular tem quantos planos?" (**4**: dois pelas diagonais da base e dois pelos pontos médios dos lados opostos).
>
> **Macete do prisma:** os planos **verticais** do prisma regular coincidem com os eixos do polígono da base (n deles); soma-se **1** plano horizontal (o do meio). Por isso o prisma triangular regular tem 4 planos e o hexagonal, 7.

## 2. Posições de retas (no plano e no espaço) — item 2.5

### 2.1 No plano

Duas retas de um mesmo plano são:

- **coincidentes** (infinitos pontos comuns);
- **paralelas distintas** (nenhum ponto comum);
- **concorrentes** (um ponto comum), e, quando formam 90°, **perpendiculares**.

(A reta cortada por transversal e os ângulos correspondentes, alternos e colaterais estão na Aula 15. A condição analítica de paralelismo e perpendicularidade está no complemento de Geometria analítica.)

### 2.2 No espaço: o novo caso, as retas reversas

No espaço, duas retas **distintas** podem ser:

| Posição | Definição | Pontos comuns | Coplanares? |
|---|---|---|---|
| **Concorrentes** | têm um ponto em comum | 1 | sim |
| **Paralelas distintas** | não têm ponto comum e estão num mesmo plano | 0 | sim |
| **Reversas** | **não** têm ponto comum e **não** existe plano que contenha as duas | 0 | **não** |

(Coincidentes: mesma reta.)

> **Ideia-chave:** "não se encontram" não basta para serem paralelas! Duas retas que não se cortam podem ser **paralelas** (se coplanares) ou **reversas** (se não coplanares). Exemplo do cotidiano: uma rua que passa por baixo de um viaduto e a pista do viaduto são retas reversas.

**Retas ortogonais:** duas retas reversas são ortogonais quando o ângulo entre elas é 90°. O **ângulo entre reversas** mede-se traçando, por um ponto qualquer, uma paralela a cada uma e tomando o ângulo entre essas paralelas. **Perpendiculares** são concorrentes que formam 90°; **ortogonais** é o termo geral (inclui as reversas).

**No cubo.** Considere o cubo ABCDEFGH, com ABCD na base e E, F, G, H acima de A, B, C, D, respectivamente.

- AB e CG: não têm ponto comum, não são coplanares → **reversas**, e ortogonais (CG é vertical e AB, horizontal).
- AB e EF: **paralelas** (mesma direção, num mesmo plano, a face lateral ABFE).
- AB e AD: **concorrentes** (perpendiculares) em A.
- Cada aresta do cubo tem **3 paralelas, 4 concorrentes e 4 reversas** entre as outras 11. Como são 12 arestas, há 12·4/2 = **24 pares** de arestas reversas (conferido por computador).

### 2.3 Reta e plano, e dois planos

| Situação | Posições possíveis |
|---|---|
| **Reta × plano** | reta **contida** no plano; **secante** (1 ponto comum, e então **perpendicular** ou **oblíqua**); **paralela** (nenhum ponto comum) |
| **Plano × plano** | **coincidentes**; **paralelos** (nenhum ponto comum); **secantes** (interseção é uma reta; se o ângulo é 90°, são **perpendiculares**) |

**Propriedades que caem em prova:**

1. Se uma reta é paralela a duas outras, essas duas são paralelas entre si (transitividade no espaço).
2. Uma reta é **perpendicular a um plano** quando é perpendicular a **todas** as retas do plano; basta ser perpendicular a **duas retas concorrentes** dele.
3. Por **três pontos não colineares** passa **um único plano**. Também determinam um plano: uma reta e um ponto fora dela; duas retas concorrentes; duas retas paralelas distintas. **Duas retas reversas não determinam plano.**
4. Se uma reta paralela a um plano está contida num segundo plano que corta o primeiro, ela é paralela à interseção dos dois planos.
5. Dois planos perpendiculares a uma mesma reta são paralelos entre si.

**Quantos planos?** Com 4 pontos, sendo **3 a 3 não colineares**, há no máximo C(4, 3) = 4 planos (e exatamente 1 se os 4 forem coplanares). Com n pontos em posição geral, no máximo C(n, 3) planos (para n = 5: 10).

## 3. Divisibilidade, fatoração, MDC e MMC (item 1.3)

### 3.1 Critérios de divisibilidade

| Divisor | Regra | Exemplo |
|---|---|---|
| **2** | último algarismo par (0, 2, 4, 6, 8) | 4.318 |
| **3** | soma dos algarismos divisível por 3 | 4.212: 4+2+1+2 = 9 |
| **4** | os dois últimos algarismos formam número divisível por 4 (ou são 00) | 7.324: 24 = 4·6 |
| **5** | termina em 0 ou 5 | 1.275 |
| **6** | divisível por 2 **e** por 3 | 5.634 |
| **8** | os três últimos algarismos formam número divisível por 8 | 12.376: 376 = 8·47 |
| **9** | soma dos algarismos divisível por 9 | 5.184: 18 |
| **10** | termina em 0 | 3.470 |
| **11** | soma dos algarismos de ordem ímpar menos a dos de ordem par (contando da direita) dá 0 ou múltiplo de 11 | 91.531: (1+5+9) − (3+1) = 11 |
| **12** | divisível por 3 **e** por 4 | 8.136 |
| **15** | divisível por 3 **e** por 5 | 2.145 |
| **25** | termina em 00, 25, 50 ou 75 | 6.475 |
| **7** | tire o último algarismo, **subtraia o dobro dele** do que sobrou; repita; o resultado deve ser 0 ou múltiplo de 7 | 1.442: 144 − 4 = 140 → 14 − 0 = 14 ✓ |

(Os exemplos foram conferidos um a um por cálculo: 4.212 = 3·1.404; 5.184 = 9·576; 91.531 = 11·8.321; 8.136 = 12·678; 2.145 = 15·143; 1.442 = 7·206.)

> **Regra geral para divisores compostos:** para testar um divisor composto, use critérios de divisores **primos entre si** cujo produto é o divisor. Divisível por 6 = por 2 e por 3 (primos entre si). **Mas** divisível por 4 e por 6 **não** implica divisível por 24 (4 e 6 não são primos entre si; 12 é divisível por 4 e por 6 e não por 24).

**Exemplo 1 (algarismo faltando).** Para que 4A12 seja divisível por 3: 4 + A + 1 + 2 = 7 + A deve ser múltiplo de 3. A ∈ {2, 5, 8}.

**Exemplo 2 (dois critérios).** Para que 2A58B seja divisível por 45 (= 5 · 9): termina em 0 ou 5, então B ∈ {0, 5}; e a soma 2 + A + 5 + 8 + B = 15 + A + B deve ser múltiplo de 9. Se B = 0: A = 3 (soma 18) e o número é 23.580. Se B = 5: 20 + A múltiplo de 9, A = 7 (soma 27) e o número é 27.585. Conferência: 23.580 = 45·524 e 27.585 = 45·613.

**Exemplo 3 (regra do 11).** O número 9A3 é divisível por 11: (3 + 9) − A = 12 − A deve ser múltiplo de 11 → A = 1 (913 = 11·83).

**Para 7, 11 e 13 juntos:** como 7 · 11 · 13 = 1.001, vale um truque: separe o número em **blocos de três algarismos** (da direita) e faça a soma alternada dos blocos (bloco1 − bloco2 + bloco3 − ...). O resto dessa soma, na divisão por 7, por 11 ou por 13, é o mesmo do número original. Exemplo: 3.465.008 → 8 − 465 + 3 = −454; e −454 = −65·7 + 1, logo o resto de 3.465.008 por 7 é 1 (conferido: 3.465.008 = 7·495.001 + 1).

### 3.2 Números primos e decomposição em fatores primos

- **Primo:** natural maior que 1 com exatamente dois divisores (1 e ele mesmo). O **2 é o único primo par**; o 1 **não** é primo.
- **Teste de primalidade:** para saber se n é primo, divida pelos primos até **√n**. Exemplo: 197 (√197 ≈ 14,03): não é divisível por 2, 3, 5, 7, 11 nem 13 → **primo**.
- **Teorema fundamental da aritmética:** todo natural maior que 1 se escreve, de modo único (a menos da ordem), como produto de primos. Exemplo: 360 = 2³ · 3² · 5.

**Quantidade de divisores positivos:** se n = p^a · q^b · r^c, então

**nº de divisores = (a + 1)(b + 1)(c + 1)**

360 = 2³ · 3² · 5¹ → 4 · 3 · 2 = **24 divisores**. 1.260 = 2² · 3² · 5 · 7 → 3 · 3 · 2 · 2 = **36**. (Os dois valores foram conferidos contando divisores por força bruta.)

**Soma dos divisores:** σ(n) = [(p^(a+1) − 1)/(p − 1)] · [(q^(b+1) − 1)/(q − 1)] · ... Para 360: (2⁴−1)/(2−1) · (3³−1)/(3−1) · (5²−1)/(5−1) = 15 · 13 · 6 = **1.170**.

> **Macete:** um número tem quantidade **ímpar** de divisores se, e somente se, é **quadrado perfeito** (todos os expoentes pares).

### 3.3 Fatoração algébrica

Fatorar é transformar soma em produto. Os casos que mais aparecem:

| Caso | Forma | Exemplo |
|---|---|---|
| Fator comum | ax + ay = a(x + y) | 6x² − 9x = 3x(2x − 3) |
| Agrupamento | ax + ay + bx + by = (a + b)(x + y) | x³ + x² + 2x + 2 = (x + 1)(x² + 2) |
| Diferença de quadrados | a² − b² = (a + b)(a − b) | x² − 9 = (x + 3)(x − 3) |
| Quadrado perfeito | a² ± 2ab + b² = (a ± b)² | 4x² − 12x + 9 = (2x − 3)² |
| Soma/diferença de cubos | a³ ± b³ = (a ± b)(a² ∓ ab + b²) | x³ − 8 = (x − 2)(x² + 2x + 4) |
| Cubo perfeito | a³ ± 3a²b + 3ab² ± b³ = (a ± b)³ | x³ + 6x² + 12x + 8 = (x + 2)³ |
| Trinômio x² + Sx + P | (x + r)(x + s), com r + s = S e rs = P | x² − 5x + 6 = (x − 2)(x − 3) |

**Aplicações em prova:**

- **Cálculo mental:** 101² − 99² = (101 + 99)(101 − 99) = 200 · 2 = **400**. Também 2.025² − 2.024² = (2.025 + 2.024) · 1 = **4.049**.
- **Simplificar frações algébricas:** (x² − 9)/(x² + 6x + 9) = (x − 3)(x + 3)/(x + 3)² = **(x − 3)/(x + 3)**, com x ≠ −3. Outro: (x³ − 8)/(x² − 4) = (x − 2)(x² + 2x + 4)/[(x − 2)(x + 2)] = (x² + 2x + 4)/(x + 2), com x ≠ ±2.

> **Atenção:** ao cancelar um fator, **registre a restrição** (x ≠ ...). Esse detalhe é o que diferencia uma função racional de sua "versão simplificada" (veja a seção 6).

### 3.4 MDC e MMC

- **MDC(a, b):** maior número que divide ambos. **MMC(a, b):** menor múltiplo comum positivo.
- Por **decomposição**: MDC = produto dos fatores primos **comuns** com o **menor** expoente; MMC = produto de **todos** os primos com o **maior** expoente.
- **Primos entre si** (coprimos): MDC = 1. Dois números consecutivos são sempre primos entre si.
- Para dois números: **MDC(a, b) · MMC(a, b) = a · b**. (Vale só para **dois** números.)

**Algoritmo de Euclides** (divisões sucessivas): o MDC é o último resto não nulo. Para MDC(252, 198):

<pre>
252 = 1 · 198 + 54
198 = 3 ·  54 + 36
 54 = 1 ·  36 + 18
 36 = 2 ·  18 +  0     →  MDC(252, 198) = 18
</pre>

Pela decomposição: 252 = 2² · 3² · 7 e 198 = 2 · 3² · 11 → comuns: 2 · 3² = 18 ✓. MMC = 252 · 198 / 18 = **2.772**.

**Problemas típicos:**

1. **"Maior tamanho possível" (MDC).** Duas cordas de 252 m e 198 m são cortadas em pedaços iguais, de maior comprimento possível, sem sobra. Cada pedaço mede MDC = 18 m; há 252/18 + 198/18 = 14 + 11 = **25 pedaços**.
2. **Ladrilhos (MDC).** Piso de 6,30 m × 4,20 m com ladrilhos quadrados inteiros, os maiores possíveis: 630 cm e 420 cm → MDC = 210 cm; usam-se (630/210) · (420/210) = 3 · 2 = **6 ladrilhos**.
3. **"Voltam a coincidir" (MMC).** Três viaturas passam por um posto a cada 12, 18 e 30 minutos e saíram juntas às 8 h. MMC(12, 18, 30) = 180 min: voltam a coincidir às **11 h**.
4. **Incógnita.** MDC(a, b) = 12, MMC(a, b) = 180 e a = 36. Então b = 12 · 180 / 36 = **60**.
5. **Agrupamento.** Em um grupo com 48, 72 e 120 pessoas, formam-se equipes iguais, o maior número possível por equipe, sem misturar categorias: MDC(48, 72, 120) = **24** pessoas por equipe.

> **Como saber se é MDC ou MMC?** Se o problema fala em **dividir, cortar, repartir em partes iguais, o maior possível** → **MDC**. Se fala em **"quando voltam a se encontrar", "de quanto em quanto tempo", o menor possível** → **MMC**.

## 4. Divisão proporcional (item 1.8)

A **divisão proporcional** reparte uma quantidade T em partes proporcionais a números dados. O curso principal traz razão, proporção e grandezas proporcionais (Aula 03); aqui, só a técnica da divisão.

**Diretamente proporcional** a a, b, c: cada parte é k vezes o número, com k = T / (a + b + c).

**Inversamente proporcional** a a, b, c: a parte é **diretamente** proporcional aos **inversos** 1/a, 1/b, 1/c. Reduza ao mesmo denominador (MMC) para trabalhar com inteiros.

**Mista** (diretamente a um conjunto e inversamente a outro): o peso de cada parte é o **produto** do número da direta pelo **inverso** do número da inversa.

**Exemplo 1 (direta).** Dividir R$ 3.600 em partes diretamente proporcionais a 2, 3 e 4. Soma = 9, k = 400 → R$ **800, R$ 1.200 e R$ 1.600**.

**Exemplo 2 (inversa).** Dividir R$ 3.600 em partes inversamente proporcionais a 2, 3 e 6. Inversos: 1/2, 1/3, 1/6 = 3/6, 2/6, 1/6 → pesos 3, 2, 1 (soma 6, k = 600) → R$ **1.800, R$ 1.200 e R$ 600**. (A maior parte vai para o **menor** número.)

**Exemplo 3 (mista).** Dividir R$ 1.020 em partes diretamente proporcionais a 3 e 5 e inversamente proporcionais a 2 e 5, respectivamente. Pesos: 3/2 e 5/5 = 1 → razão 3/2 : 1 = 3 : 2 (soma 5, k = 204) → R$ **612 e R$ 408**.

> **Pegadinha:** em "inversamente proporcional", o **maior número recebe a menor parte**. Se, no seu resultado, o maior número ficou com a maior parte, você esqueceu de inverter.

## 5. Funções polinomiais de grau 3 ou mais (item 4.4)

### 5.1 Definição, grau e operações

Um **polinômio** de grau n é P(x) = aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₁x + a₀, com aₙ ≠ 0 (o **coeficiente líder**) e a₀ o **termo independente**. A **função polinomial** associada é x → P(x).

- **Valor numérico:** P(a) é o resultado de substituir x por a. **Raiz** (ou zero) é um número a com P(a) = 0.
- P(0) = a₀ (o gráfico corta o eixo y em (0, a₀)). P(1) = soma dos coeficientes.
- **Identidade:** dois polinômios são iguais quando têm os mesmos coeficientes, termo a termo. Exemplo: a(x − 1) + b(x + 2) ≡ 3x + 3 → a + b = 3 e −a + 2b = 3 → b = 2, a = 1.
- **Graus:** gr(P · Q) = gr P + gr Q; gr(P + Q) ≤ máx(gr P, gr Q); no quociente, gr(P/Q) = gr P − gr Q; e o **resto** da divisão por D tem grau **menor** que o de D.

### 5.2 Divisão de polinômios, teorema do resto e Briot-Ruffini

**Divisão euclidiana:** P(x) = D(x) · Q(x) + R(x), com gr R < gr D (ou R = 0). Se R = 0, P é **divisível** por D.

**Teorema do resto:** o resto da divisão de P(x) por **(x − a)** é **P(a)**. Com divisor (ax + b), o resto é P(−b/a).

**Teorema de D'Alembert:** P é divisível por (x − a) **se, e somente se**, P(a) = 0. Ou seja: **a é raiz de P ⇔ (x − a) é fator de P**.

**Dispositivo de Briot-Ruffini** (divisão por x − a, de forma rápida): escreva os coeficientes de P (todos, inclusive os zeros) e "a" à esquerda; **baixe** o primeiro coeficiente; **multiplique** por a e **some** ao próximo; e repita. O último número é o **resto**; os demais são os coeficientes do **quociente** (grau uma unidade menor).

Dividir P(x) = 2x³ − 3x² + 4x − 5 por (x − 2):

<pre>
 2 |  2    −3     4     −5
   |  2     1     6      7
   (2) ; 2·2 + (−3) = 1 ; 2·1 + 4 = 6 ; 2·6 + (−5) = 7
</pre>

Quociente Q(x) = 2x² + x + 6 e resto R = **7**. Conferência pelo teorema do resto: P(2) = 16 − 12 + 8 − 5 = 7 ✓.

**Exemplo 1 (valor de k).** Para que P(x) = x³ + kx² − 5x + 6 seja divisível por (x − 2): P(2) = 8 + 4k − 10 + 6 = 4 + 4k = 0 → **k = −1**. Então P(x) = x³ − x² − 5x + 6 e, por Briot-Ruffini com a = 2: coeficientes 1, 1, −3 e resto 0, ou seja, P(x) = (x − 2)(x² + x − 3).

**Exemplo 2 (resto sem dividir).** O resto da divisão de x³ − 2x² + x − 5 por (x + 1) é P(−1) = −1 − 2 − 1 − 5 = **−9**. O resto de x⁵⁰ − 3x + 2 por (x + 1) é 1 + 3 + 2 = **6**.

**Exemplo 3 (divisor de grau 2).** Um polinômio P deixa resto 3 na divisão por (x − 1) e resto −3 na divisão por (x + 2). O resto da divisão por (x − 1)(x + 2), de grau 2, tem grau no máximo 1: R(x) = ax + b. Como P(1) = 3 e P(−2) = −3: a + b = 3 e −2a + b = −3 → 3a = 6, a = 2, b = 1. **R(x) = 2x + 1.**

### 5.3 Raízes, fatoração e o teorema fundamental

**Teorema fundamental da álgebra:** todo polinômio de grau n ≥ 1 tem **exatamente n raízes complexas**, contando as multiplicidades. Consequências:

- Um polinômio de grau 3 tem 3 raízes (algumas podem ser repetidas ou complexas). Grau **ímpar** com coeficientes reais tem **ao menos 1 raiz real**.
- **Forma fatorada:** P(x) = aₙ(x − r₁)(x − r₂)...(x − rₙ).
- **Raízes complexas** de polinômio com coeficientes **reais** vêm em **pares conjugados**: se 1 + i é raiz, 1 − i também é.
- **Multiplicidade:** a raiz r tem multiplicidade m se (x − r)^m divide P e (x − r)^(m+1) não.

**Exemplo (multiplicidade e gráfico).** P(x) = (x − 1)²(x + 2) = x³ − 3x + 2 tem raiz **1 (dupla)** e raiz **−2 (simples)**. No gráfico, numa raiz de multiplicidade **par** a curva **toca o eixo x e volta** (não troca de sinal); numa de multiplicidade **ímpar** ela **atravessa** o eixo.

**Teorema das raízes racionais:** se P tem coeficientes **inteiros** e p/q (fração irredutível) é raiz racional, então **p divide o termo independente** e **q divide o coeficiente líder**. Com coeficiente líder 1, as raízes racionais são **inteiras** e divisores do termo independente.

**Exemplo (resolver uma cúbica).** 2x³ − 3x² − 11x + 6 = 0. Candidatos p/q: ±1, ±2, ±3, ±6 e ±1/2, ±3/2. Testando: P(3) = 54 − 27 − 33 + 6 = 0 ✓. Briot-Ruffini com a = 3:

<pre>
 3 |  2    −3    −11     6
   |  2     3     −2     0
</pre>

Quociente 2x² + 3x − 2 = (2x − 1)(x + 2). Raízes: **3, 1/2 e −2**. Forma fatorada: 2(x − 3)(x − 1/2)(x + 2).

### 5.4 Relações de Girard (grau 3 e 4)

O curso principal traz Girard para o 2º grau. A ideia se generaliza: as relações ligam as **raízes** aos **coeficientes** (com aₙ ≠ 0).

**Grau 3** (ax³ + bx² + cx + d, raízes r₁, r₂, r₃):

| Relação | Valor |
|---|---|
| r₁ + r₂ + r₃ | **−b/a** |
| r₁r₂ + r₁r₃ + r₂r₃ | **c/a** |
| r₁r₂r₃ | **−d/a** |

**Grau 4** (ax⁴ + bx³ + cx² + dx + e): soma = −b/a; soma dos produtos dois a dois = c/a; soma dos produtos três a três = −d/a; produto = e/a. (**Os sinais alternam**: −, +, −, +, ...)

**Exemplo 1.** P(x) = x³ − 6x² + 11x − 6 tem raízes 1, 2 e 3: soma 6 = −(−6)/1 ✓; soma dos pares 2 + 3 + 6 = 11 ✓; produto 6 = −(−6)/1 ✓. Aplicação clássica: **soma dos quadrados das raízes** = (soma)² − 2·(soma dos pares) = 36 − 22 = **14** (1 + 4 + 9 = 14 ✓).

**Exemplo 2 (PA).** As raízes de x³ − 12x² + 44x − 48 = 0 estão em progressão aritmética. Escreva-as como r − d, r, r + d: soma = 3r = 12 → r = 4. Verifique: P(4) = 64 − 192 + 176 − 48 = 0 ✓. Briot-Ruffini com 4 dá quociente x² − 8x + 12, de raízes 2 e 6: as três raízes são **2, 4 e 6** ✓ (PA de razão 2).

**Exemplo 3 (soma dos inversos).** As raízes de x³ − 7x² + 14x − 8 são 1, 2 e 4. A soma dos inversos das raízes é (soma dos pares)/(produto) = 14/8 = **7/4** (conferência: 1 + 1/2 + 1/4 = 7/4).

**Exemplo 4 (grau 4).** (x − 1)(x − 2)(x − 3)(x − 4) = x⁴ − 10x³ + 35x² − 50x + 24: soma 10 = −(−10); pares: 2 + 3 + 4 + 6 + 8 + 12 = 35; triplos: 6 + 8 + 12 + 24 = 50; produto 24.

**Exemplo 5 (raízes complexas).** x³ − 3x² + 4x − 2 = (x − 1)(x² − 2x + 2), de raízes **1, 1 + i e 1 − i**. Soma: 3 = −(−3)/1 ✓; produto: 1 · (1 + i)(1 − i) = 2 = −(−2)/1 ✓.

### 5.5 Gráfico de uma função polinomial

- Domínio: todos os reais. O gráfico é uma curva **contínua e sem "bicos"**.
- **Interceptos:** com o eixo y em (0, a₀); com o eixo x nas raízes **reais**.
- **Comportamento nas extremidades** (dominado pelo termo de maior grau aₙxⁿ):

| Grau | aₙ > 0 | aₙ < 0 |
|---|---|---|
| **Ímpar** (3, 5, ...) | começa embaixo (x → −∞, y → −∞) e termina em cima | começa em cima e termina embaixo |
| **Par** (4, 6, ...) | começa em cima e termina em cima ("U") | começa embaixo e termina embaixo ("∩") |

- O número de raízes **reais** é no máximo o grau. O número de "curvas" (máximos e mínimos locais) é no máximo grau − 1.
- **Sinal:** entre duas raízes reais consecutivas (de multiplicidade ímpar), o sinal se mantém; ele **troca** ao passar por raiz de multiplicidade ímpar e **não troca** por raiz de multiplicidade par.

**Exemplo.** P(x) = x³ − 6x² + 11x − 6 = (x − 1)(x − 2)(x − 3), aₙ = 1 > 0, grau 3: P < 0 para x < 1; P > 0 em (1, 2); P < 0 em (2, 3); P > 0 para x > 3. Corta o eixo y em (0, −6). (Conferência: P(0) = −6; P(1,5) = 0,375 > 0.)

## 6. Funções racionais (item 4.5)

### 6.1 Definição e domínio

**Função racional** é a razão de dois polinômios: **f(x) = P(x)/Q(x)**, com Q não nulo. O **domínio** exclui os valores em que **Q(x) = 0**.

**Exemplo.** f(x) = (x + 1)/(x² − 5x + 6): Q = (x − 2)(x − 3) = 0 em x = 2 e x = 3. **Domínio: todos os reais, exceto 2 e 3.**

**Zeros** da função: raízes de P(x) que **não anulam** Q. **Interceptos:** com o eixo y em f(0) (se 0 está no domínio).

### 6.2 Assíntotas

- **Assíntota vertical:** reta x = a, onde a é zero de Q que **não** é cancelado por zero de P. Perto de a, a função "explode" para +∞ ou −∞.
- **Assíntota horizontal** (comportamento quando x → ±∞), comparando os graus de P e Q:

| Graus | Assíntota horizontal |
|---|---|
| gr P **<** gr Q | **y = 0** (o eixo x) |
| gr P **=** gr Q | **y = (coef. líder de P) / (coef. líder de Q)** |
| gr P **>** gr Q | não há horizontal. Se gr P = gr Q + 1, há assíntota **oblíqua** (a reta é o **quociente** da divisão de P por Q) |

- **"Buraco" (descontinuidade removível):** se P e Q têm um fator comum (x − a), cancelado, o gráfico é o da função simplificada com um **furo** em x = a.

**Exemplos.**

1. f(x) = (3x² + 1)/(x² − 4): graus iguais → assíntota horizontal **y = 3/1 = 3**. Q = 0 em x = ±2 (P não se anula neles) → assíntotas verticais **x = 2 e x = −2**.
2. f(x) = x/(x² − 1): gr P < gr Q → **y = 0**; verticais **x = 1 e x = −1**; zero em x = 0.
3. f(x) = (x² + 1)/x = x + 1/x: vertical **x = 0**; gr P = gr Q + 1 → assíntota **oblíqua y = x**.
4. f(x) = (x² + x − 2)/(x − 3): dividindo, x² + x − 2 = (x − 3)(x + 4) + 10 → f(x) = x + 4 + 10/(x − 3): vertical **x = 3**, oblíqua **y = x + 4**.
5. f(x) = (x² − 1)/(x − 1) = (x − 1)(x + 1)/(x − 1) = x + 1, com x ≠ 1: é uma **reta com um furo** no ponto (1, 2). Não há assíntota vertical em x = 1 (o fator foi cancelado). **Pegadinha clássica:** o domínio ainda exclui x = 1.

### 6.3 A função recíproca f(x) = 1/x e a função homográfica

**f(x) = 1/x:** domínio e imagem iguais a "todos os reais, exceto 0". O gráfico é uma **hipérbole equilátera** com dois ramos (1º e 3º quadrantes), simétrica em relação à **origem** (função **ímpar**), assíntotas **x = 0** e **y = 0**, **decrescente em cada ramo**.

**Função homográfica:** f(x) = (ax + b)/(cx + d), com c ≠ 0 e ad − bc ≠ 0 (se ad − bc = 0, a função é constante, com furo). Assíntotas: **vertical x = −d/c** e **horizontal y = a/c**. Domínio: todos os reais, exceto −d/c; imagem: todos os reais, exceto a/c. O gráfico é a hipérbole de 1/x **deslocada** (centro em (−d/c, a/c)).

**Forma canônica:** f(x) = k/(x − p) + q tem assíntotas x = p e y = q.

**Exemplo completo.** f(x) = (2x + 3)/(x − 1).

- Dividindo: 2x + 3 = 2(x − 1) + 5 → **f(x) = 2 + 5/(x − 1)** (k = 5, p = 1, q = 2).
- Assíntotas: **x = 1** e **y = 2** (também pela fórmula: −d/c = 1; a/c = 2). Domínio: R − {1}; imagem: R − {2}.
- Zero: 2x + 3 = 0 → **x = −3/2**. Intercepto com y: f(0) = −3.
- Sinal: f(x) ≥ 0 ⇔ x ≤ −3/2 ou x > 1 (estudo do sinal de quociente, como na Aula 08).
- **Inversa:** y = (2x + 3)/(x − 1) → xy − y = 2x + 3 → x(y − 2) = y + 3 → f⁻¹(x) = (x + 3)/(x − 2). Conferência: f⁻¹(5) = 8/3 e f(8/3) = (16/3 + 3)/(5/3) = 5 ✓. A inversa de uma homográfica é uma homográfica.

**Outro exemplo (transformação do gráfico).** g(x) = 1/(x − 2) + 3 é o gráfico de 1/x deslocado 2 unidades para a **direita** e 3 para **cima**: assíntotas x = 2 e y = 3; zero em 1/(x − 2) = −3 → x = 5/3; g(0) = −1/2 + 3 = 5/2.

> **Resumo de assíntotas:** vertical = zero do denominador que sobrou; horizontal = comparar graus; oblíqua = quociente da divisão (só quando gr P = gr Q + 1).

## 7. Equações e inequações exponenciais (itens 4.6 e 4.8)

O curso principal ensina a função exponencial (Aula 12). Faltou a **técnica de resolver equações** com a incógnita no expoente. A base de tudo: **a função exponencial é injetiva**, então

**aˣ = aʸ ⇔ x = y** (para a > 0 e a ≠ 1).

### 7.1 Equações

**Método 1: mesma base.** Reduza os dois lados a uma potência da mesma base e iguale os expoentes.

- 2^(x+1) = 32 → 2^(x+1) = 2⁵ → x + 1 = 5 → **x = 4**.
- 25ˣ = 125 → 5^(2x) = 5³ → 2x = 3 → **x = 3/2**.
- 5^(x−1) = 1/25 = 5⁻² → x − 1 = −2 → **x = −1**.
- (2/3)ˣ = 9/4 → (2/3)ˣ = (2/3)⁻² → **x = −2**.

**Método 2: fator comum.** 2ˣ + 2^(x+1) = 48 → 2ˣ(1 + 2) = 48 → 2ˣ = 16 → **x = 4**.

**Método 3: mudança de variável** (equações que viram do 2º grau). Faça y = aˣ (com **y > 0**).

- 4ˣ − 5 · 2ˣ + 4 = 0: com y = 2ˣ, y² − 5y + 4 = 0 → y = 1 ou y = 4 → 2ˣ = 1 (x = 0) ou 2ˣ = 4 (x = 2). **S = {0, 2}.**
- 9ˣ − 4 · 3ˣ + 3 = 0: y = 3ˣ, y² − 4y + 3 = 0 → y = 1 ou y = 3 → **x = 0 ou x = 1**. Conferência: x = 0: 1 − 4 + 3 = 0 ✓; x = 1: 9 − 12 + 3 = 0 ✓.

> **Pegadinha:** como aˣ é **sempre positivo**, descarte raízes y ≤ 0. Em 4ˣ − 5 · 2ˣ − 6 = 0: y² − 5y − 6 = 0 → y = −1 (descartado, pois 2ˣ > 0) ou y = 6 → x = log₂ 6. Só **uma** solução real.

### 7.2 Inequações

Aqui vale a monotonia: se **a > 1**, a função é crescente e o sentido da desigualdade **se mantém** ao comparar expoentes; se **0 < a < 1**, ela é decrescente e o sentido **inverte**.

- 3^(2x−1) ≥ 27 = 3³ (base 3 > 1: mantém) → 2x − 1 ≥ 3 → **x ≥ 2**.
- (1/2)ˣ > 1/8 = (1/2)³ (base entre 0 e 1: **inverte**) → **x < 3**.
- 2^(x²) < 16 → x² < 4 → **−2 < x < 2**.

## 8. Exercícios autorais (gabarito e resolução)

**1.** Quantos eixos de simetria tem um hexágono regular? (A) 3 (B) 4 (C) 5 (D) 6 (E) 12.
**Resolução:** polígono regular de n lados tem n eixos. **Gabarito D.**

**2.** Quantos planos de simetria tem um cubo? (A) 3 (B) 6 (C) 9 (D) 12 (E) 13.
**Resolução:** 3 paralelos às faces e 6 diagonais. **Gabarito C.**

**3.** Qual figura tem centro de simetria e nenhum eixo de simetria? (A) trapézio isósceles (B) paralelogramo que não é retângulo nem losango (C) triângulo isósceles (D) pentágono regular (E) triângulo equilátero.
**Resolução:** só o paralelogramo comum. **Gabarito B.**

**4.** No cubo ABCDEFGH (ABCD é a base; E, F, G, H estão acima de A, B, C, D), as arestas AB e CG são: (A) paralelas (B) concorrentes (C) coincidentes (D) reversas e ortogonais (E) reversas e não ortogonais.
**Resolução:** não têm ponto comum e não são coplanares: reversas; AB é horizontal e CG vertical, formam 90°. **Gabarito D.**

**5.** Duas cordas, de 252 m e 198 m, são cortadas em pedaços de mesmo comprimento, o maior possível, sem sobras. O número total de pedaços é: (A) 11 (B) 14 (C) 18 (D) 25 (E) 30.
**Resolução:** MDC = 18; 14 + 11 = 25. **Gabarito D.**

**6.** Para que o número 4A12 (A é algarismo) seja divisível por 3, a soma dos possíveis valores de A é: (A) 5 (B) 10 (C) 12 (D) 15 (E) 18.
**Resolução:** 7 + A múltiplo de 3 → A = 2, 5, 8; soma 15. **Gabarito D.**

**7.** O número de divisores positivos de 360 é: (A) 12 (B) 18 (C) 20 (D) 24 (E) 30.
**Resolução:** 360 = 2³·3²·5 → 4·3·2 = 24. **Gabarito D.**

**8.** O resto da divisão de P(x) = x³ − 2x² + x − 5 por x + 1 é: (A) −9 (B) −5 (C) −1 (D) 5 (E) 9.
**Resolução:** P(−1) = −1 − 2 − 1 − 5 = −9. **Gabarito A.**

**9.** Se a, b e c são as raízes de x³ − 7x² + 14x − 8 = 0, o valor de 1/a + 1/b + 1/c é: (A) 1/2 (B) 7/4 (C) 7/8 (D) 2 (E) 14.
**Resolução:** (ab + ac + bc)/(abc) = 14/8 = 7/4. **Gabarito B.**

**10.** A assíntota horizontal do gráfico de f(x) = (2x + 3)/(x − 1) é: (A) y = 1 (B) y = 2 (C) y = 3 (D) x = 1 (E) y = −3/2.
**Resolução:** graus iguais: razão dos coeficientes líderes, 2/1 = 2. (x = 1 é a vertical.) **Gabarito B.**

**11.** A solução da equação 2ˣ + 2^(x+1) = 48 é: (A) 2 (B) 3 (C) 4 (D) 5 (E) 16.
**Resolução:** 2ˣ·3 = 48 → 2ˣ = 16 → x = 4. **Gabarito C.**

**12.** Dividindo-se R$ 3.600 em partes inversamente proporcionais a 2, 3 e 6, a maior parte, em reais, é: (A) 600 (B) 1.200 (C) 1.600 (D) 1.800 (E) 2.400.
**Resolução:** pesos 3, 2, 1 (k = 600); a maior parte é 3 · 600 = 1.800. **Gabarito D.**

## Fontes

Conteúdo didático padrão de matemática do ensino fundamental e médio, redigido de forma original. Contagens de simetria (cubo, tetraedro), pares de arestas reversas, divisores e demais exemplos numéricos conferidos por programa em 08/10/2026. Edital: Anexo II do cargo de 2º Tenente do CBMPE (Matemática, itens 1.3, 1.8, 2.5, 2.6, 4.4, 4.5, 4.6 e 4.8). Estilo da banca: levantamento interno de questões de Matemática da AOCP.
