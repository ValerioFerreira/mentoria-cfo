---
id: S0500
agente: CLAUDE-L4
materia: Estatística
aula: Aula 08 — Distribuições Discretas de Probabilidade
trecho: estatistica/a08/s01
paginas_lidas: 13-22
---
# ANALÍTICO

Este trecho apresenta a distribuição de Bernoulli (um único ensaio com dois resultados) e a distribuição binomial (repetição independente do mesmo ensaio). Cobre parâmetros, esperança e variância de Bernoulli, a fórmula da probabilidade binomial, o cálculo de intervalos e do "pelo menos um", e as condições de independência em amostras.

### Distribuição de Bernoulli

Uma variável aleatória discreta X tem distribuição de Bernoulli quando, em um experimento feito **uma única vez**, assume apenas dois valores: **1 (sucesso)** ou **0 (fracasso)**. O experimento é chamado **ensaio de Bernoulli**. Define-se "sucesso" como o resultado de interesse, qualquer que seja ele (não significa algo bom).

- p = P(X = 1): probabilidade de sucesso;
- q = P(X = 0): probabilidade de fracasso;
- como há só dois resultados, p + q = 1, ou seja, **q = 1 − p**.

O único **parâmetro** é p, e escrevemos X ~ Ber(p). Um mesmo experimento pode gerar variáveis de distribuições diferentes conforme o que se observa: um dado pode ser visto como uniforme (6 valores equiprováveis) ou como Bernoulli de parâmetros diferentes, dependendo do que se chama de sucesso.

> 💡 **Exemplo:** numa urna com 4 bolas vermelhas e 6 azuis, sorteia-se uma bola e o sucesso é sair vermelha. Então p = 4/10 = 0,4 e q = 0,6. Se o sucesso fosse "sair azul", teríamos p = 0,6.

#### Esperança e variância de Bernoulli
- **E(X) = p**, pois E(X) = 0·q + 1·p.
- **V(X) = p·q = p(1 − p)**, pois E(X²) = 0²·q + 1²·p = p e V(X) = E(X²) − [E(X)]² = p − p².

Na urna do exemplo: E(X) = 0,4 e V(X) = 0,4·0,6 = 0,24. Cuidado: a esperança de Bernoulli é a própria probabilidade de **sucesso**. Se uma questão fornece a probabilidade de fracasso, calcule primeiro p = 1 − q antes de responder.

> ⚠️ **Pegadinha:** se P(X = 1) = P(Y = 0) = 0,9 e as duas são Bernoulli, então E(X) = 0,9 mas E(Y) = 1 − 0,9 = 0,1. O dado 0,9 é de **fracasso** para Y, não de média.

### Distribuição binomial

Repetir o **mesmo ensaio de Bernoulli** n vezes gera a binomial. Condições:

- a probabilidade de sucesso **p é a mesma** em todas as repetições;
- as repetições são **independentes** (o resultado de uma não afeta as outras).

Parâmetros: o **número de repetições n** e a probabilidade de sucesso **p**. Escrevemos X ~ B(n, p). A variável X é o **número de sucessos** nas n repetições e pode assumir qualquer valor de **0 a n**.

Equivalências importantes:
- A binomial é a **soma de n variáveis de Bernoulli independentes** com o mesmo p.
- A soma de binomiais independentes com o **mesmo p** também é binomial, e os números de repetições se somam. Se X ~ B(3; p) e Y ~ B(4; p), então X + Y ~ B(7; p).
- Bernoulli é o caso particular da binomial com n = 1.

#### Como surge a fórmula
Para n = 3 lançamentos de um dado em que o sucesso é a face 6 (p = 1/6, q = 5/6), há 2·2·2 = 8 sequências possíveis de 0 e 1. Agrupando pelo número de sucessos:

| Sucessos | Sequências | Probabilidade |
| --- | --- | --- |
| 0 | 1 | q³ = 125/216 |
| 1 | 3 | 3·p·q² = 75/216 |
| 2 | 3 | 3·p²·q = 15/216 |
| 3 | 1 | p³ = 1/216 |

Raciocínio: cada sequência com k sucessos e n − k fracassos tem probabilidade p^k · q^(n−k) (eventos independentes: multiplica-se). Como os sucessos podem estar em quaisquer k das n posições, e as sequências são eventos mutuamente exclusivos (soma-se), multiplica-se por **quantas maneiras há de escolher as k posições**, que é a combinação C(n, k).

**P(X = k) = C(n, k) · p^k · q^(n−k)**, com C(n, k) = n! / [k! · (n − k)!]

A combinação também aparece como C_n^k ou "n sobre k". Casos extremos: P(X = 0) = q^n e P(X = n) = p^n.

> 💡 **Exemplo resolvido:** n = 4 e p = 0,3. P(X = 2) = C(4, 2) · 0,3² · 0,7² = 6 · 0,09 · 0,49 = 0,2646.

