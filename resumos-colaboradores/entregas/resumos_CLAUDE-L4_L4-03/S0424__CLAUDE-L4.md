---
id: S0424
agente: CLAUDE-L4
materia: Estatística
aula: Aula 14 — Análise de Variância (ANOVA):
trecho: estatistica/a14/s03
paginas_lidas: 28-41
---
# ANALÍTICO

Este trecho aplica a análise de variância à regressão linear: o teste F que diz se o modelo é útil, a tabela ANOVA da regressão, o coeficiente de determinação (R²) e sua versão ajustada, além de uma menção ao Cp de Mallows.

### O modelo e as hipóteses

No modelo de regressão linear simples, cada ponto segue Y = α + β·X + ε, em que:
- X é a variável **explicativa** (regressora ou independente) e Y é a variável **explicada** (resposta ou dependente);
- α é o intercepto (coeficiente linear) e β é o coeficiente angular da reta verdadeira;
- ε é o erro entre o Y verdadeiro e o valor da reta.

Os coeficientes são estimados por a e b (pelo método dos mínimos quadrados), e a estimativa de Y é Ŷ = a + b·X. Se b < 0, a correlação linear é negativa (as variáveis variam em sentidos opostos).

A pergunta que a ANOVA responde: **vale a pena usar o modelo linear?** As hipóteses são:
- **H0: β = 0**: não há relação linear; o modelo não é adequado;
- **H1: β ≠ 0**: há relação linear; o modelo é adequado.

Concluir que o modelo é adequado exige **rejeitar H0** (teste estatisticamente significativo: a chamada "decisão forte"). Na regressão **múltipla** (várias variáveis explicativas), H0 afirma que **todos** os coeficientes são simultaneamente zero; H1, que **pelo menos um** é diferente de zero.

### Decomposição da soma de quadrados

Para cada ponto, o desvio do valor real em relação à média de Y se divide em duas partes: o que o modelo explica (Ŷ − Ȳ) e o erro que sobra (Y − Ŷ, o resíduo e). Somando os quadrados:

SQ total = SQ modelo + SQ erro
Σ(Y − Ȳ)² = Σ(Ŷ − Ȳ)² + Σ(Y − Ŷ)²

| Componente | Fórmula | Significado |
| --- | --- | --- |
| **SQ total** | Σ(Yi − Ȳ)² | variação total de Y (= variância amostral de Y × (n − 1)) |
| **SQ modelo** (regressão) | Σ(Ŷi − Ȳ)² | parte explicada pela reta |
| **SQ erro** (resíduo) | Σ(Yi − Ŷi)² | parte não explicada |

Atalhos de cálculo para a SQ modelo, quando se conhece b e dados de X:
- SQ modelo = b · Σ[(Xi − X̄)(Yi − Ȳ)]
- SQ modelo = b² · Σ(Xi − X̄)² = b² · s²X · (n − 1)

> ⚠️ **Pegadinha:** os cálculos com valores arredondados de a, b e Ŷ fazem SQ modelo + SQ erro não bater exatamente com a SQ total. Isso é efeito de arredondamento; teoricamente a igualdade é exata.

### Graus de liberdade e quadrados médios

| Fonte | Graus de liberdade |
| --- | --- |
| Total | n − 1 |
| Modelo (regressão) | k = número de **variáveis explicativas** (na regressão simples, 1) |
| Erro (resíduo) | GL total − GL modelo = n − k − 1 (na simples, n − 2) |

Os quadrados médios são, como sempre, a soma de quadrados dividida pelos graus de liberdade:
- QM modelo = SQ modelo ÷ k (na simples, igual à própria SQ modelo);
- QM erro = SQ erro ÷ (n − k − 1), chamado também de **erro quadrático médio**;
- QM total = SQ total ÷ (n − 1), que é exatamente a **variância amostral** de Y (não entra no cálculo de F).

A estatística do teste é a mesma da ANOVA geral:

F = QM modelo ÷ QM erro, com distribuição F de Fisher-Snedecor com k graus no numerador e n − k − 1 no denominador.

Rejeita-se H0 se F calculado for maior que o F tabelado (para o α escolhido), ou, de modo equivalente, se o p-valor for menor que α.

Tabela ANOVA da regressão:

| Fonte | GL | SQ | QM | F |
| --- | --- | --- | --- | --- |
| Modelo | k | SQ modelo | SQ modelo ÷ k | QM modelo ÷ QM erro |
| Erro | n − k − 1 | SQ erro | SQ erro ÷ (n − k − 1) | |
| Total | n − 1 | SQ total | | |

> 💡 **Exemplo:** n = 10 pontos, regressão simples, SQ total = 200, SQ modelo = 150, SQ erro = 50. GL: modelo 1, erro 8, total 9. QM modelo = 150; QM erro = 50 ÷ 8 = 6,25; F = 150 ÷ 6,25 = 24. Com α = 5% e graus (1; 8), o valor tabelado é cerca de 5,32; como 24 > 5,32, rejeita-se H0 e o modelo é adequado.

> 💡 **Questão típica:** n = 40 empresas, 2 variáveis regressoras, SQ erro = 555 e SQ total = 755. Então SQ modelo = 200; GL modelo = 2; GL erro = 39 − 2 = 37; QM modelo = 100; QM erro = 555 ÷ 37 = 15; F = 100 ÷ 15 = 20/3, com distribuição F de 2 e 37 graus de liberdade.

> ⚠️ **Pegadinha:** o GL do modelo é o número de variáveis explicativas, não o número de parâmetros. Duas variáveis regressoras dão GL modelo = 2 e GL erro = n − 3.

Quando F é pequeno (muito abaixo do valor tabelado), a reta não explica o suficiente: não se rejeita H0 e conclui-se que o modelo linear não é adequado.

### Coeficiente de determinação (R²)

R² = SQ modelo ÷ SQ total = 1 − SQ erro ÷ SQ total

- Mede a fração da variância total de Y **explicada pelo modelo**.
- Fica entre **0 e 1** (0% a 100%). Em geral, quanto maior, melhor o ajuste e mais forte a relação linear.
- A raiz quadrada de R² é o **módulo do coeficiente de correlação de Pearson**: R = ± √R². O **sinal de R é o mesmo do coeficiente angular b**.
- Por que tirar a raiz? Como R² compara somas de quadrados, ele é medido na unidade ao quadrado; a raiz volta à unidade original dos dados e facilita a interpretação.

> 💡 **Exemplo:** SQ modelo = 150 e SQ total = 200 dão R² = 0,75 (o modelo explica 75% da variação) e |R| = √0,75 ≈ 0,87. Se b for negativo, R ≈ −0,87.

> 💡 **Leitura direta do quadro:** se o quadro ANOVA traz SQ modelo = 4096,1644 e SQ total = 6300,1, R² = 4096,1644 ÷ 6300,1 ≈ 0,65 = 65%.

### Coeficiente de determinação ajustado

Ao acrescentar variáveis explicativas, R² **sempre sobe**, mesmo que a variável nova seja irrelevante; por isso não se deve comparar R² entre modelos com números diferentes de variáveis. O **R² ajustado** corrige isso dividindo cada soma de quadrados pelos seus graus de liberdade:

R² ajustado = 1 − (SQ erro ÷ GL erro) ÷ (SQ total ÷ GL total)

Com k variáveis explicativas, equivale a:

R² ajustado = 1 − [(n − 1) ÷ (n − k − 1)] · (1 − R²)

Na regressão simples (k = 1): R² ajustado = 1 − [(n − 1) ÷ (n − 2)] · (1 − R²).

Propriedades:
- é **sempre menor** que o R² comum (a não ser nos casos extremos de R² = 1);
- **pode ser negativo**, quando o modelo explica muito pouco;
- só aumenta com a nova variável se ela melhorar o modelo mais do que o esperado ao acaso.

> 💡 **Exemplo:** n = 25, k = 3 e R² = 0,80. R² ajustado = 1 − (24 ÷ 21) · 0,20 = 1 − 0,2286 ≈ 0,77, menor que 0,80.

> 💡 **Usando o quadro:** com SQ erro = 100 e GL erro = 10 (QM erro = 10) e SQ total = 1000 e GL total = 11 (QM total ≈ 90,9), R² ajustado = 1 − 10 ÷ 90,9 = 1 − 0,11 = 0,89.

### Cp de Mallows (apenas citação)

