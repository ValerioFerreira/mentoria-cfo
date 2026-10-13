---
id: S0517
agente: CLAUDE-L4
materia: Estatística
aula: Aula 13 — Regressão Linear Múltipla
trecho: estatistica/a13/s01
paginas_lidas: 3-12
---
# ANALÍTICO

A regressão linear múltipla estende a regressão simples para o caso de **duas ou mais variáveis explicativas**. O trecho apresenta o modelo, os pressupostos, a multicolinearidade, a notação matricial e o estimador de mínimos quadrados, com um exemplo numérico e uma questão de prova.

### Do modelo simples ao múltiplo

Na regressão simples a relação é uma reta, Y = α + βx, com α (coeficiente linear, ponto onde a reta corta o eixo y) e β (coeficiente angular, a taxa de variação de Y por unidade de x). Na **regressão múltipla** há uma variável dependente Y e k variáveis independentes (explicativas) X1, ..., Xk. O modelo populacional é:

**Y = α + β1·x1 + β2·x2 + ... + βk·xk + ε**

| Símbolo | Significado |
| --- | --- |
| Y | variável dependente (a que se quer estimar) |
| α | intercepto: valor de base de Y quando todos os x são zero |
| βi | coeficientes de regressão (efeito de cada variável) |
| xi | variáveis independentes ou explicativas |
| ε | erro aleatório |

A equação **estimada** a partir da amostra é **Ŷ = a + b1·x1 + b2·x2 + ... + bk·xk**, em que Ŷ é o valor estimado de Y e os bi são os **coeficientes de regressão parcial**.

O conceito por trás do modelo é o **ceteris paribus** ("tudo o mais constante"): cada coeficiente mede o efeito de uma variável sobre Y mantendo as demais fixas.

> 💡 **Exemplo próprio:** se Ŷ = 10 + 3·x1 − 2·x2, então, com x2 fixo, cada unidade a mais de x1 eleva Ŷ em 3; com x1 fixo, cada unidade a mais de x2 reduz Ŷ em 2.

**Tamanho da amostra:** o número de observações deve superar o de variáveis explicativas em **pelo menos 2**. Com 2 variáveis explicativas, são necessárias ao menos **4 observações**.

### Pressupostos

Como na regressão simples, exigem-se sobre os erros:

1. **Média zero**: E(εi) = 0.
2. **Variância constante** (homocedasticidade): Var(εi) = σ², igual para qualquer valor de X.
3. **Independência**: Corr(εi, εj) = 0 para i ≠ j (os erros não se correlacionam).
4. **Normalidade**: os erros têm distribuição normal.

Há ainda um pressuposto específico do modelo múltiplo: **não pode existir relação linear entre as variáveis independentes**. Se duas variáveis explicativas forem proporcionais (ou muito correlacionadas), ocorre a **multicolinearidade**, que muitas vezes torna as estimativas dos parâmetros insignificantes.

> 💡 **Exemplo próprio de multicolinearidade:** X2 = 5·X1, ou X1 = X2 + 2·X3. Em ambos há uma variável explicativa que é combinação linear de outras.

> ⚠️ **Pegadinha:** multicolinearidade é problema entre as **explicativas**, não entre a dependente e as explicativas (que podem e devem estar correlacionadas).

### Notação matricial

Os parâmetros são estimados com matrizes. O modelo é escrito como **y = Xβ + E**, em que:

- **y**: vetor-coluna dos n valores observados de Y;
- **E**: vetor-coluna dos n erros;
- **β**: vetor-coluna dos parâmetros (α, β1, ..., βk), com k + 1 elementos;
- **X**: matriz das variáveis independentes, n linhas por (k + 1) colunas. A **primeira coluna só tem 1**, pois corresponde ao intercepto; as demais trazem os valores de cada variável.

A equação estimada fica **ŷ = Xβ̂**, com β̂ = (a, b1, ..., bk), e os erros (resíduos) estimados são **E = y − ŷ**.

### Estimador de mínimos quadrados

Pelo método dos mínimos quadrados ordinários (MQO), o estimador é:

**β̂ = (XᵀX)⁻¹ · Xᵀy**

em que Xᵀ é a transposta de X e (XᵀX)⁻¹ é a inversa de XᵀX. Dimensões: XᵀX é quadrada de ordem k + 1; Xᵀy é um vetor-coluna com k + 1 linhas.

Propriedades: os estimadores de MQO são **lineares, não viesados (não viciados) e de variância mínima** entre os lineares; e, supondo erros normais, **coincidem com os de máxima verossimilhança**. A inversa só existe se não houver multicolinearidade (daí a importância do pressuposto).

### Roteiro de cálculo (exemplo do trecho)

O exemplo trabalha com cinco observações: Y valendo de 1 a 5, X1 variando de 1 a 4 (com um valor repetido) e X2 variando de 1 a 5. As etapas são:

