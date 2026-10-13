---
id: S0410
agente: CLAUDE-L4
materia: Estatística
aula: Aula 02 — Medidas Separatrizes ou Quantis
trecho: estatistica/a02/s05
paginas_lidas: 53-66
---
# ANALÍTICO

Os percentis dividem uma série ordenada em cem partes com o mesmo número de elementos. Este trecho ensina a calcular o percentil em três formatos de dados: brutos (não agrupados), agrupados por valor (sem classes) e agrupados em classes, com interpolação.

### O que são os percentis

São **99 valores** (P1, P2, ..., P99) que separam a série em 100 fatias de 1% cada. O percentil de ordem **k** deixa k% dos elementos abaixo de si (e 100 − k% acima).

- **P1**: separa o primeiro 1% dos dados;
- **P50**: separa a metade e **coincide com a mediana** (P50 = Md);
- **P99**: separa os 99% menores do último 1%.

Pela mesma lógica, P25 = Q1, P75 = Q3 e P10 = D1 (e assim por diante com os decis).

A grande ideia é que o cálculo dos percentis **reaproveita o da mediana**: onde a mediana usa Σfi/2 (metade dos elementos), o percentil usa **k × Σfi / 100** (k% dos elementos), com k = 1, 2, ..., 99.

### Percentil para dados não agrupados

Primeiro, **ordene** os dados em rol. Depois, em três etapas:

1. **posição**: Pk = k × n / 100;
2. **aproxime** essa posição para a mais próxima do rol (número inteiro);
3. **leia o valor** que ocupa a posição no rol ordenado.

> 💡 **Exemplo:** dados {31, 8, 15, 22, 40, 12, 27, 19, 35, 5}. Rol: 5, 8, 12, 15, 19, 22, 27, 31, 35, 40 (n = 10).
> - P38: posição 38 × 10/100 = 3,8, que fica mais perto da 4ª posição; valor = 15. Ou seja, 15 corresponde a 38% do rol.
> - P72: posição 72 × 10/100 = 7,2, aproximada para a 7ª; valor = 27.

> ⚠️ **Pegadinha:** o erro mais comum é esquecer de ordenar antes de contar a posição. Outro é usar n + 1 em vez de n: aqui a posição é k × n / 100.

### Percentil para dados agrupados sem classes

Os dados vêm numa tabela de valores e frequências. As etapas são:

1. posição: **k × Σfi / 100**, em que Σfi é a soma das frequências (o total de observações);
2. na coluna de **frequência acumulada (fac)**, localize a primeira fac **igual ou superior** à posição;
3. o percentil é o **valor da variável** dessa linha.

> 💡 **Exemplo:** notas de um teste, com frequências: 5 (f = 4), 6 (f = 10), 7 (f = 16), 8 (f = 14), 9 (f = 6). Total 50; fac = 4, 14, 30, 44, 50.
> - P20: posição 20 × 50/100 = 10; primeira fac ≥ 10 é 14, na linha da nota 6. Logo, P20 = 6.
> - P60: posição 30; a primeira fac ≥ 30 é exatamente 30 (nota 7). P60 = 7.
> - P90: posição 45; a primeira fac ≥ 45 é 50 (nota 9). P90 = 9.

Note que, com a posição igual à fac de uma linha, vale a **própria linha**, não a seguinte.

### Percentil para dados agrupados em classes

Aqui a tabela traz classes (intervalos) e se admite que os elementos estejam **distribuídos uniformemente dentro da classe**, o que permite **interpolar** um valor numérico. As etapas são:

1. posição: **k × Σfi / 100**;
2. na fac, ache a classe cuja acumulada é a **primeira igual ou superior** à posição (a **classe do percentil**);
3. anote os dados dessa classe;
4. aplique a fórmula, que é a da mediana com a posição trocada:

**Pk = l_inf + [ (k × Σfi / 100 − fac_ant) / f ] × h**

| Símbolo | Significado |
| --- | --- |
| l_inf | limite inferior da classe do percentil |
| fac_ant | frequência acumulada da classe **anterior** (0 se for a primeira) |
| f | frequência simples da classe do percentil |
| h | amplitude da classe (limite superior − inferior) |

> 💡 **Exemplo:** salários (R$): 1.000 ⊢ 1.500 (f = 8), 1.500 ⊢ 2.000 (20), 2.000 ⊢ 2.500 (14), 2.500 ⊢ 3.000 (8). Total 50; fac = 8, 28, 42, 50; h = 500.
> - **P40**: posição 40 × 50/100 = 20. A primeira fac ≥ 20 é 28 (2ª classe). P40 = 1.500 + [(20 − 8)/20] × 500 = 1.500 + 0,6 × 500 = **1.800**.
> - **P90**: posição 45. A primeira fac ≥ 45 é 50 (4ª classe). P90 = 2.500 + [(45 − 42)/8] × 500 = 2.500 + 187,5 = **2.687,5**.

