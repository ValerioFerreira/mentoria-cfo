---
id: S0403
agente: CLAUDE-L4
materia: Estatística
aula: Aula 04 — Medidas de Variabilidade ou Dispersão
trecho: estatistica/a04/s01
paginas_lidas: 3-16
---
# ANALÍTICO

As medidas de dispersão (ou variabilidade) mostram o quanto os dados diferem entre si. Este trecho apresenta o conceito, a classificação das medidas e as duas mais simples: a amplitude total e a amplitude interquartílica, com cálculo, limitações e propriedades.

### Por que medir a dispersão

Média, mediana e moda resumem onde os dados se concentram, mas não dizem se eles são parecidos ou muito diferentes entre si. Veja três grupos de cinco notas:

| Grupo | Notas | Média |
| --- | --- | --- |
| G1 | 6, 6, 6, 6, 6 | 6 |
| G2 | 4, 5, 6, 7, 8 | 6 |
| G3 | 1, 2, 6, 10, 11 | 6 |

Têm a mesma média, mas G1 é totalmente homogêneo e G3 é o mais heterogêneo. As **medidas de dispersão** quantificam essa diferença: quanto maior o valor da medida, maior a dispersão.

### Classificação das medidas

| Tipo | Medidas |
| --- | --- |
| **Dispersão absoluta** | amplitude total, amplitude interquartílica, desvio médio, variância, desvio-padrão |
| **Dispersão relativa** | coeficiente de variação (de Pearson), variância relativa |

> ⚠️ **Pegadinha:** média, mediana e moda são medidas de **posição** (tendência central), e quartis, decis e percentis são **separatrizes**; nenhuma delas é medida de dispersão. Já a variância e o coeficiente de variação são dispersão. Questões pedem para separar esses grupos.

### Amplitude total (AT)

É a diferença entre o maior e o menor valor do conjunto:

**AT = x_máx − x_mín**

É simples e rápida, mas **instável**, porque só considera os extremos e ignora os valores intermediários. Um único valor discrepante a altera muito. Ela também tende a **crescer com o tamanho da amostra** e varia bastante de uma amostra para outra, ainda que sejam da mesma população.

> 💡 **Exemplo:** A = {10, 12, 14, 16, 18, 20, 50} e B = {17, 18, 19, 20, 21, 22, 23} têm média 20. Mas AT(A) = 50 − 10 = 40 e AT(B) = 23 − 17 = 6. O valor 50 sozinho estica a amplitude de A, embora a maioria dos seus dados esteja entre 10 e 20.

Ela é útil quando se quer uma visão rápida (por exemplo, a variação de temperatura em um dia) e não há necessidade de precisão. Amplitude 0 indica que todos os valores são iguais (dispersão nula).

#### Cálculo conforme a organização dos dados

- **Dados não agrupados:** maior menos menor valor.
- **Agrupados por valores (sem classes):** o mesmo, lendo na tabela o menor e o maior Xi, **sem olhar as frequências**. Se a tabela traz os valores 2, 4, 6, 8 com frequências 30, 5, 5, 1, a amplitude é 8 − 2 = 6; o fato de 8 ser raro não importa.
- **Agrupados em classes:** há duas formas:
  1. **l_sup da última classe − l_inf da primeira**;
  2. **PM da última classe − PM da primeira**.

> 💡 **Exemplo:** classes 2 ⊢ 6, 6 ⊢ 10, 10 ⊢ 14 e 14 ⊢ 18 (pontos médios 4, 8, 12 e 16). Pela forma 1: 18 − 2 = 16. Pela forma 2: 16 − 4 = 12. A forma 2 é menor porque desconsidera os extremos das classes (a diferença é a própria amplitude de classe, 4).

### Propriedades da amplitude total

1. **Somar ou subtrair uma constante c** de todos os valores **não altera** a amplitude: o conjunto só se desloca.
2. **Multiplicar ou dividir** todos os valores por uma constante c **multiplica ou divide a amplitude por c** (com c negativo, vale o módulo, pois a amplitude nunca é negativa).

> 💡 **Exemplo:** {2, 5, 9} tem AT = 7. Somando 3: {5, 8, 12}, AT = 7. Multiplicando o original por 4: {8, 20, 36}, AT = 28.

### Amplitude interquartílica

Os **quartis** dividem o conjunto ordenado em quatro partes com a mesma quantidade de dados (25% cada):

