---
id: S0450
agente: CLAUDE-L4
materia: Estatística
aula: Aula 01 — Médias
trecho: estatistica/a01/s04
paginas_lidas: 47-58
---
# ANALÍTICO

Este trecho ensina a calcular a média aritmética quando os dados estão agrupados em classes (usando os pontos médios como representantes) e apresenta a média geométrica: definição, fórmula, cálculo por fatoração, aplicações e restrições.

### Média aritmética para dados agrupados em classes

Quando os dados vêm em uma tabela de intervalos com frequências, não se conhecem os valores individuais. O método é **trocar cada classe pelo seu ponto médio** e calcular uma média ponderada pelas frequências.

1. Ponto médio de cada classe: **PM = (limite inferior + limite superior) ÷ 2**.
2. Multiplique cada ponto médio pela frequência da sua classe: **PM × f**.
3. Some a coluna dos produtos e some as frequências.
4. Divida: **média = Σ(PM × f) ÷ Σf**.

> 💡 **Exemplo próprio:** classes 0 a 10 (f = 4), 10 a 20 (f = 6) e 20 a 40 (f = 10). Pontos médios: 5, 15 e 30. Produtos: 20, 90 e 300, somando 410. Total de frequências: 20. Média = 410 ÷ 20 = 20,5.

Pontos de atenção:

- Se a tabela traz **percentuais** (frequências relativas), a soma das frequências é 100% (ou 1,00) e a média é a própria soma dos produtos PM × frequência relativa; a divisão por 1 não altera nada. Pode-se também dividir por 100%, como em qualquer média ponderada.
- As classes podem ter **larguras diferentes** (por exemplo, 0 a 2, 2 a 6, 20 a 30): calcule o PM de cada uma separadamente, sem supor largura constante.
- A média de dados agrupados é uma **aproximação**: ao agrupar, perdemos o valor exato de cada observação, então o resultado costuma diferir um pouco da média calculada com os dados originais. Para a prova, usa-se o valor agrupado quando a tabela é a informação dada.
- Resultado em minutos com parte decimal: converta a fração em segundos multiplicando por 60. Por exemplo, 7,23 min = 7 min + 0,23 × 60 s ≈ 7 min e 14 s. Confira com cuidado qual alternativa corresponde ao resultado calculado.

> 💡 **Exemplo próprio (com percentuais):** classes de idade 20 a 30 (40%), 30 a 40 (35%) e 40 a 60 (25%). PM = 25, 35 e 50. Média = 25 × 0,40 + 35 × 0,35 + 50 × 0,25 = 10 + 12,25 + 12,5 = 34,75 anos.

> ⚠️ **Pegadinha:** as questões misturam perguntas de proporção (ex.: "mais da metade tem menos de 30 anos") com o cálculo da média; avalie cada afirmação separadamente. Num item desse tipo, a primeira parte vem da soma dos percentuais das classes e a segunda do cálculo da média pelos pontos médios.

### Média geométrica: definição

A média geométrica é muito usada quando há **acumulação de percentuais** (finanças) e em geometria (igualar áreas ou volumes). Para **n números não negativos**, é a **raiz n-ésima do produto** deles:

**G = (x1 × x2 × ... × xn)^(1/n)**, isto é, a raiz de índice n do produto.

A ideia é a mesma da média aritmética, mas preservando o **produto** em vez da soma: G é o valor que, colocado no lugar de todos os elementos, mantém o produto da lista (G elevado a n é igual ao produto original).

- Dois números: raiz quadrada do produto; três números: raiz cúbica; e assim por diante. O índice da raiz é sempre a **quantidade de elementos**.
- Só se define para números **não negativos**; com um número negativo a raiz pode não existir nos reais (a média geométrica de 1 e −1 exigiria a raiz de −1).
- Para números positivos, a média geométrica nunca supera a aritmética (G ≤ média aritmética), com igualdade só quando todos os valores são iguais.

### Calculando a raiz sem calculadora: fatoração

Extrair raízes não exatas de cabeça é difícil, então **fatore cada número em primos**, some os expoentes (produto de potências de mesma base) e divida o expoente de cada primo pelo índice da raiz.

> 💡 **Exemplo próprio:** média geométrica de 4, 6 e 9 (raiz cúbica). Fatoração: 4 = 2²; 6 = 2 × 3; 9 = 3². Produto = 2³ × 3³ (somando os expoentes de cada base). Dividindo cada expoente por 3: G = 2 × 3 = 6. Conferência: 4 × 6 × 9 = 216 = 6 × 6 × 6.

### Aplicações

- **Finanças (variações percentuais acumuladas):** o rigor exige usar **fatores de crescimento** (1 + taxa), pois as variações se multiplicam. A taxa média por período é a média geométrica dos fatores menos 1.

