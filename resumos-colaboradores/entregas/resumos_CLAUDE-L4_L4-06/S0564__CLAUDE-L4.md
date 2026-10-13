---
id: S0564
agente: CLAUDE-L4
materia: Estatística
aula: Aula 08 — Distribuições Discretas de Probabilidade
trecho: estatistica/a08/s06
paginas_lidas: 65-70
---
# ANALÍTICO

A distribuição binomial negativa (ou de Pascal) conta quantos ensaios de Bernoulli são necessários até obter um número fixo de sucessos. O trecho traz a fórmula de probabilidade, a lógica da combinação, o suporte, a esperança e a variância, a relação com a geométrica, a parametrização pelo número de fracassos e como reconhecer o modelo nas questões.

### Binomial × binomial negativa

| | Binomial | Binomial negativa |
| --- | --- | --- |
| Fixo | número de ensaios n | número de sucessos k |
| Variável aleatória | número de sucessos | número de ensaios até o k-ésimo sucesso |
| Exemplo | lançar a moeda 10 vezes e contar caras | lançar a moeda até sair a 5ª cara |

Os parâmetros são **p** (probabilidade de sucesso em cada ensaio) e **k** (sucessos desejados): X ~ BN(p, k). Os ensaios devem ser independentes, com p constante. Em retiradas de uma população, isso exige população infinita (ou muito grande frente à amostra) ou retiradas com reposição.

### Função de probabilidade

Probabilidade de precisar de exatamente x ensaios para atingir k sucessos:

**P(X = x) = C(x − 1, k − 1) · p^k · q^(x − k)**, com q = 1 − p.

A combinação é **C(x − 1, k − 1)** e não C(x, k), como na binomial. Motivo: o último ensaio é, necessariamente, o k-ésimo sucesso (se fosse antes, os ensaios teriam parado antes). Resta distribuir os k − 1 sucessos anteriores entre os x − 1 ensaios restantes.

O valor de X vai de **k em diante, sem limite superior**: x = k, k + 1, k + 2, … (no mínimo k ensaios; pode sempre faltar mais um sucesso).

> 💡 **Exemplo próprio:** probabilidade de exatamente 5 ensaios para conseguir 3 sucessos, com p = 0,3: P(X = 5) = C(4, 2) · 0,3³ · 0,7² = 6 · 0,027 · 0,49 ≈ 0,079 (7,9%). O 5º ensaio é sucesso; entre os 4 primeiros, 2 foram sucessos e 2 fracassos.

> 💡 **Exemplo próprio (peças):** 15% das peças têm defeito. Chance de inspecionar exatamente 3 peças até achar 2 defeituosas: p = 0,15, k = 2, x = 3: C(2, 1) · 0,15² · 0,85 = 2 · 0,0225 · 0,85 ≈ 0,038 (3,8%).

### Esperança e variância

**E(X) = k / p**   **V(X) = k · q / p²**

A esperança mantém a proporção de sucessos: com moeda justa (p = 0,5) e k = 5, espera-se lançar 5/0,5 = 10 vezes. No exemplo das peças, com p = 0,15 e k = 2: E = 2/0,15 ≈ 13,3 e V = 2 · 0,85/0,0225 ≈ 75,6.

### Relação com a geométrica

A **geométrica** (ensaios até o 1º sucesso) é a binomial negativa com **k = 1**: a fórmula vira p · q^(x − 1), a média 1/p e a variância q/p². Inversamente, a binomial negativa é a **soma de k variáveis geométricas independentes com o mesmo p**: cada geométrica mede a espera por um sucesso.

### Parametrização pelo número de fracassos

Em vez de contar os ensaios totais x, pode-se contar os **fracassos y** antes do k-ésimo sucesso, com x = y + k:

**P(Y = y) = C(k + y − 1, k − 1) · p^k · q^y**, com y = 0, 1, 2, …

O suporte começa em **zero** (pode não haver fracasso algum). É o mesmo evento visto de outro ângulo: 5 sucessos em 8 lançamentos equivalem a 3 fracassos, e as duas probabilidades coincidem. Como Y = X − k, a média do número de fracassos é k·q/p (média de X menos k) e a variância é a mesma do X, k·q/p².

