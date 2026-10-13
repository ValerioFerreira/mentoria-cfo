---
id: S0514
agente: CLAUDE-L4
materia: Estatística
aula: Aula 11 — Testes de Hipóteses
trecho: estatistica/a11/s05
paginas_lidas: 56-65
---
# ANALÍTICO

Este trecho aplica o teste de hipóteses a **proporções**: o teste para uma proporção, a comparação entre duas proporções e o teste exato baseado na distribuição binomial (sem aproximação normal), com cálculo de erros tipo I e II e do poder.

### Teste para a proporção de uma população

Vale para populações de **Bernoulli** (cada elemento é sucesso ou fracasso) com proporção p desconhecida. A hipótese nula fixa um valor para p (H0: p = p0) e a amostra fornece a proporção observada **p̂** (sucessos ÷ n).

Com amostra grande, o Teorema do Limite Central permite aproximar p̂ por uma normal e usar a transformação padrão: **z = (valor − média) ÷ desvio padrão**. Aqui:

- valor = p̂ (proporção observada);
- média = p (o valor da hipótese nula);
- variância da população: V(p) = p·q, com q = 1 − p;
- variância da proporção amostral: **V(p̂) = p·q / n**;
- desvio padrão: **σ(p̂) = raiz de (p·q / n)**.

Estatística do teste: **z = (p̂ − p) ÷ σ(p̂)**. Os valores de p e q do desvio padrão são os da hipótese nula. Essa estatística é chamada de **escore reduzido**.

> 💡 **Exemplo próprio:** uma associação afirma que 40% dos associados aprovam uma medida (H0: p = 0,4). Em n = 600 consultados, 270 aprovam, então p̂ = 0,45. Variância: 0,4 × 0,6 / 600 = 0,0004; desvio padrão = 0,02; z = (0,45 − 0,40) / 0,02 = 2,5. Com H1: p > 0,4 e 5% de significância (zc = 1,65, da tabela acumulada, P(Z < 1,65) = 0,95), 2,5 cai na região crítica e H0 é rejeitada.

**Limite da região crítica.** Em vez de calcular z, pode-se achar o limite para a proporção amostral isolando p̂: **L = p + z × σ(p̂)**. Usa-se z **positivo** para o limite superior e **negativo** para o inferior. Se o p̂ observado passar do limite (para o lado da hipótese alternativa), rejeita-se H0.

> 💡 **Exemplo (controle de qualidade, estilo Cebraspe):** H0: p = 0,04 de parafusos fora da especificação; n = 10.000, e o produto p·q vale 0,0384. Dividido pelo tamanho da amostra, dá uma variância de 0,00000384, com σ ≈ 0,002 (aproximação dada na questão). Como só importa a proporção de defeitos **superar** 4% (menos defeitos é melhor), o teste é **unilateral à direita** (H1: p > 0,04). Com α = 5%, zc = 1,65 e L = 0,04 + 1,65 × 0,002 = 0,0433. A amostra teve 1.000 defeituosos: p̂ = 0,10, muito acima de 0,0433. Rejeita-se H0 (item "Certo").

> ⚠️ **Pegadinha:** o teste unilateral ou bilateral depende da hipótese alternativa e do enunciado. Pergunte-se sempre: qual desvio é relevante (só para cima, só para baixo, ou ambos)?

**População finita.** As fórmulas supõem população infinita ou amostragem **com reposição**. Em população finita de tamanho N, com amostra **sem reposição**, multiplica-se a variância amostral por **(N − n) / (N − 1)**: V*(p̂) = (p·q / n) × (N − n) / (N − 1).

O mesmo teste serve quando a população é dividida em duas categorias quaisquer, como sinais "+" e "−": testa-se a proporção de cada sinal.

### Teste para duas proporções

Compara duas populações **independentes** quanto a uma mesma característica (ex.: proporção de homens na empresa A e na B). H0: **p1 = p2**, o mesmo que p1 − p2 = 0. A hipótese alternativa define o tipo de teste:

| Tipo de teste | H0 | H1 |
| --- | --- | --- |
| Bilateral | p1 − p2 = 0 | p1 − p2 ≠ 0 |
| Unilateral à esquerda | p1 − p2 = 0 | p1 − p2 < 0 (p1 < p2) |
| Unilateral à direita | p1 − p2 = 0 | p1 − p2 > 0 (p1 > p2) |

Pelo Teorema do Limite Central, a diferença p̂1 − p̂2 é aproximadamente normal. Sob H0, a média da diferença é **0**. Como as amostras são independentes, as variâncias **se somam**:

**V(p̂1 − p̂2) = p·q / n1 + p·q / n2**, com p o valor comum da hipótese nula e n1, n2 os tamanhos das amostras.

O desvio padrão é a raiz dessa variância, e a estatística é **z = (p̂1 − p̂2) ÷ σ(p̂1 − p̂2)**.

> 💡 **Exemplo próprio:** as duas pesquisas supõem p = 0,5; amostras de 100 cada, com 60 sucessos na primeira e 40 na segunda. Variância = 0,25/100 + 0,25/100 = 0,005; σ ≈ 0,0707; diferença observada = 0,60 − 0,40 = 0,20; z ≈ 2,83. Num teste bilateral a 5% (zc = 1,96), rejeita-se H0.

Para obter o limite da diferença: **p̂1 − p̂2 = zc × σ(p̂1 − p̂2)**, com zc positivo para o limite superior e negativo para o inferior.

Quando o valor comum de p não é fornecido, a prática usual é estimá-lo juntando as duas amostras: p = (sucessos1 + sucessos2) / (n1 + n2) (acrescentado fora do trecho).

### Teste para a distribuição binomial (exato)

Aqui **não se usa a aproximação normal**: trabalha-se com a binomial, que é a distribuição exata do número de sucessos em n ensaios independentes:

**P(X = k) = C(n, k) · p^k · q^(n − k)**, com q = 1 − p.

Parte-se do p da hipótese nula e do número de ensaios n. O mais comum é receber a **regra de rejeição** (os valores de k que levam a rejeitar H0) e calcular o nível de significância; o contrário (fixar α e achar os limites) é menos frequente.

- **α (erro tipo I)** = probabilidade de rejeitar H0 sendo ela verdadeira = soma das probabilidades de k na região de rejeição, calculadas com **p de H0**.
- **β (erro tipo II)** = probabilidade de não rejeitar H0 sendo ela falsa, calculada com **p de H1** (o parâmetro verdadeiro); β = 1 − poder.
- **Poder do teste (1 − β)** = probabilidade de rejeitar H0 sendo ela falsa = soma das probabilidades da região de rejeição, calculadas com p de H1.

Casos especiais de combinação ajudam: C(n, 0) = C(n, n) = 1 e C(n, 1) = C(n, n − 1) = n.

> 💡 **Exemplo do material (moeda honesta):** H0: p = 0,5, H1: p ≠ 0,5, n = 4 lançamentos, rejeita-se se todas as faces forem iguais (0 ou 4 caras). P(0) = P(4) = 0,0625, então **α = 0,125 = 12,5%**. Com H1: p = 0,6 e regra "rejeitar se saírem 3 ou 4 caras": P(3) = 4 × 0,6³ × 0,4 = 0,3456 e P(4) = 0,6⁴ = 0,1296, logo **poder = 0,4752** e **β = 0,5248**.

> 💡 **Exemplo próprio:** n = 3, H0: p = 0,5 contra H1: p = 0,8, rejeitando H0 só se saírem 3 sucessos. α = 0,5³ = 0,125; poder = 0,8³ = 0,512; β = 1 − 0,512 = 0,488.

> ⚠️ **Pegadinha:** α usa sempre o p de **H0**; β e o poder usam o p de **H1**. Misturar os dois parâmetros é o erro mais comum. Confira também se a regra do enunciado é de rejeição ou de **não rejeição** (por exemplo, "a hipótese é aceita se houver mais de 1 favorável" significa que se rejeita com 0 ou 1).

### Questões típicas

