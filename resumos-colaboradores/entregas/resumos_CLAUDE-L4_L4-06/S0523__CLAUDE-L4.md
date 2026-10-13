---
id: S0523
agente: CLAUDE-L4
materia: Estatística
aula: Aula 07 — Variáveis Aleatórias Discretas
trecho: estatistica/a07/s02
paginas_lidas: 17-26
---
# ANALÍTICO

As medidas de tendência central (esperança, moda e mediana) resumem a posição central de uma variável aleatória. Este trecho desenvolve a **esperança matemática** (valor esperado ou média): como calculá-la na variável discreta, como usá-la em problemas de decisão e as cinco propriedades que simplificam as contas.

### Esperança matemática: ideia e cálculo

A esperança é o **valor médio** da variável, também chamada de expectância, valor esperado ou média. Indica-se por **E(X)** ou **μX**. Ela representa o que se "espera" obter em média, como o tempo médio de deslocamento de alguém que faz o mesmo trajeto todos os dias.

- Quando os resultados são **equiprováveis**, a esperança é a média aritmética dos valores. Moeda com faces 0 e 1: E = 0,5. Dado de seis faces: soma de 1 a 6 dividida por 6, que dá 21/6 = **3,5**.
- No caso geral, para qualquer variável discreta: **E(X) = Σ x · P(X = x)**, isto é, multiplica-se cada valor pela sua probabilidade e somam-se os produtos.

Na tabela de distribuição, cria-se uma coluna extra com o produto x·P(x); a esperança é a **soma dessa coluna**. A soma das probabilidades da tabela deve ser 1.

> ⚠️ **Pegadinha:** a esperança não precisa ser um valor que a variável realmente assuma (3,5 não sai em nenhuma face do dado). E, se houver valores negativos (prejuízo), o produto fica negativo e entra na soma com o sinal.

### Esperança em problemas de decisão

Tipos frequentes de questão:

1. **Ganho ou perda esperada**: multiplica-se cada resultado (positivo ou negativo) pela probabilidade e soma-se. A probabilidade do segundo resultado, quando só há dois, é a **complementar** (1 − p).

> 💡 **Exemplo próprio:** um jogo paga R$ 90 com probabilidade 0,2 e custa R$ 20 (valor −20) com probabilidade 0,8. E = 90·0,2 + (−20)·0,8 = 18 − 16 = **R$ 2** de ganho esperado.

2. **Escolha da melhor estratégia**: dada uma tabela com cenários (cada um com sua probabilidade) e o resultado de cada estratégia em cada cenário, calcula-se a esperança de cada estratégia e escolhe-se a **maior** (ou a menor, se for custo).

> 💡 **Exemplo próprio:** cenários A (40%), B (60%). Estratégia 1 rende 100 em A e 50 em B: E = 40 + 30 = 70. Estratégia 2 rende 80 em A e 70 em B: E = 32 + 42 = 74. A estratégia 2 é preferível.

3. **Estimativa de totais**: se a esperança por unidade é E, em n unidades espera-se **n · E**. Exemplo próprio: se cada cliente compra, em média, 2,4 itens, 500 clientes devem levar cerca de 1.200 itens.

4. **Incógnita na tabela**: usa-se que a soma das probabilidades é 1 para achar o valor faltante e só depois calcula-se E(X) = Σ x·P(x).

5. **Variáveis simétricas**: se uma variável assume j e −j com probabilidade 1/2 cada, E = −j/2 + j/2 = **0**, para qualquer j.

### Propriedades da esperança

Valem também para variáveis **contínuas**. Sejam X e Y variáveis aleatórias e k uma constante real:

| Propriedade | Significado |
| --- | --- |
| E(k·X) = k·E(X) | multiplicar a variável por k multiplica a média por k |
| E(X ± k) = E(X) ± k | somar ou subtrair uma constante muda a média no mesmo valor |
| E(X ± Y) = E(X) ± E(Y) | esperança da soma (ou diferença) é a soma (ou diferença) das esperanças |
| E(k) = k | a esperança de uma constante é ela própria |
| E(X · Y) = E(X) · E(Y), se X e Y forem independentes | esperança do produto é o produto das esperanças |

Detalhes que a banca explora:

