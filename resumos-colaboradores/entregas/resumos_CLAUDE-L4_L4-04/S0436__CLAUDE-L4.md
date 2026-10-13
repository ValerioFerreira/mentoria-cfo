---
id: S0436
agente: CLAUDE-L4
materia: Estatística
aula: Aula 01 — Médias
trecho: estatistica/a01/s01
paginas_lidas: 3-15
---
# ANALÍTICO

Este trecho introduz a ideia de média como resumo de um conjunto de dados, situa a média entre as medidas de posição (tendência central e separatrizes) e ensina a notação de somatório (sigma) com suas operações e propriedades, que serão a base de todos os cálculos de média e de variabilidade.

### A média como resumo de um conjunto

A média é um número que representa, de modo sintético, as características de um grupo de valores. Exemplo: um aluno com notas 5, 7, 9, 6 e 8 tem média aritmética 35/5 = 7; esse único número descreve o desempenho da turma de notas. Médias aparecem no dia a dia (expectativa de vida, renda per capita, consumo médio, tempo médio de deslocamento) e permitem **comparar populações**: se a expectativa de vida de um país é 24 anos menor que a de outro, os habitantes do primeiro tendem a viver, em média, 24 anos a menos. A forma de calcular depende de como os dados são apresentados (dados brutos, com frequências, em classes), e a média tem propriedades que simplificam questões.

### Medidas de posição

**Medidas de posição** são estatísticas que indicam a tendência de concentração dos dados e apontam em que ponto do eixo horizontal está a distribuição, isto é, onde se localiza o valor que melhor representa o conjunto. Dividem-se em dois grupos.

| Grupo | O que faz | Medidas |
| --- | --- | --- |
| **Tendência central** | representa o valor típico, onde se concentra a maioria dos dados | média, mediana, moda |
| **Separatrizes** | divide a série ordenada em partes com a mesma quantidade de elementos | mediana, quartis, decis, percentis |

#### Medidas de tendência central

- **Média aritmética**: a mais usada; é a soma de todas as observações dividida pelo número delas.
- **Mediana**: valor que ocupa a posição central da série ordenada (crescente ou decrescente).
- **Moda**: valor mais frequente, aquele que aparece o maior número de vezes.

Elas tendem a ficar na região central da distribuição de frequências, daí o nome. A média aparece em três versões nesta matéria: **aritmética, geométrica e harmônica** (a mediana e a moda completam o grupo).

#### Medidas separatrizes

- **Mediana**: divide a série em **2** partes iguais. É separatriz e também medida de tendência central (pertence aos dois grupos).
- **Quartis**: dividem em **4** partes iguais.
- **Decis**: dividem em **10** partes iguais.
- **Percentis**: dividem em **100** partes iguais.

> ⚠️ **Pegadinha:** "partes iguais" significa partes com o mesmo número de elementos, e não com a mesma amplitude de valores. A mediana é a única medida que figura nos dois grupos.

### Notação de somatório

O somatório (notação sigma) é uma abreviação para somas longas. O símbolo Σ (sigma maiúsculo) instrui a somar os termos de uma sequência x1, x2, ..., xn, em que **xi** é o termo geral (o i-ésimo termo). Escreve-se

**Σ xi, com i de 1 até n  =  x1 + x2 + ... + xn**

Os elementos da notação são:
- **índice** (em geral i; às vezes j ou k), escrito embaixo do sigma;
- **limite inferior**, o valor inicial do índice (por exemplo i = 1 ou i = 3), escrito embaixo;
- **limite superior**, o valor onde a soma para, escrito em cima;
- **termo geral**, à direita do sigma, que pode ser uma expressão (como 2i + 1, ou xi²).

Quando os limites são i = 1 e n, costuma-se **omitir os limites**: Σx significa x1 + ... + xn.

> 💡 **Exemplo:** seja a sequência x = {2, 4, 5, 9}. Σx (i de 1 a 4) = 20. Σ xi com i de 2 a 4 = 4 + 5 + 9 = 18 (começa no segundo termo, não no primeiro). Σ xi² = 4 + 16 + 25 + 81 = 126. Para o termo geral 2k + 1 com k de 1 a 4: 3 + 5 + 7 + 9 = 24. Para um termo em fração, como Σ 1/i com i de 2 a 4: 1/2 + 1/3 + 1/4 = (6 + 4 + 3)/12 = 13/12.

### Operações que não se confundem

O ponto mais cobrado é a diferença entre operações com aparência parecida. Tome as sequências x = {2, 4, 5, 9} e y = {1, 3, 2, 0}:

| Operação | Significado | Cálculo no exemplo |
| --- | --- | --- |
| **Soma dos produtos** Σ(xi · yi) | multiplica par a par e depois soma | 2·1 + 4·3 + 5·2 + 9·0 = 24 |
| **Produto das somas** (Σxi)·(Σyi) | soma cada sequência e depois multiplica | 20 · 6 = 120 |
| **Soma dos quadrados** Σ xi² | eleva cada termo ao quadrado e depois soma | 4 + 16 + 25 + 81 = 126 |
| **Quadrado da soma** (Σ xi)² | soma tudo e depois eleva ao quadrado | 20² = 400 |

