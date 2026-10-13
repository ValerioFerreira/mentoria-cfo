---
id: S0493
agente: CLAUDE-L4
materia: Estatística
aula: Aula 14 — Análise de Variância (ANOVA):
trecho: estatistica/a14/s01
paginas_lidas: 4-13
---
# ANALÍTICO

A análise de variância (ANOVA) de um fator é um teste de hipóteses para comparar as médias de três ou mais grupos. O trecho apresenta o objetivo, as hipóteses, os pressupostos, a alternativa não paramétrica (Kruskal-Wallis) e a decomposição das somas de quadrados, com os métodos de cálculo.

### Para que serve a ANOVA

A **ANOVA simples** (também chamada ANOVA de um fator ou *one-way*) verifica se as médias de **três ou mais grupos** são todas iguais ou se pelo menos uma difere de forma significativa. Para apenas **dois grupos**, usa-se o teste de comparação de duas populações (teste t).

> 💡 **Exemplo:** uma rede de lojas quer saber se o valor médio do ticket difere entre suas quatro filiais. Calcular as quatro médias não basta: é preciso um teste que diga se as diferenças podem ser mero acaso. Esse teste é a ANOVA.

Hipóteses (para k grupos):

- **H0**: μ1 = μ2 = ... = μk (todas as médias populacionais iguais);
- **H1**: existe pelo menos um par (i, j) com μi ≠ μj.

Rejeitar H0 só diz que **alguma** média difere; não indica qual.

A ideia por trás do nome: as médias são comparadas olhando como elas **variam**. Se a variação entre as médias dos grupos é do tamanho da variação casual esperada, nada indica diferença real; se é grande demais para ser acaso, há efeito.

#### Terminologia
- **Fator**: a característica estudada, que divide a população em grupos (ex.: o professor, o turno, o fornecedor).
- **Tratamento**: cada nível do fator (ex.: professor 1, 2, 3); cada grupo recebe um tratamento.
- **Resíduo (erro)**: a variação das observações **dentro** de cada grupo, atribuída a causas alheias ao fator. Também chamado erro experimental, erro aleatório ou componente estocástica do erro.

A ANOVA separa a variação em duas partes: **entre os grupos** (atribuída ao tratamento) e **dentro dos grupos** (atribuída ao erro).

### Pressupostos

Os erros devem satisfazer:

- **Independência**: os erros são independentes entre si;
- **Normalidade**: seguem distribuição normal com média zero;
- **Homoscedasticidade**: têm variância igual em todos os grupos.

Para isso, as observações devem ser independentes, normais e de variância constante. Como se supõe uma distribuição, o teste é **paramétrico**. O modelo linear usual escreve cada observação como yij = μ + αi + εij: uma média geral (μ), mais o efeito do nível i do fator (αi), mais um erro aleatório com distribuição N(0; σ²) (εij). Os termos μ e αi são parâmetros a **estimar**; as variâncias **não podem** mudar de nível para nível. Um tamanho mínimo de amostra (como 30) não é pressuposto da ANOVA.

> ⚠️ **Pegadinha:** conceitos como correlação, autocorrelação e tendenciosidade **não** são pressupostos da ANOVA; a autocorrelação dos erros é, na verdade, uma violação da independência. Para detectá-la, usam-se a análise gráfica dos erros e testes como Durbin-Watson e Breusch-Godfrey.

### Alternativa não paramétrica: Kruskal-Wallis

Se os pressupostos (normalidade e/ou variâncias iguais) não forem atendidos, usa-se o **teste de Kruskal-Wallis**:

- não exige normalidade nem homoscedasticidade;
- exige observações **independentes** e variável pelo menos em **escala ordinal** (que possa ser ordenada);
- é a extensão do teste de **Mann-Whitney** (Wilcoxon-Mann-Whitney, ou soma de postos de Wilcoxon), que compara 2 grupos e é a versão não paramétrica do teste t;
- ordena todas as observações, atribui **postos** (nos empates, a média dos postos) e compara as médias dos postos dos grupos (pseudo-medianas);
- os grupos podem ter **tamanhos diferentes**;
- calcula a estatística **H**, comparada com o valor crítico da distribuição **qui-quadrado** com **g − 1** graus de liberdade (g = número de grupos); H acima do crítico rejeita H0.

| Situação | Teste |
| --- | --- |
| 2 grupos, dados normais | teste t |
| 2 grupos, não paramétrico | Mann-Whitney |
| 3 ou mais grupos, normais e variâncias iguais | ANOVA |
| 3 ou mais grupos, sem normalidade ou com variâncias diferentes | Kruskal-Wallis |

### Decomposição da variação

Cada observação xij (j-ésima do grupo i) pode ser separada em duas diferenças, usando a média geral x̿ e a média do grupo x̄i:

**xij − x̿ = (x̄i − x̿) + (xij − x̄i)**

A primeira parcela, (x̄i − x̿), é o efeito do **tratamento**; a segunda, (xij − x̄i), é o **erro**.

### Soma de quadrados

Elevando ao quadrado e somando, vale a identidade fundamental:

**SQTotal = SQTrat + SQErro**

| Sigla (alternativas) | Significado | Fórmula |
| --- | --- | --- |
| SQTrat (SQEntre) | variação entre grupos, devida ao tratamento | n · Σ(x̄i − x̿)² |
| SQErro (SQDentro) | variação dentro dos grupos, devida ao erro | ΣΣ(xij − x̄i)² |
| SQTotal | variação total | ΣΣ(xij − x̿)² |

