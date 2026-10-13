---
id: S0365
agente: CLAUDE-L4
materia: Estatística
aula: Aula 09 — Variáveis Aleatórias Contínuas
trecho: estatistica/a09/s03
paginas_lidas: 28-41
---
# ANALÍTICO

Este trecho leva para as variáveis contínuas as medidas que já existem para as discretas: esperança matemática, variância e desvio padrão, covariância e correlação. A ideia central é uma só: onde havia soma sobre valores possíveis, passa a haver integral ao longo da função densidade de probabilidade (f.d.p.).

### Esperança matemática

No caso discreto, E(X) = Σ x · P(X = x). Como os valores de uma variável contínua não podem ser contados um a um, a soma é trocada por integral e a probabilidade pontual pela f.d.p.:

- E(X) = ∫ x · f(x) dx, calculada no intervalo em que a densidade existe (em tese, de −∞ a +∞; na prática, de xI a xS, onde f é diferente de zero).
- Quando a densidade é definida por **partes** (uma expressão num intervalo, outra em outro), calcula-se uma integral para cada intervalo e somam-se os resultados.

> 💡 **Exemplo:** seja f(x) = 3x² para 0 < x < 1. Primeiro confira que a área total vale 1 (a integral de 3x² dá x³, que vai de 0 a 1). Depois, E(X) = ∫ x · 3x² dx = ∫ 3x³ dx = 3x⁴/4, de 0 a 1, ou seja, **3/4**.

Um truque frequente: se a f.d.p. traz uma constante desconhecida (como k), ela é achada impondo que a integral de f em todo o intervalo seja igual a 1 (probabilidade do espaço amostral inteiro). Se o gráfico for uma reta que forma um triângulo, pode-se igualar a área do triângulo (base × altura ÷ 2) a 1, o que dispensa a integral.

As propriedades da esperança são as mesmas do caso discreto:

| Propriedade | Condição |
| --- | --- |
| E(X + Y) = E(X) + E(Y) | sempre |
| E(X − Y) = E(X) − E(Y) | sempre |
| E(X · Y) = E(X) · E(Y) | só se X e Y forem independentes |
| E(k · X) = k · E(X) | k constante |
| E(k) = k | k constante |

Combinando-as, uma transformação linear se resolve sem refazer integral: se E(V) = 4/3, então E(2V + 10) = 2 · 4/3 + 10 ≈ 12,67. Num problema em que V está em milhares de reais, o resultado também está em milhares de reais.

> ⚠️ **Pegadinha:** a esperança de um produto só se separa nos fatores quando há independência; a de uma soma ou diferença se separa sempre.

### Simetria: atalho para a média

Se a distribuição é **simétrica e unimodal** (um só pico), então **média = mediana = moda**, e esse valor é o centro de simetria. Isso permite achar a média sem integrar.

- Parábola com concavidade para baixo: o pico é o ponto médio entre as duas raízes. Ex.: f(x) = (3/4)(1 − x²) em (−1, 1) tem raízes −1 e 1; logo média = mediana = moda = 0.
- Parábola com concavidade para cima (por exemplo, um "U" simétrico): continua simétrica, e média e mediana coincidem com o ponto central entre as raízes, embora existam duas modas nas extremidades.
- Densidade triangular (sobe como x de 0 a 1 e desce como 2 − x de 1 a 2): simétrica em torno de 1, e a integração por partes confirma E(X) = 1/3 + 2/3 = 1.

> ⚠️ **Pegadinha:** o atalho só vale se o **intervalo** também for simétrico em torno do ponto encontrado. Para f(x) = 3x² em (0, 1) a raiz é x = 0, mas a densidade vai de 0 a 1 e cresce até o fim: não é simétrica em torno de 0, e a média (3/4) é outra.

### Ferramentas de cálculo que aparecem nas questões

