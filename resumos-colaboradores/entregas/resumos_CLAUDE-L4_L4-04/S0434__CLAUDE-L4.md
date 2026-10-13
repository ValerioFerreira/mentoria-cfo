---
id: S0434
agente: CLAUDE-L4
materia: Estatística
aula: Aula 11 — Testes de Hipóteses
trecho: estatistica/a11/s04
paginas_lidas: 41-55
---
# ANALÍTICO

Este trecho mostra como testar se duas médias são iguais. Primeiro fecha-se o fim do teste t para uma média (limites da região de não rejeição); depois vêm a comparação de duas populações independentes com variâncias conhecidas e desconhecidas e, por fim, o teste t para amostras pareadas, em que os mesmos indivíduos são medidos duas vezes.

### Fechando o teste t para uma média: limites da região de não rejeição

Quando a questão não dá a estatística do teste, mas pede o valor da média amostral que separa rejeitar de não rejeitar, basta inverter a fórmula do teste. Com variância desconhecida, o limite é

**x̄ limite = μ0 ± t_c · s/√n**, com t_c lido na tabela para **n − 1** graus de liberdade.

> 💡 **Exemplo:** H0: μ = 50, amostra com n = 16 e s = 8. O erro padrão é 8/√16 = 2. Com 15 graus de liberdade e teste bilateral a 5%, t_c = 2,13. O limite inferior da região de não rejeição é 50 − 2,13 × 2 = 45,74 (e o superior, 54,26). Médias amostrais abaixo de 45,74 ou acima de 54,26 levam à rejeição.

### Comparação das médias de duas populações: hipóteses

O objetivo é decidir se duas populações **independentes**, X1 e X2, têm a mesma média, isto é, se na prática são a mesma população. A hipótese nula afirma igualdade, o que equivale a dizer que a diferença é nula:

**H0: μ1 = μ2 (ou H0: μ1 − μ2 = 0).**

| Tipo de teste | Hipótese alternativa | Quando se rejeita H0 |
| --- | --- | --- |
| Bilateral | H1: μ1 ≠ μ2 (μ1 − μ2 ≠ 0) | diferença x̄1 − x̄2 muito negativa **ou** muito positiva |
| Unilateral à esquerda | H1: μ1 < μ2 (μ1 − μ2 < 0) | só se x̄1 for muito menor que x̄2 |
| Unilateral à direita | H1: μ1 > μ2 (μ1 − μ2 > 0) | só se x̄1 for muito maior que x̄2 |

A lógica é a de sempre: rejeitar é a decisão forte, tomada apenas quando o resultado cai na região crítica. Exemplo intuitivo: uma fábrica que recebe dois lotes do mesmo fornecedor pode fixar que a diferença entre as médias dos lotes deve ficar entre −0,5 e +0,5; fora disso, rejeita-se que os lotes sejam equivalentes. Se só o lote 1 ser menor que o 2 for problema, o teste é unilateral à esquerda.

### Variâncias populacionais conhecidas: teste Z

Se as populações são normais (ou as amostras são grandes o bastante para a média amostral ser aproximadamente normal) e as variâncias σ1² e σ2² são conhecidas, a diferença x̄1 − x̄2 também é normal, com:

- **média** μ1 − μ2 (que vale 0 sob H0);
- **variância** V(x̄1 − x̄2) = σ1²/n1 + σ2²/n2 — **soma** das variâncias das duas médias amostrais, porque as amostras são independentes;
- **desvio padrão** = raiz quadrada dessa soma.

**Estatística:** z = (x̄1 − x̄2) / √(σ1²/n1 + σ2²/n2), comparada ao z crítico da normal padrão, conforme o nível de significância e o tipo de teste.

Se a hipótese nula fixar uma diferença diferente de zero (H0: μ1 − μ2 = Δ0), subtrai-se Δ0 no numerador: **z = (x̄1 − x̄2 − Δ0) / √(σ1²/n1 + σ2²/n2)**.

