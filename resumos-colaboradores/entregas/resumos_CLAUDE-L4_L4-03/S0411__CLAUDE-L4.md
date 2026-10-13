---
id: S0411
agente: CLAUDE-L4
materia: Estatística
aula: Aula 07 — Variáveis Aleatórias Discretas
trecho: estatistica/a07/s05
paginas_lidas: 54-70
---
# ANALÍTICO

Este trecho fecha o estudo da variância de variáveis aleatórias com suas propriedades (efeito de somar, multiplicar e combinar variáveis) e introduz as medidas que descrevem a relação entre duas variáveis: a covariância e o coeficiente de correlação.

### Propriedades da variância e do desvio padrão

Valem para variáveis discretas e contínuas. Sejam X e Y variáveis aleatórias e k uma constante real.

| Propriedade | Variância | Desvio padrão |
| --- | --- | --- |
| Somar ou subtrair constante | V(X ± k) = V(X) | D(X ± k) = D(X) |
| Multiplicar por constante | V(k·X) = k² · V(X) | D(k·X) = abs(k) · D(X) |
| Dividir por constante | V(X/k) = V(X) / k² | D(X/k) = D(X) / abs(k) |
| Constante | V(k) = 0 | D(k) = 0 |

**Por que somar constante não muda a variância:** a média também ganha k, então cada desvio (valor menos média) fica igual. Deslocar os dados não os deixa mais espalhados.

**Por que o k aparece ao quadrado:** multiplicando por k, a média é multiplicada por k e os desvios também; como a variância eleva os desvios ao quadrado, o fator vira k². O sinal de k não importa na variância (o quadrado é positivo); no desvio padrão aparece o **módulo** (valor absoluto, abs(k)), porque a raiz de k² é abs(k). Assim, D(−3X) = 3 · D(X), e nunca um valor negativo.

**Constante:** não varia, logo a média é a própria constante e todo desvio é zero.

> 💡 **Exemplo:** se V(X) = 9 (D = 3), então V(X + 10) = 9; V(−2X) = 4 × 9 = 36 e D(−2X) = 6; V(3X − 5) = 9 × 9 = 81 (o −5 não conta, e o 3 entra ao quadrado). Resumo: Y = a + bX tem V(Y) = b² · V(X).

#### Soma e diferença de variáveis

**Se X e Y são independentes**, a variância da soma é a soma das variâncias, e o mesmo vale para a **diferença**:

Para as duas operações, a variância resultante é **V(X) + V(Y)**.

Nunca se subtraem as variâncias: a diferença também aumenta a variabilidade.

> 💡 **Exemplo:** X e Y independentes com V(X) = 4 e V(Y) = 9. Então a variância de X + Y e a de X − Y valem, ambas, 13. O desvio padrão de X + Y é √13 ≈ 3,6, e **não** 2 + 3 = 5: o desvio padrão não é aditivo.

> ⚠️ **Pegadinha:** a propriedade aditiva exige **independência**. Se o enunciado não afirmar (ou não permitir concluir) que X e Y são independentes, não se pode somar as variâncias. A recíproca também é falsa: pode ocorrer V(X + Y) = V(X) + V(Y) sem que as variáveis sejam independentes.

Outras armadilhas frequentes: V(X) = E(X²) − [E(X)]² é **menor** que E(X²) sempre que a média não for zero (e igual a ele se a média for zero)
; e "Var(a·X) = a · Var(X)" está errado, o correto é a² · Var(X).

### Covariância

Quando duas variáveis se relacionam (uma influencia a outra), é útil medir **a direção e a força** dessa relação. A **covariância** mede como X e Y variam juntas:

**Cov(X, Y) = E[(X − μX) · (Y − μY)] = E(X·Y) − E(X) · E(Y)**

O termo E(X·Y) é a média dos produtos x·y (ponderados pelas probabilidades). Com valores igualmente prováveis, E(X·Y) = Σ(x·y) / N.

> 💡 **Exemplo:** pares (x, y): (1, 2), (2, 4), (3, 5), (4, 9), todos igualmente prováveis. Σxy = 2 + 8 + 15 + 36 = 61, logo E(XY) = 15,25. E(X) = 10/4 = 2,5 e E(Y) = 20/4 = 5. Então Cov = 15,25 − 2,5 × 5 = **2,75**.

Roteiro: multiplique x por y em cada par; divida a soma por N; calcule as duas médias e multiplique-as; subtraia.

**Sinal da covariância:**
- **positiva**: as variáveis variam no mesmo sentido (quando uma sobe, a outra tende a subir);
- **negativa**: sentidos opostos (preço e quantidade comprada, por exemplo);
- **zero**: sem relação linear.

**Covariância amostral:** ao estimar a partir de uma amostra, divide-se a soma dos produtos dos desvios por n − 1, em vez de n. Basta multiplicar a covariância populacional por n/(n − 1). No exemplo, 2,75 × 4/3 ≈ 3,67.

### Coeficiente de correlação

