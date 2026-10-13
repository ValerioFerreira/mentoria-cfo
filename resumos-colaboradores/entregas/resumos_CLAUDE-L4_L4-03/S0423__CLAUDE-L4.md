---
id: S0423
agente: CLAUDE-L4
materia: Estatística
aula: Aula 14 — Análise de Variância (ANOVA):
trecho: estatistica/a14/s02
paginas_lidas: 14-27
---
# ANALÍTICO

Este trecho completa o teste F da ANOVA de um fator: calcula os graus de liberdade e os quadrados médios, monta a estatística F e a tabela da ANOVA, explica como concluir (valor tabelado e p-valor) e mostra o caso de grupos com números diferentes de repetições. Traz ainda a estimativa do componente de variância, a ideia de blocos e os testes de comparações múltiplas.

### Graus de liberdade

Seja N o total de observações, k o número de tratamentos (grupos) e n o número de observações em cada tratamento (quando todos têm o mesmo n, N = k·n).

| Fonte | Graus de liberdade | Observação |
| --- | --- | --- |
| **Total** | GL total = N − 1 | |
| **Tratamento** (modelo, entre) | GL trat = k − 1 | número de grupos menos 1 |
| **Erro** (resíduo, dentro) | GL erro = k·(n − 1) = N − k | |

Os graus de liberdade se **somam**: GL total = GL trat + GL erro. Exemplo: com 3 tratamentos de 5 observações cada, N = 15, GL total = 14, GL trat = 2 e GL erro = 12 (e 2 + 12 = 14).

### Quadrado médio

Os graus de liberdade medem a quantidade de informação independente. Dividir a soma de quadrados (SQ) por seus graus de liberdade dá o **quadrado médio** (QM), uma espécie de "soma de quadrados por unidade de informação":

- QM trat = SQ trat ÷ GL trat
- QM erro = SQ erro ÷ GL erro

> 💡 **Exemplo:** se SQ trat = 30 com GL trat = 2 e SQ erro = 24 com GL erro = 12, então QM trat = 15 e QM erro = 2.

O quadrado médio do erro estima a **variância dos erros**: a variância do erro é o valor esperado de QM erro, e como esse valor esperado é desconhecido, usa-se o próprio QM erro como estimativa.

**Componente de variância do tratamento** (modelo de efeitos aleatórios): vale E(QM trat) = σ²erro + n·σ²trat. Substituindo as esperanças pelos quadrados médios observados:

σ²trat (estimado) = (QM trat − QM erro) ÷ n

> 💡 **Exemplo:** 4 tratamentos, 5 repetições, QM trat = 130 e QM erro = 30. A estimativa do componente é (130 − 30) ÷ 5 = 20. Note que o divisor é o número de **repetições** n, não o de tratamentos.

### Estatística F e a tabela da ANOVA

A estatística do teste divide o quadrado médio do tratamento pelo quadrado médio do erro:

F = QM trat ÷ QM erro

A tabela da ANOVA reúne tudo, e saber preenchê-la é muito cobrado:

| Fonte de variação | GL | Soma de quadrados | Quadrado médio | F |
| --- | --- | --- | --- | --- |
| Tratamento | k − 1 | SQ trat | SQ trat ÷ GL trat | QM trat ÷ QM erro |
| Erro | N − k | SQ erro | SQ erro ÷ GL erro | |
| Total | N − 1 | SQ total | | |

A linha **Total** é a soma das outras duas, tanto nos graus de liberdade quanto nas somas de quadrados. O quadrado médio é sempre SQ ÷ GL, e F resulta da divisão de um quadrado médio pelo outro (tratamento sobre erro).

**Interpretação intuitiva.** As hipóteses são H0: todas as médias são iguais, e H1: pelo menos uma média é diferente.
- **F pequeno** (QM trat não é muito maior que QM erro): a variação entre os grupos não supera a variação dentro dos grupos. As diferenças entre médias são atribuídas ao acaso; **não se rejeita H0**.
- **F grande** (QM trat bem maior que QM erro): a variação entre grupos domina; **rejeita-se H0** e conclui-se que há pelo menos uma média diferente, isto é, o fator influencia o resultado.

### Como concluir: valor tabelado

Sob H0, F segue a distribuição **F de Fisher-Snedecor**, razão de duas variáveis qui-quadrado, cada uma dividida pelos seus graus de liberdade. Ela tem dois parâmetros: v1 = **GL do numerador** (GL do tratamento) e v2 = **GL do denominador** (GL do erro). Há uma tabela para cada nível de significância α.

| Resultado | Decisão |
| --- | --- |
| F observado > F tabelado (α; v1; v2) | **Rejeita** H0 |
| F observado ≤ F tabelado | **Não rejeita** H0 |