Também se pode raciocinar pelo limite da diferença: **LD = ± z_c · √(σ1²/n1 + σ2²/n2)**. Sob H0 de igualdade, os dois limites têm o mesmo módulo e sinais opostos, e não é preciso conhecer μ1 nem μ2.

> 💡 **Exemplo:** σ1² = 4 com n1 = 32 e σ2² = 5 com n2 = 40. As variâncias das médias são 4/32 = 0,125 e 5/40 = 0,125; a soma é 0,25 e o desvio padrão da diferença é 0,5. Num teste bilateral a 5% (z_c = 1,96), o limite é 1,96 × 0,5 = 0,98. Se x̄1 − x̄2 = 1,2, então z = 1,2/0,5 = 2,4 > 1,96: rejeita-se H0.

> ⚠️ **Pegadinha:** a prova pode dar os valores σ/√n de cada amostra (o erro padrão de cada média). É preciso **elevá-los ao quadrado**, somar e só então extrair a raiz. **Nunca some os desvios padrão** (σ1/√n1 + σ2/√n2 está errado).

> 💡 **Nota teórica:** para variáveis independentes, a covariância é zero, por isso a variância da soma e a da diferença são iguais à soma das variâncias. Se houvesse dependência, entraria o termo 2·Cov(X1, X2) (somado na soma e subtraído na diferença).

> 💡 **Exemplo com frações:** duas amostras com n = 25 e n = 100, variâncias populacionais 50 e 200, médias 31 e 28. As variâncias das médias são 50/25 = 2 e 200/100 = 2; somadas dão 4 e o desvio padrão da diferença é 2. Logo z = (31 − 28)/2 = 1,5, que fica abaixo de 1,96: não se rejeita H0 a 5% (bilateral).

### Variâncias desconhecidas e iguais: teste t com variância combinada

Agora as duas populações são normais, com médias desconhecidas e **a mesma variância σ², também desconhecida**. As variâncias amostrais s1² e s2² são estimativas não viesadas de σ². Para ter uma estimativa única, calcula-se a **variância combinada** (estimador combinado), uma média ponderada pelos graus de liberdade:

**sp² = [(n1 − 1)·s1² + (n2 − 1)·s2²] / (n1 + n2 − 2)**

A variância estimada da diferença das médias e a estatística do teste (H0: μ1 = μ2) são:

- **V(x̄1 − x̄2) = sp² · (1/n1 + 1/n2)**;
- **t = (x̄1 − x̄2) / √[sp² · (1/n1 + 1/n2)]**, que segue t de Student com **n1 + n2 − 2** graus de liberdade.

Quando H0 fixa Δ0 ≠ 0, a estatística é t = (x̄1 − x̄2 − Δ0) / √[sp² · (1/n1 + 1/n2)], com os mesmos graus de liberdade.

> 💡 **Exemplo:** n1 = n2 = 8, s1² = 5 e s2² = 3. A variância combinada é (7·5 + 7·3)/14 = 4. O erro padrão é √[4 · (1/8 + 1/8)] = √1 = 1. Se x̄1 − x̄2 = 2,4, então t = 2,4 com 14 graus de liberdade. O valor crítico bilateral a 5% é 2,145; como 2,4 > 2,145, rejeita-se H0. Repare que, com tamanhos iguais, sp² é simplesmente a média aritmética de s1² e s2².

A variância combinada fica sempre entre s1² e s2², mais perto da variância da amostra maior (que tem mais graus de liberdade). Na prova, cobra-se muito o cálculo dela: com s1² = 5 (n1 = 21) e s2² = 10 (n2 = 31), sp² = (20·5 + 30·10)/50 = 8.

> ⚠️ **Pegadinha:** os graus de liberdade da comparação de duas médias independentes são **n1 + n2 − 2**, não n − 1. Se as amostras têm 5 observações cada, são 8 graus; com t calculado 2,28 e crítico bilateral a 5% de 2,306 (8 g.l.), **não se rejeita** H0, e a conclusão correta é que não há evidência de diferença entre as médias.

### Variâncias desconhecidas e diferentes

Se não se pode supor variâncias iguais, não há variância combinada. Cada variância amostral entra separadamente:

