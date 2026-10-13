---
id: S0524
agente: CLAUDE-L4
materia: Estatística
aula: Aula 07 — Variáveis Aleatórias Discretas
trecho: estatistica/a07/s03
paginas_lidas: 27-36
---
# ANALÍTICO

O trecho completa as medidas de tendência central de uma variável aleatória com a **moda** e a **mediana** (definições, casos especiais e propriedades), revisa as propriedades da esperança em uma questão e fecha com a comparação entre média, mediana e moda para identificar a **assimetria** da distribuição.

### Revisão rápida das propriedades da esperança

Para quaisquer variáveis X e Y e constante a: E(X + a) = E(X) + a; E(a·X) = a·E(X); E(X ± Y) = E(X) ± E(Y). Já **E(X·Y) = E(X)·E(Y) só vale se X e Y forem independentes**. Uma questão típica de prova oferece alternativas que erram exatamente esses pontos (soma de constante virando "= a", produto sem independência, constante que some ao multiplicar): a única correta costuma ser a da soma/diferença de variáveis.

### Moda

A **moda** (Mo) é o resultado que a variável tem mais chance de assumir: aquele ao qual está associada a probabilidade máxima. Na soma de duas moedas (0 ou 1), as probabilidades são 25%, 50% e 25% para os resultados 0, 1 e 2: a moda é **1**.

- **A moda é um valor da variável, não uma probabilidade.** No gráfico de barras ela está no eixo horizontal, sob a coluna mais alta.
- Em uma **amostra**, a moda amostral é o valor observado com **maior frequência**.
- Pode haver **mais de uma moda**, quando o maior valor de probabilidade se repete: duas modas = **bimodal**; três = **trimodal**; várias = **multimodal**.
- Se todos os resultados são equiprováveis (moeda ou dado equilibrados), a distribuição **não tem moda** e é chamada de **amodal**.

> 💡 **Exemplo próprio:** na amostra {3, 5, 5, 5, 8, 9, 9}, o 5 aparece três vezes, então Mo = 5. Na amostra {2, 2, 4, 4, 7}, há duas modas (2 e 4): é bimodal.

> ⚠️ **Pegadinha (Cebraspe):** dizer que a moda é "o maior valor possível" ou "o maior valor registrado" está errado. Em uma tabela de distribuição de incidentes, a moda foi o valor de frequência relativa 0,5 (o valor 2), e não o maior valor da tabela (4). Procure a maior frequência, não o maior valor.

#### Propriedades da moda

Com X variável e k constante:

- **Mo(k·X) = k·Mo(X)**: multiplicar (ou dividir, que é multiplicar por 1/k) a variável faz a moda ser multiplicada (ou dividida).
- **Mo(X ± k) = Mo(X) ± k**: somar ou subtrair uma constante desloca a moda do mesmo valor.

> 💡 **Exemplo próprio:** se a moda das notas é 6 e cada nota é multiplicada por 1,5 e acrescida de 1 ponto, a nova moda é 6 × 1,5 + 1 = 10.

### Mediana

A **mediana** (Md) é o ponto que parte a distribuição ao meio, em termos de probabilidade: metade da massa fica em valores **menores ou iguais** a ela (50%) e a outra metade em valores **maiores ou iguais** (50%).

- Quando a divisão cai **entre dois valores**, adota-se por convenção a **média aritmética** deles. Num dado viciado em que os valores até 4 somam 50% e os de 5 em diante somam 50%, Md = (4 + 5)/2 = 4,5.
- A definição pede um ajuste: a probabilidade de valores menores ou iguais à mediana deve ser **no mínimo 50%** e a de maiores ou iguais também **no mínimo 50%**. Na soma de duas moedas, P(X ≤ 1) = 75% e P(X ≥ 1) = 75%, logo Md = 1 (valores 0 e 2 não fazem sentido como mediana).

**Como achar na tabela:** acumule as probabilidades na ordem dos valores. O primeiro valor em que a acumulada chega a 50% ou mais é candidato; se a acumulada for **exatamente 50%** em um valor, a mediana é a média desse valor com o seguinte.

> 💡 **Exemplo próprio:** X = 1 (20%), 2 (30%), 3 (30%), 4 (20%). Acumulada: 20%, 50%, 80%, 100%. A acumulada é exatamente 50% em X = 2, logo Md = (2 + 3)/2 = 2,5.

#### Propriedades da mediana

São iguais às da moda: **Md(k·X) = k·Md(X)** e **Md(X ± k) = Md(X) ± k**, válidas também para divisão por constante.

> 💡 **Exemplo (questão Cebraspe):** com U = R/10 − 7 e Md(R) = 80, tem-se Md(U) = 80/10 − 7 = 1, positiva. (As informações de média e variância eram distratores.) Exemplo próprio: V = 3·W + 4 com Md(W) = 12 dá Md(V) = 40.

