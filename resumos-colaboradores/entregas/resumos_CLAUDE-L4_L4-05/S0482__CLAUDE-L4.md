---
id: S0482
agente: CLAUDE-L4
materia: Estatística
aula: Aula 04 — Medidas de Variabilidade ou Dispersão
trecho: estatistica/a04/s02
paginas_lidas: 17-26
---
# ANALÍTICO

Este trecho define o conceito de desvio e apresenta as três propriedades dos desvios em relação à média aritmética e à mediana. Elas servem de base para o desvio médio e a variância, e caem com frequência em questões de verdadeiro ou falso.

### Conceito de desvio

Em estatística, **desvio** é a distância com sinal entre uma observação e uma medida descritiva do conjunto:

**desvio = observação − medida**

Os dois casos mais cobrados:

- desvio em relação à **média**: di = xi − x̄;
- desvio em relação à **mediana**: di = xi − Md.

A leitura é intuitiva: desvios pequenos indicam dados concentrados em torno da medida (baixa variabilidade); desvios grandes indicam dados espalhados (alta variabilidade). O desvio pode ser **positivo** (observação acima da medida), **negativo** (abaixo) ou **nulo** (igual a ela). O desvio **absoluto** é o seu módulo, |di|, que descarta o sinal.

> 💡 **Exemplo:** nos salários 3, 5, 6 e 10 (em mil reais), a média é 24/4 = 6. Os desvios são −3, −1, 0 e +4. O desvio de quem ganha 6 é nulo, porque coincide com a média. A soma dos desvios absolutos é 3 + 1 + 0 + 4 = 8.

> ⚠️ **Pegadinha:** em questão sobre o desvio de um valor, calcule primeiro a média e depois faça "valor − média". Quem ganha exatamente a média tem desvio zero. E "soma dos valores absolutos dos desvios" não é zero, a menos que todos os dados sejam iguais.

### As três propriedades

| Propriedade | Enunciado | Medida de referência |
| --- | --- | --- |
| 1ª | A soma dos desvios (com sinal) é sempre **nula** | média aritmética |
| 2ª | A soma dos **quadrados** dos desvios é **mínima** | média aritmética |
| 3ª | A soma dos **módulos** dos desvios é **mínima** | mediana |

#### 1ª propriedade: soma dos desvios em relação à média é zero

Os desvios positivos e negativos se compensam exatamente, para qualquer conjunto de números. A média é o "ponto de equilíbrio" dos dados.

> 💡 **Exemplo:** no conjunto {2, 4, 9}, a média é 5 e os desvios são −3, −1 e +4, que somam zero. Isso vale independentemente dos valores escolhidos.

Por isso a soma simples dos desvios não serve para medir dispersão: sempre dá zero. Para medir variabilidade é preciso eliminar o sinal, tomando módulos (desvio médio) ou quadrados (variância).

#### 2ª propriedade: soma dos quadrados é mínima na média

Entre todos os números a que se possa medir os desvios, a soma dos **quadrados** dos desvios Σ(xi − a)² só atinge o menor valor possível quando **a = média aritmética**. Qualquer outro valor de a dá resultado maior.

> 💡 **Exemplo:** em {2, 4, 9}, com a = 5 (a média), a soma dos quadrados é 9 + 1 + 16 = 26. Com a = 4, vale 4 + 0 + 25 = 29, que é maior. Fora da média, a soma sempre cresce.

Fato útil e estável (não consta do trecho): Σ(xi − a)² = Σ(xi − x̄)² + n·(x̄ − a)²; ou seja, a soma dos quadrados em relação a a excede a mínima em n·(x̄ − a)². Por isso a variância é definida em torno da média.

#### 3ª propriedade: soma dos módulos é mínima na mediana

A soma dos **valores absolutos** dos desvios Σ|xi − a| é a menor possível quando **a = mediana**.

- Se o número de elementos é **ímpar**, a mediana é única (o termo central) e é o único ponto de mínimo.
- Se o número de elementos é **par**, a mediana é, por convenção, a média dos dois termos centrais; mas a soma dos módulos é **mínima para qualquer valor entre os dois termos centrais** (inclusive neles). Fora desse intervalo, o resultado é maior.