- **Q1:** deixa 25% dos dados abaixo dele e 75% acima;
- **Q2:** deixa 50% abaixo e 50% acima; coincide com a **mediana** (Q2 = Md);
- **Q3:** deixa 75% abaixo e 25% acima.

A **amplitude interquartílica** (ou distância ou intervalo interquartílico, AIQ ou DIQ) é a diferença entre o terceiro e o primeiro quartil, e abrange os 50% centrais dos dados:

**AIQ = Q3 − Q1**

A **amplitude semi-interquartílica** (ou **desvio quartílico**, DQ) é a **metade** dela:

**DQ = (Q3 − Q1) / 2**

> ⚠️ **Pegadinha:** as duas fórmulas são parecidas e é fácil trocar: a interquartílica é Q3 − Q1 inteira; o desvio quartílico divide por 2. Na questão em que se afirma que Q3 é a própria mediana, o item é falso: a mediana é Q2.

> 💡 **Exemplo:** {2, 4, 6, 8, 10, 12, 14}: a mediana é 8; a metade inferior {2, 4, 6} dá Q1 = 4 e a superior {10, 12, 14} dá Q3 = 12. Logo, AIQ = 12 − 4 = 8 e DQ = 4.

Como se baseia nos quartis, a AIQ não é afetada por valores extremos, ao contrário da amplitude total.

#### Propriedades da amplitude interquartílica

São as **mesmas da amplitude total**, valendo também para o desvio quartílico:

- somar ou subtrair uma constante **não altera** a AIQ;
- multiplicar ou dividir por uma constante **multiplica ou divide** a AIQ por essa constante.

No exemplo anterior, somando 5 a cada valor, obtêm-se Q1 = 9 e Q3 = 17, e a AIQ continua 8; multiplicando por 3, Q1 = 12, Q3 = 36 e a AIQ passa a 24.

### Para fixar

- Medidas de dispersão mostram a variação dos dados; média, mediana e moda são de posição.
- Absolutas: amplitude total, interquartílica, desvio médio, variância e desvio-padrão; relativas: coeficiente de variação e variância relativa.
- AT = x_máx − x_mín; é instável, sensível a valores extremos e ao tamanho da amostra.
- Em dados por valores, a amplitude ignora as frequências; em classes, usa-se l_sup final − l_inf inicial ou a diferença dos pontos médios extremos.
- Soma ou subtração de constante não muda a amplitude; multiplicação ou divisão altera na mesma proporção.
- AIQ = Q3 − Q1; DQ = (Q3 − Q1)/2; Q2 é a mediana.
- AIQ e DQ têm as mesmas propriedades da amplitude total.

# SINTÉTICO

- **Dispersão**: mede o quanto os dados variam entre si; conjuntos com a mesma média podem ter dispersões bem diferentes.
- **Classificação**: absolutas (amplitude total, interquartílica, desvio médio, variância, desvio-padrão) e relativas (coeficiente de variação e variância relativa); média, mediana e moda não são dispersão.
- **Amplitude total**: AT = x_máx − x_mín; simples, mas instável, pois usa só os extremos e cresce com o tamanho da amostra.
- **Dados por valores**: pegam-se o menor e o maior Xi, sem considerar as frequências.
- **Dados em classes**: AT = l_sup da última − l_inf da primeira, ou PM da última − PM da primeira (que resulta menor).
- **Propriedades da AT**: soma ou subtração de constante não a altera; multiplicação ou divisão a multiplica ou divide pela constante.
- **Amplitude interquartílica**: AIQ = Q3 − Q1 (50% centrais); o desvio quartílico é a metade: (Q3 − Q1)/2; Q2 é a mediana.
- **Propriedades da AIQ**: as mesmas da AT, também para o desvio quartílico.

# NOTAS

- Páginas 4, 5, 10, 14 e 15 trazem questões comentadas; só a teoria foi aproveitada.
- Nas figuras do trecho (página 13, quartis) o conteúdo está descrito no texto, e as figuras foram descartadas. As caixas das propriedades (páginas 11, 12, 15 e 16) são texto e foram aproveitadas.
- O material fala da AT em dados agrupados em classes por duas fórmulas (limites e pontos médios) e diz que a segunda resulta menor; a observação de que a diferença é exatamente h, e a ressalva sobre constante negativa, foram acrescentadas por dedução matemática (não constam no trecho). A frase sobre a AIQ não ser afetada por extremos também é consequência de usar quartis.
- O método de cálculo dos quartis usado nos exemplos (mediana das metades) é o do material para sequências ímpares simples; não há discussão de outros métodos no trecho.
