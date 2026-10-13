---
id: S0435
agente: CLAUDE-L4
materia: Estatística
aula: Aula 11 — Testes de Hipóteses
trecho: estatistica/a11/s06
paginas_lidas: 66-80
---
# ANALÍTICO

Este trecho trata de testes sobre variâncias e do p-valor. Primeiro o teste qui-quadrado para a variância de uma população, depois o teste F para comparar as variâncias de duas populações, e por fim o p-valor, a forma alternativa de decidir se H0 é rejeitada.

### Teste de hipóteses para a variância de uma população

Verifica-se se a variância σ² afirmada na hipótese nula é compatível com a variância amostral s² observada. Exige população normal. A ideia: o estimador s², multiplicado por (n − 1)/σ², segue a distribuição **qui-quadrado com n − 1 graus de liberdade**.

**χ² = (n − 1) · s² / σ²0**, em que n é o tamanho da amostra, s² a variância amostral (soma dos quadrados dos desvios dividida por **n − 1**) e σ²0 o valor dado em H0.

> 💡 **Exemplo:** H0: σ² = 8, amostra com n = 11 e s² = 12. A estatística é χ² = (10/8) · 12 = 15, com 10 graus de liberdade.

**Particularidade da qui-quadrado:** a distribuição é sempre positiva e **assimétrica**. Por isso o valor crítico inferior e o superior **não têm o mesmo módulo** (diferente do que ocorre na normal e na t). Cada um é buscado na tabela separadamente. A tabela costuma dar P(χ² < x) para cada número de graus de liberdade.

| Teste | Hipótese alternativa | Regra de rejeição |
| --- | --- | --- |
| Bilateral | H1: σ² ≠ σ²0 | χ² < χ²_inf **ou** χ² > χ²_sup, deixando α/2 em cada cauda |
| Unilateral à esquerda | H1: σ² < σ²0 | χ² < χ²_inf, com α na cauda esquerda |
| Unilateral à direita | H1: σ² > σ²0 | χ² > χ²_sup, com α na cauda direita |

Na tabela, o crítico **inferior** é o x tal que P(χ² < x) = α/2 (bilateral) ou α (esquerda); o **superior** é o x tal que P(χ² < x) = 1 − α/2 ou 1 − α. Por exemplo, para 4 graus de liberdade e α = 10% bilateral, a tabela dá P(χ² < 0,71) = 0,05 e P(χ² < 9,49) = 0,95. Logo H0 só é rejeitada se χ² < 0,71 ou χ² > 9,49. Uma estatística 6 (com 4 g.l.) cai no meio e **não rejeita** H0.

> 💡 **Exemplo (esquerda):** H0: σ² = 10 contra H1: σ² < 10, n = 21 e s² = 5. Estatística: (20/10) · 5 = 10, com 20 graus de liberdade. O crítico inferior a 5% é cerca de 10,85. Como 10 < 10,85, rejeita-se H0: há evidência de que a variância é menor que 10.

> ⚠️ **Pegadinha:** no teste unilateral à esquerda a rejeição ocorre para valores **pequenos** de χ² (abaixo do crítico inferior). Uma mesma estatística pode rejeitar H0 a 10% e não rejeitá-la a 5%, porque com α menor o crítico inferior fica mais baixo. Em alternativas de prova, confira sempre o nível de significância citado em cada uma.

Em questões com vários níveis de significância, o procedimento é: calcular a estatística uma única vez; ler, para cada α, o crítico apropriado (com os graus de liberdade n − 1); comparar. Quando o enunciado dá probabilidades do tipo P(4 < χ²10 < 18) = 0,90, os extremos 4 e 18 são, nessa ordem, os críticos inferior e superior de um teste bilateral a 10%.

### Comparação das variâncias de duas populações (teste F)

Também chamado de **teste de homogeneidade de variâncias**: compara as variâncias de duas populações normais **independentes**, A e B. Em geral H0 diz que são iguais.

- Bilateral: H0: σA² = σB² contra H1: σA² ≠ σB².
- Unilateral à direita: H1: σA² > σB².
- Unilateral à esquerda: H1: σA² < σB².

A estatística geral é F = (sA²/σA²) / (sB²/σB²). Sob H0 as variâncias populacionais se cancelam e sobra simplesmente a razão das variâncias amostrais:

**F = sA² / sB²**, que segue a **distribuição F de Snedecor** com **(nA − 1)** graus de liberdade no **numerador** e **(nB − 1)** no **denominador**.

