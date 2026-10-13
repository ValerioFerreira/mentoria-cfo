---
id: S0393
agente: CLAUDE-L4
materia: Estatística
aula: Aula 12 — Regressão Linear Simples
trecho: estatistica/a12/s04
paginas_lidas: 46-60
---
# ANALÍTICO

Este trecho completa a regressão linear simples: mostra como a máxima verossimilhança chega às mesmas estimativas dos mínimos quadrados e, principalmente, como a análise de variância (ANOVA) decompõe a variação de Y, mede a qualidade do ajuste (R² e R² ajustado) e testa se a inclinação é diferente de zero (estatística F).

### Estimativa por máxima verossimilhança (EMV)

A EMV procura os valores de a e b que tornam **máxima a probabilidade de se observar a amostra obtida**. Parte-se do modelo Y = α + βX + ε com erros independentes, de mesma distribuição normal, média zero e variância σ². A função de verossimilhança é o produto, sobre as n observações, da densidade normal de cada Yi (centrada em α + β·Xi); para facilitar, usa-se seu logaritmo natural:

log L = −(n/2) · log(2πσ²) − (1 / 2σ²) · Σ(Yi − α − β·Xi)²

Maximizar log L em relação a α e β é o mesmo que **minimizar Σ(Yi − α − β·Xi)²**. Igualando a zero as derivadas parciais, chega-se a Σ(Yi − a − b·Xi) = 0 e Σ(Yi − a − b·Xi)·Xi = 0, ou seja, o mesmo sistema do MQO. Conclusão: **sob normalidade dos erros, a EMV de a e b coincide com a dos mínimos quadrados**:

- b = Σ(Xi − X̅)(Yi − Y̅) / Σ(Xi − X̅)²
- a = Y̅ − b·X̅

Para a variância, a EMV é σ̂² = (1/n) · Σ(Yi − a − b·Xi)², com divisor n. Interpretação: a é o valor médio estimado de Y quando X = 0; b é a variação esperada de Y a cada unidade a mais de X; σ̂² mede a dispersão dos pontos em torno da reta.

### Ideia da análise de variância

Para saber se vale a pena usar a reta, compara-se o resíduo do modelo de regressão (Yi = α + β·Xi + ε) com o do modelo mais simples, em que Y flutua em torno de uma média única (Yi = μ + ε). Se a redução do resíduo for pequena, a inclinação β é nula ou quase, e os dois modelos são equivalentes. Testa-se, então:

- **H0: β = 0** (não há relação linear significativa entre X e Y);
- **H1: β ≠ 0**.

### Graus de liberdade

| Fonte | Graus de liberdade |
| --- | --- |
| Modelo | 2 − 1 = **1** (dois parâmetros, α e β, menos um) |
| Resíduos | **n − 2** |
| Total | **n − 1** |

Vale GL total = GL modelo + GL resíduos. É por aí que se descobre n em questões: o GL total mais 1 é o tamanho da amostra.

### Somas de quadrados

Escrevendo o resíduo como ei = Yi − Ŷi, o desvio de cada Yi em relação à média se divide em duas partes: Yi − Y̅ = (Ŷi − Y̅) + ei. Elevando ao quadrado e somando, o termo cruzado é nulo, e resta a decomposição:

**SQT = SQM + SQR**

| Soma | Significado | Fórmulas |
| --- | --- | --- |
| **SQT** (total) | variação total de Y | Σ(Yi − Y̅)² = Syy |
| **SQM** (modelo ou regressão) | parte **explicada** pela reta | Σ(Ŷi − Y̅)² = b·Sxy = b²·Sxx |
| **SQR** (resíduos ou erros) | parte **não explicada** | Σ(Yi − Ŷi)² = SQT − SQM |

> ⚠️ **Pegadinha de notação:** algumas questões usam "SQR" para a soma de quadrados da **regressão** (modelo), e não dos resíduos. Na maioria, SQR é a dos resíduos. Veja sempre as definições do enunciado ou o rótulo das linhas da tabela.

### Coeficiente de determinação (R²)

Mede a qualidade do ajuste: a fração da variação total de Y que a reta explica.

**R² = SQM / SQT = 1 − SQR / SQT**, com **0 ≤ R² ≤ 1**.

Quanto mais perto de 1, melhor o ajuste e mais forte a relação linear; perto de 0, a reta explica pouco. Por exemplo, R² = 0,95 quer dizer que 95% da variação de Y é explicada pelo modelo e 5% vêm de aleatoriedade ou fatores omitidos. O coeficiente de correlação linear é a raiz quadrada: **R = √(SQM/SQT)** (em módulo; o sinal é o de b).

### Quadrados médios e R² ajustado

Quadrado médio = soma de quadrados ÷ graus de liberdade:

- **QMM** = SQM / 1
- **QMR** = SQR / (n − 2): estimativa de σ², a variância dos erros
- **QMT** = SQT / (n − 1)

O **R² ajustado** corrige R² pelos graus de liberdade (útil sobretudo em regressão múltipla, mas cobrado também na simples):

**R² ajustado = 1 − [SQR/(n−2)] / [SQT/(n−1)] = 1 − QMR/QMT = 1 − (1 − R²) · (n−1)/(n−2)**

