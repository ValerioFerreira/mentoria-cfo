---
id: S0513
agente: CLAUDE-L4
materia: Estatística
aula: Aula 10 — Distribuições Aleatórias Contínuas
trecho: estatistica/a10/s04
paginas_lidas: 32-41
---
# ANALÍTICO

A distribuição normal (ou gaussiana) é o modelo contínuo mais cobrado em Estatística. Este trecho descreve o formato e as propriedades da curva, ensina a usar a tabela da normal padrão Z e mostra como converter áreas em probabilidades.

### Características da distribuição normal

A variável normal tem densidade em forma de **sino**, definida para qualquer valor real (de −∞ a +∞). A fórmula da densidade é complicada, mas não é preciso integrá-la nem derivá-la: o que importa são os dois **parâmetros independentes**, a média **μ** e a variância **σ²**. Notação: X ~ N(μ, σ²).

- **Simetria**: a curva é simétrica em torno de μ, logo **média = mediana = moda**. O topo do sino está exatamente em μ.
- **Posição**: mudar μ só desloca o sino para a direita (μ maior) ou para a esquerda (μ menor), sem alterar o formato.
- **Dispersão**: σ² controla a forma. **Variância grande** = curva mais achatada, pico baixo e caudas pesadas; **variância pequena** = pico alto e caudas finas, com os valores mais concentrados perto da média.
- **Área total** sob a curva = 1 (100%), como em qualquer densidade. A probabilidade de um intervalo é a área sob a curva nesse intervalo. Em variável contínua, a probabilidade de um ponto isolado é zero.
- **Duplamente assintótica**: a curva se aproxima do eixo horizontal nas duas pontas (x → −∞ e x → +∞), sem nunca tocá-lo.
- **Dois pontos de inflexão**: onde a concavidade muda (de "para cima" para "para baixo" e de novo para cima). Ficam a um desvio padrão da média: em **μ − σ** e **μ + σ**.

### Consequências da simetria

Como μ divide a área em duas metades iguais:

- P(X > μ) = P(X < μ) = 50%.
- Para qualquer k real: **P(X > μ + k) = P(X < μ − k)** (caudas equidistantes têm a mesma área).
- Também **P(μ < X < μ + k) = P(μ − k < X < μ)** (áreas entre a média e pontos equidistantes são iguais).

> 💡 **Exemplo:** se μ = 10, então P(X > 14) = P(X < 6) e P(10 < X < 13) = P(7 < X < 10), pois 14 e 6 estão a 4 unidades da média, e 13 e 7 a 3.

> ⚠️ **Pegadinha:** trocar o efeito da variância (dizer que aumentar σ² deixa a curva "pontuda") é erro clássico. Outra pegadinha é afirmar que a área sob a curva "é igual à média": a área é sempre 100%, qualquer que seja μ.

### A normal padrão Z

A **normal padrão** (ou reduzida) é a normal com **μ = 0 e σ² = 1**, denotada Z ~ N(0, 1). É para ela que existe a tabela de probabilidades. Para uma normal qualquer X ~ N(μ, σ²) usa-se a padronização **Z = (X − μ) / σ**, que transforma X em Z (conteúdo acrescentado, necessário para aplicar a tabela a qualquer problema).

> 💡 **Exemplo:** X ~ N(50, 16), logo σ = 4. Para P(50 < X < 58): z = (58 − 50)/4 = 2, então P(0 < Z < 2) = 0,4772.

### Como ler a tabela

A tabela mais comum fornece **P(0 < Z < z)**, a área entre a média (0) e o valor z.

- O valor de z é composto: a **linha** traz a parte inteira e o primeiro decimal; a **coluna** traz o segundo decimal.
- Exemplo: z = 1,96 fica na linha 1,9 e coluna 0,06, resultando **P(0 < Z < 1,96) = 0,475**.
- **Leitura inversa**: para achar o z que corresponde a uma área, procura-se a área nos campos da tabela e adota-se o valor mais próximo. Para P(0 < Z < z) = 0,40, o campo mais próximo é 0,3997 (linha 1,2, coluna 0,08), logo **z ≈ 1,28**.

Alguns valores úteis da tabela:

| z | P(0 < Z < z) |
| --- | --- |
| 1,00 | 0,3413 |
| 1,28 | 0,3997 |
| 1,96 | 0,4750 |
| 2,00 | 0,4772 |
| 3,00 | 0,4987 |

A tabela termina em z = 3,9, onde a área já é 0,5000 (arredondada).

### Operações com a simetria da normal padrão

Para qualquer z positivo:

| Probabilidade desejada | Como calcular |
| --- | --- |
| P(Z > z) | 0,5 − P(0 < Z < z) |
| P(−z < Z < 0) | P(0 < Z < z) (espelho) |
| P(Z < −z) | P(Z > z) = 0,5 − P(0 < Z < z) |
| P(−z < Z < z), isto é, módulo de Z menor que z | 2 × P(0 < Z < z) |
| módulo de Z maior que z (as duas caudas) | 1 − 2 × P(0 < Z < z), ou 2 × P(Z > z) |

