---
id: S0441
agente: CLAUDE-L4
materia: Estatística
aula: Aula 10 — Distribuições Aleatórias Contínuas
trecho: estatistica/a10/s07
paginas_lidas: 63-76
---
# ANALÍTICO

Este trecho apresenta três distribuições contínuas construídas a partir da normal padrão e que sustentam a inferência estatística: a qui-quadrado, a t de Student e a F de Snedecor. Para cada uma interessam a definição (como é formada), o parâmetro (graus de liberdade), o formato, a média e a variância, o uso das tabelas e as relações entre elas.

### Distribuição qui-quadrado

**Definição.** A qui-quadrado com k graus de liberdade é a **soma dos quadrados de k variáveis normais padrão independentes**:

X²_k = Z1² + Z2² + ... + Zk², com cada Z_i ~ N(0, 1).

O **número de graus de liberdade (k)** é o único parâmetro e indica quantas normais padrão foram elevadas ao quadrado e somadas. Se as normais originais não forem padrão (têm média μ_i e desvio-padrão σ_i), é preciso **padronizar antes de elevar ao quadrado**: cada termo é ((X_i − μ_i)/σ_i)². Sem padronizar, o resultado não é uma qui-quadrado comum (seria uma versão "não central").

> 💡 **Exemplo:** X ~ N(50, 16) (média 50, variância 16, desvio 4) e Y ~ N(30, 25) (desvio 5), independentes. Então Q = ((X − 50)/4)² + ((Y − 30)/5)² segue qui-quadrado com **2** graus de liberdade. Se a questão trouxer a soma dos quadrados dos desvios em relação à média verdadeira dividida pela variância, a distribuição é qui-quadrado com **n** graus (um por observação).

**Propriedades.**
- Só assume valores **não negativos** (soma de quadrados) e é **assimétrica à direita**.
- Quanto maior k, mais simétrica fica; para k grande, aproxima-se da normal (consequência do Teorema Central do Limite).
- **Esperança E = k** e **Variância = 2k**.
- **Aditividade:** a soma de qui-quadrados independentes, com k1, k2, ..., kn graus, é qui-quadrado com **k1 + k2 + ... + kn** graus de liberdade. Ex.: uma qui-quadrado com 3 graus somada a outra, independente, com 5 graus resulta em qui-quadrado com 8 graus, média 8 e variância 16.
- É um **caso particular da distribuição gama**, com parâmetros alfa = k/2 e beta = 1/2.
- Com k = 2, a gama tem alfa = 1 e vira a **exponencial**, com parâmetro lambda = 1/2 e média 2. Logo, **exponencial de média 2 = qui-quadrado com 2 graus**, e a soma de n exponenciais independentes de média 2 é qui-quadrado com **2n** graus de liberdade.

**Tabela.** Para cada k (linhas) traz o valor x que deixa uma dada probabilidade à esquerda, P(X²_k < x), indicada na primeira linha. Como a distribuição é assimétrica, a tabela cobre toda a curva (acima e abaixo da média). Exemplo de leitura: com 5 graus de liberdade e probabilidade 0,5, a mediana é 4,351 (note que a mediana é menor do que a média, 5, por causa da assimetria à direita).

| Característica | Qui-quadrado |
| --- | --- |
| Formação | soma de k normais padrão ao quadrado |
| Valores | x ≥ 0 |
| Forma | assimétrica à direita |
| Média / variância | k / 2k |
| Parâmetro | k (graus de liberdade) |

### Distribuição t de Student

**Definição.** T = Z / raiz de (X²_k / k), em que Z é normal padrão, X²_k é qui-quadrado com k graus de liberdade, e Z e X²_k são **independentes**. O único parâmetro é k (graus de liberdade).

**Propriedades.**
- Tem **forma de sino, é simétrica em torno de 0** (média, mediana e moda iguais a 0) e assume valores em toda a reta real.
- Comparada à normal padrão, é **mais baixa no centro e tem caudas mais pesadas** (mais larga nos extremos): maior variabilidade.
- **Variância = k / (k − 2), definida apenas para k > 2.** Como k/(k − 2) é sempre maior do que 1, a variância da t é sempre maior do que a da normal padrão, mas diminui e tende a 1 quando k cresce. Assim, com k grande (amostras grandes), a t **aproxima-se da normal padrão**.
- Para k = 4, a variância é 4/2 = 2; para k = 10, é 10/8 = 1,25.