> 💡 **Exemplo:** com 3 grupos de 5 observações, v1 = 2 e v2 = 12; para α = 5%, o valor tabelado é f(0,05; 2; 12) = 3,885. Se o F observado fosse 7,5 (QM trat 15 ÷ QM erro 2), como 7,5 > 3,885 rejeitaríamos H0. Se fosse F = 2, como 2 < 3,885, não rejeitaríamos, e a conclusão seria que o fator não tem influência significativa.

> ⚠️ **Pegadinha:** a **ordem** dos graus de liberdade importa. Se a tabela estiver com numerador e denominador trocados, usa-se P(F v1,v2 > f) = P(F v2,v1 < 1/f). Por exemplo, como P(F 2;12 > 3,885) = 0,05, tem-se P(F 12;2 < 1/3,885) = 0,05.

### Como concluir: p-valor

O **p-valor** é a probabilidade de obter um resultado tão ou mais extremo que o observado, **supondo H0 verdadeira**: mostra quão raro é o resultado se H0 for válida. P-valor baixo = resultado incomum, evidência contra H0; p-valor alto = resultado comum.

| Condição | Decisão |
| --- | --- |
| p-valor < α | rejeita H0; há evidência estatística (teste estatisticamente significante) |
| p-valor ≥ α | não rejeita H0; não há evidência estatística |

Com as tabelas de vários α dá para localizar o p-valor num intervalo. No exemplo de F = 2 (v1 = 2; v2 = 12): f(0,10) = 2,807 e f(0,25) = 1,56; como 1,56 < 2 < 2,807, o p-valor está **entre 10% e 25%**. Logo, não se rejeita H0 para α ≤ 10% e rejeita-se para α ≥ 25%.

> ⚠️ **Pegadinha:** a ANOVA diz **se** as médias são todas iguais, mas **não** diz quantas nem quais são diferentes. Para isso são necessários testes de comparações múltiplas.

### Blocos (mais de um fator)

Se, além do tratamento, outro fator pode influenciar o resultado (por exemplo, o turno dos alunos além do professor), as observações são separadas também por esse fator, chamado **bloco**. Então:
- SQ total = SQ trat + SQ bloco + SQ erro (e os graus de liberdade também se somam entre as três fontes);
- calculam-se **duas estatísticas F**: F trat = QM trat ÷ QM erro e F bloco = QM bloco ÷ QM erro;
- a decisão sobre a igualdade das médias dos tratamentos continua baseada em **F trat**; F bloco significativo só indica que o bloco é relevante.
Seu equivalente sem pressupostos de distribuição (não paramétrico) é o **teste de Friedman**, que trabalha com postos (ordenação).

> 💡 **Exemplo de leitura de quadro:** num quadro com GL trat = 3, SQ trat = 360, GL erro = 6 e SQ erro = 288: k = 3 + 1 = 4 tratamentos; QM trat = 360 ÷ 3 = 120; QM erro = 288 ÷ 6 = 48; F = 120 ÷ 48 = 2,5.

### Questão típica: achar a soma de quadrados a partir de F

Se F e a soma total são dados, use QM = SQ ÷ GL dos dois lados. Exemplo: 4 níveis e N = 25 dão GL trat = 3 e GL erro = 21; com F = 3,5, tem-se (SQ trat ÷ 3) = 3,5 · (SQ erro ÷ 21), logo SQ trat = 0,5 · SQ erro. A SQ do fator é **metade** da do resíduo, não o quádruplo. Com SQ total dada, usa-se SQ total = SQ trat + SQ erro para achar cada uma.

### Número distinto de repetições

Se os grupos têm tamanhos diferentes n1, n2, ..., nk (com N = soma dos ni), a ANOVA funciona com ajustes:
- SQ trat = Σ ni·(média do grupo i − média geral)², em que a média geral é a soma de todas as observações dividida por N;
- GL erro = Σ(ni − 1) = N − k (continua valendo N − k);
- SQ erro é a soma dos quadrados dos desvios de cada observação em relação à média do seu grupo;
- SQ total é a soma dos quadrados dos desvios de cada observação em relação à média geral, e continua igual a SQ trat + SQ erro;
- fórmula alternativa: SQ trat = Σ (total do grupo i)² ÷ ni − (soma de todos os valores)² ÷ N.

