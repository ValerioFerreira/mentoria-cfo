---
id: S0397
agente: CLAUDE-L4
materia: Estatística
aula: Aula 03 — Moda
trecho: estatistica/a03/s01
paginas_lidas: 3-12
---
# ANALÍTICO

A moda é a medida de posição (tendência central) que indica o valor de maior ocorrência num conjunto de observações. Este trecho ensina a identificá-la em três situações: dados não agrupados, dados agrupados por valores (sem classes) e dados agrupados em classes, neste último caso pelo método mais simples, a moda bruta.

### Conceito e classificação quanto ao número de modas

A moda (Mo) é o valor que mais se repete, isto é, o de maior frequência. O termo foi introduzido na estatística por Karl Pearson, em 1895, pela ideia de "o que está em evidência". É o único valor central que pode ser usado em **variáveis qualitativas nominais** (aquelas sem ordem, como cor, time ou cidade): a média e a mediana exigem números ou ordem, a moda só exige contagem.

Diferentemente da média e da mediana, a moda **pode não existir** e pode ser **mais de uma**. Por isso o conjunto é classificado assim:

| Classificação | Quando ocorre | Exemplo |
| --- | --- | --- |
| **Amodal** | todos os valores aparecem o mesmo número de vezes (nenhum se destaca) | {2, 4, 6, 8, 10} |
| **Unimodal** | um único valor tem a maior frequência | {3, 3, 3, 5, 5, 8}: Mo = 3 |
| **Bimodal** | dois valores empatam na maior frequência | {1, 1, 4, 4, 4, 7, 7, 7, 9}: Mo = 4 e Mo = 7 |
| **Plurimodal (multimodal)** | três ou mais valores empatam na maior frequência | {2, 2, 5, 5, 6, 6, 9}: Mo = 2, 5 e 6 |

Nos empates, a frequência dividida pelos valores precisa ser **maior** que a dos demais. No último exemplo, 2, 5 e 6 aparecem duas vezes cada um e o 9 aparece uma só.

> ⚠️ **Pegadinha:** a moda é o **valor** que mais aparece, e não a quantidade de vezes que ele aparece. Se o 22 aparece duas vezes e é o campeão, a moda é 22, e não 2. Uma banca costuma oferecer a frequência como alternativa errada.

### Dados não agrupados

Basta contar as repetições e apontar o valor (ou valores) de maior frequência. Não é necessário ordenar, embora ordenar ajude a contar.

> 💡 **Exemplo:** no conjunto {12, 15, 12, 20, 15, 12, 30}, o 12 aparece três vezes, o 15 duas e os demais uma. Logo, o conjunto é unimodal e Mo = 12. Já em {7, 9, 11, 13}, nenhum valor se repete: o conjunto é amodal e **não há moda**.

Se os valores vêm numa tabela com rótulos (dias, meses), o raciocínio é o mesmo: procure o número que mais se repete na linha dos valores e ignore os rótulos. Um valor alto que aparece uma única vez não é moda só por ser o maior.

### Dados agrupados sem intervalos de classe (por valores)

Aqui há uma tabela com cada valor (Xi) e a sua frequência absoluta (fi). A moda é o **valor Xi cuja frequência é a maior**.

> 💡 **Exemplo:** número de faltas de 40 alunos num bimestre, na tabela a seguir.

| Faltas (Xi) | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| Alunos (fi) | 6 | 11 | 17 | 4 | 2 |

A maior frequência é 17, associada a 2 faltas. Logo, **Mo = 2**. O 17 é só a frequência; a moda é o que está na linha dos valores.

Pontos de atenção:

- No gráfico de barras (frequências por valor), a moda corresponde à **barra mais alta**.
- A mesma ideia vale quando a tabela traz **frequências relativas**: o valor com maior frequência relativa é a moda, e empates geram mais de uma moda. Numa tabela em que os valores 0 e 4 têm 0,30 cada e os demais têm menos, o conjunto é bimodal, com Mo = 0 e Mo = 4. Escolher um terceiro valor "do meio" é o erro típico.
- Valores com frequência zero (por exemplo, nenhum aluno com 11 anos) podem aparecer na tabela, mas nunca serão moda.

### Dados agrupados em classes

Quando os dados estão em intervalos de classe com a **mesma amplitude**, a moda se localiza na classe de maior frequência, chamada **classe modal**. Um intervalo não revela o valor exato mais frequente, por isso a moda é estimada por fórmulas. Existem quatro métodos: **moda bruta**, **de Pearson**, **de Czuber** e **de King**. Este trecho trata do mais simples, a moda bruta.