Como (n−1)/(n−2) > 1, o R² ajustado é sempre menor que R².

### Estatística F e tabela ANOVA

Para testar H0: β = 0 usa-se **F* = QMM / QMR**. Sob H0, F* segue a distribuição F de Snedecor com **1 e n − 2** graus de liberdade. Se F* for grande o bastante, rejeita-se H0:

- F* > F crítico: rejeita-se H0 (há relação linear significativa);
- F* < F crítico: não se rejeita H0.

O F crítico vem da tabela F (1 gl no numerador, n−2 no denominador), para o nível de significância escolhido. Atenção: essa razão F testa a **inclinação β**, e não o intercepto α.

A tabela ANOVA tem sempre este formato (as questões costumam omitir algumas células, que você deve calcular):

| Fonte | GL | Soma de quadrados | Quadrado médio | F |
| --- | --- | --- | --- | --- |
| Modelo | 1 | SQM | QMM = SQM/1 | QMM/QMR |
| Resíduos | n − 2 | SQR | QMR = SQR/(n−2) | |
| Total | n − 1 | SQT | QMT = SQT/(n−1) | |

> 💡 **Exemplo:** com n = 5, X = 1, 2, 3, 4, 5 e Y = 3, 5, 4, 8, 10, tem-se b = 1,7, Sxy = 17, Sxx = 10 e Syy = 34. Então SQT = 34; SQM = b · Sxy = 28,9; SQR = 34 − 28,9 = 5,1. GL: 1, 3 e 4. QMM = 28,9; QMR = 5,1/3 = 1,7; F* = 28,9/1,7 = 17. R² = 28,9/34 = 0,85 e R² ajustado = 1 − 0,15 · (4/3) = 0,80.

> 💡 **Exemplo de tabela incompleta:** se o GL total é 10 (logo n = 11), SQM = 450 e SQR = 90, então SQT = 540; GL dos resíduos = 9; QMM = 450; QMR = 90/9 = 10 (estimativa de σ²); F* = 45; R² = 450/540 ≈ 0,83; R² ajustado = 1 − 10/54 ≈ 0,81, pois QMT = 540/10 = 54.

### Para fixar

- Sob erros normais, EMV e MQO dão os mesmos a e b; a EMV de σ² usa divisor n, e o QMR usa n − 2.
- ANOVA testa H0: β = 0 (sem relação linear); F* = QMM/QMR ~ F(1; n−2).
- GL: modelo 1, resíduos n − 2, total n − 1; o total mais 1 revela n.
- SQT = SQM + SQR; SQM = b·Sxy = b²·Sxx; SQT = Syy.
- R² = SQM/SQT = 1 − SQR/SQT, entre 0 e 1; R = √R², com o sinal de b.
- QMR estima σ²; R² ajustado = 1 − QMR/QMT, sempre menor que R².
- Cuidado com a sigla SQR, que algumas questões usam para a regressão.

# SINTÉTICO

- **EMV**: com erros normais independentes, maximizar a verossimilhança equivale a minimizar Σ(Y − a − bX)², portanto dá os mesmos a e b do MQO; a variância pela EMV usa divisor n.
- **Teste da regressão**: H0: β = 0 contra H1: β ≠ 0; rejeitar H0 indica relação linear significativa entre X e Y.
- **Graus de liberdade**: modelo 1, resíduos n − 2, total n − 1; o GL total mais 1 dá o tamanho da amostra.
- **Decomposição**: SQT = SQM + SQR, com SQM = b·Sxy = b²·Sxx (explicada) e SQR = resíduos; cuidado, pois certas questões chamam a soma da regressão de SQR.
- **R²**: SQM/SQT = 1 − SQR/SQT, entre 0 e 1, é a fração da variação de Y explicada pela reta; R = √R² (sinal de b).
- **Quadrados médios e ajustado**: QMM = SQM/1, QMR = SQR/(n−2) estima σ² e QMT = SQT/(n−1); R² ajustado = 1 − QMR/QMT, menor que R².
- **Estatística F**: F* = QMM/QMR segue F(1; n−2) sob H0; se F* superar o valor crítico, rejeita-se H0 (teste da inclinação, não do intercepto).

# NOTAS

- Nenhuma página vazia ou ilegível. A tabela comparativa de resíduos (modelo tradicional × modelo pela origem, p. 46) só repete o que o trecho anterior ensina (no modelo pela origem, a soma dos resíduos pode ser diferente de zero) e não foi reproduzida.
- Divergência no material: o texto diz que σ̂² da EMV é a soma dos quadrados dos resíduos "dividida pelos graus de liberdade", mas a fórmula escrita usa o divisor n. Adotei a fórmula (EMV com divisor n) e contrastei com o QMR, que usa n − 2.
- Em questões de concurso reproduzidas no material, "SQR" é usada ora para resíduos, ora para a regressão (inclusive na solução da p. 57, em que R = √(SQR/SQT) com SQR = 900 do modelo); registrei como pegadinha de notação.
- Acrescentei por conta própria que R tem o sinal de b e que o R² ajustado é sempre menor que R² (consequência da fórmula).
- Os exemplos numéricos do resumo são originais; os dados do material (tabela ANOVA de leitos por habitante) não foram reproduzidos.
