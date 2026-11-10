---
id: rl-operacoes-conjuntos
subject: raciocinio-logico
title: Operações com conjuntos: união, interseção, diferença, complementar e contagem de elementos
short: Operações com conjuntos
subtitle: Item 14 do edital de Raciocínio Lógico: conceitos, relações, operações, propriedades e problemas de contagem com diagramas de Venn
weight: 0.06
order: 1
resolves: rl-operacoes-conjuntos
onlyContests: "PCPE_AGENTE"
---

## O que este material cobre e como estudar

Pessoal, o item 14 do edital de Raciocínio Lógico pede **operações com conjuntos**. Na prova, isso aparece de duas formas:

1. **Questões diretas de teoria** (julgar se uma operação ou uma relação está correta: união, interseção, diferença, complementar, subconjunto, conjunto das partes);
2. **Problemas de contagem** com diagramas de Venn: "numa pesquisa com 80 pessoas, 45 usam A, 38 usam B..., quantas usam apenas um?". É aqui que mais se erra, por causa das palavras *apenas*, *pelo menos* e *nem... nem*.

> **Roteiro de estudo:** leia as seções 1 a 4 uma vez, rápido (são definições). Gaste o seu tempo nas seções 5 e 6 e refaça os exemplos sem olhar a resolução.

## 1. Conjunto, elemento e pertinência

Um **conjunto** é uma coleção de objetos, chamados **elementos**. Cada elemento pertence ou não ao conjunto; não existe "meio pertence".

- **Pertinência:** x ∈ A (x pertence a A) e x ∉ A (x não pertence a A). A relação de pertinência liga **elemento** e **conjunto**.
- **Formas de descrever um conjunto:**
  - por **listagem** (extensão): A = {2, 4, 6, 8};
  - por **propriedade** (compreensão): A = {x | x é par e 2 ≤ x ≤ 8};
  - por **diagrama de Venn**: uma região fechada que contém os elementos.
- **Número de elementos** de um conjunto finito A: n(A) (também escrito |A| ou #A). Para A = {2, 4, 6, 8}, n(A) = 4.
- **Igualdade:** dois conjuntos são iguais quando têm exatamente os mesmos elementos. A **ordem** e as **repetições** não importam: {1, 2, 3} = {3, 2, 1, 1}.

### Conjuntos especiais

| Conjunto | Definição | Exemplo |
|---|---|---|
| **Vazio** (∅ ou { }) | não tem elemento algum; n(∅) = 0 | {x | x é par e ímpar ao mesmo tempo} |
| **Unitário** | tem um único elemento | {x | x é primo e par} = {2} |
| **Universo** (U) | contém todos os elementos que a situação considera | os agentes de uma delegacia |
| **Finito / infinito** | pode ou não ser contado até o fim | {1, 2, 3} é finito; os naturais são infinitos |

> **Pegadinha:** ∅ **não** é o mesmo que {∅}. O primeiro não tem elementos; o segundo tem **um** elemento (o próprio conjunto vazio). Também {0} **não** é vazio: tem o elemento zero.

## 2. Relação entre conjuntos: inclusão e conjunto das partes

- **Subconjunto:** A ⊂ B (A está contido em B) quando **todo elemento de A também é elemento de B**. Também se escreve B ⊃ A (B contém A). A negação é A ⊄ B (há ao menos um elemento de A que não está em B).
- **Propriedades:** A ⊂ A (todo conjunto está contido em si mesmo); ∅ ⊂ A (o vazio é subconjunto de **qualquer** conjunto); se A ⊂ B e B ⊂ C, então A ⊂ C (transitiva); se A ⊂ B e B ⊂ A, então A = B.
- **Subconjunto próprio:** A ⊂ B e A ≠ B.

> **Pegadinha clássica da prova (símbolos):**
> - **∈ e ∉** relacionam **elemento com conjunto**: 2 ∈ {1, 2, 3}. Mas {2} ⊂ {1, 2, 3} (aqui {2} é um **conjunto**).
> - **⊂ e ⊄** relacionam **conjunto com conjunto**.
> - Escrever "2 ⊂ {1, 2, 3}" ou "{2} ∈ {1, 2, 3}" é erro de notação (item **errado**).

### Conjunto das partes

O **conjunto das partes** de A, indicado por P(A), é o conjunto de **todos os subconjuntos** de A (incluindo ∅ e o próprio A). Se A tem **n** elementos, então P(A) tem **2ⁿ** elementos.

> **Exemplo 1.** A = {1, 2, 3} tem n = 3, logo 2³ = **8 subconjuntos**: ∅, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}. Desses, **7** são subconjuntos próprios (todos menos o próprio A), e **6** são não vazios e próprios.