- **Aceitação com amostra pequena (n = 4, H0: p = 3/4, não rejeita se favoráveis > 1):** rejeita-se com 0 ou 1 favorável. α = P(0) + P(1) = 1/256 + 12/256 = **13/256**. O teste é unilateral, pois só rejeita para poucos sucessos.
- **Bernoulli, n = 4, H0: p = 1/4 contra H1: p = 3/4, rejeita-se H0 só com 4 sucessos:** α = (1/4)⁴ = 0,0039 (aprox.); poder = (3/4)⁴ = 0,3164; β = 1 − 0,3164 = 0,6836 (aprox.).

### Para fixar
- Proporção: z = (p̂ − p) / raiz(p·q/n), com p e q da hipótese nula.
- Limite da região crítica: L = p + z·σ(p̂); z positivo dá limite superior, negativo dá o inferior.
- População finita sem reposição: multiplicar a variância por (N − n)/(N − 1).
- Duas proporções: H0 p1 = p2; as variâncias se somam, V = p·q/n1 + p·q/n2; a média sob H0 é zero.
- Binomial exata: P(X = k) = C(n, k)·p^k·q^(n − k), sem aproximação normal.
- α usa o p de H0; β e o poder (1 − β) usam o p de H1; α, β e poder somam probabilidades da região de rejeição ou de seu complemento.
- Determine sempre se o teste é unilateral (qual lado?) ou bilateral antes de comparar com o valor crítico.

# SINTÉTICO

- **Teste para uma proporção**: população de Bernoulli; com amostra grande usa-se z = (p̂ − p) / raiz(p·q/n), com p e q tirados da hipótese nula.
- **Limite da região crítica**: L = p + z × σ(p̂); z positivo dá o limite superior e z negativo, o inferior; rejeita-se H0 se p̂ passa do limite.
- **Unilateral × bilateral**: a hipótese alternativa define o lado; só importa para cima (p > p0), só para baixo (p < p0) ou nos dois sentidos (≠).
- **População finita**: sem reposição, multiplica-se a variância da proporção amostral por (N − n)/(N − 1).
- **Duas proporções**: amostras independentes, H0: p1 = p2 (diferença zero), V(p̂1 − p̂2) = p·q/n1 + p·q/n2, e z = (p̂1 − p̂2) / desvio padrão da diferença.
- **Hipóteses para duas proporções**: bilateral (p1 − p2 ≠ 0), esquerda (< 0) ou direita (> 0); o limite da diferença é zc × σ da diferença.
- **Teste binomial**: usa a distribuição exata, P(X = k) = C(n, k)·p^k·q^(n − k), sem aproximar pela normal.
- **Erro tipo I (α)**: soma das probabilidades da região de rejeição com o p da hipótese nula.
- **Erro tipo II (β) e poder**: o poder (1 − β) soma a região de rejeição com o p de H1; β é o complemento.
- **Atalhos de combinação**: C(n, 0) = C(n, n) = 1 e C(n, 1) = C(n, n − 1) = n.
- **Cuidado com a regra**: leia se o enunciado descreve a região de rejeição ou a de aceitação; no exemplo clássico com n = 4 e p = 3/4, α = 13/256.

# NOTAS

- Fórmulas com símbolos (p̂, raízes, frações) saíram embaralhadas na extração; foram reconstruídas e conferidas pelos exemplos numéricos do trecho.
- Pág. 56 do material: a fórmula final de z mostra p̂ e q̂ no denominador; sob H0 o correto, e o usado nos exemplos do próprio trecho, é p e q da hipótese nula. O resumo usa p e q de H0.
- Pág. 65 do material: na solução da questão de erro tipo I, o texto fala "probabilidade do erro tipo II é a soma", mas a conta é do erro tipo I (13/256); gabarito E confere com 13/256.
- Pág. 61 do material: o exemplo de duas proporções supõe p = 0,5 dado; o material não trata da estimativa conjunta. O uso de p combinado = (sucessos1 + sucessos2)/(n1 + n2) foi acrescentado fora do trecho (regra estável e conhecida).
- O valor crítico 1,96 (bilateral a 5%) não aparece no trecho (só 1,65); foi acrescentado fora do trecho, em exemplo próprio.
- Figuras (regiões críticas) descartadas; o texto descreve a ideia.