> ⚠️ **Pegadinha:** o que entra como fac_ant é a acumulada da classe **anterior** (a que ficou para trás), e não a da classe do percentil. E f é a frequência **simples** da classe, não a acumulada.

#### Frequências relativas

Se a tabela dá frequências **relativas** (em %), trabalhe com porcentagens: a posição passa a ser o próprio **k%**, a fac é a relativa acumulada, e f e fac_ant também em %. O resultado é o mesmo da forma absoluta.

> 💡 **Exemplo:** classes 0 ⊢ 5 (20%), 5 ⊢ 10 (35%), 10 ⊢ 15 (30%), 15 ⊢ 20 (15%); acumuladas: 20%, 55%, 85%, 100%. Para P60, a primeira acumulada ≥ 60% é 85% (classe 10 ⊢ 15). P60 = 10 + [(60 − 55)/30] × 5 ≈ 10,83.

Esse mesmo roteiro serve para qualquer separatriz, bastando trocar a posição: mediana (Σfi/2), quartil (j × Σfi/4), decil (j × Σfi/10), percentil (k × Σfi/100). Há questões que misturam, por exemplo, Q1 e Md na mesma tabela e pedem a diferença entre elas.

### Para fixar

- Existem 99 percentis; Pk deixa k% dos dados abaixo; P50 = Md.
- Não agrupados: ordene, calcule k × n / 100, aproxime para a posição mais próxima e leia o valor.
- Agrupados por valor: posição = k × Σfi / 100; vale o valor da primeira fac maior ou igual à posição.
- Agrupados em classes: encontre a classe pela fac e aplique Pk = l_inf + [(k × Σfi/100 − fac_ant)/f] × h.
- Na fórmula, fac_ant é da classe anterior; f é a frequência simples; h, a amplitude.
- A fórmula supõe distribuição uniforme dentro da classe.
- Com frequências relativas, a posição é k% e tudo é em porcentagem.
- Mudando apenas a posição, o método vale para mediana, quartis e decis.

# SINTÉTICO

- **Percentis**: 99 valores que dividem a série ordenada em 100 partes de 1%; Pk deixa k% abaixo; P50 coincide com a mediana.
- **Ideia do cálculo**: reaproveita o da mediana, trocando Σfi/2 por k × Σfi / 100.
- **Dados não agrupados**: ordenar, achar a posição k × n / 100, aproximar para a mais próxima e ler o valor; por exemplo, 3,8 vira 4ª posição.
- **Dados por valor**: posição = k × Σfi / 100; o percentil é o valor da primeira linha cuja fac é igual ou superior à posição.
- **Dados em classes**: identifica-se a classe pela fac e interpola-se com Pk = l_inf + [(k × Σfi/100 − fac_ant)/f] × h.
- **Símbolos da fórmula**: fac_ant é a acumulada anterior à classe, f é a frequência simples da classe e h é a amplitude; supõe-se uniformidade dentro da classe.
- **Frequência relativa**: usar a posição k% e as acumuladas em porcentagem; o resultado coincide com o das frequências absolutas.
- **Erros comuns**: não ordenar os dados, usar a fac da própria classe como fac_ant e confundir f com a acumulada.

# NOTAS

- As páginas 61 a 66 trazem questões comentadas (idades de funcionários, teatros, distâncias da Defensoria); só a teoria foi aproveitada. As tabelas dos exemplos do material (filhos de professores, estaturas) foram descartadas; os exemplos do resumo são próprios.
- Erro aparente no material (pág. 60): a posição de P77 aparece como 41,04 no passo da posição, mas o produto 77 × 54/100 é 41,58, que é o valor usado depois na fórmula (e leva ao P77 = 148,66). Usei o valor correto.
- Na pág. 54, uma equação de P83 aparece rotulada como P27 (erro tipográfico); sem efeito no método.
- O material aproxima a posição fracionária para a mais próxima (ex.: 2,97 vira 3; 9,13 vira 9). Nas questões comentadas de quartis de dados brutos, o texto fala em "entre as posições 2 e 3", ou seja, convenções variam; as respostas coincidem com a aproximação para a mais próxima. Quando a posição é inteira, o método do trecho toma o termo daquela posição (não há média de dois termos como na mediana de n par); o trecho não discute o caso, fica para conferência humana.
- As equivalências P25 = Q1, P75 = Q3 e P10 = D1 são consequência da definição (não constam no trecho). A suposição de uniformidade dentro da classe é a premissa padrão da interpolação, enunciada em questão do trecho.