**Tabela.** Linhas são os graus de liberdade (v), colunas são as probabilidades acumuladas P(T < t), e o corpo traz o valor t. Como a curva é simétrica, a tabela só lista probabilidades acima de 50%; para a cauda esquerda use P(T < −t) = P(T > t), e P(T < 0) = P(T > 0) = 0,5. Exemplo de leitura: com 5 graus de liberdade e P(T < t) = 0,9, o valor é t = 1,48.

> ⚠️ **Pegadinha (caso k = 1: Cauchy):** com 1 grau de liberdade, T = Z1/Z2 é a **razão de duas normais padrão independentes**, que é a **distribuição de Cauchy**. Ela é simétrica e mais achatada do que a normal, mas é "patológica": **não tem média nem variância definidas**. Portanto, razão entre duas normais padrão independentes = Cauchy = t de Student com **1** grau de liberdade (e não 2). Se a questão apresentar (A − média de A)/(desvio de A) dividido por uma normal padrão independente, também é um t de 1 grau.

> 💡 **Exemplo:** A ~ N(10, 4) e B ~ N(0, 1) independentes. R = (A − 10)/(2B) = Z1/B é a razão de duas normais padrão, logo t com 1 grau de liberdade (Cauchy). R é simétrica em torno de 0, mas não tem variância definida.

| Característica | t de Student |
| --- | --- |
| Formação | normal padrão dividida pela raiz de (qui-quadrado / k) |
| Valores | toda a reta real |
| Forma | sino simétrico, média 0, caudas mais pesadas que a normal |
| Variância | k / (k − 2), para k > 2 |
| Limite | tende à normal padrão quando k aumenta |

### Distribuição F de Snedecor (ou Fisher-Snedecor)

**Definição.** F = (X²_k1 / k1) / (X²_k2 / k2), a **razão entre duas qui-quadrado independentes, cada uma dividida pelos seus graus de liberdade**. Os parâmetros são **k1 (numerador)** e **k2 (denominador)**: a ordem importa.

**Propriedades.**
- Só assume valores **positivos** (razão de duas quantidades positivas) e é **assimétrica à direita**; o formato depende dos dois parâmetros.
- **Média = k2 / (k2 − 2), para k2 > 2.** Só o grau de liberdade do **denominador** entra na média, e ela é sempre maior do que 1 (diminui quando k2 cresce). É a mesma expressão da variância da t.
- **Relação com a t:** o **quadrado** de uma t com k graus de liberdade é uma F com **1 grau no numerador e k no denominador**: T² = F(1, k). Isso porque o numerador de T² é Z², uma qui-quadrado com 1 grau de liberdade.

**Tabela.** Como há dois parâmetros, uma tabela serve só para **uma probabilidade fixa** na cauda direita. Por exemplo, a tabela de P(F > f) = 0,05 informa que, com 5 graus no numerador e 10 no denominador, f = 3,33. Para outra probabilidade, como 0,10, é preciso outra tabela.

| Característica | F de Snedecor |
| --- | --- |
| Formação | (qui-quadrado1 / k1) dividida por (qui-quadrado2 / k2) |
| Valores | x > 0 |
| Forma | assimétrica à direita |
| Média | k2 / (k2 − 2), k2 > 2 (só depende do denominador) |
| Parâmetros | k1 (numerador) e k2 (denominador) |

> ⚠️ **Pegadinha:** para ser F, numerador e denominador precisam ser **qui-quadrados independentes** divididos pelos respectivos graus de liberdade. Se o numerador for construído a partir da **soma** de normais (que é uma normal, não uma qui-quadrado), a razão não é F. Também é errado dizer que a média da F depende dos dois graus de liberdade: depende só do denominador.

### Visão comparativa

| Distribuição | Parâmetros | Média | Variância | Simetria |
| --- | --- | --- | --- | --- |
| Qui-quadrado | k | k | 2k | assimétrica à direita |
| t de Student | k | 0 | k/(k − 2), k > 2 | simétrica |
| F de Snedecor | k1, k2 | k2/(k2 − 2), k2 > 2 | (não tratada no trecho) | assimétrica à direita |