O Cp de Mallows ajuda a escolher entre modelos de regressão e avalia a precisão das estimativas: Cp = SQ erro ÷ QM erro − n + 2p, em que p é o número de parâmetros (variáveis explicativas + 1 do intercepto). Em bons modelos, Cp fica próximo de p; em modelos ruins, é bem maior que p.

### Para fixar
- H0 da regressão: β = 0 (modelo inadequado); na múltipla, todos os coeficientes são zero ao mesmo tempo.
- SQ total = SQ modelo + SQ erro; QM total é a variância amostral de Y.
- GL modelo = k (número de variáveis explicativas); GL erro = n − k − 1 (n − 2 na simples); GL total = n − 1.
- F = QM modelo ÷ QM erro; rejeita H0 quando F > tabelado (ou p-valor < α), e aí o modelo é adequado.
- R² = SQ modelo ÷ SQ total, entre 0 e 1; |R| = √R², com o sinal de b.
- R² nunca diminui ao incluir variáveis; por isso se usa o R² ajustado: 1 − (n − 1)/(n − k − 1) · (1 − R²).
- O R² ajustado é menor que R² e pode ser negativo.
- Cp de Mallows próximo de p indica bom modelo.

# SINTÉTICO

- **Hipóteses da ANOVA da regressão**: H0 diz que β = 0 (não há relação linear, modelo inadequado); H1, β ≠ 0. Na regressão múltipla, H0 exige todos os coeficientes nulos e H1 pelo menos um diferente de zero. Rejeitar H0 valida o modelo.
- **Decomposição**: SQ total = SQ modelo + SQ erro; a parte explicada é Σ(Ŷ − Ȳ)² e a não explicada é Σ(Y − Ŷ)².
- **Atalhos**: SQ total = s²Y · (n − 1); SQ modelo = b² · s²X · (n − 1).
- **Graus de liberdade**: modelo = número de variáveis explicativas k; erro = n − k − 1 (n − 2 na regressão simples); total = n − 1.
- **Estatística F**: QM modelo ÷ QM erro, com GL do modelo no numerador e do erro no denominador; rejeita-se H0 se F supera o valor tabelado ou se p-valor < α.
- **QM total**: SQ total ÷ (n − 1) é a variância amostral de Y e não entra no cálculo de F.
- **Exemplo de prova**: n = 40, 2 regressoras, SQ erro 555 e SQ total 755 dão SQ modelo 200, GL 2 e 37, QM 100 e 15, e F = 20/3.
- **Coeficiente de determinação**: R² = SQ modelo ÷ SQ total, entre 0 e 1, é a fração da variância explicada; |R| = √R² e o sinal de R é o de b.
- **R² ajustado**: 1 − (n − 1)/(n − k − 1) · (1 − R²); corrige o fato de R² crescer sempre que se inclui variável, é menor que R² e pode ser negativo.
- **Cp de Mallows**: Cp = SQ erro ÷ QM erro − n + 2p; bons modelos têm Cp próximo de p (número de parâmetros).

# NOTAS

- No exemplo numérico do material (5 alunos), a SQ modelo (1,79) e a SQ erro (8,39) somam 10,18, e não 10, porque usam coeficientes arredondados; o próprio texto explica a diferença. As tabelas com os dados dos alunos não foram reproduzidas; usei exemplos próprios.
- O material afirma, na fórmula alternativa da SQ do modelo, "SQ modelo = b × Σ(Xi − X̄)(Yi − Ȳ)" e depois "b² × Σ(Xi − X̄)²"; as duas são equivalentes porque b = Σ(Xi − X̄)(Yi − Ȳ) ÷ Σ(Xi − X̄)².
- A fórmula do Cp de Mallows aparece como no material (SQ erro ÷ QM erro − n + 2p), sem dizer qual QM erro entra no denominador; na literatura usa-se o QM erro do modelo completo. Não detalhei além do que o texto traz.
- O valor tabelado de F (1; 8) a 5% (cerca de 5,32) usado no exemplo é conhecimento padrão de tabelas, não vem do trecho; o trecho cita f(0,05; 1; 3) = 10,128 para o seu exemplo.
- Quadros ANOVA das questões do IF-PA e EBSERH não foram extraídos como tabela; usei os valores citados nos comentários (SQ modelo 4096,1644 e SQ total 6300,1; SQ erro 100, GL erro 10, SQ total 1000, GL total 11).
