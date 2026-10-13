---
id: S0461
agente: CLAUDE-L4
materia: Estatística
aula: Aula 04 — Medidas de Variabilidade ou Dispersão
trecho: estatistica/a04/s06
paginas_lidas: 62-72
---
# ANALÍTICO

Este trecho apresenta as duas medidas de **dispersão relativa**: o **coeficiente de variação** (CV) e a **variância relativa** (VR). Elas permitem comparar a variabilidade de conjuntos com médias muito diferentes ou unidades diferentes, o que o desvio padrão sozinho não consegue.

### Por que uma medida relativa

O desvio padrão serve para comparar duas séries quando elas estão na **mesma unidade** (por exemplo, ambas em centímetros) e possuem médias semelhantes. Se as séries têm unidades distintas (kg e cm) ou médias de ordens de grandeza diferentes, o desvio padrão perde o sentido comparativo. A solução é medir a variação **em relação à média**, o que gera uma medida **adimensional** (sem unidade).

### Coeficiente de variação (dispersão relativa)

O CV é o desvio padrão dividido pela média, expresso em porcentagem:

| Caso | Fórmula |
| --- | --- |
| População | CV = σ / μ × 100 (%) |
| Amostra | CV = s / x̄ × 100 (%) |

Quanto **menor** o CV, mais **homogêneos** são os dados (menor a dispersão em torno da média). As regras empíricas de classificação:

| Faixa do CV | Dispersão | Classificação da distribuição |
| --- | --- | --- |
| CV < 15% | baixa | homogênea |
| 15% < CV < 30% | média | homogênea |
| CV > 30% | elevada | heterogênea |

Ou seja, a distribuição é **homogênea** quando o CV é menor que 30% e **heterogênea** quando é maior que 30%.

> 💡 **Exemplo do trecho:** salário médio dos homens R$ 1.800 com desvio padrão R$ 810 (CV = 810/1.800 = 45%); salário médio das mulheres R$ 1.500 com desvio padrão R$ 705 (CV = 705/1.500 = 47%). A dispersão relativa das mulheres é maior, embora o desvio padrão absoluto dos homens também seja maior; as duas são distribuições de elevada dispersão (CV > 30%).

> 💡 **Exemplo próprio:** pesos de um grupo têm média 70 kg e desvio padrão 7 kg (CV = 10%); alturas do mesmo grupo têm média 170 cm e desvio padrão 10 cm (CV ≈ 5,9%). O 7 é menor que o 10, mas isso não diz nada, pois as unidades diferem; pelo CV, os pesos variam proporcionalmente mais que as alturas.

> ⚠️ **Pegadinha:** comparar variabilidade entre grupos com desvio padrão só vale com mesma unidade e médias parecidas. Em caso contrário, a resposta certa é calcular o CV. Além disso, o CV perde o sentido quando a média está próxima de zero (a razão explode). E, pelas propriedades da variância e do desvio padrão, multiplicar todos os dados por uma constante positiva **não altera o CV** (σ e μ mudam na mesma proporção), enquanto somar uma constante muda a média, mas não o desvio padrão, e portanto **altera o CV**.

#### Como as questões usam o CV

Quase sempre é preciso recuperar o desvio padrão (ou a média) a partir do CV: σ = CV × média. Em seguida usa-se a variância (σ²) ou a relação entre as medidas. Vale reconhecer quatro situações cobradas.

**1. Combinar dois grupos com a mesma média.** Se duas subpopulações têm a mesma média, a média geral é a mesma e a variância geral é a **média ponderada das variâncias** (pelos tamanhos). Para obter cada variância parte-se do CV: σ = CV × média.

> 💡 **Exemplo do trecho, em resumo:** 200 empregados (120 homens e 80 mulheres), média de 5 mil reais nos dois grupos; CV de 30% para eles e 20% para elas. Desvios: 1,5 e 1,0; variâncias: 2,25 e 1,0. Variância geral = (120 × 2,25 + 80 × 1,0)/200 = 350/200 = 1,75 (mil reais)².

> 💡 **Exemplo próprio:** grupo A com 30 elementos, média 10 e variância 4; grupo B com 20 elementos, média 10 e variância 9. Variância total = (30 × 4 + 20 × 9)/50 = 6; desvio padrão ≈ 2,45; CV ≈ 24,5% (dispersão média). Esse atalho **só vale com médias iguais**.

**2. Descobrir tamanhos de grupos pela média ponderada, depois calcular o CV.** Monta-se um sistema: F1 + F2 = total, e média geral = (m1 × F1 + m2 × F2)/total. Com o tamanho encontrado, obtêm-se a variância dada e o desvio padrão (raiz da variância), e o CV é o desvio padrão dividido pela média do grupo. No exemplo do trecho: 40 funcionários, médias 8 (mulheres) e 10 (homens), média geral 8,6, o que dá 12 homens; variância dos homens = 12 + 4 = 16, desvio padrão 4, CV = 4/10 = 40%.

**3. Usar a soma dos quadrados.** Quando a questão informa o CV e a soma dos quadrados dos valores, combine duas relações: CV = σ/média e variância = (média dos quadrados) − (média)². No exemplo do trecho (censo de 320 salários, CV = 16%, soma dos quadrados 8.204,80): média dos quadrados = 25,64; com média = σ/0,16, resulta σ² = 0,64 e σ = 0,8 S.M.

