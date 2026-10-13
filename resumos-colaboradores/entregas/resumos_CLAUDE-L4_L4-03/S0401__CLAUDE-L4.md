---
id: S0401
agente: CLAUDE-L4
materia: Estatística
aula: Aula 00 — Apresentação de Dados
trecho: estatistica/a00/s03
paginas_lidas: 27-41
---
# ANALÍTICO

Numa distribuição de frequências com dados agrupados em intervalos, cada coluna e cada medida tem nome e fórmula próprios. Este trecho descreve os elementos dessa tabela: classes, limites, amplitudes, ponto médio, os quatro tipos de frequência e a densidade de frequência.

Para os exemplos, usaremos a distribuição abaixo, com a idade de 60 servidores (n = 60). O símbolo ⊢ indica intervalo **fechado à esquerda e aberto à direita**: o limite inferior pertence à classe, o superior não.

| Idade (Xi) | fi |
| --- | --- |
| 20 ⊢ 30 | 6 |
| 30 ⊢ 40 | 15 |
| 40 ⊢ 50 | 24 |
| 50 ⊢ 60 | 9 |
| 60 ⊢ 70 | 6 |

### Classes e número de classes

**Classes** são os intervalos em que a variável é subdividida; aqui, cinco: a 1ª é 20 ⊢ 30, a 2ª é 30 ⊢ 40, e assim por diante. O número "ideal" de classes (k) em função do total de dados (n) pode ser estimado de duas formas:

- **Fórmula de Sturges:** k = 1 + 3,3 · log n (logaritmo na base 10);
- **Raiz quadrada**, usada quando n ≤ 50: k = √n.

Exemplo: com n = 100, Sturges dá k = 1 + 3,3 · 2 = 7,6, ou seja, em torno de 8 classes. Com n = 36, a segunda fórmula dá k = 6. São apenas referências, e o resultado costuma ser arredondado.

### Limites de classe e amplitude do intervalo

Cada classe tem **limite inferior** (l_inf), o menor valor que pode pertencer a ela, e **limite superior** (l_sup), o maior valor. Os limites são os extremos da classe. Na classe 40 ⊢ 50, l_inf = 40 e l_sup = 50.

A **amplitude do intervalo de classe** (h) mede o tamanho da classe: é quanto separa os limites inferiores (ou os superiores) de duas classes vizinhas.

**h = l_sup − l_inf**

No exemplo, h = 10 em todas as classes. Convém que seja constante, mas isso nem sempre ocorre.

### Amplitude total

A **amplitude total** (AT) é a distância entre o limite superior da última classe e o limite inferior da primeira, isto é, entre o maior e o menor extremo:

**AT = l_máx − l_mín**

Se **todas as classes têm a mesma amplitude**, também vale **AT = h · k**. No exemplo: AT = 70 − 20 = 50, e 10 · 5 = 50.

> ⚠️ **Pegadinha:** AT = h · k só funciona com amplitudes iguais; com classes de tamanhos diferentes, use a diferença dos extremos.

### Ponto médio da classe

O **ponto médio** (PM), também chamado marca ou representante da classe, é a média aritmética dos limites:

**PM = (l_inf + l_sup) / 2**

Pontos médios do exemplo: 25, 35, 45, 55 e 65. Observe que formam uma progressão aritmética de razão 10 = h: **com amplitude constante, a diferença entre pontos médios consecutivos é igual a h**. Como o ponto médio fica no meio da classe, valem também:

- PM = l_inf + h/2 e PM = l_sup − h/2;
- l_inf = PM − h/2 e l_sup = PM + h/2.

Isso resolve questões em que só se conhece o ponto médio e a amplitude: um PM de 45 com h = 10 indica a classe 40 ⊢ 50.

### Frequência absoluta simples (fi)

É o número de observações da classe (ou do valor). A soma de todas as frequências é o total de dados: **Σ fi = n**. No exemplo: 6 + 15 + 24 + 9 + 6 = 60.

### Frequência absoluta acumulada

- **Crescente (fac):** soma das frequências da primeira classe até a classe considerada; indica quantos dados são **menores que o limite superior** da classe. Constrói-se **de cima para baixo**: repete-se a frequência da 1ª classe e soma-se a cada nova frequência. Termina em **n**.
- **Decrescente (fad):** soma das frequências da classe considerada até a última; indica quantos dados são **maiores ou iguais ao limite inferior** da classe. Constrói-se **de baixo para cima**, começando pela frequência da última classe; seu primeiro valor (1ª classe) é **n**.

| Classe | fi | fac | fad |
| --- | --- | --- | --- |
| 20 ⊢ 30 | 6 | 6 | 60 |
| 30 ⊢ 40 | 15 | 21 | 54 |
| 40 ⊢ 50 | 24 | 45 | 39 |
| 50 ⊢ 60 | 9 | 54 | 15 |
| 60 ⊢ 70 | 6 | 60 | 6 |

Leitura: fac da 3ª classe = 45 servidores têm menos de 50 anos; fad da 3ª classe = 39 têm 40 anos ou mais.

### Frequência relativa simples (Fi)

É a proporção de dados da classe: a parte dividida pelo todo.

