---
id: S0387
agente: CLAUDE-L4
materia: Estatística
aula: Aula 12 — Regressão Linear Simples
trecho: estatistica/a12/s03
paginas_lidas: 30-45
---
# ANALÍTICO

A regressão linear simples dá continuidade à ideia de correlação: em vez de apenas medir se duas variáveis caminham juntas, ela escreve uma equação de reta para prever uma variável (a dependente, Y) a partir da outra (a independente, X). O trecho cobre a equação da reta, o modelo e seus pressupostos, a estimação pelos mínimos quadrados ordinários (MQO), as variâncias dos estimadores e o caso da reta forçada pela origem.

### A reta e o modelo de regressão

Na geometria, a reta é y = m·x + b: **m** é o coeficiente angular (taxa de variação) e **b** é o coeficiente linear (ponto em que a reta corta o eixo y). O sinal de m diz o comportamento: m > 0, função crescente; m < 0, decrescente; m = 0, constante. Dados dois pontos (x0, y0) e (x, y), m = Δy/Δx = (y − y0)/(x − x0), sempre mantendo a mesma ordem de subtração no numerador e no denominador. Depois, substitui-se um dos pontos para achar b.

> 💡 **Exemplo:** a reta que passa por (1, 4) e (3, 10) tem m = (10 − 4)/(3 − 1) = 3. Com o ponto (1, 4): 4 = 3·1 + b, logo b = 1 e a reta é y = 3x + 1, que corta o eixo y em (0, 1).

Quando os pontos estão todos alinhados (correlação perfeita), uma reta exata resolve. Na prática os dados se espalham, e a regressão acomoda essa variabilidade com um **termo de erro**. O modelo populacional é:

**Yi = α + β·Xi + εi**, para i = 1, 2, …, n.

- **α + β·Xi** é a parte que varia linearmente com X: o valor esperado de Y dado X, E(Yi | Xi = X) = α + β·X.
- **εi** é o erro aleatório, que reúne tudo que o modelo linear não explica (desvios para cima e para baixo da reta).
- **Yi** é a variável dependente (ou resposta); **Xi** é a independente (também chamada regressora, explanatória ou explicativa).

Atenção à notação: no modelo, α e β são os parâmetros populacionais (desconhecidos); suas estimativas amostrais são **a** e **b**. Assim, a reta estimada é Ŷi = a + b·Xi, e **b aqui é o coeficiente angular** (inclinação), diferentemente da fórmula y = m·x + b da álgebra, em que b era o intercepto.

### Pressupostos sobre o erro

| Pressuposto | Significado | Se violado |
| --- | --- | --- |
| E(εi) = 0 | média dos erros nula: desvios acima e abaixo da reta se compensam | — |
| Var(εi) = σ² | variância constante, qualquer que seja X: **homocedasticidade** | **heterocedasticidade** |
| Cov(εi, εj) = 0, i ≠ j | erros não correlacionados (independentes) | **autocorrelação** |

> ⚠️ **Pegadinha:** a banca troca os termos. Variância constante dos erros é homocedasticidade; variâncias diferentes, heterocedasticidade; erros correlacionados entre si, autocorrelação.

### Mínimos quadrados ordinários (MQO)

O MQO escolhe, entre todas as retas possíveis, a que **minimiza a soma dos quadrados dos resíduos**. O resíduo é a diferença entre o valor observado e o valor ajustado pela reta: ei = Yi − Ŷi. Portanto, o critério é minimizar Σei² = Σ(Yi − a − b·Xi)².

Para achar a e b, deriva-se essa soma em relação a cada um e iguala-se a zero. Isso gera duas equações simultâneas (as "equações normais"): Σ(Yi − a − b·Xi) = 0 e ΣXi·(Yi − a − b·Xi) = 0. Resolvendo o sistema, chega-se às fórmulas abaixo. A primeira equação mostra que, no modelo com intercepto, **a soma dos resíduos é zero**.

### Estimador da inclinação (b)

A inclinação mede quanto Y varia, em média, para cada aumento de uma unidade em X. Há formas equivalentes de calculá-la:

| Forma | Fórmula |
| --- | --- |
| Por desvios | b = Σ[(Xi − X̅)(Yi − Y̅)] / Σ(Xi − X̅)² |
| Covariância e variância | b = Cov(X, Y) / Var(X) |
| Por somas (a mais prática) | b = (ΣXiYi − n·X̅·Y̅) / (ΣXi² − n·X̅²) |
| Notação S | b = Sxy / Sxx |
| Pela correlação | b = ρ · (σy / σx) |

Na notação S: Sxx = Σ(Xi − X̅)² = ΣXi² − n·X̅² (variabilidade de X); Sxy = Σ(Xi − X̅)(Yi − Y̅) = ΣXiYi − n·X̅·Y̅ (indica direção e força da relação linear); Syy = Σ(Yi − Y̅)² = ΣYi² − n·Y̅² (variabilidade de Y).

A forma com Cov/Var é igual à de desvios porque o divisor (n) é o mesmo na covariância e na variância e se cancela. Na forma b = ρ·σy/σx, ρ é o coeficiente de correlação de Pearson (entre −1 e +1): o sinal de b é o sinal de ρ, e b só é zero se a correlação for zero.

### Estimador do intercepto (a)

A reta estimada **sempre passa pelo ponto das médias (X̅, Y̅)**. Daí vem:

**a = Y̅ − b·X̅**

O intercepto a é o valor esperado de Y quando X = 0.

### Exemplo resolvido

Cinco observações: X = 1, 2, 3, 4, 5 e Y = 3, 5, 4, 8, 10. As médias são X̅ = 3 e Y̅ = 6. Desvios de X: −2, −1, 0, 1, 2; desvios de Y: −3, −1, −2, 2, 4. Produtos dos desvios: 6, 1, 0, 2, 8, somando Sxy = 17. Quadrados dos desvios de X: 4, 1, 0, 1, 4, somando Sxx = 10.

- b = 17/10 = 1,7
- a = 6 − 1,7 · 3 = 0,9
- Reta: Ŷ = 0,9 + 1,7·X; para X = 6, a previsão é 0,9 + 10,2 = 11,1.

Conferência: os valores ajustados são 2,6; 4,3; 6,0; 7,7; 9,4 e os resíduos (0,4; 0,7; −2,0; 0,3; 0,6) somam zero.

> 💡 **Exemplo com somas:** com n = 10, ΣX = 60, ΣY = 90, ΣXY = 630 e ΣX² = 450, as médias são 6 e 9; b = (630 − 10·6·9)/(450 − 10·36) = 90/90 = 1 e a = 9 − 1·6 = 3. Logo Ŷ = 3 + X.

Dois atalhos que aparecem em prova: (i) como a reta passa por (X̅, Ȳ), se a questão informa a e as médias, descobre-se b por Ȳ = a + b·X̅; (ii) se a reta for ajustada só com uma constante (sem X), a melhor constante pelo MQO é a **média** dos valores. Em previsões com tempo t = 1, 2, …, n, converta o ano para o valor de t antes de aplicar a reta.

### Variâncias das estimativas

- **Variância dos erros:** σ̂² = Σ(Yi − Ŷi)² / (n − 2). O divisor é n − 2 (e não n) porque dois parâmetros, a e b, foram estimados.
- **Variância de b:** Var(b) = σ̂² / Σ(Xi − X̅)². Quanto maior a dispersão de X, menor a incerteza sobre a inclinação.
- **Variância de a:** Var(a) = σ̂² · [1/n + X̅² / Σ(Xi − X̅)²], em que X̅² é o quadrado da média de X. Depende de n, da posição média de X e da sua variabilidade.

Essas variâncias servem para: construir **intervalos de confiança** de a e b; fazer **testes de hipóteses** (por exemplo, se b é diferente de zero, o que indicaria relação significativa entre X e Y); e avaliar a **precisão** das previsões (variância menor, estimativa mais confiável).

No exemplo resolvido: Σe² = 0,16 + 0,49 + 4 + 0,09 + 0,36 = 5,1; σ̂² = 5,1/3 = 1,7; Var(b) = 1,7/10 = 0,17.

### Reta passando pela origem

Em alguns problemas, a teoria exige que a reta passe pela origem, isto é, o intercepto é nulo (α = 0). O modelo vira **Yi = β·Xi + εi**, e a reta ajustada é **Ŷi = b·Xi**. Pelo MQO (minimizando Σ(Yi − b·Xi)²):

