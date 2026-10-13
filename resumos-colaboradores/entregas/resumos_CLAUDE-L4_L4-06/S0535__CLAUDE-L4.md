---
id: S0535
agente: CLAUDE-L4
materia: Estatística
aula: Aula 10 — Distribuições Aleatórias Contínuas
trecho: estatistica/a10/s05
paginas_lidas: 42-50
---
# ANALÍTICO

A tabela da normal padrão só existe para a distribuição com média 0 e variância 1. Este trecho ensina a levar qualquer normal N(μ, σ²) até ela (padronização), a fazer o caminho de volta, a calcular intervalos simétricos em torno da média e a usar a Regra Empírica (68-95-99,7), com questões resolvidas.

### A fórmula de padronização

Para uma variável X normal com média **μ** e desvio padrão **σ**, o valor padronizado é:

**z = (x − μ) / σ**

O resultado z mede **quantos desvios padrão** o valor x está acima (z > 0) ou abaixo (z < 0) da média. A propriedade-chave: a probabilidade de X ficar em um intervalo é **igual** à probabilidade de Z ficar no intervalo transformado. Em símbolos, P(X > x) = P(Z > z), P(X < x) = P(Z < z) e P(a < X < b) = P(za < Z < zb), com a mesma fórmula aplicada a **cada** extremo.

> 💡 **Exemplo próprio:** X normal com μ = 10 e σ = 4. Para x = 18, z = (18 − 10)/4 = 2. Logo P(X > 18) = P(Z > 2). Como P(0 < Z < 2) = 0,4772 e a metade direita da curva vale 0,5, P(Z > 2) = 0,5 − 0,4772 = 0,0228 (2,28%).

### Como ler a tabela da normal padrão

A tabela usual dá a área entre **0 e z**, P(0 < Z < z). Como a curva é simétrica em torno de 0 e a área total é 1, cada metade vale 0,5. Isso permite montar qualquer probabilidade:

| Probabilidade pedida | Como calcular com P(0 < Z < z) |
| --- | --- |
| P(Z > z), z > 0 | 0,5 − P(0 < Z < z) |
| P(Z < z), z > 0 | 0,5 + P(0 < Z < z) (ou 1 − P(Z > z)) |
| P(−z < Z < 0) | P(0 < Z < z), pela simetria |
| P(−z < Z < z) | 2 · P(0 < Z < z) |
| P(z1 < Z < z2), 0 < z1 < z2 | P(0 < Z < z2) − P(0 < Z < z1) |

Valores que aparecem muito: P(0 < Z < 1) = 0,3413; P(0 < Z < 2) = 0,4772; P(0 < Z < 3) = 0,4987.

> 💡 **Exemplo próprio:** com μ = 10 e σ = 4, P(6 < X < 18): z vale −1 e +2. P(−1 < Z < 2) = 0,3413 + 0,4772 = 0,8185. Quando os extremos ficam em lados opostos da média, **somam-se** as áreas; do mesmo lado, **subtraem-se**.

### O caminho inverso: dada a probabilidade, achar x

Procure primeiro o z na tabela e depois isole x na fórmula: **x = μ + z · σ**.

Passo a passo para P(X < x) = p:
1. Se p > 0,5, o z é positivo e a área entre 0 e z é p − 0,5; se p < 0,5, o z é negativo (use a simetria: busque o z positivo cuja área é 0,5 − p e troque o sinal).
2. Procure na tabela o valor mais próximo da área e leia z (a tabela costuma dar aproximações; use o valor mais próximo, ou o que o enunciado fornecer).
3. Calcule x = μ + z · σ.

> 💡 **Exemplo próprio:** normal com μ = 20 e σ = 5, achar x tal que P(X < x) = 0,9. A área entre 0 e z deve ser 0,9 − 0,5 = 0,4; pela tabela, z ≈ 1,28. Então x = 20 + 1,28 · 5 = 26,4.

Muitas vezes o enunciado já fornece o valor de z (por exemplo, "P(Z ≤ 1,64) = 0,95"). Nesse caso, não consulte tabela: identifique que o corte deixa 95% abaixo e 5% acima e aplique direto x = μ + z · σ.

### Intervalos simétricos e a Regra Empírica

Quando o intervalo tem a forma **μ − k < X < μ + k** (extremos à mesma distância da média), basta padronizar **um** dos extremos: o outro dá o mesmo z com sinal trocado. Para k = 1σ, 2σ e 3σ:

| Intervalo | z | Probabilidade exata (tabela) | Aproximação (Regra Empírica) |
| --- | --- | --- | --- |
| μ ± 1σ | ±1 | 2 × 0,3413 = 0,6826 | **68%** |
| μ ± 2σ | ±2 | 2 × 0,4772 = 0,9544 | **95%** |
| μ ± 3σ | ±3 | 2 × 0,4987 = 0,9974 | **99,7%** |

