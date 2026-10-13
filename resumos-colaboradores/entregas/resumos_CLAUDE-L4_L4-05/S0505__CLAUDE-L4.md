---
id: S0505
agente: CLAUDE-L4
materia: Estatística
aula: Aula 07 — Variáveis Aleatórias Discretas
trecho: estatistica/a07/s04
paginas_lidas: 43-53
---
# ANALÍTICO

Variância e desvio padrão medem o quanto os valores se espalham em torno da média. O trecho mostra como calculá-los para um conjunto de dados e para uma variável aleatória discreta (pela definição e pelo atalho E(X²) − μ²), o papel do desvio padrão e a diferença entre a versão populacional e a amostral.

### Por que elevar os desvios ao quadrado

O **desvio** de um valor x em relação à média μ é a diferença x − μ. Somando os desvios de todos os elementos, os positivos cancelam exatamente os negativos (é a própria definição de média) e o resultado é sempre zero. Para evitar isso, elevam-se os desvios ao quadrado antes de somar.

A **variância** é a **média dos quadrados dos desvios**:

- para N dados: **σ² = Σ(x − μ)² / N**;
- com dados repetidos, usando a frequência relativa fr de cada valor: **σ² = Σ(x − μ)² · fr**;
- para uma variável aleatória, a probabilidade faz o papel da frequência relativa: **σ² = Σ(x − μ)² · P(x)**. Também se escreve V(X) ou Var(X).

> 💡 **Exemplo:** conjunto {2, 2, 4, 8}: μ = 16/4 = 4. Desvios: −2, −2, 0, 4 (soma zero). Quadrados: 4, 4, 0, 16, soma 24. Variância populacional: 24 / 4 = 6.

### Variância de uma variável aleatória

Como E(X) = Σ x · P(x), a variância é a **esperança dos quadrados dos desvios**: σ² = E[(X − μ)²].

Existe uma forma mais prática, que dispensa calcular desvio por desvio:

**σ² = E(X²) − μ² = E(X²) − [E(X)]²**

em que E(X²) = Σ x² · P(x) é a esperança dos valores elevados ao quadrado (segundo momento). A variância também é chamada de segundo momento central.

Roteiro com tabela (valores, probabilidades, x², x² · P):

1. calcule a média μ = Σ x · P(x);
2. eleve a média ao quadrado;
3. some a coluna x² · P(x) para obter E(X²);
4. subtraia: **E(X²) − μ²**.

> ⚠️ **Pegadinha:** E(X²) **não é** a variância; esquecer o último passo (subtrair μ²) é o erro clássico, e as alternativas da prova sempre trazem esse valor intermediário como isca.

> 💡 **Exemplo:** X vale 0, 1, 2, 3 com probabilidades 0,1, 0,4, 0,3 e 0,2. Média: 0 + 0,4 + 0,6 + 0,6 = 1,6. E(X²) = 0 + 0,4 + 1,2 + 1,8 = 3,4. Variância = 3,4 − 1,6² = 3,4 − 2,56 = 0,84.

Quando a função de probabilidade traz uma constante (por exemplo k), use primeiro a condição de que **as probabilidades somam 1** para achá-la. Questões também pedem, junto, média e **mediana**: no caso discreto, a mediana é o menor valor cuja função de distribuição acumulada F(x) alcança pelo menos 0,5. Exemplo: valores 1, 2, 3, 4 com probabilidades 0,1, 0,4, 0,3, 0,2 têm acumuladas 0,1, 0,5, 0,8, 1; a mediana é 2 (primeiro valor com F ≥ 0,5), a média é 0,1 + 0,8 + 0,9 + 0,8 = 2,6 e E(X²) = 0,1 + 1,6 + 2,7 + 3,2 = 7,6, logo a variância é 7,6 − 6,76 = 0,84.

Exemplo clássico: dado equilibrado. μ = 3,5; E(X²) = 91/6; variância = 91/6 − 49/4 = 35/12, cerca de 2,92 (os dois métodos concordam).

### Desvio padrão

A variância fica em unidade ao quadrado (cm², R$²), o que dificulta a leitura. O **desvio padrão** é a sua **raiz quadrada**, voltando à unidade original do dado: σ = raiz de σ². Notação: σ, DP(X) ou D(X). Se a variância das alturas é 400 cm², o desvio padrão é 20 cm, o que indica que boa parte dos adultos está cerca de 20 cm acima ou abaixo da média. Para o dado, σ = raiz de 35/12, cerca de 1,7.

