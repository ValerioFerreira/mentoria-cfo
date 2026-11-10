---
id: rl-matrizes-determinantes
subject: raciocinio-logico
title: Matrizes e determinantes: operações, propriedades, inversa e problemas matriciais
short: Matrizes e determinantes
subtitle: Item 15 do edital de Raciocínio Lógico (problemas matriciais): tipos de matriz, operações, determinantes, matriz inversa e aplicações em sistemas e tabelas
weight: 0.06
order: 2
resolves: rl-matrizes-determinantes
onlyContests: "PCPE_AGENTE"
---

## O que este material cobre e como estudar

Pessoal, o item 15 do edital fala em "problemas aritméticos, geométricos e **matriciais**". Os dois primeiros você domina com a matemática básica; os **matriciais** são o assunto deste material. Os sistemas lineares em si (item 5) são tratados em outra parte; aqui você aprende a **linguagem das matrizes**, as **operações**, os **determinantes** e a **matriz inversa**, que é o que a banca costuma explorar.

> **Dica de prova:** a banca raramente pede contas enormes. O comum é: (a) montar uma matriz a partir de uma lei de formação; (b) multiplicar duas matrizes pequenas (2×2 ou 2×3 por 3×1) ou conferir se a multiplicação é possível; (c) calcular um determinante 2×2 ou 3×3; (d) usar uma **propriedade** para dispensar a conta; e (e) julgar afirmações sobre matriz inversa e transposta.

## 1. O que é uma matriz

Uma **matriz** é uma tabela de números organizados em **linhas** (horizontais) e **colunas** (verticais). Uma matriz com **m linhas** e **n colunas** tem **ordem m × n** ("m por n", sempre linhas primeiro) e m · n elementos.

O elemento da **linha i e coluna j** é escrito **aᵢⱼ**. Exemplo, em A = (aᵢⱼ) de ordem 2 × 3:

A = | a₁₁ a₁₂ a₁₃ |
    | a₂₁ a₂₂ a₂₃ |

> **Exemplo 1 (lei de formação).** Seja A de ordem 2 × 3 com aᵢⱼ = i · j − 1. Então a₁₁ = 0, a₁₂ = 1, a₁₃ = 2, a₂₁ = 1, a₂₂ = 3, a₂₃ = 5. Logo A = | 0 1 2 | / | 1 3 5 |.

### Tipos de matriz

| Tipo | Característica |
|---|---|
| **Linha** | só uma linha (1 × n) |
| **Coluna** | só uma coluna (m × 1) |
| **Quadrada** | m = n (a "ordem n" basta); tem **diagonal principal** (aᵢᵢ) e **secundária** |
| **Nula** | todos os elementos iguais a zero |
| **Identidade (I)** | quadrada com 1 na diagonal principal e 0 fora dela |
| **Diagonal** | quadrada com elementos fora da diagonal principal nulos |
| **Triangular** | quadrada com todos os elementos acima (ou abaixo) da diagonal principal nulos |
| **Transposta (Aᵗ)** | troca linhas por colunas: (Aᵗ)ᵢⱼ = aⱼᵢ |
| **Simétrica** | quadrada com A = Aᵗ (aᵢⱼ = aⱼᵢ) |
| **Antissimétrica** | quadrada com Aᵗ = −A (diagonal nula) |
| **Oposta (−A)** | troca o sinal de todos os elementos |

Duas matrizes são **iguais** quando têm a **mesma ordem** e os **mesmos elementos nas posições correspondentes**.

## 2. Operações com matrizes

### 2.1 Soma e subtração

Só se somam (ou subtraem) matrizes de **mesma ordem**, elemento a elemento. A soma é **comutativa** e **associativa**, e o elemento neutro é a matriz nula.

> **Exemplo 2.** A = | 1 2 | / | 3 4 | e B = | 0 1 | / | −1 2 |. Então A + B = | 1 3 | / | 2 6 | e A − B = | 1 1 | / | 4 2 |.

### 2.2 Multiplicação por um número

