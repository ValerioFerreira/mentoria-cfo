---
id: S0506
agente: CLAUDE-L4
materia: Estatística
aula: Aula 02 — Medidas Separatrizes ou Quantis
trecho: estatistica/a02/s04
paginas_lidas: 44-52
---
# ANALÍTICO

Os decis são medidas separatrizes que repartem uma série ordenada em dez partes com o mesmo número de elementos. O trecho ensina o cálculo em três situações: dados brutos (não agrupados), dados agrupados sem intervalos de classe (valores isolados com frequências) e dados agrupados em classes.

### O que são os decis

São **9 valores** (D1, D2, ..., D9) que dividem a série em 10 partes, cada uma com 10% dos elementos:

- **D1** deixa abaixo de si os primeiros 10% dos elementos;
- **D5** deixa 50% abaixo e 50% acima, portanto **coincide com a mediana** (D5 = Md);
- **D9** deixa 90% abaixo e 10% acima.

O índice k vai de **1 a 9** e indica a ordem do decil. O método é o mesmo da mediana, trocando "metade do total" (Σfi / 2) por **k · Σfi / 10**. Isto é, o decil Dk é o valor que ocupa a posição correspondente a k décimos da série.

### Dados não agrupados

1. **Ordene** os dados em rol (crescente), se ainda não estiverem.
2. Calcule a **posição**: **P(Dk) = k · n / 10**, com n o número de observações.
3. Identifique a **posição mais próxima** no rol (o método é aproximado).
4. O decil é o **valor que ocupa essa posição**.

Quando a posição dá número inteiro, não há aproximação a fazer; quando dá fracionário, usa-se a posição inteira mais próxima.

> 💡 **Exemplo:** rol com n = 14: {4, 6, 7, 9, 10, 12, 15, 16, 18, 21, 23, 25, 28, 30}. D1: posição 1,4, mais próxima 1, valor 4. D3: posição 4,2, mais próxima 4, valor 9. D8: posição 11,2, mais próxima 11, valor 23. Interpretação: cerca de 80% dos dados são menores ou iguais a 23.

> ⚠️ **Pegadinha:** ordene antes de contar posições. Contar sobre os dados na ordem em que aparecem é o erro mais comum.

### Dados agrupados sem intervalos de classe

Os dados vêm numa tabela de valores isolados (xi) e frequências simples (fi), por exemplo número de filhos. É preciso incluir a coluna de **frequências acumuladas (fac)**.

1. Posição: **P(Dk) = k · Σfi / 10**, em que Σfi é o total de observações.
2. Na coluna fac, ache a **primeira frequência acumulada igual ou superior** à posição.
3. O decil é o **valor da variável** naquela linha.

> 💡 **Exemplo:** número de veículos por família, com frequências 12, 20, 25, 13 e 10 para 0, 1, 2, 3 e 4 veículos (total 80; fac: 12, 32, 57, 70, 80). D2: posição 16, primeira fac ≥ 16 é 32, valor 1. D4: posição 32, a fac 32 é igual à posição, valor 1 (igual conta). D5: posição 40, fac 57, valor 2. D9: posição 72, fac 80, valor 4.

### Dados agrupados em classes

Aqui os dados estão em intervalos (por exemplo 120 ⊢ 128: inclui o limite inferior e exclui o superior). Como não se conhece a distribuição dentro da classe, **interpola-se linearmente**: assume-se que os elementos estão distribuídos uniformemente no intervalo. É uma variação da fórmula da mediana.

1. Posição: **P(Dk) = k · Σfi / 10**.
2. Localize a **classe do decil**: a primeira cuja fac é igual ou maior que a posição.
3. Anote os dados da classe: limite inferior (linf), frequência simples da classe (fDk), frequência acumulada da classe anterior (fac ant) e amplitude (h = limite superior − inferior).
4. Aplique:

**Dk = linf + [ (k · Σfi / 10 − fac ant) / fDk ] · h**