> 💡 **Exemplo próprio:** aumentos de 25% e de 80% em dois períodos seguidos. Fatores: 1,25 e 1,80, produto 2,25, raiz quadrada 1,5. A taxa média foi de 50% por período (conferindo: 1,5 × 1,5 = 2,25).

- **Geometria:** o lado de um cubo com o mesmo volume de um prisma retangular é a média geométrica das três dimensões do prisma. Para um prisma de 5 × 10 × 20, o volume é 1.000 e o lado do cubo é a raiz cúbica de 1.000, ou seja, 10 (fatorando: 5 × (2 × 5) × (2² × 5) = 2³ × 5³).
- **Média de notas por raiz do produto:** quando o enunciado manda tirar a raiz quadrada do produto de duas notas, é a média geométrica de duas notas (ex.: notas 3 e 12 geram raiz de 36, que é 6; notas 5 e 20 geram raiz de 100, que é 10).

### Média geométrica ligada a outras médias

Questões podem combinar médias: dadas as médias aritméticas dos pares (a, b), (b, c) e (a, c), monte o sistema de três equações com as somas (a + b, b + c e a + c), resolva por substituição e depois aplique a raiz cúbica do produto a · b · c, usando fatoração para simplificar. A resposta pode ficar na forma de uma raiz não exata (por exemplo, um número inteiro multiplicado por uma raiz cúbica).

### Para fixar
- Dados em classes: troque a classe pelo ponto médio PM = (inferior + superior) ÷ 2 e use média ponderada Σ(PM × f) ÷ Σf.
- Com frequências relativas, a soma das frequências vale 1 (ou 100%) e basta somar os produtos PM × frequência relativa.
- A média agrupada é aproximada e pode diferir da média dos valores originais.
- Média geométrica: raiz n-ésima do produto de n números não negativos; preserva o produto.
- O índice da raiz é a quantidade de elementos (2 números, raiz quadrada; 3, raiz cúbica).
- Para extrair a raiz com facilidade, fatore em primos, some os expoentes e divida pelo índice da raiz.
- Em taxas acumuladas, trabalhe com fatores (1 + taxa) e subtraia 1 no final.
- G ≤ média aritmética para positivos, com igualdade quando todos os valores são iguais.

# SINTÉTICO

- **Dados agrupados em classes**: substitua cada classe pelo ponto médio (inferior + superior, dividido por 2) e calcule média ponderada Σ(PM × f) ÷ Σf.
- **Frequências em percentual**: a soma é 100% (1,00); some os produtos PM × frequência relativa, sem precisar dividir.
- **Aproximação**: ao agrupar, perde-se detalhe; a média agrupada pode diferir da média dos valores originais.
- **Decimais de minuto**: converta a parte decimal em segundos multiplicando por 60 e confira a alternativa com atenção.
- **Média geométrica**: G é a raiz n-ésima do produto de n números não negativos; preserva o produto da lista.
- **Índice da raiz**: acompanha a quantidade de elementos (quadrada para 2 números, cúbica para 3).
- **Fatoração**: decomponha em primos, some os expoentes das mesmas bases e divida pelo índice da raiz para obter G sem calculadora.
- **Taxas acumuladas**: use fatores (1 + taxa); a média geométrica dos fatores menos 1 dá a taxa média por período.
- **Restrições e comparação**: só definida para números não negativos; para positivos, G é menor ou igual à média aritmética.

# NOTAS

- Página 47: o trecho começa no fim de uma questão sobre média (cálculo com frequências); resumi apenas a parte de dados agrupados que vem depois.
- Páginas 49 e 50 (questão do tempo de chamadas): o cálculo do material dá 1700 ÷ 235 ≈ 7,23 min ≈ 7 min e 14 s, que corresponde à alternativa b, mas o gabarito impresso é "D" (7 min e 32 s). Registrei a inconsistência; o resumo ensina o método, que está correto.
- Página 55: o exemplo financeiro do material aplica a raiz cúbica diretamente aos percentuais 3, 8 e 9 (resultado 6%). Do ponto de vista matemático, o rigor financeiro usa fatores (1,03 × 1,08 × 1,09); no resumo ensinei o método com fatores e deixei de fora o exemplo literal. A prova pode seguir o enunciado, então vale conferir o comando da questão.
- Página 49: a média por valor (5,4) citada pelo material depende de uma tabela da página anterior, fora do intervalo; usei apenas a ideia de que o agrupamento altera o resultado.
- Figuras (distribuição de renda da questão do STF, gráfico de notas da questão da prefeitura) não foram extraídas; as questões foram aproveitadas só pelo método.
