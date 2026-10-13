---
id: S0511
agente: CLAUDE-L4
materia: Estatística
aula: Aula 09 — Variáveis Aleatórias Contínuas
trecho: estatistica/a09/s04
paginas_lidas: 42-48
---
# ANALÍTICO

As desigualdades de Chebyshev e de Cantelli (desigualdade unilateral) permitem limitar probabilidades conhecendo apenas a média e a variância da variável, sem saber qual é a distribuição. O trecho mostra as duas fórmulas, a versão em desvios padrão e como resolver questões diretas e inversas.

### Desigualdade de Chebyshev

Seja X uma variável aleatória (discreta ou contínua, de qualquer distribuição) com esperança μ e variância σ². Para qualquer δ > 0:

**P(|X − μ| ≥ δ) ≤ σ² / δ²**

Em palavras: a probabilidade de X se afastar da média, para cima ou para baixo, em δ ou mais é **no máximo** a variância dividida pelo quadrado de δ. O evento |X − μ| ≥ δ é a união de duas caudas: X ≤ μ − δ **ou** X ≥ μ + δ.

O nome do matemático russo tem várias grafias (Tchebychev, Tschebyscheff, Tchebyshev...) e as bancas usam todas. A desigualdade só dá **limite**, nunca o valor exato.

> 💡 **Exemplo:** uma linha de produção rende em média 500 peças por dia, com variância de 400 (peças²). A chance de produzir menos de 450 ou mais de 550 (δ = 50) é no máximo 400 / 2.500 = 0,16. Pelo complemento, produzir entre 450 e 550 tem chance **no mínimo** 1 − 0,16 = 0,84.

### Forma com desvios padrão

Fazendo δ = z · σ (z desvios padrão), o σ² cancela:

- **P(|X − μ| ≥ zσ) ≤ 1 / z²**: fora de z desvios, no máximo 1/z²;
- **P(|X − μ| < zσ) ≥ 1 − 1/z²**: dentro de z desvios, **pelo menos** 1 − 1/z².

| z (desvios padrão) | Pelo menos dentro do intervalo μ ± zσ |
| --- | --- |
| 2 | 1 − 1/4 = 75% |
| 3 | 1 − 1/9, cerca de 88,9% |
| 4 | 1 − 1/16 = 93,75% (cerca de 94%) |
| 5 | 1 − 1/25 = 96% |

> ⚠️ **Pegadinha:** o resultado é um **mínimo** para a parte dentro do intervalo e um **máximo** para a parte fora. Trocar "pelo menos" por "no máximo" torna o item errado. Além disso, o teorema não fala em coeficiente de variação, nem a variância é "limitada em z desvios"; a variância é o quadrado do desvio padrão. Para z ≤ 1 o limite 1/z² é maior ou igual a 1 e não informa nada.

### Como resolver questões diretas

1. Identifique μ e σ² (se vierem E(X) e E(X²), use σ² = E(X²) − [E(X)]²).
2. Descubra a distância δ entre a média e o limite do intervalo, ou o z.
3. Aplique σ²/δ² (ou 1/z²) para o evento "fora"; use o complemento para "dentro".

### Problemas inversos

Quando o enunciado fornece o limite da probabilidade e pede σ², iguale a desigualdade e isole a variância.

> 💡 **Exemplo:** X tem média 60 e, pelo teorema de Chebyshev, a probabilidade de X sair do intervalo (54, 66) é no máximo 4%. Aqui δ = 6, então σ² / 36 = 0,04 e σ² = 1,44, ou seja, σ = 1,2.

> 💡 **Exemplo:** média de R$ 3.000 e a prova diz que a proporção entre R$ 2.500 e R$ 3.500 é no mínimo 75%. Fora é, no máximo, 25%, com δ = 500: σ² / 250.000 = 0,25 e σ² = 62.500.

Cuidado ao converter "entre" e "fora": a probabilidade de estar dentro (no mínimo p) vira "fora, no máximo 1 − p".

### Desigualdade unilateral (Cantelli)

Quando interessa apenas o afastamento para **um lado** (por exemplo, superar a média), vale a versão unilateral, chamada de desigualdade de Cantelli ou unilateral de Chebyshev:

**P(X − μ ≥ δ) ≤ σ² / (σ² + δ²)**

Isto é, a probabilidade de X superar a média em δ ou mais é no máximo σ² / (σ² + δ²). Para a cauda inferior vale o mesmo, trocando o lado: P(μ − X ≥ δ) ≤ σ² / (σ² + δ²).

> 💡 **Exemplo:** com a mesma linha de produção (μ = 500, σ² = 400), a chance de passar de 550 (δ = 50) é no máximo 400 / (400 + 2.500), cerca de 0,138. Logo, produzir menos que 550 tem chance mínima de cerca de 0,862.

Aplicação inversa: média 0, P(X ≥ 10) ≤ 0,2 como limite exato. Então σ² / (σ² + 100) = 0,2, ou 0,8 · σ² = 20, e σ² = 25. Com E(X) = 2 e E(X²) = 13, a variância é 13 − 4 = 9; para P(X ≥ 8), δ = 6 e o limite é 9 / (9 + 36) = 0,2.

Em variável contínua, P(X > a) = P(X ≥ a), pois a probabilidade de um ponto isolado é nula; por isso é possível usar a fórmula com "maior que".

### Para fixar
- Chebyshev vale para qualquer distribuição: P(|X − μ| ≥ δ) ≤ σ² / δ², um limite máximo para o afastamento bilateral.
- Com δ = zσ: fora de z desvios, no máximo 1/z²; dentro, pelo menos 1 − 1/z² (z = 2 dá 75%; z = 3, cerca de 89%; z = 4, 93,75%).
- A desigualdade dá cotas (máximo/mínimo), nunca probabilidades exatas, e não informa nada para z ≤ 1.
- Em problemas inversos, iguale e isole σ²; converta "dentro, no mínimo p" em "fora, no máximo 1 − p".
- Cantelli (unilateral): P(X − μ ≥ δ) ≤ σ² / (σ² + δ²).
- Se vierem E(X) e E(X²), calcule a variância por E(X²) − [E(X)]².
- Em variável contínua, > e ≥ têm a mesma probabilidade.

# SINTÉTICO

- **Chebyshev**: para qualquer variável com média μ e variância σ², P(|X − μ| ≥ δ) ≤ σ² / δ², valendo para qualquer distribuição.
- **Natureza do resultado**: é um limite máximo para a probabilidade fora do intervalo e, pelo complemento, um limite mínimo para a probabilidade dentro.
- **Forma com z desvios padrão**: P(|X − μ| < zσ) ≥ 1 − 1/z²; para z = 2 dá pelo menos 75%, para z = 4 dá 93,75%.
- **Cuidado com z ≤ 1**: o limite 1/z² chega a 1 ou mais e não informa nada.
- **Cotas, não valores**: o teorema não fixa o coeficiente de variação nem o valor exato da probabilidade; não troque "pelo menos" por "no máximo".
- **Problemas inversos**: iguale σ² / δ² ao limite dado e isole σ² (média 60, fora de 54 a 66 em no máximo 4% leva a σ² = 1,44).
- **Conversão dentro × fora**: "entre os limites com probabilidade mínima p" equivale a "fora com probabilidade máxima 1 − p".
- **Cantelli (unilateral)**: P(X − μ ≥ δ) ≤ σ² / (σ² + δ²), útil quando só um lado interessa.
- **Variância via E(X²)**: se o enunciado fornece E(X) e E(X²), use σ² = E(X²) − [E(X)]² antes de aplicar as fórmulas; em variável contínua > e ≥ coincidem.

# NOTAS

- Pág. 43: o texto fala em "mais de 110 unidades" onde o correto, pelo exemplo, é 1100 unidades (erro de digitação do material).
- Págs. 45 e 46: nas questões da FCC, a leitura "mais que R$ 1.600 e menos que R$ 2.400" aparece invertida em um trecho do comentário ("mais que 1.600 ou menos que 2.400"), mas a resolução usa corretamente o complementar; resultado 25.600 confere.
- Acrescentado fora do trecho: a tabela com z = 2, 3, 5 (derivada direta da fórmula do trecho), a forma da cauda inferior de Cantelli (por simetria) e a conversão dentro/fora; exemplos numéricos próprios.
- Nenhuma página vazia ou ilegível.