Ou seja, uma normal qualquer se afasta da média em mais de 3 desvios padrão em menos de 0,3% dos casos. Algumas provas exigem decorar esses três números (eles não vêm no enunciado), e alguns enunciados aproximam 68% por "2/3".

> ⚠️ **Pegadinha:** a Regra Empírica vale para **qualquer** normal, não só para a padrão, e só para intervalos **simétricos** em torno de μ de 1, 2 ou 3 desvios padrão. Para outros valores de k, padronize e use a tabela.

### Caudas: usando a simetria na Regra Empírica

Se P(μ − σ < X < μ + σ) ≈ 68%, os 32% restantes se dividem **igualmente** entre as duas caudas, porque a curva é simétrica: cada cauda tem ≈ 16%. Analogamente, ≈ 2,5% em cada cauda para 2σ e ≈ 0,15% para 3σ. Assim, P(X > μ + σ) ≈ 16%, P(X < μ + 2σ) ≈ 97,5% etc.

### Questões típicas resolvidas

- **Intervalo simétrico (tempo de julgamento, μ = 50, σ = 10):** P(40 < X < 60) tem z = ±1, logo ≈ 0,68 pela Regra Empírica.
- **Cauda via Regra Empírica (μ = 100, σ = 10):** P(X > 110) corresponde a z = 1. Fora de 90 a 110 ficam ≈ 32%, e metade disso está acima: ≈ 16%.
- **Intervalo entre a média e um valor, com dado do enunciado (μ = 3.600 g, σ = 300 g):** para x = 3.475, z = −125/300 ≈ −0,42. Com P(Z < −0,42) = 0,338 e P(Z < 0) = 0,5, a probabilidade entre eles é 0,5 − 0,338 = 0,162. Observe o uso da forma **acumulada** P(Z < z), em vez da tabela de 0 a z.
- **Valor de corte dos 5% melhores (μ = 2.500, σ = 1.500, dado P(Z ≤ 1,64) = 0,95):** o corte deixa 95% abaixo, logo z = 1,64 e x = 2.500 + 1,64 · 1.500 = 4.960.

> ⚠️ **Pegadinha:** confira **qual tabela** o enunciado usa. Algumas dão P(0 < Z < z); outras dão a acumulada P(Z < z). As contas mudam: com a acumulada, P(a < Z < b) = F(b) − F(a) e F(0) = 0,5.

### Para fixar
- Padronização: z = (x − μ)/σ; z diz quantos desvios padrão x está da média.
- As probabilidades de X e de Z coincidem quando os extremos são transformados pela mesma fórmula.
- Inverso: x = μ + z · σ; ache z na tabela (ou no enunciado) antes.
- Simetria: P(Z > z) = P(Z < −z); a área de cada metade da curva é 0,5.
- Regra Empírica: μ ± σ ≈ 68%, μ ± 2σ ≈ 95%, μ ± 3σ ≈ 99,7%.
- Em intervalo simétrico em torno de μ, padronize um extremo só; cada cauda leva metade do restante.
- Atenção à tabela usada: área de 0 a z ou acumulada.

# SINTÉTICO

- **Padronização**: z = (x − μ)/σ transforma qualquer normal em N(0,1); z é o número de desvios padrão entre x e a média.
- **Equivalência de probabilidades**: P(a < X < b) = P(za < Z < zb), com a fórmula aplicada em cada extremo.
- **Tabela de 0 a z**: cada metade da curva vale 0,5; P(Z > z) = 0,5 − P(0 < Z < z) para z positivo, e P(−z < Z < 0) = P(0 < Z < z) pela simetria.
- **Lados opostos × mesmo lado**: extremos em lados opostos da média somam as áreas; do mesmo lado, subtraem.
- **Caminho inverso**: ache o z da probabilidade desejada e use x = μ + z · σ; se o enunciado dá o z, aplique direto.
- **Regra Empírica**: μ ± σ ≈ 68%; μ ± 2σ ≈ 95%; μ ± 3σ ≈ 99,7% (valem para qualquer normal, em intervalos simétricos).
- **Intervalo simétrico**: padronize só um extremo, o outro tem o mesmo z com sinal trocado.
- **Caudas**: o complemento do intervalo simétrico divide-se igualmente (68% centrais deixam ≈ 16% em cada cauda).
- **Tabela acumulada**: se dá P(Z < z), a probabilidade entre dois pontos é a diferença F(b) − F(a), com F(0) = 0,5.

# NOTAS

nenhuma. As figuras das curvas sombreadas foram descartadas porque o texto descreve cada área. Exemplos numéricos próprios, com valores da tabela padrão (0,3413; 0,4772; 0,4987) que são os mesmos do material por serem constantes da distribuição. Acrescentado fora do trecho: z ≈ 1,28 para a área 0,4 na exemplificação do caminho inverso, valor conhecido da tabela; e as caudas de ≈ 2,5% e ≈ 0,15%, derivadas dos 95% e 99,7%.
