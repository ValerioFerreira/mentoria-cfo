---
id: S0502
agente: CLAUDE-L4
materia: Estatística
aula: Aula 08 — Distribuições Discretas de Probabilidade
trecho: estatistica/a08/s03
paginas_lidas: 33-42
---
# ANALÍTICO

A distribuição geométrica descreve quanto tempo (em tentativas) é preciso esperar até o primeiro sucesso. O trecho traz a fórmula, a média e a variância, a versão alternativa que conta fracassos, a propriedade da falta de memória e o atalho para probabilidades do tipo "pelo menos k tentativas".

### O que a variável mede

Como na binomial, parte-se de **ensaios de Bernoulli independentes**, todos com a mesma probabilidade de sucesso p (e fracasso q = 1 − p). A diferença está no que se conta: a binomial fixa o número de tentativas e conta sucessos; a **geométrica conta o número de tentativas até aparecer o primeiro sucesso**, e o sucesso que encerra a série é incluído na contagem.

- X = 1: sucesso logo na primeira tentativa;
- X = 2: um fracasso e depois o sucesso;
- X = k: **k − 1 fracassos seguidos de um sucesso**, nessa ordem.

Como os ensaios são independentes, multiplica-se:

**P(X = k) = q^(k − 1) · p**, para k = 1, 2, 3, ...

O único parâmetro é p, por isso se escreve X ~ Geo(p). Conhecido p, toda a distribuição está determinada.

> 💡 **Exemplo:** num sorteio em que cada tentativa tem chance p = 0,25 de premiar, a probabilidade de o primeiro prêmio sair exatamente na 3ª tentativa é 0,75² · 0,25 = 0,140625, ou seja, cerca de 14%.

### Valores possíveis

A variável é discreta, mas **sem limite superior**: X pode ser 1, 2, 3, ... indefinidamente. Valores muito altos são improváveis, porém nunca impossíveis (com p = 1/6, esperar 50 tentativas tem probabilidade minúscula, mas positiva). Também **não pode ser menor que 1**: é preciso ao menos uma tentativa para ter o sucesso.

### Esperança e variância

| Medida | Fórmula (X = nº de ensaios até o 1º sucesso) |
| --- | --- |
| Esperança | E(X) = 1 / p |
| Variância | Var(X) = q / p² |
| Desvio padrão | raiz de q / p² |

A intuição da média: se a moeda dá cara com chance 1/2, espera-se 2 lançamentos até a primeira cara; com chance 1/5, espera-se 5 tentativas. Quanto menor p, maior a espera média e maior a dispersão.

> 💡 **Exemplo:** num posto de teste cada peça é defeituosa com chance 5%. O número de peças examinadas até achar a primeira defeituosa tem E(X) = 1 / 0,05 = 20 e Var(X) = 0,95 / 0,0025 = 380, de modo que o desvio padrão é cerca de 19,5, **um pouco menor que a média**. Como a raiz de q é sempre menor que 1, o desvio padrão (raiz de q, dividida por p) fica sempre abaixo de 1/p, e para p pequeno fica bem próximo dele; afirmar que ele é "superior" à média é item errado.

### Parametrização alternativa: contar fracassos

Algumas questões definem Y como o **número de fracassos antes do primeiro sucesso**. Nesse caso Y = 0, 1, 2, ... (zero é possível, pois o sucesso pode vir na primeira tentativa) e:

- **P(Y = k) = q^k · p** (expoente k, não k − 1);
- **Var(Y) = q / p²** (a mesma);
- **E(Y) = q / p** (a esperança anterior multiplicada por q; é a média de X menos 1).

> ⚠️ **Pegadinha:** antes de aplicar qualquer fórmula, veja como o enunciado define a variável. Se o primeiro elemento defeituoso encontrado corresponde a X = 1, a contagem é de **ensaios** (E = 1/p). Se se fala em reações negativas "antes da primeira" positiva, a contagem é de **fracassos** (E = q/p).

### Probabilidades de "pelo menos" e "menos de"

Para "pelo menos k tentativas" a via longa é o complementar: P(X ≥ k) = 1 − [P(X = 1) + ... + P(X = k − 1)]. Há atalho: sendo P(X ≥ k) = P(X = k) / p, obtém-se

**P(X ≥ k) = q^(k − 1)**

Faz sentido: precisar de pelo menos k tentativas é o mesmo que fracassar nas k − 1 primeiras. Exemplo: com p = 0,25, P(X ≥ 3) = 0,75² = 0,5625.

Na versão que conta fracassos, P(Y ≥ k) = q^k. Assim, a chance de "menos de 4 fracassos antes do primeiro sucesso", com p = 0,35 (q = 0,65), é P(Y < 4) = 1 − q⁴ = 1 − 0,65⁴, cerca de 0,82.