Multiplica-se **todos** os elementos pelo número: 2A = | 2 4 | / | 6 8 |.

### 2.3 Multiplicação de matrizes

> **Condição de existência:** o produto A · B só existe se **o número de colunas de A for igual ao número de linhas de B**. Se A é m × n e B é n × p, então A · B é **m × p**.

Cada elemento cᵢⱼ do produto é a soma dos produtos da **linha i de A** pela **coluna j de B**: cᵢⱼ = aᵢ₁b₁ⱼ + aᵢ₂b₂ⱼ + ... + aᵢₙbₙⱼ.

> **Exemplo 3.** Com A = | 1 2 | / | 3 4 | e B = | 0 1 | / | −1 2 |:
> A · B = | 1·0 + 2·(−1)  1·1 + 2·2 | / | 3·0 + 4·(−1)  3·1 + 4·2 | = | −2 5 | / | −4 11 |.
> B · A = | 0·1 + 1·3  0·2 + 1·4 | / | −1·1 + 2·3  −1·2 + 2·4 | = | 3 4 | / | 5 6 |.
> Veja que **A · B ≠ B · A**.

#### Propriedades da multiplicação

- **Em geral não é comutativa:** A · B ≠ B · A (e pode existir um produto sem existir o outro).
- É **associativa**: (A · B) · C = A · (B · C) e **distributiva**: A · (B + C) = A · B + A · C.
- **Elemento neutro:** A · I = I · A = A (I identidade de mesma ordem).
- **Não vale o anulamento:** A · B = 0 não implica A = 0 ou B = 0.
- **Potência** (só para quadradas): A² = A · A, e assim por diante. Atenção: (A + B)² ≠ A² + 2AB + B² em geral (porque AB ≠ BA).
- **Transposta do produto:** **(A · B)ᵗ = Bᵗ · Aᵗ** (a ordem se inverte). Além disso, (A + B)ᵗ = Aᵗ + Bᵗ e (Aᵗ)ᵗ = A.

### 2.4 Aplicação: tabelas de dados

Matrizes servem para **organizar tabelas** e fazer contas de uma só vez.

> **Exemplo 4.** Duas lojas vendem três produtos. A matriz Q (lojas × produtos) traz as quantidades vendidas: Q = | 10 5 2 | / | 8 0 6 |. Os preços unitários dos produtos formam a matriz P (produtos × 1) = | 3 | / | 4 | / | 5 |. A receita de cada loja é Q · P (2×3 por 3×1 resulta em 2×1):
> Loja 1: 10·3 + 5·4 + 2·5 = 60; Loja 2: 8·3 + 0·4 + 6·5 = 54. Logo Q · P = | 60 | / | 54 |.

## 3. Determinante

O **determinante** é um número associado a cada **matriz quadrada** (det A ou |A|).

### 3.1 Ordens 1, 2 e 3

- **Ordem 1:** det [a] = a.
- **Ordem 2:** diagonal principal menos diagonal secundária: **det | a b | / | c d | = ad − bc**.
- **Ordem 3 (regra de Sarrus):** repetem-se as duas primeiras colunas à direita da matriz; somam-se os produtos das três diagonais "descendentes" e subtrai-se a soma dos produtos das três "ascendentes".

> **Exemplo 5.** M = | 2 1 3 | / | 0 4 1 | / | 1 0 2 |.
> Descendentes: 2·4·2 + 1·1·1 + 3·0·0 = 16 + 1 + 0 = 17. Ascendentes: 3·4·1 + 2·1·0 + 1·0·2 = 12.
> **det M = 17 − 12 = 5.**
> Conferência por Laplace na 1ª coluna: 2·(4·2 − 1·0) + 0 + 1·(1·1 − 3·4) = 16 − 11 = 5.

### 3.2 Menor complementar, cofator e Laplace