> ⚠️ **Pegadinha:** as propriedades acima valem para mediana e moda, mas **não** para a variância. Se a questão fornece média, mediana e variância, use só a medida pedida e aplique a regra dela (soma e multiplicação por constante).

### Assimetria: comparando média, mediana e moda

A relação entre as três medidas mostra o quanto a distribuição se afasta da simetria.

| Distribuição | Forma | Relação |
| --- | --- | --- |
| Simétrica | caudas iguais dos dois lados | Média = Mediana = Moda |
| Assimétrica positiva (à direita) | cauda direita mais longa; mais valores acima da moda | Moda < Mediana < Média |
| Assimétrica negativa (à esquerda) | cauda esquerda mais longa; mais valores abaixo da moda | Moda > Mediana > Média |

A média é a medida mais puxada pelos valores extremos da cauda longa; a moda é a menos afetada.

> 💡 **Exemplo próprio:** em salários, poucos valores muito altos puxam a média para cima: Moda < Mediana < Média (assimetria positiva).

### Resumo das medidas

| Medida | Definição | Propriedades principais |
| --- | --- | --- |
| Esperança | Σ x·P(x) | E(kX) = k·E(X); E(X ± k) = E(X) ± k; E(X ± Y) = E(X) ± E(Y); E(XY) = E(X)·E(Y) se independentes |
| Moda | valor de maior probabilidade | Mo(kX) = k·Mo(X); Mo(X ± k) = Mo(X) ± k |
| Mediana | valor com pelo menos 50% abaixo e pelo menos 50% acima | Md(kX) = k·Md(X); Md(X ± k) = Md(X) ± k |

### Para fixar
- Moda = valor mais provável (ou mais frequente na amostra); é um valor, não uma probabilidade.
- Uma moda = unimodal; duas = bimodal; três = trimodal; várias = multimodal; todos equiprováveis = amodal.
- Mediana: ao menos 50% de probabilidade em ≤ e ao menos 50% em ≥; entre dois valores, tira-se a média deles.
- Mo e Md obedecem às mesmas regras: multiplicar por k multiplica a medida por k; somar k soma k.
- Simétrica: média = mediana = moda; assimetria positiva: moda < mediana < média; negativa: moda > mediana > média.
- E(XY) = E(X)·E(Y) só com independência; E(X ± Y) = E(X) ± E(Y) sempre.

# SINTÉTICO

- **Moda**: valor da variável com maior probabilidade (na amostra, o de maior frequência); é um valor do eixo horizontal, nunca uma probabilidade.
- **Número de modas**: duas = bimodal, três = trimodal, várias = multimodal; sem moda (resultados equiprováveis, como moeda e dado equilibrados) a distribuição é amodal.
- **Propriedades da moda**: Mo(kX) = k·Mo(X) e Mo(X ± k) = Mo(X) ± k, incluindo a divisão por k.
- **Mediana**: valor com pelo menos 50% de probabilidade em valores menores ou iguais e pelo menos 50% em maiores ou iguais.
- **Mediana entre dois valores**: quando a acumulada fecha exatamente em 50%, adota-se a média dos dois valores vizinhos (ex.: entre 4 e 5, Md = 4,5).
- **Como achar a mediana**: acumule as probabilidades na ordem crescente dos valores até alcançar 50% ou mais.
- **Propriedades da mediana**: iguais às da moda: Md(kX) = k·Md(X) e Md(X ± k) = Md(X) ± k.
- **Simetria**: numa distribuição simétrica, as três medidas coincidem: média = mediana = moda.
- **Assimetria positiva** (cauda longa à direita): moda < mediana < média.
- **Assimetria negativa** (cauda longa à esquerda): moda > mediana > média.
- **Esperança, revisão**: E(X ± Y) = E(X) ± E(Y) sempre; E(XY) = E(X)·E(Y) só se forem independentes.

# NOTAS

- Tabelas e gráficos das questões Cebraspe (incidentes em penitenciária; apreensões da PF) vieram como imagem; usei só as conclusões dos comentários (moda de N = 2, com frequência 0,5; moda de 22 kg, que aparece em 2 dos 5 dias).
- Pág. 30 do material: o exemplo de aumento de 3 mil reais escreve "X + 2" em um ponto (os valores listados, 4, 5, 5, 5... correspondem a +3). Pág. 34: a regra "Md(X − k)" aparece escrita como "Mo(X − k)" por erro de digitação; o resumo traz Md.
- Pág. 32: o texto diz "25% maior que a" (deveria ser "maior que 1"); sem impacto.
- Não aparece no trecho a moda de variáveis contínuas nem o caso de k negativo nas propriedades; não foram acrescentados.
- Exemplos "próprios" (amostras, tabela X = 1..4, V = 3W + 4, notas × 1,5 + 1) são do autor do resumo; nada acrescentado fora do trecho além deles.