A covariância depende das unidades e da escala, e por isso o valor sozinho é difícil de interpretar (2,75 é forte ou fraca?). A correlação resolve isso dividindo pela escala de cada variável:

**ρ(X, Y) = Cov(X, Y) / (σX · σY)**

Equivalente, para dados observados: ρ = [Σxy − n·x̄·ȳ] / [√(Σx² − n·x̄²) · √(Σy² − n·ȳ²)]. A correlação não tem unidade e sempre fica no intervalo **[−1, 1]**; o sinal é o da covariância.

> 💡 **Exemplo (continuando):** E(X²) = 30/4 = 7,5, então V(X) = 7,5 − 2,5² = 1,25 e σX ≈ 1,12. E(Y²) = 126/4 = 31,5, então V(Y) = 31,5 − 25 = 6,5 e σY ≈ 2,55. Logo ρ = 2,75 / (1,12 × 2,55) ≈ **0,96**: relação positiva muito forte.

Interpretação:

| Valor de ρ | Significado |
| --- | --- |
| ρ = 1 | correlação linear perfeita positiva: Y = aX + b, com a > 0 |
| ρ = −1 | correlação linear perfeita negativa: Y = aX + b, com a < 0 |
| próximo de ±1 | relação linear forte |
| próximo de 0 | relação linear fraca |
| ρ = 0 | ausência de relação linear |

Itens que dizem "coeficiente menor que −1" ou "maior que 1" estão errados. A correlação mede apenas a relação **linear**.

#### Independência, covariância e correlação

Se X e Y são independentes, então E(X·Y) = E(X)·E(Y), e portanto **Cov = 0 e ρ = 0**. A volta **não vale**: covariância zero não garante independência.

> 💡 **Exemplo:** X toma −1, 0 e 1 com probabilidade 1/3 cada, e Y = X². Então E(X) = 0 e E(XY) = E(X³) = 0, logo Cov = 0; mas Y é totalmente determinada por X, portanto são dependentes.

**Exceção importante:** para variáveis **binárias** (que assumem só dois valores), covariância nula **implica** independência.

### Para fixar

- V(X ± k) = V(X); V(kX) = k² V(X); D(kX) = abs(k) · D(X); a variância e o desvio de uma constante valem zero.
- Variância da soma e da diferença: V(X) + V(Y), só com variáveis independentes; o desvio padrão não é aditivo.
- Cov(X, Y) = E(XY) − E(X)E(Y); positiva = mesmo sentido, negativa = sentidos opostos.
- Covariância amostral: divisor n − 1 (equivale a multiplicar a populacional por n/(n − 1)).
- ρ = Cov / (σX σY), sempre entre −1 e 1; ±1 indica relação linear perfeita (sinal igual ao de a em Y = aX + b).
- Independência implica Cov = 0 e ρ = 0, mas o contrário falha, exceto para variáveis binárias.
- A correlação mede só relação linear e não tem unidade.

# SINTÉTICO

- **Somar constante**: V(X ± k) = V(X) e D(X ± k) = D(X), pois média e valores se deslocam juntos.
- **Multiplicar constante**: V(kX) = k² V(X) e D(kX) = abs(k) · D(X); dividir segue a mesma lógica; o sinal de k não altera a variância.
- **Constante**: a variância e o desvio padrão de uma constante valem zero.
- **Soma e diferença**: com X e Y independentes, a variância da soma e a da diferença são ambas V(X) + V(Y); o desvio
 padrão não é aditivo, e sem independência a regra não vale.
- **Covariância**: Cov(X, Y) = E(XY) − E(X)·E(Y); positiva = mesmo sentido, negativa = sentidos opostos; a amostral usa divisor n − 1.
- **Correlação**: ρ = Cov / (σX · σY), sem unidade e restrita a [−1, 1]; mede só a relação linear.
- **Casos extremos**: ρ = 1 indica Y = aX + b com a > 0; ρ = −1, com a < 0; ρ próximo de zero, relação linear fraca.
- **Independência**: implica Cov = 0 e ρ = 0, mas Cov = 0 não implica independência, exceto para variáveis binárias.

# NOTAS

- As páginas 54 a 60 e 67 a 70 incluem questões comentadas; só a teoria foi aproveitada. Os gráficos de dispersão (altura dos pais × filhos; preço × quantidade) são ilustrações, foram descartados; os exemplos numéricos são próprios.
- Extração: a fórmula do desvio padrão da pág. 65 e várias expressões das páginas 54 a 57 vieram embaralhadas (símbolos fora de ordem); conferidas pela álgebra. Na pág. 70 o texto escreve a covariância como "≅ 25,7" e depois usa −25,7; o sinal correto é negativo (−180/7).
- Acrescentados por conhecimento padrão (não constam no trecho): a observação de que a correlação não tem unidade e mede só a relação linear, e o exemplo de covariância nula com dependência (Y = X²). A relação geral V(X ± Y) com covariância não foi incluída, por não constar do trecho.
- O item sobre Var(X) < E(X²) vale quando E(X) ≠ 0 (se E(X) = 0, são iguais); a questão original assume a desigualdade estrita.