**t = (x̄1 − x̄2) / √(s1²/n1 + s2²/n2)**

Essa estatística segue **aproximadamente** uma t de Student, e o número de graus de liberdade k é calculado a partir das duas variâncias dos estimadores (aproximação de Welch-Satterthwaite):

**k = (s1²/n1 + s2²/n2)² / [ (s1²/n1)²/(n1 − 1) + (s2²/n2)²/(n2 − 1) ]**

Nesse caso k em geral não é inteiro e fica entre o menor dos (n − 1) e n1 + n2 − 2. Em prova, o mais comum é o enunciado dizer qual caso vale (variâncias iguais ou diferentes) e fornecer a fórmula, por isso é essencial saber **qual versão aplicar**.

### Teste t para amostras pareadas

As amostras **não são independentes**: os mesmos indivíduos (ou unidades emparelhadas) são medidos duas vezes, por exemplo antes e depois de um medicamento, de uma dieta ou de um treino. H0 diz que o tratamento não tem efeito (μ1 = μ2). A alternativa pode ser bilateral (μ1 ≠ μ2) ou unilateral (a condição melhorou, ou o tempo diminuiu).

O truque é transformar o problema em um teste para **uma única amostra**: a das **diferenças** d_i = x_i − y_i de cada indivíduo.

1. Calcule as diferenças para cada par.
2. Calcule a média das diferenças, **d̄**.
3. Calcule o desvio padrão amostral das diferenças, **s_d** (soma dos quadrados dos desvios em relação a d̄, dividida por n − 1, e raiz quadrada).
4. Erro padrão: **s_d/√n**.
5. Estatística: **t = d̄ / (s_d/√n)**, com **n − 1** graus de liberdade (n = número de pares).

Se H0 fixar uma diferença Δ0 diferente de zero: t = (d̄ − Δ0) / (s_d/√n).

> 💡 **Exemplo:** 9 pessoas, diferenças (antes − depois) 7, 7, 7, 7, 1, 1, 1, 1 e 4. A média é 36/9 = 4. Os desvios em relação à média são ±3 (oito vezes) e 0; a soma dos quadrados é 8 × 9 = 72 e a variância amostral é 72/8 = 9, logo s_d = 3. O erro padrão é 3/√9 = 1, e t = 4/1 = 4 com 8 graus de liberdade. Como o crítico bilateral a 5% é 2,306, rejeita-se H0: o tratamento teve efeito.

> ⚠️ **Pegadinha:** a **média das diferenças é igual à diferença das médias** (d̄ = x̄ − ȳ), então, se a questão der só as duas médias, o numerador sai direto. Mas isso **não vale para o desvio padrão**: s_d não se obtém a partir dos desvios padrão de x e de y separados, e sim das diferenças pares a pares. Outra armadilha comum: usar o teste de duas amostras independentes quando os dados são de antes e depois nos mesmos indivíduos.

### Resumo de fórmulas e graus de liberdade

| Situação | Estatística | Distribuição |
| --- | --- | --- |
| Uma média, variância conhecida | z = (x̄ − μ)/σ_x̄ | normal padrão |
| Uma média, variância desconhecida | t = (x̄ − μ)/(s/√n) | t com n − 1 g.l. |
| Duas médias independentes, variâncias conhecidas | z = (x̄1 − x̄2)/√(σ1²/n1 + σ2²/n2) | normal padrão |
| Duas médias independentes, variâncias desconhecidas e iguais | t = (x̄1 − x̄2)/√[sp²(1/n1 + 1/n2)] | t com n1 + n2 − 2 g.l. |
| Duas médias independentes, variâncias desconhecidas e diferentes | t = (x̄1 − x̄2)/√(s1²/n1 + s2²/n2) | t aproximada, g.l. = k |
| Amostras pareadas | t = d̄/(s_d/√n) | t com n − 1 g.l. |