A F de Snedecor é, por definição, a razão de duas qui-quadrado independentes, cada uma dividida pelos seus graus de liberdade. É sempre positiva e assimétrica, como a qui-quadrado.

> 💡 **Exemplo:** amostra de A com n = 11 e soma dos quadrados dos desvios 60 (sA² = 60/10 = 6); amostra de B com n = 21 e soma 40 (sB² = 40/20 = 2). Então F = 6/2 = 3, com 10 g.l. no numerador e 20 no denominador. Num teste unilateral à direita a 5%, o crítico (cauda superior) é cerca de 2,35; como 3 > 2,35, rejeita-se H0 e conclui-se que A é mais variável que B.

> ⚠️ **Pegadinha:** se o enunciado der a **soma dos quadrados** dos desvios (e não a variância), divida cada soma por n − 1 antes de dividir uma pela outra. Por exemplo, com somas 72 (n = 9) e 60 (n = 11), as variâncias são 72/8 = 9 e 60/10 = 6, e a estatística é 9/6 = 1,5. Também é preciso conferir a ordem: A é o numerador.

**Tabelas e a cauda inferior.** As tabelas da F trazem apenas valores que deixam 90%, 95% etc. à esquerda (cauda superior). Para o crítico **inferior** (testes bilaterais ou à esquerda), usa-se a relação com graus de liberdade invertidos:

**F(1−α; n, m) = 1 / F(α; m, n)** (o valor inferior é o inverso do superior da tabela com os graus de liberdade trocados: numerador vira denominador e vice-versa).

> 💡 **Exemplo:** num bilateral a 10%, com 10 g.l. no numerador e 20 no denominador, o crítico superior é o da tabela de 95% (≈ 2,35). O inferior é 1 dividido pelo valor da tabela de 95% com os graus invertidos (20 no numerador, 10 no denominador, ≈ 2,77): 1/2,77 ≈ 0,36. Rejeita-se H0 se F < 0,36 ou F > 2,35.

**Outras hipóteses nulas.** Nem sempre H0 é igualdade. Se H0: σA² = 2·σB² (A teria o dobro da variância), a estatística passa a ser **F = sA² / (2·sB²)**, comparada à mesma F com (nA − 1; nB − 1) graus de liberdade. No exemplo anterior, F = 6/(2 · 2) = 1,5.

> 💡 **Ordem prática:** quando se quer comparar as médias de duas populações cujas variâncias são desconhecidas, aplica-se primeiro o teste F. Se H0 de variâncias iguais não é rejeitada, usa-se o teste t com variância combinada; se for rejeitada, o teste t com variâncias diferentes.

### P-valor (nível descritivo)

O **p-valor** (também chamado nível descritivo ou probabilidade de significância) é a **probabilidade de obter um resultado igual ou mais extremo que o observado, supondo que H0 é verdadeira**. Em vez de comparar a estatística com um valor crítico, compara-se o p-valor com o nível de significância α:

| Resultado | Decisão |
| --- | --- |
| p-valor **<** α | rejeita-se H0 (resultado na região crítica) |
| p-valor **≥** α | não se rejeita H0 |

Quando p < α diz-se que o resultado é **estatisticamente significante** (há significância estatística, ou evidência estatística, contra H0). Quanto menor o p-valor, mais forte a evidência contra H0. Essa regra vale para qualquer teste (Z, t, qui-quadrado, F; bilateral ou unilateral): o que muda é a região usada para calcular o p-valor.

**Como calcular:** obtém-se a estatística do teste e procura-se, na tabela, a probabilidade na cauda a partir dela, **no sentido da região crítica**.

- Teste à esquerda: p = P(estatística ≤ valor observado) (cauda esquerda).
- Teste à direita: p = P(estatística ≥ valor observado) (cauda direita).
- Teste bilateral (distribuições simétricas, como a normal e a t): p = P(Z ≤ −|z|) + P(Z ≥ |z|) = **2 × p do teste unilateral**.

> 💡 **Exemplo:** teste Z à direita com z = 2,0. A tabela normal dá P(0 < Z < 2,0) = 0,4772, logo p = 0,5 − 0,4772 = 0,0228 (2,28%). Com α = 5%, p < α: rejeita-se H0. Com α = 1%, p > α: não se rejeita. Se o teste fosse bilateral, p = 2 × 0,0228 = 0,0456, que ainda é menor que 5% (rejeita), mas maior que 1% (não rejeita).