### Para fixar
- Qui-quadrado com k graus = soma de k normais padrão independentes ao quadrado; média k, variância 2k; assimétrica à direita; soma de qui-quadrados soma os graus de liberdade.
- Normais não padrão devem ser padronizadas (subtrair a média e dividir pelo desvio) antes de elevar ao quadrado.
- Qui-quadrado com 2 graus de liberdade é uma exponencial de média 2; a soma de n exponenciais de média 2 é qui-quadrado com 2n graus.
- t de Student = Z dividido pela raiz de (qui-quadrado/k), com Z e a qui-quadrado independentes; simétrica, média 0, caudas mais pesadas que a normal; variância k/(k − 2) para k > 2; tende à normal com k grande.
- t com 1 grau de liberdade = Cauchy = razão de duas normais padrão independentes, sem média nem variância definidas.
- F de Snedecor = razão de duas qui-quadrado independentes divididas pelos seus graus; só assume valores positivos; média k2/(k2 − 2) depende só do denominador.
- O quadrado de uma t com k graus de liberdade é uma F(1, k).
- Tabelas: qui-quadrado e t trazem P(menor que) por graus de liberdade (t só acima de 0,5, usando a simetria); a F tem uma tabela para cada probabilidade de cauda direita (por exemplo, 0,05).

# SINTÉTICO

- **Qui-quadrado**: soma de k normais padrão independentes elevadas ao quadrado; o único parâmetro é k (graus de liberdade); só valores não negativos, assimétrica à direita; média k e variância 2k.
- **Padronização**: normais com média e desvio quaisquer devem ser transformadas em Z = (X − média)/desvio antes de formar a qui-quadrado.
- **Aditividade e exponencial**: qui-quadrados independentes somam os graus de liberdade; exponencial de média 2 é qui-quadrado com 2 graus, e a soma de n delas tem 2n graus.
- **t de Student**: Z dividido pela raiz de (qui-quadrado/k), com independência entre Z e a qui-quadrado; é simétrica com média 0, mais baixa no centro e de caudas mais pesadas que a normal.
- **Variância da t**: k/(k − 2) para k > 2, sempre maior que 1 e tendendo a 1 quando k cresce, de modo que a t se aproxima da normal.
- **Cauchy**: t com 1 grau de liberdade é a razão de duas normais padrão independentes e não tem média nem variância definidas.
- **F de Snedecor**: razão de duas qui-quadrado independentes, cada uma dividida por seus graus (k1 no numerador, k2 no denominador); valores positivos e assimetria à direita.
- **Média da F**: k2/(k2 − 2) para k2 > 2; depende só do denominador e é maior que 1. Dizer que depende dos dois graus é erro clássico.
- **Relação t e F**: T² tem distribuição F com 1 e k graus de liberdade.
- **Tabelas**: qui-quadrado e t dão P(menor que) por grau de liberdade (a t só acima de 0,5 por simetria); a F exige uma tabela por probabilidade de cauda direita.

# NOTAS

- Os gráficos das densidades (páginas 63, 68 e 73) e as tabelas numéricas (páginas 64, 69, 70, 74 e 75) não foram extraídos; usei apenas os valores citados no texto (mediana 4,351 da qui-quadrado com 5 graus; t = 1,48 para 5 graus e P = 0,9; f = 3,33 para P(F > f) = 0,05 com 5 e 10 graus).
- Página 75: o texto diz que o numerador fica nas linhas e o denominador nas colunas, mas depois lê a "5ª coluna e 10ª linha" para 5 e 10 graus de liberdade; a ordem da leitura parece trocada. O valor 3,33 corresponde a F(5, 10) com 5% na cauda, então mantive o valor e não detalhei qual eixo é qual.
- Página 63: o material diz que, para normais com média diferente de zero, o parâmetro de não centralidade seria "igual à média"; na definição usual esse parâmetro é a soma dos quadrados das médias. Por não ter certeza do que a banca adota, deixei apenas a ideia de que sem padronizar a distribuição não é a qui-quadrado comum.
- A variância da F não é apresentada no trecho; ficou fora do resumo.
- Página 76, questão de F com soma de normais: na questão original aparecem expressões com barras de fração embaralhadas pela extração; usei só a conclusão do gabarito (Errado, porque o numerador é normal, não qui-quadrado).
- A média 0 da t vale para k > 1 (para k = 1 é a Cauchy, sem média definida); o material afirma média 0 de forma geral e depois trata a Cauchy separadamente.