1. Montar X (5 linhas por 3 colunas, a primeira só de 1) e achar Xᵀ.
2. Calcular XᵀX (3×3): o elemento (1,1) é n = 5, a primeira linha traz as somas de x1 e x2 (12 e 13) e os demais elementos são somas de quadrados e de produtos (34, 38 e 43 na parte inferior).
3. Inverter XᵀX pelo método da adjunta: transposta da matriz de cofatores dividida pelo determinante, que vale 8.
4. Calcular Xᵀy, um vetor com os valores 15, 43 e 48.
5. Multiplicar: β̂ = (−0,5; 2; −0,5).
6. Obter ŷ = Xβ̂ e os resíduos E = y − ŷ; só as observações 2 e 3 têm erro (−0,5 e +0,5), pois as outras três são ajustadas com exatidão.

O modelo ajustado é **Ŷ = −0,5 + 2·x1 − 0,5·x2**. A banca normalmente não pede todas as etapas (o trabalho é pesado e na prática se usa computador); costuma fornecer (XᵀX)⁻¹ e Xᵀy e cobrar só a multiplicação.

> 💡 **Exemplo próprio da última etapa:** se (XᵀX)⁻¹ = [[0,5; 0,1]; [0,1; 0,4]] e Xᵀy = (20; 10), então β̂ = (0,5·20 + 0,1·10; 0,1·20 + 0,4·10) = (11; 6). Cada linha da inversa multiplica o vetor Xᵀy.

> 💡 **Questão-tipo (Cebraspe):** o enunciado entrega a inversa 3×3 de XᵀX (diagonal 1; 0,8; 1) e o vetor Xᵀy de três elementos (30, 20 e 10), e pede para julgar um β̂ proposto. Basta multiplicar a primeira linha da inversa pelo vetor para obter o primeiro coeficiente, e assim por diante: o resultado é 35, 24 e 17, de modo que a afirmação de β̂ = (35, 24, 17)ᵀ era correta. O ganho de tempo está em não calcular nada além dessa multiplicação.

### Para fixar
- Regressão múltipla: uma variável dependente e duas ou mais explicativas; Y = α + β1·x1 + ... + βk·xk + ε.
- Coeficiente parcial = efeito de uma variável com as outras constantes (ceteris paribus).
- Amostra: n deve superar o número de explicativas em pelo menos 2.
- Erros: média zero, variância constante (homocedasticidade), independentes e normais.
- Multicolinearidade: relação linear entre explicativas; compromete as estimativas.
- Matricial: y = Xβ + E, com primeira coluna de X só de 1.
- MQO: β̂ = (XᵀX)⁻¹Xᵀy; estimador linear, não viesado e de variância mínima; equivale a máxima verossimilhança com erros normais.

# SINTÉTICO

- **Modelo**: Y = α + β1·x1 + ... + βk·xk + ε, com uma variável dependente e duas ou mais explicativas; a versão estimada é Ŷ = a + b1·x1 + ... + bk·xk.
- **Coeficientes parciais**: cada bi mede o efeito de xi sobre Y mantendo as demais constantes (ceteris paribus).
- **Observações mínimas**: o tamanho da amostra deve superar o número de explicativas em pelo menos 2 (com 2 explicativas, ao menos 4 observações).
- **Pressupostos dos erros**: média zero, variância constante (homocedasticidade), ausência de correlação entre eles e distribuição normal.
- **Multicolinearidade**: relação linear entre variáveis explicativas (ex.: uma proporcional à outra); torna insignificantes as estimativas dos parâmetros.
- **Forma matricial**: y = Xβ + E; X tem n linhas e a primeira coluna só de 1 (intercepto); a equação estimada é ŷ = Xβ̂.
- **Estimador MQO**: β̂ = (XᵀX)⁻¹Xᵀy; exige XᵀX inversível, ou seja, sem multicolinearidade.
- **Propriedades do MQO**: lineares, não viciados, de variância mínima entre os lineares e iguais aos de máxima verossimilhança sob erros normais.
- **Resíduos**: E = y − ŷ, a diferença entre o observado e o estimado.
- **Cálculo em prova**: costuma bastar multiplicar (XᵀX)⁻¹ pelo vetor Xᵀy, linha por coluna, para achar β̂.

# NOTAS

- Fórmulas e matrizes saíram embaralhadas na extração; foram reconstruídas e todos os números do exemplo (XᵀX, determinante 8, Xᵀy, β̂, ŷ, erros) e da questão (35, 24, 17) foram reconferidos por cálculo.
- Pág. 5 do material: a matriz X é descrita como representando "X1, X2, ..., Xn"; o correto é X1, ..., Xk (n é o número de observações). O resumo usa k.
- Pág. 10 do material: na linha que desenvolve ŷ aparecem sinais de subtração onde a conta é soma (ex.: "1 × (−0,5) − 1 × 2 + ..."); o resultado numérico (1; 2,5; 2,5; 4; 5) está correto e é o usado no resumo.
- Pág. 11 do material: o enunciado usa ε para os erros e o material usa E; tratados como equivalentes.
- Figuras/tabelas de dados do exemplo foram reconstruídas em texto (valores de Y, X1, X2 conferidos).
- Os exemplos "próprio" (interpretação dos coeficientes, multicolinearidade, multiplicação 2×2) são do autor do resumo; nada foi acrescentado fora do trecho além deles.