> ⚠️ **Pegadinhas:** (1) O p-valor **não é um limite** nem o próprio nível de significância; e **não é a probabilidade de H0 ser verdadeira**: é a probabilidade do dado ou de algo mais extremo, se H0 for verdadeira. (2) Se p-valor = 0,005 e α = 1%, então p < α: rejeita-se H0, e é errado concluir que H0 é verdadeira. (3) Se p = 0,02, rejeita-se H0 a 5%, mas não a 0,1%, pois a decisão depende de α. (4) Em outras palavras, o p-valor é o menor nível de significância com o qual H0 ainda seria rejeitada.

### Para fixar
- Teste de variância de uma população normal: χ² = (n − 1)·s²/σ²0, com n − 1 graus de liberdade.
- A qui-quadrado é positiva e assimétrica: os críticos inferior e superior são diferentes; no bilateral, α/2 em cada cauda; no unilateral à esquerda rejeita-se com χ² pequeno.
- Teste F para duas variâncias: F = sA²/sB² sob H0 de igualdade, com (nA − 1; nB − 1) graus de liberdade; se H0 for σA² = k·σB², F = sA²/(k·sB²).
- Para o crítico inferior da F: F(1−α; n, m) = 1/F(α; m, n), invertendo os graus de liberdade.
- Variância amostral = soma dos quadrados dos desvios ÷ (n − 1); se o enunciado der a soma, divida antes de usar.
- P-valor = probabilidade de resultado igual ou mais extremo, sob H0 verdadeira; p < α rejeita H0, p ≥ α não rejeita.
- No teste bilateral com distribuição simétrica, o p-valor é o dobro do unilateral; p < α significa significância estatística.

# SINTÉTICO

- **Teste da variância**: com população normal, χ² = (n − 1)·s²/σ²0 segue qui-quadrado com n − 1 graus de liberdade; s² usa divisor n − 1.
- **Qui-quadrado é assimétrica**: os críticos inferior e superior têm valores diferentes, lidos na tabela; no bilateral deixa-se α/2 em cada cauda, e no unilateral à esquerda rejeita-se com χ² abaixo do crítico inferior.
- **Mesma estatística, níveis diferentes**: um χ² pode rejeitar H0 a 10% e não rejeitar a 5%; sempre confira o α de cada alternativa.
- **Teste F (duas variâncias)**: sob H0: σA² = σB², F = sA²/sB² segue F de Snedecor com (nA − 1) g.l. no numerador e (nB − 1) no denominador.
- **Soma dos quadrados ≠ variância**: se o enunciado der a soma dos quadrados dos desvios, divida cada uma por n − 1 antes de calcular a razão F.
- **Cauda inferior da F**: as tabelas só dão a cauda superior; use F(1−α; n, m) = 1/F(α; m, n), trocando numerador e denominador.
- **Outras H0 de variância**: se H0 é σA² = 2·σB², a estatística vira F = sA²/(2·sB²); o teste F vem antes da comparação de médias para escolher variâncias iguais ou diferentes.
- **P-valor**: probabilidade de resultado igual ou mais extremo que o observado, supondo H0 verdadeira; p < α rejeita H0 e p ≥ α não rejeita.
- **Bilateral × unilateral e armadilhas**: nas distribuições simétricas o p-valor do bilateral é o dobro do unilateral; p-valor não é a probabilidade de H0 ser verdadeira, e p < α indica significância estatística.

# NOTAS

- Os gráficos e tabelas de valores críticos (qui-quadrado e F) das questões comentadas estavam em imagens não extraídas; os valores usados nos exemplos próprios (2,35; 2,77; 10,85) são de tabelas padrão e conferem com os valores publicados, e os do exemplo de 4 graus de liberdade (0,71 e 9,49) estão no texto da fonte.
- Divergência com a fonte: na solução da questão FGV/MPE-BA (pág. 69), a conta da alternativa C aparece com s² = 27,25 no enunciado e 25,25 no cálculo; resultado final da alternativa (rejeitar H0) não muda com 27,25 (2/3 × 27,25 ≈ 18,17 > 18). Não foi usado no resumo.
- Na pág. 80, o material julga errada a frase "o p-valor é o maior valor do nível de significância a partir do qual H0 não poderá ser rejeitada". O resumo adota a definição padrão (probabilidade de resultado igual ou mais extremo sob H0; p é o menor α com o qual H0 seria rejeitada), sem endossar essa formulação específica. Sugiro conferência humana do ponto (4) da pegadinha do p-valor.
- A orientação "teste F antes do teste de médias" vem do material (pág. 73); a escolha de teste t com variâncias iguais ou diferentes é a do trecho sobre comparação de médias.