Por quê 2ⁿ? Para formar um subconjunto, cada elemento tem duas opções (entra ou não entra): 2 × 2 × ... × 2 (n vezes), pelo princípio multiplicativo.

## 3. As operações com conjuntos

Sejam A e B conjuntos do universo U.

### 3.1 União (A ∪ B)

É o conjunto dos elementos que pertencem a **A ou B (ou a ambos)**. É o "ou" inclusivo da lógica.

> A = {1, 2, 3, 4} e B = {3, 4, 5}: **A ∪ B = {1, 2, 3, 4, 5}**. O 3 e o 4 aparecem uma vez só.

### 3.2 Interseção (A ∩ B)

É o conjunto dos elementos que pertencem a **A e B** simultaneamente. É o "e" da lógica.

> Com os mesmos conjuntos: **A ∩ B = {3, 4}**.

Dois conjuntos cuja interseção é vazia (A ∩ B = ∅) são **disjuntos** (ou mutuamente excludentes).

### 3.3 Diferença (A − B ou A \ B)

É o conjunto dos elementos de **A que não estão em B**.

> A − B = {1, 2} e B − A = {5}. **A diferença não é comutativa:** em geral A − B ≠ B − A.

Vale sempre A − B = A ∩ B̄ (elementos de A **e** não de B), em que B̄ é o complementar de B.

### 3.4 Complementar (Ā, Aᶜ ou ∁ᵤA)

É o conjunto dos elementos do **universo** que **não** pertencem a A: Ā = U − A. É a "negação" da lógica. O complementar depende do universo escolhido.

> U = {1, 2, ..., 10} e A = {números pares} = {2, 4, 6, 8, 10}: Ā = {1, 3, 5, 7, 9}. Observe que **A ∪ Ā = U** e **A ∩ Ā = ∅**.

### 3.5 Diferença simétrica (A Δ B)

É o conjunto dos elementos que estão em **exatamente um** dos dois conjuntos (em A ou em B, mas não em ambos): A Δ B = (A − B) ∪ (B − A) = (A ∪ B) − (A ∩ B). Corresponde ao "ou exclusivo" (ou... ou...).

> Com A = {1, 2, 3, 4} e B = {3, 4, 5}: A − B = {1, 2}; B − A = {5}; **A Δ B = {1, 2, 5}**.

### 3.6 Produto cartesiano (A × B)

É o conjunto dos **pares ordenados** (a, b), com a ∈ A e b ∈ B. Se n(A) = m e n(B) = p, então **n(A × B) = m · p**. A ordem importa: (1, 2) ≠ (2, 1), e em geral A × B ≠ B × A.

> A = {1, 2} e B = {x, y, z}: A × B tem 2 × 3 = 6 pares: (1,x), (1,y), (1,z), (2,x), (2,y), (2,z).

## 4. Propriedades das operações

| Propriedade | Para a união | Para a interseção |
|---|---|---|
| **Comutativa** | A ∪ B = B ∪ A | A ∩ B = B ∩ A |
| **Associativa** | (A ∪ B) ∪ C = A ∪ (B ∪ C) | (A ∩ B) ∩ C = A ∩ (B ∩ C) |
| **Distributiva** | A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) | A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) |
| **Idempotência** | A ∪ A = A | A ∩ A = A |
| **Elemento neutro** | A ∪ ∅ = A | A ∩ U = A |
| **Elemento absorvente** | A ∪ U = U | A ∩ ∅ = ∅ |
| **Absorção** | A ∪ (A ∩ B) = A | A ∩ (A ∪ B) = A |

### Leis de De Morgan para conjuntos

- **O complementar da união é a interseção dos complementares:** complementar de (A ∪ B) = Ā ∩ B̄ ("nem A nem B").
- **O complementar da interseção é a união dos complementares:** complementar de (A ∩ B) = Ā ∪ B̄ ("não ambos").
- **Dupla complementação:** o complementar de Ā é o próprio A.

