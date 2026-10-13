---
id: S0467
agente: CLAUDE-L4
materia: Estatística
aula: Aula 02 — Medidas Separatrizes ou Quantis
trecho: estatistica/a02/s03
paginas_lidas: 33-43
---
# ANALÍTICO

As medidas separatrizes dividem um conjunto ordenado em partes com a mesma quantidade de elementos. A mediana é a mais simples (duas partes); este trecho amplia a ideia para quartis, decis e percentis e ensina a calculá-los em três situações: dados brutos, dados agrupados sem classes e dados agrupados em classes.

### Quartis, decis e percentis

O nome da medida depende em quantas partes iguais o conjunto é dividido:

| Medida | Divide em | Quantos valores | Símbolos |
| --- | --- | --- | --- |
| Quartil | 4 partes (25% cada) | 3 | Q1, Q2, Q3 |
| Quintil | 5 partes (20% cada) | 4 | Qt1 a Qt4 |
| Decil | 10 partes (10% cada) | 9 | D1 a D9 |
| Percentil | 100 partes (1% cada) | 99 | P1 a P99 |

Regra de leitura: o quartil k deixa k·25% dos elementos abaixo de si. Assim, **Q1** separa os 25% menores, **Q3** separa os 75% menores (ou os 25% maiores) e **Q2** separa 50% e **coincide com a mediana** (Q2 = Md). Pela mesma lógica, D5 = P50 = Q2 = mediana, Q1 = P25, Q3 = P75, D1 = P10 e assim por diante.

A fórmula é sempre a da mediana, trocando a posição central (soma das frequências ÷ 2) por **k × (soma das frequências) ÷ 4**, para quartis; ÷ 10 para decis; ÷ 100 para percentis. O k vai de 1 a 3 nos quartis.

### Quartil em dados não agrupados (rol)

Primeiro **ordene** os dados do menor para o maior (rol). Depois:

1. calcule a posição: **P(Qk) = k × n / 4**, em que n é o número de observações;
2. se o resultado não for inteiro, tome a **posição inteira mais próxima** (aproximação adotada no trecho);
3. leia o valor que ocupa essa posição no rol.

Para **Q2** use sempre o procedimento da mediana: n ímpar, o elemento da posição (n+1)/2; n par, a média dos elementos das posições n/2 e n/2 + 1. Isso evita que a aproximação gere um valor diferente da mediana.

> 💡 **Exemplo:** rol de 8 notas: 7, 9, 10, 12, 13, 15, 16, 18. Posição de Q1 = 1 × 8/4 = 2, logo Q1 = 9. Posição de Q3 = 3 × 8/4 = 6, logo Q3 = 15. Q2 = média do 4º e do 5º = (12 + 13)/2 = 12,5.

> 💡 **Exemplo com posição quebrada:** com n = 11, Q1 está na posição 2,75, que fica mais perto da 3ª; então Q1 é o 3º valor do rol.

> ⚠️ **Pegadinha:** dados fora de ordem. Antes de contar posições, é obrigatório ordenar; ordem de coleta não vale.

### Quartil em dados agrupados sem intervalos de classe

Aqui a tabela traz cada valor da variável com sua frequência. Será preciso uma coluna de **frequência acumulada (fac)**.

1. posição: **P(Qk) = k × (soma de fi) / 4**;
2. na coluna fac, ache a **primeira frequência acumulada maior ou igual** à posição;
3. o quartil é o **valor da variável** dessa linha.

Q2 segue a regra da mediana (média das posições centrais quando a soma das frequências é par).

> 💡 **Exemplo:** número de dependentes por funcionário, com frequências 0 → 5, 1 → 8, 2 → 12, 3 → 5 (total 30; fac: 5, 13, 25, 30). Q1: posição 7,5; primeira fac ≥ 7,5 é 13, logo Q1 = 1. Q2: com 30 elementos, usam-se as posições 15 e 16, ambas na linha da fac 25, logo Q2 = 2. Q3: posição 22,5; primeira fac ≥ 22,5 é 25, logo Q3 = 2.

O raciocínio é que a fac diz até que posição do rol cada valor "chega": se o quartil cai na posição 22,5, ele pertence ao valor cuja faixa de posições (de 14 a 25, no exemplo) contém esse número.

### Quartil em dados agrupados em classes

Agora a tabela traz intervalos de classe (por exemplo, 10 ⊢ 20). Como não se sabe onde cada observação está dentro da classe, **interpola-se** dentro dela, supondo distribuição uniforme.

Passos:

1. posição: **P(Qk) = k × (soma de fi) / 4**;
2. localize na fac a **classe do quartil** (primeira fac ≥ posição);
3. levante os dados dessa classe;
4. aplique a fórmula:

**Qk = linf + [ (k × Σfi / 4 − fac_ant) / f_Qk ] × h**

- **linf**: limite inferior da classe do quartil;
- **fac_ant**: frequência acumulada da classe imediatamente anterior;
- **f_Qk**: frequência simples da classe do quartil;
- **h**: amplitude da classe (limite superior − limite inferior).

