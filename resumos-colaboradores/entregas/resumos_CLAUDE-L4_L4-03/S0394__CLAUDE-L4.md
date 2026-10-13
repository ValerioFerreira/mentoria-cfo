---
id: S0394
agente: CLAUDE-L4
materia: Estatística
aula: Aula 09 — Variáveis Aleatórias Contínuas
trecho: estatistica/a09/s01
paginas_lidas: 4-15
---
# ANALÍTICO

Este trecho apresenta as variáveis aleatórias contínuas e a ferramenta para calculá-las: a função densidade de probabilidade (f.d.p.), cuja área sob a curva fornece as probabilidades. Mostra também como obter essa área por geometria elementar ou por integral, e como achar constantes que tornam uma função uma f.d.p. válida.

### Variável discreta × contínua

- **Discreta:** os resultados possíveis são contáveis (enumeráveis), como as faces de um dado ou os lados de uma moeda.
- **Contínua:** pode assumir qualquer valor dentro de um intervalo (ou de um conjunto de intervalos); seus valores são **medidos**, não contados. Exemplos: peso, comprimento, área, volume, distância, tempo, altura.

Como sempre se pode acrescentar mais uma casa decimal à medida, o número de valores possíveis é infinito. Por isso, a probabilidade de a variável assumir **exatamente** um valor específico é **zero**. Em vez disso, calculam-se probabilidades de **intervalos** (por exemplo, a altura estar entre 1,80 m e 1,90 m).

### Função densidade de probabilidade (f.d.p.)

Nas discretas há uma função de probabilidade, f(x) = P(X = x). Nas contínuas, usa-se a **função densidade de probabilidade**, f(x), que descreve como a probabilidade se distribui ao longo dos valores. Toda f.d.p. satisfaz duas condições:

1. **f(x) ≥ 0** para todo x (probabilidade nunca é negativa). Onde f(x) = 0, o intervalo tem probabilidade zero.
2. A probabilidade de todo o espaço amostral é 1, isto é, **a área total sob a curva é igual a 1**.

> ⚠️ **Pegadinha:** f(x) não é uma probabilidade; é uma densidade. Seu valor pode passar de 1 em algum ponto (basta o intervalo ser curto). O que vale 1 é a **área total**.

**A probabilidade de um intervalo é a área sob a curva nesse intervalo.** Como o ponto isolado tem probabilidade zero, os sinais de desigualdade não mudam o resultado:

P(a < X < b) = P(a ≤ X ≤ b) = P(a ≤ X < b) = P(a < X ≤ b)

O mesmo vale para > e ≥. Isso é diferente do que ocorre nas variáveis discretas.

### Calculando a área: geometria

Quando o gráfico da f.d.p. é formado por figuras simples, use as áreas conhecidas:

- retângulo: base × altura;
- triângulo: base × altura / 2;
- trapézio: (base maior + base menor) × altura / 2.

> 💡 **Exemplo:** f(x) = α · (3 − x) para x entre 0 e 3 (e zero fora). O gráfico é um triângulo de base 3 e altura f(0) = 3α. Área = 3 · 3α / 2 = 4,5α = 1, logo α = 2/9. Para P(X > 2): triângulo de base 1 (de 2 a 3) e altura f(2) = 2/9, com área 1 · (2/9) / 2 = 1/9 ≈ 11,1%.

### Calculando a área: integral

Se a figura não é simples, usa-se a integral, que soma a área de retângulos infinitamente estreitos sob a curva. Regras básicas:

| Situação | Integral |
| --- | --- |
| Potência de x (n ≠ −1) | ∫xⁿ dx = x^(n+1) / (n+1) |
| Caso n = −1 | ∫(1/x) dx = ln x |
| Constante multiplicando | ∫a·xⁿ dx = a · x^(n+1)/(n+1) |
| Só uma constante | ∫a dx = a·x |
| Exponencial | ∫eˣ dx = eˣ; também ∫e^(x+c) dx = e^(x+c) |
| Soma ou subtração | integra-se cada parcela separadamente |

O resultado da integral (sem limites) é chamado de F(x). Para a probabilidade em um intervalo (a, b):

**P(a < X < b) = ∫ f(x) dx de a até b = F(b) − F(a)**

Ou seja, aplica-se F no limite superior, aplica-se no inferior e **subtrai-se**.

> 💡 **Exemplo:** f(x) = 2x para x em [0, 1]. Aqui F(x) = x². Então P(0,5 < X < 1) = F(1) − F(0,5) = 1 − 0,25 = 0,75. (Confere pela geometria: o triângulo total tem área 1, e o pedaço de x = 0 a 0,5 tem área 0,5 · 1 / 2 = 0,25.)