#### Esperança e variância da binomial
Como a binomial é a soma de n Bernoullis independentes, **E(X) = n·p** e **V(X) = n·p·q**. No exemplo anterior, E(X) = 1,2 e V(X) = 4·0,3·0,7 = 0,84.

### Probabilidades de intervalos e "pelo menos um"

- **Vários valores** ("1 ou 2 sucessos"): como os eventos são mutuamente exclusivos, **somam-se** as probabilidades individuais. Em 3 lançamentos de moeda honesta: P(X = 1) = 3·0,5·0,25 = 0,375, P(X = 2) = 0,375, logo P(X = 1 ou 2) = 0,75.
- **"Pelo menos um"**: use o complemento. **P(X ≥ 1) = 1 − P(X = 0) = 1 − q^n**. Em 3 lançamentos de moeda: 1 − 0,125 = 0,875.

> 💡 **Exemplo:** com p = 0,3 e n = 4, a chance de pelo menos um sucesso é 1 − 0,7⁴ = 1 − 0,2401 = 0,7599.

Em geral, escolha o caminho com menos parcelas: "pelo menos 1" e "no máximo n − 1" são muito mais simples pelo complemento.

### Binomial como amostra

A binomial também descreve uma **amostra de tamanho n** de uma população em que cada elemento é, de forma independente, sucesso com probabilidade p. Exemplo: 20% das peças de um lote são defeituosas (p = 0,2, q = 0,8) e se retiram n = 5 peças. O número de defeituosas na amostra segue B(5; 0,2). A probabilidade de exatamente 3 defeituosas é C(5, 3) · 0,2³ · 0,8² = 10 · 0,008 · 0,64 = 0,0512.

Para que valha a binomial, a proporção de sucessos **não pode mudar** entre as extrações. Isso ocorre quando:

- a seleção é **com reposição** (o elemento volta à população); ou
- a população é **infinita** ou muito grande em relação à amostra, de modo que a retirada altera pouco a proporção.

> ⚠️ **Pegadinha:** extração **sem reposição** de população pequena torna as extrações dependentes, e a binomial deixa de ser o modelo adequado.

### Para fixar
- Bernoulli: um ensaio, dois resultados (1 sucesso, 0 fracasso); X ~ Ber(p); p + q = 1.
- Bernoulli: E(X) = p e V(X) = p·q.
- Binomial: n ensaios de Bernoulli independentes e com o mesmo p; X ~ B(n, p) conta sucessos (0 a n).
- P(X = k) = C(n, k) · p^k · q^(n−k); a combinação conta as posições dos sucessos.
- A binomial é a soma de n Bernoullis independentes; somar binomiais com mesmo p soma os n.
- Vários valores: some probabilidades; "pelo menos um": 1 − q^n.
- Binomial em amostra exige independência: com reposição ou população grande.
- Binomial: E(X) = n·p e V(X) = n·p·q (fórmulas gerais da binomial).

# SINTÉTICO

- **Bernoulli**: um único ensaio com dois resultados, sucesso (X = 1, probabilidade p) e fracasso (X = 0, probabilidade q = 1 − p); o único parâmetro é p.
- **Média e variância de Bernoulli**: E(X) = p e V(X) = p·q; se a questão dá a probabilidade de fracasso, calcule p = 1 − q antes.
- **Binomial**: n repetições independentes do mesmo ensaio, com p constante; X ~ B(n, p) conta os sucessos e vai de 0 a n.
- **Soma**: a binomial é a soma de n Bernoullis independentes; binomiais independentes com o mesmo p somam os números de repetições.
- **Fórmula**: P(X = k) = C(n, k) · p^k · q^(n−k), em que a combinação conta de quantas formas os k sucessos se distribuem.
- **Casos extremos**: P(X = 0) = q^n e P(X = n) = p^n.
- **Mais de um valor**: eventos exclusivos, então se soma; "1 ou 2 sucessos" é P(1) + P(2).
- **Pelo menos um**: pelo complemento, P(X ≥ 1) = 1 − q^n.
- **Amostras**: o número de itens com certa característica numa amostra é binomial se a seleção é com reposição ou a população é grande.
- **Esperança e variância da binomial**: E(X) = n·p e V(X) = n·p·q.

# NOTAS

- O trecho (págs. 13–22) não traz E(X) = n·p e V(X) = n·p·q da binomial; acrescentei como regra estável e bem conhecida, deduzida da soma de n Bernoullis (marcado no resumo como acrescentado), com exemplo próprio.
- Pág. 17: a soma "nS = 4 + 3 = 7" aparece com os termos invertidos (nX = 3, nY = 4); o resultado 7 está correto.
- Pág. 18: a lista de valores de X = 1 tem chave aberta incorreta ("{0,0,1), ..."); erro de digitação sem efeito no conteúdo.
- Pág. 20: o material usa a mesma notação C_{n,k} para a combinação; apenas registrei as formas alternativas de escrita.
- Os exemplos numéricos do resumo (urna, n = 4 e p = 0,3) são próprios; a tabela das probabilidades do dado reaproveita os valores do trecho (p = 1/6, n = 3), reorganizados.
