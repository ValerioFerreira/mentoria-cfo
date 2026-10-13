---
id: S0501
agente: CLAUDE-L4
materia: Estatística
aula: Aula 08 — Distribuições Discretas de Probabilidade
trecho: estatistica/a08/s02
paginas_lidas: 23-32
---
# ANALÍTICO

A distribuição binomial conta o número de sucessos em uma série de tentativas independentes e idênticas. O trecho mostra como reconhecer a binomial no enunciado, calcular probabilidades pontuais e acumuladas e usar esperança e variância, inclusive para descobrir os parâmetros "de trás para frente".

### Quando a variável é binomial

Um **ensaio de Bernoulli** é um experimento com apenas dois resultados, chamados convencionalmente de **sucesso** (probabilidade p) e **fracasso** (probabilidade q = 1 − p). "Sucesso" é só o nome do evento que se quer contar: pode ser defeito, erro, ausência por doença, voto em um candidato.

A variável X é **binomial** quando conta quantos sucessos aparecem em **n ensaios de Bernoulli independentes, todos com o mesmo p**. Notação: X ~ Bin(n, p). Para reconhecer:

- número de tentativas **fixo** (n conhecido de antemão);
- cada tentativa com dois resultados;
- **mesma** probabilidade de sucesso em todas;
- tentativas **independentes** (com reposição, ou população tão grande que a retirada praticamente não a altera).

| Situação | Distribuição |
| --- | --- |
| Contar sucessos em n ensaios independentes | Binomial |
| Contar ensaios até o 1º sucesso | Geométrica |
| Contar sucessos em retiradas sem reposição de população pequena | Hipergeométrica |
| Contar eventos raros por intervalo, com taxa média constante | Poisson |
| Soma de muitos efeitos pequenos, curva simétrica em sino | Normal |

> ⚠️ **Pegadinha:** as bancas costumam trocar as alternativas por definições de outras distribuições (espera até o primeiro sucesso, contagem por intervalo, curva contínua). Fixe a palavra-chave: binomial = **n fixo, independência, p constante, conta sucessos**.

### Fórmula da probabilidade

P(X = k) = C(n, k) · p^k · q^(n − k), com k = 0, 1, ..., n

- C(n, k) = n! / [k! · (n − k)!] é o número de ordens em que os k sucessos podem aparecer entre as n tentativas;
- p^k é a probabilidade dos k sucessos e q^(n − k) a dos fracassos restantes.

Quando uma população é classificada em dois tipos (por exemplo, cível ou criminal, 60% e 40%) e se sorteia uma amostra grande, cada sorteio pode ser tratado como independente. Então "exatamente 6 de 10 serem do tipo com 60%" é P(X = 6) = C(10, 6) · 0,6^6 · 0,4^4 = 210 · 0,0467 · 0,0256, que dá cerca de 0,25. Atenção: a probabilidade de **um** sorteio (0,6) não é a probabilidade de uma **configuração** em n sorteios; um item que as confunda está errado.

> 💡 **Exemplo:** moeda viciada com P(cara) = 0,6, três lançamentos. Pelo menos duas caras: P(X = 2) = 3 · 0,36 · 0,4 = 0,432 e P(X = 3) = 0,6³ = 0,216. Soma: 0,648.

### Probabilidades acumuladas

As perguntas quase nunca pedem um único k. Traduza a expressão e some:

| Expressão | Valores de k somados |
| --- | --- |
| no máximo m, "não mais que m" | 0, 1, ..., m |
| menos de m | 0, 1, ..., m − 1 |
| pelo menos m | m, ..., n (ou 1 − P(X ≤ m − 1)) |
| mais de m | m + 1, ..., n |

Use o **complementar** quando for mais curto: "pelo menos 2" em 10 ensaios é 1 − [P(X = 0) + P(X = 1)], em vez de somar nove termos. Exemplo: três juízes independentes, cada um com 10% de chance de errar; "no máximo um erra" = 0,9³ + 3 · 0,1 · 0,9² = 0,729 + 0,243 = 0,972. Em outro exemplo, com 4% de ausência por dia e 10 empregados, P(X ≥ 2) = 1 − (0,96¹⁰ + 10 · 0,04 · 0,96⁹), cerca de 5,8%. Quando a prova fornece potências já calculadas (0,96⁹, 0,96¹⁰), é para usá-las nesse tipo de conta.

> ⚠️ **Pegadinha:** identifique corretamente quem é o "sucesso". Se a pergunta é sobre os erros dos juízes, p é a chance de **erro**, não de acerto. O sucesso é sempre o evento cuja contagem a pergunta pede.

### Esperança, variância e desvio padrão