> ⚠️ **Pegadinha:** o erro típico é calcular a diferença b − a e aplicar F nela. F(b − a) é diferente de F(b) − F(a). No exemplo, F(0,5) = 0,25, mas F(1) − F(0,5) = 0,75, que é o certo.

### Intervalo total e f.d.p. definida por partes

Se a variável vai de um mínimo xI a um máximo xS, a integral em todo esse intervalo vale 1: ∫ f(x) dx de xI até xS = 1. Quando a função vale em toda a reta real, os limites são −∞ e +∞.

Uma f.d.p. pode ter **uma expressão para cada faixa de valores**. Para um intervalo que cruza duas faixas, **separa-se a integral em duas** e somam-se os resultados.

> 💡 **Exemplo:** f(x) = 0,5x se 0 ≤ x < 1; f(x) = 0,5 se 1 ≤ x ≤ 2,5; e zero nos demais casos. Áreas: 0,25 (triângulo) + 0,75 (retângulo 1,5 × 0,5) = 1, logo é válida. P(0,5 < X < 1,5) = ∫0,5x de 0,5 a 1 + ∫0,5 de 1 a 1,5 = 0,25 · (1 − 0,25) + 0,5 · 0,5 = 0,1875 + 0,25 = 0,4375.

### Achando a constante da f.d.p.

Quando a função traz um parâmetro (α, C, k), impõe-se a condição de que a área total seja 1 e resolve-se a equação. Se a f.d.p. é uma reta, a geometria costuma bastar; se é uma potência, use a integral.

> 💡 **Exemplo:** f(x) = k · x² para x em [0, 3]. A integral de 0 a 3 é k · 27/3 = 9k = 1, então k = 1/9. P(X > 2) = F(3) − F(2), com F(x) = x³/27, que dá 1 − 8/27 = 19/27 ≈ 70,4%.

Passos práticos para questões: (1) identifique o intervalo de definição; (2) imponha área total = 1 para achar a constante; (3) escreva a probabilidade pedida como área (desenhe o gráfico se ele for reta); (4) calcule por geometria ou por F(b) − F(a).

### Para fixar

- Contínua: valores medidos, infinitos; P(X = x) = 0, e se trabalha com intervalos.
- f.d.p.: f(x) ≥ 0 e área total = 1; f(x) não é probabilidade e pode ser maior que 1.
- Probabilidade de intervalo = área sob a f.d.p.; < e ≤ dão o mesmo resultado.
- Geometria para retas (retângulo, triângulo, trapézio); integral para curvas.
- P(a < X < b) = F(b) − F(a); nunca F(b − a).
- Em f.d.p. por partes, separe a integral em cada faixa e some.
- Para achar a constante, use área total = 1.

# SINTÉTICO

- **Contínua × discreta**: a contínua é medida, não contada, e assume infinitos valores num intervalo; a discreta tem resultados enumeráveis.
- **Ponto isolado**: P(X = x) = 0 para variável contínua, então se calculam probabilidades de intervalos e tanto faz usar < ou ≤.
- **F.d.p.**: f(x) ≥ 0 e área total sob a curva igual a 1; f(x) é densidade, não probabilidade, e pode passar de 1.
- **Probabilidade**: é a área sob a f.d.p. no intervalo; use geometria (retângulo, triângulo, trapézio) quando o gráfico for simples.
- **Integral**: ∫xⁿ dx = x^(n+1)/(n+1) para n ≠ −1; ∫a dx = a·x; ∫eˣ dx = eˣ; e a integral de uma soma é a soma das integrais.
- **Intervalo**: P(a < X < b) = F(b) − F(a); o erro clássico é calcular F(b − a).
- **Constante e partes**: ache a constante impondo área total 1; se a f.d.p. tem expressões diferentes por faixa, separe a integral e some.

# NOTAS

- Nenhuma página vazia ou ilegível. Gráficos de f.d.p. foram descartados por serem ilustração do texto.
- Os exemplos numéricos do resumo são originais; os do material (f.d.p. 12x²(1−x), 3x², questões de concursos sobre erro de medição, ruído e constante normalizadora) não foram reproduzidos.
- Acrescentei por conta própria que f(x) pode ser maior que 1 (consequência de ser densidade); o material só afirma f(x) ≥ 0 e área total 1.
- O material chama o resultado da integral de "integrando" (F(x)); o termo correto é primitiva ou integral indefinida, e adotei "F(x)" sem rótulo.
