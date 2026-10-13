---
id: S0446
agente: CLAUDE-L4
materia: Estatística
aula: Aula 02 — Medidas Separatrizes ou Quantis
trecho: estatistica/a02/s06
paginas_lidas: 67-78
---
# ANALÍTICO

O box plot (diagrama de caixa, ou box-and-whisker plot) é um gráfico da análise exploratória que resume um conjunto de dados em cinco números e destaca os valores discrepantes. O trecho ensina o que cada parte do desenho representa, como calcular os cinco números, como identificar outliers e como ler o gráfico nas questões.

### O que o box plot mostra

O gráfico resume cinco medidas: **mínimo, primeiro quartil (Q1), mediana (Q2), terceiro quartil (Q3) e máximo**. Ele permite visualizar a distribuição, a dispersão, a simetria aproximada e o quão afastados da maioria estão os valores extremos. Não mostra a média: itens que dizem que o box plot informa "valores médios" ou que a caixa é feita com Q1 e Q2 estão errados.

Partes do desenho (horizontal ou vertical):

- **Haste**: linha de apoio; começa no menor valor e termina no maior valor (sem outliers).
- **Caixa (box)**: retângulo que vai de **Q1 a Q3**. Contém cerca de **50% dos dados**.
- **Linha dentro da caixa**: a **mediana** (Q2). Ela pode ficar entre Q1 e Q3 ou coincidir com um deles ou com ambos.
- **Bigodes (whiskers)**: traços que ligam a caixa aos extremos. Cada um abriga cerca de **25% dos dados**.
- **Pontos ou asteriscos**: valores discrepantes (outliers), quando existem.

Em resumo, o gráfico divide os dados em quatro partes com cerca de 25% cada: do mínimo a Q1, de Q1 à mediana, da mediana a Q3 e de Q3 ao máximo. Questões de leitura exploram isso: "metade dos dados está entre Q1 e Q3"; "25% dos valores ficam entre o mínimo e Q1"; "50% estão acima da mediana".

> ⚠️ **Pegadinha (quantidade de elementos):** o box plot mostra proporções (quartis), não quantidades. Não dá para afirmar que um grupo tem mais elementos que outro apenas olhando duas caixas. Também não dá para concluir que "mais da metade" dos dados está nas duas pontas de uma caixa: as duas partes extremas somam cerca de 50%, exatamente metade, e não mais.

### Distância interquartílica e outliers

A **distância interquartílica** (amplitude ou intervalo interquartílico) é **DIQ = Q3 − Q1**: o comprimento da caixa.

Quando o gráfico marca outliers, os bigodes não chegam necessariamente ao mínimo e ao máximo: eles ficam limitados a **1,5 × DIQ** além da caixa. Os limites são:

- **limite inferior = Q1 − 1,5 × DIQ**
- **limite superior = Q3 + 1,5 × DIQ**

Valores **abaixo do limite inferior** ou **acima do limite superior** são **valores discrepantes (outliers)** e aparecem como pontos ou asteriscos. Os extremos da haste passam a ser:

- à esquerda, o **menor valor que não fica abaixo do limite inferior**;
- à direita, o **maior valor que não ultrapassa o limite superior**.

Assim, um valor exatamente igual ao limite não é outlier (ele ainda pode ser a ponta do bigode).

> ⚠️ **Pegadinha (DIQ × desvio quartílico):** as fórmulas são parecidas. **DIQ = Q3 − Q1**; o **desvio quartílico** (amplitude semi-interquartílica) é **Dq = (Q3 − Q1)/2**, ou seja, metade da DIQ. O 1,5 do critério de outliers multiplica a DIQ inteira.

### Passo a passo da construção

1. Ordene os dados.
2. Mínimo e máximo: primeiro e último valor.
3. **Posição dos quartis** (convenção do trecho): posição de Q1 = n/4; de Q3 = 3n/4. Se o resultado for inteiro, o quartil é o valor naquela posição; se for fracionário, use o valor da posição mais próxima. A mediana é o termo central (n ímpar) ou a média dos dois centrais (n par).
4. DIQ = Q3 − Q1.
5. Calcule os limites inferior e superior (com 1,5 × DIQ).
6. Identifique os outliers (fora dos limites) e defina as pontas dos bigodes com os valores extremos não discrepantes.
7. Desenhe a caixa de Q1 a Q3, a linha da mediana, os bigodes e os pontos dos outliers.

> 💡 **Exemplo:** 20 valores ordenados: 12, 14, 15, 15, 16, 17, 18, 18, 19, 20, 20, 21, 22, 22, 23, 24, 25, 26, 27, 45. Q1: posição 20/4 = 5, valor 16. Mediana: média das posições 10 e 11, que valem 20 e 20, logo 20. Q3: posição 15, valor 23. DIQ = 23 − 16 = 7. Limites: 16 − 10,5 = 5,5 e 23 + 10,5 = 33,5. O 45 está acima de 33,5, portanto é **outlier**. O mínimo 12 está acima de 5,5 e é a ponta esquerda; a ponta direita do bigode é **27** (maior valor que não passa de 33,5).