### Relação com a lógica proposicional

Reconheça que as regras são as mesmas que você já usa na lógica:

| Conjuntos | Lógica | Leitura |
|---|---|---|
| A ∪ B | p ∨ q | "ou" |
| A ∩ B | p ∧ q | "e" |
| Ā (complementar) | ~p | "não" |
| A Δ B | p ⊻ q | "ou... ou..." |
| A ⊂ B | p → q | "todo A é B" |
| A = B | p ↔ q | "se e somente se" |

Por isso as propriedades da seção 4 e as Leis de De Morgan valem nos dois mundos: se você as decorou na lógica, já sabe aqui.

## 5. Número de elementos: a fórmula de inclusão-exclusão

### 5.1 Dois conjuntos

- **n(A ∪ B) = n(A) + n(B) − n(A ∩ B)** (subtrai-se a interseção porque ela foi contada duas vezes).
- **n(A − B) = n(A) − n(A ∩ B)** (só A).
- **n(Ā) = n(U) − n(A)** (complementar).
- **Quem não está em nenhum:** n(Ā ∩ B̄) = n(U) − n(A ∪ B).
- **Exatamente um dos dois:** n(A Δ B) = n(A) + n(B) − 2 · n(A ∩ B).

> **Exemplo 2.** Num grupo de 60 agentes, 35 fizeram o curso de tiro (T), 28 o de direção defensiva (D) e 12 fizeram os dois. Quantos fizeram:
> a) pelo menos um dos cursos? n(T ∪ D) = 35 + 28 − 12 = **51**.
> b) nenhum? 60 − 51 = **9**.
> c) somente tiro? 35 − 12 = **23**. Somente direção defensiva? 28 − 12 = **16**.
> d) exatamente um? 23 + 16 = **39** (ou 35 + 28 − 2 · 12 = 39).

### 5.2 Máximos e mínimos

Quando o enunciado não dá a interseção, ela fica **entre dois limites**:

- A interseção **não pode** ser maior que o menor dos conjuntos: n(A ∩ B) ≤ min{n(A), n(B)}.
- A interseção **não pode** ser menor que n(A) + n(B) − n(U) (nem menor que zero).

> **Exemplo 3.** Num universo de 40 pessoas, n(A) = 30 e n(B) = 25. Quantas, no mínimo, estão em A e B? Mínimo: 30 + 25 − 40 = **15** (se os dois conjuntos "quase cobrem" o universo, a sobreposição é forçada). Máximo: **25** (B inteiro dentro de A).

### 5.3 Três conjuntos

**n(A ∪ B ∪ C) = n(A) + n(B) + n(C) − n(A ∩ B) − n(A ∩ C) − n(B ∩ C) + n(A ∩ B ∩ C)**

Subtraem-se as interseções duas a duas e **soma-se de volta** a interseção tripla (ela foi somada três vezes, subtraída três vezes e ficou fora).

Na prática, **não decore a fórmula: use o diagrama de Venn** e preencha do **centro para fora**:

1. a interseção **tripla**;
2. as regiões de **duas** interseções (cada interseção dupla **menos** a tripla);
3. as regiões **só** de cada conjunto (o total do conjunto **menos** tudo o que já foi preenchido nele);
4. o que ficou **fora** de todos (o universo menos a união).

> **Exemplo 4.** Uma pesquisa com 100 pessoas sobre três canais: n(A) = 50, n(B) = 45, n(C) = 40, n(A ∩ B) = 20, n(A ∩ C) = 15, n(B ∩ C) = 12 e n(A ∩ B ∩ C) = 6.
>
> | Região | Cálculo | Valor |
> |---|---|---|
> | A, B e C | dado | **6** |
> | só A e B | 20 − 6 | **14** |
> | só A e C | 15 − 6 | **9** |
> | só B e C | 12 − 6 | **6** |
> | só A | 50 − 14 − 9 − 6 | **21** |
> | só B | 45 − 14 − 6 − 6 | **19** |
> | só C | 40 − 9 − 6 − 6 | **19** |
> | nenhum | 100 − (6 + 14 + 9 + 6 + 21 + 19 + 19) | **6** |
>
> União: 94. Exatamente um canal: 21 + 19 + 19 = **59**. Exatamente dois: 14 + 9 + 6 = **29**. Pelo menos dois: 29 + 6 = **35**. Nenhum: **6**.

