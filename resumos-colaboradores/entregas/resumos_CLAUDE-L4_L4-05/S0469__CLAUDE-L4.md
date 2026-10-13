---
id: S0469
agente: CLAUDE-L4
materia: Estatística
aula: Aula 07 — Variáveis Aleatórias Discretas
trecho: estatistica/a07/s01
paginas_lidas: 4-16
---
# ANALÍTICO

Este trecho abre a Estatística Inferencial. Apresenta a ideia de inferência, define variável aleatória, separa variáveis discretas de contínuas e mostra como funciona a função (distribuição) de probabilidade de uma variável discreta, incluindo o cálculo de constantes desconhecidas e o conceito de variáveis independentes e identicamente distribuídas.

### Ideia de inferência estatística

Em geral é impossível medir uma característica em toda a população (todos os brasileiros, todos os produtos fabricados). Por isso se observa uma **amostra** e, a partir dela, tiram-se conclusões sobre o todo. Três termos precisam ficar nítidos:

| Termo | Significado | Exemplo |
| --- | --- | --- |
| Parâmetro populacional | característica numérica da população, em regra desconhecida | salário médio de todos os servidores de um órgão |
| Estatística (estimativa) da amostra | mesma medida calculada na amostra | salário médio de 200 servidores sorteados |
| Inferência | conclusão sobre a população tirada da amostra | afirmar que o salário médio do órgão fica numa faixa estimada |

Como cada amostra sorteada produz um resultado diferente, as medidas obtidas na amostra variam ao acaso. Por isso são tratadas como **variáveis aleatórias**.

### Variável aleatória

**Variável aleatória (v.a.)** é uma regra que **transforma cada resultado possível do experimento (cada ponto do espaço amostral) em um número real**, dando uma descrição numérica ao fenômeno aleatório. Exemplos: codificar cara = 0 e coroa = 1; o número obtido na face de cima de um dado; a quantidade de cartas vermelhas numa mão de pôquer.

Pontos centrais:

- o valor que a variável assumirá é **incerto** (uma grandeza que sempre vale o mesmo não é variável aleatória);
- apesar da incerteza, os valores seguem um padrão, e por isso é possível atribuir probabilidades;
- a probabilidade passa a ser escrita como **P(X = x)**, ou simplesmente P(x), em vez de P(A) de um evento.

> 💡 **Exemplo:** seja X o número de caras em dois lançamentos de uma moeda honesta. X pode ser 0, 1 ou 2, com P(X = 0) = 1/4, P(X = 1) = 1/2 e P(X = 2) = 1/4.

### Discreta × contínua

| Aspecto | Discreta | Contínua |
| --- | --- | --- |
| Valores possíveis | enumeráveis (contáveis) | qualquer valor num intervalo |
| Como se obtém | contagem | medição |
| Probabilidade de um valor exato | pode ser positiva: P(X = x) > 0 | sempre zero |
| Onde se atribui probabilidade | em cada valor | em intervalos (por exemplo, entre 1,95 e 2,05) |
| Exemplos | número de filhos, de chamadas, de peças defeituosas | altura, peso, tempo, volume de água ingerido |

> ⚠️ **Pegadinha:** o que diferencia as duas não é o número de valores ser finito ou infinito. Uma variável discreta pode ter infinitos valores, desde que sejam contáveis (1, 2, 3, ... carros chegando a um pedágio, sem teto). A contínua tem valores que não se contam, apenas se medem. Regra de bolso: **contou, é discreta; mediu, é contínua**. Tempo, peso e distância são contínuos; "número de" é discreto.

> 💡 **Exemplo:** "tempo entre chegadas de navios" é contínua; "número de navios que chegam por dia" é discreta. Em questões de identificação, atente à ordem pedida (primeiro discreta, depois contínua) e ao fato de que ambas as variáveis de uma alternativa podem ser do mesmo tipo.

### Função de probabilidade (variável discreta)

A **função de probabilidade** atribui a cada valor x possível da variável a sua probabilidade P(X = x). Para uma amostra ou um espaço equiprovável, P(X = x) = (número de casos com X = x) / (número total de casos). Ela obedece aos axiomas da probabilidade, que viram duas condições obrigatórias:

1. **P(X = x) ≥ 0** para todo x (não há probabilidade negativa);
2. **a soma das probabilidades de todos os valores possíveis é igual a 1**, pois o espaço amostral inteiro tem probabilidade 1.

Se uma delas falhar, a função não é de probabilidade. A função de probabilidade não calcula média nem acumula probabilidades: ela só liga cada valor à sua chance. Quem leva um número real a cada resultado do experimento é a variável aleatória, não a função de probabilidade.

> 💡 **Exemplo de verificação:** num teste com 50 pacientes, 35 melhoraram. Com Y = 1 (melhora) e Y = 0 (sem melhora), P(Y = 1) = 35/50 = 0,7 e P(Y = 0) = 1 − 0,7 = 0,3. As duas condições são cumpridas.

A função pode ser dada por **fórmula** em x. Nesses casos:

- verifique que os valores são não negativos;
- se o conjunto de valores for infinito, a soma é uma série. Exemplo: P(X = x) = 1/2^x para x = 1, 2, 3, ... é uma progressão geométrica infinita com primeiro termo 1/2 e razão 1/2; sua soma é (1/2)/(1 − 1/2) = 1, logo é válida. A soma de uma PG infinita com razão de módulo menor que 1 é **primeiro termo / (1 − razão)**.

### Achando constantes desconhecidas

Muitas questões dão a função com uma incógnita k. A estratégia é **igualar a soma de todas as probabilidades a 1** e resolver.

> 💡 **Exemplo:** P(X = x) = x/k para x = 1, 2, 3 e 4. Soma: (1 + 2 + 3 + 4)/k = 1, logo k = 10. Então P(X = 3) = 3/10.

