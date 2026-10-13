---
id: S0537
agente: CLAUDE-L4
materia: Estatística
aula: Aula 00 — Apresentação de Dados
trecho: estatistica/a00/s02
paginas_lidas: 19-26
---
# ANALÍTICO

Uma série estatística organiza dados em torno de uma característica comum e os apresenta em tabela ou gráfico. O trecho mostra as partes de uma tabela, os tipos de série (temporal, geográfica, específica e mista) e a construção de uma distribuição de frequências, pontual ou por intervalos de classe.

### Série estatística, tabela e gráfico

Uma **série estatística** é um conjunto de dados ligado a uma mesma variável, apresentado de forma a facilitar a leitura. Os dois formatos usuais são a tabela e o gráfico.

**Partes da tabela:**

| Parte | O que é |
| --- | --- |
| Título | identifica o conteúdo da tabela |
| Cabeçalho | parte superior que diz o que há em cada coluna |
| Coluna indicadora | indica o conteúdo de cada linha |
| Corpo | conjunto de linhas e colunas com os dados da variável |
| Linhas | traços que ajudam a leitura |
| Célula | espaço onde fica cada dado |
| Fonte | origem dos dados, colocada no rodapé |

O **gráfico** serve para dar compreensão rápida do fenômeno. Para isso precisa ser **simples** (sem detalhes irrelevantes), **claro** (permite interpretar corretamente os valores) e **verossímil** (transmite a verdade sobre o fenômeno).

### Os três elementos e a classificação das séries

Toda série traz três elementos: **tempo** (época), **espaço** (local) e **espécie** (o fato ou fenômeno). A série se classifica conforme o elemento que **varia**, enquanto os outros dois ficam constantes.

| Série | Sinônimos | O que varia | O que fica constante |
| --- | --- | --- | --- |
| Temporal | cronológica, histórica, evolutiva | tempo | fato e local |
| Geográfica | territorial, espacial, de localização | local | fato e tempo |
| Específica | categórica | fato (categoria) | tempo e local |

> 💡 **Exemplo próprio:** número de matrículas em uma escola de 2018 a 2023 é **temporal** (só o ano varia). Matrículas em 2023 nos cinco bairros da cidade é **geográfica** (só o bairro varia). Matrículas em 2023, nessa escola, por turno (manhã, tarde, noite) é **específica** (só a categoria varia).

> ⚠️ **Pegadinha:** para classificar, pergunte "o que muda de linha para linha?". Se a coluna indicadora lista anos, é temporal; se lista regiões, geográfica; se lista categorias (sexo, zona, tipo), específica.

### Séries mistas (compostas)

Quando se precisa mostrar mais de uma variável em uma só tabela, combinam-se duas ou mais séries, formando uma **série mista (ou composta)**, apresentada em **tabela de dupla entrada** (linhas × colunas). O nome da nova série leva em conta pelo menos dois elementos:

- **específico-temporal**: fato e tempo (por exemplo, número de homens e de mulheres a cada ano);
- **geográfico-temporal**: local e tempo (por exemplo, população de cada região a cada ano).

Também é possível, em tese, ter séries com três ou mais entradas, mas são raras pela dificuldade de representação.

### Dados brutos, rol e frequência

Logo após a coleta, os dados estão **brutos**: na ordem em que foram obtidos, sem organização, e informam pouco. O primeiro passo é ordená-los em **rol** (ordem crescente ou decrescente). Do rol já se lê o menor e o maior valor e a **amplitude total**:

**AT = valor máximo − valor mínimo**

O rol também revela quais valores se repetem. O número de vezes que um valor aparece é sua **frequência**, e a tabela que reúne os valores com suas frequências é a **distribuição de frequências**. Ela é, ela própria, uma série estatística em que **fato, local e época são constantes** (só o valor da variável muda).

> 💡 **Exemplo próprio:** idades de 8 pessoas: 31, 25, 25, 40, 31, 25, 52, 40. Rol: 25, 25, 25, 31, 31, 40, 40, 52. Amplitude total = 52 − 25 = 27. Distribuição pontual: 25 (3), 31 (2), 40 (2), 52 (1); soma das frequências = 8.

### Distribuição pontual × intervalar