> 💡 **Exemplo (par):** no conjunto {1, 3, 8, 10}, os termos centrais são 3 e 8, e a mediana convencional é 5,5. A soma dos módulos vale 14 para a = 3, a = 5, a = 5,5 e a = 8 (todos dentro de [3, 8]), mas vale 16 para a = 9, que está fora do intervalo.

> 💡 **Exemplo (ímpar):** em {2, 4, 9}, a mediana é 4 e a soma dos módulos é 2 + 0 + 5 = 7. Em torno da média 5, seria 3 + 1 + 4 = 8, maior.

> ⚠️ **Pegadinha:** a média minimiza a soma dos **quadrados** e zera a soma **com sinal**; a mediana minimiza a soma dos **módulos**. Trocar as medidas nas alternativas é o erro típico da banca. A moda não participa de nenhuma dessas propriedades.

### Como a banca cobra

Questões de julgamento apresentam alternativas como:

- "∑ei² é mínimo se α for a média": **verdadeira** (2ª propriedade);
- "∑|ei| é mínimo se α for a mediana": **verdadeira** (3ª propriedade);
- "∑ei é nulo se α for a moda": **falsa**; a soma dos desvios só é nula em relação à média (e só seria nula na moda se moda e média coincidissem);
- "∑|ei| é nulo se α for a média": **falsa**; a soma dos módulos só é zero quando todos os valores são iguais, isto é, não há dispersão alguma.

### Para fixar
- Desvio = observação − medida; positivo acima, negativo abaixo, nulo quando coincide.
- Desvios pequenos significam dados concentrados; desvios grandes, dados dispersos.
- Medidos a partir da média, os desvios com sinal sempre se anulam mutuamente, seja qual for o conjunto.
- A soma dos quadrados dos desvios é mínima em relação à média aritmética.
- A soma dos módulos dos desvios é mínima em relação à mediana.
- Em conjunto de tamanho par, o mínimo dos módulos ocorre para qualquer valor entre os dois termos centrais.
- Soma dos módulos dos desvios é zero só se todos os valores forem iguais; a moda não tem propriedade desse tipo.

# SINTÉTICO

- **Desvio**: é a diferença entre a observação e uma medida (média ou mediana); o sinal indica se está acima ou abaixo.
- **Desvio e variabilidade**: desvios pequenos mostram dados concentrados; desvios grandes, dados espalhados.
- **Soma dos desvios**: em relação à média, é sempre zero para qualquer conjunto; por isso não mede dispersão por si só.
- **Quem tem o valor igual à média**: seu desvio é nulo; a soma dos módulos dos desvios só é zero se todos os dados forem iguais.
- **Quadrados**: a soma dos quadrados dos desvios é mínima quando se mede em torno da média aritmética; qualquer outro valor dá soma maior.
- **Módulos**: a soma dos valores absolutos dos desvios é mínima em torno da mediana.
- **Conjunto par**: a soma dos módulos é mínima para qualquer valor entre os dois termos centrais; fora desse intervalo, aumenta.
- **Pegadinhas**: a banca troca média por mediana ou moda; só a média zera a soma com sinal e minimiza os quadrados.

# NOTAS

- Pág. 22: o texto escreve "di = xi − x̄" ao calcular desvios em torno de 6 (rótulo digitado errado; o cálculo é xi − 6). Não afeta o resumo.
- Pág. 26 (comentário da questão FCC): a justificativa do item III fala em "soma dos módulos dos desvios" onde o conceito correto é a "soma dos desvios" (com sinal); o gabarito (A) está coerente com as propriedades. Segui a formulação correta.
- Acrescentado fora do trecho (identidade estável): Σ(xi − a)² = Σ(xi − x̄)² + n·(x̄ − a)². Os exemplos numéricos são próprios.
- As tabelas de salários das questões das págs. 17–18 aparecem apenas como coluna de valores na extração; os valores (0,9; 1,2; 1,4; 1,5; 2,0) foram conferidos pelos cálculos das resoluções.
