---
id: S0452
agente: CLAUDE-L4
materia: Estatística
aula: Aula 07 — Variáveis Aleatórias Discretas
trecho: estatistica/a07/s06
paginas_lidas: 71-84
---
# ANALÍTICO

Este trecho reúne as propriedades da covariância e da correlação (simetria, constantes, soma e produto por constante), a variância da soma e da diferença de variáveis aleatórias, e o coeficiente de variação com a variância relativa. Em todo o texto, X, Y e Z são variáveis aleatórias e k, l, a, b são constantes reais.

### Propriedades da covariância

Lembrete: Cov(X, Y) = E(XY) − E(X)·E(Y) e ρ(X, Y) = Cov(X, Y) ÷ (σX · σY). As propriedades valem para variáveis discretas e contínuas.

| Propriedade | Efeito na covariância | Efeito na correlação |
| --- | --- | --- |
| Simetria | Cov(X, Y) = Cov(Y, X) | ρ(X, Y) = ρ(Y, X) |
| Mesma variável | Cov(X, X) = Var(X) | ρ(X, X) = 1 |
| Com constante | Cov(k, X) = 0 | ρ(k, X) = 0 |
| Somar ou subtrair constantes | Cov(X ± a, Y ± b) = Cov(X, Y) | ρ(X ± a, Y ± b) = ρ(X, Y) |
| Soma de variáveis | Cov(X ± Y, Z) é a covariância de X com Z, somada ou subtraída da de Y com Z | (não se aplica diretamente) |
| Multiplicar por constantes | Cov(kX, lY) = k·l·Cov(X, Y) | ρ(kX, lY) = ρ(X, Y) se k·l > 0; = −ρ(X, Y) se k·l < 0 |

Por que valem (ideia da dedução):

- **Mesma variável:** E(X·X) − E(X)·E(X) = E(X²) − [E(X)]², que é exatamente a fórmula da variância. Daí ρ(X, X) = Var(X) ÷ σX² = 1.
- **Constante:** E(k·X) = k·E(X) e E(k) = k, então a diferença dá zero. Uma constante não varia, logo não "acompanha" X.
- **Somar constantes:** as parcelas com a e b aparecem nos dois termos da fórmula e se cancelam; mudar o ponto de partida não muda o modo como as variáveis se movem juntas.
- **Multiplicar por constante:** k sai de dentro das esperanças; se as duas variáveis são multiplicadas, aparece o produto das constantes (k² quando a constante é a mesma nas duas).

> 💡 **Exemplo próprio:** Cov(X, Y) = 8. Então Cov(X + 4, Y − 7) = 8; Cov(3X, −2Y) = 3 · (−2) · 8 = −48; Cov(5X, 5Y) = 25 · 8 = 200; Cov(X, Y ÷ 4) = 8 ÷ 4 = 2 (dividir por uma constante é multiplicar pelo inverso).

> 💡 **Soma de variáveis:** se Cov(X, Z) = 2 e Cov(Y, Z) = −5, então Cov(X + Y, Z) = 2 + (−5) = −3 e Cov(X − Y, Z) = 2 − (−5) = 7.

#### Correlação e constantes: o sinal

Na correlação, as constantes só podem **trocar o sinal**: o módulo de ρ não muda quando se multiplicam as variáveis por constantes (diferentes de zero). Usa-se que σ(kX) = |k|·σX, de modo que ρ(kX, lY) = [k·l ÷ |k·l|] · ρ(X, Y). Esse fator vale +1 se k e l têm o mesmo sinal e −1 se têm sinais contrários. Soma de constante não altera nada.

> ⚠️ **Pegadinha:** uma relação linear decrescente exata, como Y = 10 − 3X, tem ρ(X, Y) = −1. A constante 10 não conta; só importa que o coeficiente de X é negativo (k < 0) e que ρ(X, X) = 1. O sinal da correlação segue o sinal do coeficiente de X.

> 💡 **Exemplo próprio:** média de X = 5 e desvio padrão de X = 3, Y = 2 − 4X. Média de Y = 2 − 4 · 5 = −18; Var(Y) = (−4)² · 9 = 144; ρ(X, Y) = −1 (soma de constante não altera, e o coeficiente −4 é negativo).

