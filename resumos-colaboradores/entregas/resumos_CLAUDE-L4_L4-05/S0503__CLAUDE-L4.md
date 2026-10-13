---
id: S0503
agente: CLAUDE-L4
materia: Estatística
aula: Aula 08 — Distribuições Discretas de Probabilidade
trecho: estatistica/a08/s04
paginas_lidas: 43-52
---
# ANALÍTICO

A distribuição hipergeométrica trata de retiradas **sem reposição** em uma população finita dividida em dois tipos. O trecho ensina a reconhecer a situação, aplicar a fórmula com combinações, determinar os valores possíveis da variável e usar esperança, variância e o fator de correção para população finita.

### Quando usar

Parte-se de uma população de N elementos em que cada um tem um de dois atributos: **sucesso** (S elementos) ou **fracasso** (N − S elementos). Retira-se uma amostra de n elementos **sem reposição**. A variável X, número de sucessos na amostra, é hipergeométrica: X ~ Hgeo(N, S, n).

Diferença para a binomial: aqui a população é **finita** e cada retirada altera a composição do que sobra, então as extrações são **dependentes**. Na binomial há independência (reposição ou população enorme).

> ⚠️ **Pegadinha:** quando o enunciado não diz se há reposição, considera-se que **não há** (a retirada sem reposição é a mais usual). Um lote pequeno, "sorteio de regiões", "retirar peças do lote" ou "bolas de uma urna" sem menção a reposição indicam hipergeométrica. Os três parâmetros são N (população), S (sucessos na população) e n (amostra); as bancas às vezes confundem o nome com a "geométrica", que é outra distribuição.

### Fórmula da probabilidade

**P(X = k) = C(S, k) · C(N − S, n − k) / C(N, n)**

É a definição clássica de probabilidade (casos favoráveis dividido por casos possíveis), sem importar a ordem:

- denominador C(N, n): todas as amostras possíveis de n elementos;
- C(S, k): maneiras de escolher os k sucessos entre os S existentes;
- C(N − S, n − k): maneiras de escolher os n − k fracassos entre os N − S existentes;
- o numerador é o produto dos dois (princípio multiplicativo).

> 💡 **Exemplo:** urna com N = 12 bolas, das quais S = 5 são vermelhas. Retiram-se n = 4 sem reposição. Probabilidade de exatamente 2 vermelhas: C(5, 2) · C(7, 2) / C(12, 4) = 10 · 21 / 495 = 14/33, cerca de 42%.

**Caminho alternativo, probabilidade a probabilidade.** Multiplica-se a chance de cada retirada, ajustando os totais a cada passo, e depois multiplica-se pelo número de ordens possíveis (combinação, ou permutação com repetição). No exemplo: (5/12) · (4/11) · (7/10) · (6/9) · C(4, 2) = (840/11880) · 6, que também dá 14/33. Funciona bem para amostras pequenas; para amostras grandes, a fórmula com combinações é mais prática.

### Valores possíveis de X

Nem todo k de 0 a n é viável, porque a população tem quantidades limitadas de cada tipo:

- **Máximo**: o menor entre n e S. Não dá para tirar mais sucessos do que a amostra comporta nem do que existem.
- **Mínimo**: o maior entre 0 e n − (N − S). Se a amostra é maior que o número de fracassos disponíveis, parte dela terá de ser formada por sucessos.

**máx{0, n − (N − S)} ≤ k ≤ mín{n, S}**

> 💡 **Exemplo:** com N = 12 e S = 5, uma amostra de n = 4 admite k de 0 a 4. Já com n = 9: o máximo é mín(9, 5) = 5 e o mínimo é 9 − 7 = 2, de modo que X só vale de 2 a 5.

### Esperança e variância

Seja p = S / N a **proporção de sucessos na população** e q = 1 − p.

- **E(X) = n · p**, igual à esperança da binomial: espera-se que a amostra reproduza a proporção da população.
- **Var(X) = n · p · q · (N − n) / (N − 1)**.