- **Menor complementar** Mᵢⱼ: determinante da submatriz obtida eliminando a linha i e a coluna j.
- **Cofator** Cᵢⱼ = (−1)ⁱ⁺ʲ · Mᵢⱼ.
- **Teorema de Laplace:** o determinante é a soma dos produtos dos elementos de **uma fila qualquer** (linha ou coluna) pelos respectivos cofatores. Escolha a fila com mais zeros para facilitar.

### 3.3 Propriedades dos determinantes (as que mais caem)

| Propriedade | Efeito |
|---|---|
| **det A = det Aᵗ** | a transposta tem o mesmo determinante |
| Fila (linha ou coluna) **nula** | det = 0 |
| Duas filas paralelas **iguais ou proporcionais** | det = 0 |
| Uma fila é **combinação linear** das outras | det = 0 |
| **Troca** de duas filas paralelas | o determinante **muda de sinal** |
| **Multiplicar** uma fila por k | o determinante fica multiplicado por k |
| **det(k · A) = kⁿ · det A** (A de ordem n) | k multiplica todas as n filas |
| **Somar a uma fila um múltiplo de outra** (Jacobi) | o determinante **não muda** |
| Matriz **triangular** ou **diagonal** | det = produto dos elementos da diagonal principal |
| **det(A · B) = det A · det B** (Binet) | o determinante do produto é o produto dos determinantes |
| **det(I) = 1** e **det(Aⁿ) = (det A)ⁿ** | consequências de Binet |

> **Exemplo 6.** Para a matriz M do exemplo 5 (ordem 3, det M = 5), det(2M) = 2³ · 5 = **40** (e não 2 · 5 = 10). A pegadinha é multiplicar uma matriz inteira: k elevado à **ordem**.

> **Exemplo 7.** | 3 1 | / | 6 2 | tem a 2ª linha igual ao dobro da 1ª (linhas proporcionais). Sem conta: det = 0. Conferindo: 3·2 − 1·6 = 0.

## 4. Matriz inversa

A **inversa** de uma matriz quadrada A é a matriz **A⁻¹** tal que **A · A⁻¹ = A⁻¹ · A = I**.

- **Existe** (a matriz é "invertível" ou "não singular") **se e somente se det A ≠ 0**. Com det A = 0, a matriz é singular e não tem inversa.
- **Inversa 2 × 2:** para A = | a b | / | c d | com det A = ad − bc ≠ 0:
  **A⁻¹ = (1/det A) · | d −b | / | −c a |** (troca-se a diagonal principal, muda-se o sinal da secundária e divide-se pelo determinante).
- **Propriedades:** (A⁻¹)⁻¹ = A; **(A · B)⁻¹ = B⁻¹ · A⁻¹** (inverte a ordem); **det(A⁻¹) = 1/det A**; (Aᵗ)⁻¹ = (A⁻¹)ᵗ.

> **Exemplo 8.** A = | 1 2 | / | 3 4 |: det A = 1·4 − 2·3 = −2 ≠ 0. A⁻¹ = (1/−2) · | 4 −2 | / | −3 1 | = | −2 1 | / | 3/2 −1/2 |.
> Verificação rápida: a 1ª linha de A⁻¹ vezes a 1ª coluna de A = −2·1 + 1·3 = 1 e a 1ª linha de A⁻¹ vezes a 2ª coluna de A = −2·2 + 1·4 = 0, como na identidade.

## 5. Aplicação em sistemas lineares

Um sistema com n equações e n incógnitas pode ser escrito como **A · X = B**, em que A é a matriz dos coeficientes, X a coluna das incógnitas e B a coluna dos termos independentes.

- Se **det A ≠ 0**, o sistema tem **solução única**: **X = A⁻¹ · B**.
- **Regra de Cramer:** cada incógnita é xᵢ = Dᵢ/D, em que **D = det A** e Dᵢ é o determinante de A com a coluna i trocada pela coluna B.
- Se **D = 0**, o sistema é **impossível** (sem solução) ou **possível e indeterminado** (infinitas soluções): é preciso examinar o restante (por exemplo, os Dᵢ).

