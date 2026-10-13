---
id: S0382
agente: CLAUDE-L4
materia: Estatística
aula: Aula 01 — Médias
trecho: estatistica/a01/s02
paginas_lidas: 16-32
---
# ANALÍTICO

A média aritmética simples é a medida de posição mais usada em prova e no dia a dia (consumo médio, temperatura média, renda per capita). Este trecho define a média, mostra como resolver problemas de "valor que falta" e apresenta as seis propriedades que as bancas cobram com frequência.

### Definição e fórmula

A média aritmética é o quociente entre a **soma de todos os valores** e a **quantidade de valores**. A ideia por trás dela é que a média **preserva a soma**: se cada elemento da lista fosse trocado pela média, o total continuaria igual.

- Para n valores x1, x2, ..., xn: **x̅ = (x1 + x2 + ... + xn) / n**, ou x̅ = Σxi / n.
- Raciocínio: n valores iguais a x̅ somam n · x̅, que deve ser igual à soma original.
- Quando o enunciado diz apenas "média", entenda média aritmética.

> 💡 **Exemplo:** média de 6, 10, 14, 18 e 22. A soma é 70 e há 5 valores, logo x̅ = 14. Trocando os cinco por 14, a soma continua 5 · 14 = 70.

### Soma total a partir da média

Da própria definição, **soma = média × quantidade de termos** (apenas o "n" passou para o outro lado). Essa forma é a chave para resolver quase todos os problemas:

- **Valor que falta:** conhecendo a média e todos os valores menos um, calcula-se a soma total (média × n) e subtrai-se a soma dos valores conhecidos.
- Exemplo: média de 5 provas igual a 7,0; as quatro primeiras notas foram 6,5, 8, 7 e 5 (soma 26,5). A soma das cinco deve ser 35; a que falta vale 35 − 26,5 = **8,5**.
- **Juntar grupos:** a média do conjunto todo é a soma de todos os valores dividida pelo total de elementos. Somam-se as somas, não se faz média de médias, a menos que os grupos tenham o mesmo tamanho.
- Se a questão pede comparar médias em porcentagem ("a média A corresponde a quantos por cento da média B"), calcula-se cada uma e divide-se A por B (ex.: 5 ÷ 4 = 1,25 = 125%).
- Em gráficos e tabelas, leia primeiro os valores de cada barra ou linha e depois some.

### Propriedades da média aritmética

**1ª — Existência e unicidade:** para qualquer conjunto com pelo menos um elemento, a média existe e é única (é sempre possível somar e dividir, e o resultado é um único número).

**2ª — Limites:** a média fica entre o menor e o maior valor: **mínimo ≤ x̅ ≤ máximo**. Justificativa: cada elemento está entre o mínimo e o máximo; somando as n desigualdades e dividindo por n, a média herda os limites. Ex.: uma média de 12 é impossível se todos os valores são menores que 10.

**3ª — Soma ou subtração de constante:** somar (ou subtrair) c de todos os valores soma (ou subtrai) c da média: **y̅ = x̅ ± c**. Os valores 2, 4 e 9 têm média 5; somando 3 a cada um, obtém-se 5, 7 e 12, com média 8.

**4ª — Multiplicação ou divisão por constante:** multiplicar (ou dividir) todos os valores por c multiplica (ou divide) a média por c: **y̅ = x̅ · c** ou **y̅ = x̅ ÷ c**. Os mesmos valores 2, 4 e 9 multiplicados por 2 viram 4, 8 e 18, com média 10, o dobro de 5.

> ⚠️ **Pegadinha:** nas transformações lineares (y = a · x + b), a média sofre exatamente a mesma operação: y̅ = a · x̅ + b. Isso permite mudar de unidade (reais para milhares de reais, graus Celsius para Fahrenheit) sem refazer a conta.

**5ª — Soma dos desvios é zero:** o desvio de um valor é a sua diferença para a média (xi − x̅). Somando todos os desvios, com seus sinais, o resultado é sempre **zero**: Σ(xi − x̅) = 0. Os desvios negativos compensam os positivos. Ex.: 2, 4 e 9 (média 5) têm desvios −3, −1 e +4, e a soma é 0. Em termos de dedução: Σxi − n · x̅ = x̅ · n − n · x̅ = 0.