O fator **(N − n)/(N − 1)** é o **fator de correção para população finita**. A variância hipergeométrica é a binomial n · p · q multiplicada por ele. Como N − n < N − 1 (sempre que n > 1), o fator é menor que 1 e **reduz a variância**: sem reposição, a amostra varia menos. Se N é muito maior que n, o fator se aproxima de 1 e a hipergeométrica se **aproxima da binomial**; por isso usa-se a binomial mesmo sem reposição quando a população é suficientemente grande.

> 💡 **Exemplo:** na urna anterior (N = 12, S = 5, n = 4): p = 5/12, E(X) = 4 · 5/12 = 5/3, cerca de 1,67; Var(X) = 4 · (5/12) · (7/12) · (8/11) = 70/99, cerca de 0,71. Outro caso: urna com N = 20 e 5 premiadas, n = 2: p = 1/4 e Var = 2 · (1/4) · (3/4) · (18/19) = 27/76.

### Como a prova cobra

- **Reconhecer a distribuição**: sorteio de elementos de duas categorias em população finita, sem reposição, pede hipergeométrica; o item "tem distribuição hipergeométrica" é certo.
- **Probabilidade pontual**: lote com 30 itens, 5 defeituosos, retirando 3; P(exatamente 2 defeituosos) = C(5, 2) · C(25, 1) / C(30, 3) = 250 / 4060 = 25/406, cerca de 0,06. Simplifique as combinações antes de multiplicar.
- **Média**: 200 audiências, 120 com um certo perfil (p = 0,6), amostra de 80: E(X) = 80 · 0,6 = 48. Só a proporção da população e o tamanho da amostra importam.
- **Variância**: substitua em n · p · q · (N − n)/(N − 1) e simplifique as frações.

### Para fixar
- Hipergeométrica: população finita com S sucessos, retirada de n elementos **sem reposição**; X conta os sucessos da amostra.
- P(X = k) = C(S, k) · C(N − S, n − k) / C(N, n).
- Sem informação sobre reposição, assume-se que não há reposição.
- Limites de X: máx{0, n − (N − S)} ≤ k ≤ mín{n, S}.
- E(X) = n · p, com p = S/N; mesma esperança da binomial.
- Var(X) = n · p · q · (N − n)/(N − 1); o fator de correção é menor que 1 e reduz a variância.
- Com N muito maior que n, o fator tende a 1 e a hipergeométrica se aproxima da binomial.

# SINTÉTICO

- **Quando usar**: população finita com dois tipos (S sucessos e N − S fracassos), amostra de n elementos retirada sem reposição; X conta os sucessos.
- **Dependência**: cada retirada muda a composição da população, ao contrário da binomial (independência); sem informação, assume-se que não há reposição.
- **Probabilidade**: P(X = k) = C(S, k) · C(N − S, n − k) / C(N, n), casos favoráveis (produto de duas combinações) sobre casos possíveis.
- **Método alternativo**: multiplicar as probabilidades de cada retirada e depois pelo número de ordens possíveis; bom para amostras pequenas.
- **Valores possíveis**: máx{0, n − (N − S)} ≤ k ≤ mín{n, S}; nem todo k de 0 a n é viável.
- **Esperança**: E(X) = n · p com p = S/N, a mesma da binomial.
- **Variância**: Var(X) = n · p · q · (N − n)/(N − 1), a binomial vezes o fator de correção para população finita.
- **Fator de correção**: é menor que 1, reduz a variância e se aproxima de 1 quando N é muito maior que n.
- **Aproximação**: com população grande, a hipergeométrica se aproxima da binomial.

# NOTAS

- Pág. 43: o texto diz que os parâmetros N, S, n "caracterizam a distribuição geométrica", mas se refere à hipergeométrica (erro de digitação do material). No resumo usei hipergeométrica.
- Pág. 51, questão do TJDFT ("número mais provável"): a resolução usa a esperança, 48, como resposta. A moda da hipergeométrica é, a rigor, floor[(n + 1)(S + 1)/(N + 2)], que aqui também dá 48; o resumo não generaliza a moda.
- Nada foi acrescentado fora do trecho; os exemplos numéricos (urna de 12 bolas) são próprios.