Aqui n é o número de observações por grupo (iguais em todos) e k o número de grupos. Há também **fórmulas de atalho**, com N = k·n:

- SQTrat = Σ(total do grupo i)²/n − (soma de todos os valores)²/N;
- SQTotal = soma dos quadrados de todos os valores − (soma de todos os valores)²/N;
- SQErro = SQTotal − SQTrat.

> 💡 **Exemplo resolvido (próprio):** três fornecedores com 4 medições cada. A: 5, 6, 7, 6 (soma 24, média 6). B: 8, 9, 7, 8 (soma 32, média 8). C: 4, 5, 3, 4 (soma 16, média 4). A soma geral é 72 e a média geral x̿ = 72/12 = 6.
> **SQTrat** = 4·[(6−6)² + (8−6)² + (4−6)²] = 4·8 = 32. Pelo atalho: (24² + 32² + 16²)/4 − 72²/12 = 1856/4 − 432 = 464 − 432 = 32.
> **SQErro** = A: 1+0+1+0 = 2; B: 0+1+1+0 = 2; C: 0+1+1+0 = 2; total 6.
> **SQTotal** = 38 (conferindo: soma dos quadrados dos valores, 470, menos 432, dá 38 = 32 + 6).

Outro exemplo numérico: com 3 professores e 5 alunos cada (médias 8, 7 e 6, média geral 7), obtêm-se SQTrat = 10, SQErro = 30 e SQTotal = 40.

> ⚠️ **Pegadinha:** a soma dos quadrados de tratamento é multiplicada por n (repetições por grupo). Esquecer esse fator é um erro comum. E, mesmo com as somas calculadas, o teste ainda não está concluído: falta comparar as variações de forma padronizada.

#### Próximo passo do teste
Para concluir o teste, divide-se cada soma de quadrados pelos graus de liberdade (k − 1 para tratamento, N − k para erro), obtendo os quadrados médios, e compara-se a razão QMTrat/QMErro com o valor crítico da distribuição F.

### Para fixar
- ANOVA de um fator compara médias de 3 ou mais grupos; com 2 grupos, usa-se o teste t.
- H0: todas as médias iguais; H1: pelo menos uma média diferente (não diz qual).
- Fator é a característica estudada; tratamentos são seus níveis; erro é a variação dentro dos grupos.
- Pressupostos sobre os erros: independência, normalidade (média 0) e variância constante (homoscedasticidade).
- Sem normalidade ou com variâncias diferentes, usa-se Kruskal-Wallis (g − 1 graus, qui-quadrado); Mann-Whitney é para 2 grupos.
- SQTotal = SQTrat (entre) + SQErro (dentro); SQTrat = n·Σ(média do grupo − média geral)².
- Atalho: SQTotal = Σx² − (Σx)²/N e SQTrat = Σ(total do grupo)²/n − (Σx)²/N.

# SINTÉTICO

- **Objetivo**: a ANOVA de um fator testa se três ou mais médias são iguais; para dois grupos, vale o teste t.
- **Hipóteses**: H0 afirma médias todas iguais; H1, que pelo menos uma difere (sem indicar qual).
- **Conceitos**: fator é a característica estudada, tratamento é cada nível dele e o erro é a variação dentro dos grupos.
- **Pressupostos**: erros independentes, normais com média zero e de variância igual (homoscedasticidade); por isso o teste é paramétrico.
- **Não são pressupostos**: amostra mínima de 30, autocorrelação ou tendenciosidade; a autocorrelação, aliás, viola a independência.
- **Kruskal-Wallis**: alternativa não paramétrica para 3 ou mais grupos, com dados em postos; estatística H comparada ao qui-quadrado com g − 1 graus.
- **Mann-Whitney**: versão não paramétrica do teste t, só para dois grupos.
- **Decomposição**: SQTotal = SQTrat + SQErro, separando variação entre grupos (tratamento) e dentro dos grupos (erro).
- **Fórmulas**: SQTrat = n·Σ(x̄i − x̿)², SQErro = ΣΣ(xij − x̄i)² e SQTotal = ΣΣ(xij − x̿)².
- **Atalhos**: SQTotal = Σx² − (Σx)²/N e SQTrat = Σ(total do grupo)²/n − (Σx)²/N, com SQErro = SQTotal − SQTrat.

# NOTAS

- Pág. 6: a lista de métodos para identificar autocorrelação cita "Teste t" ao lado de Durbin-Watson e Breusch-Godfrey; essa menção é incomum (o teste t não é o instrumento usual para isso), por isso omiti-a do resumo e mantive apenas Durbin-Watson, Breusch-Godfrey e a análise gráfica.
- Pág. 8–9: a questão EBSERH sobre turnos mistura "variâncias diferentes" com Kruskal-Wallis; segui a lógica do comentário (homoscedasticidade + normalidade leva à ANOVA).
- Acrescentado fora do trecho: o parágrafo "O que vem depois" (graus de liberdade k − 1 e N − k, quadrados médios e razão F), conhecimento estável que o trecho apenas anuncia (termina em "ainda não acabamos o teste"); e o exemplo resolvido, com números próprios, que confere pelos dois métodos.
- Pág. 12 e 13: tabelas de diferenças extraídas em colunas; conferi que as somas (30, 40, 775, 735) fecham com os dados da tabela da pág. 11. O aviso de que as fórmulas valem para grupos de tamanhos iguais (n por grupo) é a leitura do trecho.
