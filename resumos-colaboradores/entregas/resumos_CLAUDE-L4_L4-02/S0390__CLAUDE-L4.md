---
id: S0390
agente: CLAUDE-L4
materia: Estatística
aula: Aula 02 — Medidas Separatrizes ou Quantis
trecho: estatistica/a02/s02
paginas_lidas: 17-32
---
# ANALÍTICO

A mediana é o valor que divide um conjunto ordenado em duas metades: 50% dos dados ficam abaixo dela e 50% acima. O trecho mostra como estimá-la quando os dados vêm agrupados em classes (por interpolação linear) e apresenta três propriedades da mediana que costumam ser cobradas.

### Mediana quando há frequência acumulada por valor

Quando a tabela lista valores isolados com a frequência acumulada relativa, basta percorrer as linhas de cima para baixo e parar na primeira em que a acumulada ultrapassa 50%: o valor dessa linha é a mediana. Por exemplo, se as acumuladas forem 30%, 40% e 60% para os valores 0, 1 e 2, o patamar de 50% é superado na terceira linha e a mediana é 2.

### Mediana para dados agrupados em classes

Com dados em classes (intervalos), o procedimento é único, **independentemente de n ser par ou ímpar**: não interessa identificar "o termo do meio", e sim a classe onde a metade dos dados é alcançada. A mediana é então estimada dentro dessa classe.

**Passo 1 — frequência acumulada (fac).** Some as frequências simples, de cima para baixo, formando a coluna de acumuladas.

**Passo 2 — posição da mediana.** Calcule Σfi / 2 (metade do total de observações).

**Passo 3 — classe mediana.** É a **primeira classe cuja fac é maior ou igual a Σfi / 2**. Pare a comparação ali.

**Passo 4 — fórmula:**

**Md = linf + [ (Σfi / 2 − facant) / fi ] × h**

| Símbolo | Significado |
| --- | --- |
| linf | limite inferior da classe mediana |
| Σfi / 2 | metade da soma das frequências |
| facant | frequência acumulada da classe imediatamente anterior à mediana |
| fi | frequência simples da classe mediana |
| h | amplitude da classe mediana (limite superior − limite inferior) |

Com frequências relativas (percentuais), a posição é 50% e o total é 100%; a fórmula é a mesma, com facant e fi em percentual.

> 💡 **Exemplo:** pesos de 40 caixas, em kg, distribuídos em cinco classes de amplitude 10 (tabela a seguir). Σfi / 2 = 20. A primeira fac ≥ 20 é 25, logo a classe mediana é 30 ⊢ 40, com linf = 30, facant = 13, fi = 12 e h = 10. Md = 30 + [(20 − 13)/12] × 10 = 30 + 5,83 ≈ 35,83 kg. Metade das caixas pesa menos que 35,83 kg e metade pesa mais.

| Classe (kg) | fi | fac |
| --- | --- | --- |
| 10 ⊢ 20 | 5 | 5 |
| 20 ⊢ 30 | 8 | 13 |
| 30 ⊢ 40 | 12 | 25 |
| 40 ⊢ 50 | 10 | 35 |
| 50 ⊢ 60 | 5 | 40 |

> 💡 **Exemplo com percentuais:** classes 0 ⊢ 10, 10 ⊢ 20, 20 ⊢ 30, 30 ⊢ 40 e 40 ⊢ 50 com 10%, 20%, 30%, 25% e 15%. Acumuladas: 10%, 30%, 60%, 85%, 100%. A classe mediana é 20 ⊢ 30 (60% ≥ 50%). Md = 20 + [(50 − 30)/30] × 10 ≈ 26,67.

### De onde vem a fórmula

A fórmula resulta da **interpolação linear**: supõe-se que, dentro da classe, as observações se distribuem de modo uniforme, de forma que a acumulada cresce em linha reta de facant (no limite inferior) até facant + fi (no limite superior). A mediana é o ponto dessa reta em que a acumulada vale Σfi / 2. Por semelhança de triângulos, (Md − linf) / (Σfi/2 − facant) = h / fi, e isolando Md chega-se à fórmula.

Vale memorizá-la bem: os quartis, decis e percentis seguem exatamente a mesma estrutura, mudando só a posição procurada (Σfi/2 é a posição de 50%).

