---
id: S0534
agente: CLAUDE-L4
materia: Estatística
aula: Aula 10 — Distribuições Aleatórias Contínuas
trecho: estatistica/a10/s01
paginas_lidas: 4-12
---
# ANALÍTICO

A distribuição uniforme contínua é a mais simples das distribuições teóricas de variáveis contínuas: todos os valores de um intervalo são "igualmente prováveis". O trecho mostra a função densidade, o cálculo de probabilidades por área, a função de distribuição acumulada, a esperança e a variância, além de como inverter os parâmetros a partir da média e da variância.

### Função densidade

Em uma variável **discreta uniforme**, todos os resultados têm a mesma probabilidade. Na **contínua uniforme**, a análoga é uma função densidade de probabilidade (f.d.p.) **constante** em todo o intervalo (a, b) e **nula fora dele**:

**f(x) = k, para a < x < b; f(x) = 0, nos demais casos.**

A área total sob a f.d.p. é 1 (100% do espaço amostral). A região é um retângulo com base (b − a) e altura k, então (b − a) · k = 1, o que dá:

**k = 1 / (b − a)**

Portanto os únicos **parâmetros** da distribuição uniforme são os limites **a** e **b**: sabendo o intervalo, sabe-se a altura.

> 💡 **Exemplo próprio:** variável uniforme no intervalo (2, 10): k = 1/(10 − 2) = 1/8 = 0,125.

> ⚠️ **Pegadinha:** a f.d.p. vale k, que **não é probabilidade** (pode até ser maior que 1 em intervalos curtos, como 0,5 de largura, onde k = 2). A probabilidade é a **área**.

### Probabilidade de um intervalo

A probabilidade de a variável cair em (m, n), com a < m < n < b, é a área do retângulo de base (n − m) e altura k:

**P(m < X < n) = (n − m) / (b − a)**

É a **razão entre o comprimento do intervalo de interesse e o comprimento total**.

> 💡 **Exemplo próprio:** na uniforme em (2, 10), P(4 < X < 7) = 3/8 = 0,375. Para um ônibus que passa a cada 20 minutos, com chegada do passageiro uniforme nesse intervalo, P(esperar mais de 15 minutos) = 5/20 = 0,25.

Como a variável é contínua, **a probabilidade de um ponto é zero**, e os sinais < e ≤ são equivalentes: P(m < X < n) = P(m ≤ X < n) = P(m < X ≤ n) = P(m ≤ X ≤ n).

**Passo a passo em prova:** (1) identifique a e b; (2) escreva o evento como intervalo; (3) corte o intervalo pedido nos limites a e b (quem ultrapassa o intervalo é truncado); (4) divida o comprimento do trecho pedido por (b − a). Para "maior que x", use o trecho de x até b; para "menor que x", use o trecho de a até x.

> 💡 **Exemplos de provas:** uma máquina com ciclo uniforme de 8 a 14 minutos tem P(ciclo > 12) = (14 − 12)/(14 − 8) = 2/6 = 1/3. Para X uniforme em [0, 50], P(X > 20) = 30/50 = 0,6. Para U uniforme em [0, 1], P(U > 1/10) = 0,9.

### Função de distribuição acumulada

A f.d.a. no ponto x é **F(x) = P(X ≤ x)**. Na uniforme, equivale à probabilidade de X estar entre o limite inferior a e x:

**F(x) = (x − a) / (b − a), para a < x < b.**

Vale 0 para x ≤ a e 1 para x ≥ b. Exemplo próprio: na uniforme em (2, 10), F(5) = 3/8 = 0,375.

### Esperança e variância

- **Esperança (média)**: é o ponto médio do intervalo, **E(X) = (a + b) / 2**.
- **Variância**: **Var(X) = (b − a)² / 12**. O desvio padrão é a raiz dessa variância.

> 💡 **Exemplo próprio:** em (2, 10), E = 6 e Var = 8²/12 = 64/12 = 16/3 ≈ 5,33.

> ⚠️ **Pegadinha:** a variância tem **(b − a) ao quadrado** dividido por **12**, e não (b + a)/12 nem (b − a)²/2. Alternativas erradas em provas costumam trocar o sinal (b − a por b + a) na esperança, o expoente ou o divisor.