| Tipo | Como apresenta | Vantagem | Desvantagem |
| --- | --- | --- | --- |
| **Pontual (discreta)** | cada valor observado com sua frequência | não perde nenhum dado | ocupa muito espaço quando há muitos valores distintos |
| **Intervalar (contínua)** | classes (intervalos) com a frequência de cada uma | resume bem, ideal para variável contínua | perde o detalhe de cada observação |

Na intervalar, cada valor é alocado na classe a que pertence e se lê o padrão global (onde há mais e menos casos). É o formato mais comum, porque a estatística busca visão geral e não o detalhe de casos particulares.

> 💡 **Exemplo próprio:** 20 tempos de espera entre 0 e 20 minutos agrupados em 0 ≤ x < 5 (4), 5 ≤ x < 10 (9), 10 ≤ x < 15 (5) e 15 ≤ x < 20 (2): a soma das frequências (4 + 9 + 5 + 2) é 20, e a classe modal é a de 5 a 10.

### Notação dos intervalos de classe

Cada classe tem **limite inferior** e **limite superior**, e é preciso dizer se o extremo pertence à classe:

| Tipo | Notação | Significado |
| --- | --- | --- |
| Aberto | a < x < b | entre a e b, sem incluir a nem b |
| Fechado à esquerda, aberto à direita | a ≤ x < b | inclui a, não inclui b |
| Aberto à esquerda, fechado à direita | a < x ≤ b | inclui b, não inclui a |
| Fechado | a ≤ x ≤ b | inclui a e b |

O padrão em tabelas por classes é **fechado à esquerda e aberto à direita** (a ≤ x < b): um valor igual ao limite superior vai para a classe seguinte, o que evita contagem dupla. Assim, 100 pertence à classe 100 ≤ x < 115, e não à anterior.

### Para fixar
- Série estatística: dados de uma mesma variável organizados em tabela ou gráfico.
- Tabela: título, cabeçalho, coluna indicadora, corpo, linhas, células e fonte; gráfico: simples, claro e verossímil.
- Classifique pelo que varia: tempo (temporal), local (geográfica), fato (específica).
- Série mista = tabela de dupla entrada; nomeia-se pelos dois elementos (específico-temporal, geográfico-temporal).
- Dados brutos → rol → amplitude total (máximo − mínimo).
- Frequência é o número de ocorrências; a distribuição de frequências tem fato, local e época constantes.
- Pontual não perde dados; intervalar resume, mas perde o detalhe; classe típica: a ≤ x < b.

# SINTÉTICO

- **Série estatística**: conjunto de dados de uma mesma variável, apresentado em tabela (título, cabeçalho, coluna indicadora, corpo, células, fonte) ou gráfico (simples, claro e verossímil).
- **Série temporal**: só o tempo varia (fato e local fixos); também chamada cronológica, histórica ou evolutiva.
- **Série geográfica**: só o local varia (fato e tempo fixos); também territorial, espacial ou de localização.
- **Série específica**: só o fato (categoria) varia, com tempo e local fixos; também chamada categórica.
- **Série mista**: combina duas ou mais séries em tabela de dupla entrada, nomeada pelos elementos combinados (específico-temporal, geográfico-temporal).
- **Dados brutos e rol**: dados brutos estão sem ordem; o rol os ordena e permite ler mínimo, máximo e amplitude total (máximo − mínimo).
- **Distribuição de frequências**: tabela com cada valor e seu número de ocorrências; é série em que fato, local e época são constantes.
- **Pontual × intervalar**: a pontual lista todos os valores sem perdê-los, mas ocupa espaço; a intervalar agrupa em classes, simplifica e perde o detalhe individual.
- **Intervalos de classe**: a ≤ x < b inclui o limite inferior e exclui o superior (padrão); os demais tipos são aberto, fechado e aberto à esquerda e fechado à direita.

# NOTAS

Divergência no material: na tabela de exemplo da série específica (população urbana e rural de 2010), os valores listados para urbana e rural (93.134 e 119.011) parecem ser os de 1970 e 1980 da série temporal da mesma página; o total informado (190.755) é o de 2010 e não bate com a soma das duas linhas. O resumo usa exemplos próprios e não reproduz essa tabela. Figuras e tabelas numéricas de população do material foram descartadas por apenas ilustrarem a classificação. A tabela de 50 tempos de estudo, o rol e a distribuição pontual (págs. 24-25) foram usados só para explicar o método, sem copiar os dados.