> ⚠️ **Pegadinha:** descubra qual parametrização o enunciado usa. Se a função de probabilidade tem expoente **q^y com y começando em 0**, trata-se de contagem de fracassos (média kq/p); se conta ensaios, começando em k, a média é k/p.

### Como reconhecer o modelo (questões)

| Se o enunciado fala em... | Modelo |
| --- | --- |
| número de sucessos em n ensaios fixos (com reposição) | binomial |
| ensaios até o **primeiro** sucesso | geométrica |
| ensaios até o **k-ésimo** sucesso (k > 1) | binomial negativa |
| sucessos em um intervalo fixo de tempo/espaço | Poisson |
| sucessos em amostra fixa, **sem** reposição | hipergeométrica |

> ⚠️ **Pegadinha:** "retirar uma amostra com reposição de 10 peças e contar quantas são defeituosas" é binomial, não binomial negativa, pois o tamanho (n = 10) é fixo. A binomial negativa exige parar quando se alcança o número de sucessos desejado.

A soma de duas ou mais geométricas independentes com o mesmo p é binomial negativa. Em questão com média da soma de duas dessas variáveis, aplique E = k/p com k = 2 (ou kq/p se a variável conta fracassos), verificando o suporte.

### Para fixar
- Binomial negativa: número de ensaios até k sucessos (k fixo); binomial: sucessos em n ensaios (n fixo).
- P(X = x) = C(x − 1, k − 1) · p^k · q^(x − k), para x = k, k + 1, …
- O último ensaio é sempre o k-ésimo sucesso; por isso a combinação é C(x − 1, k − 1).
- E(X) = k/p e V(X) = kq/p².
- k = 1 dá a geométrica; a binomial negativa é a soma de k geométricas de mesmo p.
- Variante por fracassos: P(Y = y) = C(k + y − 1, k − 1) · p^k · q^y, com y = 0, 1, 2, …
- Reconheça pela expressão "até o k-ésimo sucesso"; amostra de tamanho fixo é binomial (ou hipergeométrica, sem reposição).

# SINTÉTICO

- **Definição**: a binomial negativa (Pascal) conta os ensaios de Bernoulli necessários para obter k sucessos; os parâmetros são p e k, e k é o valor fixo.
- **Probabilidade**: P(X = x) = C(x − 1, k − 1) · p^k · q^(x − k), com x = k, k + 1, … e sem limite superior.
- **Combinação C(x − 1, k − 1)**: o último ensaio é obrigatoriamente o k-ésimo sucesso, então só os k − 1 anteriores são distribuídos entre x − 1 ensaios.
- **Esperança e variância**: E = k/p e V = kq/p²; com moeda justa e 5 caras, espera-se 10 lançamentos.
- **Geométrica**: é o caso k = 1 (média 1/p, variância q/p²); a binomial negativa é a soma de k geométricas independentes de mesmo p.
- **Fracassos como variável**: P(Y = y) = C(k + y − 1, k − 1) · p^k · q^y, com y começando em 0 e x = y + k; é o mesmo evento por outro ângulo.
- **Independência**: exige ensaios independentes, ou seja, população infinita ou muito grande, ou retirada com reposição.
- **Reconhecer o modelo**: "até o k-ésimo sucesso" indica binomial negativa; tamanho de amostra fixo indica binomial (com reposição).

# NOTAS

Divergência no material: a última questão (soma de dois atendimentos, com P(Y = y) = 0,1 · 0,9^y e y = 0, 1, 2, …) usa E = k/p = 20, mas, como a função começa em zero e conta fracassos, a média de cada Y é q/p = 9 e a de T é 18. O gabarito (E[T] < 17: Errado) vale nos dois cálculos. O resumo ensina a diferença das duas parametrizações. Acrescentado fora do trecho: média e variância do número de fracassos (kq/p e kq/p²), obtidas de Y = X − k. Exemplos numéricos próprios.
