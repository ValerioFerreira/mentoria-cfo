---
id: S0409
agente: CLAUDE-L4
materia: Estatística
aula: Aula 02 — Medidas Separatrizes ou Quantis
trecho: estatistica/a02/s01
paginas_lidas: 3-16
---
# ANALÍTICO

As separatrizes são medidas que cortam uma série ordenada em partes com a mesma quantidade de elementos. Este trecho apresenta a família das separatrizes e estuda a mais importante, a **mediana**, para dados brutos e para dados agrupados por valor (sem classes).

### Separatrizes: a família

Cada medida recebe o nome conforme o número de partes iguais que forma:

| Medida | Partes | Cada parte contém |
| --- | --- | --- |
| Mediana | 2 | 50% dos valores |
| Quartis | 4 | 25% |
| Quintis | 5 | 20% |
| Decis | 10 | 10% |
| Percentis | 100 | 1% |

Os quintis aparecem pouco em prova; mediana, quartis, decis e percentis são os cobrados.

### Mediana: definição e símbolos

A mediana é, ao mesmo tempo, **medida de posição**, **medida de tendência central** e **separatriz**. Representa-se por **Md** (ou x com til) e é o valor que ocupa o centro da série **depois de ordenada**, em ordem crescente ou decrescente, deixando metade dos elementos de cada lado. **Ordenar antes é obrigatório**: erro típico é pegar o elemento do meio da lista original.

### Dados não agrupados

Seja n o número de elementos (ordenados):

| Situação | Mediana |
| --- | --- |
| n ímpar | o termo de ordem (n + 1)/2 |
| n par | média aritmética dos termos de ordem n/2 e n/2 + 1 |

> 💡 **Exemplo (ímpar):** {4, 9, 2, 15, 7}. Ordenando: 2, 4, 7, 9, 15. Como n = 5, a posição é (5 + 1)/2 = 3, e Md = 7.

> 💡 **Exemplo (par):** {12, 5, 20, 8, 15, 30}. Ordenando: 5, 8, 12, 15, 20, 30. Com n = 6, os termos centrais ocupam as posições 3 e 4: Md = (12 + 15)/2 = 13,5.

Para séries grandes use as fórmulas: com 501 elementos, a mediana é o 251º termo; com 500, é a média do 250º com o 251º.

#### Detalhes que caem em prova

- Com n ímpar, a mediana é um elemento da série e seu valor é único. Com n par, ela **não precisa coincidir com um elemento**.
- Com n par, qualquer valor entre os dois termos centrais separaria a série em metades iguais; adota-se, **por convenção**, a média aritmética deles.
- A mediana divide a série em duas partes com o mesmo número de elementos, mas isso não obriga que as partes sejam "diferentes" ou "simétricas": se todos os valores forem repetidos, por exemplo, a divisão é simétrica. Item que diz "partes assimétricas desiguais" costuma ser falso.

### Mediana e valores extremos

A mediana depende da **posição** do termo central, não dos valores dos outros elementos. Por isso é pouco afetada por valores discrepantes, ao contrário da média aritmética (principal diferença entre as duas).

> 💡 **Exemplo:** {10, 12, 14, 16, 18} tem média 14 e Md = 14. Trocando o 18 por 180: a média vira (10 + 12 + 14 + 16 + 180)/5 = 46,4, enquanto a mediana continua 14. Em geral, média e mediana têm valores diferentes.

### Dados agrupados por valor (sem classes)

A ideia é a mesma: achar o valor que divide a distribuição em duas metades. O caminho prático usa a **frequência acumulada (fac)**, que é a soma das frequências até cada linha:

1. Calcule n (soma das frequências) e a **posição** da mediana: (n + 1)/2 se n for ímpar; n/2 e n/2 + 1 se n for par.
2. Monte a coluna da frequência acumulada.
3. Para cada posição, escolha o **valor da variável da primeira linha cuja fac seja igual ou maior** que a posição.
4. Se n é par, tire a média dos dois valores encontrados.