Em casos em que se informam média e variância, **recuperam-se os extremos** resolvendo um sistema:

1. a média dá **a + b = 2·μ**;
2. a variância dá **(b − a)² = 12·Var**, logo **b − a = raiz de (12·Var)** (a raiz é positiva porque b > a).
3. Somando e subtraindo as duas equações, acham-se b e a.

> 💡 **Exemplo próprio:** média 7 e variância 3. Então a + b = 14 e (b − a)² = 36, b − a = 6. Somando: 2b = 20, b = 10; logo a = 4. A variável é uniforme em (4, 10).
> No problema do material, média 4 e variância 12 levam a a = −2 e b = 10, e P(X < 7) = 9/12 = 0,75 (o intervalo pode ter limite negativo).

### Reconhecer a uniforme pela f.d.p.

Se a f.d.p. do enunciado é uma constante da forma 1 / (limite superior − limite inferior), num intervalo, é uma uniforme contínua. Com f(x) = 1/(20 − 15) entre 15 e 20, os limites são 15 e 20, E(X) = 17,5 e Var(X) = 5²/12 = 25/12.

### Família exponencial

A maioria das distribuições conhecidas faz parte da **família exponencial**: discretas (binomial, geométrica, hipergeométrica, Poisson) e contínuas (exponencial, normal, beta, Weibull). A **uniforme (contínua e discreta) é uma distribuição importante que não pertence a essa família**.

### Para fixar
- Uniforme contínua: f.d.p. constante em (a, b), k = 1/(b − a); parâmetros a e b.
- P(m < X < n) = (n − m)/(b − a); ponto isolado tem probabilidade zero.
- F(x) = (x − a)/(b − a) em a < x < b.
- E(X) = (a + b)/2 e Var(X) = (b − a)²/12.
- Dadas média e variância: a + b = 2μ e b − a = raiz de 12·Var.
- A uniforme não pertence à família exponencial.
- Sempre confira se o intervalo pedido está dentro de (a, b) antes de dividir.

# SINTÉTICO

- **Forma da f.d.p.**: constante, igual a k = 1/(b − a), dentro de (a, b) e zero fora; a e b são os únicos parâmetros.
- **Por que k = 1/(b − a)**: a área do retângulo (b − a) · k tem de ser 1 (100% da probabilidade).
- **Probabilidade de intervalo**: P(m < X < n) = (n − m)/(b − a), a razão entre o comprimento do trecho e o intervalo total.
- **Variável contínua**: probabilidade de um ponto é zero, então < e ≤ dão o mesmo resultado.
- **Acumulada**: F(x) = P(X ≤ x) = (x − a)/(b − a) entre a e b (0 antes de a, 1 depois de b).
- **Esperança**: E(X) = (a + b)/2, o ponto médio do intervalo.
- **Variância**: Var(X) = (b − a)²/12, com divisor 12 e diferença elevada ao quadrado.
- **Achar a e b**: a + b = 2μ e b − a = raiz de 12·Var; resolve-se o sistema somando e subtraindo (os extremos podem ser negativos).
- **Truncar o intervalo**: ao calcular "maior que x" ou "menor que x", use apenas a parte que está dentro de (a, b).
- **Família exponencial**: binomial, Poisson, exponencial, normal, beta e Weibull pertencem; a uniforme não pertence.

# NOTAS

- Os gráficos de f.d.p. (retângulos sombreados) foram descartados; o texto descreve a ideia.
- Dados das questões (intervalos, gabaritos) conferidos: 1/3, 0,6, 0,9, E = 17,5 e Var = 25/12, e média 4 / variância 12 resultando em a = −2, b = 10 e probabilidade 0,75.
- Pág. 9: o quadro-resumo escreve f(x) = 1/(b − a) para a ≤ x ≤ b, com sinal de igual nos limites; para variável contínua é indiferente.
- Nota de rodapé do material (pág. 11): a raiz de (b − a)² é |b − a|, igual a b − a porque b > a; incorporada acima em forma simples.
- Exemplos "próprios" (intervalo (2,10), ônibus, média 7 e variância 3) são do autor do resumo; nada foi acrescentado de fora do trecho.