- **Regra da cadeia:** a derivada de g(f(x)) é g'(f(x)) · f'(x). Assim, a derivada de e^(t·x) em relação a x é t · e^(t·x). Ao integrar, divide-se por t: a integral de e^(t·x) dx é e^(t·x)/t.
- **Regra de L'Hôpital:** diante de indeterminação do tipo 0/0 ou ∞/∞ num limite, derivam-se numerador e denominador separadamente e recalcula-se o limite. Ex.: o limite de x²/e^x quando x → ∞ vira 2x/e^x, depois 2/e^x, que tende a 0.
- Moda de uma f.d.p. = valor de x em que a derivada da densidade se anula (o gráfico para de subir e começa a descer). A moda de uma mistura de duas normais (combinação ponderada) em geral **não coincide** com nenhuma das modas das componentes, porque a derivada da mistura soma as derivadas das duas, e uma delas não é nula no pico da outra.

### Variância

Para qualquer variável, discreta ou contínua: **V(X) = E(X²) − [E(X)]²**.

- Discreta: E(X²) = Σ x² · P(X = x).
- Contínua: E(X²) = ∫ x² · f(x) dx.
- E(X²) é o **segundo momento**; a variância é o **segundo momento central** (em torno da média).
- Desvio padrão: σ = raiz quadrada de V(X).

> 💡 **Exemplo:** com f(x) = 3x² em (0, 1), E(X) = 3/4 e E(X²) = ∫ 3x⁴ dx = 3/5. Então V(X) = 3/5 − 9/16 = 48/80 − 45/80 = **3/80**.

Quando a esperança de X é zero (densidade simétrica em torno de 0), a variância é simplesmente E(X²), e não há segundo termo a subtrair. Questões também testam a fórmula com dados prontos: se E(X) = 1 e E(X²) = 4, V(X) = 4 − 1 = 3 (e não 2).

Propriedades, válidas também no caso contínuo:

| Propriedade | Observação |
| --- | --- |
| V(X + k) = V(X) | somar constante só desloca; não altera a dispersão |
| V(k · X) = k² · V(X) | a constante sai ao quadrado |
| V(X / k) = V(X) / k² | caso particular da anterior |
| V(X + Y) = V(X) + V(Y) | **só** se X e Y forem independentes |

Ex.: se V(X) = 3/20, então V(3X) = 9 · 3/20 = 27/20 = 1,35.

> ⚠️ **Pegadinha:** a constante que multiplica a variável sai **elevada ao quadrado** da variância, e a constante que apenas se soma **some**. O desvio padrão de k · X é |k| · σ.

### Covariância e correlação

**Cov(X, Y) = E(X · Y) − E(X) · E(Y)**, vale para discretas e contínuas. A diferença está só no cálculo de E(X · Y):

- Discreto: soma de x · y · P(X = x, Y = y), com a probabilidade **conjunta**.
- Contínuo: **integral dupla** de x · y · f(x, y), com a densidade **conjunta**. Resolve-se primeiro a integral interna (em y) e depois a externa (em x).

Propriedades:

- Simetria: Cov(X, Y) = Cov(Y, X).
- Cov(X, X) = V(X).
- Cov(k, X) = 0 para constante k.
- Soma: Cov(X + Y, Z) = Cov(X, Z) + Cov(Y, Z).
- Constante multiplicando: Cov(kX, Y) = Cov(X, kY) = k · Cov(X, Y).
- Se X e Y são independentes, Cov = 0 (a volta não é verdadeira: covariância nula não garante independência).

Com a covariância, a variância de soma e diferença deixa de exigir independência:

- V(X + Y) = V(X) + V(Y) + 2 · Cov(X, Y)
- V(X − Y) = V(X) + V(Y) − 2 · Cov(X, Y)
- Para várias variáveis: soma das variâncias mais o dobro da soma das covariâncias de cada par (sem repetir pares). Para três variáveis: V(X) + V(Y) + V(Z) + 2 · [Cov(X,Y) + Cov(X,Z) + Cov(Y,Z)].

> 💡 **Exemplo:** V(X) = 4, V(Y) = 9, Cov(X, Y) = 3. Então V(X + Y) = 4 + 9 + 6 = 19 e V(X − Y) = 4 + 9 − 6 = 13.