> ⚠️ **Pegadinha:** P(X = k) e P(X ≥ k) são coisas diferentes. Dizer que a chance de uma sala de espera de 4 lugares ficar insuficiente é "q⁴ · p" cobre só o caso em que chegam exatamente 5 pessoas; o correto, para 5 ou mais, é q⁴. Da mesma forma, "menos de k" é P(X ≤ k − 1) = 1 − q^(k − 1).

### Falta de memória

A geométrica é "sem memória": o que já aconteceu não altera o futuro, porque os ensaios são independentes. Duas formas aparecem em prova:

1. **P(X > t + s | X ≥ s) = P(X > t)**: sabendo que já se fracassou nas primeiras tentativas, a chance de ainda precisar de mais de t tentativas adicionais é igual à de precisar de mais de t tentativas desde o início. Se já se lançou a moeda dez vezes sem cara, a probabilidade de precisar de mais de quatro lançamentos extras é a mesma de quem começa do zero.
2. **P(X = k | X ≥ k) = p**: sabendo-se que o sucesso ainda não ocorreu até a tentativa k − 1, a chance de ele ocorrer na k-ésima é simplesmente p. Esta é a origem da identidade P(X ≥ k) = P(X = k) / p.

Aplicação típica: uma sala com 20 lugares já tem 18 ocupados e as chegadas seguem Geo(0,2). A probabilidade de lotar é a de que o tempo restante seja exatamente 2: P(X = 2) = 0,8 · 0,2 = 0,16, sem considerar as 18 anteriores.

### Jogos alternados

Em disputas em que dois jogadores tentam por turnos, o primeiro a ter sucesso vence. Para a probabilidade de o 1º jogador vencer na sua k-ésima tentativa, multiplique: k − 1 fracassos dele, k − 1 fracassos do adversário (que jogou o mesmo número de vezes antes) e o sucesso dele. Exemplo: A tem p = 1/3 e começa; B tem p = 1/4. A vence em sua 2ª jogada com (2/3) · (3/4) · (1/3) = 1/6.

### Para fixar
- Geométrica conta ensaios de Bernoulli independentes até o primeiro sucesso; X ~ Geo(p) com X = 1, 2, 3, ... sem limite superior.
- P(X = k) = q^(k − 1) · p: k − 1 fracassos e o sucesso na última tentativa.
- E(X) = 1/p e Var(X) = q/p²; o desvio padrão é sempre menor que a média, e quase igual a ela quando p é pequeno.
- Se a variável conta fracassos antes do sucesso, P(Y = k) = q^k · p, E(Y) = q/p e a variância não muda.
- P(X ≥ k) = q^(k − 1), não confundir com P(X = k); "menos de k" é o complementar.
- Falta de memória: P(X > t + s | X ≥ s) = P(X > t) e P(X = k | X ≥ k) = p; o passado não altera as probabilidades futuras.
- Não confundir com hipergeométrica (sem reposição) nem com binomial (n fixo).

# SINTÉTICO

- **Definição**: conta os ensaios de Bernoulli independentes até o primeiro sucesso, incluindo-o; X ~ Geo(p), com X = 1, 2, 3, ... sem teto.
- **Probabilidade pontual**: P(X = k) = q^(k − 1) · p, isto é, k − 1 fracassos e depois o sucesso.
- **Média e variância**: E(X) = 1/p e Var(X) = q/p²; quanto menor p, maior a espera média e a dispersão.
- **Parametrização por fracassos**: Y = 0, 1, 2, ...; P(Y = k) = q^k · p, E(Y) = q/p e a variância continua q/p²; leia o enunciado para saber qual contagem vale.
- **Pelo menos k tentativas**: P(X ≥ k) = q^(k − 1), atalho do complementar; para fracassos, P(Y ≥ k) = q^k.
- **Pegadinha**: P(X = k) não é P(X ≥ k); "menos de k" equivale a 1 − q^(k − 1) na contagem por ensaios.
- **Falta de memória**: P(X > t + s | X ≥ s) = P(X > t); já ter fracassado s vezes não melhora nem piora as chances.
- **Segunda forma da falta de memória**: P(X = k | X ≥ k) = p, a probabilidade condicional é a própria p.
- **Distinguir**: geométrica espera o 1º sucesso; hipergeométrica é sem reposição em população finita; binomial fixa n.

# NOTAS

- Pág. 41, questão da Marinha: a resolução escreve P(X > 4) onde a conta correta é P(X < 4) = 1 − q^4 (o valor 0,82 está certo). Registrado como erro de digitação do material; no resumo uso P(Y < 4).
- Pág. 42, questão da DPE/RJ, item C: o enunciado diz 0,448 e a resolução obtém 0,36, ou seja, a alternativa está errada (gabarito D); coerente.
- Acrescentado fora do trecho: o exemplo dos jogos alternados generaliza a questão resolvida na pág. 38 (números próprios); a observação de que o desvio padrão é sempre menor que 1/p decorre das fórmulas do trecho.
- Nenhuma página vazia ou ilegível.