**Fi = fi / Σ fi = fi / n**

Multiplicando por 100%, tem-se a porcentagem. A soma de todas as Fi é **1 (100%)**. A frequência relativa facilita comparar cada classe com o conjunto.

### Frequência relativa acumulada

- **Crescente (Fac):** soma das Fi da 1ª classe até a considerada; é a proporção de dados abaixo do limite superior. Parte da Fi da 1ª classe e termina em **100%**.
- **Decrescente (Fad):** soma das Fi da classe considerada até a última; é a proporção de dados a partir do limite inferior. Parte da Fi da última classe e chega a 100% na 1ª classe.

| Classe | Fi | Fac | Fad |
| --- | --- | --- | --- |
| 20 ⊢ 30 | 10% | 10% | 100% |
| 30 ⊢ 40 | 25% | 35% | 90% |
| 40 ⊢ 50 | 40% | 75% | 65% |
| 50 ⊢ 60 | 15% | 90% | 25% |
| 60 ⊢ 70 | 10% | 100% | 10% |

Em dados brutos, a frequência acumulada de um valor "inferior a x" é simplesmente a contagem dos que ficam abaixo de x; dividida por n, dá a frequência relativa acumulada. Por exemplo, 11 valores menores que 30 num conjunto de 25 resultam em 11/25 = 0,44.

### Densidade de frequência

Divide-se a frequência da classe, absoluta ou relativa, pela largura dela:

**d = fi / h** (ou Fi / h)

No exemplo, as densidades absolutas são 0,6; 1,5; 2,4; 0,9; e 0,6. A densidade permite comparar classes de larguras diferentes, pois corrige o efeito do tamanho do intervalo; quando h é constante, é proporcional à frequência.

> ⚠️ **Pegadinha:** uma tabela que só lista valores observados (um por dia, por exemplo) **não é** uma distribuição de frequências; falta associar a cada valor a sua frequência.

### Quadro-resumo

| Elemento | Fórmula |
| --- | --- |
| Número de classes | k = 1 + 3,3 · log n ou k = √n (n ≤ 50) |
| Amplitude de classe | h = l_sup − l_inf |
| Amplitude total | AT = l_máx − l_mín = h · k (classes iguais) |
| Ponto médio | PM = (l_inf + l_sup)/2 |
| Frequência relativa | Fi = fi / n |
| Densidade | d = fi / h |

### Para fixar

- Classes são os intervalos; ⊢ inclui o limite inferior e exclui o superior.
- h = l_sup − l_inf; AT = l_máx − l_mín (= h · k só com classes iguais).
- PM = (l_inf + l_sup)/2; com h constante, PMs consecutivos diferem de h.
- Σ fi = n e Σ Fi = 100%.
- fac e Fac crescem de cima para baixo e terminam em n e 100%; fad e Fad vão de baixo para cima e começam em n e 100%.
- fac responde "quantos abaixo do limite superior"; fad, "quantos a partir do limite inferior".
- Densidade = frequência / amplitude.
- Sturges: k = 1 + 3,3 · log n; raiz de n quando n ≤ 50.

# SINTÉTICO

- **Classes e número de classes**: intervalos em que a variável é dividida; k pode ser estimado por Sturges (1 + 3,3 · log n) ou por raiz de n (n ≤ 50).
- **Limites e amplitude (h)**: l_inf e l_sup são os extremos da classe; h = l_sup − l_inf, desejável constante.
- **Amplitude total**: AT = l_máx − l_mín; com classes iguais, AT = h · k.
- **Ponto médio**: PM = (l_inf + l_sup)/2; com h constante, os PMs formam progressão aritmética de razão h; l_inf = PM − h/2 e l_sup = PM + h/2.
- **Frequência absoluta (fi)**: contagem da classe; Σ fi = n.
- **Absoluta acumulada**: fac soma de cima para baixo (dados abaixo do limite superior) e termina em n; fad soma de baixo para cima (dados desde o limite inferior).
- **Relativa (Fi)**: Fi = fi/n; soma 100%; as acumuladas Fac e Fad seguem a mesma lógica e chegam a 100%.
- **Densidade**: d = frequência/h; compara classes de larguras diferentes.

# NOTAS

- As páginas 39 a 41 contêm questões comentadas; foi aproveitada apenas a teoria (a ideia de contar valores menores que x para obter a frequência acumulada, vinda de uma delas, foi mantida com exemplo próprio).
- O material apresenta o log de 50 como 1,7 e, na fórmula de Sturges, soma 1 + 5,61 = 6,61; o resumo informa só a fórmula e usa exemplos próprios. O material também não diz se o k obtido deve ser arredondado; o resumo registra que é uma referência.
- Na frequência acumulada decrescente, o material diz que a sequência "termina em n"; como é calculada de baixo para cima, o valor n aparece na primeira classe, e foi assim que o resumo descreveu.
- O comentário final sobre densidade (comparar classes de larguras diferentes) é o uso usual do conceito e não consta literalmente no trecho.
- Há texto extraído com símbolos separados das fórmulas (subscritos fora de lugar) nas páginas 27 a 29; as fórmulas foram reconstruídas com base nos exemplos numéricos.
