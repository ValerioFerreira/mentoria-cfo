---
id: S0433
agente: CLAUDE-L4
materia: Estatística
aula: Aula 05 — Análise Combinatória
trecho: estatistica/a05/s04
paginas_lidas: 49-64
---
# ANALÍTICO

Este trecho trata das seleções em que a **ordem não importa**: a combinação simples (sem repetição), seus casos particulares e propriedades (incluindo o Triângulo de Pascal), a combinação completa (com repetição) e o cálculo do número de soluções inteiras de uma equação. A primeira página traz apenas o final de uma questão de senha (letras distintas e números repetidos, resolvidas pelo princípio multiplicativo: 26 × 25 × 10⁴ = 6.500.000), que não será detalhada.

### Combinação simples

Na combinação, como no arranjo, seleciona-se parte de um conjunto, mas a **ordem da escolha é irrelevante** (sortear um grupo de pessoas, formar uma comissão). Vários arranjos viram uma só combinação: todos os que contêm as mesmas pessoas em ordens diferentes. Por isso:

C(n, k) = A(n, k) ÷ P(k) = n! ÷ [(n − k)! · k!]

ou seja, divide-se o arranjo pelas permutações dos k elementos escolhidos. Outras notações: Cn,k, C(n k) (binomial "n escolhe k") ou o símbolo com n sobre k.

> 💡 **Exemplo:** escolher 2 policiais entre 6 para uma missão: C(6, 2) = 6! ÷ (4! · 2!) = (6 · 5) ÷ 2 = 15.

> ⚠️ **Pegadinha:** escolher um grupo de 3 entre 7 alunos não é 7 · 6 · 5 (isso é o arranjo, que conta a ordem); é C(7, 3) = 7 · 6 · 5 ÷ (3 · 2) = 35. Se o enunciado diz que a ordem não importa (grupo, comissão, time, trio, par), use combinação; se a ordem diferencia (fila, pódio, cargos distintos), use arranjo.

### Restrições do tipo "pelo menos um"

O caminho mais curto é o **complementar**: calcule todas as possibilidades sem a restrição e subtraia as que a violam.

> 💡 **Exemplo:** de 6 homens e 4 mulheres, formar uma comissão de 4 com pelo menos 1 mulher. Total: C(10, 4) = 210. Sem mulheres (só homens): C(6, 4) = 15. Resposta: 210 − 15 = 195.

Outra situação frequente: escolher em **grupos diferentes** e multiplicar (princípio multiplicativo). Exemplo: 5 engenheiros e 4 médicos, comissão com 2 engenheiros e 1 médico: C(5, 2) · C(4, 1) = 10 · 4 = 40. Quando a banda precisa de 2 guitarristas (entre 6), 1 baixista (entre 2), 1 baterista (entre 4) e 1 tecladista (entre 3), calcula-se cada escolha e multiplica-se: 15 · 2 · 4 · 3 = 360. Escolhas **alternativas** (ou uma, ou outra) somam-se (princípio aditivo).

### Casos particulares

Não precisam ser decorados, mas poupam tempo.

| Caso | Valor | Raciocínio |
| --- | --- | --- |
| C(n, n) | **1** | só há uma forma de escolher todos |
| C(n, 0) | **1** | só há uma forma de não escolher ninguém |
| C(n, 1) | **n** | escolhe-se um de cada vez |
| C(n, n − 1) | **n** | basta decidir quem fica de fora (n opções) |
| C(n, k) = C(n, n − k) | simetria | escolher k é o mesmo que escolher os n − k que ficam de fora |

> 💡 **Exemplo:** C(10, 8) = C(10, 2) = 45. Use a simetria para trabalhar com o menor número.

Soma de todas as combinações: C(n, 0) + C(n, 1) + ... + C(n, n) = **2ⁿ** (é o número total de subconjuntos de um conjunto com n elementos).

> 💡 **Exemplo:** guardar 6 documentos distintos em 2 caixas distintas, cada caixa com pelo menos 1. Escolhe-se o que vai para a primeira caixa (o resto vai para a outra): de 1 a 5 documentos. A soma C(6, 1) + ... + C(6, 5) = 2⁶ − C(6, 0) − C(6, 6) = 64 − 1 − 1 = 62.

### Triângulo de Pascal

O triângulo é formado pelos números binomiais C(n, k), com n = linha e k = coluna, ambos começando em 0. As linhas são 1; 1 1; 1 2 1; 1 3 3 1; 1 4 6 4 1; 1 5 10 10 5 1; e assim por diante. Propriedades:

| Propriedade | Enunciado | Exemplo |
| --- | --- | --- |
| **Relação de Stifel** | C(n, k) + C(n, k+1) = C(n+1, k+1): dois vizinhos de uma linha somam o elemento da linha de baixo | C(5, 2) + C(5, 3) = 10 + 10 = 20 = C(6, 3) |
| **Teorema das Linhas** | a soma da linha n vale 2ⁿ | linha 5: 1 + 5 + 10 + 10 + 5 + 1 = 32 = 2⁵ |
| **Teorema das Colunas** | C(k, k) + C(k+1, k) + ... + C(k+n, k) = C(k+n+1, k+1): somando uma coluna desde o começo até certa linha, obtém-se o elemento da linha seguinte, na coluna seguinte | C(2, 2) + C(3, 2) + C(4, 2) = 1 + 3 + 6 = 10 = C(5, 3) |

Uma forma alternativa é uma tabela cuja primeira linha e primeira coluna são só 1, e cada outro elemento é a soma do valor de cima com o da esquerda. O elemento da linha i e coluna j equivale a C(n, k) com n = i + j − 2 e k = j − 1.

### Combinação completa (com repetição)

Aparece quando há **n tipos** de elemento e se escolhem **p unidades**, que podem repetir tipos: por exemplo, 3 potes de sorvete entre 5 marcas (os potes podem ser todos da mesma marca ou de marcas diferentes). É diferente de escolher 3 marcas distintas entre 5 (C(5, 3) = 10): aqui o resultado é bem maior.

**Raciocínio das divisórias:** imagine cada marca numa seção do freezer. Os p potes e as n − 1 divisórias que separam as seções são permutados; como potes são iguais entre si e divisórias também, tem-se permutação com repetição:

CR(n, p) = P(n−1+p; n−1, p) = (n − 1 + p)! ÷ [(n − 1)! · p!] = C(n − 1 + p, p)

> 💡 **Exemplo (no mesmo tema):** 5 marcas e 3 potes: CR(5, 3) = 7! ÷ (4! · 3!) = 35 = C(7, 3). Outro: escolher 4 donuts entre 3 sabores: CR(3, 4) = C(6, 4) = 15.

Use a combinação completa também para **distribuir objetos idênticos entre pessoas (ou lugares)**: n pessoas = n tipos (n − 1 divisórias) e p objetos.

> ⚠️ **Pegadinha:** conferir a identidade dos objetos. Se os objetos são **distintos**, é outra contagem (cada objeto escolhe sua pessoa). A fórmula CR vale para objetos **indistinguíveis** (convites iguais, maçãs idênticas).

**Distribuição com mínimo para cada um.** Entregue primeiro a quantia obrigatória a todos e distribua o **resto** livremente.

> 💡 **Exemplo:** 11 balas idênticas para 3 crianças, cada uma com pelo menos 2. Entregam-se 6 balas (2 para cada) e restam 5 para distribuir sem restrição: CR(3, 5) = 7! ÷ (2! · 5!) = 21.

### Número de soluções inteiras de equações

A combinação completa é o mesmo problema visto como equação. Escolher p objetos entre n tipos equivale a achar os valores x1, x2, ..., xn de x1 + x2 + ... + xn = p, em que xi é a quantidade do tipo i. Logo:

**O número de soluções inteiras e não negativas de x1 + x2 + ... + xn = p é CR(n, p) = (n − 1 + p)! ÷ [(n − 1)! · p!]**

O resultado p da equação é o número de objetos; o número de variáveis n é o número de seções (n − 1 sinais de "+" fazem o papel das divisórias).

> 💡 **Exemplo:** x + y + z = 4 em inteiros não negativos: CR(3, 4) = 6! ÷ (2! · 4!) = 15 soluções. Em a + b + c + d = 21: n = 4 e p = 21, então CR(4, 21) = 24! ÷ (3! · 21!) = (24 · 23 · 22) ÷ 6 = 2.024.

**Por que "inteiras e não negativas"?** Se pudessem ser negativas (ou decimais), seria possível tirar uma unidade de uma variável e dar a outra mantendo a soma, gerando infinitas soluções. Só no conjunto dos inteiros não negativos o número é finito. Incluem-se soluções com variáveis iguais a zero.

