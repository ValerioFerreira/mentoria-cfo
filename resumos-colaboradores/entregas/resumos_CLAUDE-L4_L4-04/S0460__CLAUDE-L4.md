---
id: S0460
agente: CLAUDE-L4
materia: Estatística
aula: Aula 04 — Medidas de Variabilidade ou Dispersão
trecho: estatistica/a04/s04
paginas_lidas: 39-49
---
# ANALÍTICO

Este trecho apresenta a **variância**, a medida de dispersão baseada nos quadrados dos desvios em relação à média: o conceito, a diferença entre variância populacional e amostral, as fórmulas (definição e "atalho") para dados não-agrupados, em tabela de frequências simples e em classes, e as duas propriedades que mais caem em prova.

### Conceito e interpretação

Os desvios (xi − média) somam zero, então não podem ser somados diretamente. Uma saída é usar o módulo; outra, mais cômoda para os cálculos, é **elevar ao quadrado**, o que elimina os sinais negativos. A **variância** é o valor médio dos desvios elevados ao quadrado, medidos a partir da média aritmética.

- Quanto **maior** a variância, mais dispersos estão os dados em torno da média.
- Usa todos os valores da variável (e não só os extremos, como a amplitude total), por isso é uma medida **estável**, que complementa as medidas de tendência central.
- É **sempre maior ou igual a zero** (não negativa) e vale **zero quando todos os valores são iguais**: a média coincide com cada valor, e todos os desvios são nulos.
- Sua unidade é o **quadrado da unidade dos dados**: dados em kg geram variância em kg². Esse é um inconveniente na estatística descritiva, mas a variância é fundamental na inferência estatística e na combinação de amostras.

### Variância populacional × amostral

Muda o divisor e o símbolo:

| Característica | Populacional | Amostral |
| --- | --- | --- |
| Símbolo | σ² (sigma ao quadrado) | s² |
| Média usada | μ | x̄ |
| Fórmula (definição) | σ² = Σ(xi − μ)² / n | s² = Σ(xi − x̄)² / (n − 1) |
| Fórmula "atalho" | σ² = média dos quadrados − (média)² | s² = [média dos quadrados − (média)²] × n/(n − 1) |
| Papel | parâmetro populacional | estimador do parâmetro |

Ligação entre as duas: **s² = σ² × n/(n − 1)**, ou seja, a variância amostral é sempre um pouco maior que a populacional calculada sobre os mesmos números.

Por que dividir por n − 1? Em geral não se estuda toda a população, mas uma amostra. Usar n − 1 produz uma estimativa melhor do parâmetro desconhecido. Há uma justificativa intuitiva: os desvios de um conjunto sempre se anulam quando somados, então só n − 1 deles são "livres"; o último fica determinado pelos demais. Para amostras grandes (n > 30), usar n ou n − 1 dá resultados praticamente iguais.

> ⚠️ **Pegadinha:** descubra, pelo enunciado, se os dados são de **população** (todos os elementos, "pesquisa censitária") ou de **amostra**. Se o enunciado fala em "amostra" ou em estimar algo, o divisor é n − 1; se fala em todos os elementos da população, é n.

#### Fórmula "média dos quadrados menos quadrado da média"

Quando a média não é um número redondo, calcular os desvios um a um é trabalhoso. O atalho é: some os quadrados dos valores, divida por n e subtraia o quadrado da média. Para a amostral, multiplique o resultado por n/(n − 1). Em termos de somas:

- população: σ² = [ Σxi² − (Σxi)²/n ] / n
- amostra: s² = [ Σxi² − (Σxi)²/n ] / (n − 1)

> 💡 **Exemplo próprio (população):** dados 2, 4, 4, 4, 5, 5, 7, 9. Média = 40/8 = 5. Pelos desvios: 9 + 1 + 1 + 1 + 0 + 0 + 4 + 16 = 32, então σ² = 32/8 = 4. Pelo atalho: média dos quadrados = (4 + 16 + 16 + 16 + 25 + 25 + 49 + 81)/8 = 232/8 = 29; σ² = 29 − 5² = 4. Se fosse uma amostra: s² = 32/7 ≈ 4,57.