A fração entre colchetes diz quanto da classe é preciso percorrer: é o que falta para alcançar a posição, dividido pela frequência da classe. Multiplicada pela amplitude, converte-se em unidades da variável.

> 💡 **Exemplo:** salários em classes de R$ 1.000, com frequências 6, 12, 18, 9 e 5 para 1.000 ⊢ 2.000, 2.000 ⊢ 3.000, 3.000 ⊢ 4.000, 4.000 ⊢ 5.000 e 5.000 ⊢ 6.000 (total 50; fac: 6, 18, 36, 45, 50). D1: posição 5, classe 1 (fac 6), D1 = 1.000 + (5 − 0)/6 · 1.000, cerca de 1.833,33. D3: posição 15, classe 2 (fac 18), D3 = 2.000 + (15 − 6)/12 · 1.000 = 2.750. D8: posição 40, classe 4 (fac 45), D8 = 4.000 + (40 − 36)/9 · 1.000, cerca de 4.444,44.

Cuidados nos cálculos: fac ant é a acumulada da classe **anterior** (zero se a classe é a primeira) e fDk é a frequência **simples** da classe do decil, não a acumulada. O resultado precisa cair dentro da classe encontrada; se não cair, houve engano na escolha da classe.

### Para fixar
- Decis: 9 valores que dividem a série em 10 partes de 10% cada; k vai de 1 a 9; D5 é a mediana.
- Posição do decil: k · n / 10 (ou k · Σfi / 10 em tabelas).
- Dados brutos: ordenar, calcular a posição, tomar a mais próxima e ler o valor.
- Valores isolados: usar a fac e escolher a primeira acumulada igual ou superior à posição.
- Classes: Dk = linf + [(k · Σfi / 10 − fac ant) / fDk] · h.
- fac ant é da classe anterior, fDk é a frequência simples da classe do decil e h é a amplitude.
- Confira se o decil calculado está dentro do intervalo da classe escolhida.

# SINTÉTICO

- **Decis**: nove valores (D1 a D9) que dividem a série ordenada em dez partes de 10% cada; D5 coincide com a mediana.
- **Posição**: P(Dk) = k · n / 10 (ou k · Σfi / 10 em tabelas de frequências), com k de 1 a 9.
- **Dados não agrupados**: ordene em rol, calcule a posição, use a posição inteira mais próxima e leia o valor ali.
- **Valores isolados com frequência**: monte a coluna de frequências acumuladas e escolha a primeira acumulada igual ou superior à posição; o decil é o valor da variável nessa linha.
- **Dados em classes**: ache a classe do decil pela fac e interpole: Dk = linf + [(k · Σfi / 10 − fac ant) / fDk] · h.
- **Elementos da fórmula**: linf é o limite inferior da classe, fac ant a acumulada da classe anterior, fDk a frequência simples da classe e h a amplitude.
- **Interpolação**: supõe distribuição uniforme dentro da classe; a fração do colchete mostra quanto da classe é percorrido.
- **Erro comum**: não ordenar o rol, usar a fac em vez da frequência simples no denominador ou esquecer a fac da classe anterior.

# NOTAS

- Pág. 45: o texto diz "Calcularemos os quartis D1 e D8"; trata-se de decis (erro de digitação do material).
- Pág. 51: no cálculo de D1 das estaturas, a conta 120 + (5,4 − 0)/6 · 8 resulta em 127,2 cm, e o material escreve 127,5 cm (erro de digitação ou de arredondamento). Os demais resultados do trecho (D2 = 131,2 e D7 ≈ 146,3) conferem. O resumo usa exemplos próprios.
- O trecho indica "posição mais próxima do rol" quando a posição é fracionária, mas não explica o desempate em x,5 (por exemplo, 3,5). Não incluí regra de desempate; vale conferir como a banca resolve nessa situação.
- Acrescentado fora do trecho: a observação de que a interpolação supõe distribuição uniforme dentro da classe e o teste de consistência (resultado dentro da classe).