**Soluções positivas (xi > 0):** reserva-se 1 unidade para cada variável e distribui-se o restante: se a soma é p com n variáveis, resolve-se a equação com soma p − n em inteiros não negativos.

> 💡 **Exemplo:** x + y + z = 8 com x, y, z positivos. Reserva 1 para cada, restam 5: CR(3, 5) = C(7, 5) = 21 soluções. Para exigir xi ≥ 2, reserve 2 para cada um e proceda da mesma maneira.

### Para fixar
- Combinação: a ordem não importa; C(n, k) = n! ÷ [(n − k)! · k!] = arranjo ÷ k!.
- "Pelo menos um": total menos o caso em que nenhum atende.
- C(n, n) = C(n, 0) = 1; C(n, 1) = C(n, n − 1) = n; C(n, k) = C(n, n − k); soma de C(n, 0) a C(n, n) = 2ⁿ.
- Stifel: C(n, k) + C(n, k+1) = C(n+1, k+1); linhas somam 2ⁿ; teorema das colunas soma de cima até certa linha e dá o próximo.
- Combinação completa (com repetição): CR(n, p) = C(n − 1 + p, p), com n tipos e p unidades idênticas.
- Distribuição de objetos idênticos entre pessoas: entregue o mínimo obrigatório e aplique CR no que sobra.
- Soluções inteiras não negativas de x1 + ... + xn = p: CR(n, p); se exigir positivas, subtraia 1 de cada variável antes (soma passa a p − n).

# SINTÉTICO

- **Combinação simples**: seleção em que a ordem não importa; C(n, k) = n! ÷ [(n − k)! · k!], ou arranjo dividido por k!; por exemplo, C(6, 2) = 15.
- **Arranjo × combinação**: grupos, comissões e duplas usam combinação; filas, pódios e cargos diferentes usam arranjo, que conta a ordem e é maior.
- **"Pelo menos um"**: calcule o total sem restrição e subtraia o caso proibido; C(9, 3) − C(5, 3) = 84 − 10 = 74 trios com pelo menos um menino entre 4 meninos e 5 meninas.
- **Casos particulares**: C(n, n) = C(n, 0) = 1; C(n, 1) = C(n, n − 1) = n; C(n, k) = C(n, n − k).
- **Soma das combinações**: C(n, 0) + ... + C(n, n) = 2ⁿ, útil para somas de várias combinações (por exemplo, 2¹⁰ − 2 = 1022 divisões de 10 pastas em 2 caixas, ambas ocupadas).
- **Triângulo de Pascal**: Stifel (C(n, k) + C(n, k+1) = C(n+1, k+1)), teorema das linhas (soma = 2ⁿ) e teorema das colunas (soma de uma coluna dá o elemento seguinte na linha e coluna seguintes).
- **Combinação completa**: n tipos, p unidades que podem repetir tipos; CR(n, p) = (n − 1 + p)! ÷ [(n − 1)! · p!] = C(n − 1 + p, p); com 5 marcas e 3 potes, CR = 35.
- **Distribuição de itens idênticos**: n pessoas e p itens são n tipos com p unidades; havendo mínimo por pessoa, entrega-se o mínimo primeiro e distribui-se o resto.
- **Soluções inteiras de equações**: x1 + ... + xn = p tem CR(n, p) soluções inteiras não negativas; se exigir positivas, reserva-se 1 por variável e a soma passa a p − n.
- **Por que não negativas**: com valores negativos ou decimais haveria infinitas soluções.

# NOTAS

- Primeira página do trecho começa no meio de uma questão de senhas (opções c, d, e); resumi apenas a ideia do princípio multiplicativo, sem reproduzir o enunciado.
- Alguns símbolos (binomiais, fórmulas em duas linhas) aparecem desordenados no texto extraído; reconstruí as fórmulas e conferi pelas contas das resoluções (C(6,2) = 15; C(9,3) = 84; CR(5,3) = 35; 2.024 soluções).
- O material mostra em figuras (não extraídas) o Triângulo de Pascal, a tabela alternativa e a ilustração com divisórias; reconstruí o conteúdo em texto. A relação n = i + j − 2 e k = j − 1 da tabela alternativa foi conferida com os primeiros elementos.
- Nas questões, os quadros com os números de instrumentistas e as figuras com as barras também não foram extraídos; usei apenas os valores citados nas resoluções.
- Os exemplos numéricos (comissão 6H/4M, 5 engenheiros e 4 médicos, 6 documentos, 11 balas, x + y + z) são próprios.