O desvio padrão é **medida de dispersão** (variabilidade, homogeneidade). Se uma questão pergunta qual medida revela a homogeneidade de um grupo, a resposta é o desvio padrão (ou a variância), e não média, mediana ou moda (posição) nem coeficiente de assimetria (forma). Quanto menor a dispersão, mais homogêneo o grupo.

### Variância e desvio padrão amostrais

Quando os dados são uma **amostra** usada para estimar a variância da população, calcula-se a média amostral x̄ = Σx / n e divide-se a soma dos quadrados dos desvios por **n − 1**, e não por n:

**s² = Σ(x − x̄)² / (n − 1)**, e o desvio padrão amostral é s = raiz de s².

A única diferença para a fórmula populacional é o denominador (N na população, n − 1 na amostra), o que torna a estimativa da variância um pouco maior.

> 💡 **Exemplo:** os mesmos dados {2, 2, 4, 8} tratados como amostra: x̄ = 4, soma dos quadrados 24, s² = 24 / 3 = 8 (contra 6 se fosse a população inteira).

Um fato útil: variância e desvio padrão medem espalhamento, não posição. Somar uma constante a todos os valores (como passar de 1, 3, 5, 7, 9 para 11, 13, 15, 17, 19) desloca a média mas não altera os desvios; as duas amostras têm a mesma variância amostral, 40 / 4 = 10.

### Para fixar
- Soma dos desvios em relação à média é sempre zero; por isso eleva-se ao quadrado.
- Variância populacional: σ² = Σ(x − μ)² / N; para variável aleatória, σ² = Σ(x − μ)² · P(x) = E[(X − μ)²].
- Atalho: σ² = E(X²) − μ², com E(X²) = Σ x² · P(x); não parar em E(X²).
- Desvio padrão = raiz da variância, na unidade original; é a medida de dispersão e de homogeneidade.
- Variância amostral: dividir por n − 1 (estimativa da variância da população); populacional divide por N.
- Somar uma constante aos dados não altera variância nem desvio padrão.
- Probabilidades somam 1; a mediana discreta é o menor x com F(x) ≥ 0,5.

# SINTÉTICO

- **Por que ao quadrado**: a soma dos desvios em relação à média é sempre zero; por isso a variância usa a média dos desvios elevados ao quadrado.
- **Variância populacional**: σ² = Σ(x − μ)² / N; com frequências, σ² = Σ(x − μ)² · fr; para variável aleatória, a probabilidade substitui fr.
- **Atalho**: σ² = E(X²) − μ², com E(X²) = Σ x² · P(x); o erro clássico é entregar E(X²) como se fosse a variância.
- **Roteiro de tabela**: calcule μ, eleve ao quadrado, some x² · P(x) e subtraia.
- **Constante da distribuição**: ache-a pela condição de que as probabilidades somam 1; a mediana discreta é o menor x com F(x) ≥ 0,5.
- **Desvio padrão**: raiz da variância, na mesma unidade dos dados; é a medida de dispersão (homogeneidade), ao contrário de média, mediana e moda.
- **Dado equilibrado**: μ = 3,5, variância 35/12 (cerca de 2,92) e desvio padrão cerca de 1,7.
- **Variância amostral**: s² = Σ(x − x̄)² / (n − 1); divide-se por n − 1 para estimar a variância da população.
- **Translação**: somar uma constante a todos os valores não muda a variância nem o desvio padrão.

# NOTAS

- O texto extraído da pág. 43 em diante trouxe as fórmulas com símbolos embaralhados e as tabelas das questões (VUNESP/TJ-PA, IF-PA, FGV/SEFAZ-AM, FGV/TRT-24) não vieram; usei os números reproduzidos nas resoluções (médias, E(X²) e variâncias) e conferi as contas (variâncias 1,85; 3,24; 1,8; e na última questão média 1, mediana 1 e variância 1,8).
- Pág. 51: o texto escreve "para o nosso exemplo da moeda equilibrada" ao se referir ao cálculo de 35/12, que na verdade é o do dado equilibrado (erro de digitação do material).
- Acrescentado fora do trecho: a observação de que somar uma constante não muda a variância (decorre do exemplo das amostras I e II) e a frase de que a variância amostral é "um pouco maior" por dividir por n − 1.
- Os exemplos numéricos ({2, 2, 4, 8} e a variável 0-3) são próprios.