**b = ΣXiYi / ΣXi²**

Note que nesta fórmula **não se subtraem as médias**. Os resíduos continuam sendo ei = Yi − Ŷi, mas aqui **não há garantia de que somem zero**, porque a reta deixa de passar necessariamente por (X̅, Y̅).

> 💡 **Exemplo:** X = 1, 2, 3 e Y = 2, 3, 7. ΣXY = 2 + 6 + 21 = 29 e ΣX² = 1 + 4 + 9 = 14, então b = 29/14 ≈ 2,07 e Ŷ = 2,07·X. Os resíduos são ≈ −0,07; −1,14; 0,79, com soma ≈ −0,43, diferente de zero.

> ⚠️ **Pegadinha:** no modelo com intercepto, b = Sxy/Sxx e a soma dos resíduos é zero; no modelo pela origem, b = ΣXY/ΣX² e a soma dos resíduos pode ser diferente de zero. Os valores de b dos dois modelos, para os mesmos dados, geralmente diferem.

### Para fixar

- Modelo: Yi = α + β·Xi + εi; reta estimada Ŷ = a + b·X, com b = inclinação e a = intercepto.
- Pressupostos do erro: média zero, variância constante (homocedasticidade) e erros não correlacionados (ausência de autocorrelação).
- MQO minimiza a soma dos quadrados dos resíduos, ei = Yi − Ŷi.
- b = Sxy/Sxx = Cov(X,Y)/Var(X) = ρ·σy/σx; a = Ȳ − b·X̅; a reta passa por (X̅, Ȳ).
- Variância dos erros estimada com divisor n − 2; Var(b) = σ̂²/Sxx.
- Pela origem: b = ΣXY/ΣX², sem médias, e os resíduos não precisam somar zero.
- Em previsão, substitua o X pedido na reta; confira se o enunciado dá a, as médias ou somas para cada caminho de cálculo.

# SINTÉTICO

- **Modelo**: Yi = α + β·Xi + εi; Y é a variável dependente (resposta) e X a independente (explicativa); estimada, a reta é Ŷ = a + b·X, com b como inclinação.
- **Pressupostos do erro**: média zero, variância constante (homocedasticidade; o contrário é heterocedasticidade) e erros não correlacionados (o contrário é autocorrelação).
- **MQO**: escolhe a reta que minimiza Σei², com resíduo ei = Yi − Ŷi, obtida igualando a zero as derivadas em relação a a e b.
- **Inclinação**: b = Sxy/Sxx = Cov(X,Y)/Var(X) = ρ·σy/σx; a forma prática por somas é (ΣXY − n·X̅·Ȳ)/(ΣX² − n·X̅²).
- **Intercepto**: a = Ȳ − b·X̅, valor esperado de Y quando X = 0; a reta passa sempre por (X̅, Ȳ).
- **Variâncias**: σ̂² = Σe²/(n − 2); Var(b) = σ̂²/Sxx; Var(a) = σ̂²·[1/n + X̅²/Sxx]; servem a intervalos de confiança, testes e precisão.
- **Reta pela origem**: α = 0, Ŷ = b·X com b = ΣXY/ΣX²; os resíduos não precisam somar zero, ao contrário do modelo com intercepto.

# NOTAS

- Nenhuma página vazia ou ilegível; as figuras (gráficos de dispersão com a reta) foram descartadas por apenas ilustrar o texto.
- A fórmula de Var(a) vem com o termo "X̅²" em notação truncada no material; adotei o quadrado da média de X (forma padrão), e não a média dos quadrados.
- Os exemplos numéricos do resumo (dados, reta e comparações) são originais, calculados e conferidos por mim; os do material (notas de alunos, quatro notas do professor, questões de concursos) não foram reproduzidos.
- A questão de concurso do material sobre o erro seguir a distribuição normal padrão (dada Y normal padrão) foi omitida: o raciocínio exposto ignora a variância de X e não é um fundamento da teoria, então preferi não registrá-lo no resumo.
- Acrescentei por conta própria dois fatos corretos e usuais: a soma dos resíduos é zero no modelo com intercepto (consequência da primeira equação normal) e o divisor n − 2 se explica pelos dois parâmetros estimados.
