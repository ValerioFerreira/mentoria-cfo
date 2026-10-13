---
id: S0418
agente: CLAUDE-L4
materia: Estatística
aula: Aula 00 — Apresentação de Dados
trecho: estatistica/a00/s01
paginas_lidas: 5-18
---
# ANALÍTICO

Este trecho apresenta a base da Estatística: o que ela estuda, seus três ramos, os conceitos de população e amostra, a diferença entre os métodos experimental e estatístico, os tipos de dados e a classificação das variáveis. Quase tudo é cobrado como definição, então a precisão dos termos importa.

### O que é Estatística e como se divide

A palavra vem do latim *status* (Estado): na origem, os governos registravam população e riquezas para cobrar impostos e cuidar da segurança. Hoje, **Estatística** é o conjunto de técnicas para **coletar, organizar, analisar e interpretar dados**, apoiando decisões em várias áreas. Os programas de computador ampliaram muito seu alcance (planejamento de experimentos, testes de hipóteses, confiabilidade, modelos de previsão).

Ela costuma ser dividida em três ramos (alguns autores incluem o segundo dentro do terceiro):

| Ramo | Função | Pergunta que responde |
| --- | --- | --- |
| **Descritiva** (ou dedutiva) | Coletar, organizar, descrever e resumir os dados observados, em tabelas, gráficos e medidas (média, mínimo, máximo, desvio padrão) | "O que os dados mostram?" |
| **Probabilística** | Construir o modelo matemático que explica os fenômenos aleatórios, cujo resultado varia de uma observação para outra; mede a chance de cada evento | "Qual a chance de ocorrer?" |
| **Inferencial** (ou indutiva) | Analisar e interpretar os dados de uma amostra para fazer previsões e generalizações sobre a população, avaliando representatividade, significância e confiabilidade | "O que posso concluir sobre o todo?" |

> ⚠️ **Pegadinha:** uma questão que descreve "obtenção, organização, redução e representação de dados" está falando da Estatística **Descritiva**. Já "análise e interpretação com conclusões sobre a população" é a **Inferencial**. Termos como "coletora" ou "populacional" não nomeiam ramo algum.

### Conceitos iniciais: população, amostra e companhia

| Conceito | Definição | Observação importante |
| --- | --- | --- |
| **População** | Conjunto de **todos** os indivíduos, objetos ou elementos estudados, que têm uma ou mais características em comum | Pode ser finita (número limitado) ou infinita (ilimitado) |
| **Amostra** | **Subconjunto** da população, escolhido para análise | Precisa ser **representativa**; serve para generalizar ou inferir sobre a população |
| **Censo** (recenseamento) | Estudo de **todos** os elementos da população | Caro e demorado; por isso se recorre a amostras |
| **Amostragem** | **Processo** de seleção criteriosa dos elementos que serão investigados | Erros na seleção tornam o estudo tendencioso |
| **Parâmetro** | Descrição numérica de uma característica **da população** | Quase sempre desconhecido; é uma constante para aquela população |
| **Estatística** (ou estimador) | Medida numérica calculada a partir de uma **amostra** | Varia de uma amostra para outra; é usada para estimar o parâmetro |

Uma amostra representativa mantém, a menos de pequenas diferenças naturais do sorteio, as mesmas características básicas da população nas variáveis pesquisadas. Em uma pesquisa eleitoral, por exemplo, escolhem-se eleitores respeitando a proporção de sexo, idade, escolaridade e classe social do eleitorado.

> 💡 **Exemplo:** o percentual de moradores de uma cidade que usam transporte coletivo, medido entre todos os moradores, é um **parâmetro**. O percentual calculado numa amostra de 400 moradores é uma **estatística** e serve para estimar aquele parâmetro.

> ⚠️ **Pegadinha:** o censo exige **mais** observações que a amostra, pois abrange toda a população. Afirmar que a amostra exige mais entrevistas que o censo está errado. Outro erro comum: dizer que o parâmetro é "da amostra". Memorize: **parâmetro = população; estatística = amostra**.

### Método experimental × método estatístico

Para investigar um fenômeno há dois caminhos:

- **Método experimental**: mantêm-se **constantes** todas as causas (fatores), exceto uma, que é variada de propósito para observar o efeito dela.
- **Método estatístico**: usado quando não dá para manter os fatores constantes. Ele **admite e registra todas as variações** das causas presentes e tenta medir a influência de cada fator no resultado, buscando relações entre eles.

> 💡 **Exemplo:** para explicar a queda de vendas de uma loja de chocolates, não se consegue segurar fixos o fluxo de turistas, a temperatura, o preço do concorrente e o mês de férias. O caminho é registrar tudo e estudar como cada fator se relaciona com as vendas, ou seja, o método estatístico.

### Dados estatísticos

**Dados** são os valores resultantes da coleta, organizados em **variáveis** (a característica medida) e **observações** (os elementos da amostra ou população). Pelo número de observações registradas para cada indivíduo:

| Tipo | Quantas características por indivíduo | Exemplo |
| --- | --- | --- |
| **Univariados** | uma | só o peso |
| **Bivariados** | duas | peso e altura |
| **Multivariados** | mais de duas | peso, altura, sexo e idade |

Pela forma de apresentação:

