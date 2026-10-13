---
id: S0449
agente: CLAUDE-L4
materia: Estatística
aula: Aula 00 — Apresentação de Dados
trecho: estatistica/a00/s04
paginas_lidas: 42-53
---
# ANALÍTICO

Este trecho trata das representações gráficas de uma distribuição de frequências: gráfico de hastes, histograma, polígono de frequências, curva de frequências (com a fórmula do polimento) e ogiva. O ponto central é saber qual gráfico serve para qual tipo de dado e como cada um é construído.

### Qual gráfico para qual dado

| Gráfico | Dado representado | Característica principal |
| --- | --- | --- |
| Hastes (bastões) | não agrupado em classes, em geral discreto | uma haste por valor da variável |
| Histograma | agrupado em classes | retângulos colados, um por classe |
| Polígono de frequências | agrupado em classes | linha que liga os pontos médios do topo dos retângulos |
| Curva de frequências | agrupado em classes | polígono "alisado", sem cantos |
| Ogiva | frequências acumuladas | linha que liga os limites das classes às acumuladas |

### Gráfico de hastes (bastões)

Serve para dados que **não foram agrupados em classes**, o que costuma ocorrer com variáveis discretas. Como cada valor aparece individualmente, **não há perda de informação**: basta traçar, sobre cada valor da variável, uma haste com altura igual à frequência (absoluta ou relativa). Por isso é possível reconstruir a tabela a partir do gráfico e vice-versa.

> 💡 **Exemplo:** numa amostra em que o valor 0 aparece 4 vezes, o 1 aparece 10, o 2 aparece 25, o 3 aparece 15 e assim por diante, desenham-se hastes de alturas 4, 10, 25, 15... sobre os valores 0, 1, 2, 3...

### Histograma

É o gráfico para dados **agrupados em classes**. É formado por retângulos **contíguos** (sem separação) apoiados no eixo horizontal:

- o número de retângulos é igual ao **número de classes**;
- a **largura** de cada retângulo é a **amplitude** do intervalo de classe, e as bases coincidem com os limites da classe (o ponto médio da base coincide com o ponto médio da classe);
- a **altura** é proporcional à frequência da classe;
- a **área total** é proporcional à soma das frequências.

Como os elementos são representados pela classe e não individualmente, o histograma **perde informação** (não se sabe onde, dentro da classe, cada valor está).

> ⚠️ **Pegadinha:** o que distingue histograma de **gráfico de colunas** é a separação entre as barras. Colunas separadas e categorias (qualitativas) indicam gráfico de colunas; retângulos colados e classes numéricas indicam histograma. Um gráfico com barras separadas representando fundos de investimento, por exemplo, não é histograma, pelos dois motivos: há espaço entre as barras e os dados são categorias, não intervalos de classe.

A **poligonal característica** é o desenho que usa apenas o **contorno** do histograma (a linha que acompanha o topo dos retângulos).

### Densidade de frequência

Quando uma questão fala em histograma com "densidade", ela se refere a:

densidade de frequência = frequência relativa da classe ÷ amplitude da classe

Com isso, a altura "correta" de cada retângulo pode ser comparada mesmo entre classes de larguras diferentes. As provas costumam dar a densidade de uma classe, pedir o total de elementos e usar esse total em outra classe.

> 💡 **Exemplo próprio:** uma classe de amplitude 1.000 tem densidade 2×10⁻⁴ e contém 30 elementos. Frequência relativa = densidade × amplitude = 2×10⁻⁴ × 1.000 = 0,2. Como 30 elementos correspondem a 20% do total, o total é 30 ÷ 0,2 = 150. Em outra classe de amplitude 2.000 e densidade 1×10⁻⁴, a frequência relativa é 0,2 e o número de elementos é 0,2 × 150 = 30.

### Polígono de frequências

É um **gráfico em linha**, obtido ligando-se com segmentos de reta os **pontos médios das bases superiores** dos retângulos do histograma. Para que a linha "feche" no eixo, acrescentam-se **uma classe anterior à primeira e uma posterior à última, ambas com frequência zero**. Assim como o histograma, a área sob o polígono é proporcional à soma das frequências.

Para montar: calcule o ponto médio de cada classe (limite inferior + limite superior, dividido por 2) e marque o par (ponto médio, frequência). Na tabela de exemplo do assunto, a classe 85 a 100 tem ponto médio 92,5 e frequência 5; a classe fictícia 70 a 85 tem ponto médio 77,5 e frequência 0.

### Curva de frequências

Resulta do **polimento** do polígono: elimina-se a "quina" dos vértices, suavizando a linha. A ideia é que o polígono mostra o fenômeno **como foi observado**, enquanto a curva mostra a **tendência**, antecipando o comportamento da distribuição quando há muitos dados (com muitos dados a linha poligonal naturalmente tende a uma curva).

O polimento usa uma média ponderada de três classes vizinhas, com peso 2 na classe central:

**fc = (f anterior + 2 × f da classe + f posterior) ÷ 4**

- fc: frequência calculada (polida) da classe;
- f: frequência simples da classe; f anterior e f posterior: as das classes vizinhas.