### Dados não-agrupados

Aplicam-se as fórmulas acima diretamente. Procedimento: (1) calcular a média; (2) montar uma tabela com os desvios ao quadrado; (3) somar; (4) dividir por n (população) ou n − 1 (amostra).

> 💡 **Exemplo do trecho:** conjunto {1, 2, 3, 5, 9}: média = 20/5 = 4; quadrados dos desvios: 9, 4, 1, 1, 25, soma 40; variância amostral = 40/4 = 10.

Para os valores 5, 10, 15, 20, 25 (média 15; desvios −10, −5, 0, 5, 10; soma dos quadrados 250): variância amostral = 250/4 = 62,5 e populacional = 250/5 = 50. Veja que a razão entre elas é 5/4, isto é, n/(n − 1).

### Dados agrupados sem intervalos de classe

Com tabela de frequências (valor Xi e frequência fi), cada desvio ao quadrado é ponderado pela frequência; n = Σfi:

- população: σ² = Σ[(Xi − μ)² × fi] / n, ou σ² = [ Σ(Xi² × fi) − (Σ Xi × fi)²/n ] / n
- amostra: s² = Σ[(Xi − x̄)² × fi] / (n − 1), ou s² = [ Σ(Xi² × fi) − (Σ Xi × fi)²/n ] / (n − 1)

A média é x̄ = Σ(Xi × fi) / n. Monta-se uma tabela com as colunas fi, Xi × fi, (Xi − x̄)² e (Xi − x̄)² × fi.

> 💡 **Exemplo próprio:** valores 1, 2 e 3 com frequências 2, 5 e 3 (n = 10). Σ Xi fi = 2 + 10 + 9 = 21, média 2,1. Σ Xi² fi = 2 + 20 + 27 = 49, logo média dos quadrados = 4,9. Variância populacional = 4,9 − 2,1² = 4,9 − 4,41 = 0,49; amostral = 0,49 × 10/9 ≈ 0,544.

### Dados agrupados em classes

As expressões são as mesmas do caso anterior, trocando Xi pelo **ponto médio (PM) da classe** (média dos limites inferior e superior). Convém organizar as colunas fi, PMi, PMi × fi, (PMi − x̄) e (PMi − x̄)² × fi.

> 💡 **Exemplo do trecho (amostra de 40 alturas, 6 classes):** com pontos médios 152, 156, ..., 172, a média ponderada deu 161 cm e a soma dos quadrados dos desvios ponderados deu 1.240; s² = 1.240/39 ≈ 31,79 cm².

> 💡 **Exemplo próprio:** classes 0 ⊢ 10, 10 ⊢ 20, 20 ⊢ 30 com frequências 2, 6 e 2. Pontos médios 5, 15, 25; n = 10; média = 15. Soma de (PM − 15)² × f = 100 × 2 + 0 + 100 × 2 = 400. Variância populacional = 40; amostral = 400/9 ≈ 44,4.

> ⚠️ **Pegadinha:** no agrupamento em classes, todos os valores da classe são tratados como se fossem o ponto médio, então o resultado é uma aproximação. Atenção também à unidade: a variância sai em unidade ao quadrado (cm², kg²).

### Propriedades da variância

**1ª propriedade: somar ou subtrair uma constante c de todos os valores não altera a variância.** A média se desloca na mesma quantidade, e os desvios continuam iguais. Exemplo: {1, 3, 5, 7, 9} tem variância 8; somando 5 a cada valor, o novo conjunto {6, 8, 10, 12, 14} segue com variância 8.

**2ª propriedade: multiplicar ou dividir todos os valores por uma constante c multiplica ou divide a variância pelo QUADRADO de c.** Exemplo: ao multiplicar {1, 3, 5, 7, 9} por 5, a variância passa de 8 para 200 = 8 × 5².