> 💡 **Exemplo (só os quartis):** Q1 = 40 e Q3 = 52. DIQ = 12 e os limites são 40 − 18 = 22 e 52 + 18 = 70. Os valores 30, 66 e 71 são analisados: 30 e 66 estão dentro; **71 é outlier**, pois passa de 70. Esse é o formato típico de questão: dados os quartis e alguns valores, testar quais ficam fora dos limites.

### Casos em que o desenho muda

Quando duas ou mais medidas coincidem, o desenho perde partes:

- Se **Q1 = mínimo**, não aparece bigode à esquerda da caixa.
- Se **Q3 = máximo**, não aparece bigode à direita.
- Se a **mediana coincide com Q1 ou Q3**, a linha da mediana se sobrepõe à borda da caixa, e a caixa mostra menos linhas.

> 💡 **Exemplo:** {4, 4, 4, 6, 8, 8, 8, 12}: n = 8; Q1 está na posição 2 (valor 4, igual ao mínimo); a mediana é (6 + 8)/2 = 7; Q3 está na posição 6 (valor 8). Resultado: a caixa vai de 4 a 8, sem bigode à esquerda, e o bigode da direita chega ao 12 (o limite superior é 8 + 1,5 × 4 = 14).

### Comparação e leitura de box plots

Pode-se desenhar várias caixas no mesmo eixo para **comparar grupos**. A leitura direta permite comparar medianas, DIQ (tamanho das caixas), amplitude (hastes) e presença de outliers. Ao comparar DIQ de dois grupos, subtraia Q3 − Q1 de cada um; caixas de mesmo comprimento têm a mesma DIQ, mesmo que estejam em posições diferentes. Quando a mediana não fica no meio da caixa ou os bigodes têm comprimentos diferentes, a distribuição não é simétrica.

Para itens com razões do tipo "o menor valor do grupo B é 37,5% da mediana de A", leia os valores no eixo e faça a divisão; para "diferença entre medianas equivale a x% do menor valor", calcule diferença ÷ menor valor.

### Para fixar
- Box plot resume cinco números: mínimo, Q1, mediana, Q3 e máximo. Não mostra a média nem o número de elementos.
- A caixa vai de Q1 a Q3 e contém cerca de 50% dos dados; cada bigode tem cerca de 25%.
- DIQ = Q3 − Q1; desvio quartílico = DIQ/2.
- Outlier: valor menor que Q1 − 1,5 × DIQ ou maior que Q3 + 1,5 × DIQ; é marcado por ponto ou asterisco.
- Pontas dos bigodes com outliers: menor e maior valores que ainda estão dentro dos limites (valor igual ao limite não é outlier).
- Posição dos quartis (convenção do trecho): n/4 e 3n/4; mediana: termo central ou média dos dois centrais.
- Medidas iguais (por exemplo Q1 = mínimo) eliminam partes do desenho.
- Vários box plots no mesmo eixo permitem comparar medianas, DIQ e outliers.

# SINTÉTICO

- **Cinco números**: o box plot resume mínimo, Q1, mediana, Q3 e máximo; não informa média nem a quantidade de elementos.
- **Caixa e bigodes**: a caixa vai de Q1 a Q3 (cerca de 50% dos dados) com a mediana marcada dentro; cada bigode abriga cerca de 25% dos dados.
- **DIQ**: distância interquartílica = Q3 − Q1, o comprimento da caixa; não confundir com o desvio quartílico, que vale (Q3 − Q1)/2.
- **Limites dos outliers**: inferior = Q1 − 1,5 × DIQ e superior = Q3 + 1,5 × DIQ; valores fora desses limites são discrepantes (pontos ou asteriscos).
- **Pontas dos bigodes**: com outliers, vão até o menor valor não menor que o limite inferior e o maior valor não maior que o limite superior; valor igual ao limite não é outlier.
- **Quartis na prática**: posição n/4 para Q1 e 3n/4 para Q3 (valor da posição mais próxima se a conta não for inteira); mediana pelo termo central ou média dos dois centrais.
- **Coincidências**: se Q1 = mínimo some o bigode esquerdo; se Q3 = máximo some o direito; se a mediana coincide com um quartil, as linhas se sobrepõem.
- **Questões de leitura**: o gráfico mostra proporções, então não se pode comparar o número de elementos de dois grupos; as duas pontas somam 50%, não mais.
- **Comparação**: várias caixas no mesmo eixo permitem comparar medianas, DIQ e outliers.

# NOTAS

- Os gráficos de box plot das páginas 68, 70, 72, 73, 74 (página sem texto), 75 e 77 não foram extraídos; os valores lidos nos desenhos pelos comentários das questões (ex.: Q1 = 10, mediana 20, medianas 8 e 7) foram usados só para entender os tipos de pergunta, e escrevi exemplos próprios.
- O material adota, para os quartis, o método de posição n/4 e 3n/4 com valor da posição mais próxima; outros métodos de cálculo (interpolação) podem dar quartis ligeiramente diferentes. Registrei apenas a convenção do trecho.
- Página 67 diz que os bigodes ficam "limitados a 1,5 × DIQ" quando há outliers; entendi como limite medido a partir de Q1 e Q3, como detalhado na página 68.
- A observação de que mediana fora do centro da caixa indica assimetria é conhecimento geral de leitura do gráfico e não está literalmente no trecho.