> **Exemplo 9.** Resolva x + 2y = 5 e 3x + 4y = 11. D = 1·4 − 2·3 = −2. Dₓ = 5·4 − 2·11 = −2 e D_y = 1·11 − 5·3 = −4. Logo x = −2/−2 = **1** e y = −4/−2 = **2**. Pela inversa do exemplo 8: X = A⁻¹ · | 5 | / | 11 | = | −2·5 + 1·11 | / | 1,5·5 − 0,5·11 | = | 1 | / | 2 |. Mesmo resultado.

> **Exemplo 10.** Para 2x + 3y = 12 e x + 4y = 11: D = 2·4 − 3·1 = 5; Dₓ = 12·4 − 3·11 = 15; D_y = 2·11 − 1·12 = 10. Logo **x = 3** e **y = 2**.

## 6. Pegadinhas frequentes

1. **Ordem m × n:** primeiro linhas, depois colunas. A ordem do produto é "linhas de A × colunas de B".
2. **A · B ≠ B · A.** Se a prova pergunta "A · B = B · A?", a resposta, em geral, é **não**.
3. **(A · B)ᵗ = Bᵗ · Aᵗ** e **(A · B)⁻¹ = B⁻¹ · A⁻¹** (ordem invertida nos dois casos).
4. **det(A + B) ≠ det A + det B** (não é linear na soma).
5. **det(kA) = kⁿ · det A**; para multiplicar só **uma linha** por k, vale det × k.
6. **Matriz com linhas proporcionais ou fila nula** tem determinante zero e, portanto, **não tem inversa**.
7. **Soma de matrizes** exige mesma ordem; **produto** exige colunas de A = linhas de B.

## 7. Exemplos para julgar (estilo certo ou errado)

1. **O produto de uma matriz 2 × 3 por uma matriz 3 × 4 é uma matriz 2 × 4.** *Certo.*
2. **A matriz 3 × 2 multiplicada pela matriz 3 × 2 existe e resulta numa matriz 3 × 2.** *Errado:* as colunas da primeira (2) não coincidem com as linhas da segunda (3).
3. **Se det A = 5 e A é de ordem 3, então det(2A) = 10.** *Errado:* é 2³ · 5 = 40.
4. **Uma matriz quadrada com duas linhas iguais tem determinante nulo e não admite inversa.** *Certo.*
5. **Se A e B são quadradas de mesma ordem, então (A · B)ᵗ = Aᵗ · Bᵗ.** *Errado:* é Bᵗ · Aᵗ.
6. **A matriz | 2 3 | / | 1 4 | tem determinante 5, logo possui inversa.** *Certo:* 2·4 − 3·1 = 5 ≠ 0.
7. **Se A · B = 0, então A = 0 ou B = 0.** *Errado:* o anulamento do produto não vale para matrizes.
8. **A transposta de uma matriz simétrica é igual a ela mesma.** *Certo.*

## 8. Resumo para revisão

- Ordem m × n; produto A (m×n) · B (n×p) = m × p; **não é comutativo**.
- det 2×2 = ad − bc; 3×3 por Sarrus ou Laplace; det(kA) = kⁿ det A; Binet: det(AB) = det A · det B.
- Fila nula, filas iguais ou proporcionais ⇒ det = 0; troca de filas ⇒ muda o sinal; Jacobi não altera.
- Inversa existe ⇔ det ≠ 0; 2×2: troca a diagonal principal, muda o sinal da secundária e divide pelo det.
- (AB)ᵗ = BᵗAᵗ e (AB)⁻¹ = B⁻¹A⁻¹.
- Sistema quadrado: D ≠ 0 ⇒ solução única (Cramer ou A⁻¹B).

## Fontes

Conteúdo elaborado a partir da teoria padrão de Álgebra Linear elementar e de Matemática do ensino médio (matrizes, determinantes e sistemas lineares) e do item 15 do edital do concurso de Agente de Polícia da PCPE (Cebraspe). Todos os exemplos numéricos foram conferidos por cálculo direto. Consulta e revisão em 19/10/2026.