### Para fixar
- Comparação de médias: H0 é de igualdade (μ1 − μ2 = 0, ou = Δ0 quando o enunciado fixar uma diferença) e H1 define o tipo de teste: ≠ bilateral, < esquerda, > direita.
- Variâncias conhecidas: z = (x̄1 − x̄2)/√(σ1²/n1 + σ2²/n2). Somam-se **variâncias**, nunca desvios padrão.
- Variâncias desconhecidas e iguais: variância combinada sp² (média ponderada por n − 1) e t com n1 + n2 − 2 graus de liberdade.
- Variâncias desconhecidas e diferentes: usa-se s1²/n1 + s2²/n2 sem combinar, e os graus de liberdade vêm da fórmula aproximada k.
- Amostras pareadas: trabalha-se com as diferenças pares a pares, t = d̄/(s_d/√n) com n − 1 graus de liberdade.
- Média das diferenças = diferença das médias, mas o desvio padrão das diferenças exige as diferenças individuais.
- Decisão: estatística calculada além do valor crítico (em módulo, no bilateral) leva à rejeição de H0; senão, não se rejeita.

# SINTÉTICO

- **Hipóteses**: H0 é sempre de igualdade (μ1 = μ2, ou seja, μ1 − μ2 = 0); H1 pode ser ≠ (bilateral), < (esquerda) ou > (direita), e só se rejeita H0 quando a diferença amostral cai na região crítica.
- **Variâncias conhecidas (teste Z)**: z = (x̄1 − x̄2)/√(σ1²/n1 + σ2²/n2); a variância da diferença é a soma das variâncias das médias, pois as amostras são independentes.
- **Armadilha do erro padrão**: ao receber σ/√n de cada amostra, eleve ao quadrado, some e extraia a raiz; somar os desvios padrão está errado.
- **Diferença Δ0 ≠ 0**: se H0 fixa uma diferença Δ0, subtrai-se Δ0 de x̄1 − x̄2 no numerador da estatística (z ou t).
- **Variâncias desconhecidas e iguais**: sp² = [(n1 − 1)s1² + (n2 − 1)s2²]/(n1 + n2 − 2); t = (x̄1 − x̄2)/√[sp²(1/n1 + 1/n2)] com n1 + n2 − 2 graus de liberdade.
- **Variâncias desconhecidas e diferentes**: t = (x̄1 − x̄2)/√(s1²/n1 + s2²/n2), com t aproximada e graus de liberdade k pela fórmula de Welch-Satterthwaite (em geral não inteiro).
- **Amostras pareadas**: mesmos indivíduos medidos antes e depois; calcule as diferenças e aplique t = d̄/(s_d/√n) com n − 1 graus de liberdade.
- **Pareado × independente**: a média das diferenças equivale à diferença das médias, mas s_d vem das diferenças par a par; nunca trate dados pareados como duas amostras independentes.
- **Decisão**: compare a estatística ao valor crítico da tabela (z ou t, conforme o caso) para o nível de significância e o tipo de teste; passou do crítico, rejeita-se H0.

# NOTAS

- Página 41 começa no meio de uma questão comentada sobre o limite inferior da região de não rejeição do teste t (resumida no início do analítico, com exemplo próprio).
- Divergência com a fonte: ao apresentar o teste com variância comum, o material diz que as variâncias amostrais "seguem distribuição t de Student". Isso não está correto: s1² e s2² são estimadores não viesados de σ² (e (n − 1)s²/σ² segue qui-quadrado); o que segue t é a estatística do teste. O resumo não repete a afirmação.
- Divergência com a fonte (pág. 48, exemplo de variâncias combinadas): o valor crítico unilateral a 5% citado para 11 g.l. (2,6) está inconsistente com a tabela t usual (cerca de 1,80), e o bilateral citado (2,2) é correto (2,201). Por isso o resumo usa exemplos próprios, com valores críticos de tabela padrão (t com 14 g.l. = 2,145; com 8 g.l. = 2,306; com 15 g.l. = 2,13).
- Tabelas t e dados de várias questões do material estavam em imagens não extraídas (pág. 49, 50, 52, 53); usei apenas o que o texto e os comentários permitem reconstruir.