Em geral **Σ(xi·yi) ≠ (Σxi)·(Σyi)** e **(Σxi)² ≠ Σxi²**. Essa distinção reaparece nas fórmulas de variância e covariância.

### Propriedades do somatório

**1ª — somatório de uma constante:** somar uma constante k, n vezes, dá **k · n**.

Σ k (i de 1 a n) = k + k + ... + k = k · n

A prova é imediata: k = k·1, e colocando k em evidência sobra (1 + 1 + ... + 1) com n parcelas. Exemplo: 99 termos iguais a 9 somam 9 · 99 = 891. Atenção: o que conta é o **número de termos** da soma (limite superior − limite inferior + 1), e não o valor da constante.

**2ª — constante multiplicando a variável:** a constante sai do somatório.

Σ (k · xi) = k · Σ xi

Exemplo: se os 5 salários de uma equipe somam 7.500 e todos forem dobrados, a nova folha é 2 · 7.500 = 15.000, sem precisar recalcular termo a termo.

**3ª — soma ou subtração:** o somatório de uma soma (ou subtração) é a soma (ou subtração) dos somatórios.

Σ (xi ± yi) = Σ xi ± Σ yi

Exemplo: se os salários somam 12.500 e se paga um bônus fixo de 1.000 a cada um dos 5 empregados (bônus total 5 · 1.000 = 5.000), o total pago é 12.500 + 5.000 = 17.500.

**Consequência útil** (juntando as três): Σ (a·xi + b) = a · Σxi + b · n. No exemplo x = {2, 4, 5, 9}: Σ(3xi − 2) = 3 · 20 − 2 · 4 = 52. O termo constante, quando está dentro da soma, vira "constante × número de termos".

> ⚠️ **Pegadinha:** as propriedades valem para **soma, subtração e constantes**. Não se pode "distribuir" o somatório em produtos ou em potências: Σ(xi·yi) não é (Σxi)(Σyi), e (Σxi)² não é Σxi².

### Para fixar
- Medidas de posição: tendência central (média, mediana, moda) e separatrizes (mediana, quartis, decis, percentis).
- A mediana pertence aos dois grupos; quartis dividem a série em 4 partes, decis em 10 e percentis em 100, sempre com a mesma quantidade de elementos.
- Σ é a soma dos termos do índice inicial ao final; sem limites escritos, subentende-se de 1 a n.
- Soma dos produtos ≠ produto das somas; soma dos quadrados ≠ quadrado da soma.
- Σ k = k·n, em que n é o número de termos da soma.
- Σ k·xi = k·Σxi (a constante sai do somatório).
- Σ (xi ± yi) = Σxi ± Σyi; juntando as três regras: Σ(a·xi + b) = a·Σxi + b·n.

# SINTÉTICO

- **Média**: resume um conjunto de dados num único valor e permite comparar grupos; a forma de calcular muda conforme os dados vêm brutos, com frequências ou em classes.
- **Medidas de posição**: mostram onde os dados se concentram; dividem-se em tendência central (média, mediana, moda) e separatrizes (mediana, quartis, decis, percentis).
- **Separatrizes**: dividem a série ordenada em partes com o mesmo número de elementos: mediana em 2, quartis em 4, decis em 10, percentis em 100; a mediana é também medida de tendência central.
- **Somatório**: Σ xi com limites i = a até b soma os termos xi dessa faixa; se os limites são omitidos, vale de 1 até n; o termo geral pode ser uma expressão, como 2i + 1 ou xi².
- **Operações parecidas**: soma dos produtos Σ(xi·yi) difere do produto das somas (Σxi)(Σyi); o quadrado da soma (Σxi)² difere da soma dos quadrados Σxi².
- **Soma de constante**: Σ k = k·n, com n igual ao número de termos (limite superior − inferior + 1).
- **Constante em evidência**: Σ k·xi = k·Σxi; dobrar todos os valores dobra o total.
- **Soma e subtração**: Σ (xi ± yi) = Σxi ± Σyi; combinando as regras, Σ (a·xi + b) = a·Σxi + n·b.

# NOTAS

- Divergência com a fonte (pág. 8): o exemplo de Σ xi com i de 3 a 10, para a sequência 1 a 10, aparece com resultado 55. O valor correto é 3 + 4 + ... + 10 = 52 (55 menos x1 e x2). O resumo usa exemplos próprios e não repete o erro.
- Pág. 8: o exemplo Σ(2xk + 1) com k de 1 a 4 mistura xk com o termo 2k + 1 (a conta feita usa k = 1, 2, 3, 4, e não valores de x). No resumo foi tratado como termo geral 2k + 1.
- Pág. 3 e 5: há figuras (barras de notas e esquema das medidas de posição) cujo conteúdo foi descrito no texto; o esquema da pág. 5 lista média aritmética, geométrica e harmônica, mediana e moda sem definições neste trecho.
