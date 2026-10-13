---
id: S0565
agente: CLAUDE-L4
materia: Estatística
aula: Aula 13 — Regressão Linear Múltipla
trecho: estatistica/a13/s03
paginas_lidas: 30-33
---
# ANALÍTICO

O problema da especificação é o risco de montar o modelo de regressão de forma inadequada: escolher a forma matemática errada ou incluir variáveis explicativas a mais ou a menos. O trecho mostra os dois lados do problema e quais são as consequências para as estimativas dos coeficientes.

### O que é especificar o modelo

Especificar é definir **qual função matemática** relaciona a variável dependente Y às independentes e **quais variáveis** entram nela. Com mais de uma variável independente (regressão múltipla), a escolha fica mais delicada, e um modelo mal especificado produz uma análise que não corresponde à realidade.

A escolha da forma funcional costuma vir de **conhecimento prévio** sobre o fenômeno ou da **análise gráfica** dos dados (diagrama de dispersão). Algumas formas usuais, com α e β como parâmetros:

| Forma | Equação |
| --- | --- |
| Linear | Y = α + β·X |
| Potência | Y = α·X^β |
| Exponencial | Y = α·β^X |
| Logarítmica | Y = α + β·log(X) |
| Polinomial (quadrática) | Y = α + β·X + γ·X² |

Ajustar uma reta a dados que seguem uma curva é um erro de especificação, do mesmo modo que incluir ou retirar indevidamente um logaritmo ou uma função exponencial.

### Omitir variável importante (subespecificação)

Suponha que o modelo verdadeiro seja Y = β1·x1 + β2·x2 + β3·x3 + erro, mas o pesquisador estima só com x1 e x2, esquecendo x3. Os valores esperados dos estimadores deixam de coincidir com os parâmetros verdadeiros:

- E(b1) = β1 + θ1·β3
- E(b2) = β2 + θ2·β3

Ou seja, parte do efeito da variável omitida (β3) é "atribuída" aos coeficientes das variáveis incluídas, através da relação (θ) entre elas. Os estimadores ficam **tendenciosos** (viesados): não acertam o parâmetro, nem em média.

> 💡 **Exemplo próprio:** para explicar o preço de imóveis, um analista usa só a área e o número de quartos, esquecendo o bairro. Como bairro e área costumam estar relacionados, o coeficiente da área passa a captar também o efeito do bairro, e a estimativa fica errada.

O mesmo vale para o termo quadrático omitido: se o modelo correto para o salário médio (em logaritmo) tem conhecimento, tempo no cargo e experiência ao quadrado, tirar a experiência² a joga para o termo de erro. Se esse fator tem relação com as outras variáveis, **todos** os coeficientes restantes (inclusive o intercepto) ficam viesados. A correção é **incluir** o fator omitido.

### Incluir variável desnecessária (superespecificação)

Agora o modelo verdadeiro é Y = β1·x1 + β2·x2 + erro, mas se estima com x3 a mais. Nesse caso:

- E(b1) = β1 e E(b2) = β2 (continuam **não tendenciosos**);
- E(b3) = 0 (o coeficiente da variável inútil tende a zero).

Logo, incluir variável desnecessária **não gera viés**. Porém, tem um custo: geralmente a **variância dos estimadores aumenta**, isto é, as estimativas ficam menos precisas.

| Situação | Viés dos estimadores | Variância |
| --- | --- | --- |
| Omitir variável relevante | **tendenciosos** | — |
| Incluir variável desnecessária | não tendenciosos | geralmente **maior** |

> ⚠️ **Pegadinha:** a conclusão é que é preferível incluir uma variável a mais do que deixar de fora uma significativa, mas **incluir sem necessidade não é gratuito** (perde-se precisão). As duas frases costumam aparecer juntas na prova, e a banca troca "tendenciosos" por "não tendenciosos".

### Outras causas do problema

Omissão de variável relevante não é a única fonte de erro de especificação. A **forma funcional errada** (linear no lugar de logarítmica, por exemplo) também compromete o modelo. A importância prática: é preciso conhecer quais variáveis são essenciais antes de ajustar, porque uma especificação incorreta leva a conclusões incompatíveis com a realidade.

### Para fixar
- Problema da especificação: escolher forma funcional e conjunto de variáveis do modelo de regressão.
- A forma é escolhida por conhecimento prévio ou análise gráfica; há formas linear, potência, exponencial, logarítmica e polinomial.
- Omitir variável importante: estimadores tendenciosos (E(b1) = β1 + θ1·β3).
- Incluir variável desnecessária: estimadores continuam não tendenciosos, e o coeficiente extra tende a 0.
- Mas incluir variável sem necessidade geralmente aumenta a variância dos estimadores.
- Forma funcional errada (log, exponencial, termo quadrático) também é erro de especificação.
- Corrige-se incluindo a variável omitida.

# SINTÉTICO

- **Especificação**: é a escolha da forma funcional e das variáveis do modelo de regressão; erro nela leva a conclusões distantes da realidade.
- **Forma funcional**: decidida por conhecimento prévio ou análise gráfica; exemplos: linear, potência, exponencial, logarítmica e polinomial.
- **Variável importante omitida**: os estimadores ficam tendenciosos, pois E(b1) = β1 + θ1·β3, com parte do efeito omitido contaminando os incluídos.
- **Variável desnecessária incluída**: os estimadores permanecem não tendenciosos (E(b1) = β1) e o coeficiente da inútil tem esperança zero.
- **Custo da inclusão desnecessária**: a variância dos estimadores geralmente aumenta, reduzindo a precisão.
- **Regra prática**: é melhor incluir uma variável a mais do que omitir uma significativa, mas nenhuma das duas é ideal.
- **Termo omitido (ex.: quadrático)**: se tem relação com as demais variáveis, todos os coeficientes ficam viesados; corrige-se incluindo o termo.
- **Outros erros**: usar ou não usar logaritmo ou função exponencial, no lugar certo, também é questão de especificação.

# NOTAS

Páginas 30 e 31 trazem gráficos de ajuste (R² de modelos linear, potência, exponencial, logarítmico e polinomial) usados só como ilustração e descartados; o resumo lista as equações. Acrescentado fora do trecho: os termos θ1 e θ2 representam a relação entre a variável omitida e as incluídas (o material não os define), e os nomes subespecificação e superespecificação para omissão e inclusão desnecessária (o material só usa "subespecificado" para o modelo com omissão). O texto não detalha as condições em que não há viés; por isso não foram incluídas.
