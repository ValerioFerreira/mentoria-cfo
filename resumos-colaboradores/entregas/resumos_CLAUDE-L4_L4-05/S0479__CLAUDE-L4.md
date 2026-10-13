---
id: S0479
agente: CLAUDE-L4
materia: Estatística
aula: Aula 10 — Distribuições Aleatórias Contínuas
trecho: estatistica/a10/s06
paginas_lidas: 51-62
---
# ANALÍTICO

Este trecho mostra o que acontece quando se somam variáveis aleatórias: a soma de normais continua normal, e a soma de variáveis quaisquer tende à normal quando há muitas parcelas (Teorema Central do Limite). Dessa ideia sai a aproximação da binomial pela normal, que exige a correção de continuidade.

### Soma e diferença de normais independentes

Se X1, X2, ..., Xn são normais **independentes**, a soma Y = X1 + X2 + ... + Xn também é normal, com:

- E(Y) = E(X1) + E(X2) + ... + E(Xn);
- Var(Y) = Var(X1) + Var(X2) + ... + Var(Xn).

Para a **diferença** Y = X1 − X2, a média é a diferença das médias, mas a variância é a **soma** das variâncias: Var(Y) = Var(X1) + Var(X2). A variância nunca é subtraída, pois cada variável acrescenta incerteza.

> 💡 **Exemplo:** X1 ~ N(10; 9) e X2 ~ N(4; 16), independentes. Então X1 − X2 ~ N(10 − 4; 9 + 16) = N(6; 25), com desvio padrão 5.

Uma transformação linear também mantém a normalidade. Para Y = aX + b, com X normal: **E(Y) = a·E(X) + b** e **Var(Y) = a²·Var(X)**. A constante somada (b) desloca a média, mas não altera a variância; o multiplicador (a) entra elevado ao quadrado na variância.

> 💡 **Exemplo:** X ~ N(3; 4) e Y = 5X − 2. E(Y) = 5·3 − 2 = 13 e Var(Y) = 25·4 = 100, logo Y ~ N(13; 100).

> ⚠️ **Pegadinha:** some **variâncias**, nunca desvios padrão. E a regra de somar variâncias exige independência: X + X = 2X tem variância 4·Var(X), e não 2·Var(X), porque as duas parcelas são a mesma variável.

| Operação | Média | Variância |
| --- | --- | --- |
| X1 + X2 (independentes) | soma das médias | soma das variâncias |
| X1 − X2 (independentes) | diferença das médias | soma das variâncias |
| aX + b | a·média + b | a² · variância |

### Teorema Central do Limite (TLC)

Considere X1, ..., Xn **independentes e identicamente distribuídas** (i.i.d.), com qualquer distribuição de média E(X) e variância Var(X). A soma S = X1 + ... + Xn **tende a uma distribuição normal** à medida que n cresce, com:

- E(S) = n · E(X);
- Var(S) = n · Var(X).

O ponto central: a distribuição de origem **não precisa ser normal**; basta ter muitas parcelas. Por isso o TLC é a base da inferência com amostras, já que os elementos de uma amostra aleatória são independentes e seguem a distribuição da população. Na prática, também se obtém a distribuição aproximadamente normal para variáveis independentes **não idênticas**, desde que as variâncias sejam de ordens parecidas (nenhuma parcela domina as outras); nesse caso, soma-se cada média e cada variância separadamente.

> 💡 **Exemplo:** em 50 lançamentos de um dado honesto, cada lançamento tem média 3,5 e variância 35/12 ≈ 2,92. A soma dos pontos é aproximadamente normal, com média 50·3,5 = 175 e variância 50·35/12 ≈ 145,8 (desvio padrão ≈ 12,1).

> ⚠️ **Pegadinha:** a convergência do TLC é **em distribuição**: o que se aproxima são as funções de distribuição acumulada, e não necessariamente as densidades ponto a ponto. Esse é o tipo de convergência mais fraco entre os usuais. A aproximação é por definição aproximada; "é exatamente normal" só vale quando as parcelas já são normais.

Resolução típica (soma de binomiais): 64 variáveis binomiais independentes, cada uma com n = 12 e p = 0,25. Cada uma tem média 3 e variância 12·0,25·0,75 = 2,25. A soma tem média 64·3 = 192, variância 64·2,25 = 144 e desvio padrão 12. A probabilidade de a soma exceder 207 é P(Z > (207 − 192)/12) = P(Z > 1,25) = 1 − Φ(1,25), ou seja, 1 − 0,894 = 0,106.

### Aproximação da binomial pela normal

Uma binomial X é a soma de n ensaios de Bernoulli independentes e idênticos. Pelo TLC, para n grande, ela se aproxima de uma normal Y com:

- E(Y) = n·p;
- Var(Y) = n·p·(1 − p) = n·p·q.

Quanto **maior o n** e quanto **mais próximo de 1/2 for p**, melhor a aproximação: com n = 10, a binomial de p = 0,5 já é bem parecida com uma normal, enquanto a de p = 0,1 é assimétrica e se afasta dela; com n = 50, até p = 0,1 fica razoável. A regra empírica usual exige **n · min(p, q) > 5** (e, para precisão melhor, maior que 15). Em prova, o enunciado costuma deixar claro que a aproximação é permitida.

### Correção de continuidade

A binomial é discreta e a normal é contínua. Para compensar, **amplia-se meia unidade** de cada lado do intervalo discreto. Com os extremos **incluídos**:

**P(a ≤ X ≤ b) ≅ P(a − 0,5 < Y < b + 0,5)**

Se o intervalo não inclui um extremo, **primeiro converta** a desigualdade para uma que inclua os extremos (valores inteiros), e só então aplique ±0,5:

| Binomial (discreta) | Equivale a | Normal (contínua) |
| --- | --- | --- |
| P(X = k) | P(k ≤ X ≤ k) | P(k − 0,5 < Y < k + 0,5) |
| P(X ≥ k) | k ou mais | P(Y > k − 0,5) |
| P(X > k) | P(X ≥ k + 1) | P(Y > k + 0,5) |
| P(X ≤ k) | k ou menos | P(Y < k + 0,5) |
| P(X < k) | P(X ≤ k − 1) | P(Y < k − 0,5) |
| P(a < X < b) | P(a + 1 ≤ X ≤ b − 1) | P(a + 0,5 < Y < b − 0,5) |

Exemplo do próprio intervalo aberto: "mais de 3 e menos de 8 sucessos" é [4, 7], que vira P(3,5 < Y < 7,5).

#### Roteiro de resolução
1. Calcular a média n·p e a variância n·p·q (e o desvio padrão, a raiz da variância).
2. Aplicar a correção de continuidade ao intervalo.
3. Padronizar cada limite: z = (y − média)/desvio padrão.
4. Consultar a tabela da normal padrão e usar complemento ou simetria quando necessário.

> 💡 **Exemplo resolvido:** X ~ Binomial(n = 200; p = 0,3). Média = 60; variância = 200·0,3·0,7 = 42; desvio ≈ 6,48. Para P(X ≥ 70): P(Y > 69,5), com z = (69,5 − 60)/6,48 ≈ 1,47. A resposta é 1 − Φ(1,47).

Na prática, o efeito é grande: para X binomial com n = 50 e p = 0,5, a probabilidade de ficar entre 20 e 30 vale cerca de 0,8811 exatamente. Sem correção, a normal dá aproximadamente 0,8414. Com a correção (19,5 a 30,5), dá cerca de 0,8812, praticamente igual ao valor exato.

> ⚠️ **Pegadinha:** a correção não é "sempre +0,5": o sinal depende do lado. Em P(X ≥ k) subtrai-se 0,5 do limite; em P(X ≤ k) soma-se. Quando o intervalo é simétrico em torno da média, é comum usar 2 vezes a probabilidade de um lado só, mas lembre de corrigir o limite antes.

### Para fixar
- Soma de normais independentes é normal: somam-se as médias e as variâncias.
- Na diferença X1 − X2, a média subtrai, mas a variância continua somando.
- Em aX + b: média a·E(X) + b, variância a²·Var(X); a constante b não altera a variância.
- TLC: soma de n variáveis i.i.d. é aproximadamente normal, com média n·E(X) e variância n·Var(X), para qualquer distribuição de origem.
- A convergência do TLC é em distribuição (das acumuladas), o tipo mais fraco entre as usuais.
- Binomial grande ≅ normal com média n·p e variância n·p·q; melhor com n grande e p perto de 0,5 (regra: n·min(p, q) > 5).
- Correção de continuidade: P(a ≤ X ≤ b) ≅ P(a − 0,5 < Y < b + 0,5); antes, ajuste desigualdades estritas para incluir os extremos.
- Siga o roteiro: média e variância, correção, padronização z, tabela.

# SINTÉTICO

- **Soma de normais independentes**: continua normal; a média é a soma das médias e a variância é a soma das variâncias (não some desvios padrão).
- **Diferença de normais**: a média subtrai, mas a variância soma; por exemplo, N(10; 9) − N(4; 16) = N(6; 25).
- **Transformação linear**: Y = aX + b tem média a·E(X) + b e variância a²·Var(X); a constante b não altera a variância.
- **Teorema Central do Limite**: soma de n variáveis i.i.d., de qualquer distribuição, tende à normal com média n·E(X) e variância n·Var(X).
- **Tipo de convergência**: o TLC é convergência em distribuição, das acumuladas, não ponto a ponto das densidades.
- **Variáveis não idênticas**: a soma também fica aproximadamente normal se forem independentes e com variâncias parecidas.
- **Binomial pela normal**: usa média n·p e variância n·p·q; melhora com n grande e p perto de 0,5 (regra empírica n·min(p, q) > 5).
- **Correção de continuidade**: P(a ≤ X ≤ b) ≅ P(a − 0,5 < Y < b + 0,5); tira 0,5 do limite inferior e soma 0,5 ao superior.
- **Desigualdade estrita**: converta antes para extremos incluídos; P(3 < X < 8) = P(4 ≤ X ≤ 7) vira P(3,5 < Y < 7,5).
- **Roteiro**: calcular média e variância, aplicar a correção, padronizar com z = (y − média)/desvio e consultar a tabela.

# NOTAS

- Pág. 57: a conta de z usa o desvio 3,5255 (digitação; o valor correto é 3,5355, como na linha anterior). Não afeta o resumo.
- Pág. 53 (questão FADESP): o comentário escreve "V(X) = 36" por engano; o dado correto do enunciado é variância 9, e a resposta usa 4·9 = 36. Não afeta o resumo.
- Pág. 55–56 (questão sobre soma de 64 binomiais): a solução usa o limite 207 sem correção de continuidade, coerente com as alternativas dadas. Apresentei o cálculo assim, como no material.
- Acrescentado fora do trecho (regras estáveis): o alerta de que X + X = 2X tem variância 4·Var(X), por dependência entre as parcelas; os exemplos numéricos e a tabela de conversão de desigualdades da correção de continuidade (consequência direta da regra do trecho).
- A tabela normal parcial citada nas questões das págs. 60–62 não foi extraída; usei apenas os valores que o texto cita. Figuras (histogramas) descartadas.