- **Dados brutos** (tabela primitiva): estão como foram coletados, sem ordenação por tamanho. Dão pouca informação ao leitor.
- **Rol**: os mesmos dados colocados em ordem **crescente ou decrescente**. Facilita enxergar o menor e o maior valor.

> 💡 **Exemplo:** os tempos de estudo 40, 15, 30, 25 são dados brutos; em rol crescente ficam 15, 25, 30, 40, e já se vê que o mínimo é 15 e o máximo é 40.

### Variáveis estatísticas

**Variável** é a característica que se deseja investigar: o objeto da pesquisa. Se o interesse é saber quantas horas por dia os alunos estudam, a variável é "horas estudadas por dia". Ela se divide em dois grandes grupos.

| Grupo | Tipo | Como reconhecer | Exemplos |
| --- | --- | --- | --- |
| **Qualitativa** (categórica) | **Nominal** | categorias **sem** ordem natural | cor dos olhos, esporte praticado, estado civil |
| **Qualitativa** (categórica) | **Ordinal** | categorias que podem ser **ordenadas** | grau de instrução (fundamental, médio, superior), patente |
| **Quantitativa** | **Discreta** | valores de um conjunto finito ou enumerável, resultado de **contagem** (só fazem sentido valores inteiros) | número de leitos, número de filhos, idade em anos completos |
| **Quantitativa** | **Contínua** | valores num intervalo de números reais, resultado de **mensuração** (valores fracionários fazem sentido) | peso, altura, tempo, temperatura |

> ⚠️ **Pegadinha:** ter aparência de número não torna a variável quantitativa. O **CEP** é um código que apenas identifica uma localidade: é **qualitativa**. Já o valor de uma fatura é quantitativo. O teste é perguntar se faz sentido somar, comparar quantidades e calcular média.

> ⚠️ **Pegadinha:** as palavras "nominal" e "ordinal" pertencem às qualitativas; "discreta" e "contínua" pertencem às quantitativas. Alternativas que misturam os pares (por exemplo, "quantitativas: ordinal ou discreta") estão erradas. Uma variável que só assume dois valores, como R$ 70 ou R$ 0, é **discreta**, mesmo sendo dinheiro. Uma variável que vai de 0 a 3,10 assumindo qualquer valor do intervalo é quantitativa (contínua).

### Para fixar
- Estatística: coleta, organização, análise e interpretação de dados; três ramos: descritiva, probabilística e inferencial.
- Descritiva resume e descreve; probabilística modela o aleatório; inferencial generaliza da amostra para a população.
- População = todos os elementos; amostra = subconjunto representativo; censo = estudo de toda a população; amostragem = processo de seleção.
- Parâmetro descreve a população (constante, geralmente desconhecido); estatística descreve a amostra (muda de amostra para amostra).
- Método experimental mantém os fatores constantes menos um; o estatístico registra as variações de todos e busca a influência de cada um.
- Dados: univariados (1 característica), bivariados (2), multivariados (mais de 2); brutos não têm ordem, rol está ordenado.
- Qualitativas: nominal (sem ordem) e ordinal (com ordem). Quantitativas: discreta (contagem) e contínua (medida).
- Número que funciona como código (CEP, telefone) é qualitativo.

# SINTÉTICO

- **Ramos da Estatística**: a descritiva organiza e resume os dados observados; a probabilística constrói o modelo para fenômenos aleatórios; a inferencial usa a amostra para concluir sobre a população.
- **População × amostra**: população é o conjunto de todos os elementos estudados (finita ou infinita); amostra é um subconjunto que precisa ser representativo para permitir generalizar.
- **Censo e amostragem**: censo estuda toda a população e, por isso, é caro e demorado; amostragem é o processo de selecionar a amostra com critério, pois erro nessa etapa gera resultado tendencioso.
- **Parâmetro × estatística**: parâmetro descreve a população e quase nunca é conhecido; estatística é calculada na amostra, muda de amostra para amostra e estima o parâmetro.
- **Método experimental × estatístico**: o experimental mantém constantes todos os fatores menos um, que é variado; o estatístico é usado quando isso é impossível e registra as variações de todos os fatores para medir a influência de cada um.
- **Dados univariados, bivariados e multivariados**: dependem de quantas características são registradas por indivíduo (uma, duas ou mais de duas).
- **Dados brutos × rol**: brutos estão na ordem da coleta (tabela primitiva, pouco informativa); o rol os ordena de forma crescente ou decrescente e mostra de imediato mínimo e máximo.
- **Variáveis qualitativas**: expressam qualidades; são nominais quando as categorias não têm ordem (cor dos olhos) e ordinais quando podem ser ordenadas (escolaridade).
- **Variáveis quantitativas**: discretas resultam de contagem e assumem valores enumeráveis (número de leitos); contínuas resultam de medição e preenchem intervalos (altura, peso).
- **Pegadinha do código numérico**: CEP e outros códigos têm forma de número, mas só identificam; são qualitativos.

# NOTAS

nenhuma. Observações: a tabela com 50 tempos de estudo (dados brutos e rol) foi usada apenas como ilustração e não foi reproduzida; o exemplo do rol foi substituído por valores próprios. As figuras das questões do CESPE (histograma e tabela de estatísticas) não foram extraídas, mas não são necessárias ao conteúdo.