## 6. Vocabulário que decide a questão

Quase todo erro de contagem vem da leitura. Traduza a frase para regiões do diagrama:

| Expressão | Região do Venn (dois conjuntos A e B) |
|---|---|
| "A **ou** B", "pelo menos um" | A ∪ B (tudo dentro dos círculos) |
| "A **e** B", "ambos" | A ∩ B |
| "**apenas** A", "somente A", "A e não B" | A − B (A sem a interseção) |
| "**exatamente um**" | (A − B) + (B − A) |
| "**nem** A **nem** B", "nenhum" | fora dos dois círculos |
| "**não** A" | tudo que está fora de A (inclui B − A e o exterior) |
| "pelo menos dois" (três conjuntos) | duas interseções + a tripla |
| "**no máximo** um" (três conjuntos) | só um + nenhum |

> **Atenção:** quando o enunciado diz "35 fazem tiro", esses 35 incluem quem também faz direção defensiva (é o total do conjunto). "Apenas tiro" é outra coisa (no exemplo, 23). Confundir *total do conjunto* com *apenas* é o erro número um.

### Eventos e conjuntos

Em probabilidade, os eventos são conjuntos do espaço amostral, e P(A ∪ B) = P(A) + P(B) − P(A ∩ B) é a fórmula da inclusão-exclusão dividida pelo total. Dominar esta seção ajuda também nas questões de probabilidade.

## 7. Exemplos para julgar (estilo certo ou errado)

1. **Dados A = {1, 2, 3} e B = {2, 3, 4, 5}, tem-se A ∪ B = {1, 2, 3, 4, 5} e A ∩ B = {2, 3}.** *Certo.*
2. **Se A = {a, b}, então {a} ∈ A.** *Errado:* {a} é um conjunto e deveria vir com ⊂ ({a} ⊂ A); o elemento é a, então a ∈ A.
3. **O conjunto das partes de um conjunto com 4 elementos possui 16 elementos.** *Certo:* 2⁴ = 16.
4. **A − B = B − A para quaisquer conjuntos A e B.** *Errado:* a diferença não é comutativa; a igualdade só ocorre no caso particular A = B (as duas diferenças ficam vazias).
5. **O complementar de A ∪ B é Ā ∪ B̄.** *Errado:* é Ā ∩ B̄ (De Morgan).
6. **Se A ⊂ B, então A ∪ B = B e A ∩ B = A.** *Certo.*
7. **Num universo de 50 pessoas, 30 leem jornal e 25 leem revista; então ao menos 5 leem os dois.** *Certo:* 30 + 25 − 50 = 5 é o mínimo forçado.
8. **Se n(A) = 12, n(B) = 9 e n(A ∩ B) = 4, então n(A ∪ B) = 21.** *Errado:* é 12 + 9 − 4 = **17**. Quem soma direto 12 + 9 caiu na pegadinha clássica de esquecer de subtrair a interseção.
9. **Nas mesmas condições do item anterior, n(A Δ B) = 13.** *Certo:* 12 + 9 − 2 · 4 = 13 (são os que estão em exatamente um dos conjuntos).

## 8. Resumo para revisão

- ∈ liga elemento a conjunto; ⊂ liga conjunto a conjunto; ∅ está contido em qualquer conjunto e P(A) tem 2ⁿ elementos.
- União = "ou"; interseção = "e"; diferença = "e não"; complementar = "não"; diferença simétrica = "ou exclusivo".
- De Morgan: complementar da união = interseção dos complementares; complementar da interseção = união dos complementares.
- n(A ∪ B) = n(A) + n(B) − n(A ∩ B); com três conjuntos, preencha o Venn do centro para fora.
- Cuidado: *total do conjunto* ≠ *apenas*; *pelo menos um* = união; *nem... nem* = fora de tudo.

## Fontes

Conteúdo elaborado a partir da teoria elementar de conjuntos, de conhecimento didático padrão de Matemática (ensino médio e superior) e do item 14 do edital do concurso de Agente de Polícia da PCPE (Cebraspe). Os exemplos numéricos foram conferidos por cálculo direto. Consulta e revisão em 19/10/2026.