> 💡 **Exemplo com z = 1,96** (P(0 < Z < 1,96) = 0,475): P(Z > 1,96) = 0,5 − 0,475 = 0,025; P(Z < −1,96) = 0,025; P(\|Z\| < 1,96) = 2 × 0,475 = 0,95; P(\|Z\| > 1,96) = 1 − 0,95 = 0,05, que é o mesmo que 2 × 0,025.

Em P(|Z| > z) são duas caudas: a probabilidade do módulo maior que z é a soma das duas caudas, P(Z < −z) + P(Z > z). Em P(|Z| < z) é a faixa central, de −z a +z.

### Outro tipo de tabela: normal acumulada

Algumas provas trazem tabelas da **função de distribuição acumulada**, com **P(Z ≤ z) = P(−∞ < Z ≤ z)**, a área desde a cauda esquerda até z. Ela inclui a metade esquerda inteira (0,5) quando z > 0. Nesse caso: P(0 < Z < z) = P(Z ≤ z) − 0,5.

> ⚠️ **Pegadinha (Cebraspe):** afirmar que a simetria implica P(Z ≥ 2) = 1 − P(Z ≤ −2) é falso. A simetria dá P(Z ≥ 2) = P(Z ≤ −2): as duas caudas são iguais e pequenas. Já 1 − P(Z ≤ −2) é quase tudo (bem acima de 50%), o complemento da cauda esquerda. Confira a ordem de grandeza antes de aceitar uma igualdade.

### Para fixar
- Normal: sino simétrico, média = mediana = moda = μ, definida em toda a reta, com duas assíntotas.
- μ desloca a curva; σ² a achata (grande) ou afunila (pequena). Área total sempre 100%.
- Pontos de inflexão em μ − σ e μ + σ.
- P(X > μ + k) = P(X < μ − k) e P(X > μ) = P(X < μ) = 50%.
- Normal padrão: Z ~ N(0, 1), com Z = (X − μ)/σ. A tabela dá P(0 < Z < z).
- P(Z > z) = 0,5 − tabela; P(\|Z\| < z) = 2 × tabela; P(\|Z\| > z) = 1 − 2 × tabela.
- Valor-chave: P(0 < Z < 1,96) = 0,475, logo as duas caudas somam 5%.

# SINTÉTICO

- **Forma da normal**: curva em sino, simétrica em torno de μ, definida de −∞ a +∞, com duas assíntotas no eixo horizontal; média = mediana = moda.
- **Parâmetros**: μ desloca a curva; σ² controla a abertura (variância maior = curva mais achatada e caudas pesadas; menor = pico alto e concentrado).
- **Pontos de inflexão**: ficam em μ − σ e μ + σ, onde a concavidade da curva muda.
- **Área e probabilidade**: a área total é 100% e a probabilidade de um intervalo é a área sob a curva nele; P(X > μ) = P(X < μ) = 50%.
- **Simetria em torno de μ**: P(X > μ + k) = P(X < μ − k) e P(μ < X < μ + k) = P(μ − k < X < μ).
- **Normal padrão**: Z ~ N(0, 1); padroniza-se com Z = (X − μ)/σ e a tabela dá P(0 < Z < z) (linha = inteiro e décimo; coluna = centésimo).
- **Leitura inversa**: busca-se a área nos campos da tabela e toma-se o z do valor mais próximo (0,40 leva a z ≈ 1,28).
- **Caudas**: P(Z > z) = 0,5 − P(0 < Z < z) = P(Z < −z).
- **Módulo**: P(|Z| < z) = 2 × P(0 < Z < z) e P(|Z| > z) = 1 − 2 × P(0 < Z < z) = 2 × P(Z > z).
- **Referência**: com z = 1,96, P(0 < Z < z) = 0,475, então P(|Z| < 1,96) = 0,95 e P(|Z| > 1,96) = 0,05.
- **Tabela acumulada**: dá P(Z ≤ z); para z > 0, P(0 < Z < z) = P(Z ≤ z) − 0,5.

# NOTAS

- Fórmula da densidade (com símbolos matemáticos) veio embaralhada na extração; não foi reproduzida (não é cobrada para cálculo).
- Figuras (gráficos de sino, áreas sombreadas) descartadas; o texto já descreve o conteúdo.
- Na pág. 40 do material há erro de digitação: uma linha escreve P(|Z| < z) = 2 × P(Z > z) quando o correto é P(|Z| > z) = 2 × P(Z > z). O resumo traz a forma correta.
- Acrescentado fora do trecho: a fórmula de padronização Z = (X − μ)/σ e a relação com a tabela acumulada P(0 < Z < z) = P(Z ≤ z) − 0,5 (regras estáveis e bem conhecidas).
- A afirmação do material de que P(0 < Z < 1,96) = 0,475 usa a tabela de 4 casas (0,4750); confere.