É exatamente a fórmula da mediana, só com a posição trocada. Para decis, a posição é k × Σfi / 10; para percentis, k × Σfi / 100; o resto não muda.

> 💡 **Exemplo:** classes 0 ⊢ 10 (f = 8), 10 ⊢ 20 (f = 12), 20 ⊢ 30 (f = 20), 30 ⊢ 40 (f = 10); total 50 e fac 8, 20, 40, 50.
> Q1: posição 12,5, classe 10 ⊢ 20: Q1 = 10 + [(12,5 − 8)/12] × 10 = 13,75.
> Q2: posição 25, classe 20 ⊢ 30: Q2 = 20 + [(25 − 20)/20] × 10 = 22,5.
> Q3: posição 37,5, classe 20 ⊢ 30: Q3 = 20 + [(37,5 − 20)/20] × 10 = 28,75.

Observações úteis:

- Se a posição coincidir exatamente com uma fac (por exemplo, posição 40 e fac 40), o quartil cai no **limite superior** da classe: a fração entre colchetes dá 1 e o resultado é linf + h.
- O quartil é sempre um valor **dentro** da classe encontrada; se o resultado fugiu dela, houve erro ao escolher a classe ou a fac_ant.
- Os valores de uma questão podem ser pedidos como "valor que deixa 25% abaixo e 75% acima", que é só a definição de Q1; saiba traduzir a linguagem.

### Erros comuns

- Usar a posição n/2 para Q1 ou Q3, esquecendo o 4 no denominador.
- Pegar a classe pela frequência simples em vez da frequência acumulada.
- Usar como fac_ant a acumulada da própria classe, em vez da anterior.
- Esquecer a amplitude h, ou usar a amplitude de outra classe quando elas são desiguais.

### Para fixar
- Quartis dividem em 4 partes iguais (Q1, Q2, Q3), decis em 10 (D1 a D9), percentis em 100 (P1 a P99); Q2 = D5 = P50 = mediana.
- A posição do quartil é k × n / 4 (ou k × Σfi / 4); decil usa 10 e percentil usa 100 no denominador.
- No rol, ordene antes; posição quebrada é aproximada para a mais próxima, e Q2 segue sempre a regra da mediana.
- Sem classes, use a fac: o quartil é o valor da primeira linha com fac maior ou igual à posição.
- Com classes, Qk = linf + [(posição − fac_ant) / f] × h.
- Tenha certeza de qual é a classe do quartil, qual é a fac anterior e qual é a amplitude.
- O resultado precisa cair dentro da classe do quartil.

# SINTÉTICO

- **Separatrizes**: dividem o conjunto ordenado em partes iguais; quartil (4 partes, Q1 a Q3), quintil (5), decil (10, D1 a D9) e percentil (100, P1 a P99).
- **Equivalências**: Q2 = D5 = P50 = mediana; Q1 = P25 e Q3 = P75.
- **Posição**: k × n / 4 para quartis (k de 1 a 3); trocar o 4 por 10 (decil) ou 100 (percentil).
- **Rol**: ordene os dados; se a posição não for inteira, use a mais próxima; Q2 sempre pelo procedimento da mediana (n ímpar: (n+1)/2; n par: média de n/2 e n/2 + 1).
- **Dados sem classes**: monte a frequência acumulada e escolha o valor da primeira linha cuja fac é maior ou igual à posição.
- **Dados em classes**: ache a classe pela fac e interpole: Qk = linf + [(k·Σfi/4 − fac_ant) / f] × h.
- **Fórmula = mediana adaptada**: só a posição muda; a estrutura (linf, fac_ant, f, h) é a mesma.
- **Pegadinhas**: não ordenar o rol, confundir f com fac, usar fac da própria classe como fac_ant, errar a amplitude.
- **Conferência**: o quartil calculado deve estar dentro dos limites da classe encontrada; se a posição for igual a uma fac, o resultado cai no limite superior da classe.

# NOTAS

- Decis e percentis: o trecho apresenta a definição, mas os procedimentos de cálculo só são desenvolvidos para quartis. A afirmação de que decil usa posição k·n/10 e percentil k·n/100 (com a mesma fórmula de interpolação) foi acrescentada fora do trecho, é regra estável.
- Os quintis (Qt1 a Qt4) são citados pelo material apenas na definição; não há procedimento próprio.
- Na regra do rol, o material fala em "posição mais próxima" quando o resultado não é inteiro; existem outras convenções em estatística (interpolação linear entre vizinhos), mas segui a do trecho.
- Páginas 36 e 38-39 repetem a tabela do rol (11 a 27) e a de frequências em desordem na extração; as tabelas foram reconstruídas apenas conceitualmente, com exemplos próprios.
- Cálculos conferidos: nos exemplos do material, Q1 = 53,9, Q2 = 69,7 e Q3 = 90 (classes de 20 em 20), consistentes.