**Moda bruta** = ponto médio da classe modal:

**Mo = (l_inf + l_sup) / 2**

em que l_inf e l_sup são os limites inferior e superior da classe modal.

Passo a passo:

1. identifique a classe de maior frequência (a classe modal);
2. anote seus limites inferior e superior;
3. calcule a média aritmética dos dois limites.

> 💡 **Exemplo resolvido:** tempo de deslocamento até o trabalho de 50 pessoas, na tabela a seguir.

| Classe (min) | 0 ⊢ 10 | 10 ⊢ 20 | 20 ⊢ 30 | 30 ⊢ 40 | 40 ⊢ 50 |
| --- | --- | --- | --- | --- | --- |
| fi | 6 | 14 | 18 | 8 | 4 |

A maior frequência é 18, logo a classe modal é 20 ⊢ 30 e **Mo bruta = (20 + 30) / 2 = 25 min**. Para fins de comparação, a média dessa distribuição usa os pontos médios (5, 15, 25, 35, 45): (5·6 + 15·14 + 25·18 + 35·8 + 45·4) / 50 = 1.150 / 50 = 23 min. Média e moda bruta são valores diferentes e podem aparecer juntas na mesma questão, como nos itens que pedem "a média e a moda bruta" de uma tabela de pesos.

> ⚠️ **Pegadinha:** a classe modal é decidida pela **frequência**, não pela posição. Não confunda com a classe que contém a mediana, nem tome o ponto médio da classe do meio da tabela. O símbolo ⊢ indica intervalo fechado à esquerda e aberto à direita: o limite superior não pertence à classe.

Observação de prova: a moda de dados agrupados em classes é pouco explorada nos concursos; o mais comum é cobrar a moda de listas e de tabelas por valores, o conceito (unimodal, bimodal, amodal) e a distinção entre moda, média e mediana.

### Para fixar

- Moda é o valor de maior frequência; é medida de posição e de tendência central.
- Pode não existir (amodal), ser única (unimodal), dupla (bimodal) ou múltipla (plurimodal).
- É a única medida central aplicável a variáveis qualitativas nominais.
- Em tabelas por valores, a moda é o Xi de maior fi (ou maior frequência relativa), nunca a frequência em si.
- Em classes de mesma amplitude, a classe modal é a de maior frequência.
- Moda bruta = (l_inf + l_sup) / 2 da classe modal.
- Pearson, Czuber e King são outros métodos de estimar a moda em classes.

# SINTÉTICO

- **Moda**: é o valor de maior frequência do conjunto; medida de posição e de tendência central, usada quando o valor mais comum é o que importa.
- **Classificação**: amodal (todos com a mesma frequência, sem moda), unimodal (uma moda), bimodal (duas) e plurimodal (três ou mais); o empate vale só se for na frequência máxima.
- **Variável qualitativa nominal**: a moda é a única medida de posição que se aplica, pois só exige contar ocorrências.
- **Dados não agrupados**: conte as repetições e aponte o valor mais frequente; sem repetição, não há moda.
- **Dados por valores**: a moda é o Xi da maior frequência absoluta (ou relativa), e não a frequência; no gráfico, é a barra mais alta; empates dão mais de uma moda.
- **Classe modal**: com classes de mesma amplitude, é a de maior frequência.
- **Moda bruta**: ponto médio da classe modal, Mo = (l_inf + l_sup) / 2; por exemplo, classe 30 ⊢ 40 resulta em 35.
- **Outros métodos**: Pearson, Czuber e King também estimam a moda em classes; a moda bruta é a forma mais simples.

# NOTAS

- Páginas 4 a 12 contêm, além da teoria, enunciados de questões; foi aproveitada apenas a teoria.
- O texto apenas cita os métodos de Pearson, Czuber e King em classes, sem detalhá-los neste intervalo (são tratados em trecho seguinte); por isso o resumo só os nomeia.
- A figura da página 8 (gráfico de barras das frequências) foi descartada: o texto já descreve que a barra mais alta corresponde à moda.
- No material, o conjunto amodal é definido como aquele em que "todos os elementos têm a mesma frequência"; o caso de um conjunto com um único valor repetido (por exemplo, {5, 5, 5}) não é discutido e foi evitado nos exemplos.