### Variância da soma e da diferença

No caso geral (sem exigir independência):

- **Var(X + Y) = Var(X) + Var(Y) + 2·Cov(X, Y)**
- **Var(X − Y) = Var(X) + Var(Y) − 2·Cov(X, Y)**

O truque de memória é o quadrado da soma e o quadrado da diferença: o termo do meio é o dobro do produto. Em ambas as fórmulas as variâncias **somam**; só muda o sinal do termo da covariância.

> 💡 **Exemplo próprio:** Var(X) = 9, Var(Y) = 16, Cov(X, Y) = 6. Var(X + Y) = 9 + 16 + 12 = 37. Var(X − Y) = 9 + 16 − 12 = 13.

Se X e Y são **independentes**, Cov(X, Y) = 0 e então Var(X + Y) = Var(X − Y) = Var(X) + Var(Y) (propriedade aditiva da variância). Atenção: covariância zero não garante independência; a ligação é no sentido independência ⇒ covariância zero.

Com constantes (junte as propriedades Var(kX) = k²·Var(X) e Cov(kX, lY) = k·l·Cov(X, Y)):

- **Var(kX + lY) = k²·Var(X) + l²·Var(Y) + 2·k·l·Cov(X, Y)**
- **Var(kX − lY) = k²·Var(X) + l²·Var(Y) − 2·k·l·Cov(X, Y)**

> 💡 **Exemplo próprio:** com os dados anteriores (Var(X) = 9, Var(Y) = 16, Cov = 6): Var(2X − 3Y) = 4 · 9 + 9 · 16 − 2 · 2 · 3 · 6 = 36 + 144 − 72 = 108.

#### Mais de duas variáveis

A variância da soma é a soma das variâncias mais **o dobro da soma das covariâncias de todos os pares distintos**, cada par contado uma só vez (a covariância é simétrica). Com três variáveis:

Var(X + Y + Z) = Var(X) + Var(Y) + Var(Z) + 2·[Cov(Y, Z) + Cov(X, Y) + Cov(X, Z)]

Para n variáveis: Var(ΣXi) = ΣVar(Xi) + 2·ΣΣ Cov(Xi, Xj), somando os pares com j > i. Com todas independentes, sobra só a soma das variâncias.

> 💡 **Exemplo próprio:** Var(X) = 2, Var(Y) = 3, Var(Z) = 4, Cov(X, Y) = 1, Cov(X, Z) = −1 e Cov(Y, Z) = 0,5. Var(X + Y + Z) = 9 + 2 · (1 − 1 + 0,5) = 9 + 1 = 10.

#### Usos típicos em questões

- **Achar a correlação a partir de variâncias:** se Var(X), Var(Y) e Var(X + Y) são dados, isole a covariância em Var(X + Y) = Var(X) + Var(Y) + 2·Cov e depois divida pelo produto dos desvios padrão. Exemplo próprio: Var(X) = 16, Var(Y) = 9 e Var(X + Y) = 19 dão 2·Cov = 19 − 25 = −6, Cov = −3 e ρ = −3 ÷ (4 · 3) = −0,25.
- **Correlação negativa:** então Cov < 0, o que implica Var(X + Y) < Var(X) + Var(Y) (a soma das variâncias é maior que a variância da soma) e E(X·Y) < E(X)·E(Y). A esperança da soma, porém, é sempre E(X) + E(Y), com ou sem correlação. E, em média, quando X cresce Y diminui.

### Coeficiente de variação e variância relativa

O **coeficiente de variação** (conhecido ainda como desvio padrão relativo ou coeficiente de variabilidade) é o desvio padrão dividido pela média:

**CV = σ ÷ μ**

Serve para **comparar a dispersão de variáveis com médias diferentes**. Comparar só os desvios padrão pode enganar, pois um desvio de 20 em torno de uma média 100 é pouco, enquanto um desvio de 5 em torno de 10 é muito. Como σ e μ têm a mesma unidade, o CV é **adimensional** (um número puro, em geral expresso em decimal ou percentual). Pressupõe média diferente de zero.