> 💡 **Exemplo:** frequências sequenciais 0, 5, 5, 12, 10. Para a classe de frequência 5 (a segunda): fc = (0 + 2×5 + 5) ÷ 4 = 15 ÷ 4 = 3,75. Para a classe de frequência 12: fc = (5 + 2×12 + 10) ÷ 4 = 39 ÷ 4 = 9,75.

#### Formas características das curvas

| Forma | Descrição |
| --- | --- |
| Sino, simétrica | valores concentrados no centro, com as duas caudas iguais |
| Sino, assimétrica à direita | concentração central com cauda mais longa à direita |
| Sino, assimétrica à esquerda | concentração central com cauda mais longa à esquerda |
| J | ponto de máximo em uma extremidade (distribuição extremamente assimétrica) |
| J invertido | o máximo está na extremidade oposta à do J |
| U | máximos nas duas extremidades |

O nome da assimetria segue a **cauda** (o lado em que a curva se alonga), não o lado da concentração.

### Ogiva (polígono de frequências acumuladas)

A ogiva representa **frequências acumuladas**, crescentes ou decrescentes. Diferenças em relação ao polígono de frequências:

- no eixo horizontal vão os **extremos (limites) das classes**, e não os pontos médios;
- no eixo vertical vão as **frequências acumuladas**;
- também se considera uma classe anterior à primeira, com frequência nula.

> 💡 **Exemplo:** com frequências 5, 5, 12, 10, 7, 9, 2 nas classes de 85 a 190, de largura 15, as acumuladas são 5, 10, 22, 32, 39, 48, 50. A ogiva sobe de 0 (no limite inferior da primeira classe, 85) até 50 (no limite superior da última, 190).

### Como as questões cobram o tema

- **Ler o histograma:** some as alturas para achar o total e, para "percentual a partir de certo valor", some só as colunas pedidas e divida pelo total (por exemplo, 22 de 44 elementos dá 50%).
- **Densidade de frequência:** a conta é sempre densidade = (n da classe ÷ total) ÷ amplitude; isole o total na primeira classe e use-o na segunda.
- **Identificar o gráfico:** verifique se o dado é agrupado em classes (histograma) ou categórico/discreto (colunas ou hastes) e se as barras estão coladas ou separadas.

### Para fixar
- Hastes: dados não agrupados (discretos), sem perda de informação; histograma: dados agrupados em classes, com perda de informação.
- Histograma tem retângulos colados, um por classe; largura = amplitude, altura proporcional à frequência, área proporcional ao total.
- Barras separadas ou dados qualitativos indicam gráfico de colunas, nunca histograma.
- Polígono de frequências liga os pontos médios do topo dos retângulos e usa classes extras de frequência zero nas pontas.
- Curva de frequências: polimento com fc = (anterior + 2 × própria + posterior) ÷ 4; mostra a tendência, não o fenômeno observado.
- Formas: sino (simétrica ou assimétrica), J e J invertido, U.
- Ogiva usa os limites das classes e as frequências acumuladas; o polígono usa os pontos médios.
- Densidade de frequência = frequência relativa ÷ amplitude da classe.

# SINTÉTICO

- **Hastes × histograma**: hastes para dados não agrupados (discretos), sem perda de informação; histograma para dados agrupados em classes, com perda de informação.
- **Histograma**: retângulos colados, um por classe; largura igual à amplitude, altura proporcional à frequência e área proporcional ao total.
- **Histograma × colunas**: barras separadas ou dados em categorias formam gráfico de colunas; só o retângulo colado sobre classes numéricas é histograma.
- **Densidade de frequência**: frequência relativa dividida pela amplitude da classe; permite achar o total de elementos a partir de uma classe e aplicá-lo às demais.
- **Polígono de frequências**: liga os pontos médios do topo dos retângulos, com uma classe vazia antes da primeira e outra depois da última.
- **Poligonal característica**: usa apenas o contorno do histograma.
- **Curva de frequências**: polimento do polígono pela fórmula fc = (anterior + 2 × própria + posterior) ÷ 4; mostra a tendência da distribuição.
- **Formas das curvas**: sino (simétrica ou assimétrica à direita ou à esquerda), J, J invertido e U (máximos nas duas pontas).
- **Ogiva**: polígono das frequências acumuladas, desenhado sobre os limites das classes (e não sobre os pontos médios), podendo ser crescente ou decrescente.

# NOTAS

- Os gráficos do material (hastes, histograma, curvas, ogiva e o histograma da primeira questão) não foram extraídos como texto; usei apenas as tabelas e as descrições escritas. A questão sobre as notas da turma depende do gráfico, então usei só o método (somar as colunas e dividir pelo total).
- Página 45 do material: na tabela do polimento, o valor da classe 145 a 160 aparece como 8,75, mas (10 + 2×7 + 9) ÷ 4 = 8,25. Considerei o cálculo correto (8,25); não coloquei esse valor no resumo.
- Página 47: o texto cita ogiva "decrescente" sem detalhar a construção; no resumo não aprofundei esse caso.