O **coeficiente de correlação** padroniza a covariância: **ρ(X, Y) = Cov(X, Y) / (σX · σY)**. No exemplo acima, ρ = 3 / (2 · 3) = 0,5. Em outra situação, com variâncias 8 e 2 e covariância 3, ρ = 3 / (raiz de 8 · raiz de 2) = 3 / raiz de 16 = 3/4 = 0,75. Atenção: o denominador usa **desvios padrão**, não variâncias.

### Para fixar
- Contínua: soma vira integral e P(X = x) vira f(x); E(X) = ∫ x · f(x) dx e E(X²) = ∫ x² · f(x) dx.
- Constante desconhecida na f.d.p. se acha impondo que a integral total valha 1.
- Densidade definida por partes: integra-se cada parte e somam-se.
- Simetria + unimodal = média, mediana e moda iguais; o atalho exige intervalo simétrico em torno do centro.
- V(X) = E(X²) − [E(X)]²; V(X + k) = V(X); V(kX) = k² · V(X).
- V(X ± Y) = V(X) + V(Y) ± 2 · Cov(X, Y); sem o termo de covariância só se independentes.
- Cov(X, Y) = E(XY) − E(X)E(Y); independência implica Cov = 0, mas não o inverso.
- ρ = Cov / (σX · σY).

# SINTÉTICO

- **Esperança contínua**: E(X) = ∫ x · f(x) dx; a integral substitui o somatório do caso discreto, e densidades por partes exigem uma integral por trecho, depois somadas.
- **Constante da f.d.p.**: a integral de f em todo o domínio deve valer 1; com reta formando triângulo, área = 1 resolve sem integral.
- **Propriedades da esperança**: soma e diferença sempre se separam; E(XY) = E(X)E(Y) só com independência; E(kX) = kE(X); E(k) = k.
- **Simetria**: densidade simétrica e unimodal tem média = mediana = moda; numa parábola é o ponto médio das raízes, desde que o intervalo seja simétrico em torno dele.
- **Variância**: V(X) = E(X²) − [E(X)]², com E(X²) = ∫ x² · f(x) dx; desvio padrão é a raiz da variância.
- **Transformações**: V(X + k) = V(X) e V(kX) = k² · V(X); somar constante não muda a dispersão, multiplicar eleva a constante ao quadrado.
- **Soma de variâncias**: V(X + Y) = V(X) + V(Y) apenas se independentes; no caso geral soma-se 2 · Cov(X, Y) (e subtrai-se em X − Y).
- **Covariância**: Cov(X, Y) = E(XY) − E(X)E(Y); no contínuo, E(XY) vem de integral dupla da densidade conjunta; Cov(X, X) = V(X) e Cov(k, X) = 0.
- **Correlação**: ρ = Cov(X, Y) / (σX · σY); o denominador usa desvios padrão (ex.: 3 / raiz de 16 = 0,75).
- **Cálculo de apoio**: a derivada de e^(tx) é t · e^(tx) (regra da cadeia); L'Hôpital resolve 0/0 e ∞/∞ derivando numerador e denominador.

# NOTAS

- Pág. 35: no exemplo com f(x) = 9x² em (0, raiz cúbica de 1/3), o texto-fonte mostra E(X²) com coeficiente 9/4 após a integração, mas a primitiva de 9x⁴ é (9/5)x⁵ (o coeficiente correto é 9/5). Erro aparente do material; o resumo não reproduz esse exemplo e usa exemplos próprios.
- Pág. 37: a resolução da questão CESPE/2014 aparece duplicada no texto extraído (sem prejuízo).
- Nos exemplos do material há figuras (gráfico das densidades normais e da mistura, parábolas, triângulo) que não foram extraídas; as conclusões foram aproveitadas a partir do texto que as descreve.
- A frase "covariância nula não implica independência" não consta literalmente no trecho; foi incluída como complemento conceitual padrão da teoria de probabilidade.