> 💡 **Exemplo com forma inversa:** P(X = x) = c/x para x = 1, 2 e 4. Soma: c × (1 + 1/2 + 1/4) = c × 7/4 = 1, logo c = 4/7. Então P(X = 1) = 4/7, P(X = 2) = 2/7, P(X = 4) = 1/7.

Para eventos que reúnem vários valores, **some as probabilidades** dos valores incluídos. Por exemplo, P(1 ≤ X ≤ 2) no exemplo c/x acima é P(1) + P(2) = 4/7 + 2/7 = 6/7. Em intervalos entre valores permitidos, conte só os valores que a variável realmente assume.

### Distribuição de probabilidade: tabela e gráfico

O conjunto dos pares (valor, probabilidade) é a **distribuição de probabilidade** da variável. Pode ser apresentada:

- em **tabela**, com os valores xi, as probabilidades P(X = xi) e, no rodapé, a soma igual a 1;
- em **gráfico de barras**, com os valores no eixo horizontal e as probabilidades no vertical. As barras são **separadas** por espaços porque os valores são pontuais.

O **histograma** é outro gráfico: serve para variáveis contínuas agrupadas em faixas e tem barras **coladas**, sem espaço. Barras separadas indicam variável discreta; barras unidas, contínua.

> 💡 **Exemplo:** um dado carregado em que a face 6 sai com 35%, a face 5 com 25%, a face 4 com 20%, a face 3 com 10%, a face 2 com 6% e a face 1 com 4% tem soma 1 e é uma distribuição válida. Já um dado honesto tem probabilidade 1/6 em todas as faces.

### Variáveis independentes e identicamente distribuídas (i.i.d.)

Duas ou mais variáveis são **i.i.d.** quando:

- são **mutuamente independentes** (o valor de uma não influencia as demais); e
- têm a **mesma distribuição de probabilidade**, isto é, os **mesmos valores possíveis com as mesmas probabilidades**.

Não basta repetir as probabilidades: os valores também precisam ser os mesmos.

> ⚠️ **Pegadinha:** se Yj assume os valores +j e −j, cada um com probabilidade 1/2, as variáveis Y1, Y2, Y3... têm as mesmas probabilidades, mas valores diferentes (±1, ±2, ±3...). Logo, **não são identicamente distribuídas**.

Dois lançamentos independentes de um mesmo dado viciado são exemplo clássico de variáveis i.i.d.

### Para fixar
- Inferência: concluir sobre a população (parâmetro) com base na amostra (estatística); como a amostra varia, a estatística é uma variável aleatória.
- Variável aleatória: transforma cada resultado do espaço amostral em um número real.
- Discreta: valores contáveis (mesmo infinitos); contínua: valores num intervalo, com probabilidade zero em cada ponto.
- Função de probabilidade: P(X = x) ≥ 0 para todo x e soma das probabilidades igual a 1.
- Para achar uma constante k, iguale a soma de todas as probabilidades a 1; para P(a ≤ X ≤ b), some as probabilidades dos valores incluídos.
- Gráfico de barras (barras separadas) é para discreta; histograma (barras coladas) é para contínua.
- i.i.d.: independentes e com a mesma distribuição (mesmos valores e mesmas probabilidades).

# SINTÉTICO

- **Inferência**: usa a amostra para concluir sobre o parâmetro populacional; a estatística da amostra varia de amostra para amostra, por isso é variável aleatória.
- **Variável aleatória**: regra que converte cada resultado do experimento em um número real; seus valores são incertos, mas probabilizáveis, e escreve-se P(X = x).
- **Discreta × contínua**: discreta tem valores contáveis (inclusive infinitos), contínua assume qualquer valor num intervalo; contou é discreta, mediu é contínua.
- **Probabilidade na contínua**: P(X = valor exato) é zero; só intervalos têm probabilidade.
- **Função de probabilidade**: dá P(X = x) a cada valor; exige P ≥ 0 e soma total igual a 1; não calcula média nem probabilidade acumulada.
- **Constante k**: iguale a soma das probabilidades a 1; exemplo x/k com x de 1 a 4 gera k = 10.
- **Série infinita**: uma PG com razão de módulo menor que 1 soma primeiro termo / (1 − razão); serve para validar funções com x = 1, 2, 3, ...
- **Intervalos**: P(a ≤ X ≤ b) é a soma das probabilidades dos valores que a variável de fato assume entre a e b.
- **Gráficos**: barras separadas para variável discreta; histograma, com barras coladas, para contínua.
- **i.i.d.**: variáveis independentes com mesmos valores e mesmas probabilidades; mesmas probabilidades com valores diferentes não bastam.

# NOTAS

- Pág. 10: a função de probabilidade do exemplo geométrico aparece na extração como "(2/3)^x" mas os valores calculados (2/3, 2/9, 2/27) e a soma 1 correspondem a 2/3^x; a formatação do texto está embaralhada. No resumo usei exemplo próprio (1/2^x), que evita a ambiguidade.
- Pág. 5: o material afirma que os valores de variáveis discretas "normalmente são números racionais"; ressalva imprecisa (o critério é serem enumeráveis), e por isso o resumo usa só o critério da enumerabilidade.
- Pág. 16: no comentário da questão Cebraspe há uma troca de rótulo (P(Y1 = -2) em vez de P(Y2 = -2)), erro de digitação sem efeito no resultado (gabarito Errado).
- Figuras (gráfico de barras do dado viciado e histograma) não foram extraídas; as informações relevantes estavam em tabela e no texto.
- Mais de um terço do trecho são questões comentadas; foram resumidos os métodos que elas ensinam (identificação de discreta × contínua, achar k, i.i.d.).