- **Divisão** é o mesmo que multiplicar por 1/k: E(X/k) = E(X)/k. A **subtração** de constante é soma de −k.
- **Exemplo de intuição:** se todos os salários de um grupo dobram, a média dobra; se todos recebem um aumento fixo, a média sobe esse mesmo valor. Somar uma constante apenas **desloca** a média; multiplicar por uma constante **reescala** a média.
- A propriedade da soma vale para **qualquer número de variáveis**, com os sinais que cada uma tiver: E(X1 + X2 − X3) = E(X1) + E(X2) − E(X3). (Ela não exige independência, pois é regra geral da esperança; acréscimo fora do trecho.)
- A propriedade do **produto** exige **independência** e se estende a qualquer quantidade de variáveis independentes. Ela **não é de "ida e volta"**: independentes implica E(XY) = E(X)·E(Y), mas encontrar E(XY) = E(X)·E(Y) **não prova** independência.
- Para a soma de duas moedas (0 ou 1), E(X1 + X2) = 1/2 + 1/2 = 1; para o produto, E(X1·X2) = 1/4 = (1/2)·(1/2).

As propriedades se combinam:

**E(3·X + Y/4 − 2·Z + 1) = 3·E(X) + E(Y)/4 − 2·E(Z) + 1**

> 💡 **Exemplo próprio:** com E(X) = 4, E(Y) = 8 e E(Z) = 1: 3·4 + 8/4 − 2·1 + 1 = 12 + 2 − 2 + 1 = **13**.

> 💡 **Questão-tipo:** sendo Y = a + b·X e E(X) = μ, então E(Y) = a + b·μ (a constante a sai somando; b multiplica a média). Alternativas que somam a + b ou deixam só a ou só b·μ estão erradas.

> ⚠️ **Pegadinha:** não confunda E(X²) com [E(X)]², nem E(X·Y) com E(X)·E(Y) sem independência. O trecho só autoriza a fatoração do produto quando há independência.

### Para fixar
- Esperança = média ponderada: E(X) = Σ x·P(X = x); com resultados equiprováveis, é a média aritmética.
- A soma das probabilidades da tabela é 1; use isso para achar valores faltantes.
- Em decisão, calcule E de cada alternativa (com sinais) e escolha o maior valor esperado.
- E(kX) = k·E(X); E(X ± k) = E(X) ± k; E(k) = k.
- E(X ± Y) = E(X) ± E(Y), em qualquer quantidade de variáveis.
- E(XY) = E(X)·E(Y) se X e Y forem independentes; a volta não vale.
- As propriedades valem para variáveis discretas e contínuas.

# SINTÉTICO

- **Medidas de tendência central**: esperança, moda e mediana resumem a posição central da variável aleatória; este trecho trata da esperança.
- **Esperança (valor esperado ou média)**: E(X) = Σ x·P(X = x), cada valor multiplicado pela sua probabilidade e os produtos somados (na tabela, coluna extra x·P(x)).
- **Equiprováveis**: a esperança é a média aritmética (moeda 0/1: 0,5; dado de seis faces: 3,5).
- **Decisão**: o ganho ou a perda esperados somam valor × probabilidade com sinal; a estratégia ótima é a de maior esperança.
- **Incógnita**: a soma das probabilidades é 1, o que permite achar o valor faltante antes de calcular E(X).
- **Multiplicação por constante**: E(kX) = k·E(X); dividir por k equivale a multiplicar por 1/k, e a média é multiplicada ou dividida junto.
- **Soma de constante**: E(X ± k) = E(X) ± k; a constante desloca a média, mas não é multiplicada.
- **Soma e diferença de variáveis**: E(X ± Y) = E(X) ± E(Y), para qualquer número de variáveis.
- **Constante**: E(k) = k, pois uma variável que sempre vale k tem média k (n·k/n = k).
- **Produto**: E(XY) = E(X)·E(Y) só se X e Y forem independentes; a recíproca é falsa (a igualdade não prova independência).
- **Combinação**: E(aX + bY + c) = a·E(X) + b·E(Y) + c; valem também para contínuas.

# NOTAS

- A tabela de cenários e estratégias e as distribuições das questões vieram como imagem; reconstruí o raciocínio a partir dos cálculos escritos, sem reproduzir os dados. Os resultados conferidos: ganho esperado de R$ 500 (4.000×0,3 − 1.000×0,7), 3,15 pessoas por carro (1.260 em 400), K = 1/2 e E(X) = 9/4, E(Yj) = 0.
- Pág. 22 do material: no exemplo de Y2 aparece "P(Y1 = −2)" por erro de digitação (deveria ser Y2). Pág. 23: o cálculo da esperança de Y está rotulado como E(X). Não afeta o resultado.
- O trecho cita três medidas (esperança, moda, mediana) na abertura, mas só desenvolve a esperança; moda e mediana estão no trecho seguinte.
- Acrescentado fora do trecho: a observação de que E(X ± Y) = E(X) ± E(Y) não exige independência (regra geral e bem conhecida). Os exemplos numéricos "próprios" são do autor do resumo.