> 💡 **Exemplo próprio:** turma A com média 50 e desvio padrão 10 (CV = 0,20) e turma B com média 8 e desvio padrão 2 (CV = 0,25). Apesar de o desvio de A ser maior, a dispersão relativa de B é maior.

A **variância relativa** é o quadrado do coeficiente de variação:

**VR = CV² = σ² ÷ μ² = Var(X) ÷ μ²**

Com CV = 0,2, a variância relativa é 0,04.

> ⚠️ **Pegadinha:** um CV de 0,5 significa desvio padrão igual a 50% da média, e não "50% maior" nem "50% menor" que ela. E conhecer só os CVs não permite comparar os desvios padrão absolutos, porque as médias podem não ser conhecidas.

### Para fixar
- Covariância e correlação são simétricas; Cov(X, X) = Var(X) e ρ(X, X) = 1.
- Cov(k, X) = 0, e somar ou subtrair constantes não altera covariância nem correlação.
- Cov(kX, lY) = k·l·Cov(X, Y); a correlação mantém o módulo e troca de sinal apenas se k·l < 0.
- Em Y = c + kX (k ≠ 0), ρ(X, Y) = +1 se k > 0 e −1 se k < 0.
- Var(X ± Y) = Var(X) + Var(Y) ± 2·Cov(X, Y); independentes: Var(X + Y) = Var(X − Y) = Var(X) + Var(Y).
- Var(kX ± lY) = k²·Var(X) + l²·Var(Y) ± 2·k·l·Cov(X, Y); em soma de várias variáveis, cada par de covariância entra uma vez, multiplicado por 2.
- CV = σ ÷ μ (adimensional) compara dispersões de variáveis com médias diferentes; VR = CV².
- Correlação negativa ⇒ Cov < 0 ⇒ Var(X + Y) menor que Var(X) + Var(Y).

# SINTÉTICO

- **Simetria e mesma variável**: Cov(X, Y) = Cov(Y, X), Cov(X, X) = Var(X) e ρ(X, X) = 1.
- **Constantes**: Cov(k, X) = 0, e somar ou subtrair constantes não muda covariância nem correlação.
- **Multiplicação por constantes**: Cov(kX, lY) = k·l·Cov(X, Y); se as duas são multiplicadas pela mesma constante, o fator é k².
- **Sinal da correlação**: o módulo de ρ não muda ao multiplicar por constantes; só troca de sinal quando k·l < 0 (por exemplo, Y = 6 − 2X dá ρ = −1).
- **Variância da soma e da diferença**: Var(X ± Y) = Var(X) + Var(Y) ± 2·Cov(X, Y), análogo ao quadrado da soma e da diferença.
- **Independentes**: Cov = 0, então a variância da soma e a da diferença valem Var(X) + Var(Y).
- **Com constantes e várias variáveis**: Var(kX ± lY) = k²·Var(X) + l²·Var(Y) ± 2·k·l·Cov; para várias variáveis, some as variâncias e o dobro de cada covariância de par.
- **Coeficiente de variação**: CV = σ ÷ μ, adimensional; serve para comparar dispersões quando as médias são diferentes.
- **Variância relativa**: VR = CV² = Var(X) ÷ μ²; por exemplo, CV = 0,2 resulta em VR = 0,04.

# NOTAS

- Página 76 do material: na dedução do coeficiente de correlação com constantes aparecem trechos como "σ(l·X)" e "σX·σX" no denominador, onde o correto seria σ(l·Y) e σX·σY (erro de digitação evidente). O resultado final do material está correto e foi o utilizado.
- A observação de que covariância zero não implica independência é conhecimento geral de estatística, não consta do trecho; incluí por ser a forma segura de cobrar a relação.
- Questões do trecho (Recife/FGV, IBGE, TJ/RO, planejamento e orçamento) foram aproveitadas só pelos métodos; resultados conferidos: média de Y = 2, V(Y) = 16, ρ = −1; correlação −0,5 com V(X) = 25, V(Y) = 16, V(X + Y) = 21.
- Página 84: o símbolo usado para a correlação no enunciado difere do restante do material (δ no lugar de ρ); sem impacto no conteúdo.