Há um atalho que decorre dessas mesmas relações: **média dos quadrados = média² × (1 + CV²)**. Com CV = 16% = 0,16: média dos quadrados = média² × 1,0256, daí média² = 25,64/1,0256 = 25 (média = 5) e σ = 0,16 × 5 = 0,8. Chega-se ao mesmo resultado sem montar a equação.

**4. Alterar o conjunto e recalcular.** Veja a variância relativa abaixo.

### Variância relativa

A **variância relativa** é o quociente entre a variância e o **quadrado da média**; equivale ao **quadrado do CV** (sem a multiplicação por 100):

| Caso | Fórmula |
| --- | --- |
| População | VR = (σ/μ)² = σ²/μ² |
| Amostra | VR = (s/x̄)² = s²/x̄² |

Também é **adimensional**: o numerador (variância) e o denominador (quadrado da média) estão na mesma unidade ao quadrado, que se cancela na divisão.

> 💡 **Exemplo do trecho:** com os mesmos salários (homens: 810/1.800 = 0,45; mulheres: 705/1.500 = 0,47), VR dos homens = 0,45² ≈ 0,20 e das mulheres = 0,47² ≈ 0,22. A variância relativa das mulheres é maior, conclusão igual à do CV.

> ⚠️ **Pegadinha:** o CV vem em porcentagem; a VR vem em número decimal, sem porcentagem. Um CV de 30% corresponde a VR = 0,09, e não 0,30 nem 9%. Para passar de uma para outra, eleve ao quadrado (CV → VR) ou extraia a raiz (VR → CV).

#### Questão de alteração do conjunto (o método dos somatórios)

Quando o enunciado retira ou inclui elementos, trabalhe com **somas**: guarde Σx (soma) e Σx² (soma dos quadrados), atualize-as com o que sai ou entra e recalcule as médias.

> 💡 **Exemplo do trecho, em resumo:** população de 20 elementos com média 20 e CV de 30% (o enunciado o chama de coeficiente de variação de Pearson, que é o mesmo CV). Então σ = 6 e a variância é 36; média dos quadrados = 36 + 400 = 436; Σx = 400 e Σx² = 8.720. Retirando dois elementos iguais a 11: Σx = 378 e Σx² = 8.478, com 18 elementos. Nova média = 21, nova média dos quadrados = 471, nova variância = 471 − 441 = 30, e a variância relativa vale 30/441 = 10/147.

### Para fixar
- O CV divide o desvio padrão pela média e se expressa em %; é adimensional e permite comparar séries de unidades ou médias diferentes.
- Interpretação: CV < 15% baixa dispersão; entre 15% e 30% média; acima de 30% elevada. Homogênea: CV < 30%; heterogênea: CV > 30%.
- Menor CV significa dados mais homogêneos; o CV não muda quando todos os dados são multiplicados por uma constante positiva, mas muda se for somada uma constante.
- A variância relativa é a variância dividida pelo quadrado da média, ou seja, o quadrado do CV, em número decimal.
- Para variância de dois grupos com a mesma média, faça a média ponderada das variâncias pelos tamanhos.
- Em questões com CV e soma dos quadrados, use média dos quadrados = média² × (1 + CV²) ou a variância = média dos quadrados − média².
- Ao retirar ou incluir elementos, atualize a soma e a soma dos quadrados antes de recalcular média e variância.

# SINTÉTICO

- **Dispersão relativa**: o desvio padrão só compara séries na mesma unidade e com médias parecidas; para unidades ou médias distintas, use medida relativa.
- **Coeficiente de variação**: CV = desvio padrão / média × 100 (%), com σ/μ na população e s/x̄ na amostra; é adimensional.
- **Classificação**: CV < 15% baixa dispersão; 15% a 30% média; > 30% elevada. Homogênea se CV < 30%, heterogênea se maior.
- **Leitura**: menor CV significa dados mais homogêneos; no exemplo, CV de 45% (homens) e 47% (mulheres) indicam dispersão elevada nos dois grupos, maior para elas.
- **Variância relativa**: VR = variância / média² = (CV)² (em decimal); também adimensional. Com CV de 30%, VR = 0,09.
- **Do CV ao desvio**: desvio padrão = CV × média; a variância é o quadrado dele.
- **Dois grupos com a mesma média**: a variância total é a média ponderada das variâncias pelos tamanhos (120 × 2,25 e 80 × 1,0 dão 1,75).
- **Soma dos quadrados**: variância = média dos quadrados − média²; combinada com o CV, resolve questões de censo (CV de 16%, 320 dados, soma dos quadrados 8.204,80: σ = 0,8).
- **Retirar elementos**: atualize Σx e Σx², recalcule média e variância; depois VR = variância / média².

# NOTAS

Páginas 62-72 legíveis; fórmulas recompostas pelo contexto e valores numéricos refeitos e conferidos. Observações: (1) o texto-fonte diz que o desvio padrão compara séries com "a mesma média"; adotei a leitura "médias semelhantes e mesma unidade". (2) As faixas de CV (15% e 30%) são tratadas na fonte com sinais estritos; o que ocorre exatamente em 15% ou 30% não é definido, e não afirmei. (3) A observação de que o CV perde o sentido com média próxima de zero e a invariância do CV à multiplicação por constante são consequências matemáticas diretas das definições e não constam no trecho. (4) O atalho média dos quadrados = média² × (1 + CV²) é dedução própria a partir de variância = média dos quadrados − média². (5) Aproximadamente metade do trecho é de questões comentadas; os métodos foram extraídos delas.