- **E(X) = n · p** (média de sucessos: 100 lançamentos de moeda justa esperam 50 caras; o valor esperado pode ser fracionário, como 3 · 1/2 = 1,5);
- **Var(X) = n · p · q**;
- **DP(X) = raiz quadrada de n · p · q**.

A binomial é a soma de n Bernoullis independentes; por isso a esperança é n vezes a da Bernoulli (p) e a variância é n vezes a da Bernoulli (p · q).

Relações úteis para provas: Var(X) = E(X) · q, logo **q = Var / E**, e a variância é sempre menor que a esperança (q < 1).

### Forma da distribuição

- p = q = 0,5: distribuição **simétrica**, porque C(n, k) = C(n, n − k) e os pesos se equivalem;
- p > 0,5: assimetria **negativa** (cauda à esquerda);
- p < 0,5: assimetria **positiva** (cauda à direita);
- se n · p for um número **inteiro**, ele é ao mesmo tempo média, mediana e moda, mesmo com assimetria.

### Problemas inversos (achar p e n)

Quando o enunciado dá E(X) e/ou Var(X) em vez de n e p, monte o sistema n·p = E e n·p·q = Var.

1. Só a esperança e n: p = E / n. Exemplo: 5 clientes, E = 1, então p = 0,2; a chance de nenhuma venda é 0,8⁵, cerca de 0,33.
2. Esperança e variância: q = Var / E; p = 1 − q; n = E / p. Exemplo: E = 12 e Var = 2,4 dão q = 0,2, p = 0,8 e p/q = 4. Outro: média 20 e variância 4 dão q = 0,2, p = 0,8 e n = 20 / 0,8 = 25.

### Para fixar
- Binomial: n ensaios independentes, p constante, conta o número de sucessos; X ~ Bin(n, p).
- P(X = k) = C(n, k) · p^k · q^(n − k); a combinação conta as ordens possíveis.
- Traduza "no máximo", "menos de", "pelo menos" e "mais de" em somas de valores de k; use o complementar quando abreviar a conta.
- E(X) = n · p e Var(X) = n · p · q; o desvio padrão é a raiz da variância.
- q = Var / E permite recuperar p e n a partir de média e variância.
- Simétrica só com p = 0,5; p > 0,5 gera assimetria negativa e p < 0,5, positiva; n · p inteiro é média, mediana e moda.
- O sucesso é o evento que se conta, e a probabilidade de uma configuração não é o p de um ensaio.

# SINTÉTICO

- **Quando é binomial**: n ensaios de Bernoulli independentes, com p constante, contando o número de sucessos; X ~ Bin(n, p).
- **Probabilidade pontual**: P(X = k) = C(n, k) · p^k · q^(n − k); a combinação representa as ordens possíveis dos k sucessos.
- **Acumuladas**: "no máximo m" soma de 0 a m; "menos de m" vai até m − 1; "pelo menos m" costuma ser 1 menos a soma abaixo de m.
- **Sucesso é o que se conta**: se a pergunta é sobre erros, p é a chance de erro; confundir isso inverte a resposta.
- **Esperança**: E(X) = n · p, que pode ser fracionária (3 lançamentos de moeda justa esperam 1,5 cara).
- **Variância e desvio padrão**: Var(X) = n · p · q e DP = raiz de n · p · q; Var = E · q, portanto a variância é menor que a esperança.
- **Problemas inversos**: q = Var / E; depois p = 1 − q e n = E / p (média 20 e variância 4 dão p = 0,8 e n = 25).
- **Forma**: simétrica se p = 0,5; p > 0,5 dá assimetria negativa e p < 0,5, positiva; se n · p é inteiro, vale como média, mediana e moda.
- **Armadilha de item**: a probabilidade de um sorteio (0,6) não é a de uma configuração em n sorteios (0,6^6 · 0,4^4 vezes C(10, 6), cerca de 0,25).

# NOTAS

- O trecho (págs. 23-32) é inteiramente de questões comentadas; a definição e a fórmula da binomial foram apresentadas na página anterior ao trecho. A teoria resumida foi reconstruída a partir do que as questões usam (definição, fórmula, E, Var, simetria), com acréscimo de regras estáveis fora do trecho: a tabela comparativa com outras distribuições, a tradução de "no máximo/menos de/pelo menos" e o método dos problemas inversos (derivado das fórmulas do trecho).
- Divergência do material (pág. 24): no cálculo de P(X = 3) da moeda viciada aparece "1 × 0,36 × 1 = 0,216"; o correto é 0,6³ = 0,216 (a soma final 0,648 está certa).
- Pág. 26: a tabela com valores de 0,96^9 e 0,96^10 citada na questão da EBSERH não foi extraída do PDF; usei os valores que a resolução reproduz (0,665 e 0,693).