| Operação nos dados | Efeito na variância |
| --- | --- |
| x + c ou x − c | não muda |
| x × c | multiplica por c² |
| x ÷ c | divide por c² |

> 💡 **Exemplo próprio:** se um conjunto tem variância 12 e todos os valores são multiplicados por 3 e depois acrescidos de 10, a nova variância é 12 × 9 = 108 (o acréscimo de 10 não interfere).

> ⚠️ **Pegadinha:** o erro comum é multiplicar a variância por c (e não por c²) ou achar que somar uma constante também aumenta a variância.

### Para fixar
- Variância = média dos quadrados dos desvios em relação à média; mede dispersão; é sempre ≥ 0 e zero só quando todos os valores são iguais.
- Populacional: σ² = Σ(xi − μ)²/n; amostral: s² = Σ(xi − x̄)²/(n − 1); relação s² = σ² × n/(n − 1).
- Atalho: média dos quadrados menos o quadrado da média (população); multiplicar por n/(n − 1) para a amostra.
- Dados em tabela: ponderar por fi (n = Σfi); em classes: usar o ponto médio da classe no lugar de Xi.
- A unidade da variância é o quadrado da unidade dos dados (kg², cm²).
- Somar ou subtrair constante não muda a variância; multiplicar ou dividir por c altera a variância por c².
- Para n > 30, as diferenças entre dividir por n e por n − 1 são desprezíveis; ainda assim, siga o que o enunciado pede.

# SINTÉTICO

- **Conceito**: variância é a média dos quadrados dos desvios em torno da média; quanto maior, mais dispersos os dados; é sempre ≥ 0 e vale zero se todos os valores forem iguais.
- **População × amostra**: σ² divide por n e usa μ; s² divide por n − 1 e usa x̄; vale s² = σ² × n/(n − 1).
- **Por que n − 1**: gera melhor estimativa do parâmetro populacional; com n > 30 a diferença é irrelevante.
- **Atalho de cálculo**: σ² = média dos quadrados − (média)²; para a amostra, multiplique por n/(n − 1).
- **Exemplo**: {1, 2, 3, 5, 9} tem média 4, soma dos quadrados dos desvios 40 e s² = 10; para 5, 10, 15, 20, 25, s² = 62,5 e σ² = 50.
- **Tabela de frequências**: pondere por fi e use n = Σfi; a média é Σ(Xi × fi)/n.
- **Classes**: troque Xi pelo ponto médio da classe; o resultado é aproximado.
- **Unidade**: a variância é expressa em unidade ao quadrado (kg², cm²), por isso o desvio padrão é mais intuitivo, e a variância pesa na inferência estatística.
- **Soma/subtração de constante**: não altera a variância.
- **Multiplicação/divisão por constante c**: multiplica/divide a variância por c², não por c; multiplicar por 5 leva a variância de 8 para 200.

# NOTAS

Páginas 39-49 legíveis; as fórmulas com somatório foram recompostas pelo contexto, e todos os números foram refeitos e conferidos. Divergências com a fonte: (1) o material diz que a variância "sempre tem valor positivo"; o correto é não negativa (≥ 0), pois vale zero quando todos os valores são iguais; foi usado o correto. (2) No exemplo da tabela de filhos por professor, o texto pede variância amostral, mas a nota da tabela diz "pesquisa populacional", e o resultado final é 29/19 ≈ 1,526 (o texto arredonda para 1,52, o correto é 1,53); além disso o texto chama a fórmula de "desvio padrão amostral" quando calcula a variância. Esse exemplo não foi reproduzido; usei exemplos próprios. (3) No exemplo das estaturas a nota da tabela também diz "pesquisa populacional" em uma das tabelas, enquanto o cálculo é amostral (n − 1). Os resultados numéricos usados (média 161, soma 1.240, s² ≈ 31,79) estão corretos.