> ⚠️ **Pegadinha:** a classe mediana é a primeira com fac **maior ou igual** à metade, e facant é a acumulada da classe **anterior** (não a da própria classe). Se a fac de uma classe for exatamente igual a Σfi/2, a fórmula dá Md igual ao limite superior dessa classe. Outra armadilha: os valores mínimo e máximo observados não bastam para dizer em que ponto está a mediana; é preciso a distribuição.

### Propriedades da mediana

**1ª propriedade — soma ou subtração de constante.** Somando (ou subtraindo) uma constante c a todos os valores, a mediana também é somada (ou subtraída) de c.

> 💡 **Exemplo:** em {2, 4, 7, 9, 13} a mediana é 7. Somando 3 a cada elemento, o conjunto passa a {5, 7, 10, 12, 16} e a mediana vira 10.

**2ª propriedade — multiplicação ou divisão por constante.** Multiplicando (ou dividindo) todos os valores por uma constante c, a mediana fica multiplicada (ou dividida) por c.

> 💡 **Exemplo:** multiplicando o mesmo conjunto por 2, obtém-se {4, 8, 14, 18, 26} e a mediana passa de 7 para 14.

**3ª propriedade — desvios absolutos.** A **soma dos desvios absolutos** de um conjunto em relação a um número a, isto é, Σ|xi − a|, é **mínima quando a é a mediana**. (Comparação útil: a média, por sua vez, minimiza a soma dos quadrados dos desvios.)

Com número par de elementos, a mediana não é única: qualquer valor entre os dois termos centrais serve (a convenção é usar a média deles). Então a soma dos desvios absolutos é mínima para **todo valor entre os dois centrais**, e maior para qualquer valor fora desse intervalo.

> 💡 **Exemplo:** no conjunto {2, 4, 7, 9} os termos centrais são 4 e 7, e a mediana por convenção é 5,5. Soma dos desvios absolutos: em relação a 5,5, 3,5 + 1,5 + 1,5 + 3,5 = 10; em relação a 4, 2 + 0 + 3 + 5 = 10; em relação a 7, 5 + 3 + 0 + 2 = 10; em relação a 8 (fora do intervalo), 6 + 4 + 1 + 1 = 12.

### Para fixar

- Em dados agrupados, a classe mediana é a primeira com fac ≥ Σfi/2, valendo para n par ou ímpar.
- Md = linf + [(Σfi/2 − facant) / fi] × h; facant é a acumulada da classe anterior e h é a amplitude.
- A fórmula vem da interpolação linear (distribuição uniforme dentro da classe) e é a base de quartis, decis e percentis.
- Com frequências em percentual, use 50% como posição.
- Somar ou subtrair c de todos os dados altera a mediana do mesmo valor; multiplicar ou dividir por c multiplica ou divide a mediana por c.
- A soma dos desvios absolutos é mínima na mediana (em qualquer ponto entre os dois centrais, se n for par).
- Mínimo e máximo da série não determinam a mediana.

# SINTÉTICO

- **Classe mediana**: é a primeira classe cuja frequência acumulada é maior ou igual a Σfi/2; o critério vale tanto para n par quanto para ímpar.
- **Fórmula**: Md = linf + [(Σfi/2 − facant) / fi] × h, com facant da classe anterior, fi da classe mediana e h a sua amplitude.
- **Origem**: interpolação linear dentro da classe (semelhança de triângulos); a mesma estrutura serve a quartis, decis e percentis.
- **Frequências relativas**: usa-se 50% como posição e 100% como total; a conta é idêntica.
- **Soma ou subtração de constante**: a mediana é deslocada da mesma constante.
- **Multiplicação ou divisão por constante**: a mediana é multiplicada ou dividida pela mesma constante.
- **Desvios absolutos**: Σ|xi − a| é mínima quando a é a mediana; com n par, é mínima em todo o intervalo entre os dois termos centrais.

# NOTAS

- Nenhuma página vazia ou ilegível. As figuras (gráfico da interpolação) foram descartadas, mas o raciocínio que elas ilustram está descrito em texto.
- Os exemplos numéricos são originais; os do material (idades de alunos, estaturas, questões de concursos) não foram reproduzidos.
- A primeira página do trecho começa no fim do tópico anterior (leitura de frequência acumulada por valor); resumi só o que está no intervalo.
- Acrescentei por conta própria dois fatos corretos e usuais: a média minimiza a soma dos quadrados dos desvios (comparação) e que, quando a fac iguala Σfi/2, a fórmula resulta no limite superior da classe.