**6ª — Mínimo da soma dos quadrados:** se os desvios de cada valor até um número a qualquer forem elevados ao quadrado e somados, o total é **mínimo quando a = x̅**. Para qualquer outro valor, o resultado é maior. A relação exata é Σ(xi − a)² = Σ(xi − x̅)² + n · (x̅ − a)². No exemplo 2, 4 e 9: em torno da média (5), 9 + 1 + 16 = 26; em torno de a = 4, 4 + 0 + 25 = 29, que é 26 + 3 · (5 − 4)², confirmando a fórmula.

| Propriedade | Resumo | Ideia para a prova |
| --- | --- | --- |
| 1ª | existe e é única | sempre calculável com n ≥ 1 |
| 2ª | mín ≤ x̅ ≤ máx | a média nunca sai do intervalo dos dados |
| 3ª | x̅ ± c | constante somada desloca a média |
| 4ª | x̅ · c ou x̅ ÷ c | constante multiplicada escala a média |
| 5ª | Σ(xi − x̅) = 0 | desvios se anulam |
| 6ª | Σ(xi − a)² mínima em a = x̅ | média minimiza o erro quadrático |

> ⚠️ **Pegadinha:** a média pode ser um número que não pertence ao conjunto e não precisa ser inteira; só está obrigada a ficar entre o mínimo e o máximo. A soma dos desvios em valor absoluto não é zero, só a soma algébrica.

### Para fixar
- Média aritmética = soma dos valores ÷ quantidade; ela conserva a soma total.
- Soma total = média × n: usar para achar valor faltante e para juntar grupos (somar somas, não médias).
- Média sempre entre o menor e o maior valor.
- Somar/subtrair constante altera a média na mesma medida; multiplicar/dividir escala a média.
- Soma dos desvios em relação à média é zero.
- Soma dos quadrados dos desvios é mínima em relação à média: Σ(xi − a)² = Σ(xi − x̅)² + n(x̅ − a)².
- Média de um conjunto com um único elemento é o próprio elemento.

# SINTÉTICO

- **Definição**: média aritmética é a soma dos valores dividida pela quantidade (x̅ = Σxi / n); ela preserva a soma total, e sem outra indicação "média" é a aritmética.
- **Soma total**: soma = média × n; com ela se descobre o valor que falta (n · média menos a soma dos conhecidos).
- **Grupos**: a média do conjunto todo sai da soma de todas as somas dividida pelo total de elementos, e não da média das médias.
- **Limites**: a média está sempre entre o mínimo e o maior valor do conjunto (mín ≤ x̅ ≤ máx).
- **Constante somada ou subtraída**: a média sofre a mesma soma ou subtração (y̅ = x̅ ± c).
- **Constante que multiplica ou divide**: a média é multiplicada ou dividida pela mesma constante; em y = a · x + b, a média é a · x̅ + b.
- **Desvios**: somados com sinal, os desvios em torno da média resultam em zero, pois positivos e negativos se compensam.
- **Mínimos quadrados**: Σ(xi − a)² é mínima quando a é a média, e Σ(xi − a)² = Σ(xi − x̅)² + n · (x̅ − a)².
- **Existência**: a média sempre existe e é única para conjuntos com ao menos um elemento.

# NOTAS

- Págs. 18 a 21: as questões usam gráficos e tabelas cujos dados só aparecem nas resoluções; o resumo ensina o método, não reproduz as questões.
- Pág. 21: a resolução de uma das questões mostra o denominador como "6 / 0" no texto extraído (erro de extração; a conta correta é 150 ÷ 6 = 25).
- Págs. 30 a 31: no cálculo dos desvios em relação a 6, o texto mantém o símbolo da média nas linhas (x̅) em vez de a; a conta numérica está correta (soma 56). O resumo usa exemplo próprio.
- A observação de que a média pode ficar fora do conjunto e não ser inteira, e a equação das transformações lineares, são consequências diretas das propriedades 3 e 4, incluídas como esclarecimento.