> 💡 **Exemplo (n ímpar):** número de filhos por funcionário: 0 filhos (f = 6), 1 (9), 2 (12), 3 (5), 4 (3). Então n = 35 e as fac são 6, 15, 27, 32, 35. A posição é (35 + 1)/2 = 18. A primeira fac ≥ 18 é 27, na linha de 2 filhos: Md = 2.

> 💡 **Exemplo (n par):** valores 1 (f = 4), 2 (6), 3 (6), 4 (4): n = 20; fac = 4, 10, 16, 20. As posições são 10 e 11. A posição 10 cai na linha do 2 (fac = 10 ≥ 10); a 11 cai na linha do 3 (fac = 16 ≥ 11). Md = (2 + 3)/2 = 2,5.

> ⚠️ **Pegadinha:** no segundo exemplo a fac é exatamente 10, igual à posição n/2. Esse valor ainda é o 10º termo, mas o 11º já está na linha seguinte; por isso a mediana é a média de dois valores diferentes, e não o próprio 2.

#### Frequência relativa acumulada

Se a tabela traz frequências relativas, a mediana é o valor em que a **frequência relativa acumulada atinge 50%**: o primeiro valor com acumulada maior que 50%. Se algum valor chegar exatamente a 50%, a mediana é a média desse valor com o seguinte.

> 💡 **Exemplo:** X = 0 (0,40), 1 (0,35), 2 (0,25). As acumuladas são 40%, 75% e 100%. A primeira acima de 50% é a de X = 1, logo Md = 1.

### Para fixar

- Separatrizes: mediana (2 partes), quartis (4), decis (10), percentis (100); a mediana é também medida de posição e de tendência central.
- Sempre ordene os dados antes de procurar a mediana.
- n ímpar: termo de ordem (n + 1)/2; n par: média dos termos de ordem n/2 e n/2 + 1.
- Com n par, a mediana não precisa ser um elemento da série.
- A mediana depende da posição, não dos valores; resiste a extremos melhor que a média.
- Dados por valor: calcule a fac e pegue o valor da primeira fac maior ou igual à posição.
- Com n par, atenção ao caso em que a fac é igual a n/2: o 2º termo central está na linha seguinte.
- Com frequências relativas, procure o ponto em que a acumulada alcança 50%.

# SINTÉTICO

- **Separatrizes**: dividem a série ordenada em partes iguais: mediana (2 partes de 50%), quartis (4 de 25%), decis (10 de 10%) e percentis (100 de 1%).
- **Mediana**: é medida de posição, de tendência central e separatriz; só se obtém após ordenar os dados.
- **Cálculo bruto**: n ímpar, termo de ordem (n + 1)/2; n par, média dos termos de ordem n/2 e n/2 + 1 (por convenção).
- **Valor da mediana**: com n ímpar é um elemento da série; com n par pode não ser.
- **Robustez**: depende da posição central, não dos extremos; mudar o maior valor altera a média, mas não a mediana.
- **Dados por valor**: acha-se a posição, monta-se a frequência acumulada e usa-se o valor da primeira fac maior ou igual à posição.
- **n par em tabela**: calcular os dois termos centrais separadamente; se a fac for exatamente n/2, o segundo termo está na linha seguinte.
- **Frequência relativa**: a mediana é o valor em que a acumulada chega a 50%; se atinge exatamente 50%, média com o valor seguinte.

# NOTAS

- Páginas 9 a 10, 14 a 16 trazem questões comentadas; só a teoria e a técnica foram aproveitadas. As tabelas das páginas 11 a 14 (satisfação e notas) foram descartadas; os exemplos do resumo são próprios.
- A regra para a frequência relativa acumulada exatamente igual a 50% (média com o valor seguinte) e a explicação da pegadinha da fac igual a n/2 foram deduzidas da definição (n par); o trecho só usa o caso em que a acumulada passa de 50%.
- Os valores 780 e 870 da questão da pág. 15 vêm de tabela parcialmente embaralhada na extração; não foram usados.