> 💡 **Exemplo:** grupo A com 6 e 8; B com 4 e 6; C com 2, 4, 4 e 6 (N = 8; soma geral 40; média geral 5). Médias: A = 7, B = 5, C = 4. SQ trat = 2·(7−5)² + 2·(5−5)² + 4·(4−5)² = 8 + 0 + 4 = 12. Pela fórmula alternativa: 14²/2 + 10²/2 + 16²/4 − 40²/8 = 98 + 50 + 64 − 200 = 12. SQ erro = 2 + 2 + 8 = 12 e SQ total = 24. GL: total 7, trat 2, erro 5. QM trat = 6, QM erro = 2,4, F = 2,5.

### Comparações múltiplas

Quando a ANOVA rejeita H0, usam-se testes de comparação entre **pares de médias**: **teste t**, **teste de Tukey** e **teste de Dunnett** (amplitudes múltiplas de Dunnett). Eles comparam a diferença entre as médias de cada par a um limite chamado **diferença mínima significativa (DMS)**, cujo cálculo usa o QM do erro. O teste t usa a tabela t de Student; os demais usam tabelas próprias de amplitudes estudentizadas. O teste de Tukey serve para saber **quais pares de médias** diferem; ele não verifica interação entre tratamentos.

### Para fixar
- GL total = N − 1; GL trat = k − 1; GL erro = N − k; GL total = GL trat + GL erro.
- QM = SQ ÷ GL; F = QM trat ÷ QM erro; a linha Total soma GL e SQ, mas não tem QM nem F.
- QM erro estima a variância dos erros; o componente do tratamento é (QM trat − QM erro) ÷ n.
- Rejeita-se H0 (médias iguais) quando F > F tabelado, com GL trat no numerador e GL erro no denominador.
- Pelo p-valor: rejeita-se H0 quando p-valor < α.
- A ANOVA não indica quais médias diferem; isso exige Tukey, Dunnett ou teste t.
- Com blocos há dois F (tratamento e bloco), e a decisão sobre as médias usa F trat; o equivalente não paramétrico é Friedman.
- Com repetições desiguais, SQ trat = Σ ni·(média i − média geral)² e GL erro continua N − k.

# SINTÉTICO

- **Graus de liberdade**: total = N − 1, tratamento = k − 1, erro = N − k (ou k·(n − 1)); total = tratamento + erro.
- **Quadrado médio**: soma de quadrados dividida pelos respectivos graus de liberdade; o QM do erro estima a variância dos erros.
- **Estatística F**: F = QM trat ÷ QM erro; F pequeno indica variação entre grupos semelhante à interna, F grande indica diferença real entre médias.
- **Tabela da ANOVA**: a linha Total soma GL e SQ das outras duas; os QM são SQ ÷ GL e F é a razão dos QM (só na linha do tratamento).
- **Componente de variância**: estimativa = (QM trat − QM erro) ÷ n, em que n é o número de repetições; por exemplo, (360 − 60) ÷ 4 = 75.
- **Decisão pelo valor tabelado**: usa-se a distribuição F de Fisher-Snedecor com GL trat no numerador e GL erro no denominador; rejeita H0 se F observado > F tabelado.
- **Decisão pelo p-valor**: p-valor é a probabilidade de resultado tão ou mais extremo supondo H0 verdadeira; rejeita H0 se p-valor < α.
- **Blocos**: SQ total = trat + bloco + erro, com dois F (trat e bloco) e decisão baseada em F trat; o equivalente não paramétrico é o de Friedman.
- **Repetições desiguais**: SQ trat = Σ ni·(média i − média geral)²; GL erro continua N − k e SQ total = SQ trat + SQ erro.
- **Comparações múltiplas**: a ANOVA não diz quais médias diferem; para isso usam-se teste t, Tukey ou Dunnett, comparando cada par à DMS.

# NOTAS

- No exemplo de repetições desiguais do material, a média do grupo B aparece escrita como "28/4 = 7" e a soma como 35; o correto é 35/5 = 7 (o resultado 7 está certo). Na SQ do tratamento, o termo do grupo B aparece como "4 × 0²" em vez de "5 × 0²" (valor zero, sem efeito no resultado).
- Na conclusão final desse exemplo (última página do trecho), o material compara F = 1,2 com f(0,25; 12; 2) = 1,56, reaproveitando os graus de liberdade do exemplo anterior; neste exemplo os graus corretos seriam 2 (numerador) e 8 (denominador). O resumo não reproduz essa conclusão e ensina apenas a regra geral.
- No quadro da questão de blocos (UFRN) as figuras não foram extraídas; usei apenas os valores citados no comentário (GL trat = 3, SQ trat = 360, GL erro = 6, SQ erro = 288).
- Os valores 3,885, 2,807 e 1,56 (tabela F com 2 e 12 graus de liberdade) vêm do texto e conferem com as tabelas usuais.
- Exemplos numéricos do resumo (30/24, 130/30, grupos A, B e C de 8 observações) são próprios.
